"""Generate docs/outer-banks/index.html."""
import json
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import card, head, explore, day, page_start, page_end, fbo, know  # noqa: E402

OUT = sys.argv[1]
PHOTO = json.load(open(__file__.rsplit("/", 1)[0] + '/photos.json'))['outer-banks']
NAV = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('explore', 'Explore'), ('spa', 'Spa'),
       ('events', 'Events'), ('itinerary', 'Itinerary')]
P = [page_start(
    slug='outer-banks', name='Outer Banks', state='North Carolina', number=11,
    description='A curated two-night Outer Banks getaway for GA pilots and their partners, from KMYR to KMQI. The Wright Brothers National Memorial, Jockey’s Ridge, Manteo’s waterfront and wild beaches.',
    lede='Fly to where flight began.',
    intro='On December 17, 1903, the Wright brothers flew here for the first time. Today the Outer Banks pairs that pilgrimage with wide, quiet beaches, the East Coast’s tallest dunes and Manteo’s small-town waterfront.',
    pills=['Aviation history', 'Beaches & dunes', 'Waterfront town'],
    photo=PHOTO['slug'], widths=PHOTO['widths'], alt=PHOTO['alt'], img_w=PHOTO['w'], img_h=PHOTO['h'],
    caption=PHOTO['caption'], airport='KMQI', nm=208, flight_time='~1 hr 39 <small>min</small>',
    style='Courtesy or rental car', nav=NAV)]

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Land on Roanoke Island.',
    'KMQI, Dare County Regional Airport, sits beside Manteo on Roanoke Island, with full services and room to park for the weekend.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>The airport FBO</h3>' +
    fbo('Dare County Regional Airport', '410 Airport Road, Manteo, NC 27954', '252-475-5575') +
    '<p class="note">The county-run FBO lists self-serve and full-serve 100LL, a courtesy car, crew cars and rental cars, plus a pilot lounge and showers. Ask about two-night parking, fees and after-hours access. CTAF/UNICOM 122.8. No live fuel price is shown.</p>'
    '<p class="note">Military restricted areas lie over the mainland west of Roanoke Island. Review the sectional and current NOTAMs, and expect strong coastal winds.</p>'
    '<p class="note"><strong>Bucket-list hop:</strong> First Flight Airport (KFFA) is a 3,000-foot strip inside the Wright Brothers National Memorial, about 15 minutes away by air. No fuel, VFR only, deer on the runway and a ditch off Runway 21. Older listings show a 24-hour parking limit; confirm current rules with the National Park Service and the Chart Supplement. Keep the airplane based at KMQI and make it a short visit.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>You’ll want a car.</h3><p>Manteo is walkable, but the memorial, Jockey’s Ridge and the beaches are 15–35 minutes away. Use the courtesy car for short trips or arrange a rental car for the weekend.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'Choose your kind of weekend.',
    'Stay in Manteo for an easy small-town base close to the airport, or in Duck for a resort on the sound.') +
    '<div class="grid three">' +
    card('Manteo · Romantic inn', 'The White Doe Inn',
         'A Victorian bed and breakfast in the middle of Manteo, walkable to the waterfront and restaurants. The classic romantic choice.') +
    card('Manteo · On the water', 'Tranquil House Inn',
         'A waterfront inn on Shallowbag Bay with its own restaurant, 1587. Minutes from the airport.') +
    card('Duck · Resort & spa', 'The Sanderling Resort',
         'A soundfront resort in Duck with a spa, beach access and sunset views. Choose it for a more indulgent weekend; about 35 minutes from the airport.') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Two dinners. One relaxed lunch.',
    'Seafood is the point. Reserve weekend dinners, especially in summer.') +
    '<div class="grid three">' +
    card('Friday dinner · Manteo', '1587 Restaurant & Lounge',
         'Fresh seafood, cocktails and an intimate room at the Tranquil House Inn, overlooking the water. An easy first night close to the airport.') +
    card('Saturday dinner · Duck', 'Blue Point',
         'One of the Outer Banks’ best-known upscale restaurants, on the sound in Duck. Time it for sunset.') +
    card('Lunch · Manteo waterfront', 'Salt & Cypress Kitchen',
         'A newer waterfront restaurant in Manteo. For an Outer Banks classic instead, try Owens’ Restaurant in Nags Head.') +
    '</div></section>')

P.append('<section id="explore">' + head('04', 'Things to do', 'Stand where it happened.',
    'Start with the memorial, then let the beaches and dunes set the pace.') +
    '<div class="explore-list">' +
    explore(1, 'Wright Brothers National Memorial',
            'Walk the first-flight path, with markers for each of the four 1903 flights, see the reconstructed camp buildings and climb Big Kill Devil Hill to the granite monument. The visitor center has a full-size reproduction of the 1903 Flyer.',
            'https://www.nps.gov/wrbr/', 'Park information') +
    explore(2, 'Jockey’s Ridge State Park',
            'The tallest living sand dune system on the East Coast, in Nags Head. Climb it at sunset; take shoes, as the sand gets hot.') +
    explore(3, 'Manteo waterfront',
            'A boardwalk, shops and the reconstructed Roanoke Marshes Lighthouse on Shallowbag Bay. Lovely in the evening.') +
    explore(4, 'The Lost Colony & Elizabethan Gardens',
            'On Roanoke Island near the airport: the long-running outdoor drama about the 1587 colony (summer) and formal gardens beside it.') +
    explore(5, 'Bodie Island Lighthouse',
            'A striped lighthouse in Cape Hatteras National Seashore, about 25 minutes south. Check whether climbs are open.') +
    '</div>')

P.append('<div id="spa" class="couples"><span class="eyebrow">Optional / Spa & relaxation</span><h3>The spa at The Sanderling · Time for two</h3>'
    '<p>The Sanderling Resort in Duck has a full-service spa. A couples treatment pairs well with dinner at Blue Point nearby.</p>'
    '<p><strong>Booking:</strong> Ask about couples treatments, access for non-resort guests, current pricing and cancellation policy. No prices are shown here, and no appointment has been booked.</p></div></section>')

P.append('<section id="events">' + head('05', 'What’s happening', 'Sometimes the date is the reason to fly.',
    'This prototype links to the destination calendar. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('December 17', 'First Flight anniversary',
         'Each year the memorial marks the Wright brothers’ first flight, often with aviation guests and a flyover. A special date for pilots; check the park’s plans.') +
    card('Summer', 'The Lost Colony',
         'America’s long-running outdoor symphonic drama on Roanoke Island. Summer evenings only.') +
    card('Spring & fall', 'Best seasons',
         'Mild weather, quieter beaches and lower rates. Summer is busy and hot; hurricane season runs June–November.') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>Check the destination calendar when choosing a weekend, and confirm dates and tickets with the organizer.</p></div>'
    '<a class="button" href="https://www.outerbanks.org/" target="_blank" rel="noopener">Browse Outer Banks events</a></div></section>')

P.append('<section id="itinerary">' + head('06', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend: the first-flight pilgrimage, sunset on the dunes and two seafood dinners. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & unwind', [
        ('Late-morning arrival', 'Land at KMQI, subject to weather and your actual flight plan, and pick up the car.'),
        ('Afternoon', 'Lunch on the Manteo waterfront and a walk to the Roanoke Marshes Lighthouse. Check in.'),
        ('Evening', 'Dinner at 1587.')]) +
    day('SAT', 'Where flight began', [
        ('Morning', 'Wright Brothers National Memorial: the visitor center, the flight markers and the climb to the monument.'),
        ('Afternoon', 'Beach time, or a spa treatment at The Sanderling.'),
        ('Evening', 'Sunset from the top of Jockey’s Ridge, then dinner at Blue Point.')]) +
    day('SUN', 'An easy departure', [
        ('Morning', 'The Elizabethan Gardens or Bodie Island Lighthouse.'),
        ('Before leaving', 'Return the car and allow time at the FBO; coastal winds can pick up through the day.'),
        ('Fly home', 'Let weather and your flight plan set the departure.')]) +
    '</div></section>')

P.append('<section id="know">' + head('07', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    know([('Book in this order', 'Car and lodging first, then dinners and any spa time.'),
          ('Coastal weather', 'Strong winds and fast-moving storms are common. Build in a backup day.'),
          ('Hurricane season', 'June through November. Watch the tropics and keep plans flexible.'),
          ('Dates come next', 'Rates, show tickets and restaurant hours are date-dependent. No availability or live price is implied here.')]) +
    '</section>')

P.append(page_end(number=11, place='Outer Banks, North Carolina', note='Several picks have no website link because official addresses could not be confirmed; check each one, and confirm hours, prices and availability directly before booking.',
    credit_html=PHOTO['credit_html']))

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
