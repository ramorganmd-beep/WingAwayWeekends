"""Generate docs/hudson-valley/index.html (Hudson Valley, New York)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='hudson-valley', name='Hudson Valley', state='New York', number=37, reviewed='November 3, 2026',
    airport='KPOU', nm=534, flight_time='~3 hr 49 <small>min</small>', style='Rental car',
    place='Hudson Valley, New York',
    description='A curated two-night Hudson Valley getaway for GA pilots and their partners, from KMYR to KPOU. Grand estates, the Culinary Institute, the Old Rhinebeck Aerodrome, art and river views.',
    lede='River estates, great food and vintage airplanes.',
    intro='Two hours north of Manhattan, the Hudson Valley is a land of river views, grand estates and small towns full of good food. Tour FDR’s home, walk a bridge 212 feet above the Hudson, dine at the Culinary Institute of America and watch World War I biplanes fly at the Old Rhinebeck Aerodrome.',
    pills=['River estates', 'Food & farms', 'Vintage aviation'],
    flight=dict(
        title='Land in the middle of the valley.',
        intro='KPOU, Hudson Valley Regional, is a towered airport south of Poughkeepsie, about 25 minutes from Hyde Park and 35 from Rhinebeck.',
        fbo=('FlightLevel Dutchess', '263 New Hackensack Road, Wappingers Falls, NY 12590', '845-849-3770'),
        notes=['Directories list hours of 7 a.m. to 8 p.m. daily. Ask about rental cars, parking and fees. No live fuel price is shown.',
               'New York Class B airspace lies to the south; Stewart’s Class C is across the river. Review the sectional and current NOTAMs, and plan a fuel stop for most piston aircraft.'],
        around_title='You’ll need a car.',
        around='The estates, towns and restaurants are spread along both sides of the river.'),
    stay=dict(title='Riverfront, farm or historic inn.', intro='Rates and availability need travel dates.',
        cards=[('Kingston · Riverfront', 'Hutton Brickyards', 'Cabins and rooms on the site of an old brickworks on the Hudson, with river views and a relaxed, design-forward feel.', 'https://www.huttonbrickyards.com/'),
               ('Gardiner · Auberge', 'Wildflower Farms', 'A luxury farm resort below the Shawangunk Ridge, with cabins, a spa and farm-to-table dining.', 'https://auberge.com/wildflower-farms/'),
               ('Rhinebeck · Historic inn', 'Beekman Arms & Delamater Inn', 'One of the oldest inns in America, in the middle of Rhinebeck village, with a colonial tavern.', 'https://www.beekmandelamaterinn.com/')]),
    eat=dict(title='Two dinners. One with chefs in training.', intro='Reserve dinners ahead.',
        cards=[('Friday dinner · Hyde Park', 'The Culinary Institute of America', 'Dine at one of the CIA’s student-run restaurants on its campus above the Hudson. Polished, fun and a great value. Check which restaurants are open.', 'https://www.ciafoodies.com/'),
               ('Saturday dinner · Farm resort', 'Wildflower Farms', 'Seasonal farm-to-table dining at Wildflower Farms in Gardiner, with views of the ridge.', 'https://auberge.com/wildflower-farms/'),
               ('Lunch · Rhinebeck', 'Beekman Arms tavern', 'A colonial tavern lunch in Rhinebeck, then a walk through the village shops.', 'https://www.beekmandelamaterinn.com/')]),
    explore=dict(title='Estates, art and old airplanes.', intro='Choose one big outing a day.',
        items=[('Old Rhinebeck Aerodrome', 'A living museum of pioneer and World War I aircraft, with weekend air shows in summer and fall, and biplane rides. A must for pilots.', 'https://oldrhinebeck.org/', 'Shows and hours'),
               ('Home of Franklin D. Roosevelt', 'FDR’s home, library and museum in Hyde Park, next to the Vanderbilt Mansion.', 'https://www.nps.gov/hofr/', 'Park information'),
               ('Walkway Over the Hudson', 'A 1.3-mile walk across an old railroad bridge 212 feet above the river.', 'https://walkway.org/', 'Walkway information'),
               ('Storm King Art Center', 'Huge outdoor sculptures across 500 acres of fields and hills, about 40 minutes south.', 'https://stormking.org/', 'Tickets'),
               ('Dia Beacon', 'A major museum of contemporary art in a former box factory in Beacon.')]),
    events=dict(url='https://travelhudsonvalley.com/', button='Browse Hudson Valley events',
        cards=[('June–October', 'Aerodrome air shows', 'Weekend shows of vintage aircraft at Old Rhinebeck.'),
               ('October', 'Fall color & harvest', 'Orchards, cideries and fall foliage along the river.'),
               ('Spring & summer', 'Farm season', 'Farmers markets, farm dinners and open studios.')]),
    itinerary=dict(intro='A sample Friday–Sunday weekend: estates, vintage airplanes and two memorable dinners. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & Hyde Park', [('Arrival', 'Land at KPOU, subject to weather, your fuel stop and your actual flight plan, and pick up the car.'), ('Afternoon', 'FDR’s home and library.'), ('Evening', 'Dinner at the Culinary Institute.')]),
              ('SAT', 'Airplanes & Rhinebeck', [('Morning', 'The Old Rhinebeck Aerodrome, with an air show on weekends in season.'), ('Afternoon', 'Lunch in Rhinebeck and a walk through the village.'), ('Evening', 'Dinner at Wildflower Farms.')]),
              ('SUN', 'The river & home', [('Morning', 'Walk the Walkway Over the Hudson.'), ('Before leaving', 'Return the car and allow time at the FBO.'), ('Fly home', 'Let weather and your flight plan set the departure.')])]),
    know=[('Book in this order', 'A car and lodging first, then dinners.'),
          ('Airspace', 'New York Class B is to the south. Brief your route carefully.'),
          ('Aerodrome', 'Air shows run on weekends in season; check the schedule.'),
          ('Fall weekends', 'October is beautiful and busy. Book early.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
