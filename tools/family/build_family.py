"""Generate docs/family/index.html: the 17 fly-in weekends built around kids.
Ages come from tools/guides/kids.py; photos and coordinates from docs/destinations.js.
Usage (repo root): python3 tools/family/build_family.py
"""
import json, sys, html
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools/guides'))
sys.argv = sys.argv[:1]
from kids import KIDS  # noqa: E402  (kids.py does nothing without file arguments)

GROUPS = [
    ('Theme parks', 'Rides, characters and a park day the kids will talk about for months.', [
        ('orlando', 'Walt Disney World, Universal and Gatorland', 'Year-round', 'Class B nearby; landing fee; summer storms'),
        ('disneyland', 'Disneyland, California Adventure and Knott’s', 'Year-round', 'Short 3,121 ft runway; busy LA airspace'),
        ('carlsbad', 'LEGOLAND and Miniland USA', 'Year-round', 'Landing fee; morning marine layer'),
        ('smoky-mountains', 'Dollywood', 'Spring to fall', 'Mountain terrain; approaches to runway 10 only'),
        ('hershey', 'Hersheypark and the chocolate tour ride', 'Spring to fall', ''),
        ('branson', 'Silver Dollar City', 'Spring to fall', ''),
        ('williamsburg', 'Busch Gardens and Colonial Williamsburg', 'Spring to fall', 'Short 3,204 ft runway; circling approaches only'),
    ]),
    ('Beach & water', 'Sand, waterparks and warm water, with very little to plan.', [
        ('destin', 'Calm, clear water and a dolphin cruise', 'Spring to fall', 'Eglin military airspace nearby'),
        ('wisconsin-dells', 'Indoor waterparks, rain or shine', 'Year-round', ''),
        ('traverse-city', 'The Dune Climb and freshwater beaches', 'Summer', 'Landing fee'),
    ]),
    ('Adventure', 'Bikes, tide pools and mountain air.', [
        ('mackinac', 'No cars: bikes, carriages and a fort', 'Summer', 'No fuel and no FBO; 3,501 ft runway'),
        ('bar-harbor', 'Tide pools and the carriage roads', 'Summer to early fall', 'Landing fee; summer fog'),
        ('colorado-springs', 'The zoo and a train to 14,115 ft', 'Spring to fall', '6,187 ft field: high density altitude'),
    ]),
    ('Explore & learn', 'Rockets, aquariums and history they can touch.', [
        ('space-coast', 'Kennedy Space Center and real rockets', 'Year-round', 'Launch flight restrictions: check TFRs'),
        ('chattanooga', 'The Tennessee Aquarium', 'Spring to fall', ''),
        ('monterey-carmel', 'The Monterey Bay Aquarium and sea otters', 'Year-round', 'Summer fog and low clouds'),
        ('san-antonio', 'River Walk boats and the DoSeum', 'Fall to spring', ''),
    ]),
]
s = (ROOT / 'docs/destinations.js').read_text(); D = {d['guide'].strip('/'): d for d in json.loads(s[s.index('['):s.rindex(']') + 1]) if d.get('guide')}
e = html.escape


def img(d):
    p = d['photo']
    if p.get('remote'):
        return p['remote'] + '&w=640&h=480&fit=crop&fm=jpg&q=75'
    return '../assets/destinations/' + p['slug'] + '-480.jpg'


def card(slug, hi, season, warn):
    d = D[slug]; k = KIDS[slug]
    w = f'<i>✈ {e(warn)}</i>' if warn else ''
    return (f'<a class="fm-card" href="../{slug}/" data-lat="{d["lat"]}" data-lon="{d["lon"]}" data-apt="{d["airport"]}">'
            f'<img src="{e(img(d))}" alt="{e(d["photo"].get("alt", d["name"]))}" loading="lazy">'
            f'<span><small>{e(d["state"])} · {d["airport"]}<em class="fm-time"></em></small><b>{e(d["name"])}</b>'
            f'<strong>{e(hi)}</strong><u>Best ages {e(k["ages"])} · {e(season)}</u>{w}</span></a>')


groups = ''.join(f'<section class="fm-group"><h2>{e(t)}</h2><p class="fm-sub">{e(sub)}</p><div class="fm-grid">'
                 + ''.join(card(*c) for c in cards) + '</div></section>' for t, sub, cards in GROUPS)
n = sum(len(c) for _, _, c in GROUPS)
page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#102d40"><meta name="description" content="{n} fly-in weekends built around kids: theme parks, beaches and real rockets, each with the airport facts a pilot parent needs.">
<title>Family Fly-Ins | WingAway Weekends</title><link rel="canonical" href="https://wingawayweekends.com/family/"><link rel="icon" type="image/png" href="/favicon-32.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="stylesheet" href="../style.css">
<meta property="og:title" content="Family Fly-Ins | WingAway Weekends"><meta property="og:description" content="{n} fly-in weekends built around kids, with the airport facts a pilot parent needs."><meta property="og:image" content="https://wingawayweekends.com/assets/share-wingaway.jpg"><meta name="twitter:card" content="summary_large_image">
<style>
.fm{{max-width:1080px;padding-top:52px;padding-bottom:60px}}.fm h1{{margin:10px 0 12px}}.fm-home{{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin:18px 0 6px;font-size:15px}}
.fm-home input{{width:110px;padding:9px 10px;border:1px solid #bfc9cb;border-radius:6px;font:inherit;text-transform:uppercase}}.fm-home span{{color:#647784}}
.fm-group{{margin:34px 0 0}}.fm-group h2{{margin:0 0 4px}}.fm-sub{{margin:0 0 14px;color:#51666f}}
.fm-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:16px}}
.fm-card{{display:flex;flex-direction:column;background:#fff;border:1px solid #dbe3e9;border-radius:3px;overflow:hidden;color:#102d40;text-decoration:none}}.fm-card:hover{{border-color:#ba7d2f}}
.fm-card img{{width:100%;aspect-ratio:4/3;object-fit:cover;display:block;background:#eef2f4}}.fm-card span{{padding:12px 14px 16px;display:flex;flex-direction:column;gap:5px}}
.fm-card small{{font-size:12.5px;color:#8a571c;font-weight:700}}.fm-card em{{font-style:normal}}.fm-card b{{font-size:19px}}.fm-card strong{{font-weight:600;font-size:15px}}
.fm-card u{{text-decoration:none;font-size:14px;color:#33475a}}.fm-card i{{font-style:normal;font-size:13.5px;color:#7a4a12;background:#fbf6ec;border-radius:3px;padding:4px 7px;margin-top:2px}}
.fm-more{{margin:40px 0 0;padding:18px 20px;background:#eef5f9;border:1px solid #c9dde8;border-radius:3px}}
</style></head><body>
<header><a href="../" class="brand"><span class="mark">W</span><span>WingAway<span class="brand-small">WEEKENDS</span></span></a><span class="header-right" style="display:flex;flex-wrap:wrap;justify-content:flex-end;gap:6px 16px"><a class="header-link" href="../map/">Map</a><a class="header-link" href="../wx/">Weather</a><a class="header-link" href="../trips/">Trips</a></span></header>
<main class="fm"><span class="eyebrow">Flying with children</span><h1>Family fly-ins</h1>
<p class="lede">{n} fly-in weekends built around the kids: theme parks, beaches and real rockets, each with the airport facts a pilot parent needs.</p>
<p>Every guide has a <b>Best for kids</b> box with the best ages, the top three things to do and any airport limits. On the home page, switch on <a href="../?kids=1">Traveling with kids</a> to see all of our family-friendly guides.</p>
<label class="fm-home">Flight times from <input id="fm-home" maxlength="4" autocomplete="off" spellcheck="false" placeholder="KMYR" aria-label="Home airport"><span id="fm-note">Enter your home airport to sort each group by flight time.</span></label>
{groups}
<div class="fm-more"><b>Want to fly in with other pilot families?</b> We are gauging interest in WingAway family weekends at some of these destinations. <a href="mailto:hello@wingawayweekends.com?subject=Family%20fly-in%20interest">Tell us which one</a>.</div>
<p class="estimate" style="margin-top:22px">Flight times are illustrative: straight-line distance at 150 KTAS plus 15 minutes. Airport notes are for planning; check the chart supplement, NOTAMs and your own minimums.</p>
</main>
<footer><a class="brand" href="../">WingAway Weekends</a><p class="feedback"><strong>Help us improve and grow.</strong> <a href="mailto:hello@wingawayweekends.com?subject=WingAway%20feedback%3A%20Family%20fly-ins">Suggest a family destination</a></p></footer>
<script src="../airports-us.js?v=202611121500"></script>
<script>(function(){{var A=window.WINGAWAY_AIRPORTS||[],I={{}};A.forEach(function(a){{I[a[0]]=a;if(a[1])I[a[1]]=a;if(/^K[A-Z0-9]{{3}}$/.test(a[0])&&!I[a[0].slice(1)])I[a[0].slice(1)]=a}});
var inp=document.getElementById('fm-home'),note=document.getElementById('fm-note');
function nm(a,b,c,d){{var r=Math.PI/180,x=Math.sin((c-a)*r/2),y=Math.sin((d-b)*r/2);return 3440.065*2*Math.asin(Math.sqrt(x*x+Math.cos(a*r)*Math.cos(c*r)*y*y))}}
function go(){{var h=I[inp.value.trim().toUpperCase()];document.querySelectorAll('.fm-grid').forEach(function(g){{var cs=[].slice.call(g.children);cs.forEach(function(c){{var t=c.querySelector('.fm-time');if(!h){{t.textContent='';c.dataset.m=0;return}}
var m=Math.round(nm(h[5],h[6],+c.dataset.lat,+c.dataset.lon)/150*60+15);c.dataset.m=m;t.textContent=' · ~'+(m>=60?Math.floor(m/60)+' hr '+(m%60?m%60+' min':''):m+' min')}});
if(h)cs.sort(function(a,b){{return a.dataset.m-b.dataset.m}}).forEach(function(c){{g.append(c)}})}});
if(h){{note.textContent='Closest first in each group.';try{{localStorage.setItem('wingaway-home',h[0])}}catch(e){{}}}}}}
try{{inp.value=localStorage.getItem('wingaway-home')||''}}catch(e){{}}inp.addEventListener('input',go);go()}})();</script>
</body></html>
'''
(ROOT / 'docs/family').mkdir(exist_ok=True)
(ROOT / 'docs/family/index.html').write_text(page)
print('family page:', n, 'destinations')
