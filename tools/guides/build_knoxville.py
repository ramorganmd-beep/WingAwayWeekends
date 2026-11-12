"""Generate docs/knoxville/index.html."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = {
    'slug': 'knoxville', 'name': 'Knoxville', 'state': 'Tennessee', 'number': 302, 'reviewed': None,
    'researched': 'November 12, 2026',
    'airport': 'KDKX', 'nm': 280, 'flight_time': '~2 hr 7 <small>min</small>', 'style': 'Uber + walks',
    'place': 'Knoxville, Tennessee',
    'description': 'A curated Knoxville getaway for GA pilots and their partners, from KMYR to KDKX. Land on the river minutes from downtown: Market Square, a James Beard chef’s wood-fired kitchen, the Sunsphere, the Urban Wilderness and the Smokies an hour away.',
    'lede': 'Land on the river, minutes from Market Square.',
    'intro': 'Knoxville’s Downtown Island Airport sits on the Tennessee River a few minutes from Market Square and Gay Street. Stay downtown, eat at J.C. Holdway, walk World’s Fair Park to the Sunsphere and hike the Urban Wilderness at Ijams. The Great Smoky Mountains are about an hour away, and Cirrus’s Vision Center is across town at McGhee Tyson.',
    'pills': ['Downtown airport', 'Food & music', 'Smokies nearby'],
    'flight': {
        'title': 'Land on the river.',
        'intro': 'KDKX, Knoxville Downtown Island Airport, is a non-towered field on an island in the Tennessee River with one paved runway (08/26, 3,499 ft), a few minutes from downtown. For a longer runway, a tower or the Cirrus Vision Center, use McGhee Tyson (KTYS, 9,000 and 10,000 ft) about 25 minutes south.',
        'fbo': ['Knoxville Downtown Island Airport', 'Metropolitan Knoxville Airport Authority · 100LL and Jet A', '865-577-4461'],
        'notes': ['Confirm FBO hours, fees, parking and ground transportation. No live fuel price is shown.',
                  'Mind the 3,499 ft runway and the river and ridgelines around it; check density altitude and your performance numbers. About 280 nm from Myrtle Beach, roughly two hours over the mountains.'],
        'around_title': 'Uber and walking.',
        'around': 'Take an Uber from the airport; downtown, Market Square, the Old City and World’s Fair Park are walkable.',
    },
    'stay': {
        'title': 'Downtown luxury or a boutique on Market Square.',
        'intro': 'Rates and availability need travel dates. Tennessee football weekends sell out early.',
        'cards': [
            ('Downtown · Luxury', 'The Tennessean Hotel', 'A luxury hotel central to Market Square, the Old City and the university.', 'https://www.thetennesseanhotel.com/'),
            ('Market Square · Boutique', 'The Oliver Hotel', 'A restored historic boutique hotel steps from Market Square, home of the Peter Kern Library bar.', 'https://theoliverhotel.com/knoxville'),
            ('Gay Street · Suites', 'Embassy Suites by Hilton Knoxville Downtown', 'Two-room suites with breakfast, a short walk from Market Square.'),
        ],
    },
    'eat': {
        'title': 'Wood-fired Southern and pasta on the square.',
        'intro': 'Reserve weekend dinners.',
        'cards': [
            ('Friday dinner · Wood-fired Southern', 'J.C. Holdway', 'James Beard Award-winning chef Joseph Lenn’s wood-fired Southern kitchen downtown.', 'https://www.jcholdway.com/'),
            ('Saturday dinner · Italian', 'Emilia', 'House-made pasta on Market Square.'),
            ('Cocktails · Hotel bar', 'Peter Kern Library', 'The cocktail bar at The Oliver Hotel.', 'https://theoliverhotel.com/knoxville'),
        ],
    },
    'explore': {
        'title': 'Market Square, the Sunsphere and the Urban Wilderness.',
        'intro': 'A walkable downtown with the mountains on the horizon.',
        'items': [
            ('Market Square & Gay Street', 'Shops, patios and restaurants in the heart of downtown.', 'https://www.downtownknoxville.org/', 'Downtown Knoxville'),
            ('World’s Fair Park & the Sunsphere', 'The 1982 World’s Fair site, with lawns, fountains and the Sunsphere.', 'https://www.visitknoxville.com/', 'Visit Knoxville'),
            ('Knoxville Museum of Art', 'Art of East Tennessee and beyond, in World’s Fair Park.', 'https://knoxart.org/', 'Knoxville Museum of Art'),
            ('Ijams Nature Center & the Urban Wilderness', 'Trails, a quarry and the river, on Island Home Avenue near the airport.', 'https://www.ijams.org/', 'Ijams'),
            ('Tennessee Theatre', 'A restored historic movie palace on Gay Street with concerts and shows.', 'https://www.tennesseetheatre.com/', 'Tennessee Theatre'),
        ],
    },
    'events': {
        'url': 'https://www.visitknoxville.com/', 'button': 'Browse Knoxville events',
        'cards': [
            ('Fall Saturdays', 'Tennessee football', 'Game weekends fill hotels and restaurants; book early or pick another weekend.'),
            ('April', 'Dogwood season', 'Spring blooms and the Dogwood Arts festival around town.'),
            ('April–May & October', 'Best seasons', 'Mild weather, spring blooms or fall color in the nearby Smokies.'),
        ],
    },
    'itinerary': {
        'intro': 'A sample weekend: downtown, the Urban Wilderness and dinner at J.C. Holdway. No bookings or availability confirmed.',
        'days': [
            ('DAY 1', 'Arrive & Market Square', [
                ('Arrival', 'Land at KDKX, subject to weather, runway length and your actual flight plan.'),
                ('Afternoon', 'Market Square and Gay Street.'),
                ('Evening', 'Dinner at J.C. Holdway.')]),
            ('DAY 2', 'Trails & the Sunsphere', [
                ('Morning', 'Ijams Nature Center and the Urban Wilderness trails.'),
                ('Afternoon', 'World’s Fair Park, the Sunsphere and the Knoxville Museum of Art.'),
                ('Evening', 'Dinner at Emilia, then a nightcap at the Peter Kern Library.')]),
            ('DAY 3', 'Brunch & home', [
                ('Morning', 'Brunch downtown, or a drive toward the Smokies.'),
                ('Before leaving', 'Allow time at the airport.'),
                ('Fly home', 'Watch mountain weather and winds over the ridges.')]),
        ],
    },
    'know': [
        ('Book in this order', 'Lodging first (check the football schedule), then J.C. Holdway.'),
        ('Short runway', 'KDKX has 3,499 ft; McGhee Tyson (KTYS) is the long-runway, towered option.'),
        ('Mountain flying', 'About 280 nm from Myrtle Beach over the Appalachians: check winds, ceilings and terrain.'),
        ('Cirrus owners', 'Cirrus’s Vision Center (sales, delivery, training and service) is at KTYS.'),
    ],
}

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
