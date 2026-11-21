"""Copy each Built-for-kids guide's 'why' line and best ages from kids.py into docs/destinations.js
(fields kidsWhy, kidsAges), for the homepage cards when the Built for kids switch is on.
Usage: python3 tools/guides/kids_blurbs.py"""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent)); sys.argv = sys.argv[:1]
from kids import KIDS  # noqa: E402
p = Path(__file__).resolve().parents[2] / 'docs/destinations.js'; s = p.read_text()
for slug, k in KIDS.items():
    s = re.sub(r'\n\s*"kidsWhy": .*?,\n\s*"kidsAges": .*?,(?=\n\s*"guide": "%s/")' % re.escape(slug), '', s)
    m = re.search(r'\n(\s*)"guide": "%s/",' % re.escape(slug), s)
    assert m, slug
    ind = m.group(1)
    s = s[:m.start()] + '\n%s"kidsWhy": %s,\n%s"kidsAges": %s,' % (ind, json.dumps(k['why'], ensure_ascii=False), ind, json.dumps(k['ages'])) + s[m.start():]
p.write_text(s); print(len(KIDS), 'guides')
