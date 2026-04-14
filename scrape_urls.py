#!/usr/bin/env python3
"""
Scraper to collect all internal URLs from https://national-claims.co.uk/
Uses a breadth-first crawl starting from the homepage.
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque
import time
import sys

BASE_URL = "https://national-claims.co.uk"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; URLScraper/1.0)"
}

visited = set()
queue = deque([BASE_URL])
all_urls = set()

def is_internal(url):
    parsed = urlparse(url)
    return parsed.netloc in ("", "national-claims.co.uk", "www.national-claims.co.uk")

def normalize(url):
    parsed = urlparse(url)
    # Remove fragment, keep path/query
    return parsed._replace(fragment="").geturl()

print(f"Starting crawl of {BASE_URL} ...\n")

while queue:
    url = queue.popleft()
    url = normalize(url)

    if url in visited:
        continue
    visited.add(url)

    try:
        resp = requests.get(url, headers=HEADERS, timeout=15, allow_redirects=True)
        final_url = normalize(resp.url)
        visited.add(final_url)
        all_urls.add(final_url)

        print(f"  [{resp.status_code}] {final_url}")

        if "text/html" not in resp.headers.get("Content-Type", ""):
            continue

        soup = BeautifulSoup(resp.text, "lxml")
        for tag in soup.find_all("a", href=True):
            href = tag["href"].strip()
            if not href or href.startswith("#") or href.startswith("mailto:") or href.startswith("tel:"):
                continue
            full = urljoin(final_url, href)
            full = normalize(full)
            if is_internal(full) and full not in visited:
                queue.append(full)

    except Exception as e:
        print(f"  [ERROR] {url} — {e}", file=sys.stderr)

    time.sleep(0.3)  # polite delay

# Sort and deduplicate
sorted_urls = sorted(all_urls)

print(f"\n{'='*60}")
print(f"Total unique URLs found: {len(sorted_urls)}")
print(f"{'='*60}\n")

output_file = "/home/user/claude-seo/national_claims_urls.txt"
with open(output_file, "w") as f:
    for u in sorted_urls:
        f.write(u + "\n")

print(f"All URLs saved to: {output_file}\n")
for u in sorted_urls:
    print(u)
