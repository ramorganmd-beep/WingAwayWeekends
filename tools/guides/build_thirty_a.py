"""Generate docs/30a/index.html (Seaside and Scenic Highway 30A, Florida)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='30a', name='Seaside & 30A', state='Florida', number=61, reviewed='November 3, 2026',
    airport='KECP', nm=402, flight_time='~2 hr 56 <small>min</small>', style='Rental car + bikes',
    place='Seaside & 30A, Florida',
    description='A curated two-night Seaside and 30A getaway for GA pilots and their partners, from KMYR to KECP. Sugar-white beaches, emerald water, pastel beach towns, rare coastal dune lakes and a bike path along Scenic Highway 30A.',
    lede='Sugar-white sand and pastel beach towns.',
    intro='Scenic Highway 30A runs for about 24 miles along the Florida Panhandle through a string of beach towns, each with its own style, from the pastel cottages of Seaside to the white walls of Alys Beach. Bike the path between them, swim in emerald water, walk the dunes around rare coastal lakes and dine looking out over the Gulf.',
    pills=['Beaches', 'Beach towns', 'Bike path'],
    flight=dict(
        title='Land 35 minutes from Seaside.',
        intro='KECP, Northwest Florida Beaches International, is a towered airline airport in Panama City Beach, about 30 minutes from Rosemary Beach and 35 from Seaside.',
        fbo=('Sheltair', '5325 Johnny Reaver Road, Panama City, FL 32409', '850-233-4717'),
        notes=['Listed hours are 6 a.m. to 10 p.m. Southern Sky Aviation is also on the field. Ask about rental cars, parking and fees. No live fuel price is shown.',
               'Tyndall and Eglin Air Force Bases have busy military airspace nearby. Summer brings afternoon storms; hurricane season runs June to November. Review the sectional, restricted areas and current NOTAMs.'],
        around_title='A car, then bikes.',
        around='Rent a car at the airport, then use the 30A bike path between towns. Parking in Seaside and Rosemary Beach fills up on busy days.'),
    stay=dict(title='Choose your beach town.', intro='Rates and availability need travel dates; summer and spring break are busiest.',
        cards=[('WaterColor · Beachfront', 'WaterColor Inn', 'A beachfront inn next to Seaside, with the Gulf out the door.', 'https://www.watercolorresort.com/'),
               ('Rosemary Beach · Boutique', 'The Pearl Hotel', 'A boutique hotel in Rosemary Beach’s town center, steps from the beach.', 'https://www.thepearlrb.com/'),
               ('Miramar Beach · Luxury', 'Hotel Effie', 'A modern luxury hotel with a rooftop pool and spa, at the western end near Destin.', 'https://www.hoteleffie.com/')]),
    eat=dict(title='Two dinners. One with a view.', intro='Reserve dinners in season.',
        cards=[('Friday dinner · Seaside', 'Bud & Alley’s', 'A Seaside original since 1986, with a rooftop bar for sunset.', 'https://budandalleys.com/'),
               ('Saturday dinner · Rosemary Beach', 'Restaurant Paradis', 'Polished coastal cooking in Rosemary Beach.', 'https://www.restaurantparadis.com/'),
               ('Lunch · Grayton Beach', 'The Red Bar', 'A funky Grayton Beach institution with live music.', 'https://www.theredbar.com/')]),
    explore=dict(title='Beaches, lakes and towns.', intro='Bike between towns and leave time for the beach.',
        items=[('Seaside', 'The pastel planned town that inspired New Urbanism, and the setting of The Truman Show.', 'https://seasidefl.com/', 'Seaside'),
               ('Grayton Beach State Park', 'Dunes, pine forest and a coastal dune lake.'),
               ('Coastal dune lakes', 'Rare lakes that open to the Gulf only now and then; paddle one by kayak or paddleboard.'),
               ('The 30A bike path', 'A paved path linking the towns along the highway.'),
               ('Rosemary & Alys Beach', 'Two strikingly designed towns at the eastern end of 30A.', 'https://alysbeach.com/', 'Alys Beach')]),
    spa=dict(title='The spa at Hotel Effie', body='Hotel Effie’s spa offers couples treatments near the beach.'),
    events=dict(url='https://www.visitsouthwalton.com/', button='Browse South Walton events',
        cards=[('Spring & fall', 'Best seasons', 'Warm water, lighter crowds and mild days.'),
               ('Summer', 'High season', 'Busy beaches and towns; book early.'),
               ('Winter', 'Quiet season', 'Cool, peaceful and inexpensive.')]),
    itinerary=dict(intro='A sample Friday–Sunday weekend: the beach, the bike path and two good dinners. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & Seaside', [('Arrival', 'Land at KECP, subject to weather and your actual flight plan, and pick up the car.'), ('Afternoon', 'Check in and walk Seaside.'), ('Evening', 'Sunset at Bud & Alley’s rooftop, then dinner.')]),
              ('SAT', 'Bikes & beaches', [('Morning', 'Bike the path to Grayton Beach.'), ('Afternoon', 'Lunch at The Red Bar, then a dune lake paddle.'), ('Evening', 'Dinner at Restaurant Paradis.')]),
              ('SUN', 'An easy departure', [('Morning', 'A walk through Rosemary and Alys Beach.'), ('Before leaving', 'Return the car and allow time at the FBO.'), ('Fly home', 'Summer storms build in the afternoon; leave early.')])]),
    know=[('Book in this order', 'Lodging and a car first, then dinners and bikes.'),
          ('Military airspace', 'Brief Tyndall and Eglin restricted areas.'),
          ('Parking', 'Town parking fills up; bikes are easier.'),
          ('Hurricane season', 'June through November. Keep plans flexible.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
