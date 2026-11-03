"""Generate docs/islamorada/index.html (Islamorada, Florida Keys)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='islamorada', name='Islamorada', state='Florida', number=58, reviewed=None,
    airport='KMTH', nm=549, flight_time='~3 hr 55 <small>min</small>', style='Rental car',
    place='Islamorada, Florida Keys',
    description='A curated two-night Islamorada getaway for GA pilots and their partners, from KMYR to KMTH. The sport-fishing capital of the world: oceanfront resorts, tarpon at Robbie’s, reef snorkeling and sunset dinners in the sand.',
    lede='Turquoise water, tarpon and sunsets in the sand.',
    intro='Islamorada, in the upper Florida Keys, calls itself the sport-fishing capital of the world. Stay at a relaxed oceanfront resort, hand-feed giant tarpon at Robbie’s, snorkel the reef, and watch the sunset from a table in the sand on Florida Bay. It is quieter and greener than Key West.',
    pills=['Florida Keys', 'Fishing & snorkeling', 'Sunsets'],
    flight=dict(
        title='Land in Marathon, 45 minutes south.',
        intro='KMTH, Florida Keys Marathon International, is the closest public airport to Islamorada, about 45 minutes north up the Overseas Highway.',
        fbo=('Million Air Florida Keys', '9400 Overseas Highway, Marathon, FL 33050', '305-743-1995'),
        notes=['Listed hours are 7 a.m. to 7 p.m., with an after-hours call-out fee; sources give slightly different street numbers, so confirm. Arrange a rental car ahead. No live fuel price is shown.',
               'The route crosses open water and military airspace near Key West and Homestead. Summer brings afternoon storms; hurricane season runs June to November. Review the sectional, restricted areas and current NOTAMs.'],
        around_title='You’ll want a car.',
        around='The Overseas Highway links everything. Allow extra time; traffic can be slow on weekends.'),
    stay=dict(title='Oceanfront and laid-back.', intro='Rates and availability need travel dates.',
        cards=[('Oceanfront · Resort', 'Cheeca Lodge & Spa', 'A classic Islamorada resort on the ocean, with a long pier, a spa and golf.', 'https://www.cheeca.com/'),
               ('Bayside · Cottages', 'The Moorings Village', 'Romantic cottages under the palms on a private beach.', 'https://www.themooringsvillage.com/'),
               ('Explore more', 'Islamorada visitor guide', 'More resorts and inns from the Florida Keys visitor site.', 'https://visitfloridakeys.com/discover-the-keys/destinations/islamorada')]),
    eat=dict(title='Two dinners. One in the sand.', intro='Reserve sunset tables.',
        cards=[('Friday dinner · Sunset in the sand', 'Morada Bay Beach Café', 'Tables in the sand on Florida Bay, best at sunset.', 'https://www.cheeca.com/dine-drink/the-beach-cafe'),
               ('Saturday dinner · Oceanfront', 'Atlantic’s Edge', 'Cheeca Lodge’s oceanfront restaurant, the special-occasion dinner.', 'https://www.cheeca.com/dine-drink/atlantics-edge'),
               ('Lunch · Waterfront', 'Islamorada Fish Company', 'Casual waterfront seafood on Florida Bay.', 'https://www.islamoradafishco.com/')]),
    explore=dict(title='Water, fish and history.', intro='Plan one day on the water.',
        items=[('Robbie’s of Islamorada', 'Hand-feed giant tarpon from the dock, then rent a boat or kayak.', 'https://www.robbies.com/', 'Visit information'),
               ('Snorkel or dive the reef', 'Trips go out to Alligator Reef and other spots on the only living coral barrier reef in the continental U.S.'),
               ('A fishing charter', 'Backcountry or offshore charters for tarpon, bonefish and sailfish.'),
               ('History of Diving Museum', 'Helmets, suits and stories from centuries of diving.', 'https://divingmuseum.org/', 'Museum information'),
               ('Theater of the Sea', 'A long-running marine park with dolphins and sea lions.', 'https://theaterofthesea.com/', 'Visit information')]),
    spa=dict(title='The spa at Cheeca Lodge', body='Cheeca’s spa offers couples treatments steps from the ocean.'),
    events=dict(url='https://visitfloridakeys.com/discover-the-keys/destinations/islamorada', button='Browse Islamorada events',
        cards=[('Spring', 'Tarpon season', 'Prime months for tarpon fishing.'),
               ('December–April', 'High season', 'Dry, warm and busy.'),
               ('Summer & fall', 'Quiet season', 'Calm seas for snorkeling; afternoon storms and hurricane season.')]),
    itinerary=dict(intro='A sample Friday–Sunday weekend: tarpon, the reef and two sunset dinners. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & sunset', [('Arrival', 'Land at KMTH, subject to weather and your actual flight plan, and drive north.'), ('Afternoon', 'Check in and feed the tarpon at Robbie’s.'), ('Evening', 'Sunset dinner at Morada Bay Beach Café.')]),
              ('SAT', 'On the water', [('Morning', 'A reef snorkel trip or a fishing charter.'), ('Afternoon', 'Lunch at Islamorada Fish Company, then the spa.'), ('Evening', 'Dinner at Atlantic’s Edge.')]),
              ('SUN', 'An easy departure', [('Morning', 'The History of Diving Museum.'), ('Before leaving', 'Allow time for the drive and the FBO.'), ('Fly home', 'Summer storms build in the afternoon; leave early.')])]),
    know=[('Book in this order', 'Lodging and a car first, then charters and dinners.'),
          ('Airport', 'Marathon is 45 minutes away. Plan the drive.'),
          ('Military airspace', 'Brief restricted areas near Key West and Homestead.'),
          ('Hurricane season', 'June through November. Keep plans flexible.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
