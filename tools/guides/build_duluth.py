"""Generate docs/duluth/index.html (Duluth and the North Shore, Minnesota)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='duluth', name='Duluth & the North Shore', state='Minnesota', number=55, reviewed='November 3, 2026',
    airport='KDLH', nm=994, flight_time='~6 hr 53 <small>min</small>', style='Rental car',
    place='Duluth & the North Shore, Minnesota',
    description='A curated getaway to Duluth and Minnesota’s North Shore for GA pilots and their partners, from KMYR to KDLH. Lake Superior, the Aerial Lift Bridge, ore ships, a lakefront mansion, Split Rock Lighthouse and waterfalls.',
    lede='Lake Superior, ore ships and a lighthouse on the cliffs.',
    intro='Duluth climbs a hillside above Lake Superior, the largest freshwater lake in the world. Watch 1,000-foot ore ships pass under the Aerial Lift Bridge, walk the Lakewalk, tour a lakefront mansion, then drive the North Shore to waterfalls and Split Rock Lighthouse on its cliff.',
    pills=['Lake Superior', 'North Shore drive', 'Lighthouses & waterfalls'],
    flight=dict(
        title='Land above the city.',
        intro='KDLH, Duluth International, is a towered airport about 15 minutes from Canal Park.',
        fbo=('Vantage Aviation · Duluth', '4535 Airport Approach Road, Duluth, MN 55811', '218-727-2911'),
        notes=['Some directories list the FBO as Monaco Air Duluth; the airport site names Vantage Aviation. Confirm the name, hours and fees, and ask about rental cars. No live fuel price is shown.',
               'This is a long trip, about 1,000 nm from Myrtle Beach, so plan one or two fuel stops and three or four nights. Lake Superior brings fog, low clouds and early winter. Review the sectional and current NOTAMs.'],
        around_title='You’ll want a car.',
        around='Canal Park and the Lakewalk are walkable; the North Shore drive needs a car.'),
    stay=dict(title='By the lake.', intro='Rates and availability need travel dates; summer and fall fill early.',
        cards=[('Canal Park · Lakefront', 'Pier B Resort', 'A modern resort on the harbor, steps from the Aerial Lift Bridge.', 'https://www.pierbresort.com/'),
               ('Lakewalk · Historic', 'Fitger’s Inn', 'A hotel in a restored 1880s brewery complex on the Lakewalk.', 'https://fitgers.com/'),
               ('Explore more', 'Visit Duluth', 'More lakefront hotels and North Shore lodges.', 'https://visitduluth.com/')]),
    eat=dict(title='Two dinners. One smoked-fish lunch.', intro='Reserve weekend dinners.',
        cards=[('Friday dinner · Italian', 'Va Bene', 'Scratch Italian cooking with views over the lake.', 'https://vabenecaffe.com/'),
               ('Saturday dinner · Canal Park', 'Lake Avenue Restaurant', 'Inventive cooking in Canal Park.', 'https://www.lakeaveduluth.com/'),
               ('Lunch · Smoked fish', 'Northern Waters Smokehaus', 'A tiny Canal Park favorite for smoked Lake Superior fish sandwiches.', 'https://northernwaterssmokehaus.com/')]),
    explore=dict(title='Ships, mansions and the shore.', intro='Spend one day in Duluth and one on the North Shore.',
        items=[('Aerial Lift Bridge & Canal Park', 'Watch the bridge lift for ore ships and lakers entering the harbor; check the shipping schedule.'),
               ('Glensheen', 'A 39-room 1908 lakefront mansion with gardens, run by the University of Minnesota.', 'https://glensheen.d.umn.edu/', 'Tours'),
               ('The Lakewalk', 'A walking path along the shore from Canal Park.'),
               ('Split Rock Lighthouse', 'A 1910 lighthouse on a 130-foot cliff, about 45 minutes up the North Shore.', 'https://www.mnhs.org/splitrock', 'Visit information'),
               ('Gooseberry Falls', 'Waterfalls and trails in a state park along the North Shore.', 'https://www.dnr.state.mn.us/state-parks/park.html?id=spk00266', 'Park information')]),
    events=dict(url='https://visitduluth.com/', button='Browse Duluth events',
        cards=[('Summer', 'Shipping season', 'Ore ships and tall ships; cool, clear days.'),
               ('Late September–early October', 'Fall color', 'The North Shore turns gold and red.'),
               ('Winter', 'Snow and ice', 'Beautiful but challenging; winter flying needs careful planning.')]),
    itinerary=dict(intro='A sample long weekend: the harbor, a mansion and the North Shore. Plan three or four nights for the flight. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & Canal Park', [('Arrival', 'Land at KDLH, subject to weather, your fuel stops and your actual flight plan, and pick up the car.'), ('Afternoon', 'Canal Park and the Aerial Lift Bridge.'), ('Evening', 'Dinner at Va Bene.')]),
              ('DAY 2', 'The North Shore', [('Morning', 'Drive the shore to Gooseberry Falls.'), ('Afternoon', 'Split Rock Lighthouse.'), ('Evening', 'Dinner at Lake Avenue Restaurant.')]),
              ('DAY 3', 'Glensheen & home', [('Morning', 'Glensheen and the Lakewalk.'), ('Before leaving', 'Return the car and allow time at the FBO.'), ('Fly home', 'A long trip home. Start early and let weather set the plan.')])]),
    know=[('Book in this order', 'Lodging and a car first, then dinners.'),
          ('Very long flight', 'About 1,000 nm. Plan fuel stops and extra nights.'),
          ('Lake weather', 'Fog, low clouds and early winter. Keep backup days.'),
          ('Seasons', 'Summer and early fall are best.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
