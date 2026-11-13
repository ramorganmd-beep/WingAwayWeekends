"""Generate docs/charleston/index.html using the Savannah guide's markup and classes."""
import sys

OUT = sys.argv[1]


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

parts = []
parts.append(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#102d40"><meta name="description" content="A curated two-night Charleston getaway for GA pilots and their partners, from KMYR to KCHS. Hotels, dining, Patriots Point, the harbor and a flexible weekend itinerary."><title>Charleston Couples Getaway | WingAway Weekends</title><link rel="canonical" href="https://wingawayweekends.com/charleston/"><link rel="icon" type="image/svg+xml" href="{ICON}"><link rel="stylesheet" href="../style.css"></head><body>
<a class="skip" href="#main">Skip to destination</a><header><a href="../" class="brand"><span class="mark">W</span><span>WingAway<span class="brand-small">WEEKENDS</span></span></a><span class="header-note">Destination guide <span>02</span></span></header>
<main id="main"><div class="destination"><div class="intro"><span class="eyebrow">South Carolina · Couples · Two nights</span><h1>Charleston</h1><p class="lede">A short flight. A whole other pace.</p><p>Cobblestones, pastel row houses and some of the South’s best restaurants, with a harbor full of history and an aircraft carrier to explore. Stay on the peninsula and let the weekend unfold on foot.</p><div class="pills"><span>Historic streets</span><span>Dining</span><span>Harbor & aviation history</span></div><div class="hero-actions"><a class="button" href="#itinerary">See the weekend itinerary</a><a href="#flight" class="secondary">Flight & arrival details</a></div></div><figure><picture><source type="image/webp" srcset="../assets/destinations/charleston-480.webp 480w, ../assets/destinations/charleston-960.webp 960w" sizes="(max-width:800px) 100vw, 50vw"><img src="../assets/destinations/charleston-960.jpg" srcset="../assets/destinations/charleston-480.jpg 480w, ../assets/destinations/charleston-960.jpg 960w" sizes="(max-width:800px) 100vw, 50vw" alt="Pastel historic houses on Rainbow Row in Charleston" width="960" height="720"></picture><figcaption>Rainbow Row · An easy walk from the Battery</figcaption></figure></div>
<div class="snapshot" aria-label="Trip snapshot"><div><span>YOUR ROUTE</span><strong>KMYR <span class="route-line">to</span> KCHS</strong></div><div><span>STRAIGHT-LINE DISTANCE</span><strong>~73 <small>NM</small></strong></div><div><span>ILLUSTRATIVE FLIGHT TIME</span><strong>~45 <small>min</small></strong></div><div><span>WEEKEND STYLE</span><strong>Two nights <small>· Uber + walks</small></strong></div></div><p class="estimate">Time illustration: direct distance at 150 KTAS plus 15 minutes for departure and arrival, matching the discovery page. Use ForeFlight for your actual flight plan.</p>
<nav class="jump" aria-label="Destination sections"><a href="#flight">Fly & arrive</a><a href="#stay">Stay</a><a href="#eat">Eat</a><a href="#explore">Explore</a><a href="#spa">Spa</a><a href="#shopping">Shop</a><a href="#wine">Wine</a><a href="#breweries">Breweries</a><a href="#events">Sports & events</a><a href="#itinerary">Itinerary</a></nav>''')

# 01 Flight
parts.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Land, then settle in.',
    'KCHS is the selected arrival airport. It is a joint civil–military field shared with Joint Base Charleston; general aviation is on the east side. Compare the total FBO cost before choosing.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>Two FBOs to compare</h3>'
    '<div class="fbo"><div><strong>Atlantic Aviation</strong><p>6060 S. Aviation Ave., Suite 99, North Charleston, SC 29406</p></div><a href="tel:+18437467600">843-746-7600</a><a href="https://www.atlanticaviation.com/location/CHS" target="_blank" rel="noopener">FBO details</a></div>'
    '<div class="fbo"><div><strong>Signature Aviation</strong><p>5875 S. Aviation Ave., North Charleston, SC 29406</p></div><a href="tel:+18434149200">843-414-9200</a><a href="https://www.signatureaviation.com/locations/CHS" target="_blank" rel="noopener">FBO details</a></div>'
    '<p class="note">Ask each for 100LL pricing, handling or facility fees, two-night parking, minimum fuel for fee waivers and after-hours arrangements. No live fuel price or parking quote is shown. Expect military traffic and follow current NOTAMs and the Chart Supplement.</p>'
    '<p class="note"><strong>Alternative:</strong> Charleston Executive (KJZI) on Johns Island is quieter and closer to Kiawah, but a longer ride to the historic district.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>Uber in. Walk the peninsula.</h3><p>The historic district is roughly 12 miles from the airport, typically a 20–30 minute ride depending on traffic. Confirm rideshare pickup at your FBO entrance.</p><p>Once downtown, most of this guide is walkable. Patriots Point is across the harbor in Mount Pleasant: a short ride, or the Fort Sumter ferry links it with downtown’s Liberty Square.</p></aside></div></section>')

# 02 Stay
parts.append('<section id="stay">' + head('02', 'Where to stay', 'Choose your kind of weekend.',
    'Three different stays, rather than three versions of the same hotel. Rates and availability need travel dates.') +
    '<div class="grid three">' +
    card('Historic warehouse · Suites', 'The Ansonborough',
         'Formerly the Ansonborough Inn: a converted historic warehouse at 21 Hasell Street, reopened in 2024 after a top-to-bottom renovation. Roomy suites, a short walk from the City Market, King Street and the waterfront. Call <a href="tel:+18437231655">843-723-1655</a> or book on its website; confirm room type and parking.',
         'https://www.theansonborough.com/') +
    card('Grand mansion · Romantic splurge', 'Wentworth Mansion',
         'An 1886 mansion turned inn, with period rooms, a cupola view over the city and on-site dining. It sits on the upper part of the peninsula, so plan a short ride or longer walk to the waterfront.',
         'https://www.wentworthmansion.com/') +
    card('French Quarter · Steps from the water', 'The Vendue',
         'An art-filled boutique hotel near Waterfront Park, with a rooftop bar that works well for a sunset drink. The most walkable of the three for the harbor, the Battery and Rainbow Row. Check rooftop hours for your dates.',
         'https://www.thevendue.com/') +
    '</div><h3 class="subhead">Luxury alternatives</h3><div class="grid three">' +
    card('Grand hotel · Spa', 'The Charleston Place',
         'The city’s landmark luxury hotel on Meeting Street, steps from King Street and the City Market, with the full-service spa featured below. Ideal if you want the spa on site.',
         'https://www.charlestonplace.com/') +
    card('Marion Square · Rooftop', 'Hotel Bennett',
         'A polished luxury hotel overlooking Marion Square on upper King Street, with a rooftop bar, a spa and an elegant champagne bar. Great for a King Street shopping weekend.',
         'https://www.hotelbennett.com/') +
    card('Harborfront · New in 2026', 'The Cooper',
         'Charleston’s first luxury waterfront hotel, opened in spring 2026 on Concord Street beside Waterfront Park and the Pineapple Fountain. Harbor views, a full-service spa, three restaurants and its own marina with sunset yacht cruises. A top-end splurge.',
         'https://www.thecooper.com/') +
    '</div></section>')

# 03 Eat
parts.append('<section id="eat">' + head('03', 'Where to eat', 'Two dinners, a happy hour and brunch.',
    'Charleston’s best tables book up, especially Friday and Saturday. Reserve your anchor dinner first.') +
    '<div class="grid four">' +
    card('Friday dinner · Reserve ahead', 'FIG',
         'A long-running Charleston favorite for seasonal, ingredient-driven cooking, on Meeting Street. Make it your anchor reservation and keep the first afternoon flexible in case the flight runs late.',
         'https://www.eatatfig.com/') +
    card('Afternoon happy hour · Oysters', 'Rappahannock Oyster Bar',
         'From the Virginia family that farms Rappahannock River oysters: a lively raw bar at 701 East Bay Street, open daily from 11 AM. Perfect for oysters and a drink before the sunset sail. Check current happy-hour times; call <a href="tel:+18435764693">843-576-4693</a>.',
         'https://www.rroysters.com/restaurants/rappoysterbarchs') +
    card('Saturday dinner · Late & intimate', 'Chez Nous',
         'A tiny restaurant in a cottage at 6 Payne Court, with a handwritten menu that changes every day: two starters, two mains and two desserts, French- and Spanish-leaning. Book a later table after the sail. Only a handful of tables, so call <a href="tel:+18435793060">843-579-3060</a> early. Listed dinner hours run Tuesday–Sunday; confirm for your date.',
         'https://www.cheznouschs.com/') +
    card('Sunday brunch · Southern classic', 'Husk',
         'Southern cooking in a restored Victorian house on Queen Street, close to the historic core. Confirm brunch days and hours for your date before planning around it.',
         'https://www.huskrestaurant.com/') +
    '</div><details class="pending"><summary>Alternative dinner: Halls Chophouse</summary><p>A polished King Street steakhouse with a strong local reputation. Swap it in for Friday or Saturday if you want a classic steak dinner.</p><div class="more"><a href="https://www.hallschophouse.com/" target="_blank" rel="noopener">Halls Chophouse official details</a></div></details></section>')

# 04 Explore
parts.append('<section id="explore">' + head('04', 'Things to do', 'Walk the old city. Climb aboard a carrier.',
    'Choose a few memorable experiences; you do not need to fit every attraction into one weekend.') +
    '<div class="explore-list">' +
    explore(1, 'King Street shopping',
            'Charleston’s main shopping street, best walked in sections: antiques, galleries and fine jewelry on Lower King, boutiques and familiar names in the middle, and design shops and restaurants on Upper King. Plan an unhurried afternoon.') +
    explore(2, 'The Battery, Waterfront Park & Rainbow Row',
            'The classic Charleston walk: the Pineapple Fountain in Waterfront Park, the pastel houses of Rainbow Row on East Bay Street, then the harbor-side promenade at the Battery. Free, flexible and best in the morning or toward sunset.') +
    explore(3, 'Patriots Point & the USS Yorktown',
            'The pilot’s pick. Admission covers the aircraft carrier USS Yorktown with its collection of historic aircraft, the destroyer USS Laffey, the Vietnam Experience and the Medal of Honor Museum. The museum lists daily hours of 10 AM–5 PM with the ticket office closing at 4 PM; it occasionally closes for events, so check the news page before you go. Allow at least two to three hours.',
            'https://www.patriotspoint.org/', 'Patriots Point visitor information') +
    explore(4, 'Fort Sumter',
            'Where the Civil War began, reached only by the park’s official ferry, Fort Sumter Tours. Boats leave from Liberty Square downtown and from Patriots Point; the round trip takes about 2¼ hours, including roughly an hour at the fort. Leaving from Patriots Point pairs naturally with the Yorktown. Weather and tides can affect departures.',
            'https://www.nps.gov/fosu/faqs.htm', 'National Park Service visitor FAQ') +
    explore(5, 'A foodie walking tour',
            'About two and a half hours of tastings and stories with a local guide, a great first-day introduction to the city’s food. Our pick is Bulldog Tours, a long-running, well-reviewed Charleston company whose food tour covers grits, she-crab soup and barbecue. Book ahead and check current prices and times.',
            'https://bulldogtours.com/tours/food', 'Bulldog Tours food walking tour') +
    explore(6, 'Evening carriage ride',
            'Clip-clop through the old walled city as the gas lamps come on. Palmetto Carriage Works and Old South Carriage Co. both run early-evening tours (listed around 5:30–8 PM), including private rides for two and a haunted-history option. Evening tours often sell out, so book ahead; carriages pause in extreme heat.',
            'https://palmettocarriage.com/', 'Palmetto Carriage Works') +
    '</div><h3 class="subhead">One water outing is enough</h3><div class="grid three">' +
    card('Sunset sail · Tall ship', 'Schooner Pride',
         'A two-hour sail on an 84-foot, three-masted schooner from Aquarium Wharf, timed for sunset, past Fort Sumter, the Yorktown and the Ravenel Bridge. Lightly narrated; drinks available on board. Confirm the current schedule and price.',
         'https://charleston.com/schooner-pride') +
    card('History by boat', 'Fort Sumter Tours',
         'If Fort Sumter is on your list, this counts as your water outing. Book the departure point that fits your day: Liberty Square or Patriots Point.',
         'https://www.fortsumtertours.com/tours/fort-sumter-tour/') +
    '</div>')

parts.append('<div id="spa" class="couples"><span class="eyebrow">Optional / Spa & relaxation</span><h3>The Spa at The Charleston Place · Time for two</h3>'
    '<p>A full-service hotel spa at 205 Meeting Street, in the middle of the historic district, with couples treatment rooms and a relaxation lounge. Treatments are open to visitors as well as hotel guests.</p>'
    '<p><strong>Booking:</strong> Call <a href="tel:+18437514019">843-751-4019</a> to ask about couples massages, current pricing, gratuity, cancellation policy and Saturday availability. No prices are shown here because they change; no appointment has been booked.</p>'
    '<p>Optional Saturday afternoon, between Patriots Point and dinner, if timing allows.</p>'
    '<a href="https://www.charlestonplace.com/spa-wellness" target="_blank" rel="noopener">Spa details</a></div></section>')

# 05 Shopping
parts.append('<section id="shopping">' + head('05', 'Shopping & boutiques', 'Bring home something with a story.',
    'King Street is the spine: antiques and galleries on Lower King, fashion and familiar names in the middle, design and dining on Upper King.') +
    '<div class="grid three">' +
    card('Historic shopping street', 'King Street',
         'Walk it in sections rather than end to end. Lower King, below Market Street, suits antiques and fine jewelry; middle King has boutiques and well-known brands; Upper King leans toward design shops and restaurants.') +
    card('Market stalls · Local crafts', 'Charleston City Market',
         'A favorite: one of the country’s oldest public markets, four blocks of open market halls with more than 300 vendors. Many sell what they make: local lotions and soaps, jewelry, art and crafts. Buy sweetgrass baskets from the weavers themselves. Open daily; ask about its evening night market for your dates.') +
    card('Fine jewelry · Since 1919', 'Croghan’s Jewel Box',
         'A family-owned King Street jeweler and a Charleston institution for estate pieces and gifts. A memorable stop on a couples weekend.',
         'https://www.croghansjewelbox.com/') +
    '</div></section>')

# 06 Wine
parts.append('<section id="wine">' + head('06', 'Wine & wine experiences', 'A glass, and no hurry.',
    'For a two-night weekend, wine bars beat a vineyard excursion.') +
    '<div class="grid three">' +
    card('Upper King · Wine shop & bar', 'Graft Wine Shop',
         'A wine shop and bar at 700B King Street, with a relaxed, music-forward feel. Good for a glass on a King Street shopping afternoon.',
         'https://www.graftchs.com/') +
    card('Lower King · Wine & cheese bar', 'Bin 152',
         'An intimate wine and cheese bar on lower King Street, one of the city’s most respected wine lists (a star in the 2025 World’s Best Wine List Awards). Perfect for a quiet glass after dinner.',
         'https://www.bin152.com/') +
    card('French Quarter · Rooftop', 'The Rooftop at The Vendue',
         'An easy sunset glass with harbor views, especially if you stay at The Vendue. Check hours and weather; rooftops can close early or for events.',
         'https://www.thevendue.com/') +
    '</div></section>')

# 07 Breweries
parts.append('<section id="breweries">' + head('07', 'Breweries & craft drinks', 'Make room for a local pour.',
    'Charleston’s brewery district runs along “the Neck,” north of downtown. Pick one stop; it is a short ride, not a walk.') +
    '<div class="grid three">' +
    card('Brewery district · Brewpub', 'Edmund’s Oast',
         'Brewery and restaurant at 1081 Morrison Drive, with a separate taproom on upper King Street. The best choice if you want food with your beer.',
         'https://www.edmundsoast.com/') +
    card('Brewery district · Rooftop', 'Revelry Brewing Co.',
         'A casual brewery at 10 Conroy Street, known for its rooftop with sunset views of the skyline and the Ravenel Bridge. Check taproom hours and any event closures.',
         'https://revelrybrewingco.com/') +
    '</div></section>')

# 08 Events
parts.append('<section id="events">' + head('08', 'Sports & what’s happening', 'Sometimes the event is the reason to fly.',
    'Links go to current schedules. Check them against your travel dates before booking.') +
    '<div class="grid three">' +
    card('Minor league baseball · April–September', 'Charleston RiverDogs',
         'A relaxed evening at Joseph P. Riley Jr. Park (“The Joe”), on the Ashley River side of the peninsula. Check the home schedule before booking.',
         'https://www.milb.com/charleston/schedule', 'Schedule & ticket information') +
    card('Pro hockey · Fall–spring', 'South Carolina Stingrays',
         'ECHL hockey at the North Charleston Coliseum, closer to the airport than to downtown. Check the team’s home schedule for your dates.',
         'https://www.stingrayshockey.com/', 'Schedule & tickets') +
    card('Pro soccer · Spring–fall · Mount Pleasant', 'Charleston Battery soccer',
         'Not the waterfront park: the Charleston Battery is the city’s professional soccer team (USL Championship), playing at Patriots Point Soccer Complex in Mount Pleasant. A match pairs well with a Yorktown visit on the same side of the harbor.',
         'https://www.charlestonbattery.com/', 'Schedule & tickets') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>Check the destination calendar when choosing a weekend; spring festival season and holiday weekends fill hotels quickly.</p></div>'
    '<a class="button" href="https://www.charlestoncvb.com/" target="_blank" rel="noopener">Browse Charleston events</a></div></section>')

# 09 Itinerary
parts.append('<section id="itinerary">' + head('09', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend: one special dinner, one casual evening, aviation history and the harbor. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & unwind', [
        ('Late-morning arrival', 'Land at KCHS, subject to the actual flight plan, and ride downtown. Ask your hotel to hold luggage if the room is not ready.'),
        ('Afternoon', 'A foodie walking tour, which doubles as lunch, then an unhurried King Street shopping afternoon. Check in when your room is ready.'),
        ('Evening', 'An early-evening carriage ride through the old city, then dinner at FIG if reserved. A nightcap at The Vendue’s rooftop if the weather is good.')]) +
    day('SAT', 'Carrier deck & harbor', [
        ('Morning', 'Ride to Patriots Point when it opens. Explore the USS Yorktown and its aircraft, then take the Fort Sumter ferry from Patriots Point if you want to add the fort.'),
        ('Afternoon', 'Back downtown: Waterfront Park, Rainbow Row and the Battery. Optional couples massage at <a href="#spa">The Charleston Place</a> instead, if timing allows.'),
        ('Evening', 'Happy hour at Rappahannock Oyster Bar, the Schooner Pride sunset sail from nearby Aquarium Wharf, then a later dinner at Chez Nous.')]) +
    day('SUN', 'An easy departure', [
        ('Morning', 'Brunch at Husk, if open, and a last walk through the historic district.'),
        ('Before leaving', 'Check out and return to the FBO with ample time for aircraft preparation.'),
        ('Fly home', 'Let actual weather and your flight plan set the departure. Leave room to linger over a last coffee.')]) +
    '</div></section>')

# 10 Good to know
parts.append('<section id="know">' + head('10', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    '<div class="know-grid">'
    '<article><h3>Book in this order</h3><p>If a game or event drives the trip, secure tickets first. Then flexible lodging, the Friday dinner reservation and one water outing.</p></article>'
    '<article><h3>Allow for the season</h3><p>Summers are hot and humid with afternoon storms; spring and fall are peak seasons. Coastal weather can disrupt flights, sails and the Fort Sumter ferry.</p></article>'
    '<article><h3>Watch your footing</h3><p>Historic streets include cobblestones, uneven sidewalks and older buildings with stairs. Comfortable shoes help; confirm elevator access with lodging.</p></article>'
    '<article><h3>Dates come next</h3><p>Hotel prices, tickets, hours and rideshare fares are date-dependent. No availability or live price is implied here.</p></article>'
    '</div></section>')

parts.append('<div class="prototype-note reviewed"><span class="eyebrow">Reviewed · Destination 02</span><h3>Reviewed November 2, 2026.</h3>'
    '<p>Picks and links reviewed by WingAway Weekends. Hours, prices, menus and availability change often, so confirm directly with each place before booking.</p>'
    '<p class="note">WingAway Weekends helps you discover the destination. Use ForeFlight and current official aviation information for route, performance, weather, NOTAMs and preflight decisions. Flight planning and PIC responsibility stay with the pilot.</p></div></main>'
    '<footer><a class="brand" href="#main">WingAway Weekends</a><p>Charleston, South Carolina · Couples guide</p><details><summary>Photo credit</summary>'
    '<p>Rainbow Row Charleston July 2024 by Thomson200, <a href="https://commons.wikimedia.org/wiki/File:Rainbow_Row_Charleston_July_2024_1.jpg">Wikimedia Commons</a>, <a href="https://creativecommons.org/publicdomain/zero/1.0/deed.en">CC0</a>. Resized for display.</p></details></footer></body></html>')

with open(OUT, 'w') as f:
    f.write('\n'.join(parts))
