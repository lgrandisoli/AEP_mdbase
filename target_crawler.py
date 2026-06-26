#!/usr/bin/env python3
"""
Adobe Target crawler -> one Markdown file per page.

What it does:
- Starts from the Target URLs you pass in (or the built-in defaults)
- Follows internal subpages inside Experience League Target / Target Dev / Target Learn
- Extracts the main article content and converts it to Markdown
- Writes every page directly into a single output folder (no subdirectories)
- Creates manifest.json and README.md for quick browsing

Install:
    pip install requests beautifulsoup4

Run:
    python3 target_crawler.py --output-dir ./target_guides
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import time
from collections import deque
from dataclasses import dataclass
from datetime import datetime, timezone
from html import unescape
from pathlib import Path
from typing import List, Optional, Tuple
from urllib.parse import urljoin, urlparse, urldefrag

import requests
from bs4 import BeautifulSoup, NavigableString, Tag


ALLOWED_DOMAINS = {
    "experienceleague.adobe.com",
    "helpx.adobe.com",
}
DEFAULT_OUTPUT_DIR = "./target_guides"
DEFAULT_MAX_PAGES = 2000

START_URLS = [
    "https://experienceleague.adobe.com/pt-br/browse/target",
    "https://experienceleague.adobe.com/pt-br/docs/target/using/target-home",
    "https://experienceleague.adobe.com/pt-br/docs/target/using/release-notes/release-notes",
    "https://experienceleague.adobe.com/pt-br/docs/target/using/introduction/intro",
    "https://experienceleague.adobe.com/pt-br/docs/target/using/introduction/understand-the-target-ui",
    "https://experienceleague.adobe.com/pt-br/docs/target/using/introduction/assistant-ai/ai-assistant",
    "https://experienceleague.adobe.com/pt-br/docs/target-learn/tutorials/overview",
    "https://experienceleague.adobe.com/pt-br/docs/target-dev/developer/mobile-apps/overview",
    "https://experienceleague.adobe.com/pt-br/docs/target/using/activities/activities",
    "https://experienceleague.adobe.com/pt-br/docs/target/using/audiences/target",
    "https://experienceleague.adobe.com/pt-br/docs/target/using/experiences/experiences",
    "https://experienceleague.adobe.com/pt-br/docs/target-dev/developer/overview",
    "https://experienceleague.adobe.com/pt-br/docs/target/using/administer/administrating-target",
    "https://experienceleague.adobe.com/pt-br/docs/target/using/reports/reports",
    # Product Description
    "https://helpx.adobe.com/legal/product-descriptions/adobe-target.html",
]

ALLOWED_PREFIXES = (
    "/pt-br/browse/target",
    "/pt-br/docs/target",
    "/pt-br/docs/target-dev",
    "/pt-br/docs/target-learn",
      # Product Description
    "/legal/product-descriptions",
)

DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
    )
}


@dataclass
class Page:
    url: str
    title: str
    content_md: str
    breadcrumbs: List[str]
    section_title: Optional[str] = None


# -----------------------------------------------------------------------------
# URL helpers
# -----------------------------------------------------------------------------

def slugify(text: str) -> str:
    text = unescape(text or "").strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"[\s_-]+", "-", text)
    text = re.sub(r"-{2,}", "-", text)
    return text.strip("-") or "untitled"


def is_allowed_target_url(url: str) -> bool:
    parsed = urlparse(url)
    if parsed.netloc not in ALLOWED_DOMAINS:
     return False
    if parsed.scheme not in {"http", "https"}:
        return False
    if parsed.path.endswith((".pdf", ".zip", ".png", ".jpg", ".jpeg", ".svg", ".gif", ".mp4")):
        return False
    return any(parsed.path.startswith(prefix) for prefix in ALLOWED_PREFIXES)


def normalize_url(base_url: str, href: str) -> Optional[str]:
    if not href:
        return None
    href = href.strip()
    if href.startswith(("mailto:", "tel:", "javascript:")):
        return None

    abs_url = urljoin(base_url, href)
    abs_url, _ = urldefrag(abs_url)
    if is_allowed_target_url(abs_url):
        return abs_url
    return None


# -----------------------------------------------------------------------------
# Fetch and HTML parsing
# -----------------------------------------------------------------------------

def fetch_html(url: str, session: requests.Session, delay_s: float = 0.0) -> str:
    if delay_s:
        time.sleep(delay_s)
    resp = session.get(url, headers=DEFAULT_HEADERS, timeout=120)
    resp.raise_for_status()
    return resp.text


def extract_title(soup: BeautifulSoup) -> str:
    h1 = soup.select_one("h1")
    if h1:
        txt = h1.get_text(" ", strip=True)
        if txt:
            return txt

    og = soup.select_one('meta[property="og:title"]')
    if og and og.get("content"):
        return og["content"].strip()

    title = soup.select_one("title")
    if title:
        txt = title.get_text(" ", strip=True)
        if txt:
            return txt

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
            for node in nodes:
                txt = node.get_text(" ", strip=True)
                if txt:
                    crumbs.append(txt)
            break

    deduped: List[str] = []
    seen = set()
    for crumb in crumbs:
        key = crumb.lower()
        if key not in seen:
            deduped.append(crumb)
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

    def walk(n: Tag | NavigableString) -> None:
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
    sections: List[Tuple[str, str]] = []
    current_title = "main"
    buffer: List[str] = []

    def flush() -> None:
        nonlocal buffer, current_title
        html = "".join(buffer).strip()
        if html:
            sections.append((current_title, html))
        buffer = []

    for child in list(main.children):
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


# -----------------------------------------------------------------------------
# Page extraction and saving
# -----------------------------------------------------------------------------

def extract_page(url: str, html: str, split_h2_enabled: bool = False) -> List[Page]:
    soup = BeautifulSoup(html, "html.parser")
    title = extract_title(soup)
    breadcrumbs = extract_breadcrumbs(soup)

    main = pick_main_container(soup)
    remove_noise(main)

    pages: List[Page] = []

    if split_h2_enabled:
        sections = split_by_h2(main)
        if len(sections) > 1:
            for section_title, section_html in sections:
                section_soup = BeautifulSoup(section_html, "html.parser")
                pages.append(
                    Page(
                        url=url,
                        title=title,
                        content_md=node_to_markdown(section_soup),
                        breadcrumbs=breadcrumbs,
                        section_title=section_title,
                    )
                )
            return pages

    pages.append(
        Page(
            url=url,
            title=title,
            content_md=node_to_markdown(main),
            breadcrumbs=breadcrumbs,
            section_title=None,
        )
    )
    return pages


def output_filename(page: Page, index: int = 1) -> str:
    parsed = urlparse(page.url)
    base = slugify(page.section_title or page.title)
    url_bits = slugify(parsed.path.replace("/", "-"))
    digest = hashlib.sha1(page.url.encode("utf-8")).hexdigest()[:8]

    if page.section_title:
        candidate = f"{base}-{digest}"
    else:
        candidate = f"{base}-{digest}"

    candidate = re.sub(r"-+", "-", candidate).strip("-") or f"page-{digest}"
    if index > 1:
        candidate = f"{candidate}-{index}"
    return f"{candidate}.md"


def save_page(page: Page, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)

    target = output_dir / output_filename(page)
    n = 2
    while target.exists():
        target = output_dir / output_filename(page, index=n)
        n += 1

    front_matter = [
        "---",
        f'title: "{page.title}"',
        f'url: "{page.url}"',
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


# -----------------------------------------------------------------------------
# Crawling and indexing
# -----------------------------------------------------------------------------

def extract_links(soup: BeautifulSoup, base_url: str) -> List[str]:
    links: List[str] = []
    for node in soup.find_all("a"):
        href = node.get("href")
        url = normalize_url(base_url, href or "")
        if url:
            links.append(url)

    deduped: List[str] = []
    seen = set()
    for url in links:
        if url not in seen:
            deduped.append(url)
            seen.add(url)
    return deduped


def build_readme(output_dir: Path, manifest: List[dict]) -> None:
    lines: List[str] = []
    lines.append("# Target Guides")
    lines.append("")
    lines.append("Generated from Adobe Experience League Target documentation.")
    lines.append("")

    for item in manifest:
        if item.get("status") != "saved":
            continue
        rel = Path(item["saved_path"]).name
        title = item.get("title", "untitled")
        lines.append(f"- [{title}]({rel})")

    (output_dir / "README.md").write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def crawl(
    start_urls: List[str],
    output_dir: Path,
    max_pages: int = DEFAULT_MAX_PAGES,
    split_h2_enabled: bool = False,
    delay_s: float = 0.0,
) -> None:
    session = requests.Session()
    queue = deque(start_urls)
    queued = set(start_urls)
    visited = set()
    manifest: List[dict] = []
    saved_count = 0

    while queue and saved_count < max_pages:
        url = queue.popleft()
        queued.discard(url)
        if url in visited:
            continue
        visited.add(url)

        try:
            html = fetch_html(url, session, delay_s=delay_s)
        except Exception as exc:
            manifest.append({"url": url, "status": "error", "error": str(exc)})
            continue

        pages = extract_page(url, html, split_h2_enabled=split_h2_enabled)
        for page in pages:
            saved_path = save_page(page, output_dir)
            manifest.append(
                {
                    "url": page.url,
                    "title": page.title,
                    "saved_path": str(saved_path),
                    "status": "saved",
                    "section_title": page.section_title,
                }
            )
            saved_count += 1
            if saved_count >= max_pages:
                break

        soup = BeautifulSoup(html, "html.parser")
        main = pick_main_container(soup)
        remove_noise(main)
        for link_url in extract_links(main, url):
            if link_url in visited or link_url in queued:
                continue
            queue.append(link_url)
            queued.add(link_url)

    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    build_readme(output_dir, manifest)


# -----------------------------------------------------------------------------
# CLI
# -----------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Crawler de Adobe Target para Markdown plano"
    )
    parser.add_argument(
        "--start-urls",
        nargs="*",
        default=START_URLS,
        help="URLs iniciais do crawl",
    )
    parser.add_argument(
        "--output-dir",
        default=DEFAULT_OUTPUT_DIR,
        help="Diretório de saída",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=DEFAULT_MAX_PAGES,
        help="Limite de páginas Markdown salvas",
    )
    parser.add_argument(
        "--delay-s",
        type=float,
        default=0.0,
        help="Delay entre requisições em segundos",
    )
    parser.add_argument(
        "--split-h2",
        action="store_true",
        help="Divide páginas grandes por H2",
    )

    args = parser.parse_args()

    unique_start_urls = list(dict.fromkeys(args.start_urls or START_URLS))
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    crawl(
        start_urls=unique_start_urls,
        output_dir=output_dir,
        max_pages=args.max_pages,
        split_h2_enabled=args.split_h2,
        delay_s=args.delay_s,
    )


if __name__ == "__main__":
    main()
