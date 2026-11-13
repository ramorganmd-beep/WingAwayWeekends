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
    'nantucket': {
        'h2': 'Lightship baskets, Nantucket Reds and island-made treats.',
        'intro': 'Main Street’s cobblestones are the shopping district. Many shops shorten hours off-season; call ahead in winter.',
        'shops': [
            ('Island craft · Heirloom', 'Nantucket lightship baskets',
             'The island’s signature keepsake: hand-woven baskets and the miniature gold basket jewelry they inspired. Real ones start around $500; buy from island makers or ask for a certificate of authenticity.',
             '', 'Nantucket Lightship Basket Museum, Nantucket, MA'),
            ('Main Street · Island classic', 'Murray’s Toggery Shop',
             'Home of Nantucket Reds, the faded-red cotton that became the island’s uniform. A classic, wearable souvenir.',
             'https://www.nantucketreds.com/', 'Murray’s Toggery Shop, Main Street, Nantucket, MA'),
            ('Downtown · Books', 'Mitchell’s Book Corner',
             'An island bookshop with a strong Nantucket and maritime section, good for a beach read or a local history to take home.',
             'https://www.mitchellsbookcorner.com/', 'Mitchell’s Book Corner, Nantucket, MA'),
        ],
        'food': [
            ('Take home · Farm market', 'Bartlett’s Farm',
             'Nantucket’s oldest and largest family farm, farming since 1843, with a market, bakery and gift baskets. Tomatoes and corn in season.',
             'https://bartlettsfarm.com/', 'Bartlett’s Farm, Nantucket, MA'),
            ('Take home · Island spirits & wine', 'Cisco Brewers',
             'Beer, Nantucket Vineyard wines and Triple Eight spirits, all made on the island. A bottle travels well in the baggage compartment.',
             'https://www.ciscobrewers.com/', 'Cisco Brewers, Bartlett Farm Road, Nantucket, MA'),
        ],
    },
    'monterey-carmel': {
        'h2': 'Galleries, courtyards and a taste of Monterey County.',
        'intro': 'Carmel-by-the-Sea packs dozens of galleries and small shops into a few walkable blocks; there are no street addresses, so use the map links.',
        'shops': [
            ('Carmel · Art', 'Carmel’s galleries',
             'Around 80 to 100 galleries in about a square mile, from plein-air painting to ceramics and photography. Pick a street and wander; many artists are local.',
             '', 'art galleries, Carmel-by-the-Sea, CA'),
            ('Carmel · Courtyard shops', 'Carmel Plaza',
             'An open-air plaza at Ocean and Junipero with independent boutiques, fashion and home shops.',
             'https://carmelplaza.com/', 'Carmel Plaza, Carmel-by-the-Sea, CA'),
        ],
        'food': [
            ('Take home · Monterey wines', 'A Taste of Monterey',
             'A wine market and tasting room on Cannery Row pouring wines from more than 60 Monterey County wineries, with a view of the bay. Taste first, then pick a bottle to fly home.',
             'https://atasteofmonterey.com/', 'A Taste of Monterey, Cannery Row, Monterey, CA'),
        ],
    },
    'santa-fe': {
        'h2': 'Pueblo pottery, turquoise and red chile.',
        'intro': 'Buy directly from Native artists under the Palace portal, browse the galleries off the Plaza and on Canyon Road, and leave room for chile.',
        'shops': [
            ('Plaza · Native artists', 'Native American Artisans Portal',
             'Under the portal of the Palace of the Governors, Native artists sell jewelry, pottery and crafts they made themselves, a tradition the museum oversees. The best place to buy directly from the maker.',
             'https://www.nmhistorymuseum.dca.nm.gov/', 'Palace of the Governors, Santa Fe, NM'),
            ('Near the Plaza · Fine pottery', 'Andrea Fisher Fine Pottery',
             'Historic and contemporary Pueblo pottery, including the work of Maria Martinez of San Ildefonso, with knowledgeable staff. A high-end keepsake with a story.',
             'https://www.andreafisherpottery.com/', 'Andrea Fisher Fine Pottery, Santa Fe, NM'),
            ('East Side · Galleries', 'Canyon Road',
             'Half a mile of galleries in old adobes: Native American art, painting, sculpture and ceramics. Best on a slow morning walk.',
             '', 'Canyon Road, Santa Fe, NM'),
        ],
        'food': [
            ('Take home · Chile & spices', 'Santa Fe School of Cooking market',
             'Red and green chile, spices, cookbooks and cookware at 125 North Guadalupe Street, a short walk from the Plaza.',
             'https://santafeschoolofcooking.com/', 'Santa Fe School of Cooking, 125 N Guadalupe St, Santa Fe, NM'),
            ('Take home · Chocolate', 'Kakawa Chocolate House',
             'Historic drinking-chocolate elixirs, truffles and chile chocolates, with gift sets to take home.',
             'https://kakawachocolates.com/', 'Kakawa Chocolate House, Santa Fe, NM'),
        ],
    },
    'fredericksburg': {
        'h2': 'Main Street boutiques and a Hill Country pantry.',
        'intro': 'Main Street is lined with boutiques, galleries and food shops. Peach season runs roughly May through August.',
        'shops': [
            ('Downtown · Shopping street', 'Main Street',
             'Blocks of boutiques, home and gift shops, galleries and German-heritage storefronts. Easy to walk from the inns and B&Bs.',
             '', 'Main Street, Fredericksburg, TX'),
        ],
        'food': [
            ('Take home · Jams & sauces', 'Fischer & Wieser',
             'Started in 1969 as a roadside peach stand; taste jams, preserves and sauces at Das Peach Haus or the shop on Main Street.',
             'https://fwfarmstead.com/', 'Das Peach Haus, Fredericksburg, TX'),
            ('Take home · Texas gourmet', 'Rustlin’ Rob’s',
             'Hundreds of Texas foods to sample before you buy, from dips and salsas to jellies, at 121 East Main Street. Closed Sundays.',
             'https://www.rustlinrobs.com/', 'Rustlin’ Rob’s, 121 E Main St, Fredericksburg, TX'),
        ],
    },
    'highlands-cashiers': {
        'h2': 'Mountain galleries and handmade pottery.',
        'intro': 'Highlands’ Main Street and the side streets around it hold galleries, boutiques and gourmet shops; Cashiers adds more galleries 10 miles east.',
        'shops': [
            ('Highlands · Pottery & crafts', 'Peak Experience',
             'Known for the area’s largest selection of handmade pottery, plus American handcrafts and estate jewelry, at 2820 Dillard Road. A good stop for one-of-a-kind mugs.',
             '', 'Peak Experience, 2820 Dillard Road, Highlands, NC'),
            ('Highlands · Main Street', 'Main Street shops & galleries',
             'Boutiques, galleries, outfitters and specialty shops along Main Street, with more on Spring Street, Fourth Street and Carolina Way.',
             'https://www.highlandschamber.org/things-to-do/shopping/', 'Main Street, Highlands, NC'),
        ],
    },
    'bucks-county': {
        'h2': 'Potters’ studios, galleries and a country market.',
        'intro': 'New Hope’s galleries line Main and Mechanic Streets; Peddler’s Village in Lahaska is 10 minutes away.',
        'shops': [
            ('New Hope · Pottery studio', 'Goose Creek Pottery',
             'A working studio and gallery where porcelain and stoneware are made on site. A good place for a handmade mug.',
             'https://www.goosecreekpottery.com/', 'Goose Creek Pottery, 17 W Ferry St, New Hope, PA'),
            ('Lahaska · Village shops', 'Peddler’s Village',
             'More than 60 shops and boutiques in a garden village, most of them small and locally owned.',
             'https://peddlersvillage.com/shop/', 'Peddler’s Village, Lahaska, PA'),
        ],
        'food': [
            ('Take home · Country market', 'Rice’s Market',
             'A market of more than 150 years outside New Hope with hundreds of vendors: produce, baked goods, antiques and collectibles. Tuesdays and Saturdays, 7 a.m. to 1 p.m., March through December.',
             'https://www.ricesmarket.com/', 'Rice’s Market, New Hope, PA'),
        ],
    },
    'st-augustine': {
        'h2': 'Datil heat, chocolate and the old town’s shops.',
        'intro': 'St. George Street is the pedestrian heart; Aviles Street, the oldest street in town, holds the galleries.',
        'shops': [
            ('Historic district · Pedestrian street', 'St. George Street',
             'Shops, sweets and souvenirs in the old town’s car-free main street. Go early or late to avoid the midday crowds.',
             '', 'St. George Street, St. Augustine, FL'),
            ('Historic district · Galleries', 'Aviles Street',
             'Small galleries and local art on the oldest street in the city, a short walk south of the Plaza.',
             '', 'Aviles Street, St. Augustine, FL'),
        ],
        'food': [
            ('Take home · Datil pepper sauce', 'Dat’l Do-It',
             'St. Augustine’s own hot sauce, made with the datil pepper the city’s Minorcan families have grown for generations. Sweet heat; sold around town and online.',
             'https://www.datldoit.com/', ''),
            ('Take home · Chocolate', 'Whetstone Chocolates',
             'A local chocolate maker with tasting tours and gift boxes; the shop is at 139 King Street.',
             'https://www.whetstonechocolates.com/', 'Whetstone Chocolates, 139 King St, St. Augustine, FL'),
        ],
    },
    'key-west': {
        'h2': 'Key lime everything, island pottery and handmade sandals.',
        'intro': 'Duval Street is the main drag; the best local shops are on the side streets around it.',
        'shops': [
            ('Old Town · Studio & gallery', 'Key West Pottery',
             'A working pottery studio and gallery: handmade mugs, vases and island-inspired ceramics. A good one-of-a-kind souvenir.',
             'https://www.keywestpottery.com/', 'Key West Pottery, Key West, FL'),
            ('Old Town · Since 1966', 'Kino Sandals',
             'Leather sandals still cut and assembled in the little factory at Greene and Fitzpatrick Streets since 1966. Inexpensive and very Key West.',
             'https://kinosandals.com/', 'Kino Sandal Factory, Key West, FL'),
        ],
        'food': [
            ('Take home · Key lime', 'Kermit’s Key West Key Lime Shoppe',
             'Key lime pie, pie bars, candy, cookies, juice and pantry goods. Pick up a frozen pie for the flight home if you have a cooler.',
             'https://kermitskeylime.com/', 'Kermit’s Key West Key Lime Shoppe, Key West, FL'),
        ],
    },
    'charlottesville': {
        'h2': 'Local pottery on the Downtown Mall.',
        'intro': 'The Downtown Mall, one of the country’s longest pedestrian malls, is the place to browse; it’s an easy walk between shops, galleries and dinner.',
        'shops': [
            ('Downtown Mall · Pedestrian street', 'The Downtown Mall',
             'Eight blocks of brick pedestrian street lined with independent shops, galleries, bookstores and restaurants.',
             '', 'Downtown Mall, Charlottesville, VA'),
            ('Downtown Mall · Local artists', 'C’ville Arts Cooperative Gallery',
             'A cooperative gallery of more than 60 local artists: pottery, jewelry and prints. A good place for a handmade mug.',
             'https://www.cvillearts.org/', 'C’ville Arts Cooperative Gallery, Charlottesville, VA'),
        ],
    },
    'annapolis': {
        'h2': 'Pottery, boutiques and the Maryland Avenue shops.',
        'intro': 'Main Street runs from the State House down to the harbor; Maryland Avenue, behind the State House, has the smaller specialty shops.',
        'shops': [
            ('State Circle · Pottery', 'The Annapolis Pottery',
             'A pottery studio and shop at 40 State Circle, with pieces from Maryland blue crabs to bold contemporary glazes. Mugs make an easy carry-home.',
             'https://annapolispottery.com/', 'The Annapolis Pottery, 40 State Circle, Annapolis, MD'),
            ('Historic district · Specialty shops', 'Maryland Avenue',
             'More than twenty small specialty stores, boutiques and galleries in historic storefronts.',
             'https://www.visitannapolis.org/plan/landmarks-and-neighborhoods/maryland-avenue/', 'Maryland Avenue, Annapolis, MD'),
        ],
    },
    'kennebunkport': {
        'h2': 'Dock Square galleries and Maine-made crafts.',
        'intro': 'Dock Square’s shops fill old houses and 18th-century warehouses by the river; many keep shorter hours off-season.',
        'shops': [
            ('Dock Square · Shopping', 'Dock Square',
             'The village’s hub: boutiques, galleries and specialty shops selling art, clothing, jewelry and Maine-made gifts.',
             '', 'Dock Square, Kennebunkport, ME'),
            ('Dock Square · American crafts', 'Abacus Gallery',
             'A Maine gallery of American handmade crafts and jewelry, with a shop in Kennebunkport. Good for pottery, glass and gifts.',
             'https://abacusgallery.com/', 'Abacus Gallery, Kennebunkport, ME'),
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
    food = ''.join(card(*c) for c in d.get('food', []))
    return ('<!--wa-shop--><section id="shopping"><div class="section-head"><div><span class="eyebrow">00 / Shopping &amp; take home</span>'
            f'<h2>{esc(d["h2"])}</h2></div><p>{esc(d["intro"])}</p></div>'
            f'<div class="grid three">{shops}</div>'
            + (f'<h3 class="subhead">Local flavors to take home</h3><div class="grid three">{food}</div>' if food else '')
            + '<p class="estimate">Hours change with the season; check before you go. No paid placements.</p></section><!--/wa-shop-->\n')


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
