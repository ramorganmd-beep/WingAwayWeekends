"""Generate docs/orlando/index.html."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = {
    'slug': 'orlando', 'name': 'Orlando & Walt Disney World', 'state': 'Florida', 'number': 312, 'reviewed': 'November 21, 2026',
    'researched': 'November 21, 2026',
    'airport': 'KISM', 'nm': 348, 'flight_time': '~2 hr 34 <small>min</small>', 'style': 'Rental car or Uber',
    'place': 'Kissimmee, Florida',
    'description': 'A family fly-in weekend in Orlando: land at Kissimmee Gateway, the general aviation airport closest to Walt Disney World, then spend a day at the parks, an evening at Disney Springs and a morning at Gatorland.',
    'lede': 'The parks, without the airline airport.',
    'intro': 'Kissimmee Gateway is a towered general aviation airport southwest of Orlando, a short drive from Walt Disney World and usually a shorter drive to the parks than Orlando International. Pick one park for one big day, stay at a Disney resort or nearby in Kissimmee, spend an evening at Disney Springs, and add Gatorland or Universal if the kids still have energy. Works for every age; the sweet spot is about 4 to 12.',
    'pills': ['Family', 'Theme parks', 'Disney'],
    'flight': {
        'title': 'Skip the airline airports.',
        'intro': 'KISM, Kissimmee Gateway, has a control tower (7 a.m. to 10 p.m.) and two runways: 15/33, 6,001 ft, and 6/24, 5,001 ft. Signature and Velocity are the FBOs, and the airport charges a landing fee.',
        'fbo': ['Signature Kissimmee (ISM)', 'Kissimmee Gateway Airport, Kissimmee, FL', '407-846-6128', 'https://www.signatureaviation.com/locations/ism'],
        'notes': ['Velocity Aviation Kissimmee (407-846-8001, open 24 hours) is the other FBO. Confirm FBO fees, the landing fee, parking and rental cars. No live fuel price is shown.',
                  'KISM sits just southwest of the Orlando Class B airspace, with arrival procedures and busy training traffic. Summer thunderstorms build most afternoons from about June to September: plan morning flights.',
                  'Cirrus Aircraft has a service and training center on the field.'],
        'around_title': 'Rental car or Uber.',
        'around': 'The Disney parks are roughly 20 to 30 minutes by car, Universal a little farther. Arrange a rental car with child seats through the FBO, or use Uber with your own car seats; Disney resort guests can ride Disney buses between the parks.',
    },
    'stay': {
        'title': 'Inside Disney, or close by.',
        'intro': 'Rates and availability need travel dates. Spring break, summer and the holidays fill early.',
        'cards': [
            ('At Disney · Family suites', 'Disney’s Art of Animation Resort', 'Themed family suites that sleep six, on the Disney bus and Skyliner routes.', 'https://disneyworld.disney.go.com/resorts/art-of-animation-resort/'),
            ('At Disney · Monorail', 'Disney’s Polynesian Village Resort', 'A splurge on the monorail line, with fireworks views across the lagoon to Magic Kingdom.', 'https://disneyworld.disney.go.com/resorts/polynesian-resort/'),
            ('Kissimmee · Resort', 'Margaritaville Resort Orlando', 'A big resort near the parks in Kissimmee, with several pools and a choice of room sizes for larger families.', 'https://www.margaritavilleresorts.com/margaritaville-resort-orlando'),
        ],
    },
    'eat': {
        'title': 'Disney Springs and a Florida classic.',
        'intro': 'Park food is part of the fun; these are for the evenings.',
        'cards': [
            ('Dinner · Shopping district', 'Disney Springs', 'Disney’s free-to-enter dining and shopping district: dozens of restaurants, the big LEGO store and live music in the evening.', 'https://www.disneysprings.com/'),
            ('Dinner · Irish pub', 'Raglan Road', 'An Irish pub at Disney Springs with live music and dancing nightly.', 'https://www.raglanroad.com/'),
            ('Dinner · Spanish & Cuban', 'Columbia Restaurant Celebration', 'The Celebration location of Florida’s Spanish-Cuban classic, in the town of Celebration, a short drive from the parks.', 'https://www.columbiarestaurant.com/celebration'),
        ],
    },
    'explore': {
        'title': 'One big park day, then something different.',
        'intro': 'Choose one park and do it well; a single day at each of several parks wears out small children.',
        'items': [
            ('Walt Disney World', 'Four theme parks: Magic Kingdom for the youngest, plus EPCOT, Hollywood Studios and Animal Kingdom. Buy tickets and park reservations ahead.', 'https://disneyworld.disney.go.com/', 'Walt Disney World'),
            ('Universal Orlando Resort', 'Universal’s theme parks, better for older children and teens who want bigger rides.', 'https://www.universalorlando.com/', 'Universal Orlando'),
            ('Gatorland', 'An old-Florida park in Orlando with alligators, crocodiles and a zip line, a calm half day away from the crowds.', 'https://www.gatorland.com/', 'Gatorland'),
            ('Old Town Kissimmee', 'An entertainment district near the parks with shops, attractions and regular car shows.', 'https://www.myoldtownusa.com/', 'Old Town'),
        ],
    },
    'events': {
        'url': 'https://disneyworld.disney.go.com/', 'button': 'See Walt Disney World',
        'cards': [
            ('Fall & winter', 'Best weather', 'Cooler, drier days and fewer afternoon storms; holiday decorations from about November.'),
            ('Spring', 'Spring break crowds', 'Pleasant weather but the busiest weeks of the year; book early.'),
            ('Summer', 'Heat and storms', 'Long park hours, high heat and afternoon thunderstorms: fly in the morning.'),
        ],
    },
    'itinerary': {
        'intro': 'A sample family weekend: one park day and one easy day. No bookings or availability confirmed.',
        'days': [
            ('DAY 1', 'Arrive & Disney Springs', [
                ('Arrival', 'Land at KISM, subject to weather and your actual flight plan; pick up the rental car and check in.'),
                ('Afternoon', 'Pool time at the hotel.'),
                ('Evening', 'Dinner and the LEGO store at Disney Springs.')]),
            ('DAY 2', 'Park day', [
                ('Morning', 'Be at the gate at opening for the shortest lines.'),
                ('Afternoon', 'A midday break at the hotel helps younger children.'),
                ('Evening', 'Back for the evening fireworks if everyone has the energy.')]),
            ('DAY 3', 'Gators & home', [
                ('Morning', 'Gatorland, or a slow breakfast and the pool.'),
                ('Before leaving', 'Allow time at the FBO to load car seats and souvenirs.'),
                ('Fly home', 'In summer, leave before the afternoon storms build.')]),
        ],
    },
    'know': [
        ('Best ages', 'Magic Kingdom suits children about 3 to 10; older kids and teens may prefer Universal or Hollywood Studios.'),
        ('Book in this order', 'Park tickets and any park reservations first, then the hotel, then the rental car with child seats.'),
        ('Summer weather', 'Afternoon thunderstorms are common from about June to September; plan morning arrivals and departures.'),
        ('Car seats', 'Bring your own or reserve them with the rental car; Uber drivers do not supply them.'),
    ],
}

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
    # A family guide: say so in the tagline and page title.
    t = open(sys.argv[1]).read().replace(' · Couples · Two nights', ' · Families · Two nights').replace(' Couples Getaway |', ' Family Getaway |')
    open(sys.argv[1], 'w').write(t)
