"""Build the multi-stop trip pages in docs/trips/ from ROUTES below and template.html.
Usage: python3 tools/trips/build_trips.py
Each route: id, title (page title), h1, lede, desc (meta), wx (weather tip), regions (for "add a stop"),
defaultSeason (months 1-12), season overrides, and route: [slug, nights, [alternative slugs]].
The page logic lives in docs/trips/trip.js.
"""
import json, urllib.parse
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
TPL = (ROOT / 'tools/trips/template.html').read_text()
SUMMER = [5, 6, 7, 8, 9, 10]
ROUTES = [
 dict(id='northeast', title='Northeast Flying Trip', h1='The Northeast in a week',
  lede='Seven nights by air: Cape May’s Victorian beach town, Newport’s mansions, Nantucket, Acadia and Bar Harbor, then Stowe in the Green Mountains.',
  desc='A seven-night flying loop through the Northeast, with dates, legs, fuel-stop flags and a guide for every stop. Swap stops to make it your own.',
  wx='Northeast summers bring afternoon thunderstorms and coastal fog; plan at least one spare day on a week-long trip, and fly the long legs in the morning.',
  regions=['Northeast', 'Mid-Atlantic'], defaultSeason=SUMMER,
  season={'stowe': [1, 2, 3, 6, 7, 8, 9, 10, 12], 'woodstock-vt': [1, 2, 3, 5, 6, 7, 8, 9, 10, 12], 'north-conway': [1, 2, 3, 6, 7, 8, 9, 10], 'lake-placid': [1, 2, 3, 6, 7, 8, 9, 10],
          'annapolis': [4, 5, 6, 7, 8, 9, 10], 'st-michaels': [4, 5, 6, 7, 8, 9, 10], 'bucks-county': [4, 5, 6, 7, 8, 9, 10, 11, 12], 'providence': [4, 5, 6, 7, 8, 9, 10, 11, 12],
          'burlington-vt': [6, 7, 8, 9, 10], 'bar-harbor': [6, 7, 8, 9, 10], 'camden': [6, 7, 8, 9, 10]},
  route=[['cape-may', 1, ['annapolis', 'st-michaels', 'rehoboth-lewes', 'bucks-county']],
         ['newport', 2, ['mystic', 'watch-hill', 'block-island', 'providence']],
         ['nantucket', 1, ['marthas-vineyard', 'chatham', 'block-island']],
         ['bar-harbor', 2, ['camden', 'portland-maine', 'kennebunkport', 'portsmouth']],
         ['stowe', 1, ['burlington-vt', 'woodstock-vt', 'manchester-vt', 'lake-placid', 'north-conway']]]),
 dict(id='lowcountry', title='Carolina & Georgia Coast Flying Trip', h1='The Carolina and Georgia coast',
  lede='Seven nights down the coast: Ocracoke’s island airstrip, Southport and Bald Head Island, Charleston, Beaufort and Savannah’s squares.',
  desc='A seven-night flying trip down the Carolina and Georgia coast, with dates, legs, fuel-stop flags and a guide for every stop.',
  wx='Summer afternoons bring thunderstorms along the coast, and hurricane season runs June to November; spring and fall are the best months. Plan a spare day.',
  regions=['Southeast', 'Florida'], defaultSeason=[3, 4, 5, 6, 9, 10, 11],
  season={'ocracoke': [5, 6, 7, 8, 9, 10], 'outer-banks': [5, 6, 7, 8, 9, 10]},
  route=[['ocracoke', 1, ['outer-banks']],
         ['southport', 1, ['pinehurst']],
         ['charleston', 2, ['hilton-head']],
         ['beaufort', 1, ['hilton-head']],
         ['savannah', 2, ['golden-isles', 'amelia-island', 'st-augustine']]]),
 dict(id='florida', title='Florida Flying Trip', h1='Florida, coast to Keys',
  lede='Seven nights around Florida: St. Augustine’s old town, Gulf beaches on Sanibel, Naples, Key West and Islamorada, home by way of Palm Beach.',
  desc='A seven-night flying loop around Florida, from St. Augustine to Key West, with dates, legs, fuel-stop flags and a guide for every stop.',
  wx='Winter and spring are the best flying months; summer brings daily afternoon thunderstorms, and hurricane season runs June to November. Watch the Key West and Miami airspace.',
  regions=['Florida'], defaultSeason=[11, 12, 1, 2, 3, 4, 5],
  route=[['st-augustine', 1, ['amelia-island', 'tavares']],
         ['sanibel', 2, ['anna-maria-island', 'naples', 'crystal-river']],
         ['key-west', 2, ['islamorada']],
         ['islamorada', 1, ['palm-beach']],
         ['palm-beach', 1, ['tavares', 'amelia-island']]]),
 dict(id='rockies', title='Rocky Mountain Flying Trip', h1='The Colorado and Utah high country',
  lede='Seven nights in the mountains: Aspen, Telluride’s box canyon, the red rock of Moab, Park City and Steamboat Springs.',
  desc='A seven-night mountain flying trip through Colorado and Utah, with dates, legs, fuel-stop flags and a guide for every stop.',
  wx='Mountain flying: high density altitude on summer afternoons, strong winds over the ridges and afternoon thunderstorms. Fly early, compute performance at every airport and plan a spare day.',
  regions=['Mountain West'], defaultSeason=[6, 7, 8, 9],
  season={'aspen': [1, 2, 3, 6, 7, 8, 9, 12], 'telluride': [1, 2, 3, 6, 7, 8, 9, 12], 'park-city': [1, 2, 3, 6, 7, 8, 9, 12], 'steamboat-springs': [1, 2, 3, 6, 7, 8, 9, 12], 'moab': [3, 4, 5, 9, 10]},
  route=[['aspen', 2, ['crested-butte', 'estes-park', 'colorado-springs']],
         ['telluride', 1, ['durango', 'crested-butte']],
         ['moab', 2, ['bryce-canyon', 'zion']],
         ['park-city', 1, ['bear-lake', 'jackson-hole']],
         ['steamboat-springs', 1, ['estes-park', 'saratoga-wy']]]),
 dict(id='california', title='California Coast Flying Trip', h1='The California coast',
  lede='Seven nights up the coast: San Diego, Santa Barbara, Paso Robles wine country, Monterey and Carmel, and Napa and Sonoma.',
  desc='A seven-night flying trip up the California coast, from San Diego to wine country, with dates, legs, fuel-stop flags and a guide for every stop.',
  wx='Coastal marine layer and low ceilings are common on summer mornings, especially May to July; plan coastal legs for midday and keep an inland alternate. Brief the busy Los Angeles and Bay Area airspace.',
  regions=['Southern California', 'Central California', 'Northern California'], defaultSeason=[3, 4, 5, 6, 7, 8, 9, 10, 11],
  route=[['san-diego', 1, ['temecula', 'catalina-island', 'palm-springs']],
         ['santa-barbara', 2, ['solvang', 'ojai', 'catalina-island']],
         ['paso-robles', 1, ['solvang', 'big-sur']],
         ['monterey-carmel', 2, ['big-sur', 'san-francisco']],
         ['napa-sonoma', 1, ['mendocino', 'san-francisco', 'lake-tahoe']]]),
 dict(id='great-lakes', title='Great Lakes Flying Trip', h1='The upper Great Lakes',
  lede='Seven nights around Lake Michigan and Lake Superior: Traverse City, Mackinac Island, Marquette and Pictured Rocks, the Apostle Islands and Door County.',
  desc='A seven-night flying loop through Michigan and Wisconsin, with dates, legs, fuel-stop flags and a guide for every stop.',
  wx='Summer is the season up north; watch for lake fog, cold water under long overwater legs and fast-moving fronts. Plan a spare day and carry flotation for the big-water crossings.',
  regions=['Midwest'], defaultSeason=[6, 7, 8, 9],
  route=[['traverse-city', 1, ['saugatuck', 'harbor-springs']],
         ['mackinac', 2, ['harbor-springs', 'drummond-island']],
         ['marquette', 1, ['drummond-island']],
         ['bayfield', 1, ['hayward', 'minocqua']],
         ['door-county', 2, ['kohler', 'elkhart-lake', 'lake-geneva']]]),
 dict(id='texas', title='Texas Hill Country Flying Trip', h1='Texas Hill Country and the Gulf',
  lede='Seven nights in Texas: Galveston’s Victorian Strand, Round Top’s antiques, Fredericksburg’s wineries, a fly-in resort at Horseshoe Bay and San Antonio’s River Walk.',
  desc='A seven-night flying trip through the Texas Hill Country and Gulf Coast, with dates, legs, fuel-stop flags and a guide for every stop.',
  wx='Spring brings wildflowers and severe storms; summer afternoons are hot and bumpy. Fly early, watch for morning stratus off the Gulf and brief the Houston and San Antonio airspace.',
  regions=['Texas'], defaultSeason=[3, 4, 5, 10, 11],
  route=[['galveston', 1, ['port-aransas', 'south-padre']],
         ['round-top', 1, ['waco', 'austin']],
         ['fredericksburg', 2, ['new-braunfels', 'austin']],
         ['horseshoe-bay', 1, ['granbury', 'austin']],
         ['san-antonio', 2, ['new-braunfels', 'port-aransas']]]),
 dict(id='southwest', title='Southwest Flying Trip', h1='Red rock and the high desert',
  lede='Seven nights in Arizona and New Mexico: Sedona’s red rock, the Grand Canyon, Santa Fe’s plazas, Taos and Albuquerque.',
  desc='A seven-night flying trip through Arizona and New Mexico, with dates, legs, fuel-stop flags and a guide for every stop.',
  wx='Desert and mountain flying: high density altitude, strong afternoon winds and turbulence, and monsoon storms from July to September. Fly in the morning and compute performance at every field.',
  regions=['Mountain West'], defaultSeason=[3, 4, 5, 9, 10, 11],
  route=[['sedona', 2, ['prescott', 'scottsdale']],
         ['grand-canyon', 1, ['lake-havasu', 'zion']],
         ['santa-fe', 2, ['taos', 'albuquerque']],
         ['taos', 1, ['ruidoso']],
         ['albuquerque', 1, ['white-sands', 'ruidoso', 'tucson']]]),
 dict(id='pacific-northwest', title='Pacific Northwest Flying Trip', h1='Puget Sound to the Columbia Gorge',
  lede='Seven nights in Washington and Oregon: Seattle and the Museum of Flight, the San Juan Islands, Port Townsend, Willamette Valley wine country and Hood River.',
  desc='A seven-night flying trip through Washington and Oregon, with dates, legs, fuel-stop flags and a guide for every stop.',
  wx='Summer is the dry, clear season; the rest of the year brings low ceilings, rain and icing in the mountains. Watch for marine stratus on summer mornings and plan Cascade crossings carefully.',
  regions=['Pacific Northwest'], defaultSeason=[6, 7, 8, 9],
  route=[['seattle', 1, ['leavenworth', 'lake-chelan']],
         ['san-juan-islands', 2, ['port-townsend', 'victoria-bc']],
         ['port-townsend', 1, ['oregon-coast']],
         ['willamette-valley', 2, ['oregon-coast', 'eugene', 'bend-sunriver']],
         ['hood-river', 1, ['walla-walla', 'bend-sunriver', 'crater-lake']]]),
 dict(id='virginia', title='Virginia Flying Trip', h1='Virginia, coast to Blue Ridge',
  lede='Seven nights in Virginia: Colonial Williamsburg, Chincoteague’s wild ponies, Hunt Country wineries, Charlottesville and Monticello, and a Blue Ridge lake.',
  desc='A seven-night flying trip through Virginia, from Williamsburg and the Eastern Shore to the Blue Ridge, with dates, legs, fuel-stop flags and a guide for every stop.',
  wx='Summer haze and afternoon thunderstorms, busy military and Washington-area airspace (brief the restricted areas and the DC SFRA), and mountain turbulence over the Blue Ridge. Spring and fall are the best months; plan a spare day.',
  regions=['Mid-Atlantic'], defaultSeason=[4, 5, 6, 9, 10, 11],
  route=[['williamsburg', 2, ['annapolis', 'st-michaels']],
         ['chincoteague', 1, ['ocean-city', 'st-michaels']],
         ['hunt-country', 1, ['harpers-ferry', 'shenandoah']],
         ['charlottesville', 2, ['shenandoah', 'homestead']],
         ['smith-mountain-lake', 1, ['homestead', 'greenbrier', 'elkins']]]),
 dict(id='upstate-new-york', title='Upstate New York Flying Trip', h1='Upstate New York and the Finger Lakes',
  lede='Seven nights upstate: Cooperstown and the Hall of Fame, Ithaca’s gorges, Belhurst Castle and the Seneca Lake wine trail, the Thousand Islands and Lake Placid.',
  desc='A seven-night flying trip through upstate New York and the Finger Lakes wine country, with dates, legs, fuel-stop flags and a guide for every stop.',
  wx='Summer and early fall are the season; watch for lake-effect showers, morning valley fog, summer thunderstorms and the high terrain of the Adirondacks. Plan a spare day.',
  regions=['Northeast'], defaultSeason=[6, 7, 8, 9, 10],
  route=[['cooperstown', 1, ['hudson-valley', 'saratoga', 'niagara-on-the-lake']],
         ['finger-lakes', 1, ['seneca-lake']],
         ['seneca-lake', 2, ['finger-lakes']],
         ['thousand-islands', 2, ['long-lake-ny', 'quebec-city']],
         ['lake-placid', 1, ['saratoga', 'long-lake-ny']]]),
]
def main():
    js = (ROOT / 'docs/destinations.js').read_text()
    for r in ROUTES:
        for s, n, alts in r['route']:
            for x in [s] + alts:
                assert f'"guide": "{x}/"' in js, (r['id'], x)
        cfg = {k: r[k] for k in ('id', 'route', 'regions', 'season', 'defaultSeason') if k in r}
        html = TPL
        for k, v in [('__TRIP__', json.dumps(cfg, ensure_ascii=False)), ('__TITLE__', r['title']), ('__DESC__', r['desc']), ('__H1__', r['h1']),
                     ('__LEDE__', r['lede']), ('__WX__', r['wx']), ('__SUBJ__', urllib.parse.quote(r['title'])), ('__ID__', r['id'])]:
            html = html.replace(k, v)
        out = ROOT / 'docs/trips' / r['id'] / 'index.html'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html)
        print('wrote', out.relative_to(ROOT))
    return ROUTES
if __name__ == '__main__':
    main()

def index(routes):
    js = (ROOT / 'docs/destinations.js').read_text()
    import re as _re
    s = js[js.index('['):js.rindex(']') + 1]
    D = {d['guide'].strip('/'): d for d in json.loads(s) if d.get('guide')}
    cards = []
    for r in routes:
        first = D[r['route'][0][0]]
        p = first.get('photo') or {}
        img = (p['remote'] + '&w=600&h=450&fit=crop&q=75') if p.get('remote') else ('../assets/destinations/' + p.get('slug', '') + '-480.jpg')
        stops = ' → '.join(_re.sub(r' & .*|,.*', '', D[x[0]]['name']) for x in r['route'])
        nights = sum(x[1] for x in r['route'])
        cards.append(f'<a class="tr-card" href="{r["id"]}/"><img src="{img}" alt="" loading="lazy"><span><b>{r["h1"]}</b><small>{nights} nights · {stops}</small><em>{r["lede"]}</em></span></a>')
    tpl = (ROOT / 'tools/trips/index_template.html').read_text()
    (ROOT / 'docs/trips/index.html').write_text(tpl.replace('__CARDS__', '\n'.join(cards)))
    print('wrote docs/trips/index.html')

if __name__ == '__main__':
    index(ROUTES)
