"""Add a "Shop & take home" section to a guide: local shops and makers, plus local foods to carry home.

Usage: python3 tools/guides/shop.py docs/<guide>/index.html [...]

Inserted before the Events section (or the Itinerary when a guide has no Events), with a "Shop" link in the
section menu. Section numbers in the eyebrows are renumbered after insertion. Idempotent: the section sits
between <!--wa-shop--> markers. Only shops with an official website checked before publishing; no paid picks.
"""
import re
import sys
from pathlib import Path
from urllib.parse import quote_plus

# guide folder -> {'h2', 'intro', 'shops': [...], 'food': [...]}; each card: (tag, name, text, url, map query)
SHOP = {
    'charleston': {
        'h2': 'Baskets, makers and a pantry to take home.',
        'intro': 'Start at the City Market, then wander King Street. Leave room in the baggage compartment.',
        'shops': [
            ('Downtown · Open-air market', 'Charleston City Market',
             'A favorite: four blocks of open market halls with more than 300 vendors, many selling what they make: local lotions and soaps, jewelry, art and crafts. Watch sweetgrass baskets being woven, and buy them from the weavers themselves.',
             'https://www.thecharlestoncitymarket.com/', 'Charleston City Market, Charleston, SC'),
            ('Downtown · Shopping street', 'King Street',
             'Charleston’s main shopping street: independent boutiques, antiques on lower King and well-known stores in between. Easy to walk from the hotels above.',
             '', 'King Street, Charleston, SC'),
        ],
        'food': [
            ('Take home · Lowcountry pantry', 'Charleston Specialty Foods',
             'Local brands in one stop: benne wafers, pralines, stone-ground grits, Lowcountry rice and honey. Gift baskets ship if the airplane is full.',
             'https://www.charlestonspecialtyfoods.com/', ''),
            ('Take home · Benne wafers', 'Olde Colony Bakery',
             'The Mt. Pleasant bakery behind the classic benne (sesame) wafer, a Lowcountry cookie with West African roots. Light, and travels well.',
             'https://www.oldecolonybakery.com/', 'Olde Colony Bakery, Mount Pleasant, SC'),
            ('Take home · Spices & teas', 'The Spice & Tea Exchange',
             'A favorite near the City Market, at 170 Church Street: spices, hand-blended seasonings, flavored salts and sugars, and loose-leaf teas, with plenty to smell and sample before you choose.',
             'https://www.spiceandtea.com/charleston', 'The Spice & Tea Exchange, 170 Church St, Charleston, SC'),
            ('Take home · Carolina Gold rice', 'Carolina Plantation Rice',
             'Carolina Gold, the heirloom rice that built the Lowcountry kitchen, grown in South Carolina. Look for it in local food shops, or order from the grower.',
             'https://www.carolinaplantationrice.com/', ''),
        ],
    },
    'savannah': {
        'h2': 'Honey, cookies and Savannah design.',
        'intro': 'Broughton Street is the shopping spine; the squares make the walk between shops the best part.',
        'shops': [
            ('Downtown · Shopping street', 'Broughton Street',
             'Savannah’s main street for local boutiques and familiar names, a few blocks from the river and the squares.',
             '', 'Broughton Street, Savannah, GA'),
            ('Downtown · Art & design', 'shopSCAD',
             'Jewelry, prints, home goods and fashion made by students, alumni and faculty of the Savannah College of Art and Design.',
             'https://www.shopscad.com/', 'shopSCAD, Savannah, GA'),
        ],
        'food': [
            ('Take home · Local honey', 'Savannah Bee Company',
             'Honey from Savannah’s own beekeeping company, with a tasting bar to try before you buy, plus honey-based body care.',
             'https://savannahbee.com/', 'Savannah Bee Company, Savannah, GA'),
            ('Take home · Cookies', 'Byrd’s Cookies',
             'A Savannah bakery since 1924. The cookies come in decorative tins that survive a baggage compartment.',
             'https://byrdcookiecompany.com/', 'Byrd Cookie Company, Savannah, GA'),
            ('Take home · Salts & seasonings', 'The Salt Table',
             'Savannah-made salts, seasoning blends, oils and vinegars, blended and packed locally.',
             'https://www.salttable.com/', 'The Salt Table, Savannah, GA'),
        ],
    },
    'asheville': {
        'h2': 'Mountain crafts and chocolate to carry home.',
        'intro': 'Asheville is one of the great craft towns in the South. Plan an afternoon downtown and one in the studios.',
        'shops': [
            ('Downtown · Local artisans', 'Grove Arcade',
             'A grand 1928 arcade with local shops: pottery, jewelry, woodwork, weaving and blown glass. Outside, the Portico Market sells local crafts, honey and handmade soaps.',
             'https://grovearcade.com/', 'Grove Arcade, Asheville, NC'),
            ('River Arts District · Studios', 'River Arts District',
             'A mile of artists’ studios and galleries in old riverside buildings along the French Broad. Many artists work in the open and sell directly.',
             'https://www.riverartsdistrict.com/', 'River Arts District, Asheville, NC'),
        ],
        'food': [
            ('Take home · Chocolate', 'French Broad Chocolate',
             'Bean-to-bar chocolate made in Asheville, in gift-ready packaging. Buy downtown or order ahead.',
             'https://frenchbroadchocolates.com/', 'French Broad Chocolate Lounge, Asheville, NC'),
            ('Take home · Mountain pantry', 'Mast General Store',
             'The old-time general store at 15 Biltmore Avenue: candy, regional jams and Southern pantry goods from local makers, plus outdoor gear.',
             'https://www.mastgeneralstore.com/', 'Mast General Store, Biltmore Avenue, Asheville, NC'),
        ],
    },
    'knoxville': {
        'h2': 'Market Square shops and Old City makers.',
        'intro': 'Downtown is compact: Market Square, Gay Street and the Old City are a short walk apart.',
        'shops': [
            ('Market Square · Gifts', 'Earth to Old City',
             'An eclectic local shop for gifts, handmade soaps and bath goods, jewelry and Knoxville souvenirs.',
             'https://earthtooldcity.com/', 'Earth to Old City, Market Square, Knoxville, TN'),
            ('Downtown · Local artists', 'Art Market Gallery',
             'A collective of more than 50 regional artists showing and selling their own work.',
             'https://www.artmarketgallery.net/', 'Art Market Gallery, Knoxville, TN'),
        ],
        'food': [
            ('Take home · Mountain pantry', 'Mast General Store',
             'The old-time general store at 402 South Gay Street: candy, regional jams and Southern pantry goods from local makers, plus outdoor gear.',
             'https://www.mastgeneralstore.com/', 'Mast General Store, Gay Street, Knoxville, TN'),
            ('Take home · Farmers’ market', 'Market Square Farmers’ Market',
             'Wednesdays and Saturdays, May through November, with a smaller winter market on some Saturdays: local produce, honey, preserves and baked goods.',
             'https://www.visitknoxville.com/things-to-do/popular-spots/market-square/', 'Market Square, Knoxville, TN'),
        ],
    },
    'beaufort': {
        'food': [
            ('Take home · Local shrimp', 'Gay Fish Company',
             'A family shrimp dock on St. Helena Island since 1948. Fresh local shrimp, plus grits, hot sauce, spices and Frogmore Stew fixings to take home. Ask them to pack shrimp on ice for the flight.',
             '', 'Gay Fish Company, 1948 Sea Island Parkway, St. Helena Island, SC'),
        ],
    },
    'nashville': {
        'food': [
            ('Take home · Candy since 1912', 'Goo Goo Chocolate Co.',
             'The home of the Goo Goo Cluster, just south of Broadway on Third Avenue, with shop-only flavors and candy-making experiences.',
             'https://googoo.com/', 'Goo Goo Chocolate Co., 3rd Avenue South, Nashville, TN'),
            ('Take home · Chocolate', 'Olive & Sinclair',
             'Bean-to-bar Southern chocolate made in East Nashville; the factory at 1628 Fatherland Street offers tours and tastings. Try the brittle.',
             'https://oliveandsinclair.com/', 'Olive & Sinclair Chocolate, 1628 Fatherland St, Nashville, TN'),
        ],
    },
    'pinehurst': {
        'add': [
            ('Seagrove · Pottery', 'North Carolina Pottery Center',
             'About 45 minutes north, Seagrove is the heart of North Carolina’s handmade pottery tradition. Start at the center, at 233 East Avenue, then visit working potters nearby. Open Tuesday–Saturday.',
             'https://www.ncpotterycenter.org/', 'North Carolina Pottery Center, Seagrove, NC'),
        ],
    },
}

MARK = re.compile(r'<!--wa-shop-->.*?<!--/wa-shop-->\n?', re.S)
ADDMARK = re.compile(r'<!--wa-shopadd-->.*?<!--/wa-shopadd-->', re.S)
NAVMARK = '<a href="#shopping">Shop</a>'


def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def card(tag, name, text, url, q):
    # One link per card, as elsewhere in the guides: the official site, or a map when there is none.
    if url:
        link = f'<a class="textlink" href="{esc(url)}" target="_blank" rel="noopener">Official details<span class="sr"> for {esc(name)}</span></a>'
    else:
        link = (f'<a class="textlink maplink" href="https://www.google.com/maps/search/?api=1&amp;query={quote_plus(q)}" '
                f'target="_blank" rel="noopener">Website &amp; map<span class="sr"> for {esc(name)}</span></a>')
    return f'<article class="card"><div class="tag">{esc(tag)}</div><h3>{esc(name)}</h3><p>{esc(text)}</p>{link}</article>'


def section(d):
    shops = ''.join(card(*c) for c in d['shops'])
    food = ''.join(card(*c) for c in d['food'])
    return ('<!--wa-shop--><section id="shopping"><div class="section-head"><div><span class="eyebrow">00 / Shopping &amp; take home</span>'
            f'<h2>{esc(d["h2"])}</h2></div><p>{esc(d["intro"])}</p></div>'
            f'<div class="grid three">{shops}</div>'
            '<h3 class="subhead">Local flavors to take home</h3>'
            f'<div class="grid three">{food}</div>'
            '<p class="estimate">Hours change with the season; check before you go. No paid placements.</p></section><!--/wa-shop-->\n')


def renumber(s):
    n = [0]

    def rep(m):
        n[0] += 1
        return f'{m.group(1)}{n[0]:02d} / '
    return re.sub(r'(<span class="eyebrow">)\d{2} / ', rep, s)


def food_block(d):
    food = ''.join(card(*c) for c in d['food'])
    return ('<!--wa-shop--><h3 class="subhead">Local flavors to take home</h3>'
            f'<div class="grid three">{food}</div>'
            '<p class="estimate">Hours change with the season; check before you go. No paid placements.</p><!--/wa-shop-->')


def main(paths):
    for p in map(Path, paths):
        key = p.parent.name
        if key not in SHOP:
            continue
        s = ADDMARK.sub('', MARK.sub('', p.read_text())).replace(NAVMARK, '')
        d = SHOP[key]
        if '<section id="shopping"' in s:
            # The guide already has a Shopping section: add extra shops to its cards and the take-home foods below.
            i = s.index('<section id="shopping"')
            j = s.index('</section>', i)
            if d.get('add'):
                k = s.rindex('</article>', i, j) + len('</article>')
                s = s[:k] + '<!--wa-shopadd-->' + ''.join(card(*c) for c in d['add']) + '<!--/wa-shopadd-->' + s[k:]
                j = s.index('</section>', i)
            if d.get('food'):
                s = s[:j] + food_block(d) + s[j:]
            p.write_text(s)
            print('shop (take-home added):', p)
            continue
        anchor = '<section id="events"' if '<section id="events"' in s else '<section id="itinerary"'
        assert s.count(anchor) == 1, p
        s = s.replace(anchor, section(SHOP[key]) + anchor)
        nav = '<a href="#events">' if '<a href="#events">' in s else '<a href="#itinerary">'
        if nav in s:
            s = s.replace(nav, NAVMARK + nav, 1)
        s = renumber(s)
        p.write_text(s)
        print('shop:', p)


if __name__ == '__main__':
    main(sys.argv[1:])
