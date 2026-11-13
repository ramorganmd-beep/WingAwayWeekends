"""Keep the homepage "Shopping" interest in step with the guides.

Usage: python3 tools/guides/shop_tags.py

Adds the "Shopping" tag in docs/destinations.js to every destination whose guide has a Shopping section
(<section id="shopping">), and removes it from any that don't. Run after tools/guides/shop.py.
"""
import re
from pathlib import Path

DOCS = Path(__file__).resolve().parents[2] / 'docs'
path = DOCS / 'destinations.js'
s = path.read_text()
has = {p.parent.name for p in DOCS.glob('*/index.html') if '<section id="shopping"' in p.read_text()}

# Each destination is a {...} block at one indent level; its tags list comes before its guide.
out, n_add, n_del = [], 0, 0
for block in re.split(r'(?m)(?=^ ?\{$)', s):
    g = re.search(r'"guide": "([^"/]+)/"', block)
    m = re.search(r'"tags": \[(.*?)\]', block, re.S)
    if g and m:
        tags = re.findall(r'"([^"]+)"', m.group(1))
        want = g.group(1) in has
        if want and 'Shopping' not in tags:
            tags.append('Shopping'); n_add += 1
        elif not want and 'Shopping' in tags:
            tags.remove('Shopping'); n_del += 1
        else:
            out.append(block); continue
        items = re.findall(r'(\s*)"([^"]+)"', m.group(1))
        ind = items[0][0] if items else '\n   '
        close = re.search(r'(\s*)$', m.group(1)).group(1)
        new = '"tags": [' + ','.join(f'{ind}"{t}"' for t in tags) + close + ']'
        block = block[:m.start()] + new + block[m.end():]
    out.append(block)
path.write_text(''.join(out))
print(f'shopping tags: +{n_add} -{n_del} ({len(has)} guides with a Shopping section)')
