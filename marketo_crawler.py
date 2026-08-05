#!/usr/bin/env python3
"""
Adobe Marketo Engage — Knowledge Builder

O que faz:
- Rastreia a documentação do Adobe Marketo Engage no Experience League (pt-br)
  a partir de uma ou mais URLs semente
- Mantém apenas links internos de documentação sob /pt-br/docs/marketo-learn
  e /pt-br/docs/marketo (além das Product Descriptions no helpx)
- Extrai o conteúdo principal do artigo e converte para Markdown
- Salva cada arquivo Markdown direto numa pasta plana (sem subpastas)
- Gera um README.md de índice e um manifest.json para publicação downstream

Instalação sugerida:
    pip install requests beautifulsoup4

Exemplo:
    python marketo_crawler.py \
        --output-dir "./marketo_guides" \
        --max-pages 5000 \
        --delay-s 0.5 \
        --split-h2
"""

from __future__ import annotations

import argparse
import json
import re
import time
from collections import defaultdict, deque
from dataclasses import dataclass
from datetime import datetime, timezone
from html import unescape
from pathlib import Path
from typing import DefaultDict, List, Optional, Tuple
from urllib.parse import urljoin, urlparse, urldefrag

import requests
from bs4 import BeautifulSoup, NavigableString, Tag


DOMAIN = "experienceleague.adobe.com"
ROOT_PREFIXES = ("/pt-br/docs/marketo-learn", "/pt-br/docs/marketo")
ALLOWED_DOMAINS = {
    "experienceleague.adobe.com",
    "helpx.adobe.com",
}
ALLOWED_PREFIXES = [
    "/pt-br/docs/marketo-learn",
    "/pt-br/docs/marketo",
    "/legal/product-descriptions",
]

DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) "
        "Version/17.0 Safari/605.1.15"
    )
}

CATEGORY_MAP = {
    "overview": "overview",
    "visão geral": "overview",
    "visao geral": "overview",
    "landing": "overview",
    "home": "overview",
    "guides": "guides",
    "guide": "guides",
    "guias": "guides",
    "using": "guides",
    "tutorials": "tutorials",
    "tutorial": "tutorials",
    "tutoriais": "tutorials",
    "reference": "reference",
    "referência": "reference",
    "referencia": "reference",
    "api": "reference",
    "apis": "reference",
    "resources": "reference",
    "recursos": "reference",
    "release notes": "release-notes",
    "release-notes": "release-notes",
    "notas de versão": "release-notes",
    "notas de versao": "release-notes",
    "what’s new": "release-notes",
    "what's new": "release-notes",
    "whats-new": "release-notes",
    "novidades": "release-notes",
}

GENERIC_TOPICS = {
    "documentação",
    "documentacao",
    "documentation",
    "marketo",
    "marketo engage",
    "adobe marketo engage",
}

ALLOWED_DEFAULT = ["guides", "tutorials", "reference", "overview"]


@dataclass
class Page:
    url: str
    title: str
    category: str
    topic_path: str
    content_md: str
    breadcrumbs: List[str]
    section_slug: Optional[str] = None


def slugify(text: str) -> str:
    text = unescape(text or "").strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"[\s_-]+", "-", text)
    text = re.sub(r"-{2,}", "-", text)
    return text.strip("-") or "untitled"


def normalize_url(base_url: str, href: str) -> Optional[str]:
    if not href:
        return None

    href = href.strip()
    if href.startswith(("mailto:", "tel:", "javascript:")):
        return None

    abs_url = urljoin(base_url, href)
    abs_url, _frag = urldefrag(abs_url)
    parsed = urlparse(abs_url)

    if parsed.scheme not in {"http", "https"}:
        return None
    if parsed.netloc not in ALLOWED_DOMAINS:
        return None
    if not any(parsed.path.startswith(prefix) for prefix in ALLOWED_PREFIXES):
        return None

    return abs_url


def is_doc_url(url: str) -> bool:
    parsed = urlparse(url)
    if parsed.path.endswith((".pdf", ".zip", ".png", ".jpg", ".jpeg", ".svg")):
        return False
    return any(parsed.path.startswith(prefix) for prefix in ROOT_PREFIXES)


def fetch(url: str, session: requests.Session, delay_s: float = 0.0) -> str:
    if delay_s:
        time.sleep(delay_s)
    resp = session.get(url, headers=DEFAULT_HEADERS, timeout=120)
    resp.raise_for_status()
    return resp.text


def extract_title(soup: BeautifulSoup) -> str:
    h1 = soup.select_one("h1")
    if h1 and h1.get_text(" ", strip=True):
        return h1.get_text(" ", strip=True)

    og = soup.select_one('meta[property="og:title"]')
    if og and og.get("content"):
        return og["content"].strip()

    title = soup.select_one("title")
    if title and title.get_text(" ", strip=True):
        return title.get_text(" ", strip=True)

    return "untitled"


def extract_breadcrumbs(soup: BeautifulSoup) -> List[str]:
    selectors = [
        'nav[aria-label*="breadcrumb"] a',
        'nav[aria-label*="Breadcrumb"] a',
        ".breadcrumb a",
        '[class*="breadcrumb"] a',
    ]
    crumbs: List[str] = []
    for sel in selectors:
        nodes = soup.select(sel)
        if nodes:
            for n in nodes:
                txt = n.get_text(" ", strip=True)
                if txt:
                    crumbs.append(txt)
            break

    deduped = []
    seen = set()
    for c in crumbs:
        key = c.lower()
        if key not in seen:
            deduped.append(c)
            seen.add(key)
    return deduped


def pick_main_container(soup: BeautifulSoup) -> Tag:
    for sel in ["main", "article", '[role="main"]', ".content", ".article", ".markdown"]:
        node = soup.select_one(sel)
        if node:
            return node
    return soup.body or soup


def remove_noise(root: Tag) -> None:
    for tag_name in ["script", "style", "nav", "footer", "header", "aside", "form", "noscript"]:
        for node in root.find_all(tag_name):
            node.decompose()

    for cls in ["cookie", "breadcrumb", "sidebar", "toc", "feedback"]:
        for node in root.find_all(class_=re.compile(cls, re.I)):
            try:
                node.decompose()
            except Exception:
                pass


def inline_text(node: Tag | NavigableString) -> str:
    if isinstance(node, NavigableString):
        return unescape(str(node))

    pieces: List[str] = []
    for child in node.children:
        if isinstance(child, NavigableString):
            pieces.append(unescape(str(child)))
        elif isinstance(child, Tag):
            if child.name == "a":
                text = child.get_text(" ", strip=True)
                href = child.get("href", "").strip()
                pieces.append(f"[{text}]({href})" if href and text else text)
            elif child.name in {"strong", "b"}:
                pieces.append(f"**{child.get_text(' ', strip=True)}**")
            elif child.name in {"em", "i"}:
                pieces.append(f"*{child.get_text(' ', strip=True)}*")
            else:
                pieces.append(child.get_text(" ", strip=True))
    return re.sub(r"\s+", " ", "".join(pieces)).strip()


def node_to_markdown(node: Tag | NavigableString) -> str:
    out: List[str] = []

    def walk(n: Tag | NavigableString):
        if isinstance(n, NavigableString):
            txt = unescape(str(n)).strip()
            if txt:
                out.append(txt)
            return
        if not isinstance(n, Tag):
            return

        name = n.name.lower()

        if name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            level = int(name[1])
            text = n.get_text(" ", strip=True)
            if text:
                out.append(f"{'#' * level} {text}")
                out.append("")
            return

        if name == "p":
            text = inline_text(n)
            if text:
                out.append(text)
                out.append("")
            return

        if name in {"ul", "ol"}:
            for li in n.find_all("li", recursive=False):
                li_text = inline_text(li)
                if li_text:
                    out.append(f"- {li_text}")
            out.append("")
            return

        if name == "pre":
            code = n.get_text("\n", strip=False).rstrip()
            out.append("```")
            out.append(code)
            out.append("```")
            out.append("")
            return

        if name == "table":
            rows = []
            for tr in n.find_all("tr"):
                cells = [inline_text(td) for td in tr.find_all(["th", "td"])]
                if any(cells):
                    rows.append(cells)
            if rows:
                header = rows[0]
                out.append("| " + " | ".join(header) + " |")
                out.append("| " + " | ".join(["---"] * len(header)) + " |")
                for row in rows[1:]:
                    padded = row + [""] * (len(header) - len(row))
                    out.append("| " + " | ".join(padded) + " |")
                out.append("")
            return

        for child in n.children:
            walk(child)

    walk(node)
    md = "\n".join(out)
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    return md + "\n"


def split_by_h2(main: Tag) -> List[Tuple[str, str]]:
    children = list(main.children)
    sections: List[Tuple[str, str]] = []

    current_title = "main"
    buffer: List[str] = []

    def flush():
        nonlocal buffer, current_title
        html = "".join(buffer).strip()
        if html:
            sections.append((current_title, html))
        buffer = []

    for child in children:
        if isinstance(child, NavigableString):
            if str(child).strip():
                buffer.append(str(child))
            continue

        if not isinstance(child, Tag):
            continue

        if child.name == "h2":
            flush()
            current_title = child.get_text(" ", strip=True) or "section"
            buffer.append(str(child))
        else:
            buffer.append(str(child))

    flush()
    return sections


def infer_category_from_url_or_breadcrumbs(url: str, breadcrumbs: List[str]) -> str:
    for crumb in breadcrumbs:
        k = slugify(crumb)
        if k in CATEGORY_MAP:
            return CATEGORY_MAP[k]

    path = urlparse(url).path.lower()
    if "tutorial" in path or "marketo-learn" in path:
        return "tutorials"
    if "release" in path or "version" in path or "notes" in path or "novidades" in path:
        return "release-notes"
    if "guide" in path or "/using/" in path:
        return "guides"
    if "reference" in path or "/api" in path:
        return "reference"
    return "overview" if path.endswith(("/home", "/overview")) else "other"


def infer_topic_path(url: str, breadcrumbs: List[str], title: str) -> str:
    crumbs = [slugify(c) for c in breadcrumbs if slugify(c) not in GENERIC_TOPICS]
    if len(crumbs) >= 2:
        return "/".join(crumbs[:4])

    parsed = urlparse(url)
    parts = [p for p in parsed.path.split("/") if p]
    anchor = None
    for candidate in ("marketo-learn", "marketo"):
        if candidate in parts:
            anchor = candidate
            break
    if anchor:
        idx = parts.index(anchor)
        tail = parts[idx + 1:]
    else:
        tail = parts

    tail = [
        slugify(p)
        for p in tail
        if p and p not in {"pt-br", "docs", "marketo-learn", "marketo"}
    ]
    if tail:
        return "/".join(tail[:3])

    return slugify(title)


def extract_page(url: str, html: str, split_h2_enabled: bool = True) -> List[Page]:
    soup = BeautifulSoup(html, "html.parser")
    title = extract_title(soup)
    breadcrumbs = extract_breadcrumbs(soup)
    category = infer_category_from_url_or_breadcrumbs(url, breadcrumbs)

    main = pick_main_container(soup)
    remove_noise(main)

    pages: List[Page] = []

    if split_h2_enabled:
        sections = split_by_h2(main)
        if len(sections) > 1:
            for section_title, section_html in sections:
                section_soup = BeautifulSoup(section_html, "html.parser")
                md = node_to_markdown(section_soup)
                pages.append(
                    Page(
                        url=url,
                        title=title,
                        category=category,
                        topic_path=infer_topic_path(url, breadcrumbs, title),
                        content_md=md,
                        breadcrumbs=breadcrumbs,
                        section_slug=slugify(section_title),
                    )
                )
            return pages

    md = node_to_markdown(main)
    pages.append(
        Page(
            url=url,
            title=title,
            category=category,
            topic_path=infer_topic_path(url, breadcrumbs, title),
            content_md=md,
            breadcrumbs=breadcrumbs,
            section_slug=None,
        )
    )
    return pages


def friendly_filename(title: str, section_slug: Optional[str] = None) -> str:
    base = slugify(section_slug or title)
    if base == "untitled":
        base = "page"
    return base


def save_page(page: Page, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)

    base = friendly_filename(page.title, page.section_slug)
    target = output_dir / f"{base}.md"

    n = 2
    while target.exists():
        target = output_dir / f"{base}-{n}.md"
        n += 1

    front_matter = [
        "---",
        f'title: "{page.title}"',
        f'url: "{page.url}"',
        f'category: "{page.category}"',
        f'topic: "{page.topic_path}"',
        f'created_at: "{datetime.now(timezone.utc).isoformat()}"',
        "---",
        "",
    ]

    body = ""
    if page.breadcrumbs:
        body += "Breadcrumbs: " + " > ".join(page.breadcrumbs) + "\n\n"
    body += page.content_md.strip() + "\n"

    target.write_text("\n".join(front_matter) + body, encoding="utf-8")
    return target


def extract_links_with_context(soup: BeautifulSoup, base_url: str) -> List[Tuple[str, str]]:
    result: List[Tuple[str, str]] = []
    current_section = ""

    for node in soup.find_all(["h2", "h3", "a"]):
        if node.name in {"h2", "h3"}:
            current_section = node.get_text(" ", strip=True)
            continue

        if node.name == "a":
            href = node.get("href")
            url = normalize_url(base_url, href or "")
            if url and is_doc_url(url):
                result.append((url, current_section))

    deduped = []
    seen = set()
    for url, ctx in result:
        if url not in seen:
            deduped.append((url, ctx))
            seen.add(url)
    return deduped


def category_from_section_context(section_context: str) -> Optional[str]:
    key = slugify(section_context)
    return CATEGORY_MAP.get(key)


def build_readme(output_dir: Path, manifest: List[dict]) -> None:
    grouped: DefaultDict[str, DefaultDict[str, List[str]]] = defaultdict(lambda: defaultdict(list))

    for item in manifest:
        if item.get("status") != "saved":
            continue
        category = item["category"]
        topic = item["topic_path"]
        rel = item["saved_path"]
        grouped[category][topic].append(rel)

    lines: List[str] = []
    lines.append("# Marketo Engage Knowledge Index")
    lines.append("")
    lines.append("Gerado a partir da documentação do Adobe Marketo Engage (Experience League).")
    lines.append("")

    for category in ["overview", "guides", "tutorials", "reference", "release-notes", "other"]:
        if category not in grouped:
            continue
        lines.append(f"## {category}")
        lines.append("")
        for topic in sorted(grouped[category].keys()):
            lines.append(f"- {topic}")
            for rel in sorted(grouped[category][topic]):
                rel_path = Path(rel).relative_to(output_dir)
                lines.append(f"  - {rel_path.as_posix()}")
        lines.append("")

    (output_dir / "README.md").write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def crawl(
    start_urls: List[str],
    output_dir: Path,
    max_pages: int = 5000,
    split_h2_enabled: bool = True,
    delay_s: float = 0.0,
    only_categories: Optional[List[str]] = None,
) -> None:
    session = requests.Session()
    queue = deque([(url, None) for url in start_urls])
    visited = set()
    manifest: List[dict] = []
    saved_count = 0

    allowed = set(only_categories) if only_categories else None

    while queue and saved_count < max_pages:
        url, forced_category = queue.popleft()
        if url in visited:
            continue
        visited.add(url)

        try:
            html = fetch(url, session, delay_s=delay_s)
        except Exception as e:
            manifest.append({"url": url, "status": "error", "error": str(e)})
            continue

        pages = extract_page(url, html, split_h2_enabled=split_h2_enabled)

        for page in pages:
            if forced_category:
                page.category = forced_category

            if allowed is not None and page.category not in allowed:
                continue

            saved_path = save_page(page, output_dir)
            manifest.append(
                {
                    "url": page.url,
                    "title": page.title,
                    "category": page.category,
                    "topic_path": page.topic_path,
                    "section_slug": page.section_slug,
                    "saved_path": str(saved_path),
                    "status": "saved",
                }
            )
            saved_count += 1
            if saved_count >= max_pages:
                break

        soup = BeautifulSoup(html, "html.parser")
        for link_url, section_ctx in extract_links_with_context(soup, url):
            if link_url in visited:
                continue
            category = category_from_section_context(section_ctx)
            queue.append((link_url, category))

    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    build_readme(output_dir, manifest)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Crawler do Adobe Marketo Engage para Markdown em pasta plana"
    )
    parser.add_argument(
        "--start-urls",
        nargs="*",
        default=[
            "https://experienceleague.adobe.com/pt-br/docs/marketo-learn/tutorials/overview",
            "https://experienceleague.adobe.com/pt-br/docs/marketo/using/home",
            # Product Descriptions (HelpX)
            "https://helpx.adobe.com/legal/product-descriptions/marketo-engage.html",
        ],
        help="URLs iniciais",
    )
    parser.add_argument(
        "--output-dir",
        default="./marketo_guides",
        help="Diretório de saída",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=5000,
        help="Máximo de páginas/arquivos Markdown",
    )
    parser.add_argument(
        "--split-h2",
        action="store_true",
        help="Divide páginas longas em arquivos por H2",
    )
    parser.add_argument(
        "--delay-s",
        type=float,
        default=0.0,
        help="Delay entre requisições",
    )
    parser.add_argument(
        "--only",
        nargs="*",
        default=ALLOWED_DEFAULT,
        help="Categorias a manter no recorte inicial. Ex: guides tutorials reference overview",
    )
    parser.add_argument(
        "--include-all",
        action="store_true",
        help="Inclui overview, guides, tutorials, reference, release-notes e other",
    )

    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    only_categories = None if args.include_all else args.only

    crawl(
        start_urls=args.start_urls,
        output_dir=output_dir,
        max_pages=args.max_pages,
        split_h2_enabled=args.split_h2,
        delay_s=args.delay_s,
        only_categories=only_categories,
    )


if __name__ == "__main__":
    main()
