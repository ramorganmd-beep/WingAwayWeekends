"""Generate docs/charleston/index.html using the Savannah guide's markup and classes."""
import sys



def ext(href, text, sr=None):
    s = f'<span class="sr"> for {sr}</span>' if sr else ''
    return f'<a class="textlink" href="{href}" target="_blank" rel="noopener">{text}{s}</a>'


def card(tag, name, body, href=None, link_text='Official details'):
    link = ext(href, link_text, name) if href else ''
    return f'<article class="card"><div class="tag">{tag}</div><h3>{name}</h3><p>{body}</p>{link}</article>'


def head(num, eyebrow, h2, p):
    return (f'<div class="section-head"><div><span class="eyebrow">{num} / {eyebrow}</span>'
            f'<h2>{h2}</h2></div><p>{p}</p></div>')


def explore(n, title, body, href=None, link_text=None):
    a = f'<a href="{href}" target="_blank" rel="noopener">{link_text}</a>' if href else ''
    return f'<article><span>{n:02d}</span><div><h3>{title}</h3><p>{body}</p>{a}</div></article>'


def day(label, title, items):
    lis = ''.join(f'<li><strong>{t}</strong><p>{p}</p></li>' for t, p in items)
    return f'<article><div class="day-label"><span>{label}</span><h3>{title}</h3></div><ol>{lis}</ol></article>'


ICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' "
        "height='32' rx='7' fill='%23102d40'/%3E%3Cpath d='M4 10l5 13 7-9 7 9 5-13' fill='none' stroke='%23efbd70' "
        "stroke-width='3'/%3E%3C/svg%3E")



SECTIONS = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('explore', 'Explore'), ('spa', 'Spa'),
            ('shopping', 'Shop'), ('wine', 'Wine'), ('breweries', 'Breweries'), ('events', 'Sports & events'),
            ('itinerary', 'Itinerary')]


def page_start(*, slug, name, state, number, description, lede, intro, pills, photo, widths, alt, img_w, img_h,
               caption, airport, nm, flight_time, style, estimate_extra='', nav=None, img_style=''):
    """Shared page head, hero, trip snapshot and section menu for a destination guide."""
    def srcset(ext):
        return ', '.join(f'../assets/destinations/{photo}-{w}.{ext} {w}w' for w in widths)
    nav = nav or SECTIONS
    pills_html = ''.join(f'<span>{p}</span>' for p in pills)
    nav_html = ''.join(f'<a href="#{i}">{t}</a>' for i, t in nav)
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="theme-color" content="#102d40"><meta name="description" content="{description}">'
            f'<title>{name} Couples Getaway | WingAway Weekends</title><link rel="canonical" href="https://wingawayweekends.com/{slug}/">'
            f'<link rel="icon" type="image/svg+xml" href="{ICON}"><link rel="stylesheet" href="../style.css"></head><body>\n'
            f'<a class="skip" href="#main">Skip to destination</a><header><a href="../" class="brand"><span class="mark">W</span><span>WingAway<span class="brand-small">WEEKENDS</span></span></a>'
            f'<span class="header-note">Destination prototype <span>{number:02d}</span></span></header>\n'
            f'<main id="main"><div class="destination"><div class="intro"><span class="eyebrow">{state} · Couples · Two nights</span><h1>{name}</h1>'
            f'<p class="lede">{lede}</p><p>{intro}</p><div class="pills">{pills_html}</div>'
            f'<div class="hero-actions"><a class="button" href="#itinerary">See the weekend itinerary</a><a href="#flight" class="secondary">Flight & arrival details</a></div></div>'
            f'<figure><picture><source type="image/webp" srcset="{srcset("webp")}" sizes="(max-width:800px) 100vw, 50vw">'
            f'<img src="../assets/destinations/{photo}-960.jpg" srcset="{srcset("jpg")}" sizes="(max-width:800px) 100vw, 50vw" alt="{alt}" width="{img_w}" height="{img_h}"{f' style="{img_style}"' if img_style else ''}></picture>'
            f'<figcaption>{caption}</figcaption></figure></div>\n'
            f'<div class="snapshot" aria-label="Trip snapshot"><div><span>YOUR ROUTE</span><strong>KMYR <span class="route-line">to</span> {airport}</strong></div>'
            f'<div><span>STRAIGHT-LINE DISTANCE</span><strong>~{nm} <small>NM</small></strong></div>'
            f'<div><span>ILLUSTRATIVE FLIGHT TIME</span><strong>{flight_time}</strong></div>'
            f'<div><span>WEEKEND STYLE</span><strong>Two nights <small>· {style}</small></strong></div></div>'
            f'<p class="estimate">Time illustration: direct distance at 150 KTAS plus 15 minutes for departure and arrival, matching the discovery page. {estimate_extra}Use ForeFlight for your actual flight plan.</p>\n'
            f'<nav class="jump" aria-label="Destination sections">{nav_html}</nav>')


def page_end(*, number, place, credit_html, note='Several official links could not be opened during research; check each one, and confirm hours, prices and availability directly before booking.'):
    return (f'<div class="prototype-note"><span class="eyebrow">Testing / Destination {number:02d}</span><h3>Draft for review.</h3>'
            f'<p>Research-based selections, not personal-visit endorsements. Researched November 1, 2026. {note}</p>'
            '<p class="note">WingAway Weekends helps you discover the destination. Use ForeFlight and current official aviation information for route, performance, weather, NOTAMs and preflight decisions. Flight planning and PIC responsibility stay with the pilot.</p></div></main>'
            f'<footer><a class="brand" href="#main">WingAway Weekends</a><p>{place} · Couples prototype</p><details><summary>Photo credit</summary>'
            f'<p>{credit_html}</p></details></footer></body></html>')


def fbo(name, line, phone=None, href=None):
    tel = f'<a href="tel:+1{phone.replace("-", "")}">{phone}</a>' if phone else ''
    link = f'<a href="{href}" target="_blank" rel="noopener">FBO details</a>' if href else ''
    return f'<div class="fbo"><div><strong>{name}</strong><p>{line}</p></div>{tel}{link}</div>'


def know(items):
    return '<div class="know-grid">' + ''.join(f'<article><h3>{h}</h3><p>{p}</p></article>' for h, p in items) + '</div>'


def wine_and_flying(extra=''):
    """Reminder for wine-country guides about drinking and flying."""
    return ('<div class="couples wine-fly"><span class="eyebrow">Pilot note / Wine & flying</span><h3>Taste on the non-flying day.</h3>'
            '<p>FAA rules (14 CFR 91.17) require at least 8 hours from bottle to throttle, a blood alcohol below 0.04% and no lingering effects. '
            'Many pilots use 12–24 hours as a personal minimum, since a hangover can impair you long after the legal limit is met. '
            'Plan the tasting day for the middle of the weekend, keep the evening before departure dry, and let a driver or shuttle handle the roads. '
            f'If the pilot wants a full tasting day, add a third night. {extra}</p></div>')
