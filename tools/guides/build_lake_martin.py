"""Generate docs/lake-martin/index.html (Lake Martin, Alabama)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='lake-martin', name='Lake Martin', state='Alabama', number=76, reviewed=None,
    airport='KALX', nm=356, flight_time='~2 hr 37 <small>min</small>', style='Rental or arranged car',
    place='Lake Martin, Alabama',
    description='A curated Lake Martin getaway for GA pilots and their partners, from KMYR to KALX. A clear, 40,000-acre lake with lake-cottage rentals, SpringHouse dinners at Russell Crossroads, boating and a fire-tower hike.',
    lede='A clear, quiet lake with 700 miles of wooded shoreline.',
    intro='Lake Martin is one of the South’s prettiest lakes: about 40,000 acres of clear water and some 700 miles of wooded shoreline. Rent a lake cottage, spend a day on a boat, hike to the Smith Mountain fire tower and have dinner on the porch at SpringHouse, overlooking the lake.',
    pills=['Lake cottage', 'Boating', 'Lakeside dining'],
    flight=dict(
        title='Land at Alexander City.',
        intro='KALX, Thomas C. Russell Field, is a non-towered field in Alexander City, about 20 minutes from the lake.',
        fbo=('Alexander City Flying Service', 'Thomas C. Russell Field, Alexander City, AL', '256-392-5401'),
        notes=['Confirm FBO hours, overnight parking and ground transportation; rental cars may need to be arranged in advance. No live fuel price is shown.',
               'About 355 nm from Myrtle Beach. Summer brings afternoon storms.'],
        around_title='Arrange a car ahead.',
        around='The lake is spread out; you need a car, and a boat is the best way to see it.'),
    stay=dict(title='A cottage on the water.', intro='Rates and availability need travel dates. Summer weekends book early.',
        cards=[('Lakeside · Cottages', 'Russell Lands on Lake Martin', 'Cottage and home rentals around Russell Crossroads and Willow Point.', 'https://www.russelllands.com/'),
               ('Lakeside · Park', 'Wind Creek State Park', 'A large state park on the lake with campsites and a marina.', 'https://www.alapark.com/parks/wind-creek-state-park', 'Park'),
               ('Local guide', 'More rentals', 'Browse the local visitor guide for lake homes and inns.', 'https://www.lakemartin.com/', 'Visitor guide')]),
    eat=dict(title='Dinner by the lake.', intro='Reserve SpringHouse, especially in summer.',
        cards=[('Saturday dinner · Lakeview', 'SpringHouse', 'Seasonal Southern cooking with a porch overlooking the lake.', 'https://springhouseatcrossroads.com/'),
               ('Friday dinner · On the water', 'Kowaliga Restaurant', 'A lakeside restaurant you can reach by boat.', 'https://www.kowaligarestaurant.com/'),
               ('Lunch · Russell Crossroads', 'Catherine’s Market', 'A market and café for picnic supplies and lunch.', 'https://russellcrossroads.com/catherines-market.html')]),
    explore=dict(title='Water, woods and a fire tower.', intro='Slow days on the water.',
        items=[('Rent a boat', 'Pontoons and ski boats are available from marinas around the lake; book ahead in summer.', 'https://explorelakemartin.com/renting-a-boat-on-lake-martin/', 'Boat rentals'),
               ('Smith Mountain Fire Tower', 'A short hike to a restored fire tower with sweeping lake views.', 'https://www.lmra.info/smith-mountain-fire-tower', 'Fire tower'),
               ('Russell Crossroads', 'Trails, stables and a small village center.', 'https://russellcrossroads.com/', 'Russell Crossroads'),
               ('Wind Creek State Park', 'Swimming, trails and a marina.', 'https://www.alapark.com/parks/wind-creek-state-park', 'Park')]),
    events=dict(url='https://www.lakemartin.com/', button='Browse Lake Martin events',
        cards=[('Summer', 'Lake season', 'Warm water and busy coves; book everything early.'),
               ('Fourth of July', 'Fireworks on the lake', 'Boats gather to watch fireworks.', 'https://explorelakemartin.com/4th-of-july-on-lake-martin-fireworks-festivals-summer-fun/', 'Fireworks'),
               ('Spring & fall', 'Quieter weekends', 'Mild weather and calmer water.')]),
    itinerary=dict(intro='A sample weekend: the lake, the tower and dinner on the porch. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & settle in', [('Arrival', 'Land at KALX, subject to weather and your actual flight plan.'), ('Afternoon', 'Check in and get on the water.'), ('Evening', 'Dinner at Kowaliga.')]),
              ('DAY 2', 'A day on the lake', [('Morning', 'Hike to the Smith Mountain fire tower.'), ('Afternoon', 'A boat day, with a picnic from Catherine’s Market.'), ('Evening', 'Dinner at SpringHouse.')]),
              ('DAY 3', 'Slow morning & home', [('Morning', 'Coffee on the dock.'), ('Before leaving', 'Allow time at the airport.'), ('Fly home', 'Summer storms build in the afternoon; leave early.')])]),
    know=[('Book in this order', 'Lodging and a boat first, then SpringHouse.'),
          ('Ground transport', 'Arrange a car before you land.'),
          ('Summer crowds', 'Holiday weekends are busy on the water.'),
          ('Best seasons', 'May to October for the water; spring and fall for quiet.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
