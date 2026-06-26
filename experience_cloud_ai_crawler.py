#!/usr/bin/env python3
"""
Adobe Experience Cloud AI crawler -> one Markdown file per page.

What it does:
- Starts from the Experience Cloud AI URLs you pass in (or the built-in defaults)
- Follows internal subpages inside Experience League Experience Cloud AI docs
- Extracts the main article content and converts it to Markdown
- Writes every page directly into a single output folder called "agents" (no subdirectories)
- Creates manifest.json and README.md for quick browsing

Install:
    pip install requests beautifulsoup4

Run:
    python3 experience_cloud_ai_crawler.py --output-dir ./agents
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
from typing import List, Optional, Sequence, Tuple
from urllib.parse import urljoin, urlparse, urldefrag

import requests
from bs4 import BeautifulSoup, NavigableString, Tag

DOMAIN = "experienceleague.adobe.com"
ROOT_PREFIX = "/en/docs/experience-cloud-ai"

HELPX_DOMAIN = "helpx.adobe.com"
HELPX_PREFIX = "/legal/product-descriptions"

DEFAULT_OUTPUT_DIR = "./agents"
DEFAULT_MAX_PAGES = 2000

DEFAULT_START_URLS = [
    "https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/agents/agent-orchestrator",
    "https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/agents/audience",
    "https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/agents/cja-data-insights-agent",
    "https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/agents/agent-experiment",
    "https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/agents/field-discovery-agent",
    "https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/agents/ajo-agent",
    "https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/agents/product-support",
    "https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/agents/ama-ms",
    "https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/mcp/rtcdp-mcp",
    "https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/ai-assistant/prompt-library",
    "https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/ai-assistant/legal-disclaimer",
    "https://helpx.adobe.com/legal/product-descriptions/adobe-experience-platform-agents.html",
]

DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) "
        "Version/17.0 Safari/605.1.15"
    )
}


@dataclass
class Page:
    url: str
    title: str
    content_md: str
    breadcrumbs: List[str]
    section_title: Optional[str] = None


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
    if href.startswith(("mailto:", "tel:", "javascript:", "#")):
        return None

    abs_url = urljoin(base_url, href)
    abs_url, _frag = urldefrag(abs_url)
    parsed = urlparse(abs_url)

    if parsed.scheme not in {"http", "https"}:
        return None
    if parsed.netloc == HELPX_DOMAIN:
        if not parsed.path.startswith(HELPX_PREFIX):
            return None
        return abs_url
    if parsed.netloc != DOMAIN:
        return None
    if not parsed.path.startswith(ROOT_PREFIX):
        return None
    if parsed.path.endswith((".pdf", ".zip", ".png", ".jpg", ".jpeg", ".svg", ".gif", ".webp", ".mp4")):
        return None

    return abs_url


def fetch(url: str, session: requests.Session, delay_s: float = 0.0) -> str:
    if delay_s:
        time.sleep(delay_s)
    resp = session.get(url, headers=DEFAULT_HEADERS, timeout=45)
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

    deduped: List[str] = []
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
    for tag_name in ["script", "style", "noscript", "header", "footer", "aside", "form"]:
        for node in root.find_all(tag_name):
            node.decompose()

    for cls in ["cookie", "breadcrumb", "sidebar", "toc", "feedback", "promo", "modal"]:
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


def extract_page(url: str, html: str) -> Page:
    soup = BeautifulSoup(html, "html.parser")
    title = extract_title(soup)
    breadcrumbs = extract_breadcrumbs(soup)
    main = pick_main_container(soup)
    remove_noise(main)
    return Page(
        url=url,
        title=title,
        content_md=node_to_markdown(main),
        breadcrumbs=breadcrumbs,
    )


def filename_for_page(page: Page, used: set[str]) -> str:
    parsed = urlparse(page.url)
    base = slugify(page.title)
    if base == "untitled":
        base = slugify(Path(parsed.path).name or "page")

    digest = hashlib.sha1(page.url.encode("utf-8")).hexdigest()[:8]
    candidate = f"{base}-{digest}.md"
    if candidate not in used:
        used.add(candidate)
        return candidate

    n = 2
    while True:
        candidate = f"{base}-{digest}-{n}.md"
        if candidate not in used:
            used.add(candidate)
            return candidate
        n += 1


def save_page(page: Page, output_dir: Path, used: set[str]) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / filename_for_page(page, used)

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
    lines.append("# Experience Cloud AI Agents")
    lines.append("")
    lines.append("Generated from Adobe Experience League Experience Cloud AI documentation.")
    lines.append("")
    lines.append("## Files")
    lines.append("")

    for item in manifest:
        if item.get("status") != "saved":
            continue
        rel = Path(item["saved_path"]).name
        title = item.get("title", "untitled")
        lines.append(f"- [{title}]({rel})")

    (output_dir / "README.md").write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def crawl(
    start_urls: Sequence[str],
    output_dir: Path,
    max_pages: int = DEFAULT_MAX_PAGES,
    delay_s: float = 0.0,
) -> None:
    session = requests.Session()
    queue = deque()
    for url in start_urls:
        if url not in queue:
            queue.append(url)

    queued = set(queue)
    visited = set()
    manifest: List[dict] = []
    used_filenames: set[str] = set()
    saved_count = 0

    while queue and saved_count < max_pages:
        url = queue.popleft()
        queued.discard(url)
        if url in visited:
            continue
        visited.add(url)

        try:
            html = fetch(url, session, delay_s=delay_s)
        except Exception as exc:
            manifest.append({"url": url, "status": "error", "error": str(exc)})
            continue

        page = extract_page(url, html)
        saved_path = save_page(page, output_dir, used_filenames)
        manifest.append(
            {
                "url": page.url,
                "title": page.title,
                "saved_path": str(saved_path),
                "status": "saved",
            }
        )
        saved_count += 1

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


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Crawler de Adobe Experience Cloud AI para Markdown plano"
    )
    parser.add_argument(
        "--start-urls",
        nargs="*",
        default=DEFAULT_START_URLS,
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

    args = parser.parse_args()
    unique_start_urls = list(dict.fromkeys(args.start_urls or DEFAULT_START_URLS))
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    crawl(
        start_urls=unique_start_urls,
        output_dir=output_dir,
        max_pages=args.max_pages,
        delay_s=args.delay_s,
    )


if __name__ == "__main__":
    main()
