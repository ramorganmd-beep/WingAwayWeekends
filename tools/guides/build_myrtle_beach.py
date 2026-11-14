"""Generate docs/myrtle-beach/index.html."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = {
    'slug': 'myrtle-beach', 'name': 'Myrtle Beach', 'state': 'South Carolina', 'number': 303, 'reviewed': 'November 14, 2026',
    'researched': 'November 14, 2026',
    'airport': 'KMYR', 'nm': 0, 'flight_time': 'Home field', 'style': 'Rental car or Uber',
    'place': 'Myrtle Beach, South Carolina',
    'description': 'A curated Myrtle Beach getaway for GA pilots and their partners. Land at Myrtle Beach International, minutes from the sand, then stay on the Intracoastal or the oceanfront, eat seafood on the Murrells Inlet MarshWalk and play some of the Grand Strand’s famous golf.',
    'lede': '60 miles of beach, the Golf Capital of the World, great seafood and lots of fun things to do.',
    'intro': 'Myrtle Beach International sits on the old Air Force base at the south end of town, a few minutes from the ocean. Next door at the Market Common, Warbird Park displays an A-10 Warthog, an F-100 and an A-7 from the base’s flying days. Stay at a resort at Grande Dunes, spend an evening on the Murrells Inlet MarshWalk and save a morning for the Boardwalk or a round of golf in the Golf Capital of the World.',
    'pills': ['Beach', 'Golf Capital of the World', 'Seafood'],
    'flight': {
        'title': 'Land minutes from the beach.',
        'intro': 'KMYR, Myrtle Beach International, is a towered airport in Class C airspace with a 9,503 ft runway (18/36). The general aviation side is served by Myrtle Beach Aviation. Grand Strand Airport (KCRE) in North Myrtle Beach is a quieter alternative closer to the north end of the beach.',
        'fbo': ['Myrtle Beach Aviation', 'Beach Aviation Services · Myrtle Beach International · reported hours 6 a.m.–9 p.m., after hours by arrangement', '843-839-6740', 'https://www.myrtlebeachaviation.com/'],
        'notes': ['Confirm FBO fees, parking and ground transportation. No live fuel price is shown.',
                  'Class C airspace with airline traffic: contact approach before entering. Summer afternoons bring pop-up thunderstorms; plan morning arrivals.'],
        'around_title': 'Rental car or Uber.',
        'around': 'Take an Uber or rent a car for the weekend: the Market Common is next to the airport, the oceanfront is a few minutes away and Murrells Inlet is about 20 minutes south. A car makes the gardens, state park and golf easy.',
    },
    'stay': {
        'title': 'The Intracoastal or Oceanfront.',
        'intro': 'Rates and availability need travel dates. Summer weekends and spring golf season fill early.',
        'cards': [
            ('Oceanfront · Resort & spa', 'Marriott Myrtle Beach Resort & Spa at Grande Dunes', 'An oceanfront resort at Grande Dunes with indoor and outdoor pools and the Hibiscus Spa.', 'https://www.marriott.com/en-us/hotels/myrgd-marriott-myrtle-beach-resort-and-spa-at-grande-dunes/overview/'),
            ('Grande Dunes · Resort', 'Marina Inn at Grande Dunes', 'A full-service resort on the Intracoastal Waterway, with a marina, pools and the Grande Dunes golf nearby.', 'https://www.marinainnatgrandedunes.com/'),
            ('Oceanfront · Resort', 'The Breakers Resort', 'A long-running resort with pools, right on the beach.', 'https://www.breakers.com/'),
            ('Oceanfront · Family', 'The Caravelle Resort', 'An oceanfront resort with breakfast on site and a poolside bar, popular with families.', 'https://www.thecaravelle.com/'),
        ],
    },
    'eat': {
        'title': 'Seafood on the water.',
        'intro': 'Reserve weekend dinners in season.',
        'cards': [
            ('Friday dinner · Raw bar', '357 Raw Coastal Bar', 'Oysters and clams on the half shell, a lobster roll and cocktails, dockside on the Intracoastal at the Grande Dunes Marina. 8205 Marina Parkway.', 'https://www.357raw.com/'),
            ('Oceanfront · Classic', 'Sea Captain’s House', 'A Myrtle Beach classic with ocean views from the dining room.', 'https://www.seacaptains.com/'),
            ('Saturday dinner · MarshWalk', 'Wicked Tuna', 'Seafood and sushi over the marsh on the Murrells Inlet MarshWalk.', 'https://www.thewickedtuna.com/'),
            ('Lunch · Murrells Inlet', 'Drunken Jack’s', 'A long-time seafood spot overlooking the inlet.', 'https://www.drunkenjacks.com/'),
        ],
    },
    'explore': {
        'title': 'The MarshWalk, the Boardwalk and the golf courses.',
        'intro': 'Beach days, salt marsh and some of the best-known golf on the East Coast.',
        'items': [
            ('Murrells Inlet MarshWalk', 'A boardwalk along the salt marsh lined with restaurants and live music; best at sunset.', 'https://www.marshwalk.com/', 'MarshWalk'),
            ('Brookgreen Gardens', 'Sculpture gardens, a zoo and Lowcountry history across the road from the state park.', 'https://www.google.com/maps/search/?api=1&query=Brookgreen+Gardens+Murrells+Inlet+SC', 'Map'),
            ('The Market Common & Warbird Park', 'Shops and restaurants on the old air base next to the airport, and Warbird Park’s A-10 Warthog, F-100 and A-7 on display. The park is free and open in daylight.', 'https://www.marketcommonmb.com/', 'The Market Common'),
            ('Grande Dunes Resort Course', 'A public course high above the Intracoastal Waterway at Grande Dunes, in the Golf Capital of the World. Book tee times ahead.', 'https://www.grandedunesgolf.com/', 'Grande Dunes Golf'),
        ],
    },
    'events': {
        'url': 'https://myrtlebeachareachamber.com/', 'button': 'Browse Myrtle Beach events',
        'cards': [
            ('June 10–13, 2027', 'Carolina Country Music Fest', 'Four days of country music on the Myrtle Beach oceanfront. Hotels and the FBO get busy that week: book early.', 'https://carolinacountrymusicfest.com/'),
            ('Spring & fall', 'Best seasons', 'Definitely a golf mecca in spring and fall, with warm days and quieter beaches.'),
            ('Summer', 'Peak beach season', 'Busy beaches, packed roads and full hotels; book early and arrive in the morning.'),
        ],
    },
    'itinerary': {
        'intro': 'A sample weekend: the Intracoastal, the MarshWalk and a beach morning. No bookings or availability confirmed.',
        'days': [
            ('DAY 1', 'Arrive & the Market Common', [
                ('Arrival', 'Land at KMYR, subject to weather and your actual flight plan; check in at Grande Dunes or the oceanfront.'),
                ('Afternoon', 'Walk the Market Common next to the airport, or straight to the beach.'),
                ('Evening', 'Dinner on the Intracoastal at 357 Raw Coastal Bar.')]),
            ('DAY 2', 'Gardens, beach & the MarshWalk', [
                ('Morning', 'The Boardwalk, or a round of golf.'),
                ('Afternoon', 'Brookgreen Gardens, across the road from the park.'),
                ('Evening', 'Sunset and dinner on the Murrells Inlet MarshWalk at Wicked Tuna.')]),
            ('DAY 3', 'Beach & home', [
                ('Morning', 'A beach walk and breakfast, or brunch at Sea Captain’s House.'),
                ('Before leaving', 'Allow time at the FBO.'),
                ('Fly home', 'Summer storms build in the afternoon; leave early.')]),
        ],
    },
    'know': [
        ('Book in this order', 'Lodging first in summer and spring golf season, then dinners on the MarshWalk and a rental car.'),
        ('Two airports', 'KMYR has the long runway, the tower and Myrtle Beach Aviation; Grand Strand Airport (KCRE) is closer to North Myrtle Beach.'),
        ('Summer weather', 'Afternoon thunderstorms are common in summer; plan morning arrivals and departures.'),
        ('Beach traffic', 'Summer weekends crowd Kings Highway and Ocean Boulevard; a car makes the south end and Murrells Inlet easier.'),
    ],
}

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
