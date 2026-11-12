"""Generate docs/knoxville/index.html."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = {
    'slug': 'knoxville', 'name': 'Knoxville', 'state': 'Tennessee', 'number': 302, 'reviewed': None,
    'researched': 'November 12, 2026',
    'airport': 'KTYS', 'nm': 281, 'flight_time': '~2 hr 7 <small>min</small>', 'style': 'Rental car or Uber',
    'place': 'Knoxville, Tennessee',
    'description': 'A curated Knoxville getaway for GA pilots and their partners, from KMYR to KTYS. Land at McGhee Tyson, home of Cirrus’s Vision Center, then head downtown for Market Square, a James Beard chef’s wood-fired kitchen, the Sunsphere, the Urban Wilderness and the Smokies an hour away.',
    'lede': 'Fly in where Cirrus delivers its airplanes, then head downtown.',
    'intro': 'McGhee Tyson Airport is home to Cirrus’s Vision Center, where the company delivers airplanes and trains and supports owners. From there it is about 25 minutes to Market Square and Gay Street. Stay downtown, eat at J.C. Holdway, walk World’s Fair Park to the Sunsphere and hike the Urban Wilderness at Ijams. The Great Smoky Mountains are about an hour away.',
    'pills': ['Cirrus Vision Center', 'Food & music', 'Smokies nearby'],
    'flight': {
        'title': 'Land at McGhee Tyson.',
        'intro': 'KTYS, McGhee Tyson Airport, is a towered airport in Class C airspace with two long runways (05L/23R, 10,000 ft, and 05R/23L, 9,000 ft), about 25 minutes south of downtown. Cirrus’s Vision Center (sales, delivery, training and service) is on the field. For an airport minutes from downtown, Knoxville Downtown Island Airport (KDKX, non-towered, 3,499 ft runway) sits on the Tennessee River.',
        'fbo': ['Signature Knoxville', '2343 W General Aviation Drive, Alcoa, TN · open 24 hours', '865-970-9000', 'https://www.signatureaviation.com/locations/tys'],
        'notes': ['Confirm FBO fees, parking and ground transportation. No live fuel price is shown.',
                  'Class C airspace: contact approach before entering. About 280 nm from Myrtle Beach, roughly two hours over the mountains; check winds, ceilings and terrain.'],
        'around_title': 'Rental car or Uber.',
        'around': 'Rent a car or take an Uber the 25 minutes downtown; downtown, Market Square, the Old City and World’s Fair Park are walkable. A car also makes the Smokies an easy day trip.',
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
                ('Arrival', 'Land at KTYS, subject to weather and your actual flight plan; drive downtown.'),
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
        ('Book in this order', 'Lodging first (check the football schedule), then J.C. Holdway and a rental car.'),
        ('Two airports', 'KTYS has the long runways, the tower and the Cirrus Vision Center; KDKX (3,499 ft) is closer to downtown.'),
        ('Mountain flying', 'About 280 nm from Myrtle Beach over the Appalachians: check winds, ceilings and terrain.'),
        ('Cirrus owners', 'The Vision Center is on the field at KTYS; contact Cirrus ahead about a visit.'),
    ],
}

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
