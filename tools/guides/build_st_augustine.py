"""Generate docs/st-augustine/index.html."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import card, head, explore, day, page_start, page_end, fbo, know  # noqa: E402

OUT = sys.argv[1]
NAV = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('explore', 'Explore'), ('spa', 'Spa'),
       ('wine', 'Wine & spirits'), ('events', 'Events'), ('itinerary', 'Itinerary')]
P = [page_start(
    slug='st-augustine', name='St. Augustine', state='Florida', number=6,
    description='A curated two-night St. Augustine getaway for GA pilots and their partners, from KMYR to KSGJ. A Spanish fort, Gilded Age hotels, bayfront dining and a winery downtown.',
    lede='The oldest city. A long weekend’s worth of stories.',
    intro='Coquina walls, narrow Spanish streets, Henry Flagler’s grand hotels and sunsets over Matanzas Bay. St. Augustine is the longest flight in this collection from KMYR and one of the most rewarding.',
    pills=['History', 'Bayfront', 'Dining'],
    photo='st-augustine', widths=[480, 960], alt='St. Augustine and its waterfront viewed from the lighthouse', img_w=960, img_h=720,
    caption='The view from the St. Augustine Lighthouse', airport='KSGJ', nm=255, flight_time='~1 hr 57 <small>min</small>',
    style='Rideshare + walks', estimate_extra='Coastal Florida afternoon storms can build quickly in summer. ', nav=NAV)]

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Land, then head for the old city.',
    'KSGJ, Northeast Florida Regional Airport, is a towered field about 15–20 minutes north of the historic district.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>Full service or self-serve</h3>' +
    fbo('Atlantic Aviation', 'Full-service FBO', '904-824-1995', 'https://www.atlanticaviation.com/location/SGJ') +
    '<p class="note">Atlantic Aviation is the FBO. Directory listings also show self-serve 100LL on the field. Ask Atlantic about facility fees, two-night parking, waivers with fuel and after-hours fees. Prices vary widely between listings, so call ahead; no live price is shown.</p>'
    '<p class="note">The airport authority can be reached at 904-209-0090.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>Ride in. Walk the old city.</h3><p>Rideshare or a taxi to the historic district takes about 15–20 minutes. Once there, everything in this guide is walkable or a short trolley ride.</p><p>Parking downtown is tight, so a rental car is only worth it if you plan to visit the beaches.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'Choose your kind of weekend.',
    'Three different stays in the historic district. Rates and availability need travel dates.') +
    '<div class="grid three">' +
    card('Grand historic hotel · Spa', 'Casa Monica Resort & Spa',
         'An 1888 Moorish Revival landmark across from the Flagler buildings, now part of Marriott’s Autograph Collection, with a full-service spa. The splurge choice.',
         'https://www.casamonica.com/') +
    card('Adults-only · Historic houses', 'The Collector Luxury Inn & Gardens',
         'A collection of restored historic houses around courtyard gardens, adults-only and quiet, a few minutes’ walk from the plaza.',
         'https://www.thecollectorinn.com/') +
    card('Classic inn · Oldest in town', 'St. Francis Inn',
         'A long-running bed and breakfast in one of the city’s oldest buildings, on a quiet street in the historic district. Classic B&B charm.',
         'https://stfrancisinn.com/') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Two dinners. One long lunch.',
    'The historic district is busy on weekends, so reserve your anchor dinner early.') +
    '<div class="grid three">' +
    card('Friday dinner · Intimate', 'Collage',
         'A small, romantic restaurant known for globally inspired cooking and live piano. The classic St. Augustine date night. Reserve well ahead.',
         'https://collagestaug.com/') +
    card('Saturday dinner · Lively', 'The Ice Plant Bar',
         'A restored 1920s ice plant with craft cocktails and a farm-to-table menu, in the same building as the St. Augustine Distillery. Fun and buzzy rather than quiet.') +
    card('Lunch · Spanish-Cuban', 'The Columbia',
         'A long-running Spanish and Cuban restaurant on St. George Street. A leisurely lunch between sights; try the 1905 salad.',
         'https://www.columbiarestaurant.com/historic-district-st-augustine') +
    '</div></section>')

P.append('<section id="explore">' + head('04', 'Things to do', 'Walk five centuries.',
    'Choose a few memorable experiences; the old city is compact enough to wander between them.') +
    '<div class="explore-list">' +
    explore(1, 'Castillo de San Marcos',
            'The 17th-century Spanish stone fort on the bay, a National Park Service site. Go early or late in the day to avoid the heat and crowds.',
            'https://www.nps.gov/casa/', 'Park information') +
    explore(2, 'St. Augustine Lighthouse & Maritime Museum',
            'Climb the striped lighthouse for the view in this guide’s photo, then explore the maritime museum. Across the bridge on Anastasia Island.',
            'https://www.staugustinelighthouse.org/', 'Lighthouse information') +
    explore(3, 'Flagler College & the Gilded Age',
            'Henry Flagler’s 1888 Hotel Ponce de Leon is now Flagler College. Ask about guided historic tours of its Tiffany-glass dining hall and grand rotunda.') +
    explore(4, 'St. George Street & Lincolnville',
            'The pedestrian heart of the old city, busy by day. For a quieter walk, wander Lincolnville’s historic streets or the bayfront at sunset.') +
    explore(5, 'Sunset on Matanzas Bay',
            'Several operators run sunset sails and cruises from the downtown marina. Choose one water outing and book a day or two ahead.') +
    '</div>')

P.append('<div id="spa" class="couples"><span class="eyebrow">Optional / Spa & relaxation</span><h3>The spa at Casa Monica · Time for two</h3>'
    '<p>Casa Monica Resort & Spa has a full-service spa in the heart of the historic district, a good fit for a couples treatment after a morning of walking.</p>'
    '<p><strong>Booking:</strong> Ask about couples treatments, access for non-hotel guests, current pricing, gratuity and cancellation policy. No prices are shown here because they change, and no appointment has been booked.</p>'
    '<p>Optional Saturday afternoon, before dinner.</p>'
    '<a href="https://www.casamonica.com/" target="_blank" rel="noopener">Spa details</a></div></section>')

P.append('<section id="wine">' + head('05', 'Wine & spirits', 'A glass, and no hurry.',
    'Two downtown tasting stops, both walkable from the historic district.') +
    '<div class="grid three">' +
    card('King Street · Winery', 'San Sebastian Winery',
         'A working winery at 157 King Street with tours and tastings of Florida wines, plus a rooftop bar. Check tour times and the rooftop’s hours.',
         'https://www.sansebastianwinery.com/') +
    card('Distillery · Tours', 'St. Augustine Distillery',
         'Craft spirits made in the restored ice plant, with distillery tours and tastings. Pair it with dinner upstairs at the Ice Plant Bar.',
         'https://www.staugustinedistillery.com/') +
    '</div></section>')

P.append('<section id="events">' + head('06', 'What’s happening', 'Sometimes the event is the reason to fly.',
    'This prototype links to the destination calendar. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('Mid-November to January', 'Nights of Lights',
         'Millions of white lights across the historic district, a much-loved holiday tradition. Beautiful and crowded; book lodging early.',
         'https://www.visitstaugustine.com/event/nights-lights') +
    card('Spring & fall', 'Best seasons',
         'Comfortable walking weather. Summer is hot and humid, with afternoon thunderstorms that can affect flights.') +
    card('Year-round', 'Concerts & festivals',
         'Music at the St. Augustine Amphitheatre and festivals through the year. Check the calendar for your dates.') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>Check the destination calendar when choosing a weekend, and confirm dates and tickets with the organizer.</p></div>'
    '<a class="button" href="https://www.floridashistoriccoast.com/" target="_blank" rel="noopener">Browse St. Augustine events</a></div></section>')

P.append('<section id="itinerary">' + head('07', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend: the fort, the Flagler buildings, a sunset on the bay and two very different dinners. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & unwind', [
        ('Midday arrival', 'Land at KSGJ, subject to weather and your actual flight plan, and ride into the old city.'),
        ('Afternoon', 'Lunch at The Columbia, then a slow walk down St. George Street. Check in when your room is ready.'),
        ('Evening', 'Dinner at Collage if reserved.')]) +
    day('SAT', 'Fort, hotels & bay', [
        ('Morning', 'Castillo de San Marcos when it opens, then a Flagler College tour.'),
        ('Afternoon', 'San Sebastian Winery tasting, or a couples treatment at Casa Monica. Late afternoon: the lighthouse climb.'),
        ('Evening', 'Sunset on Matanzas Bay, then dinner at the Ice Plant Bar.')]) +
    day('SUN', 'An easy departure', [
        ('Morning', 'Breakfast and a quiet walk through Lincolnville or along the bayfront.'),
        ('Before leaving', 'Check out and allow ample time at the FBO.'),
        ('Fly home', 'Plan around afternoon storms in warm months; a morning departure is often smoother.')]) +
    '</div></section>')

P.append('<section id="know">' + head('08', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    know([('Book in this order', 'Lodging first, then the Friday dinner, a Flagler College tour and one water outing.'),
          ('Allow for the season', 'Summer heat and daily storms; holiday lights season is crowded. Spring and fall are easiest.'),
          ('Wear good shoes', 'Old streets are uneven, and the lighthouse has a lot of steps.'),
          ('Dates come next', 'Hotel rates, tours and restaurant hours are date-dependent. No availability or live price is implied here.')]) +
    '</section>')

P.append(page_end(number=6, place='St. Augustine, Florida',
    credit_html='St. Aug from lighthouse west01 by Ebyabe, <a href="https://commons.wikimedia.org/wiki/File:St._Aug_from_lighthouse_west01.jpg">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0/">CC BY-SA 3.0</a>. Resized for display; adaptations shared under the same license.'))

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
