"""Generate docs/san-luis-obispo/index.html."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = {
    'slug': 'san-luis-obispo', 'name': 'San Luis Obispo & Pismo Beach', 'state': 'California', 'number': 314, 'reviewed': 'November 22, 2026',
    'researched': 'November 22, 2026',
    'airport': 'KSBP', 'nm': 2052, 'flight_time': '~13 hr 56 <small>min</small>', 'style': 'Rental car or Uber',
    'place': 'San Luis Obispo, California',
    'description': 'A Central Coast weekend in San Luis Obispo and Pismo Beach: land at San Luis Obispo County Regional, then the Thursday night farmers’ market, the Madonna Inn, Edna Valley wine and clam chowder by the pier. Or land at Oceano, half a mile from the beach, and camp by the runway.',
    'lede': 'A college town, the beach and wine country, ten minutes apart.',
    'intro': 'San Luis Obispo County Regional sits just south of town, with a downtown full of restaurants along San Luis Creek and Pismo Beach about 15 minutes away. Stay at the famously over-the-top Madonna Inn or on the bluffs in Pismo, walk the Thursday night farmers’ market, taste in the Edna Valley and end with chowder by the pier. For the beach itself, Oceano County Airport (L52) is half a mile from the sand, with a fly-in campground beside the ramp.',
    'pills': ['Beach', 'Wine', 'Downtown'],
    'flight': {
        'title': 'A towered field, or the beach strip.',
        'intro': 'KSBP has a control tower and two runways: 11/29, 6,101 ft, and 7/25, 2,500 ft. ACI Jet is the FBO. Landing fees apply only to aircraft of 6,000 lb and up, so most piston singles pay none.',
        'fbo': ['ACI Jet San Luis Obispo', 'San Luis Obispo County Regional Airport, San Luis Obispo, CA', '805-548-1330', 'https://fbo.acijet.com/san-luis-obispo/'],
        'notes': ['Noise-sensitive airport; runway 29 is the calm-wind runway. Waterfowl gather on and near the field in winter. Transient parking over two hours: contact the FBO. Coastal fog and low clouds are common, especially late spring and summer mornings.',
                  'Beach option: Oceano County Airport (L52), 8 nm south, is untowered with a 2,325 ft by 50 ft runway, self-serve 100LL, $15-a-night tie-downs and a fly-in-only campground ($25 a night, first come, restrooms, no showers). It is extremely noise sensitive: departing runway 29, hold runway heading until crossing the shoreline. Watch for kites along the beach.'],
        'around_title': 'Rental car or Uber.',
        'around': 'Downtown San Luis Obispo is about 10 minutes from KSBP and Pismo Beach about 15. From Oceano, the beach is a short walk; Enterprise in Grover Beach offers pickup, and taxis and rideshare serve the area.',
    },
    'stay': {
        'title': 'Pink and whimsical, or on the bluffs.',
        'intro': 'Rates and availability need travel dates. Summer weekends and Cal Poly graduation fill early.',
        'cards': [
            ('San Luis Obispo · Icon', 'Madonna Inn', '110 themed rooms, each one different, with a pool, spa, bakery and famously pink dining room.', 'https://www.madonnainn.com/'),
            ('Downtown · Boutique', 'Hotel Cerro', 'A boutique hotel in the heart of downtown, steps from the creek and the Thursday market.', 'https://www.hotelcerro.com/'),
            ('Pismo Beach · Oceanfront', 'Dolphin Bay Resort & Spa', 'Beachfront suites on the Shell Beach bluffs with balcony ocean views.', 'https://www.thedolphinbay.com/'),
        ],
    },
    'eat': {
        'title': 'Creekside dinners and chowder.',
        'intro': 'Downtown SLO for dinner, the pier for lunch.',
        'cards': [
            ('Dinner · Creekside', 'Novo Restaurant & Lounge', 'Global plates and a long wine list on decks over San Luis Creek downtown.', 'https://www.novorestaurant.com/'),
            ('Dinner · Italian', 'Giuseppe’s Cucina Italiana', 'Southern Italian cooking, with restaurants in downtown San Luis Obispo and Pismo Beach.', 'https://giuseppesrestaurant.com/'),
            ('Lunch · Chowder', 'Splash Cafe', 'Award-winning clam chowder in a bread bowl, a block from the Pismo Beach pier.', 'https://www.splashcafe.com/'),
        ],
    },
    'explore': {
        'title': 'Market night, wine and the dunes.',
        'intro': 'Easy days on the Central Coast.',
        'items': [
            ('Downtown SLO Farmers’ Market', 'Every Thursday evening downtown: produce, barbecue smoke, music and half the town out walking.', 'https://downtownslo.com/', 'Downtown SLO'),
            ('Madonna Inn', 'Even if you stay elsewhere, see the rooms, have cake at the bakery and a drink in the pink dining room.', 'https://www.madonnainn.com/', 'Madonna Inn'),
            ('Pismo Beach', 'The pier, the beach and, in winter, monarch butterflies at the grove south of town.', 'https://experiencepismobeach.com/', 'Visit Pismo Beach'),
            ('Hearst Castle', 'About an hour north up the coast at San Simeon: book a tour ahead.', 'https://hearstcastle.org/', 'Hearst Castle'),
        ],
    },
    'events': {
        'url': 'https://www.slocal.com/', 'button': 'Browse SLO CAL events',
        'cards': [
            ('Every Thursday', 'Farmers’ market', 'Downtown San Luis Obispo’s Thursday night market, year-round.', 'https://downtownslo.com/'),
            ('Winter', 'Monarch butterflies', 'Monarchs cluster in the eucalyptus grove at Pismo Beach in winter.'),
            ('Summer', 'Fog season', 'Warm inland, cool at the beach; morning low clouds are common at both airports.'),
        ],
    },
    'itinerary': {
        'intro': 'A sample weekend: downtown, the coast and wine. No bookings or availability confirmed.',
        'days': [
            ('DAY 1', 'Arrive & downtown', [
                ('Arrival', 'Land at KSBP, subject to weather and your actual flight plan; pick up the rental car.'),
                ('Afternoon', 'Check in, then walk the creek downtown.'),
                ('Evening', 'Dinner at Novo, or the farmers’ market if it’s Thursday.')]),
            ('DAY 2', 'Coast & wine', [
                ('Morning', 'Edna Valley tasting rooms, a few minutes south of the airport.'),
                ('Afternoon', 'Chowder at Splash Cafe and a walk on the Pismo Beach pier.'),
                ('Evening', 'A drink and dinner at the Madonna Inn.')]),
            ('DAY 3', 'Slow morning & home', [
                ('Morning', 'Bakery breakfast at the Madonna Inn.'),
                ('Before leaving', 'Check the fog; it often lifts by late morning.'),
                ('Fly home', 'Follow the noise-abatement procedures on departure.')]),
        ],
    },
    'know': [
        ('Fog', 'Marine layer is common on summer and spring mornings; plan late-morning arrivals and departures.'),
        ('Landing fees', 'KSBP charges general aviation only for aircraft of 6,000 lb and over.'),
        ('Oceano option', 'L52 is short (2,325 ft) and narrow (50 ft), untowered and extremely noise sensitive; read the airport remarks before you go.'),
        ('Book in this order', 'Hotel first, especially on summer and graduation weekends, then the rental car.'),
    ],
}

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
