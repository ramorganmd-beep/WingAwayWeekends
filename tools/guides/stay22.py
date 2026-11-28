"""Add a Stay22 "compare hotel prices" link under each guide's Where to stay cards.

Usage: python3 tools/guides/stay22.py docs/<slug>/index.html [...]

Idempotent (replaces the block between the wa-stay22 markers). Uses the guide's
coordinates from docs/destinations.js. The link is labeled as an affiliate link
and carries rel="sponsored". Our own hotel picks stay first and are never paid.
"""
import json
import re
import sys
import urllib.parse
from pathlib import Path

AID = 'wingawayweekend'
ROOT = Path(__file__).resolve().parents[2]
START, END = '<!--wa-stay22-->', '<!--/wa-stay22-->'
BLOCK = re.compile(re.escape(START) + '.*?' + re.escape(END), re.S)


def destinations():
    s = (ROOT / 'docs/destinations.js').read_text()
    s = s[s.index('['):s.rindex(']') + 1]
    return {d['guide'].strip('/'): d for d in json.loads(s) if d.get('guide')}


# Islands reached only by air or ferry: hotel searches also show mainland hotels, so name the island's towns.
ISLAND = {
    'block-island': ('New Shoreham, Rhode Island', 'New Shoreham'),
    'nantucket': ('Nantucket, Massachusetts', 'Nantucket or Siasconset'),
    'marthas-vineyard': ('Edgartown, Massachusetts', 'Edgartown, Oak Bluffs, Vineyard Haven, West Tisbury, Chilmark or Aquinnah'),
    'mackinac': ('Mackinac Island, Michigan', 'Mackinac Island'),
    'catalina-island': ('Avalon, California', 'Avalon or Two Harbors'),
    'put-in-bay': ('Put-in-Bay, Ohio', 'Put-in-Bay'),
    'drummond-island': ('Drummond Island, Michigan', 'Drummond Island'),
    'ocracoke': ('Ocracoke, North Carolina', 'Ocracoke'),
    'lanai': ('Lanai City, Hawaii', 'Lanai City or Manele'),
    'san-juan-islands': ('Friday Harbor, Washington', 'Friday Harbor, Orcas Island or Lopez Island'),
}


def link(d, slug):
    addr = ISLAND[slug][0] if slug in ISLAND else re.sub(r' & .*|,.*| National Park.*', '', d['name']) + ', ' + d.get('state', '')
    q = {'aid': AID, 'lat': d['lat'], 'lng': d['lon'], 'address': addr, 'campaign': 'guide-' + slug}
    return 'https://www.stay22.com/allez/roam?' + urllib.parse.urlencode(q)


def block(d, slug):
    short = re.sub(r' & .*|,.*| National Park.*', '', d['name'])
    return (START + '<div class="wa-s22" style="margin:18px 0 0;padding:14px 16px;border:1px solid #dbe3e9;border-radius:3px;background:#f7f9fa">'
            f'<a href="{link(d, slug)}" target="_blank" rel="sponsored noopener" style="font-weight:700">Compare hotel prices near {short} →</a>'
            '<p style="margin:6px 0 0;font-size:13px;color:#526471">Prices and availability for your dates, through our partner Stay22. '
            'This is an affiliate link: we may earn a commission at no cost to you. The picks above are never paid.</p>'
            + (f'<p style="margin:6px 0 0;font-size:13px;color:#8a3b12;font-weight:600">Island stays only: listings outside {ISLAND[slug][1]} are on the mainland and need a flight or ferry.</p>' if slug in ISLAND else '')
            + '</div>' + END)


def main(paths):
    D = destinations()
    for path in map(Path, paths):
        slug = path.parent.name
        d = D.get(slug)
        s = path.read_text()
        s = BLOCK.sub('', s)
        i = s.find('<section id="stay"')
        if not d or i < 0:
            print('skip', slug)
            continue
        j = s.find('</section>', i)
        s = s[:j] + block(d, slug) + s[j:]
        path.write_text(s)


if __name__ == '__main__':
    main(sys.argv[1:])
