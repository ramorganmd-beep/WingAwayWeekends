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
    'lede': 'Sixty miles of beach, golf and seafood, minutes from the runway.',
    'intro': 'Myrtle Beach International sits on the old air force base at the south end of town, a few minutes from the ocean. Stay at a resort on the Intracoastal or right on the beach, walk the Market Common next to the airport, spend an evening on the Murrells Inlet MarshWalk and save a morning for Huntington Beach State Park or a round of golf.',
    'pills': ['Beach', 'Golf', 'Seafood'],
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
        'title': 'The Intracoastal or the oceanfront.',
        'intro': 'Rates and availability need travel dates. Summer weekends and spring golf season fill early.',
        'cards': [
            ('Grande Dunes · Resort', 'Marina Inn at Grande Dunes', 'A full-service resort on the Intracoastal Waterway, with a marina, pools and the Grande Dunes golf nearby.', 'https://www.marinainnatgrandedunes.com/'),
            ('Oceanfront · Resort & spa', 'Marriott Myrtle Beach Resort & Spa at Grande Dunes', 'An oceanfront resort at Grande Dunes with indoor and outdoor pools and the Hibiscus Spa.', 'https://www.marriott.com/en-us/hotels/myrgd-marriott-myrtle-beach-resort-and-spa-at-grande-dunes/overview/'),
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
        'title': 'The MarshWalk, the state park and the golf.',
        'intro': 'Beach days, salt marsh and some of the best-known golf on the East Coast.',
        'items': [
            ('Murrells Inlet MarshWalk', 'A boardwalk along the salt marsh lined with restaurants and live music; best at sunset.', 'https://www.marshwalk.com/', 'MarshWalk'),
            ('Huntington Beach State Park', 'An unspoiled beach, a salt-marsh boardwalk for birding and historic Atalaya.', 'https://southcarolinaparks.com/huntington-beach', 'SC State Parks'),
            ('Brookgreen Gardens', 'Sculpture gardens, a zoo and Lowcountry history across the road from the state park.', 'https://www.google.com/maps/search/?api=1&query=Brookgreen+Gardens+Murrells+Inlet+SC', 'Map'),
            ('The Market Common', 'Shops, restaurants and a lakeside park on the old air base, next to the airport.', 'https://www.marketcommonmb.com/', 'The Market Common'),
            ('Dunes Golf & Beach Club', 'A classic oceanside course on a coast known for its golf.', 'https://www.thedunesclub.net/', 'Dunes Club'),
        ],
    },
    'events': {
        'url': 'https://myrtlebeachareachamber.com/', 'button': 'Browse Myrtle Beach events',
        'cards': [
            ('Summer', 'Peak season', 'Busy beaches, packed roads and full hotels; book early and arrive in the morning.'),
            ('Spring & fall', 'Best seasons', 'Warm days, quieter beaches and prime golf weather.'),
            ('Winter', 'Off season', 'Quiet beaches and lower rates; some seasonal restaurants close.'),
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
                ('Morning', 'Huntington Beach State Park, or a round of golf.'),
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
