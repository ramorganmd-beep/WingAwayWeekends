"""Generate docs/south-padre/index.html (South Padre Island, Texas)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='south-padre', name='South Padre Island', state='Texas', number=66, reviewed='November 4, 2026',
    airport='KPIL', nm=1057, flight_time='~7 hr 18 <small>min</small>', style='Rental car',
    place='South Padre Island, Texas',
    description='A curated South Padre Island getaway for GA pilots and their partners, from KMYR to KPIL. Texas’s southernmost beaches, sea turtles, dolphins, a historic lighthouse and seafood by the bay.',
    lede='Texas’s tropical tip: beaches, turtles and dolphins.',
    intro='At the southern tip of Texas, South Padre Island has warm water, wide beaches and a laid-back, almost tropical feel. Meet rescued sea turtles, watch dolphins in the Laguna Madre, climb the 1852 Port Isabel Lighthouse and eat fresh Gulf shrimp on the bay at sunset.',
    pills=['Beaches', 'Sea turtles', 'Bay sunsets'],
    flight=dict(
        title='Land on the mainland, 15 minutes from the island.',
        intro='KPIL, Port Isabel–Cameron County Airport, is a non-towered field on the mainland, about 15 minutes from the Queen Isabella Causeway and the island.',
        fbo=('Southwind Airlines (FBO) · Port Isabel–Cameron County Airport', 'Port Isabel–Cameron County Airport, Los Fresnos, TX 78566', '956-559-6677'),
        notes=['Sources give different FBO phone numbers, so confirm. Listed hours are 8 a.m. to 5 p.m. Arrange a rental car ahead. No live fuel price is shown.',
               'SpaceX’s Starbase at Boca Chica is nearby; launches bring TFRs and closures, so check NOTAMs closely. The Mexican border is close; brief the ADIZ and airspace. About 1,060 nm from Myrtle Beach: plan one or two fuel stops and three or four nights.'],
        around_title='A car, then flip-flops.',
        around='The island is small and easy to explore; a car helps for the causeway and Port Isabel.'),
    stay=dict(title='On the beach.', intro='Rates and availability need travel dates; spring break is busiest.',
        cards=[('Beachfront · Resort', 'Margaritaville Beach Resort South Padre Island', 'The island’s big beachfront resort, transformed from the former Pearl, with pools and Gulf views.', 'https://www.margaritavilleresorts.com/margaritaville-beach-resort-south-padre-island'),
               ('Explore more', 'Visit South Padre Island', 'Beach condos, small hotels and rentals from the island visitor bureau.', 'https://visitsouthpadreisland.com/'),
               ('Port Isabel · Lighthouse town', 'Port Isabel', 'The mainland fishing town across the causeway has small inns and the historic lighthouse.', 'https://www.portisabellighthouse.com/')]),
    eat=dict(title='Gulf seafood by the bay.', intro='Reserve sunset tables in season.',
        cards=[('Friday dinner · Bayside', 'Sea Ranch Restaurant', 'Fresh Gulf seafood on the bay at the island’s south end.', 'https://www.searanchrestaurant.com/'),
               ('Saturday dinner · Sunset', 'Pier 19', 'A long-running restaurant on a pier over the Laguna Madre; go for sunset.', 'https://www.pier19.us/'),
               ('Lunch · Bayside', 'Louie’s Backyard', 'A big, casual bayside spot famous for its sunset views.', 'https://www.louiesbackyard.com/')]),
    explore=dict(title='Turtles, dolphins and a lighthouse.', intro='Slow beach days.',
        items=[('Sea Turtle, Inc.', 'A rescue center for sea turtles, with daily presentations.', 'https://seaturtleinc.org/', 'Visit information'),
               ('Dolphin watching', 'Boat tours on the Laguna Madre, where bottlenose dolphins are common.'),
               ('Port Isabel Lighthouse', 'Climb the 1852 lighthouse for views over the bay and island.', 'https://www.portisabellighthouse.com/', 'Lighthouse information'),
               ('The beaches', 'Wide, uncrowded beaches north of town.'),
               ('Laguna Atascosa National Wildlife Refuge', 'Birding and wild Texas on the mainland.')]),
    events=dict(url='https://visitsouthpadreisland.com/', button='Browse South Padre events',
        cards=[('March', 'Spring break', 'Very busy; best avoided for a quiet getaway.'),
               ('October–November', 'Fall season', 'Warm water and quiet beaches.'),
               ('Winter', 'Mild winter', 'Pleasant days and birding season.')]),
    itinerary=dict(intro='A sample long weekend: turtles, dolphins and two bayside sunsets. Plan three or four nights for the flight. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & the island', [('Arrival', 'Land at KPIL, subject to weather, TFRs, your fuel stops and your actual flight plan.'), ('Afternoon', 'Cross the causeway and check in.'), ('Evening', 'Dinner at Sea Ranch.')]),
              ('DAY 2', 'Turtles & dolphins', [('Morning', 'Sea Turtle, Inc.'), ('Afternoon', 'A dolphin boat tour, then the beach.'), ('Evening', 'Sunset dinner at Pier 19.')]),
              ('DAY 3', 'The lighthouse & home', [('Morning', 'Climb the Port Isabel Lighthouse.'), ('Before leaving', 'Check TFRs and allow time at the FBO.'), ('Fly home', 'A long trip home. Start early and let weather set the plan.')])]),
    know=[('Book in this order', 'Lodging and a car first, then dinners and a dolphin tour.'),
          ('Launch TFRs', 'SpaceX launches nearby close airspace. Check NOTAMs every day.'),
          ('Long flight', 'About 1,060 nm. Plan fuel stops and extra nights.'),
          ('Hurricane season', 'June through November. Keep plans flexible.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
