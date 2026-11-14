"""Generate docs/panama-city-beach/index.html."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = {
    'slug': 'panama-city-beach', 'name': 'Panama City Beach', 'state': 'Florida', 'number': 304, 'reviewed': 'November 14, 2026',
    'researched': 'November 14, 2026',
    'airport': 'KECP', 'nm': 402, 'flight_time': '~2 hr 56 <small>min</small>', 'style': 'Rental car or Uber',
    'place': 'Panama City Beach, Florida',
    'description': 'A curated Panama City Beach getaway for GA pilots and their partners, from KMYR to KECP. White sand and emerald water, a boat to Shell Island, seafood on the Grand Lagoon and beach bars by the pier.',
    'lede': 'White sand, emerald water and an easy beach weekend.',
    'intro': 'Northwest Florida Beaches International sits just north of Panama City Beach, about 20 minutes from the sand. Stay on the beach, take the shuttle boat to undeveloped Shell Island from St. Andrews State Park, eat seafood on the Grand Lagoon and catch the sunset at a beach bar near the City Pier.',
    'pills': ['Beach', 'Shell Island', 'Seafood'],
    'flight': {
        'title': 'Land at Northwest Florida Beaches.',
        'intro': 'KECP, Northwest Florida Beaches International, is a towered airport with a 10,000 ft runway (16/34) and airline traffic, about 20 minutes from the beach. Sheltair and Southern Sky Aviation both serve general aviation. It is also the airport for our Seaside &amp; 30A guide, about 30–40 minutes west.',
        'fbo': ['Sheltair ECP', '5325 Johnny Reaver Road, Panama City, FL', '850-233-4717', 'https://www.sheltairaviation.com/locations/ecp/'],
        'notes': ['Second FBO: <a href="https://southernskyaviation.com/fbo/northwest-florida-beaches-ecp/" target="_blank" rel="noopener">Southern Sky Aviation</a>. Compare fees and parking. No live fuel price is shown.',
                  'Military airspace (Tyndall and Eglin) surrounds the area: check the chart, NOTAMs and restricted areas. Summer afternoons bring thunderstorms; plan morning arrivals.'],
        'around_title': 'Rental car or Uber.',
        'around': 'Rent a car or take an Uber the 20 minutes to the beach. Front Beach Road connects the resorts, Pier Park and the City Pier; a car makes St. Andrews State Park and 30A easy.',
    },
    'stay': {
        'title': 'On the sand.',
        'intro': 'Rates and availability need travel dates. Spring break and summer fill early.',
        'cards': [
            ('Beachfront · Resort & golf', 'Edgewater Beach & Golf Resort', 'A large beachfront resort with pools and its own golf course.', 'https://www.resortcollection.com/edgewater-beach-resort/'),
            ('Pier Park area · Resort', 'Laketown Wharf Resort', 'A resort with condos and pools near Pier Park, across from the beach.', 'https://laketownwharfresort.com/'),
            ('Beachfront · Condo resort', 'Shores of Panama', 'Beachfront condos with pools, right on the sand.', 'https://www.shoresofpanama.com/'),
        ],
    },
    'eat': {
        'title': 'Seafood on the lagoon and the beach.',
        'intro': 'Reserve weekend dinners in season.',
        'cards': [
            ('Friday dinner · Seafood', 'Capt. Anderson’s', 'A long-time seafood restaurant on the waterfront at the Grand Lagoon.', 'https://www.captanderson.com/'),
            ('Sunset · Beach club', 'Schooners', 'Calling itself “the last local beach club,” right on the sand, known for its sunset.', 'https://www.schooners.com/'),
            ('Lunch · Beachfront', 'Pineapple Willy’s', 'Beachfront seafood and drinks next to the City Pier.', 'https://www.pwillys.com/'),
            ('Family · Casual', 'The Wicked Wheel', 'A family-friendly favorite for wings and burgers.', 'https://thewickedwheel.com/'),
        ],
    },
    'explore': {
        'title': 'Shell Island, the state park and the pier.',
        'intro': 'Beach days, clear water and a few easy outings.',
        'items': [
            ('Shell Island', 'An undeveloped barrier island; take the shuttle boat from St. Andrews State Park for shelling and snorkeling.', 'https://www.shellislandshuttle.com/', 'Shell Island Shuttle'),
            ('St. Andrews State Park', 'Beaches, a jetty and calm lagoon water at the east end of the beach.', 'https://www.google.com/maps/search/?api=1&query=St.+Andrews+State+Park+Panama+City+Beach+FL', 'Map'),
            ('Pier Park', 'An open-air shopping and dining district on Front Beach Road.', 'https://www.google.com/maps/search/?api=1&query=Pier+Park+Panama+City+Beach+FL', 'Map'),
            ('Russell-Fields City Pier', 'A long fishing pier with gulf views, across from Pier Park.', 'https://www.google.com/maps/search/?api=1&query=Russell-Fields+City+Pier+Panama+City+Beach+FL', 'Map'),
        ],
    },
    'events': {
        'url': 'https://www.visitpanamacitybeach.com/', 'button': 'Browse Panama City Beach events',
        'cards': [
            ('March', 'Spring break', 'Crowded beaches and busy nights; pick another weekend for a quiet getaway.'),
            ('Summer', 'Peak beach season', 'Full hotels and afternoon storms; book early and fly in the morning.'),
            ('September–November', 'Best season', 'Warm water, quieter beaches and lower rates.'),
        ],
    },
    'itinerary': {
        'intro': 'A sample weekend: the beach, Shell Island and seafood on the lagoon. No bookings or availability confirmed.',
        'days': [
            ('DAY 1', 'Arrive & the beach', [
                ('Arrival', 'Land at KECP, subject to weather and your actual flight plan; head to the beach.'),
                ('Afternoon', 'Settle in and walk the beach.'),
                ('Evening', 'Sunset at Schooners.')]),
            ('DAY 2', 'Shell Island', [
                ('Morning', 'Shuttle boat to Shell Island from St. Andrews State Park.'),
                ('Afternoon', 'Pier Park and the City Pier.'),
                ('Evening', 'Dinner at Capt. Anderson’s on the Grand Lagoon.')]),
            ('DAY 3', 'Beach & home', [
                ('Morning', 'A last beach walk and breakfast.'),
                ('Before leaving', 'Allow time at the FBO.'),
                ('Fly home', 'Watch for afternoon storms in summer.')]),
        ],
    },
    'know': [
        ('Book in this order', 'Lodging first (avoid spring break if you want quiet), then dinners and a rental car.'),
        ('Two FBOs', 'Sheltair and Southern Sky Aviation are both at KECP; compare fees before you go.'),
        ('Military airspace', 'Tyndall and Eglin are nearby: check restricted areas and NOTAMs.'),
        ('Nearby', 'Seaside and 30A are about 30–40 minutes west, from the same airport.'),
    ],
}

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
