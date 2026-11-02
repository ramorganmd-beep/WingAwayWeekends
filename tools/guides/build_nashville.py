"""Generate docs/nashville/index.html."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import card, head, explore, day, page_start, page_end, fbo, know  # noqa: E402

OUT = sys.argv[1]
REVIEWED = 'November 2, 2026'  # owner review date; None while still a draft
NAV = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('explore', 'Music & sights'), ('spa', 'Spa'), ('shopping', 'Shop'),
       ('events', 'Events'), ('itinerary', 'Itinerary')]
P = [page_start(
    slug='nashville', name='Nashville', state='Tennessee', number=9, reviewed=REVIEWED,
    description='A curated two-night Nashville getaway for GA pilots and their partners, from KMYR to KJWN. The Ryman, the Opry, Germantown dining and Music City nights.',
    lede='Fly in for the music. Stay for dinner.',
    intro='The Ryman Auditorium, the Grand Ole Opry, honky-tonks on Broadway and one of the South’s most exciting restaurant scenes. John C. Tune Airport puts you about 15 minutes from downtown.',
    pills=['Live music', 'Dining', 'History'],
    photo='nashville', widths=[480, 960], alt='Nashville skyline reflected in the Cumberland River', img_w=960, img_h=640,
    caption='Nashville from the Cumberland River', airport='KJWN', nm=419, flight_time='~3 hr 3 <small>min</small>',
    style='Rideshare', estimate_extra='At about three hours from KMYR, consider a fuel stop and plan for winds aloft across the Appalachians. ', nav=NAV)]

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Land at Tune, not BNA.',
    'KJWN, John C. Tune Airport, is Nashville’s general aviation reliever, west of downtown and far easier than the airline airport.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>The FBO</h3>' +
    fbo('Contour Flight Support', '110 Tune Airport Drive · listed 24 hours', '615-350-5000') +
    '<p class="note">Full-service and self-serve 100LL and Jet A are listed. The control tower is listed as operating 7 AM–9 PM, so check procedures for late arrivals. Ask about facility fees, two-night parking and waivers with fuel. Atlantic Aviation won a bid to build a second FBO here; check whether it has opened. No live price is shown.</p>'
    '<p class="note">Nashville’s Class C airspace (BNA) sits to the southeast; review the sectional and arrival procedures.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>Rideshare everywhere.</h3><p>Downtown is about 15 minutes away. Rideshare is the easy option; parking downtown is expensive and you won’t want to drive after a night of music.</p><p>Downtown, Germantown and The Gulch are each a short ride apart.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'Choose your kind of weekend.',
    'Three different stays. Rates and availability need travel dates; book six to eight weeks ahead for weekends.') +
    '<div class="grid three">' +
    card('Historic grand hotel', 'The Hermitage Hotel',
         'One of Nashville’s oldest and most beautiful hotels, with a grand lobby and old-school service. Walkable to the Ryman and downtown.',
         'https://www.thehermitagehotel.com/') +
    card('Downtown · Spa', 'Omni Nashville',
         'Connected to the Country Music Hall of Fame, with the Mokara Spa and its couples treatments. Easy for a music-and-spa weekend.',
         'https://www.omnihotels.com/hotels/nashville') +
    card('Quiet & walkable', 'Germantown Inn',
         'A small inn in Germantown, the city’s most walkable neighborhood for dinner and a slow evening, away from the Broadway crowds.',
         'https://germantowninn.com/') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Two dinners. One easy lunch.',
    'Nashville’s best reservations go fast. Book the special dinner as soon as you know your dates.') +
    '<div class="grid three">' +
    card('Friday dinner · Downtown', 'Boqueria',
         'Barcelona-style tapas, paella and sangria at Fifth + Broadway, a short walk from the Ryman and the honky-tonks. Reservations and walk-ins; call <a href="tel:+16152457160">615-245-7160</a>.',
         'https://boqueriarestaurant.com/location/nsh-fifth-broadway/') +
    card('Saturday dinner · Special occasion', 'Locust',
         'A small restaurant named among North America’s 50 Best and one of the city’s toughest reservations. Book the moment reservations open.',
         'https://www.locustnashville.com/') +
    card('Alternative dinner · Germantown', 'Rolf & Daughters',
         'Seasonal, pasta-focused cooking in a warm Germantown room. Swap it in for either night; The Optimist, a lively seafood restaurant, is another easy alternative.',
         'https://www.rolfanddaughters.com/') +
    '</div></section>')

P.append('<section id="explore">' + head('04', 'Music & sights', 'Hear it where it happened.',
    'Choose one big show and leave the rest of the music to chance.') +
    '<div class="explore-list">' +
    explore(1, 'Broadway honky-tonks',
            'The classic Nashville night: live bands from late morning to late night along Lower Broadway, no cover at most places. Hop between a few, then find a quieter listening room if you want to hear songwriters up close.') +
    explore(2, 'Ryman Auditorium',
            'The “Mother Church of Country Music” and home of the Opry from 1943 to 1974. Take the daytime tour, with a 2026 Opry 100 exhibit, or see a concert or an “Opry at the Ryman” show at night.',
            'https://www.ryman.com/', 'Shows & tours') +
    explore(3, 'Grand Ole Opry',
            'The live radio show at the Grand Ole Opry House, with several artists per night. Book tickets ahead and check whether your date is at the Opry House or the Ryman.') +
    explore(4, 'Country Music Hall of Fame and Museum',
            'Downtown, beside the Omni. Allow a few hours even if you are not a country fan.') +
    explore(5, 'Germantown stroll',
            'Historic brick streets, cafés and restaurants just north of downtown. The calm counterpoint to Broadway.') +
    explore(6, 'Arrington Vineyards (wine side trip)',
            'A hillside winery co-founded by Kix Brooks, about 25 miles south in the Williamson County countryside, named Southeast Winery of the Year for 2026. Bring a picnic; weekends from April to November add live music on the lawn. Taste on the non-flying day, and plan a driver.',
            'https://www.arringtonvineyards.com/', 'Winery information') +
    '</div>')

P.append('<div id="spa" class="couples"><span class="eyebrow">Optional / Spa & relaxation</span><h3>Mokara Spa at Omni Nashville · Time for two</h3>'
    '<p>Couples massages, steam rooms and relaxation lounges downtown. A good Saturday-afternoon reset before a night out.</p>'
    '<p><strong>Booking:</strong> Ask about couples treatments, access for non-hotel guests, current pricing and cancellation policy. No prices are shown here, and no appointment has been booked.</p>'
    '<a href="https://www.omnihotels.com/hotels/nashville/spa" target="_blank" rel="noopener">Mokara Spa details</a></div></section>')

P.append('<section id="shopping">' + head('05', 'Shopping & boutiques', 'Bring home a little Music City.',
    'Most of it is walkable from Broadway: boots, gig posters, records and Nashville-made goods.') +
    '<div class="grid four">' +
    card('Across from Bridgestone Arena', 'Fifth + Broadway',
         'The downtown shopping and dining block on Broadway, with apparel and lifestyle shops that lean toward Nashville brands, plus Boqueria for Friday dinner. Store lineups change, so check the directory.') +
    card('Lower Broadway', 'Boot shops',
         'Cowboy boots are the classic Nashville souvenir, and several boot stores line Lower Broadway, some with multi-pair deals. Try on plenty, and compare quality before you buy.') +
    card('Letterpress posters', 'Hatch Show Print',
         'The legendary letterpress poster shop, with its store at the Country Music Hall of Fame. Pair it with your museum visit and bring home a gig poster.') +
    card('Historic arcade', 'The Arcade',
         'A 1903 glass-roofed shopping arcade between Fourth and Fifth Avenues, home to small galleries and shops. A quiet browse a few blocks off Broadway.') +
    '</div><p class="note">Record lovers: Third Man Records, Jack White’s label and shop, is a short ride away near The Gulch.</p></section>')

P.append('<section id="events">' + head('06', 'Sports & what’s happening', 'Sometimes the event is the reason to fly.',
    'This prototype links to current calendars. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('Year-round', 'Concerts at the Ryman',
         'Big names in an intimate, historic hall. Build the weekend around a show you love.',
         'https://www.ryman.com/', 'Ryman calendar') +
    card('Pro hockey · Fall–spring', 'Nashville Predators',
         'NHL games at Bridgestone Arena, right on Broadway. A lively night out in season.') +
    card('Busy weekends', 'Festivals & big events',
         'Major festivals and conventions fill hotels and raise prices. Check the city calendar before booking.') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>Check the destination calendar when choosing a weekend, and confirm dates and tickets with the organizer.</p></div>'
    '<a class="button" href="https://www.visitmusiccity.com/" target="_blank" rel="noopener">Browse Nashville events</a></div></section>')

P.append('<section id="itinerary">' + head('07', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend: the Ryman, a show, two standout dinners and a quiet Sunday. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & unwind', [
        ('Midday arrival', 'Land at KJWN, subject to weather and your actual flight plan, and ride downtown.'),
        ('Afternoon', 'Ryman Auditorium tour.'),
        ('Evening', 'Dinner at Boqueria, then the honky-tonks on Lower Broadway.')]) +
    day('SAT', 'Music City', [
        ('Morning', 'Country Music Hall of Fame and Museum, with Hatch Show Print’s shop, then browse Fifth + Broadway and the boot shops.'),
        ('Afternoon', 'Couples treatment at Mokara Spa, or rest before the evening.'),
        ('Evening', 'Dinner at Locust, then the Grand Ole Opry or a Ryman concert.')]) +
    day('SUN', 'An easy departure', [
        ('Morning', 'A slow brunch and a stroll through Germantown.'),
        ('Before leaving', 'Ride back to KJWN with ample time for aircraft preparation.'),
        ('Fly home', 'A long leg: plan fuel, weather and daylight carefully.')]) +
    '</div></section>')

P.append('<section id="know">' + head('08', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    know([('Book in this order', 'Show tickets first, then hotel, Locust and the spa.'),
          ('A longer flight', 'About three hours from KMYR. Consider a fuel stop and a backup day for weather.'),
          ('Busy weekends', 'Bachelorette parties and festivals make Broadway crowded. Germantown is the quieter base.'),
          ('Dates come next', 'Hotel rates, show tickets and restaurant hours are date-dependent. No availability or live price is implied here.')]) +
    '</section>')

P.append(page_end(number=9, place='Nashville, Tennessee', reviewed=REVIEWED, note='Several picks have no website link because official addresses could not be confirmed; check each one, and confirm hours, prices and availability directly before booking.',
    credit_html='Nashville from Cumberland River September 2026 002 by King of Hearts, <a href="https://commons.wikimedia.org/wiki/File:Nashville_from_Cumberland_River_September_2026_002.jpg">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0">CC BY-SA 4.0</a>. Resized for display; adaptations shared under the same license.'))

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
