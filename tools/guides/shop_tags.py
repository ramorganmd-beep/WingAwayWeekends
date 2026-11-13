"""Keep the homepage interest tags that come from the guides in step with them.

Usage: python3 tools/guides/shop_tags.py

In docs/destinations.js, every destination gets
  "Shopping"         when its guide has a Shopping section (<section id="shopping">), and
  "No rental car"    when its Getting into town box answers "No rental car needed?" with Likely or Yes,
and loses them when that stops being true. Run after tools/guides/shop.py and tools/guides/ground.py.
"""
import re
from pathlib import Path

DOCS = Path(__file__).resolve().parents[2] / 'docs'
RULES = {
    'Shopping': lambda s: '<section id="shopping"' in s,
    'No rental car': lambda s: bool(re.search(r'No rental car needed\?</dt><dd>(Likely|Yes)', s)),
}
pages = {p.parent.name: p.read_text() for p in DOCS.glob('*/index.html')}
path = DOCS / 'destinations.js'
s = path.read_text()

out, counts = [], {t: [0, 0, 0] for t in RULES}  # added, removed, total
for block in re.split(r'(?m)(?=^ ?\{$)', s):
    g = re.search(r'"guide": "([^"/]+)/"', block)
    m = re.search(r'"tags": \[(.*?)\]', block, re.S)
    if g and m and g.group(1) in pages:
        tags = re.findall(r'"([^"]+)"', m.group(1))
        old = list(tags)
        for t, rule in RULES.items():
            want = rule(pages[g.group(1)])
            counts[t][2] += want
            if want and t not in tags:
                tags.append(t); counts[t][0] += 1
            elif not want and t in tags:
                tags.remove(t); counts[t][1] += 1
        if tags != old:
            items = re.findall(r'(\s*)"([^"]+)"', m.group(1))
            ind = items[0][0] if items else '\n   '
            close = re.search(r'(\s*)$', m.group(1)).group(1)
            block = block[:m.start()] + '"tags": [' + ','.join(f'{ind}"{t}"' for t in tags) + close + ']' + block[m.end():]
    out.append(block)
path.write_text(''.join(out))
for t, (a, r, n) in counts.items():
    print(f'{t}: +{a} -{r} ({n} destinations)')
