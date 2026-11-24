"""Generate docs/halter-ranch/index.html: a fly-in winery on a private airstrip (prior permission required)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = {
    'slug': 'halter-ranch', 'name': 'Halter Ranch Fly-In Winery', 'state': 'California', 'number': 316, 'reviewed': 'November 24, 2026',
    'researched': 'November 24, 2026',
    'airport': '89CA', 'nm': 2058, 'flight_time': '~13 hr 58 <small>min</small>', 'style': 'Walk from the airstrip',
    'place': 'Paso Robles, California',
    'description': 'A fly-in winery in Paso Robles wine country: by prior permission, land on Halter Ranch’s private airstrip, walk to lunch at Restaurant Alice and the estate tasting room, and fly home with a case of organic estate wine.',
    'lede': 'Land in the vineyard, walk to lunch.',
    'intro': 'Halter Ranch is a 2,500-acre organic estate in the hills west of Paso Robles, and it calls itself the only fly-in winery and vineyard in the world. By prior permission, you can land on its private airstrip, walk to lunch at Restaurant Alice and the estate tasting room, tour the vineyards and fly home with wine. Wine club members can stay in the Pilot Cottages by the creek; everyone else can book an estate house or stay in Paso Robles, 11 nm east.',
    'pills': ['Fly-in winery', 'Wine', 'Prior permission'],
    'flight': {
        'title': 'A private strip in the vineyards: ask first.',
        'intro': '89CA is a private-use airstrip: you must request a fly-in date from Halter Ranch at least 3 days ahead. One asphalt runway, 4/22, 3,353 ft long and only 25 ft wide; field elevation 1,488 ft. No fuel or services are listed.',
        'fbo': ['Halter Ranch (fly-in requests)', '8910 Adelaida Rd, Paso Robles, CA', '805-226-9455', 'https://www.halterranch.com/pages/airport'],
        'notes': ['Request your date through the winery’s fly-in page or by phone at least 3 days ahead, and wait for their confirmation. Check that your insurance covers private airstrips.',
                  'The runway is very narrow (25 ft) in hilly terrain: plan a stable approach, check crosswinds and your landing and takeoff numbers, and avoid hot, gusty afternoons. Fuel up beforehand: Paso Robles (KPRB), 11 nm east, has fuel and a full-service FBO.',
                  'Morning fog and low clouds are common on the Central Coast, especially in late spring and summer.'],
        'around_title': 'Walk on the estate.',
        'around': 'The tasting room and Restaurant Alice are on the estate. For Paso Robles town, arrange a car or taxi ahead, or fly the 11 nm to KPRB.',
    },
    'stay': {
        'title': 'On the estate, or in town.',
        'intro': 'Estate lodging is booked through Halter Ranch; wine club members get preferred rates.',
        'cards': [
            ('On the estate · Members', 'Pilot Cottages', 'Historic cottages along the wooded creekside, built for pilots flying in. Lodging here is a perk for wine club members.', 'https://www.halterranch.com/pages/airport'),
            ('On the estate · Groups', 'Estate homes', 'The restored 1880 Victorian (sleeps 14), the hilltop Vineyard View with a private pool (sleeps 12), and the renovated Hunting Lodge.', 'https://www.halterranch.com/pages/stay'),
            ('In town · Paso Robles', 'Our Paso Robles guide', 'Hotels, dinner and more wineries in Paso Robles, 11 nm east at KPRB.', '../paso-robles/'),
        ],
    },
    'eat': {
        'title': 'Lunch among the vines.',
        'intro': 'Lunch is served 11 a.m. to 3:30 p.m.; the estate is open 10:30 a.m. to 5 p.m. daily, except a few holidays.',
        'cards': [
            ('Lunch · On the estate', 'Restaurant Alice', 'Lunch paired with Halter Ranch’s organic estate wines, steps from the tasting room. Last call for food is 3:30 p.m.', 'https://www.halterranch.com/pages/the-estate'),
        ],
    },
    'explore': {
        'title': 'Tastings, tours and the Ancestor Tree.',
        'intro': 'Book tastings and tours ahead.',
        'items': [
            ('Estate tastings', 'Organic, estate-grown wines in the Paso Robles tasting room. If you bring pets or guests under 21, call ahead for a reservation.', 'https://www.halterranch.com/pages/the-estate', 'Halter Ranch'),
            ('Tours & expeditions', 'See more of the 2,500-acre estate, including a Defender tour, with a glass in hand.', 'https://www.halterranch.com/pages/the-estate', 'Halter Ranch'),
            ('The Ancestor Tree', 'A huge, ancient oak on the estate, one of the reasons people come.', 'https://www.halterranch.com/', 'Halter Ranch'),
        ],
    },
    'events': {
        'url': 'https://www.halterranch.com/', 'button': 'See Halter Ranch events',
        'cards': [
            ('Daily', 'Open 10:30 to 5', 'Closed Easter, Thanksgiving and the day after, Christmas Eve, Christmas Day and New Year’s Day.'),
            ('Summer', 'Hot afternoons', 'Inland Paso Robles gets hot: land in the morning and watch density altitude.'),
            ('Harvest', 'Fall in wine country', 'Late summer and fall are harvest season across Paso Robles.'),
        ],
    },
    'itinerary': {
        'intro': 'A sample fly-in visit. Request the landing date first; no bookings or availability confirmed.',
        'days': [
            ('ARRIVE', 'Land & lunch', [
                ('Before', 'Confirm your fly-in date with Halter Ranch at least 3 days ahead; top off fuel at KPRB or earlier.'),
                ('Late morning', 'Land at 89CA, subject to weather, the winery’s permission and your actual flight plan.'),
                ('Lunch', 'Restaurant Alice, then a tasting.')]),
            ('AFTERNOON', 'Tour & fly on', [
                ('Afternoon', 'A vineyard tour and a walk to the Ancestor Tree.'),
                ('Before leaving', 'Load the wine and check weight and balance.'),
                ('Depart', 'Leave before the afternoon heat and gusts, or stay the night.')]),
        ],
    },
    'know': [
        ('Prior permission', 'Private-use airstrip: request a date at least 3 days ahead and wait for confirmation.'),
        ('Narrow runway', '25 ft wide and 3,353 ft long, at 1,488 ft elevation in the hills: check your numbers and crosswind.'),
        ('Fuel', 'None listed on the field. KPRB, 11 nm east, has fuel and an FBO.'),
        ('Pilot in command', 'Wine on board is cargo, not lunch: no tasting before you fly.'),
    ],
}

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
    t = open(sys.argv[1]).read().replace(' · Couples · Two nights', ' · Fly-in winery · Lunch or one night').replace(' Couples Getaway |', ' |')
    t = t.replace('<span>WEEKEND STYLE</span><strong>Two nights ', '<span>VISIT</span><strong>Lunch or one night ')
    open(sys.argv[1], 'w').write(t)
