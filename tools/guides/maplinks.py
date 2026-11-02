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
    'yadkin-valley': 'Elkin, NC', 'hunt-country': 'Middleburg, VA', 'dahlonega': 'Dahlonega, GA',
    'gulf-shores': 'Gulf Shores, AL', 'chattanooga': 'Chattanooga, TN', 'smoky-mountains': 'Gatlinburg, TN',
    'lake-lure': 'Lake Lure, NC', 'lake-keowee': 'Seneca, SC', 'lake-lanier': 'Gainesville, GA',
    'harpers-ferry': 'Harpers Ferry, WV',
}
# Full search text where the name plus the guide's town would be ambiguous or wrong.
QUERY = {
    'Montage Palmetto Bluff': 'Montage Palmetto Bluff, Bluffton, SC',
    'Ponte Vedra Inn & Club': 'Ponte Vedra Inn & Club, Ponte Vedra Beach, FL',
    'The Lodge & Club at Ponte Vedra Beach': 'The Lodge & Club at Ponte Vedra Beach, FL',
    'Hotel Domestique': 'Hotel Domestique, Travelers Rest, SC',
    'Elliotts on Linden': 'Elliotts on Linden, Southern Pines, NC',
    'Mid Pines Inn & Golf Club': 'Mid Pines Inn & Golf Club, Southern Pines, NC',
    'Pine Needles Lodge': 'Pine Needles Lodge & Golf Club, Southern Pines, NC',
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
    'The Rockford Inn': 'The Rockford Inn, Dobson, NC',
    'JOLO Winery & Vineyards': 'JOLO Winery & Vineyards, Pilot Mountain, NC',
    'Wisdom Table': 'Wisdom Table, 101 E Main St, Elkin, NC',
    'Spirits Tavern': 'Spirits Tavern, Dahlonega, GA',
    'The Bavarian Inn': 'Bavarian Inn, Shepherdstown, WV',
    'Redbook at Hillbrook Inn': 'Hillbrook Inn, Charles Town, WV',
    'Hillbrook Inn': 'Hillbrook Inn, Charles Town, WV',
    'Snallygasters Cafe & Wine Bar': 'Snallygasters, Harpers Ferry, WV',
    'Grassy Creek Klondike Cabins': 'Grassy Creek Vineyard & Winery, State Road, NC',
    'The Inn at Little Washington': 'The Inn at Little Washington, Washington, VA',
    'Salamander suites': 'Salamander Middleburg, VA',
    'The Conservatory at Goodstone': 'Goodstone Inn & Restaurant, Middleburg, VA',
    'Turquoise Place': 'Turquoise Place, Orange Beach, AL',
    'Turquoise Place suites': 'Turquoise Place, Orange Beach, AL',
    'Perdido Beach Resort': 'Perdido Beach Resort, Orange Beach, AL',
    'Voyagers': 'Voyagers, Perdido Beach Resort, Orange Beach, AL',
    'Perch': 'Perch, The Lodge at Gulf State Park, Gulf Shores, AL',
    'Doc’s Seafood Shack & Oyster Bar': 'Doc’s Seafood Shack & Oyster Bar, Orange Beach, AL',
    'The Edwin suites': 'The Edwin Hotel, Chattanooga, TN',
    'Dancing Bear Lodge': 'Dancing Bear Lodge, Townsend, TN',
    'Dancing Bear Appalachian Bistro': 'Dancing Bear Appalachian Bistro, Townsend, TN',
    'Blackberry Farm': 'Blackberry Farm, Walland, TN',
    'Blackberry Mountain': 'Blackberry Mountain, Walland, TN',
    'Devils Fork State Park villas': 'Devils Fork State Park, Salem, SC',
    'The Lighthouse Restaurant': 'The Lighthouse Restaurant, Lake Keowee, Seneca, SC',
    'Lanier Islands Legacy Lodge': 'Lanier Islands Legacy Lodge, Buford, GA',
    'Sidney’s at Legacy Lodge': 'Sidney’s, Lanier Islands Legacy Lodge, Buford, GA',
}
SKIP = {'Luxury beach homes', 'Vineyard cottage rentals', 'Gulf-front beach homes', 'A picnic in Cades Cove', 'Lake Lure vacation rentals', 'Lake Keowee vacation rentals'}
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
