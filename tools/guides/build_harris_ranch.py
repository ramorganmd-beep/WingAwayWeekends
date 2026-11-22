"""Generate docs/harris-ranch/index.html: an overnight stop, not a full weekend."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = {
    'slug': 'harris-ranch', 'name': 'Harris Ranch', 'state': 'California', 'number': 315, 'reviewed': 'November 22, 2026',
    'researched': 'November 22, 2026',
    'airport': '3O8', 'nm': 2023, 'flight_time': '~13 hr 44 <small>min</small>', 'style': 'Walk from the airstrip',
    'place': 'Coalinga, California',
    'description': 'An overnight stop at Harris Ranch Resort in Coalinga, California: land on the resort’s own airstrip, tie down free, walk to a steak dinner and the pool, and be back in the air after breakfast.',
    'lede': 'Land, tie down, walk to a steak dinner.',
    'intro': 'Harris Ranch Resort sits beside Interstate 5 halfway between Los Angeles and San Francisco, with its own paved, lighted airstrip on the south side of the property. Tie down for free, walk to your room, swim in the heated pool, have a Prime steak dinner and a slice of pie from the bakery, and fly on after breakfast. It is the classic overnight stop on a long West Coast trip, not a full weekend.',
    'pills': ['Overnight stop', 'Steakhouse', 'No rental car'],
    'flight': {
        'title': 'The resort’s own airstrip.',
        'intro': '3O8 is a public-use, untowered airstrip owned by the resort: one runway, 14/32, 2,820 ft long and only 30 ft wide. Parking and tie-downs are free, and Shell self-serve 100LL is available 24 hours.',
        'fbo': ['Harris Ranch Airport', 'Harris Ranch Resort, 24505 W. Dorris Ave., Coalinga, CA', '559-935-0717', 'https://www.harrisranch.com/airport/'],
        'notes': ['There is no FBO staff: for questions about landing, the resort asks pilots to call 559-935-0717, extension 6444.',
                  'The runway is narrow (30 ft): plan a stable approach and check crosswinds. A power line 40 ft above the ground runs 0.3 nm south of the airport, and run-ups are not allowed at the approach end of runway 32. No instrument procedures; New Coalinga Municipal (C80) is 6 nm southwest.',
                  'Summer afternoons in the San Joaquin Valley are hot: check density altitude and your takeoff numbers. Winter tule fog can sit in the valley for days.'],
        'around_title': 'Walk.',
        'around': 'The hotel, restaurants, pool and Country Store are a short walk from the tie-downs. No car needed for an overnight stop.',
    },
    'stay': {
        'title': 'One night, a short walk from the airplane.',
        'intro': 'Check-in is 4 p.m. and check-out noon. Rates need travel dates.',
        'cards': [
            ('On the ranch · Hotel', 'Harris Ranch Hotel', '153 rooms with an Olympic-style heated pool, a pool bar, three spas, an outdoor fireplace and a fitness room. Pets are welcome.', 'https://www.harrisranch.com/hotel/'),
        ],
    },
    'eat': {
        'title': 'Steak night, then breakfast.',
        'intro': 'Everything is on the property.',
        'cards': [
            ('Dinner · Steakhouse', 'Prime Steakhouse', 'USDA Prime steaks, seafood and desserts from the in-house bakery. Closed Tuesdays and Wednesdays; reserve ahead.', 'https://www.harrisranch.com/primesteakhouse/'),
            ('Breakfast · All day', 'Ranch Kitchen', 'Breakfast, lunch and dinner daily from 7 a.m.; breakfast until 11. Walk-ins only.', 'https://www.harrisranch.com/ranchkitchen/'),
            ('Lounge · Live music', 'Horseshoe Lounge', 'The full menu and a bar, with live music on Friday and Saturday nights.', 'https://www.harrisranch.com/horseshoelounge/'),
        ],
    },
    'explore': {
        'title': 'An easy evening.',
        'intro': 'This is a rest stop, done well.',
        'items': [
            ('The pool and spas', 'An Olympic-style heated pool with a pool bar and three spas, good after a long day in the cockpit.', 'https://www.harrisranch.com/hotel/', 'Harris Ranch'),
            ('Country Store & bakery', 'Harris Ranch sauces, almonds and jerky, Western wear, and cookies, cakes and pies from the bakery.', 'https://www.harrisranch.com/countrystore/', 'Harris Ranch'),
            ('Harris BBQ', 'Tri-tip, brisket and ribs to go from the Fast Track store, open 9 a.m. to 9 p.m.: an easy lunch for the next leg.', 'https://www.harrisranch.com/harrisbbq/', 'Harris Ranch'),
            ('Pinnacles National Park', 'Volcanic spires and California condors, about 40 to 60 miles west, if you stay an extra day with a car.', 'https://www.nps.gov/pinn/', 'National Park Service'),
        ],
    },
    'events': {
        'url': 'https://www.harrisranch.com/', 'button': 'See Harris Ranch Resort',
        'cards': [
            ('Weekends', 'Live music', 'Live music in the Horseshoe Lounge on Friday and Saturday nights.', 'https://www.harrisranch.com/horseshoelounge/'),
            ('Summer', 'Valley heat', 'Very hot afternoons: arrive early evening and leave early morning.'),
            ('Winter', 'Tule fog', 'Dense valley fog can linger for days; have a plan B.'),
        ],
    },
    'itinerary': {
        'intro': 'A sample overnight stop. No bookings or availability confirmed.',
        'days': [
            ('EVENING', 'Arrive & steak night', [
                ('Arrival', 'Land at 3O8 in the late afternoon, subject to weather and your actual flight plan; fuel up and tie down.'),
                ('Before dinner', 'Check in and swim.'),
                ('Dinner', 'Prime Steakhouse (Thursday to Monday), or the Horseshoe Lounge.')]),
            ('MORNING', 'Breakfast & go', [
                ('Breakfast', 'Ranch Kitchen, from 7 a.m.'),
                ('Before leaving', 'Pie or barbecue from the Country Store or Harris BBQ for the next leg.'),
                ('Depart', 'Leave before the valley heats up in summer.')]),
        ],
    },
    'know': [
        ('Narrow runway', '30 ft wide and 2,820 ft long, with a power line just south: brief it before you go.'),
        ('Steakhouse days', 'Prime Steakhouse is closed Tuesday and Wednesday; the Ranch Kitchen and lounge are open daily.'),
        ('Fuel', 'Self-serve 100LL, 24 hours. No jet fuel listed and no FBO staff.'),
        ('Plan B', 'In tule fog or summer heat, New Coalinga Municipal (C80) is 6 nm away.'),
    ],
}

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
    t = open(sys.argv[1]).read().replace(' · Couples · Two nights', ' · Overnight stop · One night').replace(' Couples Getaway |', ' Overnight Stop |')
    t = t.replace('<span>WEEKEND STYLE</span><strong>Two nights ', '<span>STAY</span><strong>One night ')
    open(sys.argv[1], 'w').write(t)
