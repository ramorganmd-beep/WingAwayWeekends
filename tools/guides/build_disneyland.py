"""Generate docs/disneyland/index.html."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = {
    'slug': 'disneyland', 'name': 'Anaheim & Disneyland', 'state': 'California', 'number': 313, 'reviewed': 'November 21, 2026',
    'researched': 'November 21, 2026',
    'airport': 'KFUL', 'nm': 1937, 'flight_time': '~13 hr 10 <small>min</small>', 'style': 'Rental car or Uber',
    'place': 'Anaheim, California',
    'description': 'A family fly-in weekend at Disneyland: land at Fullerton Municipal, a small towered airport a short drive from the Disneyland Resort, then add Knott’s Berry Farm, Downtown Disney and a hands-on science museum.',
    'lede': 'The original Disney park, from a small airport next door.',
    'intro': 'Fullerton Municipal is a small towered airport in north Orange County, a short drive from the Disneyland Resort in Anaheim, and much quieter than John Wayne or Long Beach. Stay at a Disney hotel or close by, spend a day at Disneyland Park or Disney California Adventure, and add Knott’s Berry Farm, a few minutes from the airport, for a second park day. The sweet spot is about 4 to 12.',
    'pills': ['Family', 'Theme parks', 'Disney'],
    'flight': {
        'title': 'A small airport close to the parks.',
        'intro': 'KFUL, Fullerton Municipal, has a control tower and one runway, 6/24, 3,121 ft by 75 ft. General Aviation Co. is the FBO; it advertises no landing or ramp fees, and Hertz and Enterprise rental cars.',
        'fbo': ['General Aviation Co.', 'Fullerton Municipal Airport, Fullerton, CA', '714-526-6611', 'https://www.airnav.com/airport/KFUL'],
        'notes': ['FBO hours are listed as 8 a.m. to 5 p.m. weekdays and 9 a.m. to 5 p.m. weekends: arrange late arrivals ahead. Confirm fees, parking and rental cars. No live fuel price is shown.',
                  'The runway is 3,121 ft: check your takeoff and landing numbers, especially on warm days. KFUL sits under busy Los Angeles-area airspace, with the Los Angeles Class B and other towered airports close by; brief the arrival before you go.',
                  'A morning marine layer is common in late spring and early summer; it usually burns off by late morning.'],
        'around_title': 'Rental car or Uber.',
        'around': 'The Disneyland Resort is a short drive from the airport, and Knott’s Berry Farm in Buena Park is even closer. Reserve a rental car with child seats through the FBO, or use Uber with your own car seats.',
    },
    'stay': {
        'title': 'Inside the resort, or close by.',
        'intro': 'Rates and availability need travel dates. Summer, spring break and holidays fill early.',
        'cards': [
            ('At Disney · Classic', 'Disneyland Hotel', 'The original Disneyland hotel, a short walk through Downtown Disney to the park gates.', 'https://disneyland.disney.go.com/hotels/disneyland-hotel/'),
            ('At Disney · Splurge', 'Disney’s Grand Californian Hotel & Spa', 'A Craftsman-style lodge with its own entrance into Disney California Adventure.', 'https://disneyland.disney.go.com/hotels/grand-californian-hotel/'),
            ('At Disney · Pixar', 'Pixar Place Hotel', 'A Pixar-themed tower hotel within walking distance of both parks.', 'https://disneyland.disney.go.com/hotels/pixar-place-hotel/'),
        ],
    },
    'eat': {
        'title': 'Downtown Disney and a food hall.',
        'intro': 'Easy, casual and close to the parks.',
        'cards': [
            ('Dinner · Shopping district', 'Downtown Disney District', 'The free-to-enter dining and shopping street between the hotels and the park gates.', 'https://disneyland.disney.go.com/destinations/downtown-disney-district/'),
            ('Lunch · Food hall', 'Anaheim Packing District', 'A food hall in a restored citrus packing house in downtown Anaheim, with something for every child.', 'https://www.anaheimpackingdistrict.com/'),
            ('Breakfast · Bakery', 'Porto’s Bakery & Cafe, Buena Park', 'A famous Cuban bakery near Knott’s Berry Farm: pastries, sandwiches and long but fast-moving lines.', 'https://www.portosbakery.com/locations/'),
        ],
    },
    'explore': {
        'title': 'Disneyland, Knott’s and a rainy-day museum.',
        'intro': 'Pick one Disney park per day; the two parks face each other across a plaza.',
        'items': [
            ('Disneyland Resort', 'Disneyland Park, the original Disney park, and Disney California Adventure, with Pixar Pier and Avengers Campus. Buy tickets and any reservations ahead.', 'https://disneyland.disney.go.com/', 'Disneyland Resort'),
            ('Knott’s Berry Farm', 'A theme park in Buena Park, a few minutes from the airport, with rides for small children and big coasters for teens.', 'https://www.knotts.com/', 'Knott’s Berry Farm'),
            ('Discovery Cube Orange County', 'A hands-on science museum in Santa Ana, good for a slower morning or a hot afternoon.', 'https://www.discoverycube.org/orange-county/visit/', 'Discovery Cube'),
        ],
    },
    'events': {
        'url': 'https://disneyland.disney.go.com/', 'button': 'See the Disneyland Resort',
        'cards': [
            ('Fall', 'Halloween season', 'Both Disneyland and Knott’s decorate for Halloween; check each park’s calendar.'),
            ('Winter', 'Holidays', 'Holiday decorations from about mid-November; busy around Christmas and New Year’s.'),
            ('Summer', 'Busy season', 'Longest park hours and the biggest crowds; a morning marine layer at the airport is common.'),
        ],
    },
    'itinerary': {
        'intro': 'A sample family weekend: one Disney day and one easier day. No bookings or availability confirmed.',
        'days': [
            ('DAY 1', 'Arrive & Downtown Disney', [
                ('Arrival', 'Land at KFUL, subject to weather and your actual flight plan; pick up the rental car and check in.'),
                ('Afternoon', 'Pool time at the hotel.'),
                ('Evening', 'Dinner and a stroll in the Downtown Disney District.')]),
            ('DAY 2', 'Disney day', [
                ('Morning', 'Be at the gate at opening for the shortest lines.'),
                ('Afternoon', 'A midday break at the hotel helps younger children.'),
                ('Evening', 'Back for the evening shows if everyone has the energy.')]),
            ('DAY 3', 'Knott’s or the museum, then home', [
                ('Morning', 'Breakfast at Porto’s, then Knott’s Berry Farm or Discovery Cube.'),
                ('Before leaving', 'The FBO closes at 5 p.m.; plan your departure around its hours.'),
                ('Fly home', 'Check your performance numbers for the 3,121 ft runway.')]),
        ],
    },
    'know': [
        ('Best ages', 'Disneyland Park suits children about 3 to 10; older kids and teens may prefer California Adventure or Knott’s bigger coasters.'),
        ('Book in this order', 'Park tickets and any reservations first, then the hotel, then the rental car with child seats.'),
        ('Short runway', 'KFUL’s runway is 3,121 ft. Load and plan with your aircraft’s numbers; on a hot day, consider a lighter fuel load.'),
        ('Car seats', 'Bring your own or reserve them with the rental car; Uber drivers do not supply them.'),
    ],
}

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
    t = open(sys.argv[1]).read().replace(' · Couples · Two nights', ' · Families · Two nights').replace(' Couples Getaway |', ' Family Getaway |')
    open(sys.argv[1], 'w').write(t)
