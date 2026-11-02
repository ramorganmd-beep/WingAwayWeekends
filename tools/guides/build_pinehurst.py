"""Generate docs/pinehurst/index.html in the same format as the other destination guides."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import card, head, explore, day, ICON  # noqa: E402

OUT = sys.argv[1]
P = []
P.append(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#102d40"><meta name="description" content="A curated two-night Pinehurst getaway for GA pilots and their partners, from KMYR to KSOP. Historic golf, resort stays, spa time and the Village of Pinehurst."><title>Pinehurst Couples Getaway | WingAway Weekends</title><link rel="canonical" href="https://wingawayweekends.com/pinehurst/"><link rel="icon" type="image/svg+xml" href="{ICON}"><link rel="stylesheet" href="../style.css"></head><body>
<a class="skip" href="#main">Skip to destination</a><header><a href="../" class="brand"><span class="mark">W</span><span>WingAway<span class="brand-small">WEEKENDS</span></span></a><span class="header-note">Destination prototype <span>04</span></span></header>
<main id="main"><div class="destination"><div class="intro"><span class="eyebrow">North Carolina · Couples · Two nights</span><h1>Pinehurst</h1><p class="lede">A short flight. A century of golf.</p><p>Longleaf pines, sandy fairways and a village built for strolling. Pinehurst is the “Home of American Golf,” but a weekend here works just as well for the partner who would rather be at the spa, on a carriage ride or browsing downtown Southern Pines.</p><div class="pills"><span>Golf</span><span>Spa</span><span>Village charm</span></div><div class="hero-actions"><a class="button" href="#itinerary">See the weekend itinerary</a><a href="#flight" class="secondary">Flight & arrival details</a></div></div><figure><picture><source type="image/webp" srcset="../assets/destinations/pinehurst-golf-480.webp 480w, ../assets/destinations/pinehurst-golf-960.webp 960w, ../assets/destinations/pinehurst-golf-1600.webp 1600w" sizes="(max-width:800px) 100vw, 50vw"><img src="../assets/destinations/pinehurst-golf-960.jpg" srcset="../assets/destinations/pinehurst-golf-480.jpg 480w, ../assets/destinations/pinehurst-golf-960.jpg 960w, ../assets/destinations/pinehurst-golf-1600.jpg 1600w" sizes="(max-width:800px) 100vw, 50vw" alt="Fairway and sand bunkers at Pinehurst No. 4 golf course" width="960" height="720"></picture><figcaption>Pinehurst No. 4 · Sand, pines and wiregrass</figcaption></figure></div>
<div class="snapshot" aria-label="Trip snapshot"><div><span>YOUR ROUTE</span><strong>KMYR <span class="route-line">to</span> KSOP</strong></div><div><span>STRAIGHT-LINE DISTANCE</span><strong>~96 <small>NM</small></strong></div><div><span>ILLUSTRATIVE FLIGHT TIME</span><strong>~54 <small>min</small></strong></div><div><span>WEEKEND STYLE</span><strong>Two nights <small>· Car or shuttle</small></strong></div></div><p class="estimate">Time illustration: direct distance at 150 KTAS plus 15 minutes for departure and arrival, matching the discovery page. Use ForeFlight for your actual flight plan.</p>
<nav class="jump" aria-label="Destination sections"><a href="#flight">Fly & arrive</a><a href="#stay">Stay</a><a href="#eat">Eat</a><a href="#explore">Golf & explore</a><a href="#spa">Spa</a><a href="#shopping">Shop</a><a href="#wine">Drinks</a><a href="#breweries">Breweries</a><a href="#events">Events</a><a href="#itinerary">Itinerary</a></nav>''')

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Land, then settle in.',
    'KSOP, Moore County Airport, serves Pinehurst and Southern Pines. It is a relaxed, uncontrolled field a short drive from the village.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>One FBO</h3>'
    '<div class="fbo"><div><strong>Moore County Airport FBO</strong><p>7825 Aviation Drive, Carthage, NC 28327</p></div><a href="tel:+19106923212">910-692-3212</a></div>'
    '<p class="note">The airport’s own FBO lists transient tiedowns and hangars, and crew or courtesy cars. Call ahead about two-night parking, hangar space if you want it, fees and after-hours arrangements. Directory fuel prices conflict, so no price is shown. CTAF/UNICOM 123.05.</p>'
    '<p class="note">Big golf weekends and championships bring a lot of traffic. Arrange parking early if your dates coincide with an event.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>Short hops, few rideshares.</h3><p>The village and downtown Southern Pines are each a short drive from the airport, but rideshare cars can be scarce in a small town. Arrange a rental car, a local taxi or a resort transfer before you fly; ask your hotel what it offers.</p><p>Once in the village, everything is walkable.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'Choose your kind of weekend.',
    'Staying at Pinehurst Resort is also the usual way to get a tee time on No. 2. Rates and availability need travel dates.') +
    '<div class="grid three">' +
    card('Grand resort hotel · The flagship', 'The Carolina',
         'Pinehurst Resort’s landmark hotel, with wide verandas, formal dining and the spa next door. The best choice if golf on No. 2 is part of the plan. Ask what golf and spa access your package includes.',
         'https://www.pinehurst.com/accommodations/the-carolina-hotel/') +
    card('In the village · The original', 'The Holly Inn',
         'The resort’s first hotel, in the middle of the Village of Pinehurst. Smaller and cozier than The Carolina, with shops and restaurants outside the door. Resort amenities are a short walk or shuttle away.',
         'https://www.pinehurst.com/') +
    card('Classic Donald Ross · Southern Pines', 'Mid Pines Inn & Golf Club',
         'A 1920s inn beside a Donald Ross course from 1921, with a quieter, old-school feel. Pairs well with a Southern Pines dinner. Check room style and golf packages.',
         'https://midpinesinn.com/') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Two dinners. One relaxed lunch.',
    'Pinehurst and Southern Pines are small, so popular tables fill on golf weekends. Reserve dinners early.') +
    '<div class="grid three">' +
    card('Friday dinner · In the village', 'Villaggio Ristorante',
         'An Italian restaurant and bar in the Magnolia Inn in the Village of Pinehurst. Consistently well reviewed for date nights, and walkable from The Holly Inn. Reserve ahead.',
         'https://www.pinehurst.com/dining/villaggio/') +
    card('Saturday dinner · Southern Pines', 'Elliotts on Linden',
         'A highly rated American restaurant in Southern Pines, known for polished service and seasonal cooking. Worth the short drive for your anchor dinner.',
         'https://www.elliottsonlinden.com/') +
    card('Casual lunch · In the village', 'Pinehurst Brewing Co.',
         'Beer brewed on site and barbecue in the village’s restored 1895 steam plant. An easy lunch after golf or a morning walk. Check the beer garden’s seasonal hours.',
         'https://www.pinehurstbrewing.com/') +
    '</div></section>')

P.append('<section id="explore">' + head('04', 'Golf & things to do', 'Play a legend. Or don’t.',
    'Golf is the headline, but the best Pinehurst weekends leave room for slower things too.') +
    '<div class="explore-list">' +
    explore(1, 'Pinehurst No. 2',
            'Donald Ross’s masterpiece and a regular U.S. Open venue. Tee times are essentially reserved for resort guests, so book it with your stay. Expect a premium green fee; ask about caddies, who make the round.',
            'https://www.pinehurst.com/', 'Pinehurst Resort golf') +
    explore(2, 'The Cradle & Thistle Dhu',
            'The Cradle is a fun nine-hole short course, and Thistle Dhu is a large putting course: both perfect for a partner who does not play 18 holes. Book The Cradle through the resort’s Starting Tower (<a href="tel:+19102358960">910-235-8960</a>); confirm how far ahead you can book.',
            'https://www.pinehurst.com/golf/courses/cradle-short-course/', 'The Cradle details') +
    explore(3, 'Village of Pinehurst',
            'A planned New England-style village from the 1890s, with tree-lined lanes, historic cottages and shops. Walk it in the morning, or ask the resort about a carriage ride.') +
    explore(4, 'Downtown Southern Pines',
            'Five minutes away: a walkable main street with independent shops, galleries and restaurants along the railroad. The Reservoir Park greenway offers an easy 2-mile loop walk.') +
    explore(5, 'Mid Pines & Pine Needles',
            'Two classic Donald Ross courses in Southern Pines that welcome outside play. A good alternative if No. 2 is booked or out of budget.') +
    '</div>')

P.append('<div id="spa" class="couples"><span class="eyebrow">Optional / Spa & relaxation</span><h3>The Spa at Pinehurst · Time for two</h3>'
    '<p>Pinehurst Resort’s full-service spa, next to The Carolina, with couples massages and relaxation areas. A natural plan for the non-golfer while the other plays No. 2, or a shared treatment after golf.</p>'
    '<p><strong>Booking:</strong> Ask about couples treatments, spa access for non-resort guests, current pricing, gratuity and the cancellation policy. Weekend appointments fill early. No prices are shown here because they change, and no appointment has been booked.</p>'
    '<p>Optional Saturday morning during the golf round, or Sunday before flying home.</p>'
    '<a href="https://www.pinehurst.com/spa/east-wing-treatments/" target="_blank" rel="noopener">Spa treatments at Pinehurst Resort</a></div></section>')

P.append('<section id="shopping">' + head('05', 'Shopping & boutiques', 'Bring home something with a story.',
    'Two compact, walkable areas: the Village of Pinehurst and downtown Southern Pines.') +
    '<div class="grid three">' +
    card('Historic village', 'Village of Pinehurst shops',
         'Boutiques, gift shops and golf apparel in a few walkable blocks around the village green. An easy browse before lunch.') +
    card('Main street', 'Downtown Southern Pines',
         'Independent clothing, home, book and gift shops along Broad Street. Pair it with Saturday dinner in town.',
         'https://southernpines.biz/members/3-shop') +
    card('For the golfer', 'Pinehurst Resort golf shops',
         'Logo shirts, caps and Putter Boy keepsakes from the Home of American Golf. Probably the most-requested souvenir of the weekend.') +
    '</div></section>')

P.append('<section id="wine">' + head('06', 'Wine & drinks', 'A glass, and no hurry.',
    'For this weekend, the best drinks come with a view of the golf.') +
    '<div class="grid three">' +
    card('Overlooking No. 2', 'The Deuce',
         'The bar and restaurant in the resort clubhouse, looking out over the 18th green of No. 2. Ideal for a glass while golfers finish their rounds. Confirm hours.') +
    card('Dinner pairing', 'Elliotts on Linden',
         'Let Saturday’s anchor dinner double as your wine stop, and ask the staff for a pairing.',
         'https://www.elliottsonlinden.com/') +
    '</div></section>')

P.append('<section id="breweries">' + head('07', 'Breweries & craft drinks', 'Make room for a local pour.',
    'The Sandhills have a small, friendly brewery scene. Pick one.') +
    '<div class="grid three">' +
    card('Village of Pinehurst', 'Pinehurst Brewing Co.',
         'In the historic steam plant, with barbecue alongside. The easiest choice if you are staying at the resort.',
         'https://www.pinehurstbrewing.com/') +
    card('Aberdeen · The original', 'Railhouse Brewery',
         'The area’s first microbrewery, with a taproom pouring small-batch beers. A short drive from Pinehurst.',
         'https://railhousebrewery.com/') +
    '</div></section>')

P.append('<section id="events">' + head('08', 'Sports & what’s happening', 'Sometimes the event is the reason to fly.',
    'This prototype links to current calendars. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('Championship golf', 'U.S. Open at Pinehurst',
         'Pinehurst is a USGA “anchor site,” hosting the U.S. Open regularly, with the next scheduled for 2029. Championship weeks are a spectacle, but lodging and airport parking book up years ahead.') +
    card('Peak seasons', 'Spring & fall golf',
         'Spring and fall bring the best golf weather and the busiest weekends. Winter is quieter, with lower rates and mild days.') +
    card('Resort calendar', 'Pinehurst events',
         'The resort runs regular events, such as evening glow golf at The Cradle and seasonal celebrations. Check what is on for your dates.',
         'https://www.pinehurst.com/', 'Pinehurst Resort events') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>The Pinehurst, Southern Pines and Aberdeen visitor bureau lists area events, from golf to horse-country happenings.</p></div>'
    '<a class="button" href="https://www.homeofgolf.com/" target="_blank" rel="noopener">Browse area events</a></div></section>')

P.append('<section id="itinerary">' + head('09', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend: one round for the golfer, spa time for two, a village evening and a Southern Pines dinner. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & unwind', [
        ('Late-morning arrival', 'Land at KSOP, subject to the actual flight plan, and head to the resort. Ask about luggage storage if your room is not ready.'),
        ('Afternoon', 'Lunch at Pinehurst Brewing Co., then a walk through the village, or nine holes together at The Cradle.'),
        ('Evening', 'Dinner at Villaggio, then a nightcap on a hotel veranda.')]) +
    day('SAT', 'Golf & spa', [
        ('Morning', 'The golfer plays No. 2 (or Mid Pines or Pine Needles); the other books The Spa at Pinehurst. Or share a couples massage instead.'),
        ('Afternoon', 'Meet for a drink at The Deuce overlooking the 18th green, then browse downtown Southern Pines.'),
        ('Evening', 'Dinner at Elliotts on Linden.')]) +
    day('SUN', 'An easy departure', [
        ('Morning', 'Breakfast, a putting contest at Thistle Dhu and a last walk through the village.'),
        ('Before leaving', 'Check out and return to the FBO with ample time for aircraft preparation.'),
        ('Fly home', 'Let weather and your flight plan set the departure; there is no need to rush.')]) +
    '</div></section>')

P.append('<section id="know">' + head('10', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    '<div class="know-grid">'
    '<article><h3>Book in this order</h3><p>Resort stay and No. 2 tee time together, then ground transport, dinners and the spa.</p></article>'
    '<article><h3>Allow for the season</h3><p>Summers are hot and humid, with afternoon storms. Spring and fall are peak golf seasons; book early.</p></article>'
    '<article><h3>Dress codes</h3><p>Resort dining rooms and golf courses have dress codes. Check them before you pack a light airplane.</p></article>'
    '<article><h3>Dates come next</h3><p>Hotel prices, green fees, tee times and spa rates are date-dependent. No availability or live price is implied here.</p></article>'
    '</div></section>')

P.append('<div class="prototype-note"><span class="eyebrow">Testing / Destination 04</span><h3>Draft for review.</h3>'
    '<p>Research-based selections, not personal-visit endorsements. Researched November 1, 2026. Several restaurants and venues have no website link because official addresses could not be confirmed; check each one, and confirm hours, prices and availability directly before booking.</p>'
    '<p class="note">WingAway Weekends helps you discover the destination. Use ForeFlight and current official aviation information for route, performance, weather, NOTAMs and preflight decisions. Flight planning and PIC responsibility stay with the pilot.</p></div></main>'
    '<footer><a class="brand" href="#main">WingAway Weekends</a><p>Pinehurst, North Carolina · Couples prototype</p><details><summary>Photo credit</summary>'
    '<p>Pinehurst No. Four 4 Golf Course by Dan Perry from Atlanta, USA, <a href="https://commons.wikimedia.org/wiki/File:Pinehurst_No._Four_4_Golf_Course_(4599708312).jpg">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by/2.0">CC BY 2.0</a>. Resized and converted for display; cropped to fit. Photographed in 2010; not a current course-layout reference.</p></details></footer></body></html>')

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
