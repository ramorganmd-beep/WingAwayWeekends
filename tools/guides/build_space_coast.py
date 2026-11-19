"""Generate docs/space-coast/index.html."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = {
    'slug': 'space-coast', 'name': 'Space Coast & Kennedy Space Center', 'state': 'Florida', 'number': 311, 'reviewed': 'November 19, 2026',
    'researched': 'November 19, 2026',
    'airport': 'KTIX', 'nm': 325, 'flight_time': '~2 hr 25 <small>min</small>', 'style': 'Rental car',
    'place': 'Titusville, Florida',
    'description': 'A family fly-in weekend on Florida’s Space Coast: land at Space Coast Regional in Titusville, next to a warbird museum, then visit Kennedy Space Center, watch for a launch, see the wildlife refuge and spend a day at Cocoa Beach.',
    'lede': 'Rockets, warbirds and the beach.',
    'intro': 'Space Coast Regional in Titusville sits across the Indian River from Kennedy Space Center, with the Valiant Air Command Warbird Museum right on the field. Spend a day with the rockets at the Kennedy Space Center Visitor Complex, drive the wildlife refuge, eat rock shrimp in Titusville and finish on the sand at Cocoa Beach. If a launch is scheduled, the whole family will remember it.',
    'pills': ['Family', 'Space', 'Aviation museum'],
    'flight': {
        'title': 'Land across the river from the launch pads.',
        'intro': 'KTIX, Space Coast Regional, is a towered airport with two runways: 18/36, 7,319 ft, and 9/27, 5,000 ft. Space Coast Executive Jet Center is the FBO, and the Valiant Air Command Warbird Museum is on the field.',
        'fbo': ['Space Coast Executive Jet Center', 'Space Coast Regional Airport, Titusville, FL', '321-267-8355', 'https://www.spacecoastfbo.com/'],
        'notes': ['Confirm FBO fees, parking and rental cars. No live fuel price is shown.',
                  'Launches bring temporary flight restrictions and closed airspace around Cape Canaveral: check NOTAMs and TFRs before you go. Summer afternoons bring thunderstorms.'],
        'around_title': 'Rental car.',
        'around': 'Rent a car through the FBO. Kennedy Space Center is a short drive east across the river; Cocoa Beach and Port Canaveral are farther south. Bring car seats or reserve them with the car.',
    },
    'stay': {
        'title': 'On the beach at Cocoa Beach.',
        'intro': 'Rates and availability need travel dates. Launch weekends and spring break fill early.',
        'cards': [
            ('Oceanfront · Resort', 'Westgate Cocoa Beach Resort', 'Suites with kitchens, on the beach near the Cocoa Beach Pier.', 'https://www.westgateresorts.com/hotels/florida/cocoa-beach/westgate-cocoa-beach-resort/'),
            ('Oceanfront · Hotel', 'Hilton Cocoa Beach Oceanfront', 'A beachfront hotel with a pool, a good base for a beach day.', 'https://www.hilton.com/en/hotels/ccbochf-hilton-cocoa-beach-oceanfront/'),
        ],
    },
    'eat': {
        'title': 'Rock shrimp and seafood on the water.',
        'intro': 'Casual and kid-friendly.',
        'cards': [
            ('Dinner · Titusville', 'Dixie Crossroads', 'A Titusville institution known for its local rock shrimp.', 'https://www.dixiecrossroads.com/'),
            ('Lunch · Port Canaveral', 'Grills Seafood Deck & Tiki Bar', 'Seafood on the water at Port Canaveral, with a kids menu and cruise ships going by.', 'https://www.grillsseafood.com/'),
            ('Lunch · Cocoa Beach', 'Coconuts on the Beach', 'Seafood and live music right on the sand at Cocoa Beach.', 'https://coconutsonthebeach.com/'),
        ],
    },
    'explore': {
        'title': 'Rockets, warbirds and wildlife.',
        'intro': 'A full space day, an aviation morning on the field and the wild side of the Cape.',
        'items': [
            ('Kennedy Space Center Visitor Complex', 'Space Shuttle Atlantis, the rocket garden and the bus tour to the Apollo/Saturn V Center. Plan a full day and buy tickets ahead.', 'https://www.kennedyspacecenter.com/', 'Kennedy Space Center'),
            ('Valiant Air Command Warbird Museum', 'Restored military aircraft in hangars on the airport, at 6600 Tico Road. Call 321-268-1941 for hours.', 'https://www.valiantaircommand.com/', 'Valiant Air Command'),
            ('Merritt Island National Wildlife Refuge', 'Birds, alligators and, in season, manatees around the launch complex; Black Point Wildlife Drive is an easy loop by car.', 'https://www.fws.gov/refuge/merritt-island', 'U.S. Fish & Wildlife Service'),
            ('American Space Museum', 'A small museum in Titusville on the people who built the space program.', 'https://www.americanspacemuseum.org/', 'American Space Museum'),
        ],
    },
    'events': {
        'url': 'https://www.kennedyspacecenter.com/launches-and-events', 'button': 'See upcoming launches',
        'cards': [
            ('Most weeks', 'Rocket launches', 'Launches are frequent but dates slip; check the schedule close to the trip and have a backup plan.', 'https://www.kennedyspacecenter.com/launches-and-events'),
            ('Spring', 'Tico Warbird Airshow', 'An annual airshow at Space Coast Regional; check the dates, as the airport gets busy.', 'https://www.valiantaircommand.com/'),
            ('Summer', 'Storm season', 'Hot afternoons with thunderstorms; fly in the morning.'),
        ],
    },
    'itinerary': {
        'intro': 'A sample family weekend: a space day and a beach day. No bookings or availability confirmed.',
        'days': [
            ('DAY 1', 'Arrive & warbirds', [
                ('Arrival', 'Land at KTIX, subject to weather, launch restrictions and your actual flight plan.'),
                ('Afternoon', 'The Valiant Air Command Warbird Museum, on the field.'),
                ('Evening', 'Rock shrimp at Dixie Crossroads.')]),
            ('DAY 2', 'Kennedy Space Center', [
                ('Morning', 'Arrive at opening; start with the bus tour to the Saturn V.'),
                ('Afternoon', 'Space Shuttle Atlantis and the rocket garden.'),
                ('Evening', 'Black Point Wildlife Drive at sunset, then on to Cocoa Beach.')]),
            ('DAY 3', 'Beach & home', [
                ('Morning', 'The beach and the Cocoa Beach Pier.'),
                ('Before leaving', 'Check NOTAMs for any launch restrictions.'),
                ('Fly home', 'Summer storms build in the afternoon; leave early.')]),
        ],
    },
    'know': [
        ('Best ages', 'Kennedy Space Center works best for children about 5 and up; the beach and the warbirds suit every age.'),
        ('Launches', 'Launch times slip and restrictions close nearby airspace. Check NOTAMs and TFRs, and never plan the flight around a launch time.'),
        ('Book in this order', 'Lodging and Kennedy Space Center tickets first, then the rental car with child seats.'),
        ('Summer weather', 'Afternoon thunderstorms are common; plan morning arrivals and departures.'),
    ],
}

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
    # A family guide: say so in the tagline and page title.
    t = open(sys.argv[1]).read().replace(' · Couples · Two nights', ' · Families · Two nights').replace(' Couples Getaway |', ' Family Getaway |')
    open(sys.argv[1], 'w').write(t)
