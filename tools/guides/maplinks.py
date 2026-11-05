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
    'hilton-head': 'Hilton Head Island, SC', 'highlands-cashiers': 'Highlands, NC',
    'st-michaels': 'St. Michaels, MD', 'cape-may': 'Cape May, NJ', 'shenandoah': 'Luray, VA',
    'homestead': 'Hot Springs, VA', 'greenbrier': 'White Sulphur Springs, WV',
    'newport': 'Newport, RI', 'nantucket': 'Nantucket, MA', 'bar-harbor': 'Bar Harbor, ME',
    'stowe': 'Stowe, VT', 'saratoga': 'Saratoga Springs, NY', 'gettysburg': 'Gettysburg, PA',
    'lancaster': 'Lancaster, PA', 'hudson-valley': 'Rhinebeck, NY', 'mystic': 'Mystic, CT', 'portsmouth': 'Portsmouth, NH',
    'kennebunkport': 'Kennebunkport, ME', 'berkshires': 'Lenox, MA', 'lake-placid': 'Lake Placid, NY', 'marthas-vineyard': 'Edgartown, MA',
    'bardstown': 'Bardstown, KY', 'dayton': 'Dayton, OH', 'mackinac': 'Mackinac Island, MI', 'french-lick': 'French Lick, IN',
    'galena': 'Galena, IL', 'door-county': 'Fish Creek, WI',
    'branson': 'Branson, MO', 'lake-ozarks': 'Osage Beach, MO', 'hot-springs': 'Hot Springs, AR', 'bentonville': 'Bentonville, AR',
    'eureka-springs': 'Eureka Springs, AR', 'duluth': 'Duluth, MN',
    'naples': 'Naples, FL', 'sanibel': 'Sanibel, FL', 'islamorada': 'Islamorada, FL', 'palm-beach': 'Palm Beach, FL',
    'cedar-key': 'Cedar Key, FL', '30a': 'Santa Rosa Beach, FL',
    'fredericksburg': 'Fredericksburg, TX', 'san-antonio': 'San Antonio, TX', 'fort-worth': 'Fort Worth, TX', 'galveston': 'Galveston, TX', 'new-orleans': 'New Orleans, LA', 'mountain-view-ar': 'Mountain View, AR', 'buffalo-river': 'Ponca, AR', 'bowling-green': 'Bowling Green, KY', 'red-river-gorge': 'Slade, KY', 'sedona': 'Sedona, AZ', 'moab': 'Moab, UT', 'sun-valley': 'Ketchum, ID', 'jackson-hole': 'Jackson, WY', 'santa-fe': 'Santa Fe, NM', 'aspen': 'Aspen, CO', 'gunflint-trail': 'Grand Marais, MN', 'drummond-island': 'Drummond Island, MI', 'lake-wawasee': 'Syracuse, IN', 'long-lake-ny': 'Long Lake, NY', 'moosehead-lake': 'Greenville, ME', 'rangeley': 'Rangeley, ME', 'tavares': 'Tavares, FL', 'havre-de-grace': 'Havre de Grace, MD', 'okoboji': 'Okoboji, IA', 'des-moines': 'Des Moines, IA', 'dubuque': 'Dubuque, IA', 'amana-colonies': 'Amana, IA', 'rehoboth-lewes': 'Rehoboth Beach, DE', 'bethany-beach': 'Bethany Beach, DE', 'brandywine-valley': 'Wilmington, DE', 'dover-de': 'Dover, DE', 'tulsa': 'Tulsa, OK', 'oklahoma-city': 'Oklahoma City, OK', 'wichita-mountains': 'Medicine Park, OK', 'broken-bow': 'Broken Bow, OK', 'north-shore': 'Grand Marais, MN', 'twin-cities': 'Minneapolis, MN', 'stillwater': 'Stillwater, MN', 'minocqua': 'Minocqua, WI', 'elkhart-lake': 'Elkhart Lake, WI', 'wisconsin-dells': 'Wisconsin Dells, WI', 'hayward': 'Hayward, WI', 'bedford-springs': 'Bedford, PA', 'laurel-highlands': 'Ligonier, PA', 'pittsburgh': 'Pittsburgh, PA', 'pine-creek-gorge': 'Wellsboro, PA', 'hershey': 'Hershey, PA', 'erie': 'Erie, PA', 'put-in-bay': 'Put-in-Bay, OH', 'hocking-hills': 'Logan, OH', 'cleveland': 'Cleveland, OH', 'indianapolis': 'Indianapolis, IN', 'brown-county': 'Nashville, IN', 'indiana-dunes': 'Chesterton, IN', 'chicago': 'Chicago, IL', 'starved-rock': 'Utica, IL', 'shawnee-hills': 'Cobden, IL', 'bayfield': 'Bayfield, WI', 'madison': 'Madison, WI', 'lake-geneva': 'Lake Geneva, WI', 'kohler': 'Kohler, WI', 'harbor-springs': 'Harbor Springs, MI', 'saugatuck': 'Saugatuck, MI', 'traverse-city': 'Traverse City, MI', 'lindsborg': 'Lindsborg, KS', 'lawrence': 'Lawrence, KS', 'flint-hills': 'Cottonwood Falls, KS', 'wichita': 'Wichita, KS', 'valentine': 'Valentine, NE', 'scottsbluff': 'Scottsbluff, NE', 'lincoln-ne': 'Lincoln, NE', 'omaha': 'Omaha, NE', 'peace-garden': 'Bottineau, ND', 'bismarck': 'Bismarck, ND', 'fargo': 'Fargo, ND', 'medora': 'Medora, ND', 'sioux-falls': 'Sioux Falls, SD', 'badlands': 'Interior, SD', 'deadwood': 'Deadwood, SD', 'black-hills': 'Custer, SD', 'north-conway': 'North Conway, NH', 'lake-winnipesaukee': 'Meredith, NH', 'bretton-woods': 'Bretton Woods, NH', 'burlington-vt': 'Burlington, VT', 'manchester-vt': 'Manchester, VT', 'woodstock-vt': 'Woodstock, VT', 'atlantic-city': 'Atlantic City, NJ', 'asbury-park': 'Asbury Park, NJ', 'litchfield-hills': 'Litchfield County, CT', 'essex-ct': 'Essex, CT', 'new-haven': 'New Haven, CT', 'watch-hill': 'Watch Hill, RI', 'providence': 'Providence, RI', 'block-island': 'Block Island, RI', 'princeton': 'Princeton, NJ', 'chatham': 'Chatham, MA', 'portland-maine': 'Portland, ME', 'camden': 'Camden, ME', 'poconos': 'Mount Pocono, PA', 'bucks-county': 'New Hope, PA', 'finger-lakes': 'Ithaca, NY', 'paducah': 'Paducah, KY', 'louisville': 'Louisville, KY', 'lexington': 'Lexington, KY', 'berkeley-springs': 'Berkeley Springs, WV', 'new-river-gorge': 'Fayetteville, WV', 'deep-creek-lake': 'Oakland, MD', 'ocean-city': 'Ocean City, MD', 'annapolis': 'Annapolis, MD', 'kansas-city': 'Kansas City, MO', 'st-louis': 'St. Louis, MO', 'little-rock': 'Little Rock, AR', 'natchitoches': 'Natchitoches, LA', 'clarksdale': 'Clarksdale, MS', 'golden-isles': 'St. Simons Island, GA', 'memphis': 'Memphis, TN', 'birmingham': 'Birmingham, AL', 'lake-martin': 'Dadeville, AL', 'huntsville': 'Huntsville, AL', 'fairhope': 'Fairhope, AL', 'lafayette': 'Lafayette, LA', 'st-francisville': 'St. Francisville, LA', 'bay-st-louis': 'Bay St. Louis, MS', 'oxford': 'Oxford, MS', 'natchez': 'Natchez, MS',
    'south-padre': 'South Padre Island, TX', 'marfa': 'Marfa, TX',
}
# Full search text where the name plus the guide's town would be ambiguous or wrong.
QUERY = {
    'The Tidewater Inn': 'The Tidewater Inn, Easton, MD',
    'The Wylder Hotel': 'The Wylder Hotel, Tilghman Island, MD',
    'Bas Rouge': 'Bas Rouge, Easton, MD',
    'Stars': 'Stars, Inn at Perry Cabin, St. Michaels, MD',
    'Skyland': 'Skyland, Shenandoah National Park, VA',
    'Big Meadows Lodge': 'Big Meadows Lodge, Shenandoah National Park, VA',
    'Pollock Dining Room at Skyland': 'Pollock Dining Room, Skyland, Shenandoah National Park, VA',
    'The Inn at Little Washington': 'The Inn at Little Washington, Washington, VA',
    'The Inn at Gristmill Square': 'Inn at Gristmill Square, Warm Springs, VA',
    'Jefferson’s Restaurant & Taproom': 'Jefferson’s Restaurant, Omni Homestead, Hot Springs, VA',
    'American Audubon Dining Room': 'American Audubon Dining Room, Omni Homestead, Hot Springs, VA',
    'Sam Snead’s Tavern': 'Sam Snead’s Tavern, Hot Springs, VA',
    'The General Lewis Inn': 'The General Lewis Inn, Lewisburg, WV',
    'Prime 44 West': 'Prime 44 West, The Greenbrier, White Sulphur Springs, WV',
    'The Main Dining Room': 'Main Dining Room, The Greenbrier, White Sulphur Springs, WV',
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
    'Hotel Cashiers': 'Hotel Cashiers, Cashiers, NC',
    'The Orchard': 'The Orchard, Cashiers, NC',
    'High Hampton': 'High Hampton, Cashiers, NC',
    'CQ’s Restaurant': 'CQ’s Restaurant, Harbour Town, Hilton Head Island, SC',
    'Snallygasters Cafe & Wine Bar': 'Snallygasters, Harpers Ferry, WV',
    'Grassy Creek Klondike Cabins': 'Grassy Creek Vineyard & Winery, State Road, NC',
    'The Inn at Little Washington': 'The Inn at Little Washington, Washington, VA',
    'Salamander suites': 'Salamander Middleburg, VA',
    'The Conservatory at Goodstone': 'Goodstone Inn & Restaurant, Middleburg, VA',
    'Turquoise Place': 'Turquoise Place, Orange Beach, AL',
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
SKIP = {'The Downtown Historic Island Hotel', 'Dock Street at sunset', 'Branson Landing', 'A dock-and-dine restaurant', 'A lakeside grill', 'Downtown Hot Springs', 'Downtown Eureka Springs', 'Downtown Bardstown', 'Main Street cafés', 'Fudge on Main Street', 'Stonington Borough', 'Greenbrier cottages & estate homes', 'Luxury beach homes', 'Vineyard cottage rentals', 'A picnic in Cades Cove'}
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
