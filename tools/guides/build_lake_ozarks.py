"""Generate docs/lake-ozarks/index.html (Lake of the Ozarks, Missouri)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='lake-ozarks', name='Lake of the Ozarks', state='Missouri', number=51, reviewed='November 3, 2026',
    airport='KAIZ', nm=713, flight_time='~5 hr 1 <small>min</small>', style='Rental car + boat',
    place='Lake of the Ozarks, Missouri',
    description='A curated two-night Lake of the Ozarks getaway for GA pilots and their partners, from KMYR to KAIZ. A huge winding lake, castle ruins, caves, boating and lakeside resorts.',
    lede='A thousand miles of shoreline and a castle on the bluff.',
    intro='Lake of the Ozarks winds for 92 miles through the Missouri hills, with more shoreline than the California coast. Spend a day on the water, hike to the stone ruins of a 1900s castle above the lake at Ha Ha Tonka, explore a cave, and settle into a lakeside resort for sunset.',
    pills=['Lake life', 'Castle ruins', 'Lakeside resorts'],
    flight=dict(
        title='Land above the lake.',
        intro='KAIZ, Lee C. Fine Memorial, is a city-run airport near the Grand Glaize arm of the lake, about 15 minutes from Osage Beach.',
        fbo=('City of Osage Beach FBO · Lee C. Fine Memorial', 'Lee C. Fine Road, Brumley, MO 65017', '573-348-5251'),
        notes=['Listed hours vary by season. A recent pilot report says the field was out of service for a stretch in 2025, so call ahead to confirm status, fuel, ground transport and parking. No live fuel price is shown.',
               'Rolling, wooded hills and the lake surround the field. About 710 nm from Myrtle Beach: plan a fuel stop and consider a third night. Review the sectional and current NOTAMs.'],
        around_title='A car, then a boat.',
        around='Resorts and restaurants are spread around the lake; many are easiest to reach by water. Rent a boat for a day.'),
    stay=dict(title='Lakeside resorts.', intro='Rates and availability need travel dates; summer weekends fill early.',
        cards=[('Camdenton · Lodge & golf', 'Old Kinderhook', 'A lodge and golf resort in the hills above the lake, with a spa and a lakeside beach club.', 'https://oldkinderhook.com/'),
               ('Osage Beach · Luxury condos', 'Camden on the Lake', 'A lakeside resort with suites and a pool on the water.', 'https://www.camdenonthelake.com/'),
               ('Explore more', 'Lake of the Ozarks visitor guide', 'More resorts and rentals around the lake.', 'https://funlake.com/')]),
    eat=dict(title='Dinners by the water.', intro='Many lake restaurants have boat docks.',
        cards=[('Friday dinner · Resort', 'Old Kinderhook', 'Dinner at the resort, then a sunset on the deck.', 'https://oldkinderhook.com/'),
               ('Saturday dinner · Dock & dine', 'Windrose Marker 26', 'Waterfront dining at Margaritaville Lake Resort, with boat slips for diners. Seasonal, about April to September.', 'https://www.margaritavilleresortlakeoftheozarks.com/'),
               ('Lunch · By boat', 'Shady Gators', 'A lively waterfront bar and grill with docks and live music; busiest on summer weekends.', 'https://www.shadygators.com/')]),
    explore=dict(title='Water, castle and caves.', intro='Plan one day on the water.',
        items=[('Ha Ha Tonka State Park', 'The stone ruins of a 1900s castle on a bluff over the lake, with natural bridges, springs and trails.', 'https://mostateparks.com/park/ha-ha-tonka-state-park', 'Park information'),
               ('A day on the lake', 'Rent a pontoon or tritoon and explore the coves. Bigfoot Boat Rentals operates from Alhonna Resort in Lake Ozark.', 'https://www.bigfootboatrentals.com/', 'Bigfoot Boat Rentals'),
               ('Caves', 'Guided tours of the area’s show caves, a cool break on summer days.'),
               ('Lake of the Ozarks State Park', 'Missouri’s largest state park, with beaches and trails.'),
               ('Bagnell Dam Strip', 'The old-fashioned strip by the 1931 dam that created the lake.')]),
    events=dict(url='https://funlake.com/', button='Browse Lake of the Ozarks events',
        cards=[('Summer', 'Lake season', 'Boating, swimming and lively weekends.'),
               ('October', 'Fall color', 'Quieter coves and colorful hills.'),
               ('Spring', 'Quiet season', 'Mild weather and lower rates.')]),
    itinerary=dict(intro='A sample weekend: a day on the water, castle ruins and lakeside dinners. A third night makes the long flight easier. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & the lake', [('Arrival', 'Land at KAIZ, subject to weather, your fuel stop and your actual flight plan.'), ('Afternoon', 'Check in and walk to the water.'), ('Evening', 'Dinner at Old Kinderhook.')]),
              ('SAT', 'On the water', [('Morning', 'Pick up a pontoon from Bigfoot Boat Rentals and explore the coves.'), ('Afternoon', 'Lunch by boat at Shady Gators.'), ('Evening', 'Dinner by boat at Windrose Marker 26.')]),
              ('SUN', 'Castle & home', [('Morning', 'Ha Ha Tonka’s castle ruins and springs.'), ('Before leaving', 'Return the car and allow time at the airport.'), ('Fly home', 'Let weather and your flight plan set the departure.')])]),
    know=[('Book in this order', 'Lodging, a car and a boat rental first.'),
          ('Airport status', 'Call ahead; the field has had service interruptions.'),
          ('Long flight', 'About 710 nm. Plan a fuel stop and consider a third night.'),
          ('Summer weekends', 'The lake is busy in summer; weekdays are calmer.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
