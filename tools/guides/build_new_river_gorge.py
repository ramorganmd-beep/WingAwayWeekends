"""Generate docs/new-river-gorge/index.html."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='new-river-gorge', name='New River Gorge', state='West Virginia', number=88, reviewed=None,
    airport='KBKW', nm=269, flight_time='~2 hr 02 <small>min</small>', style='Rental car',
    place='Fayetteville, West Virginia',
    description='A curated New River Gorge getaway for GA pilots and their partners, from KMYR to KBKW. America’s newest national park: the New River Gorge Bridge, whitewater rafting, cliffside trails and a small mountain town.',
    lede='A national park gorge, a famous bridge and whitewater.',
    intro='New River Gorge became a national park in 2020, and it is one of the East’s great outdoor weekends. Walk the catwalk beneath the New River Gorge Bridge, raft some of the country’s best whitewater, hike to Long Point for the classic bridge view, see the Glade Creek Grist Mill and eat pizza in the little town of Fayetteville.',
    pills=['National park', 'Whitewater', 'Cabins'],
    flight=dict(
        title='Land at Beckley.',
        intro='KBKW, Raleigh County Memorial Airport, sits on a plateau at about 2,500 feet, about 30 minutes from Fayetteville and the bridge.',
        fbo=('Raleigh County Memorial Airport', 'Raleigh County Memorial Airport, Beaver, WV', '304-255-0476'),
        notes=['Confirm FBO hours, fees and rental cars. No live fuel price is shown.',
               'Mountain terrain: check ceilings, density altitude and ridge winds. About 270 nm from Myrtle Beach.'],
        around_title='Rent a car.',
        around='The park, bridge and Fayetteville are spread out; you need a car.'),
    stay=dict(title='A cabin by the gorge.', intro='Rates and availability need travel dates. Bridge Day weekend books far ahead.',
        cards=[('Gorge rim · Resort', 'Adventures on the Gorge', 'Cabins, restaurants and rafting trips on the rim.', 'https://www.adventuresonthegorge.com/'),
               ('Fayetteville · Cabins', 'The Outpost', 'Modern cabins near town and the park.', 'https://outpostnrg.com/'),
               ('Near the park · Cabins', 'New River Cabins', 'Cabins minutes from the gorge.', 'https://newrivercabinswv.com/')]),
    eat=dict(title='Pizza, sandwiches and a café in a church.', intro='Small-town hours; check before you go.',
        cards=[('Friday dinner · Pizza', 'Pies & Pints', 'The original location of a well-loved pizza and craft-beer spot.', 'https://www.piesandpints.net/'),
               ('Lunch · Sandwiches', 'Secret Sandwich Society', 'Creative sandwiches with a deck.', 'https://www.secretsandwichsociety.com/'),
               ('Saturday dinner · On the rim', 'Adventures on the Gorge restaurants', 'Several restaurants at the resort.', 'https://www.adventuresonthegorge.com/')]),
    explore=dict(title='The bridge, the river and the rim.', intro='Pick one big adventure a day.',
        items=[('Bridge Walk', 'A guided walk on the catwalk 850 feet above the river.', 'https://www.bridgewalk.com/', 'Bridge Walk'),
               ('Whitewater rafting', 'Gentle upper New or big-water lower New and the Gauley in fall.', 'https://www.adventuresonthegorge.com/', 'Rafting'),
               ('New River Gorge National Park', 'Long Point Trail, the Canyon Rim Visitor Center and overlooks.', 'https://www.nps.gov/neri/', 'Park'),
               ('Babcock State Park', 'The much-photographed Glade Creek Grist Mill.', 'https://www.wvstateparks.com/park/babcock-state-park/', 'Babcock')]),
    events=dict(url='https://www.newrivergorgecvb.com/', button='Browse New River Gorge events',
        cards=[('Third Saturday in October', 'Bridge Day', 'The bridge closes to cars; BASE jumpers leap from it.', 'https://officialbridgeday.com/', 'Bridge Day'),
               ('September–October', 'Gauley season', 'Famous whitewater on dam-release days.', 'https://www.adventuresonthegorge.com/', 'Rafting'),
               ('October', 'Fall color', 'Peak foliage in the gorge.')]),
    itinerary=dict(intro='A sample weekend: the bridge, a raft and a hike. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & the rim', [('Arrival', 'Land at KBKW, subject to weather and your actual flight plan.'), ('Afternoon', 'The Canyon Rim Visitor Center and overlook.'), ('Evening', 'Dinner at Pies & Pints.')]),
              ('DAY 2', 'Raft or walk the bridge', [('Morning', 'Rafting on the New River, or the Bridge Walk.'), ('Afternoon', 'Hike Long Point Trail.'), ('Evening', 'Dinner at the resort.')]),
              ('DAY 3', 'Grist mill & home', [('Morning', 'Babcock State Park.'), ('Before leaving', 'Allow time at the airport.'), ('Fly home', 'Mountain weather changes fast; leave early.')])]),
    know=[('Book in this order', 'Lodging first, then rafting or the Bridge Walk.'),
          ('Mountain flying', 'Check ceilings and winds over the ridges.'),
          ('Whitewater', 'Trip difficulty varies widely; pick the right section.'),
          ('Best seasons', 'May to October.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
