"""Add a "Weather" link (the weather outlook, /wx/) to the top menu of a page, after its "Fly to lunch" link.

Usage: python3 tools/guides/wx_nav.py docs/index.html docs/*/index.html docs/trips/*/index.html
Idempotent. The link's path and style copy the page's own "Fly to lunch" (or other) menu link, so it
matches each header. Run after feedback.py when rebuilding guides; the trip templates carry it already.
"""
import re, sys
from pathlib import Path

for path in map(Path, sys.argv[1:]):
    s = path.read_text()
    m = re.search(r'<header\b.*?</header>', s, re.S)
    if not m or 'href="' not in m.group(0) or '/wx/"' in m.group(0) or 'href="wx/"' in m.group(0):
        continue
    head = m.group(0)
    links = list(re.finditer(r'<a class="header-link" href="([^"]*)"([^>]*)>[^<]*</a>', head))
    if not links:
        continue
    ref = next((l for l in links if l.group(1).endswith('fly-to-lunch/')), links[-1])
    href = ref.group(1)
    base = href[:href.rstrip('/').rfind('/') + 1] if href.rstrip('/').count('/') else ''
    if path.parent.name == 'wx':
        continue
    link = f'<a class="header-link" href="{base}wx/"{links[-1].group(2)}>Weather</a>'
    new_head = head[:ref.end()] + link + head[ref.end():]  # right after "Fly to lunch" (or the last link)
    path.write_text(s[:m.start()] + new_head + s[m.end():])
    print('added', path)
