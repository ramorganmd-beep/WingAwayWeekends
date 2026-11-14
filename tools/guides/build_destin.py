"""Generate docs/destin/index.html."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = {
    'slug': 'destin', 'name': 'Destin', 'state': 'Florida', 'number': 305, 'reviewed': 'November 14, 2026',
    'researched': 'November 14, 2026',
    'airport': 'KDTS', 'nm': 431, 'flight_time': '~3 hr 8 <small>min</small>', 'style': 'Rental car or Uber',
    'place': 'Destin, Florida',
    'description': 'A curated Destin getaway for GA pilots and their partners, from KMYR to KDTS. Land at Destin Executive, minutes from the harbor, then stay on the sand, eat seafood on the harbor, boat to Crab Island and visit the Air Force Armament Museum.',
    'lede': 'Emerald water, a working harbor and an airport minutes from the beach.',
    'intro': 'Destin Executive sits right in town, a few minutes from the beach and the harbor. Stay at a beach resort, eat fresh Gulf seafood along the harbor, take a boat out to Crab Island, walk the Village of Baytowne Wharf at Sandestin and, for pilots, see the aircraft at the Air Force Armament Museum near Eglin.',
    'pills': ['Beach', 'Harbor seafood', 'Aviation museum'],
    'flight': {
        'title': 'Land minutes from the harbor.',
        'intro': 'KDTS, Destin Executive, has a 5,001 ft runway (14/32) and sits in town between the harbor and the beach. Atlantic Aviation is the FBO. Eglin Air Force Base is next door.',
        'fbo': ['Atlantic Aviation DTS', 'Destin Executive Airport, Destin, FL', '850-424-6890', 'https://www.atlanticaviation.com/location/DTS'],
        'notes': ['Confirm FBO fees, parking and ground transportation. No live fuel price is shown.',
                  'Busy military airspace (Eglin) surrounds the field: check the chart supplement, restricted areas and NOTAMs before you go. Summer afternoons bring thunderstorms.'],
        'around_title': 'Rental car or Uber.',
        'around': 'The beach and the harbor are a few minutes from the airport by Uber. Rent a car for Sandestin, Baytowne Wharf and the Armament Museum.',
    },
    'stay': {
        'title': 'On the beach or on the harbor.',
        'intro': 'Rates and availability need travel dates. Summer and October fill early.',
        'cards': [
            ('Beachfront · Luxury', 'Henderson Beach Resort', 'A luxury resort next to Henderson Beach State Park, with a spa.', 'https://www.hendersonbeachresort.com/'),
            ('Resort · Golf & beach', 'Sandestin Golf and Beach Resort', 'A large resort with golf, beach and the Village of Baytowne Wharf.', 'https://www.sandestin.com/'),
            ('Harbor · Condo resort', 'Emerald Grande at HarborWalk Village', 'Resort condos on Destin Harbor, steps from the restaurants and boats.', 'https://www.emeraldgrande.com/'),
        ],
    },
    'eat': {
        'title': 'Seafood on the harbor and the beach.',
        'intro': 'Reserve weekend dinners in season.',
        'cards': [
            ('Lunch · Beachfront', 'The Back Porch', 'Casual seafood on the beach with Gulf views.', 'https://www.theback-porch.com/'),
            ('Friday dinner · Harbor', 'Boshamps', 'A seafood and oyster house on Destin Harbor.', 'https://www.boshamps.com/'),
            ('Local seafood', 'Dewey Destin’s', 'Fresh local seafood from a long-time Destin fishing family.', 'https://www.destinseafood.com/'),
            ('Saturday dinner · Harbor', 'Harbor Docks', 'Seafood and sushi on the harbor.', 'https://www.harbordocks.com/'),
        ],
    },
    'explore': {
        'title': 'Crab Island, the harbor and the Armament Museum.',
        'intro': 'Boats, beach and a stop for the aviation buffs.',
        'items': [
            ('Crab Island', 'A shallow sandbar near the Destin bridge where boats anchor in clear water; go by boat rental or tour.', 'https://www.google.com/maps/search/?api=1&query=Crab+Island+Destin+FL', 'Map'),
            ('Air Force Armament Museum', 'Aircraft and weapons history outside Eglin Air Force Base, a short drive from Destin.', 'https://www.google.com/maps/search/?api=1&query=Air+Force+Armament+Museum+Eglin+FL', 'Map'),
            ('HarborWalk Village', 'Restaurants, shops and charter boats along Destin Harbor.', 'https://www.google.com/maps/search/?api=1&query=HarborWalk+Village+Destin+FL', 'Map'),
            ('Henderson Beach State Park', 'Dunes and a quiet stretch of beach in town.', 'https://www.google.com/maps/search/?api=1&query=Henderson+Beach+State+Park+Destin+FL', 'Map'),
            ('The Village of Baytowne Wharf', 'A pedestrian village at Sandestin with shops, dining and events.', 'https://www.baytownewharf.com/', 'Baytowne Wharf'),
        ],
    },
    'events': {
        'url': 'https://www.destinfishingrodeo.org/', 'button': 'See the Destin Fishing Rodeo',
        'cards': [
            ('October 1–31', 'Destin Fishing Rodeo', 'A month-long fishing tournament on Destin Harbor; a fun time to visit, but book early.', 'https://www.destinfishingrodeo.org/'),
            ('Summer', 'Peak beach season', 'Full hotels and afternoon storms; book early and fly in the morning.'),
            ('Spring & fall', 'Best seasons', 'Warm water, quieter beaches and easier reservations.'),
        ],
    },
    'itinerary': {
        'intro': 'A sample weekend: the harbor, Crab Island and the Armament Museum. No bookings or availability confirmed.',
        'days': [
            ('DAY 1', 'Arrive & the harbor', [
                ('Arrival', 'Land at KDTS, subject to weather and your actual flight plan; a few minutes to the hotel.'),
                ('Afternoon', 'Beach time.'),
                ('Evening', 'Dinner at Boshamps on the harbor.')]),
            ('DAY 2', 'Crab Island & Baytowne', [
                ('Morning', 'A boat to Crab Island.'),
                ('Afternoon', 'The Air Force Armament Museum, or a round of golf at Sandestin.'),
                ('Evening', 'Baytowne Wharf, or dinner at Harbor Docks.')]),
            ('DAY 3', 'Beach & home', [
                ('Morning', 'Lunch at The Back Porch on the beach.'),
                ('Before leaving', 'Allow time at the FBO.'),
                ('Fly home', 'Watch for afternoon storms in summer.')]),
        ],
    },
    'know': [
        ('Book in this order', 'Lodging first in summer and October, then a boat for Crab Island and dinners.'),
        ('Military airspace', 'Eglin is next door: check restricted areas, NOTAMs and the chart supplement.'),
        ('Short runway', 'KDTS has a 5,001 ft runway; check performance on hot summer days.'),
        ('Pilots', 'The Air Force Armament Museum is a short drive away near Eglin.'),
    ],
}

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
