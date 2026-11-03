"""Generate docs/cape-may/index.html (Cape May, New Jersey)."""
import json
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import card, head, explore, day, page_start, page_end, fbo, know  # noqa: E402

OUT = sys.argv[1]
REVIEWED = None  # owner review date; None while still a draft
PHOTO = json.load(open(__file__.rsplit("/", 1)[0] + '/photos.json'))['cape-may']
NAV = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('explore', 'Explore'), ('spa', 'Spa'),
       ('events', 'Events'), ('itinerary', 'Itinerary')]
P = [page_start(
    slug='cape-may', name='Cape May', state='New Jersey', number=26, reviewed=REVIEWED,
    description='A curated two-night Cape May getaway for GA pilots and their partners, from KMYR to KWWD. Victorian inns, beach walks, the lighthouse, wineries and a naval aviation museum on the field.',
    lede='Victorian porches, the beach and a hangar full of history.',
    intro='At the southern tip of New Jersey, Cape May is a seaside town of painted Victorian houses, wide beaches and long porches. Land beside a World War II hangar that is now an aviation museum, walk the historic district, watch the sunset at Cape May Point, and finish with dinner at a grand old hotel.',
    pills=['Victorian inns', 'Beaches', 'Aviation museum'],
    photo=PHOTO['slug'], widths=PHOTO['widths'], alt=PHOTO['alt'], img_w=PHOTO['w'], img_h=PHOTO['h'],
    caption=PHOTO['caption'], airport='KWWD', nm=374, flight_time='~2 hr 45 <small>min</small>',
    style='Rental car or taxi + walks', nav=NAV)]

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Land at a Navy field, minutes from the beach.',
    'KWWD, Cape May County Airport, was Naval Air Station Wildwood in World War II. It sits about 15 minutes north of Cape May’s historic district.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>The FBO</h3>' +
    fbo('FlightLevel Aviation · Cape May', '201 Forrestal Road, Rio Grande, NJ 08242', '609-889-0750', 'https://www.flightlevelaviation.com/?p=351') +
    '<p class="note">FlightLevel lists hours of 8 a.m. to 5 p.m. daily; after-hours fuel or service needs at least an hour’s notice and costs extra. Ask about rental cars, two-night parking and fees. No live fuel price is shown.</p>'
    '<p class="note">Atlantic City’s Class C airspace lies to the north, and military warning areas lie offshore. Coastal fog and sea breezes are common. Review the sectional and current NOTAMs.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>Walk once you arrive.</h3><p>Cape May’s historic district, beach and restaurants are walkable, and many inns lend bikes. Use a rental car or taxi to get from the airport and out to Cape May Point.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'Choose your porch.',
    'A grand hotel, a small luxury hotel or a classic Victorian. Rates and availability need travel dates.') +
    '<div class="grid three">' +
    card('Grand hotel · On the beach', 'Congress Hall',
         'Cape May’s landmark hotel, across from the beach, with a long colonnaded porch, the Sea Spa and the Blue Pig Tavern. The classic choice.',
         'https://www.caperesorts.com/congress-hall') +
    card('Boutique · Historic district', 'The Virginia Hotel',
         'A small, elegant 1879 hotel on Jackson Street, a block from the beach, home to The Ebbitt Room. The romantic choice.',
         'https://www.caperesorts.com/virginia-hotel') +
    card('Victorian · Seasonal', 'The Chalfonte Hotel',
         'A rambling 1876 hotel with wraparound porches and Southern cooking, open in the warmer months. Old-fashioned charm.',
         'https://www.chalfonte.com/') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Two dinners. One dockside lunch.',
    'Seafood and porches. Reserve weekend dinners, especially in summer.') +
    '<div class="grid three">' +
    card('Friday dinner · The Virginia', 'The Ebbitt Room',
         'Refined farm-to-table dining in The Virginia Hotel, much of it from the hotel’s own farm. Intimate and romantic.',
         'https://www.caperesorts.com/virginia-hotel/ebbittroom') +
    card('Saturday dinner · Oceanfront', 'Peter Shields Inn & Restaurant',
         'A candlelit dining room in a 1907 Georgian Revival mansion across from the beach. Go for sunset.',
         'https://www.petershieldsinn.com/') +
    card('Lunch · Fishing docks', 'The Lobster House',
         'A long-running restaurant on the working docks of Cape May harbor, with a raw bar and a schooner bar. Casual and fun.',
         'https://thelobsterhouse.com/') +
    '</div></section>')

P.append('<section id="explore">' + head('04', 'Things to do', 'Victorians, the lighthouse and a Navy hangar.',
    'Choose one outing a day and leave time for the beach.') +
    '<div class="explore-list">' +
    explore(1, 'Naval Air Station Wildwood Aviation Museum',
            'On the airport in Hangar No. 1, a restored World War II wooden hangar with aircraft, engines and exhibits on the dive-bomber squadrons that trained here. Listed as open daily from March through December; walk over from the FBO.',
            'https://usnasw.org/', 'Museum information') +
    explore(2, 'The Victorian historic district',
            'Hundreds of restored Victorian houses on shaded streets. Take a trolley or walking tour, and visit the Emlen Physick Estate.',
            'https://capemaymac.org/', 'Tours and tickets') +
    explore(3, 'Cape May Point & the lighthouse',
            'Climb the 1859 Cape May Lighthouse, walk the state park, then watch the sunset at Sunset Beach, where the wreck of a concrete ship sits just offshore.') +
    explore(4, 'Wineries',
            'Cape May has a small, growing wine country a short drive from town, with tastings, vineyard views and summer music.') +
    explore(5, 'Washington Street Mall & the beach',
            'Three pedestrian blocks of shops and cafés, a short walk from the beach promenade.') +
    '</div>')

P.append('<div id="spa" class="couples"><span class="eyebrow">Optional / Spa & relaxation</span><h3>The Sea Spa at Congress Hall · Time for two</h3>'
    '<p>Congress Hall’s spa offers couples treatments a short walk from the beach. <a href="https://www.caperesorts.com/congress-hall/sea-spa" target="_blank" rel="noopener">Sea Spa details</a>.</p>'
    '<p><strong>Booking:</strong> Ask about couples treatments, access for non-hotel guests, current pricing and cancellation policy. No prices are shown here, and no appointment has been booked.</p></div></section>')

P.append('<section id="events">' + head('05', 'What’s happening', 'Sometimes the season is the reason to fly.',
    'This prototype links to the town visitor site. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('September–October', 'Fall migration',
         'Cape May is one of North America’s great places to watch migrating hawks, songbirds and monarch butterflies. Quieter beaches, too.') +
    card('October', 'Victorian Weekend',
         'House tours, period costumes and events across the historic district. Book early.') +
    card('December', 'Christmas in Cape May',
         'Candlelight house tours, trolley rides and decorated Victorians. A festive winter weekend.') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>Check the town calendar when choosing a weekend, and confirm dates and tickets with the organizer.</p></div>'
    '<a class="button" href="https://www.capemay.com/" target="_blank" rel="noopener">Browse Cape May events</a></div></section>')

P.append('<section id="itinerary">' + head('06', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend: the hangar, the beach, the lighthouse and two seaside dinners. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & the hangar', [
        ('Late-morning arrival', 'Land at KWWD, subject to weather and your actual flight plan.'),
        ('Afternoon', 'The NAS Wildwood Aviation Museum, then check in and walk to the beach.'),
        ('Evening', 'Dinner at The Ebbitt Room.')]) +
    day('SAT', 'Victorians & the Point', [
        ('Morning', 'A historic district tour and the Physick Estate.'),
        ('Afternoon', 'Lunch at The Lobster House, then the lighthouse, a winery or the spa.'),
        ('Evening', 'Sunset at Sunset Beach, then dinner at Peter Shields Inn.')]) +
    day('SUN', 'An easy departure', [
        ('Morning', 'A beach walk and breakfast on a porch.'),
        ('Before leaving', 'Allow time at the FBO.'),
        ('Fly home', 'Coastal fog can linger in the morning; let weather set the departure.')]) +
    '</div></section>')

P.append('<section id="know">' + head('07', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    know([('Book in this order', 'Lodging first, then dinners and a car.'),
          ('Summer', 'July and August are busy and many inns require multi-night stays. Spring and fall are easier.'),
          ('Coastal weather', 'Sea fog and gusty sea breezes are common. Keep a backup day.'),
          ('Seasonal places', 'Some inns and restaurants close in winter. Check before an off-season trip.')]) +
    '</section>')

P.append(page_end(number=26, place='Cape May, New Jersey', reviewed=REVIEWED, note='Several picks have no website link because official addresses could not be confirmed; check each one, and confirm hours, prices and availability directly before booking.',
    credit_html=PHOTO['credit_html']))

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
