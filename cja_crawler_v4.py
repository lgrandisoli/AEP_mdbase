#!/usr/bin/env python3
"""
Customer Journey Analytics tree crawler for Experience League.

This crawler is designed to be more robust than a simple "follow <a> tags"
approach. It:

- starts from the CJA hub pages
- follows all internal links found anywhere in the HTML
- also extracts URLs from raw HTML using regex to catch nav JSON / embedded
  links that are not exposed as normal anchors
- keeps pages under a configurable set of CJA-related prefixes
- saves each page as Markdown in a flat output directory
- writes manifest.json and README.md

Install:
    pip install requests beautifulsoup4

Example:
    python cja_tree_crawler.py --output-dir ./CJA --max-pages 2000
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
from typing import DefaultDict, Iterable, List, Optional, Sequence, Set, Tuple
from urllib.parse import urljoin, urlparse, urldefrag

import requests
from bs4 import BeautifulSoup, NavigableString, Tag

ALLOWED_DOMAINS = {
    "experienceleague.adobe.com",
    "helpx.adobe.com",
}
DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) "
        "Version/17.0 Safari/605.1.15"
    )
}

DEFAULT_START_URLS = [
    "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-landing",
    "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-overview/cja-b2c-overview/cja-overview",
    "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-overview/cja-b2c-overview/cja-getting-started",
    "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-data-mirror/data-mirror",

    # Product Description
    "https://helpx.adobe.com/legal/product-descriptions/customer-journey-analytics.html",
]

DEFAULT_ALLOWED_PREFIXES = [
    "/en/docs/analytics-platform/using",
    "/en/docs/customer-journey-analytics",
    "/en/docs/customer-journey-analytics-learn",
    "/en/docs/analytics-learn",
    "/en/browse/customer-journey-analytics",

    # Product Descriptions
    "/legal/product-descriptions",
]

CATEGORY_HINTS = {
    "landing": "overview",
    "overview": "overview",
    "home": "overview",
    "getting-started": "guides",
    "quick-start": "guides",
    "guide": "guides",
    "tutorial": "tutorials",
    "tutorials": "tutorials",
    "reference": "reference",
    "api": "reference",
    "release-notes": "release-notes",
    "release notes": "release-notes",
}


def slugify(text: str) -> str:
    text = unescape(text or "").strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"[\s_-]+", "-", text)
    text = re.sub(r"-{2,}", "-", text)
    return text.strip("-") or "untitled"


@dataclass
class Page:
    url: str
    title: str
    content_md: str
    breadcrumbs: List[str]
    category: str
    topic_path: str
    section_slug: Optional[str] = None


def normalize_url(base_url: str, href: str, allowed_prefixes: Sequence[str]) -> Optional[str]:
    if not href:
        return None

    href = href.strip()
    if href.startswith(("mailto:", "tel:", "javascript:", "#")):
        return None

    abs_url = urljoin(base_url, href)
    abs_url, _ = urldefrag(abs_url)
    parsed = urlparse(abs_url)

    if parsed.scheme not in {"http", "https"}:
        return None
    if parsed.netloc not in ALLOWED_DOMAINS:
        return None

    if not any(parsed.path.startswith(prefix) for prefix in allowed_prefixes):
        return None

    if parsed.path.endswith((".pdf", ".zip", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp")):
        return None

    return abs_url


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

    deduped: List[str] = []
    seen: Set[str] = set()
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


def infer_category(url: str, breadcrumbs: Sequence[str], title: str) -> str:
    for crumb in breadcrumbs:
        key = slugify(crumb)
        if key in CATEGORY_HINTS:
            return CATEGORY_HINTS[key]

    path = urlparse(url).path.lower()
    title_key = slugify(title)
    for key, category in CATEGORY_HINTS.items():
        if key in path or key in title_key:
            return category

    if "overview" in path or path.endswith("/home") or "landing" in path:
        return "overview"
    if "guide" in path or "getting-started" in path:
        return "guides"
    if "tutorial" in path:
        return "tutorials"
    if "api" in path or "reference" in path:
        return "reference"
    return "other"


GENERIC_TOPICS = {
    "documentation",
    "customer-journey-analytics",
    "customer-journey-analytics-guide",
    "experience-league",
}


def infer_topic_path(url: str, breadcrumbs: Sequence[str], title: str) -> str:
    crumbs = [slugify(c) for c in breadcrumbs if slugify(c) not in GENERIC_TOPICS]
    if len(crumbs) >= 2:
        return "/".join(crumbs[:4])

    parsed = urlparse(url)
    parts = [p for p in parsed.path.split("/") if p]
    tail = [p for p in parts if p not in {"en", "docs"}]
    if tail:
        return "/".join([slugify(x) for x in tail[:4]])
    return slugify(title)


def extract_urls_from_html(html: str, base_url: str, allowed_prefixes: Sequence[str]) -> List[str]:
    urls: Set[str] = set()

    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all(True):
        for attr in ("href", "data-href", "data-url", "data-path", "src"):
            val = tag.get(attr)
            if not val or not isinstance(val, str):
                continue
            url = normalize_url(base_url, val, allowed_prefixes)
            if url:
                urls.add(url)

    # Regex fallback for URLs embedded in scripts / JSON / raw markup.
    patterns = [
        r'https?://[^"\'\s<>]+',
        r'(?<![\w-])/(?:en/docs|en/browse)/[^"\'\s<>]+',
    ]
    for pattern in patterns:
        for match in re.findall(pattern, html):
            url = normalize_url(base_url, match, allowed_prefixes)
            if url:
                urls.add(url)

    return sorted(urls)


def extract_page(url: str, html: str) -> List[Page]:
    soup = BeautifulSoup(html, "html.parser")
    title = extract_title(soup)
    breadcrumbs = extract_breadcrumbs(soup)
    category = infer_category(url, breadcrumbs, title)

    main = pick_main_container(soup)
    remove_noise(main)

    md = node_to_markdown(main)
    return [
        Page(
            url=url,
            title=title,
            content_md=md,
            breadcrumbs=breadcrumbs,
            category=category,
            topic_path=infer_topic_path(url, breadcrumbs, title),
            section_slug=None,
        )
    ]


def friendly_filename(title: str, section_slug: Optional[str] = None) -> str:
    base = slugify(section_slug or title)
    return base if base != "untitled" else "page"


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


def build_readme(output_dir: Path, manifest: List[dict]) -> None:
    grouped: DefaultDict[str, DefaultDict[str, List[str]]] = defaultdict(lambda: defaultdict(list))

    for item in manifest:
        if item.get("status") != "saved":
            continue
        grouped[item["category"]][item["topic_path"]].append(item["saved_path"])

    lines: List[str] = []
    lines.append("# Customer Journey Analytics Knowledge Index")
    lines.append("")
    lines.append("Generated from Experience League Customer Journey Analytics documentation.")
    lines.append("")

    for category in ["overview", "guides", "tutorials", "reference", "release-notes", "other"]:
        if category not in grouped:
            continue
        lines.append(f"## {category}")
        lines.append("")
        for topic in sorted(grouped[category].keys()):
            lines.append(f"- {topic}")
            for rel in sorted(grouped[category][topic]):
                lines.append(f"  - {Path(rel).name}")
        lines.append("")

    (output_dir / "README.md").write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def crawl(
    start_urls: Sequence[str],
    output_dir: Path,
    allowed_prefixes: Sequence[str],
    max_pages: int = 2000,
    delay_s: float = 0.0,
) -> None:
    session = requests.Session()
    queue = deque(start_urls)
    seen: Set[str] = set()
    manifest: List[dict] = []
    saved_count = 0

    while queue and saved_count < max_pages:
        url = queue.popleft()
        if url in seen:
            continue
        seen.add(url)

        try:
            html = fetch(url, session, delay_s=delay_s)
        except Exception as e:
            manifest.append({"url": url, "status": "error", "error": str(e)})
            continue

        for page in extract_page(url, html):
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

        for link in extract_urls_from_html(html, url, allowed_prefixes):
            if link not in seen:
                queue.append(link)

    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    build_readme(output_dir, manifest)


def main() -> None:
    parser = argparse.ArgumentParser(description="Crawler de Customer Journey Analytics para Markdown")
    parser.add_argument(
        "--start-urls",
        nargs="*",
        default=DEFAULT_START_URLS,
        help="URLs iniciais",
    )
    parser.add_argument(
        "--output-dir",
        default="./CJA",
        help="Diretório de saída",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=2000,
        help="Máximo de páginas/arquivos Markdown",
    )
    parser.add_argument(
        "--delay-s",
        type=float,
        default=0.0,
        help="Delay entre requisições",
    )
    parser.add_argument(
        "--allowed-prefixes",
        nargs="*",
        default=DEFAULT_ALLOWED_PREFIXES,
        help="Prefixes internos permitidos",
    )

    args = parser.parse_args()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    crawl(
        start_urls=args.start_urls,
        output_dir=output_dir,
        allowed_prefixes=args.allowed_prefixes,
        max_pages=args.max_pages,
        delay_s=args.delay_s,
    )


if __name__ == "__main__":
    main()
