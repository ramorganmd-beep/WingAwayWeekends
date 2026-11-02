"""Generate docs/key-west/index.html."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import card, head, explore, day, page_start, page_end, fbo, know  # noqa: E402

OUT = sys.argv[1]
NAV = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('explore', 'Explore'),
       ('events', 'Events'), ('itinerary', 'Itinerary')]
P = [page_start(
    slug='key-west', name='Key West', state='Florida', number=10,
    description='A curated getaway to Key West for GA pilots and their partners, from KMYR to KEYW. Sunset at Mallory Square, adults-only guesthouses, Pan Am’s first office and a seaplane to the Dry Tortugas.',
    lede='The end of the road. The start of Pan Am.',
    intro='Palm-lined streets, Victorian guesthouses, sunsets over the Gulf and the town where Pan American Airways sold its first tickets. Key West is the longest flight in this collection, so it shines as a longer stay.',
    pills=['Island evenings', 'Aviation history', 'On the water'],
    photo='key-west-duval', widths=[480, 960, 1600], alt='Palm-lined Duval Street in Key West', img_w=960, img_h=688,
    caption='Duval Street', airport='KEYW', nm=567, flight_time='~4 hr 2 <small>min</small>',
    style='On foot + bikes', estimate_extra='At about four hours from KMYR, most piston aircraft will need a fuel stop. The route includes long stretches over water. ', nav=NAV)]

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Plan this one carefully.',
    'KEYW, Key West International, is a towered airline airport at the end of the Keys, with restricted and military airspace nearby (Naval Air Station Key West).') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>One FBO</h3>' +
    fbo('Signature Aviation', '3471 S. Roosevelt Blvd., Key West, FL 33040', '305-296-5422') +
    '<p class="note">Signature is the only FBO, and Key West is among the more expensive stops in this collection. Recent pilot reports describe 100LL above $11 a gallon, overnight parking around $125 a night for a single-engine aircraft and a hefty fee for departures after the FBO closes at 9 PM. Confirm every fee before you go; no live price is shown.</p>'
    '<p class="note">Review restricted and warning areas, NAS Key West traffic, overwater equipment (life vests, raft) and any special procedures for flights along the Keys. A fuel stop on the mainland is the norm.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>Taxi in. Walk or bike.</h3><p>Old Town is about 10 minutes by taxi. Once there, walk or rent bikes; parking is scarce and a car is rarely needed.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'Choose your kind of weekend.',
    'Adults-only guesthouses are Key West’s sweet spot for couples. Rates and availability need travel dates; winter is peak season.') +
    '<div class="grid three">' +
    card('Adults-only guesthouse', 'The Marquesa',
         'Restored historic houses around pools and gardens in Old Town, with its own restaurant, Hot Tin Roof. Quiet, romantic and walkable.') +
    card('Grand hotel · On the beach', 'Casa Marina',
         'A historic 1920s grand hotel on its own beach, now part of Hilton’s Curio Collection. Choose it for beach time and a classic resort feel.') +
    card('Small & adults-only', 'H2O Suites or Almond Tree Inn',
         'Two other adults-only boutique options often recommended for couples. Compare rooms and location for your dates.') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Two dinners by the water.',
    'Sunset tables book up. Reserve the special dinner first.') +
    '<div class="grid three">' +
    card('The romantic dinner', 'Latitudes, Sunset Key',
         'Oceanfront dining on a small island a short boat ride from Old Town. Often called the most romantic table in Key West; the launch is part of the evening.') +
    card('In Old Town', 'Hot Tin Roof',
         'The Marquesa’s restaurant, a favorite for a polished, relaxed dinner within walking distance of Duval Street.') +
    card('Aviation history · Casual', 'First Flight Island Restaurant & Brewery',
         'At 301 Whitehead Street, in the building where Pan American Airways sold its first tickets in 1927. Lunch with a story.') +
    '</div></section>')

P.append('<section id="explore">' + head('04', 'Things to do', 'Sunsets, seaplanes and stories.',
    'Choose one big outing and let island time do the rest.') +
    '<div class="explore-list">' +
    explore(1, 'Seaplane to the Dry Tortugas',
            'Fly about 70 miles west by floatplane to Fort Jefferson in Dry Tortugas National Park. Key West Seaplane Adventures is the only seaplane operator. Book well ahead; the ferry is the slower alternative.') +
    explore(2, 'Pan Am’s first office',
            'Pan American Airways began Key West–Havana mail flights in October 1927. Stop at 301 Whitehead Street, now a restaurant, to see where it all began.') +
    explore(3, 'Sunset at Mallory Square',
            'The nightly sunset celebration with street performers on the harbor. Arrive early, or watch from a quieter rooftop or a sunset sail.') +
    explore(4, 'Old Town on foot or by bike',
            'Victorian houses, hidden lanes and the Hemingway Home and Museum. Rent bikes for an easy loop.') +
    '</div></section>')

P.append('<section id="events">' + head('05', 'What’s happening', 'Sometimes the event is the reason to fly.',
    'This prototype links to the destination calendar. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('December–April', 'Peak season',
         'The best weather and the highest prices. Book lodging and the seaplane early.') +
    card('June–November', 'Hurricane season',
         'Lower rates, more heat and storm risk. Keep plans flexible and watch the tropics.') +
    card('Year-round', 'Festivals',
         'Key West hosts festivals through the year that fill hotels. Check the calendar before booking.') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>Check the destination calendar when choosing dates, and confirm details with the organizer.</p></div>'
    '<a class="button" href="https://fla-keys.com/keywest/" target="_blank" rel="noopener">Browse Key West events</a></div></section>')

P.append('<section id="itinerary">' + head('06', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday version. Given the flight, Key West works best as a longer stay; choose Longer stay on the homepage to see an extra day. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & unwind', [
        ('Midday arrival', 'Land at KEYW after a mainland fuel stop, subject to weather and your actual flight plan. Taxi to Old Town.'),
        ('Afternoon', 'Lunch at First Flight, then a bike loop through Old Town.'),
        ('Evening', 'Sunset at Mallory Square, then dinner at Hot Tin Roof.')]) +
    day('SAT', 'Seaplane day', [
        ('Morning', 'Seaplane to the Dry Tortugas: Fort Jefferson, snorkeling and the flight itself.'),
        ('Afternoon', 'Back in town by mid-afternoon; pool time at your guesthouse.'),
        ('Evening', 'The launch to Sunset Key for dinner at Latitudes.')]) +
    day('SUN', 'An easy departure', [
        ('Morning', 'Breakfast and the Hemingway Home.'),
        ('Before leaving', 'Get to the FBO with time to spare; late departures cost extra.'),
        ('Fly home', 'A long trip with a fuel stop. Plan for afternoon storms and daylight.')]) +
    '</div></section>')

P.append('<section id="know">' + head('07', 'Good to know', 'Keep the trip easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    know([('Book in this order', 'FBO parking, lodging and the seaplane first, then Latitudes.'),
          ('A serious cross-country', 'Four hours, a fuel stop and overwater flying. Build in a weather day.'),
          ('Allow for the season', 'Winter is ideal and busy; summer and fall bring heat, storms and hurricane risk.'),
          ('Dates come next', 'Rates, fees and tour availability are date-dependent. No availability or live price is implied here.')]) +
    '</section>')

P.append(page_end(number=10, place='Key West, Florida', note='Several picks have no website link because official addresses could not be confirmed; check each one, and confirm hours, prices and availability directly before booking.',
    credit_html='KeyWestFL Duval St 20230125 by Niranjan Arminius, <a href="https://commons.wikimedia.org/wiki/File:KeyWestFL_Duval_St_20230125.jpg">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0">CC BY-SA 4.0</a>. Resized for display; adaptations shared under the same license.'))

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
