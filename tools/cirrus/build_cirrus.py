"""Build docs/cirrus/index.html: a preview page for Cirrus owners (noindex, not in the sitemap).
Usage: python3 tools/cirrus/build_cirrus.py
Getaway cards are generated from docs/destinations.js so names, runways and photos stay in sync."""
import json, html
from pathlib import Path
root = Path(__file__).resolve().parents[2]
src = (root / 'docs/destinations.js').read_text()
dest = json.loads(src[src.index('[', src.index('=')):src.rindex(']') + 1])
by_guide = {d['guide']: d for d in dest}

GETAWAYS = ['bar-harbor/', 'charleston/', 'key-west/', 'sedona/', 'jackson-hole/', 'santa-barbara/']
TRIPS = [('northeast', 'The Northeast in a week', 'Cape May, Newport, Nantucket, Bar Harbor and Stowe'),
         ('lowcountry', 'Carolina & Georgia coast', 'Seven nights down the Carolina and Georgia coast'),
         ('florida', 'Florida loop', 'St. Augustine to Key West and back'),
         ('rockies', 'Rocky Mountains', 'Seven nights of mountain flying in Colorado and Utah'),
         ('california', 'California coast', 'San Diego to wine country'),
         ('pacific-northwest', 'Pacific Northwest', 'Seven nights through Washington and Oregon')]
MODELS = [('sr20', 'SR20'), ('sr22', 'SR22'), ('sr22t', 'SR22T'), ('sf50', 'Vision Jet')]
e = html.escape

def photo(d, w=480):
    p = d['photo']
    if p.get('remote'):
        return f"{p['remote']}&w={w}&h={w * 3 // 4}&fit=crop&fm=jpg&q=80"
    return f"../assets/destinations/{p['slug']}-{w}.jpg"

cards = []
for g in GETAWAYS:
    d = by_guide[g]
    rwy = f" · {d['rwy']:,} ft rwy" if d.get('rwy') else ''
    alt = d['photo'].get('alt') or d['name']
    cards.append(f'<a class="cx-card" href="../{g}"><img src="{e(photo(d))}" alt="{e(alt)}" loading="lazy" width="480" height="360">'
                 f'<span class="cx-body"><strong>{e(d["name"])}</strong><span class="cx-meta">{e(d["airport"])}{rwy}</span>'
                 f'<span class="cx-desc">{e(d["desc"])}</span></span></a>')
trips = ''.join(f'<a class="cx-trip" href="../trips/{t}/"><strong>{e(n)}</strong><span>{e(s)}</span></a>' for t, n, s in TRIPS)
models = ''.join(f'<button type="button" class="cx-model" data-id="{i}">{e(n)}</button>' for i, n in MODELS)

page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#102d40">
<meta name="robots" content="noindex,nofollow"><meta name="description" content="A preview of a WingAway Weekends page for Cirrus owners: aircraft profiles, a getaway collection and a sample group fly-out.">
<title>For Cirrus Owners (Preview) | WingAway Weekends</title><link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%23102d40'/%3E%3Cpath d='M4 10l5 13 7-9 7 9 5-13' fill='none' stroke='%23efbd70' stroke-width='3'/%3E%3C/svg%3E"><link rel="stylesheet" href="../style.css">
<style>
.cx{{max-width:1080px;padding:44px 0 70px}}.cx h1{{margin:10px 0 12px}}.cx h2{{margin:44px 0 6px}}.cx .sub{{margin:0 0 16px;color:#51666f}}
.cx-preview{{display:inline-block;background:#fdf3e1;border:1px solid #efbd70;color:#6b4513;font-size:13px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;padding:5px 10px;border-radius:3px}}
.cx-models{{display:flex;flex-wrap:wrap;gap:10px;margin:12px 0}}.cx-model{{font:inherit;font-weight:700;font-size:16px;padding:12px 20px;border:1px solid #102d40;background:#fff;color:#102d40;border-radius:3px;cursor:pointer}}
.cx-model[aria-pressed="true"]{{background:#102d40;color:#fff}}.cx-status{{min-height:24px;color:#33475a}}.cx-status a{{font-weight:700}}
.cx-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:18px}}
.cx-card{{display:flex;flex-direction:column;background:#fff;border:1px solid #dbe3e9;border-radius:3px;overflow:hidden;color:inherit;text-decoration:none}}
.cx-card img{{width:100%;height:auto;aspect-ratio:4/3;object-fit:cover;display:block}}.cx-body{{display:flex;flex-direction:column;gap:6px;padding:14px 16px 18px}}
.cx-body strong{{font-family:Georgia,serif;font-size:21px;font-weight:400;color:#102d40}}.cx-meta{{font-size:13px;color:#51666f}}.cx-desc{{font-size:15px;line-height:1.5;color:#33475a}}
.cx-trips{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px}}.cx-trip{{display:flex;flex-direction:column;gap:4px;padding:16px 18px;background:#fff;border:1px solid #dbe3e9;border-left:4px solid #efbd70;border-radius:3px;text-decoration:none;color:#33475a}}
.cx-trip strong{{color:#102d40;font-size:17px}}
.cx-fly{{margin-top:14px;background:#102d40;color:#f6f4ef;border-radius:3px;padding:26px 28px;display:grid;grid-template-columns:1.3fr 1fr;gap:24px}}
.cx-fly h3{{margin:4px 0 8px;font-family:Georgia,serif;font-weight:400;font-size:28px;color:#fff}}.cx-fly p{{margin:0 0 10px;line-height:1.55;color:#d5dee4}}.cx-fly ul{{margin:0;padding-left:20px;line-height:1.7;color:#d5dee4}}
.cx-fly .tag{{font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#efbd70}}.cx-fly a{{color:#efbd70}}
.cx-signup{{margin-top:14px;font:inherit;font-weight:700;padding:12px 18px;border:0;border-radius:3px;background:#efbd70;color:#102d40;opacity:.65;cursor:not-allowed}}
.cx-note{{margin-top:40px;font-size:13px;color:#647784;border-top:1px solid #dbe3e9;padding-top:14px}}
@media(max-width:760px){{.cx-fly{{grid-template-columns:1fr}}}}
</style></head><body>
<a class="skip" href="#main">Skip to content</a><header><a href="../" class="brand"><span class="mark">W</span><span>WingAway<span class="brand-small">WEEKENDS</span></span></a><span class="header-right" style="display:flex;gap:18px"><a class="header-link" href="../trips/">Trips</a><a class="header-link" href="../map/">Map</a></span></header>
<main id="main"><div class="cx">
<span class="cx-preview">Preview · For discussion</span>
<h1>Where to fly your Cirrus next</h1>
<p class="lede">Weekend getaways and week-long trips chosen for Cirrus owners, with flight time and fuel worked out for your airplane.</p>

<h2>1. Pick your Cirrus</h2>
<p class="sub">Every guide and trip then shows time and fuel for your model. You can fine-tune the numbers on the homepage.</p>
<div class="cx-models" role="group" aria-label="Choose your Cirrus model">{models}</div>
<p class="cx-status" id="cx-status" aria-live="polite"></p>

<h2>2. Weekend getaways</h2>
<p class="sub">Six favorites, coast to coast. Each guide covers the FBO, where to stay and eat, and a sample weekend.</p>
<div class="cx-grid">{''.join(cards)}</div>

<h2>3. Week-long trips</h2>
<p class="sub">Pick your dates; the planner lays out every leg with fuel-stop suggestions for your airplane.</p>
<div class="cx-trips">{trips}</div>

<h2>4. Fly together</h2>
<div class="cx-fly">
<div><span class="tag">Sample fly-out · example only</span><h3>The Great Smoky Mountains, a group weekend</h3>
<p>A short hop for most of the Southeast and Midwest. Fly in on Friday to Gatlinburg–Pigeon Forge (KGKT), or to Knoxville (KTYS), home of the Cirrus Vision Center, 23 nm away. Saturday in the park: Cades Cove at sunrise, a picnic and a waterfall hike, then dinner together in Townsend.</p>
<p><a href="../smoky-mountains/">See the Great Smoky Mountains guide</a> · Nearby: <a href="../asheville/">Asheville</a>, <a href="../highlands-cashiers/">Highlands–Cashiers</a></p>
<button class="cx-signup" type="button" disabled>Sign-up opens when dates are announced</button></div>
<ul><li>Dates, host and event details to be set</li><li>Arrival at KGKT (5,506 ft) or KTYS</li><li>An optional stop at the Cirrus Vision Center, if Cirrus hosts</li><li>Route and fuel options for each Cirrus model</li><li>Lodging and dining picks from the guide</li><li>See who’s flying in before you go</li></ul>
</div>

<p class="cx-note">This page is a preview prepared for discussion. WingAway Weekends is independent and is not affiliated with or endorsed by Cirrus Aircraft. Times and fuel are planning estimates, not flight plans.</p>
</div></main>
<footer><a class="brand" href="../">WingAway Weekends</a><p>A short flight. A slower weekend.</p></footer>
<script src="../aircraft.js?v=202611071530"></script>
<script>
(function(){{var A=window.WingAwayAircraft,st=document.getElementById('cx-status'),bs=document.querySelectorAll('.cx-model');
function mark(id){{bs.forEach(function(b){{b.setAttribute('aria-pressed',b.dataset.id===id?'true':'false')}})}}
var cur=A&&A.load();if(cur)mark(cur.id);
bs.forEach(function(b){{b.addEventListener('click',function(){{var p=A.PRESETS.filter(function(x){{return x.id===b.dataset.id}})[0];if(!p)return;A.save(p);A.saveGear('land');mark(p.id);
st.innerHTML='Saved: '+p.label+', '+p.tas+' kt, '+p.gph+' gal/hr. <a href="../">See getaways from your home airport →</a>'}})}})}})();
</script>
<script src="/contact.js" defer></script></body></html>'''
(root / 'docs/cirrus/index.html').write_text(page)
print('wrote docs/cirrus/index.html')
