"""Generate docs/st-michaels/index.html (St. Michaels, Easton and Oxford, Maryland)."""
import json
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import card, head, explore, day, page_start, page_end, fbo, know  # noqa: E402

OUT = sys.argv[1]
REVIEWED = 'November 3, 2026'  # owner review date; None while still a draft
PHOTO = json.load(open(__file__.rsplit("/", 1)[0] + '/photos.json'))['st-michaels']
NAV = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('explore', 'Explore'), ('spa', 'Spa'),
       ('events', 'Events'), ('itinerary', 'Itinerary')]
P = [page_start(
    slug='st-michaels', name='St. Michaels & Easton', state='Maryland', number=25, reviewed=REVIEWED,
    description='A curated two-night Chesapeake Bay getaway in St. Michaels, Easton and Oxford for GA pilots and their partners, from KMYR to KESN. A waterfront inn, crab houses, the Maritime Museum and the Oxford ferry.',
    lede='Crabs, sailboats and a waterfront inn.',
    intro='On Maryland’s Eastern Shore, the old harbor towns of St. Michaels and Oxford sit on quiet creeks off the Chesapeake Bay, with historic Easton a short drive inland. Stay at a waterfront inn, pick crabs on the harbor, ride the little Oxford ferry, and watch the sunset from the deck of a sailboat.',
    pills=['Waterfront inns', 'Chesapeake crabs', 'Maritime history'],
    photo=PHOTO['slug'], widths=PHOTO['widths'], alt=PHOTO['alt'], img_w=PHOTO['w'], img_h=PHOTO['h'],
    caption=PHOTO['caption'], airport='KESN', nm=337, flight_time='~2 hr 30 <small>min</small>',
    style='Courtesy or rental car', nav=NAV)]

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Land in Easton, drive to the water.',
    'KESN, Easton/Newnam Field, is a towered airport just north of Easton, about 20 minutes from St. Michaels and Oxford.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>The FBO</h3>' +
    fbo('Maryland Air · Easton/Newnam Field', '29137 Newnam Road, Suite 5, Easton, MD 21601', '410-822-0400') +
    '<p class="note">Directories list a courtesy car and rental cars at Maryland Air. Easton Jet Service (410-820-8770), also on the field, lists a rental car office on site. Ask about two-night parking and fees. No live fuel price is shown.</p>'
    '<p class="note">The Washington, DC SFRA lies across the Bay to the west, and Patuxent River and Dover have busy military airspace nearby. Review the sectional, restricted areas and current NOTAMs and TFRs.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>A car, then bikes.</h3><p>Rent a car for the weekend. St. Michaels and Oxford are small and walkable, and the flat country roads are made for bikes, rented in town.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'Choose your stretch of shoreline.',
    'A celebrated waterfront inn, a grand historic hotel or a relaxed island hideaway. Rates and availability need travel dates.') +
    '<div class="grid three">' +
    card('St. Michaels · Waterfront luxury', 'Inn at Perry Cabin',
         'A luxury inn on the Miles River at the edge of St. Michaels, with gardens, a spa and Stars restaurant. The romantic splurge.',
         'https://innatperrycabin.com/') +
    card('Easton · Historic', 'The Tidewater Inn',
         'A classic 1949 hotel with 86 rooms in the middle of Easton, home to Hunters’ Tavern and an easy walk to shops and the Avalon Theatre. The inn was listed for sale in 2026; confirm details when you book.',
         'https://tidewaterinn.com/') +
    card('Tilghman Island · Waterfront', 'The Wylder Hotel',
         'A relaxed waterfront hotel in an 1898 boarding house on nine acres of Tilghman Island, about 15 minutes past St. Michaels, with Tickler’s Crab Shack and sunset views over the Bay.',
         'https://wylderhotels.com/tilghman-island/') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Two dinners. One crab feast.',
    'Blue crabs are the point from late spring to fall. Reserve weekend dinners.') +
    '<div class="grid three">' +
    card('Friday dinner · Easton', 'Bas Rouge',
         'Refined contemporary European dining in an intimate room in downtown Easton. The special-occasion dinner.',
         'https://www.basrougeeaston.com/') +
    card('Saturday dinner · Perry Cabin', 'Stars',
         'Locally inspired cooking at Inn at Perry Cabin, inside or on the terrace overlooking the river. Go early for sunset.',
         'https://innatperrycabin.com/dining/stars/') +
    card('Lunch · St. Michaels harbor', 'The Crab Claw',
         'A St. Michaels institution on the harbor, where you pick steamed crabs at picnic tables by the water. Seasonal; check that it is open.',
         'https://www.thecrabclaw.com/') +
    '</div></section>')

P.append('<section id="explore">' + head('04', 'Things to do', 'Boats, a ferry and a lighthouse.',
    'Slow and easy. Leave time to sit by the water.') +
    '<div class="explore-list">' +
    explore(1, 'Chesapeake Bay Maritime Museum',
            'A waterfront campus in St. Michaels with the 1879 Hooper Strait Lighthouse, working boatyards and historic Bay boats. Allow two hours.',
            'https://cbmm.org/', 'Museum information') +
    explore(2, 'The Oxford–Bellevue Ferry',
            'One of the oldest privately operated ferries in the country, crossing the Tred Avon River between Bellevue and Oxford. Ride it with bikes or the car for a loop to Oxford. Seasonal.',
            'https://www.oxfordferry.com/', 'Ferry schedule') +
    explore(3, 'Oxford',
            'A tiny, quiet town of shaded streets, boatyards and a little beach on the Tred Avon. Lovely for a slow afternoon.') +
    explore(4, 'A sail on the Bay',
            'Sunset sails and skipjack cruises leave from St. Michaels and Tilghman Island in season.') +
    explore(5, 'Downtown Easton',
            'Brick sidewalks, galleries, the Academy Art Museum and the restored Avalon Theatre.') +
    '</div>')

P.append('<div id="spa" class="couples"><span class="eyebrow">Optional / Spa & relaxation</span><h3>The Spa at Perry Cabin · Time for two</h3>'
    '<p>The inn’s spa has a private couples suite, a steam room and a relaxation lounge with an outdoor terrace.</p>'
    '<p><strong>Booking:</strong> Ask about couples treatments, access for non-inn guests, current pricing and cancellation policy. No prices are shown here, and no appointment has been booked.</p></div></section>')

P.append('<section id="events">' + head('05', 'What’s happening', 'Sometimes the season is the reason to fly.',
    'This prototype links to the county visitor site. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('November', 'Waterfowl Festival',
         'Easton’s big wildlife art and decoy festival, usually the second weekend of November. Fun and busy; book early.') +
    card('July', 'Plein Air Easton',
         'One of the country’s largest outdoor painting competitions, with artists painting all over town.') +
    card('May–October', 'Crab and sailing season',
         'The best months for crabs, sails and waterfront dining. Summer is warm and busy, with afternoon storms.') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>Check the county visitor site when choosing a weekend, and confirm dates and tickets with the organizer.</p></div>'
    '<a class="button" href="https://tourtalbot.org/" target="_blank" rel="noopener">Browse Talbot County events</a></div></section>')

P.append('<section id="itinerary">' + head('06', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend: the harbor, the ferry and two waterfront dinners. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & Easton', [
        ('Late-morning arrival', 'Land at KESN, subject to weather and your actual flight plan, and pick up the car.'),
        ('Afternoon', 'Check in, then walk downtown Easton.'),
        ('Evening', 'Dinner at Bas Rouge.')]) +
    day('SAT', 'St. Michaels & the water', [
        ('Morning', 'The Chesapeake Bay Maritime Museum.'),
        ('Afternoon', 'Crabs at The Crab Claw, then the spa or a sail.'),
        ('Evening', 'Sunset dinner at Stars.')]) +
    day('SUN', 'Oxford & home', [
        ('Morning', 'Drive or bike to Bellevue, ride the ferry to Oxford and stroll the town.'),
        ('Before leaving', 'Return the car and allow time at the FBO.'),
        ('Fly home', 'Summer storms build over the Bay in the afternoon; let weather set the departure.')]) +
    '</div></section>')

P.append('<section id="know">' + head('07', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    know([('Book in this order', 'Lodging and a car first, then dinners and any spa time.'),
          ('Airspace', 'The DC SFRA and military areas are close by. Brief them, and check TFRs before every flight.'),
          ('Seasons', 'The ferry and crab houses are seasonal. Check opening dates for spring and late-fall trips.'),
          ('Dates come next', 'Rates and restaurant hours are date-dependent. No availability or live price is implied here.')]) +
    '</section>')

P.append(page_end(number=25, place='St. Michaels & Easton, Maryland', reviewed=REVIEWED, note='Several picks have no website link because official addresses could not be confirmed; check each one, and confirm hours, prices and availability directly before booking.',
    credit_html=PHOTO['credit_html']))

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
