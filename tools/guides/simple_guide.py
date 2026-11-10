"""Shared builder for data-driven guides (Northeast and later regions).

Each build_<slug>.py defines a GUIDE dict and calls build(GUIDE, out_path).
Sections follow the standard guide layout: flight, stay, eat, explore (+ optional spa),
events, itinerary, good to know. Cards are (tag, name, body[, url[, link text]]).
"""
import json
from pathlib import Path
from guide_helpers import card, head, explore, day, page_start, page_end, fbo, know

PHOTOS = json.load(open(Path(__file__).with_name('photos.json')))


def _cards(items):
    return ''.join(card(*c) for c in items)


def _water(w):
    """Optional seaplane-access block: {'base': (name, line, phone), 'lanes': str, 'notes': [...]}."""
    if not w:
        return ''
    out = ('<p class="note water-toggle" data-water-toggle hidden><button type="button" class="textlink">Flying a floatplane or amphibian? Show seaplane access</button></p>'
           '<div class="water-block" data-water><h3 class="water-head">Seaplane access</h3>' + fbo(*w['base']))
    if w.get('lanes'):
        out += f'<p class="note"><strong>Water lanes:</strong> {w["lanes"]}</p>'
    out += ''.join(f'<p class="note">{n}</p>' for n in w.get('notes', []))
    return out + '</div>'


def build(g, out):
    photo = PHOTOS[g['slug']]
    nav = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('explore', 'Explore')]
    if g.get('spa'):
        nav.append(('spa', 'Spa'))
    nav += [('events', 'Events'), ('itinerary', 'Itinerary')]
    reviewed = g.get('reviewed')
    P = [page_start(slug=g['slug'], name=g['name'], state=g['state'], number=g['number'], reviewed=reviewed,
                    description=g['description'], lede=g['lede'], intro=g['intro'], pills=g['pills'],
                    photo=photo['slug'], widths=photo['widths'], alt=photo['alt'], img_w=photo['w'], img_h=photo['h'],
                    caption=photo['caption'], airport=g['airport'], nm=g['nm'], flight_time=g['flight_time'],
                    style=g['style'], nav=nav)]
    f = g['flight']
    P.append('<section id="flight">' + head('01', 'Aviation & getting around', f['title'], f['intro']) +
             '<div class="arrival-grid"><div class="arrival-main"><h3>The FBO</h3>' +
             fbo(*f['fbo']) + ''.join(f'<p class="note">{n}</p>' for n in f['notes']) + _water(f.get('water')) + '</div>'
             f'<aside><span class="eyebrow">Getting around</span><h3>{f["around_title"]}</h3><p>{f["around"]}</p></aside></div></section>')
    s = g['stay']
    P.append('<section id="stay">' + head('02', 'Where to stay', s['title'], s['intro']) +
             '<div class="grid three">' + _cards(s['cards']) + '</div></section>')
    e = g['eat']
    P.append('<section id="eat">' + head('03', 'Where to eat', e['title'], e['intro']) +
             f'<div class="grid {"four" if len(e["cards"]) == 4 else "three"}">' + _cards(e['cards']) + '</div></section>')
    x = g['explore']
    body = '<section id="explore">' + head('04', 'Things to do', x['title'], x['intro']) + '<div class="explore-list">' + \
        ''.join(explore(i, *item) for i, item in enumerate(x['items'], 1)) + '</div>'
    if g.get('spa'):
        sp = g['spa']
        body += (f'<div id="spa" class="couples"><span class="eyebrow">Optional / Spa & relaxation</span><h3>{sp["title"]} · Time for two</h3>'
                 f'<p>{sp["body"]}</p>'
                 '<p><strong>Booking:</strong> Ask about couples treatments, access for non-guests, current pricing and cancellation policy. '
                 'No prices are shown here, and no appointment has been booked.</p></div>')
    P.append(body + '</section>')
    ev = g['events']
    P.append('<section id="events">' + head('05', 'What’s happening', ev.get('title', 'Sometimes the season is the reason to fly.'),
                                            'This prototype links to the local visitor site. It does not yet match events to your travel dates.') +
             '<div class="grid three">' + _cards(ev['cards']) + '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3>'
             '<p>Check the local calendar when choosing a weekend, and confirm dates and tickets with the organizer.</p></div>'
             f'<a class="button" href="{ev["url"]}" target="_blank" rel="noopener">{ev["button"]}</a></div></section>')
    it = g['itinerary']
    P.append('<section id="itinerary">' + head('06', 'Suggested itinerary', 'Friday in. Sunday home.', it['intro']) +
             '<div class="days">' + ''.join(day(*d) for d in it['days']) + '</div></section>')
    P.append('<section id="know">' + head('07', 'Good to know', 'Keep the weekend easy to change.',
                                          'These details make the difference between an appealing list and a usable getaway.') +
             know(g['know']) + '</section>')
    P.append(page_end(number=g['number'], place=g['place'], reviewed=reviewed,
                      note='Confirm hours, prices and availability directly with each place before booking.',
                      credit_html=photo['credit_html'], **({'researched': g['researched']} if g.get('researched') else {})))
    Path(out).write_text('\n'.join(P))
