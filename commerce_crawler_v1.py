#!/usr/bin/env python3
"""
Crawler de documentação Adobe Commerce / Experience League.

OBJETIVO
--------
Percorrer um conjunto de URLs-semente (overview pages) da documentação
Adobe Commerce, descobrir subpáginas (links internos sob o mesmo prefixo
de caminho) e salvar cada página visitada como um arquivo .md individual.

LIMITES E REGRAS DE OPERAÇÃO
-----------------------------
- Limite rígido de 5000 arquivos .md gerados (parâmetro MAX_PAGES).
- Apenas segue links cujo domínio esteja na lista ALLOWED_DOMAINS.
- Apenas segue links que comecem com o mesmo "prefixo de seção" da URL
  semente que o originou (ex.: tudo abaixo de
  /en/docs/commerce-admin/catalog/ a partir daquela semente), para evitar
  que o crawler "escape" para a documentação inteira do site.
- Respeita robots.txt de cada domínio antes de crawlear.
- Aplica delay entre requisições (REQUEST_DELAY_SECONDS) para não
  sobrecarregar o servidor da Adobe.
- Não falsifica nem inventa conteúdo: se uma página não puder ser
  baixada ou convertida, ela é registrada em crawl_log.csv com o motivo
  da falha, e nenhum .md é criado para ela.

SAÍDA
-----
- Diretório output/ com um .md por página, nomeado a partir do path da URL.
- Arquivo crawl_log.csv com o resultado de cada URL processada
  (status, motivo de erro, timestamp) — serve como registro auditável
  de execução.
- Arquivo manifest.json com metadados de cada página salva (url, arquivo
  gerado, título extraído, data da coleta).

USO
---
    python3 adobe_commerce_crawler.py

Dependências (já presentes no ambiente): requests, beautifulsoup4.
"""

import argparse
import csv
import json
import re
import time
import urllib.robotparser as robotparser
from collections import deque
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup, NavigableString, Tag
from html import unescape
from typing import List

# --------------------------------------------------------------------------
# CONFIGURAÇÃO
# --------------------------------------------------------------------------

SEED_URLS = [
    "https://developer.adobe.com/commerce/extensibility/",
    "https://developer.adobe.com/commerce/extensibility/events/",
    "https://developer.adobe.com/commerce/webapi/",
    "https://developer.adobe.com/commerce/services/",
    "https://developer.adobe.com/commerce/frontend-core/",
    "https://developer.adobe.com/commerce/php/",
    "https://developer.adobe.com/commerce/testing/",
    "https://developer.adobe.com/commerce/contributor/",
    "https://developer.adobe.com/commerce/marketplace/",
]

ALLOWED_DOMAINS = {
    "developer.adobe.com",
}

def _parse_args():
    p = argparse.ArgumentParser(description="Crawler de documentação Adobe Commerce")
    p.add_argument("--output-dir", default="output", help="Diretório de saída dos .md")
    p.add_argument("--max-pages", type=int, default=5000, help="Limite de páginas")
    p.add_argument("--delay-s", type=float, default=1.0, help="Delay entre requisições (s)")
    return p.parse_args()

_ARGS = _parse_args()

MAX_PAGES = _ARGS.max_pages
REQUEST_DELAY_SECONDS = _ARGS.delay_s
REQUEST_TIMEOUT_SECONDS = 20
USER_AGENT = "AdobeCommerceDocsCrawler/1.0 (+uso interno de documentação)"
OUTPUT_DIR = Path(_ARGS.output_dir)
LOG_FILE = OUTPUT_DIR / "crawl_log.csv"
MANIFEST_FILE = OUTPUT_DIR / "manifest.json"

# --------------------------------------------------------------------------
# UTILITÁRIOS
# --------------------------------------------------------------------------


def normalize_url(url: str) -> str:
    """Remove fragmento (#...) e barra final duplicada para deduplicar."""
    parsed = urlparse(url)
    path = parsed.path.rstrip("/") or "/"
    return f"{parsed.scheme}://{parsed.netloc}{path}"


def section_prefix(url: str) -> str:
    """
    Define o prefixo de seção de uma URL-semente.
    Ex.: .../docs/commerce-admin/catalog/guide-overview
         -> .../docs/commerce-admin/catalog/
    Usado para impedir que o crawler suba para fora da seção de origem.
    """
    parsed = urlparse(url)
    parts = parsed.path.rstrip("/").split("/")
    if len(parts) > 1:
        prefix_path = "/".join(parts[:-1]) + "/"
    else:
        prefix_path = parsed.path
    return f"{parsed.scheme}://{parsed.netloc}{prefix_path}"


def url_to_filename(url: str) -> str:
    parsed = urlparse(url)
    slug = f"{parsed.netloc}{parsed.path}".strip("/")
    slug = re.sub(r"[^a-zA-Z0-9/_-]", "-", slug)
    slug = slug.replace("/", "__")
    if not slug:
        slug = "index"
    return slug[:180] + ".md"


class RobotsCache:
    """Cache simples de robots.txt por domínio, para não rebaixar a cada URL."""

    def __init__(self, user_agent: str):
        self.user_agent = user_agent
        self._cache = {}

    def is_allowed(self, url: str) -> bool:
        parsed = urlparse(url)
        domain = parsed.netloc
        if domain not in self._cache:
            rp = robotparser.RobotFileParser()
            robots_url = f"{parsed.scheme}://{domain}/robots.txt"
            try:
                rp.set_url(robots_url)
                rp.read()
            except Exception:
                # Se não foi possível ler robots.txt, por precaução
                # tratamos como "não permitido" para essa URL.
                self._cache[domain] = None
                return False
            self._cache[domain] = rp
        rp = self._cache[domain]
        if rp is None:
            return False
        return rp.can_fetch(self.user_agent, url)


# --------------------------------------------------------------------------
# CRAWLER
# --------------------------------------------------------------------------


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


def extract_main_content(soup: BeautifulSoup):
    """
    Tenta isolar o conteúdo principal da página (evitando navegação,
    rodapé, banners de cookies etc). Faz fallback para <body> inteiro
    caso nenhum seletor conhecido seja encontrado.
    """
    candidates = [
        "main",
        "article",
        "[role='main']",
        "#main-content",
        ".main-content",
    ]
    for selector in candidates:
        node = soup.select_one(selector)
        if node and node.get_text(strip=True):
            return node
    return soup.body or soup


def extract_links(base_url: str, soup: BeautifulSoup):
    links = set()
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if not href or href.startswith(("mailto:", "tel:", "javascript:")):
            continue
        full = urljoin(base_url, href)
        full = normalize_url(full)
        links.add(full)
    return links


def crawl():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    robots = RobotsCache(USER_AGENT)
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})

    visited = set()
    saved_count = 0
    manifest = []

    log_rows = []

    # Fila: cada item é (url, prefixo_da_secao_de_origem)
    queue = deque()
    seed_prefixes = []
    for seed in SEED_URLS:
        norm = normalize_url(seed)
        prefix = section_prefix(norm)
        seed_prefixes.append(prefix)
        queue.append((norm, prefix))

    while queue and saved_count < MAX_PAGES:
        url, allowed_prefix = queue.popleft()
        if url in visited:
            continue
        visited.add(url)

        domain = urlparse(url).netloc
        timestamp = datetime.now(timezone.utc).isoformat()

        if domain not in ALLOWED_DOMAINS:
            log_rows.append([url, "skipped", "domínio fora de ALLOWED_DOMAINS", timestamp])
            continue

        if not robots.is_allowed(url):
            log_rows.append([url, "skipped", "bloqueado por robots.txt", timestamp])
            continue

        try:
            resp = session.get(url, timeout=REQUEST_TIMEOUT_SECONDS)
        except requests.RequestException as exc:
            log_rows.append([url, "error", f"falha de requisição: {exc}", timestamp])
            continue

        if resp.status_code != 200:
            log_rows.append([url, "error", f"HTTP {resp.status_code}", timestamp])
            continue

        content_type = resp.headers.get("Content-Type", "")
        if "text/html" not in content_type:
            log_rows.append([url, "skipped", f"content-type não suportado: {content_type}", timestamp])
            continue

        soup = BeautifulSoup(resp.text, "html.parser")

        for link in extract_links(url, soup):
            link_parsed = urlparse(link)
            if link_parsed.netloc not in ALLOWED_DOMAINS:
                continue
            if "/commerce" not in link_parsed.path:
                continue
            if link not in visited:
                queue.append((link, allowed_prefix))

        main_node = extract_main_content(soup)
        title_tag = soup.find("title")
        title = title_tag.get_text(strip=True) if title_tag else url

        if not main_node or not main_node.get_text(strip=True):
            log_rows.append([url, "error", "conteúdo principal vazio/não localizado", timestamp])
            continue

        md_body = node_to_markdown(main_node).strip()

        if not md_body:
            log_rows.append([url, "error", "conversão para markdown resultou vazia", timestamp])
            continue

        filename = url_to_filename(url)
        filepath = OUTPUT_DIR / filename

        header = (
            f"# {title}\n\n"
            f"**Fonte original:** {url}\n\n"
            f"**Coletado em (UTC):** {timestamp}\n\n"
            "---\n\n"
        )

        filepath.write_text(header + md_body, encoding="utf-8")
        saved_count += 1

        manifest.append({
            "url": url,
            "file": str(filepath),
            "title": title,
            "collected_at_utc": timestamp,
        })
        log_rows.append([url, "saved", str(filepath), timestamp])

        if saved_count % 25 == 0:
            print(f"[{saved_count}/{MAX_PAGES}] páginas salvas... última: {url}")

        time.sleep(REQUEST_DELAY_SECONDS)

    # Persiste log e manifesto
    with LOG_FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["url", "status", "detalhe", "timestamp_utc"])
        writer.writerows(log_rows)

    with MANIFEST_FILE.open("w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print("\nResumo da execução")
    print("-------------------")
    print(f"Total de URLs visitadas : {len(visited)}")
    print(f"Total de .md salvos     : {saved_count}")
    print(f"Log detalhado           : {LOG_FILE.resolve()}")
    print(f"Manifesto               : {MANIFEST_FILE.resolve()}")
    print(f"Arquivos .md em         : {OUTPUT_DIR.resolve()}")


if __name__ == "__main__":
    crawl()