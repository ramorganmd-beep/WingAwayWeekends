"""Generate docs/sanibel/index.html (Sanibel and Captiva, Florida)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='sanibel', name='Sanibel & Captiva', state='Florida', number=57, reviewed='November 3, 2026',
    airport='KFMY', nm=452, flight_time='~3 hr 16 <small>min</small>', style='Rental car + bikes',
    place='Sanibel & Captiva, Florida',
    description='A curated two-night Sanibel and Captiva getaway for GA pilots and their partners, from KMYR to KFMY. Shell-covered beaches, a wildlife refuge, bike paths, island restaurants and Captiva sunsets.',
    lede='Shells, wildlife and island sunsets.',
    intro='Sanibel and Captiva are barrier islands off Fort Myers, famous for some of the best shelling in the world. Bike the island paths, drive or kayak the J.N. “Ding” Darling National Wildlife Refuge, walk the beach doing the “Sanibel stoop,” and watch the sun set over the Gulf from Captiva. The islands are still rebuilding after 2022’s Hurricane Ian, so check that places are open.',
    pills=['Shelling', 'Wildlife', 'Island sunsets'],
    flight=dict(
        title='Land at Page Field, 40 minutes from the islands.',
        intro='KFMY, Page Field, is a towered general aviation airport in Fort Myers, about 40 minutes from Sanibel across the causeway.',
        fbo=('Base Operations at Page Field', '5200 Captain Channing Page Drive, Fort Myers, FL 33907', '239-590-6600'),
        notes=['Self-serve 100LL is listed as available around the clock. Ask about rental cars, parking and fees. No live fuel price is shown.',
               'Southwest Florida International’s Class C airspace lies just to the south. Summer brings afternoon storms; hurricane season runs June to November. Review the sectional and current NOTAMs.'],
        around_title='A car, then bikes.',
        around='The Sanibel Causeway has a toll. On the islands, bike paths are the best way around.'),
    stay=dict(title='Island resorts.', intro='Rates and availability need travel dates; winter is peak season.',
        cards=[('Captiva · Historic resort', '’Tween Waters Island Resort', 'A long-running resort between the Gulf and the bay on Captiva, with a marina and sunsets.', 'https://tween-waters.com/'),
               ('Captiva · Resort', 'South Seas', 'A large island resort at the north end of Captiva, rebuilt and reopened after Hurricane Ian.', 'https://www.southseas.com/'),
               ('Sanibel · Beachfront', 'Island Inn', 'A beachfront inn on Sanibel with cottages and a relaxed feel.', 'https://islandinnsanibel.com/')]),
    eat=dict(title='Two dinners. One famous dessert.', intro='Reserve dinners in season.',
        cards=[('Friday dinner · Sunset', 'The Mucky Duck', 'A Captiva pub right on the beach, famous for its sunsets.', 'https://www.muckyduck.com/'),
               ('Saturday dinner · Captiva', 'The Bubble Room', 'A quirky Captiva institution full of vintage toys, known for its giant cakes.', 'https://bubbleroomrestaurant.com/'),
               ('Lunch · Sanibel', 'Doc Ford’s Rum Bar & Grille', 'A casual island spot named for novelist Randy Wayne White’s character.', 'https://docfords.com/')]),
    explore=dict(title='Shells, birds and bikes.', intro='Slow island days.',
        items=[('J.N. “Ding” Darling National Wildlife Refuge', 'Drive, bike or kayak through mangroves full of wading birds.', 'https://www.fws.gov/refuge/jn-ding-darling', 'Refuge information'),
               ('Shelling', 'Bowman’s Beach and Blind Pass are famous for shells, especially after a storm or at low tide.'),
               ('Bailey-Matthews National Shell Museum', 'Shells and sea life from around the world.', 'https://shellmuseum.org/', 'Museum information'),
               ('Sanibel Lighthouse', 'An 1884 lighthouse at the island’s eastern tip, with a fishing pier.'),
               ('Bike the islands', 'More than 25 miles of shared-use paths across Sanibel.')]),
    events=dict(url='https://www.visitfortmyers.com/', button='Browse Fort Myers & Sanibel events',
        cards=[('March', 'Sanibel Shell Festival', 'A long-running festival of shells and shell art.'),
               ('December–April', 'High season', 'Warm, dry and busy.'),
               ('Summer & fall', 'Quiet season', 'Lower rates, afternoon storms and hurricane season.')]),
    itinerary=dict(intro='A sample Friday–Sunday weekend: shells, wildlife and two island dinners. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & Captiva', [('Arrival', 'Land at KFMY, subject to weather and your actual flight plan, and pick up the car.'), ('Afternoon', 'Cross the causeway and check in.'), ('Evening', 'Sunset and dinner at The Mucky Duck.')]),
              ('SAT', 'Shells & birds', [('Morning', 'Shelling at low tide, then “Ding” Darling.'), ('Afternoon', 'Lunch at Doc Ford’s and the Shell Museum.'), ('Evening', 'Dinner and cake at The Bubble Room.')]),
              ('SUN', 'An easy departure', [('Morning', 'A bike ride to the lighthouse.'), ('Before leaving', 'Allow time for the causeway and the FBO.'), ('Fly home', 'Summer storms build in the afternoon; leave early.')])]),
    know=[('Book in this order', 'Lodging and a car first, then dinners.'),
          ('After Hurricane Ian', 'Some places are still rebuilding. Confirm they are open.'),
          ('Causeway toll', 'The Sanibel Causeway charges a toll.'),
          ('Hurricane season', 'June through November. Keep plans flexible.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
