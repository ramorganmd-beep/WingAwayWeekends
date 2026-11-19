"""Generate docs/carlsbad/index.html."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = {
    'slug': 'carlsbad', 'name': 'Carlsbad & LEGOLAND', 'state': 'California', 'number': 310, 'reviewed': 'November 19, 2026',
    'researched': 'November 19, 2026',
    'airport': 'KCRQ', 'nm': 1911, 'flight_time': '~12 hr 59 <small>min</small>', 'style': 'Rental car or Uber',
    'place': 'Carlsbad, California',
    'description': 'A family fly-in weekend in Carlsbad, California: land at McClellan-Palomar, minutes from LEGOLAND California, then add the beach, the spring Flower Fields and fish tacos in Carlsbad Village.',
    'lede': 'LEGOLAND, the beach and an airport a few minutes from the park.',
    'intro': 'McClellan-Palomar Airport sits on the mesa above Carlsbad, a short drive from LEGOLAND California. Stay at a LEGOLAND hotel or next door at the Sheraton with its own walkway into the park, spend a day on the rides and at the SEA LIFE Aquarium, then cool off at Carlsbad State Beach and eat fish tacos in Carlsbad Village. A strong pick for children about 3 to 12.',
    'pills': ['Family', 'LEGOLAND', 'Beach'],
    'flight': {
        'title': 'Land a few minutes from the park.',
        'intro': 'KCRQ, McClellan-Palomar, is a towered airport with one runway, 6/24, 4,897 ft long. Atlantic Aviation and Western Flight serve general aviation; the airport charges a landing fee.',
        'fbo': ['Atlantic Aviation CRQ', 'McClellan-Palomar Airport, Carlsbad, CA', '760-930-0123', 'https://www.atlanticaviation.com/location/CRQ'],
        'notes': ['Confirm FBO fees, the landing fee, parking and rental cars. Western Flight (760-438-6800) is the other FBO on the field. No live fuel price is shown.',
                  'Busy Southern California airspace and noise-sensitive neighborhoods: review the noise procedures. A morning marine layer is common, especially May through July; it usually burns off by late morning.'],
        'around_title': 'Rental car or Uber.',
        'around': 'LEGOLAND, the hotels around it and Carlsbad Village are all a short drive from the airport. Arrange a rental car with child seats through the FBO, or use Uber with your own car seats.',
    },
    'stay': {
        'title': 'At the park, or right next door.',
        'intro': 'Rates and availability need travel dates. Summer, spring break and holiday weekends fill early.',
        'cards': [
            ('In the park · Themed', 'LEGOLAND Hotel', 'Themed rooms right at the park entrance.', 'https://www.legoland.com/california/hotels-packages/'),
            ('In the park · Castle', 'LEGOLAND Castle Hotel', 'Knights-and-castles themed rooms, steps from the park.', 'https://www.legoland.com/california/hotels-packages/'),
            ('Next door · Resort', 'Sheraton Carlsbad Resort & Spa', 'A resort beside the park with a private walkway into LEGOLAND for guests, pools and a spa.', 'https://www.marriott.com/stay/hotel-info/sanbs'),
        ],
    },
    'eat': {
        'title': 'Fish tacos and pizza.',
        'intro': 'Casual and kid-friendly; Carlsbad Village is the easy dinner stop.',
        'cards': [
            ('Dinner · Village', 'Pizza Port Carlsbad', 'A busy, casual brewpub in Carlsbad Village with pizza for the kids and local beer for the grown-ups.', 'https://www.pizzaport.com/'),
            ('Lunch · Near the beach', 'Harbor Fish Cafe', 'Fish tacos, clam chowder and fish and chips on Carlsbad Boulevard, steps from the beach.', 'https://www.harborfishcafe.com/'),
            ('Dinner · Italian', 'Vigilucci’s Cucina Italiana', 'Italian classics on State Street in Carlsbad Village, with outdoor seating.', 'https://www.vigiluccis.com/'),
        ],
    },
    'explore': {
        'title': 'LEGOLAND, the beach and the Flower Fields.',
        'intro': 'One big park day, one beach day, and something for a slower morning.',
        'items': [
            ('LEGOLAND California', 'Rides, Miniland USA built from LEGO bricks, a water park and the SEA LIFE Aquarium, built for children about 3 to 12. Buy tickets ahead.', 'https://www.legoland.com/california/', 'LEGOLAND'),
            ('Carlsbad State Beach', 'A long beach with a walkway along the bluff, a short drive from the park.', 'https://www.parks.ca.gov/?page_id=653', 'California State Parks'),
            ('The Flower Fields', 'Hillsides of giant ranunculus flowers next to LEGOLAND, open in spring during the bloom.', 'https://theflowerfields.com/', 'The Flower Fields'),
            ('Museum of Making Music', 'A hands-on music museum in Carlsbad where kids can play the instruments.', 'https://www.museumofmakingmusic.org/', 'Museum of Making Music'),
        ],
    },
    'events': {
        'url': 'https://www.visitcarlsbad.com/', 'button': 'Browse Carlsbad events',
        'cards': [
            ('Spring', 'Flower Fields bloom', 'The ranunculus fields next to LEGOLAND bloom in spring; check the season dates before you plan around them.'),
            ('Summer', 'Busy season', 'Longest park hours and the biggest crowds; morning marine layer at the airport is common.'),
            ('Fall & holidays', 'Seasonal park events', 'LEGOLAND runs seasonal events in fall and around the holidays; check the park calendar.', 'https://www.legoland.com/california/'),
        ],
    },
    'itinerary': {
        'intro': 'A sample family weekend: one park day, one beach day. No bookings or availability confirmed.',
        'days': [
            ('DAY 1', 'Arrive & settle in', [
                ('Arrival', 'Land at KCRQ, subject to weather and your actual flight plan; pick up the rental car and check in.'),
                ('Afternoon', 'Pool time at the hotel, or a short walk on Carlsbad State Beach.'),
                ('Evening', 'Pizza in Carlsbad Village.')]),
            ('DAY 2', 'LEGOLAND', [
                ('Morning', 'Be at the gate at opening for the shortest lines.'),
                ('Afternoon', 'Miniland, the water park in season and the SEA LIFE Aquarium.'),
                ('Evening', 'An early dinner and an early night.')]),
            ('DAY 3', 'Beach & home', [
                ('Morning', 'Fish tacos and the beach, or the Flower Fields in spring.'),
                ('Before leaving', 'Allow time at the FBO to load car seats and luggage.'),
                ('Fly home', 'Plan around the marine layer and your own minimums.')]),
        ],
    },
    'know': [
        ('Best ages', 'LEGOLAND is built for children about 3 to 12. Teens may prefer the beach and San Diego’s bigger parks.'),
        ('Book in this order', 'Park tickets and the hotel first, then the rental car with child seats.'),
        ('Marine layer', 'Low morning clouds are common on the coast, especially late spring and early summer. Plan late-morning arrivals and departures.'),
        ('Car seats', 'Bring your own or reserve them with the rental car; Uber drivers do not supply them.'),
    ],
}

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
    # A family guide: say so in the tagline and page title.
    t = open(sys.argv[1]).read().replace(' · Couples · Two nights', ' · Families · Two nights').replace(' Couples Getaway |', ' Family Getaway |')
    open(sys.argv[1], 'w').write(t)
