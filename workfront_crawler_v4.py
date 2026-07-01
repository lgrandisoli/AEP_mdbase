#!/usr/bin/env python3

import argparse
import json
import re
import time
from collections import deque
from dataclasses import dataclass, asdict
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

ALLOWED_DOMAINS = {
    "experienceleague.adobe.com",
    "helpx.adobe.com",
}
DEFAULT_START_URLS = [
    "https://experienceleague.adobe.com/en/docs/workfront/using/home",
    # Product Description
    "https://helpx.adobe.com/br/legal/product-descriptions/adobe-workfront.html",
]

DEFAULT_ALLOWED_PREFIXES = [
    "/en/docs/workfront",
    "/en/browse/workfront",
    # Product Description
    "/br/legal/product-descriptions",
]

# Paths excluídos mesmo que comecem com um prefixo permitido
BLOCKED_PREFIXES = [
    "/en/docs/workfront/using/product-announcements",
    "/en/docs/workfront-learn",
]

USER_AGENT = (
    "Mozilla/5.0 "
    "(Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 "
    "(KHTML, like Gecko) "
    "Chrome/126.0 Safari/537.36"
)


@dataclass
class Page:
    url: str
    title: str
    category: str
    topic_path: str
    section_slug: str | None
    markdown: str


session = requests.Session()
session.headers.update({"User-Agent": USER_AGENT})


def clean_filename(text):
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text[:180]


def infer_category(path):
    p = path.lower()

    if "/api/" in p:
        return "reference"

    if "/tutorial" in p:
        return "tutorials"

    if "/learn/" in p:
        return "tutorials"

    if "release-notes" in p:
        return "release-notes"

    if p.endswith("/home"):
        return "overview"

    return "guides"


def allowed_url(url, prefixes):
    parsed = urlparse(url)

    if parsed.netloc and parsed.netloc not in ALLOWED_DOMAINS:
        return False

    path = parsed.path

    if any(path.startswith(blocked) for blocked in BLOCKED_PREFIXES):
        return False

    for prefix in prefixes:
        if path.startswith(prefix):
            return True

    return False


def fetch(url):
    r = session.get(url, timeout=120)
    r.raise_for_status()
    return r.text


def html_to_markdown(html):
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = soup.get_text("\n")

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    return "\n\n".join(lines)


def extract_urls_from_html(html, current_url, allowed_prefixes):

    urls = set()

    soup = BeautifulSoup(html, "html.parser")

    attrs = [
        "href",
        "data-href",
        "data-url",
        "data-path"
    ]

    for tag in soup.find_all(True):

        for attr in attrs:

            value = tag.get(attr)

            if not value:
                continue

            absolute = urljoin(current_url, value)

            if allowed_url(absolute, allowed_prefixes):
                urls.add(absolute)

    pattern = re.compile(
        r'https://experienceleague\.adobe\.com[^\s"\']+'
    )

    for match in pattern.findall(html):

        if allowed_url(match, allowed_prefixes):
            urls.add(match)

    return urls


def extract_page(url, html):

    soup = BeautifulSoup(html, "html.parser")

    title = (
        soup.title.text.strip()
        if soup.title
        else url
    )

    path = urlparse(url).path

    markdown = html_to_markdown(html)

    return Page(
        url=url,
        title=title,
        category=infer_category(path),
        topic_path=path.strip("/"),
        section_slug=None,
        markdown=markdown,
    )


def save_page(page, output_dir):

    filename = clean_filename(page.title)

    if not filename:
        filename = "untitled"

    md_path = output_dir / f"{filename}.md"

    md_path.write_text(
        page.markdown,
        encoding="utf-8"
    )

    return md_path


def build_readme(output_dir, manifest):

    saved_items = [item for item in manifest if item.get("status") == "saved"]

    lines = [
        "# Adobe Workfront Documentation",
        "",
        f"Total pages: {len(saved_items)}",
        ""
    ]

    for item in saved_items[:200]:
        lines.append(
            f"- [{item['title']}]({item['url']})"
        )

    (output_dir / "README.md").write_text(
        "\n".join(lines),
        encoding="utf-8"
    )


def crawl(
    start_urls,
    output_dir,
    allowed_prefixes,
    max_pages,
):

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    queue = deque(start_urls)

    seen = set()

    manifest = []

    while queue and len(seen) < max_pages:

        url = queue.popleft()

        if url in seen:
            continue

        seen.add(url)

        print(
            f"[{len(seen)}/{max_pages}] {url}"
        )

        try:

            html = fetch(url)

            page = extract_page(
                url,
                html
            )

            saved_path = save_page(
                page,
                output_dir
            )

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

            for link in extract_urls_from_html(
                html,
                url,
                allowed_prefixes,
            ):

                if link not in seen:
                    queue.append(link)

        except Exception as e:

            manifest.append(
                {
                    "url": url,
                    "status": "error",
                    "error": str(e),
                }
            )

        time.sleep(0.2)

    (output_dir / "manifest.json").write_text(
        json.dumps(
            manifest,
            indent=2,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )

    build_readme(
        output_dir,
        manifest
    )

    print()
    print(
        f"Finished. Pages processed: {len(manifest)}"
    )


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--output-dir",
        default="workfront_guides"
    )

    parser.add_argument(
        "--max-pages",
        type=int,
        default=5000
    )

    args = parser.parse_args()

    crawl(
        start_urls=DEFAULT_START_URLS,
        output_dir=Path(args.output_dir),
        allowed_prefixes=DEFAULT_ALLOWED_PREFIXES,
        max_pages=args.max_pages,
    )


if __name__ == "__main__":
    main()

