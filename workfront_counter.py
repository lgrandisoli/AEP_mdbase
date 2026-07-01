#!/usr/bin/env python3
"""
Conta o total de páginas que o workfront_crawler_v4 processaria,
sem baixar conteúdo nem gerar arquivos .md.
"""

import argparse
import re
import time
from collections import deque
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

ALLOWED_DOMAINS = {
    "experienceleague.adobe.com",
    "helpx.adobe.com",
}
DEFAULT_START_URLS = [
    "https://experienceleague.adobe.com/en/docs/workfront/using/home",
    "https://helpx.adobe.com/br/legal/product-descriptions/adobe-workfront.html",
]
DEFAULT_ALLOWED_PREFIXES = [
    "/en/docs/workfront",
    "/en/browse/workfront",
    "/br/legal/product-descriptions",
]
BLOCKED_PREFIXES = [
    "/en/docs/workfront-learn",
    "/en/docs/workfront-known-issues",
    "/en/docs/workfront-fusion",
]
BLOCKED_PATH_SUBSTRINGS = [
    "/tutorial",
    "/learn/",
    "/beta/",
    "known-issue",
    "known-issues",
    "release-activity",
]
LATEST_RELEASE_SLUG = "release-26-q3"
RELEASE_NOTES_PREFIX = (
    "/en/docs/workfront/using/product-announcements/product-releases/"
)
USER_AGENT = (
    "Mozilla/5.0 "
    "(Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 "
    "(KHTML, like Gecko) "
    "Chrome/126.0 Safari/537.36"
)

session = requests.Session()
session.headers.update({"User-Agent": USER_AGENT})


def path_matches_prefix(path, prefix):
    prefix = prefix.rstrip("/")
    return path == prefix or path.startswith(prefix + "/")


def allowed_url(url, prefixes):
    parsed = urlparse(url)
    if parsed.netloc and parsed.netloc not in ALLOWED_DOMAINS:
        return False
    path = parsed.path
    if any(path_matches_prefix(path, b) for b in BLOCKED_PREFIXES):
        return False
    if any(b in path for b in BLOCKED_PATH_SUBSTRINGS):
        return False
    if path.startswith(RELEASE_NOTES_PREFIX):
        if LATEST_RELEASE_SLUG not in path:
            return False
    return any(path_matches_prefix(path, p) for p in prefixes)


def fetch(url):
    r = session.get(url, timeout=120)
    r.raise_for_status()
    return r.text


def extract_urls(html, current_url, allowed_prefixes):
    urls = set()
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all(True):
        for attr in ("href", "data-href", "data-url", "data-path"):
            value = tag.get(attr)
            if not value:
                continue
            absolute = urljoin(current_url, value)
            if allowed_url(absolute, allowed_prefixes):
                urls.add(absolute)
    pattern = re.compile(r'https://experienceleague\.adobe\.com[^\s"\']+')
    for match in pattern.findall(html):
        if allowed_url(match, allowed_prefixes):
            urls.add(match)
    return urls


def infer_category(path):
    p = path.lower()
    if "/api/" in p:
        return "reference"
    if "/tutorial" in p or "/learn/" in p:
        return "tutorials"
    if "release-notes" in p:
        return "release-notes"
    if p.endswith("/home"):
        return "overview"
    return "guides"


def count(start_urls, allowed_prefixes, max_pages, delay_s=0.2):
    queue = deque(start_urls)
    seen = set()
    totals = {"saved": 0, "skipped-tutorial": 0, "error": 0}

    while queue and len(seen) < max_pages:
        url = queue.popleft()
        if url in seen:
            continue
        seen.add(url)

        print(f"[{len(seen)}/{max_pages}] {url}", flush=True)

        try:
            html = fetch(url)
            path = urlparse(url).path
            category = infer_category(path)

            if category == "tutorials":
                totals["skipped-tutorial"] += 1
            else:
                totals["saved"] += 1

            for link in extract_urls(html, url, allowed_prefixes):
                if link not in seen:
                    queue.append(link)

        except Exception as e:
            totals["error"] += 1
            print(f"  ERROR: {e}", flush=True)

        time.sleep(delay_s)

    print()
    print("=" * 50)
    print(f"Total de URLs visitadas : {len(seen)}")
    print(f"  Páginas que virariam .md : {totals['saved']}")
    print(f"  Tutoriais ignorados      : {totals['skipped-tutorial']}")
    print(f"  Erros de fetch           : {totals['error']}")
    print("=" * 50)


def main():
    parser = argparse.ArgumentParser(
        description="Conta páginas do Workfront sem gerar arquivos."
    )
    parser.add_argument("--max-pages", type=int, default=5000)
    parser.add_argument(
        "--delay-s", type=float, default=0.2,
        help="Delay em segundos entre requisições"
    )
    args = parser.parse_args()

    count(
        start_urls=DEFAULT_START_URLS,
        allowed_prefixes=DEFAULT_ALLOWED_PREFIXES,
        max_pages=args.max_pages,
        delay_s=args.delay_s,
    )


if __name__ == "__main__":
    main()
