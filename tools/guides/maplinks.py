"""Give every hotel and restaurant card a link.

Usage: python3 tools/guides/maplinks.py docs/*/index.html

Cards in the Stay (including Luxury alternatives) and Eat sections that have
no confirmed official link get a "Website & map" link to a Google Maps search
for the place, which shows its website, phone and hours. Cards with an
official link keep it. Idempotent; run after luxury.py.
"""
import html
import re
import sys
import urllib.parse
from pathlib import Path

TOWN = {
    'savannah': 'Savannah, GA', 'charleston': 'Charleston, SC', 'asheville': 'Asheville, NC',
    'pinehurst': 'Pinehurst, NC', 'beaufort': 'Beaufort, SC', 'st-augustine': 'St. Augustine, FL',
    'greenville': 'Greenville, SC', 'charlottesville': 'Charlottesville, VA', 'nashville': 'Nashville, TN',
    'key-west': 'Key West, FL', 'outer-banks': 'Outer Banks, NC', 'amelia-island': 'Fernandina Beach, FL',
}
# Full search text where the name plus the guide's town would be ambiguous or wrong.
QUERY = {
    'Montage Palmetto Bluff': 'Montage Palmetto Bluff, Bluffton, SC',
    'The Inn & Club at Harbour Town': 'The Inn & Club at Harbour Town, Hilton Head Island, SC',
    'Ponte Vedra Inn & Club': 'Ponte Vedra Inn & Club, Ponte Vedra Beach, FL',
    'The Lodge & Club at Ponte Vedra Beach': 'The Lodge & Club at Ponte Vedra Beach, FL',
    'Hotel Domestique': 'Hotel Domestique, Travelers Rest, SC',
    'Elliotts on Linden': 'Elliotts on Linden, Southern Pines, NC',
    'Mid Pines Inn & Golf Club': 'Mid Pines Inn & Golf Club, Southern Pines, NC',
    'Pine Needles Lodge': 'Pine Needles Lodge & Golf Club, Southern Pines, NC',
    'Carolina suites': 'The Carolina Hotel, Pinehurst Resort, Pinehurst, NC',
    'The Sanderling Resort': 'The Sanderling Resort, Duck, NC',
    'Sanderling soundfront suites': 'The Sanderling Resort, Duck, NC',
    'Blue Point': 'The Blue Point, Duck, NC',
    'The White Doe Inn': 'White Doe Inn, Manteo, NC',
    'Tranquil House Inn': 'Tranquil House Inn, Manteo, NC',
    '1587 Restaurant & Lounge': '1587 Restaurant, Manteo, NC',
    'Salt & Cypress Kitchen': 'Salt & Cypress Kitchen, Manteo, NC',
    'Latitudes, Sunset Key': 'Latitudes, Sunset Key, Key West, FL',
    'Keswick Hall': 'Keswick Hall, Keswick, VA',
    'The Clifton': 'The Clifton, Charlottesville, VA',
    'The Ritz-Carlton, Amelia Island': 'The Ritz-Carlton, Amelia Island, FL',
    'Club level at The Ritz-Carlton': 'The Ritz-Carlton, Amelia Island, FL',
    'Omni oceanfront villas': 'Omni Amelia Island Resort, FL',
    'Elizabeth Pointe Lodge': 'Elizabeth Pointe Lodge, Fernandina Beach, FL',
}
SKIP = {'Luxury beach homes', 'H2O Suites or Almond Tree Inn'}
OLD = re.compile(r'<a class="textlink maplink"[^>]*>.*?</a>', re.S)


def link(name, slug):
    q = QUERY.get(name, f'{name}, {TOWN[slug]}')
    url = 'https://www.google.com/maps/search/?api=1&query=' + urllib.parse.quote(q)
    return (f'<a class="textlink maplink" href="{url}" target="_blank" rel="noopener">Website &amp; map'
            f'<span class="sr"> for {html.escape(name)}</span></a>')


for path in map(Path, sys.argv[1:]):
    slug = path.parent.name
    if slug not in TOWN:
        continue
    s = OLD.sub('', path.read_text())
    added = 0
    for sec in ('stay', 'eat'):
        i = s.index(f'<section id="{sec}">')
        j = s.index('</section>', i)
        part = s[i:j]

        def fix(m):
            global added
            art = m.group(0)
            if 'class="textlink"' in art:
                return art
            name = html.unescape(re.search(r'<h3>(.*?)</h3>', art).group(1))
            if name in SKIP:
                return art
            added += 1
            return art[:-len('</article>')] + link(name, slug) + '</article>'
        part = re.sub(r'<article class="card">.*?</article>', fix, part, flags=re.S)
        s = s[:i] + part + s[j:]
    path.write_text(s)
    print(f'map links: {path} (+{added})')
