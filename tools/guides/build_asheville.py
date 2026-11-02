"""Generate docs/asheville/index.html in the same format as the Savannah and Charleston guides."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import ext, card, head, explore, day, ICON  # noqa: E402

OUT = sys.argv[1]
P = []
P.append(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#102d40"><meta name="description" content="A curated two-night Asheville getaway for GA pilots and their partners, from KMYR to KAVL. Biltmore, mountain views, spa time, dining and an aviation museum."><title>Asheville Couples Getaway | WingAway Weekends</title><link rel="canonical" href="https://wingawayweekends.com/asheville/"><link rel="icon" type="image/svg+xml" href="{ICON}"><link rel="stylesheet" href="../style.css"></head><body>
<a class="skip" href="#main">Skip to destination</a><header><a href="../" class="brand"><span class="mark">W</span><span>WingAway<span class="brand-small">WEEKENDS</span></span></a><span class="header-note">Destination prototype <span>03</span></span></header>
<main id="main"><div class="destination"><div class="intro"><span class="eyebrow">North Carolina · Couples · Two nights</span><h1>Asheville</h1><p class="lede">Fly to the mountains. Slow all the way down.</p><p>A Gilded Age estate with its own winery, Blue Ridge views, a serious food scene and some of the South’s best spa time. Asheville is still rebuilding from Hurricane Helene in places, and the visitors who come back are part of the recovery.</p><div class="pills"><span>Biltmore</span><span>Spa & mountains</span><span>Dining</span></div><div class="hero-actions"><a class="button" href="#itinerary">See the weekend itinerary</a><a href="#flight" class="secondary">Flight & arrival details</a></div></div><figure><picture><source type="image/webp" srcset="../assets/destinations/asheville-biltmore-480.webp 480w, ../assets/destinations/asheville-biltmore-960.webp 960w, ../assets/destinations/asheville-biltmore-1600.webp 1600w" sizes="(max-width:800px) 100vw, 50vw"><img src="../assets/destinations/asheville-biltmore-960.jpg" srcset="../assets/destinations/asheville-biltmore-480.jpg 480w, ../assets/destinations/asheville-biltmore-960.jpg 960w, ../assets/destinations/asheville-biltmore-1600.jpg 1600w" sizes="(max-width:800px) 100vw, 50vw" alt="Front facade of Biltmore House at Biltmore Estate in Asheville" width="960" height="524"></picture><figcaption>Biltmore House · Give it most of a day</figcaption></figure></div>
<div class="snapshot" aria-label="Trip snapshot"><div><span>YOUR ROUTE</span><strong>KMYR <span class="route-line">to</span> KAVL</strong></div><div><span>STRAIGHT-LINE DISTANCE</span><strong>~207 <small>NM</small></strong></div><div><span>ILLUSTRATIVE FLIGHT TIME</span><strong>~1 hr 38 <small>min</small></strong></div><div><span>WEEKEND STYLE</span><strong>Two nights <small>· Rental car</small></strong></div></div><p class="estimate">Time illustration: direct distance at 150 KTAS plus 15 minutes for departure and arrival, matching the discovery page. Mountain terrain, weather and routing matter more here than at coastal destinations. Use ForeFlight for your actual flight plan.</p>
<nav class="jump" aria-label="Destination sections"><a href="#flight">Fly & arrive</a><a href="#stay">Stay</a><a href="#eat">Eat</a><a href="#explore">Explore</a><a href="#spa">Spa</a><a href="#shopping">Shop</a><a href="#wine">Wine</a><a href="#breweries">Breweries</a><a href="#events">Sports & events</a><a href="#itinerary">Itinerary</a></nav>''')

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Land, then head for the hills.',
    'KAVL is the selected arrival airport: Class C, one 8,000-foot runway, about 15 miles south of downtown. The field sits in a valley surrounded by mountains, so plan for terrain and fast-changing weather.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>One FBO</h3>'
    '<div class="fbo"><div><strong>Signature Aviation</strong><p>40 Lindbergh Lane, Fletcher</p></div><a href="tel:+18286877110">828-687-7110</a><a href="https://www.signatureaviation.com/locations/AVL" target="_blank" rel="noopener">FBO details</a></div>'
    '<p class="note">Signature is the only FBO. Ask about 100LL pricing, facility fees, two-night parking, fee waivers with fuel and after-hours access. The airport is redeveloping land for a terminal expansion and removing some GA hangars, so <strong>confirm transient parking space before you go</strong>. No live fuel price or parking quote is shown.</p>'
    '<p class="note">Check density altitude in summer and the mountain-flying considerations for your route and aircraft. Ridges and valleys can hold cloud long after the coast is clear.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>A car makes this weekend.</h3><p>Asheville is spread out: the airport, Biltmore, downtown and the Grove Park Inn are each 10–20 minutes apart, and the Blue Ridge Parkway and the air museum need a car. Arrange a rental car or FBO-arranged car ahead of time.</p><p>Rideshare works for evenings downtown if you would rather not drive after dinner.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'Choose your kind of weekend.',
    'Three different stays, rather than three versions of the same hotel. Rates and availability need travel dates.') +
    '<div class="grid three">' +
    card('Historic resort · Mountain views', 'Omni Grove Park Inn',
         'A 1913 stone lodge on Sunset Mountain, known for its huge fireplaces, terrace views and an underground spa. The classic Asheville splurge and the easiest way to make spa time part of the stay. Ask for a view room and check resort fees.',
         'https://www.omnihotels.com/hotels/asheville-grove-park') +
    card('On the estate · Romantic splurge', 'The Inn on Biltmore Estate',
         'Stay on the Biltmore grounds, above Antler Hill Village and the winery. The most romantic option if the estate is the heart of your trip. Ask what estate access is included with your stay.',
         'https://www.biltmore.com/stay/') +
    card('Downtown · Walk to dinner', 'Kimpton Hotel Arras',
         'A modern hotel in a historic downtown tower, close to restaurants, galleries and shops. The best choice if you want evenings on foot rather than driving back up a mountain. Check parking for your rental car.',
         'https://www.hotelarras.com/') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Two dinners. One easy brunch.',
    'Asheville’s food scene is recovering from Helene, and some well-known restaurants have closed for good. Confirm each one is open for your dates, then reserve the anchor dinner first.') +
    '<div class="grid three">' +
    card('Friday dinner · Reserve ahead', 'Cúrate',
         'Award-winning Spanish tapas on Biltmore Avenue downtown, from chef Katie Button. Lively and made for sharing. Book well ahead for a weekend table.',
         'https://www.curatetapasbar.com/') +
    card('Saturday dinner · Casual & celebrated', 'Chai Pani',
         'Colorful Indian street food from a restaurant group that was a 2026 James Beard finalist. Relaxed and fun after a long Biltmore day. Check whether it takes reservations or is walk-in for your night.',
         'https://chaipani.com/') +
    card('Sunday brunch · Biltmore Village', 'Corner Kitchen',
         'A Biltmore Village favorite that came back after Helene flooding and won a national small-business recovery award in 2026. Convenient on the way back to the airport. Confirm brunch hours.',
         'https://thecornerkitchen.com/') +
    '</div></section>')

P.append('<section id="explore">' + head('04', 'Things to do', 'One great house. A lot of sky.',
    'Biltmore deserves most of a day. Choose one or two other experiences and leave the rest for next time.') +
    '<div class="explore-list">' +
    explore(1, 'Biltmore Estate',
            'America’s largest private home, with formal gardens, miles of grounds and Antler Hill Village. The estate reopened quickly after Helene. Book a timed house entry ahead, allow five to six hours, and wear comfortable shoes. Daytime admission includes a complimentary wine tasting for guests 21 and over; confirm what your ticket includes.',
            'https://www.biltmore.com/', 'Tickets & visit details') +
    explore(2, 'Western North Carolina Air Museum',
            'The pilot’s pick: a volunteer-run collection of vintage and restored aircraft at 1340 Gilbert Street in Hendersonville, about 25–30 minutes south. Admission is free (donations welcome). It is only open a few days a week, typically Wednesday, Saturday and Sunday afternoons, and reopened after Helene flooding. Confirm hours before driving down.',
            'https://www.wncam.org/', 'Museum information') +
    explore(3, 'Blue Ridge Parkway',
            'Drive up from Asheville for overlooks and short walks. Fall color and clear winter days are spectacular. Sections can close for weather or storm repairs, so check the National Park Service road status before heading out.',
            'https://www.nps.gov/blri/planyourvisit/roadclosures.htm', 'Parkway road status') +
    explore(4, 'Downtown & the River Arts District',
            'Downtown’s galleries, bookstores and Art Deco buildings are easy to explore on foot. The River Arts District was badly hit by Helene and is rebuilding; many studios have reopened, so check before you go and buy something from a working artist.') +
    '</div>')

P.append('<div id="spa" class="couples"><span class="eyebrow">Optional / Spa & relaxation</span><h3>The Spa at Omni Grove Park Inn · Time for two</h3>'
    '<p>A large underground spa built into the mountainside, with mineral pools, waterfalls and a fireplace lounge. It is the best-known spa in the region and a natural fit for a couples weekend.</p>'
    '<p><strong>Booking:</strong> Ask about couples treatments, whether spa access is included with a treatment for non-hotel guests, current pricing, gratuity and the cancellation policy. Weekends book up; reserve early. No prices are shown here because they change, and no appointment has been booked.</p>'
    '<p>Optional Sunday morning, or Saturday afternoon if you split Biltmore across two days.</p>'
    '<a href="https://www.omnihotels.com/hotels/asheville-grove-park/spa" target="_blank" rel="noopener">Spa details</a></div></section>')

P.append('<section id="shopping">' + head('05', 'Shopping & boutiques', 'Bring home something handmade.',
    'Asheville is a craft town: pottery, woodwork, jewelry and art, often bought straight from the maker.') +
    '<div class="grid three">' +
    card('Downtown · Historic arcade', 'Grove Arcade',
         'A grand 1920s building downtown with independent shops and places to eat under one roof. An easy rainy-day stop.',
         'https://www.grovearcade.com/') +
    card('Working studios', 'River Arts District',
         'Artists’ studios and galleries along the French Broad River, many rebuilt after Helene. Buying directly from studios supports the recovery. Check which are open on your dates.') +
    card('Near the estate', 'Biltmore Village',
         'Historic shops at the Biltmore gate, convenient before or after an estate visit. Parts of the village were still recovering from flooding into 2026, so expect some closed storefronts.') +
    '</div></section>')

P.append('<section id="wine">' + head('06', 'Wine & wine experiences', 'A glass, and a view.',
    'Biltmore’s winery is the easy choice: it is part of the estate day rather than a separate trip.') +
    '<div class="grid three">' +
    card('Antler Hill Village · On the estate', 'Biltmore Winery',
         'A tasting room and wine bar in the estate’s former dairy barn. Daytime estate tickets include a complimentary tasting; upgraded tastings cost extra. Plan it for late afternoon, and decide who is driving.',
         'https://www.biltmore.com/', 'Winery details') +
    card('Grove Park Inn · Sunset', 'The Sunset Terrace',
         'Not a winery, but a glass of wine on the Grove Park Inn’s terrace as the sun goes down over the mountains is a quintessential Asheville moment. Confirm hours and whether reservations are needed.') +
    '</div></section>')

P.append('<section id="breweries">' + head('07', 'Breweries & craft drinks', 'Make room for a local pour.',
    'Asheville has dozens of breweries, and many have reopened since the storm. Pick one; there is no need for a crawl.') +
    '<div class="grid three">' +
    card('Mills River · Near the airport', 'Sierra Nevada Brewing',
         'The California brewer’s large East Coast brewery, with a restaurant, gardens and tours, just minutes from KAVL. An easy first or last stop of the weekend. Check tour times and hours.',
         'https://sierranevada.com/visit/mills-river-nc/') +
    card('Downtown · South Slope', 'South Slope breweries',
         'A cluster of taprooms on the south side of downtown, walkable from many restaurants. Check current openings on the visitor bureau’s site.',
         'https://www.exploreasheville.com/', 'Explore Asheville') +
    card('Downtown · Pizza & pints', 'Asheville Brewing',
         'A long-running local brewery and pizza kitchen downtown, known for its Ninja Porter and a relaxed, family-friendly feel. A good casual lunch or early dinner.',
         'https://www.ashevillebrewing.com/location/downtown/') +
    '</div></section>')

P.append('<section id="events">' + head('08', 'Sports & what’s happening', 'Sometimes the season is the reason to fly.',
    'This prototype links to current calendars. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('Peak season · October', 'Fall color',
         'Mid to late October is Asheville’s busiest time, as the leaves turn along the Parkway. Book lodging very early and expect crowds and higher prices.') +
    card('November–early January', 'Christmas at Biltmore',
         'The house decorated for the holidays, with evening candlelight visits on select nights. A memorable couples trip; separate tickets sell out.',
         'https://www.biltmore.com/', 'Seasonal details') +
    card('Minor league baseball · Spring–summer', 'Asheville Tourists',
         'An easygoing evening at historic McCormick Field, a short drive from downtown. Check the home schedule.',
         'https://www.milb.com/asheville', 'Schedule & tickets') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>Check the destination calendar when choosing a weekend, and confirm dates, location and tickets with the organizer.</p></div>'
    '<a class="button" href="https://www.exploreasheville.com/" target="_blank" rel="noopener">Browse Asheville events</a></div></section>')

P.append('<section id="itinerary">' + head('09', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend built around Biltmore, with one aviation stop and plenty of slack for mountain weather. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & settle in', [
        ('Late-morning arrival', 'Land at KAVL, subject to weather and your actual flight plan. Pick up the rental car; lunch at Sierra Nevada in Mills River is a few minutes away.'),
        ('Afternoon', 'Check in, then wander downtown and the Grove Arcade, or drive up to the Grove Park Inn for the view.'),
        ('Evening', 'Dinner at Cúrate if reserved.')]) +
    day('SAT', 'Biltmore day', [
        ('Morning', 'Timed entry to Biltmore House, then the gardens and conservatory.'),
        ('Afternoon', 'Antler Hill Village and the winery tasting. Alternatively, split the day: drive to the WNC Air Museum (if open) and keep Biltmore for the morning.'),
        ('Evening', 'Sunset on the Grove Park Inn terrace, then a relaxed dinner at Chai Pani.')]) +
    day('SUN', 'An easy departure', [
        ('Morning', 'Brunch at Corner Kitchen in Biltmore Village, or a couples spa appointment at the Grove Park Inn.'),
        ('Before leaving', 'Short Blue Ridge Parkway drive if roads and time allow; return the car and allow ample time at the FBO.'),
        ('Fly home', 'Let mountain weather and your flight plan set the departure. Leave room to stay another night if the ceilings do not cooperate.')]) +
    '</div></section>')

P.append('<section id="know">' + head('10', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    '<div class="know-grid">'
    '<article><h3>Book in this order</h3><p>FBO parking and a car first, then lodging, Biltmore timed entry, the Friday dinner and any spa appointment.</p></article>'
    '<article><h3>Mountain weather</h3><p>Valley fog, low ceilings and summer storms are common. Build in a backup day and have a plan B for the drive or a later departure.</p></article>'
    '<article><h3>Still recovering</h3><p>Hurricane Helene hit in September 2024. Most of the city is open, but some businesses closed permanently and others moved. Check every booking directly.</p></article>'
    '<article><h3>Dates come next</h3><p>Hotel prices, tickets, hours and rental rates are date-dependent, and October is peak season. No availability or live price is implied here.</p></article>'
    '</div></section>')

P.append('<div class="prototype-note"><span class="eyebrow">Testing / Destination 03</span><h3>Draft for review.</h3>'
    '<p>Research-based selections, not personal-visit endorsements. Researched November 1, 2026. Several official links could not be opened during research; check each one, and confirm hours, prices and availability directly before booking.</p>'
    '<p class="note">WingAway Weekends helps you discover the destination. Use ForeFlight and current official aviation information for route, performance, weather, NOTAMs and preflight decisions. Flight planning and PIC responsibility stay with the pilot.</p></div></main>'
    '<footer><a class="brand" href="#main">WingAway Weekends</a><p>Asheville, North Carolina · Couples prototype</p><details><summary>Photo credit</summary>'
    '<p>Biltmore House front facade, Asheville, North Carolina, May 2026, by WillThomas, <a href="https://commons.wikimedia.org/wiki/File:Biltmore_House_front_facade_Asheville_North_Carolina_-_May_2026.jpg">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by/4.0">CC BY 4.0</a>. Resized for display.</p></details></footer></body></html>')

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
