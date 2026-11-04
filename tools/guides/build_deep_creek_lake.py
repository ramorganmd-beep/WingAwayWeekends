"""Generate docs/deep-creek-lake/index.html."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='deep-creek-lake', name='Deep Creek Lake', state='Maryland', number=87, reviewed='November 4, 2026',
    airport='2G4', nm=355, flight_time='~2 hr 36 <small>min</small>', style='Rental or arranged car',
    place='Deep Creek Lake, Maryland',
    description='A curated Deep Creek Lake getaway for GA pilots and their partners, from KMYR to 2G4. A mountain lake in western Maryland: a lakefront inn, Swallow Falls, Wisp Resort and lake days by boat.',
    lede='A mountain lake in western Maryland, with an airport next door.',
    intro='Deep Creek Lake is Maryland’s largest lake, high in the Allegheny Mountains and cool even in summer. Land at an airport right by the lake, stay at the adults-only Lake Pointe Inn, hike to Muddy Creek Falls in Swallow Falls State Park, ride the mountain coaster at Wisp and spend an afternoon on a pontoon.',
    pills=['Mountain lake', 'Waterfalls', 'Lakefront inn'],
    flight=dict(
        title='Land beside the lake.',
        intro='2G4, Garrett County Airport, is a non-towered field at about 2,900 feet, just north of the lake.',
        fbo=('Garrett County Airport', 'Garrett County Airport, Oakland, MD', '301-746-8599'),
        notes=['Fuel is available; confirm hours, parking and how you will get to your lodging. No live fuel price is shown.',
               'Mountain airport: compute density altitude, watch for ridge turbulence and fog in the valleys. About 355 nm from Myrtle Beach.'],
        around_title='Arrange a car.',
        around='You need a car around the lake; ask your lodging about pickup before you go.'),
    stay=dict(title='A lakefront inn or a mountain resort.', intro='Rates and availability need travel dates.',
        cards=[('Lakefront · Adults only', 'Lake Pointe Inn', 'A lakefront inn next to Wisp, with a big porch on the water.', 'https://deepcreekinns.com/'),
               ('Mountain · Resort', 'Wisp Resort', 'A four-season resort with skiing, golf and a mountain coaster.', 'https://www.wispresort.com/'),
               ('Lake homes', 'Railey Mountain Lake Vacations', 'Lakefront home rentals.', 'https://www.deepcreek.com/')]),
    eat=dict(title='Lake views and local beer.', intro='Summer weekends are busy; check hours in the off-season.',
        cards=[('Friday dinner · Casual', 'Ace’s Run', 'A local restaurant and pub near the lake.', 'https://www.acesrun.com/'),
               ('Saturday dinner · Brewpub', 'Mountain State Brewing', 'Pizza and local beer with lake views.', 'https://www.mountainstatebrewing.com/'),
               ('Local guide', 'More restaurants', 'The county’s dining list.', 'https://www.visitdeepcreek.com/', 'Visit Deep Creek')]),
    explore=dict(title='Falls, forest and water.', intro='Outdoors days.',
        items=[('Swallow Falls State Park', 'Muddy Creek Falls, Maryland’s highest free-falling waterfall, among old hemlocks.', 'https://dnr.maryland.gov/publiclands/Pages/western/swallowfalls.aspx', 'Park'),
               ('Wisp Resort', 'The mountain coaster, golf and, in winter, skiing.', 'https://www.wispresort.com/', 'Wisp'),
               ('A day on the lake', 'Rent a pontoon or kayak from a lakeside marina.', 'https://www.visitdeepcreek.com/', 'Rentals')]),
    events=dict(url='https://www.visitdeepcreek.com/', button='Browse Deep Creek events',
        cards=[('October', 'Autumn Glory Festival', 'Fall color and a festival in Oakland.', 'https://www.autumnglory.com/', 'Festival'),
               ('Winter', 'Ski season', 'Skiing and snow tubing at Wisp.', 'https://www.wispresort.com/', 'Wisp'),
               ('Summer', 'Lake season', 'Cool mountain weather; book early.')]),
    itinerary=dict(intro='A sample weekend: falls, the lake and a porch dinner. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & the lake', [('Arrival', 'Land at 2G4, subject to weather and your actual flight plan.'), ('Afternoon', 'Settle in at the inn.'), ('Evening', 'Dinner at Ace’s Run.')]),
              ('DAY 2', 'Falls & a boat', [('Morning', 'Swallow Falls State Park.'), ('Afternoon', 'A pontoon on the lake.'), ('Evening', 'Mountain State Brewing.')]),
              ('DAY 3', 'Coaster & home', [('Morning', 'The mountain coaster at Wisp.'), ('Before leaving', 'Allow time at the airport.'), ('Fly home', 'Mountain weather changes fast; leave early.')])]),
    know=[('Book in this order', 'Lodging first, then a car and a boat.'),
          ('Mountain flying', 'Density altitude, ridges and valley fog.'),
          ('Ground transport', 'Arrange a car before you land.'),
          ('Best seasons', 'Summer for the lake, October for color.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
