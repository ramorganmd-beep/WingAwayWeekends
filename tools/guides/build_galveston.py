"""Generate docs/galveston/index.html (Galveston, Texas)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='galveston', name='Galveston', state='Texas', number=65, reviewed='November 4, 2026',
    airport='KGLS', nm=857, flight_time='~5 hr 58 <small>min</small>', style='Rental car or trolley',
    place='Galveston, Texas',
    description='A curated Galveston getaway for GA pilots and their partners, from KMYR to KGLS. A Victorian island city on the Gulf: the Strand, grand mansions, a tall ship, the seawall and seafood since 1911.',
    lede='Victorian mansions, the Strand and Gulf seafood.',
    intro='Galveston was once Texas’s richest city, and its Victorian mansions and the iron-front buildings of the Strand still show it. Walk the historic district, tour the 1892 Bishop’s Palace, climb aboard the 1877 tall ship Elissa, ride a bike along the seawall and eat seafood at a restaurant that has been on the beach since 1911.',
    pills=['Victorian island', 'Historic Strand', 'Gulf seafood'],
    flight=dict(
        title='Land on the island.',
        intro='KGLS, Scholes International at Galveston, is a towered airport on the island, about 10 minutes from the Strand and the seawall.',
        fbo=('Island Jet Center', '2115 Terminal Drive, Galveston, TX 77554', '409-572-2555'),
        notes=['Directories list two FBO names here, Island Jet Center and Galveston Aviation Services; confirm the current operator, hours and fees. No live fuel price is shown.',
               'Houston’s Class B airspace lies to the north. Summer brings afternoon storms, and hurricane season runs June to November. About 860 nm from Myrtle Beach: plan a fuel stop and three nights.'],
        around_title='A car or the trolley.',
        around='The Strand and downtown are walkable; a car or the island trolley helps for the seawall and beaches.'),
    stay=dict(title='A grande dame on the Gulf or a downtown classic.', intro='Rates and availability need travel dates.',
        cards=[('Seawall · Since 1911', 'Grand Galvez', 'The historic “Queen of the Gulf,” restored, with a spa and Gulf views.', 'https://www.grandgalvez.com/'),
               ('Downtown · Historic', 'The Tremont House', 'An elegant 1879 hotel a block from the Strand, with a rooftop bar.', 'https://www.thetremonthouse.com/'),
               ('Seawall · Resort', 'The San Luis Resort', 'A beachfront resort on the seawall with pools and a spa.', 'https://www.sanluisresort.com/')]),
    eat=dict(title='Seafood with a view.', intro='Reserve weekend dinners.',
        cards=[('Friday dinner · Since 1911', 'Gaido’s', 'A classic seafood restaurant on the seawall, run by the same family for more than a century.', 'https://www.gaidos.com/'),
               ('Saturday dinner · Fine dining', 'Rudy & Paco', 'South and Central American–inspired seafood and steaks downtown.', 'https://www.rudyandpaco.com/'),
               ('Lunch · Seawall', 'The Spot', 'A casual seawall favorite with Gulf views, from Island Famous.', 'https://www.islandfamous.com/')]),
    explore=dict(title='Mansions, ships and the seawall.', intro='Mix history with beach time.',
        items=[('The Strand Historic District', 'Iron-front Victorian buildings full of shops and cafés.'),
               ('Bishop’s Palace & Moody Mansion', 'Two grand Gilded Age houses, run by the Galveston Historical Foundation.', 'https://www.galvestonhistory.org/', 'Tours'),
               ('Elissa & the Texas Seaport Museum', 'An 1877 iron-hulled tall ship that still sails.'),
               ('The seawall', 'A 10-mile path above the beach, best by bike at sunrise.'),
               ('Pleasure Pier', 'A historic pier with rides over the Gulf.', 'https://www.pleasurepier.com/', 'Pleasure Pier')]),
    spa=dict(title='The spa at Grand Galvez', body='Grand Galvez’s spa offers couples treatments overlooking the Gulf.'),
    events=dict(url='https://www.visitgalveston.com/', button='Browse Galveston events',
        cards=[('February', 'Mardi Gras! Galveston', 'One of the largest Mardi Gras celebrations in the country.'),
               ('Early December', 'Dickens on The Strand', 'A Victorian holiday festival downtown.'),
               ('Spring & fall', 'Best seasons', 'Warm, with fewer storms than summer.')]),
    itinerary=dict(intro='A sample long weekend: the Strand, a mansion and the seawall. Plan three nights for the flight. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & the Strand', [('Arrival', 'Land at KGLS, subject to weather, your fuel stop and your actual flight plan.'), ('Afternoon', 'Walk the Strand.'), ('Evening', 'Dinner at Gaido’s.')]),
              ('DAY 2', 'Mansions & ships', [('Morning', 'Bishop’s Palace.'), ('Afternoon', 'Elissa, then the spa or the beach.'), ('Evening', 'Dinner at Rudy & Paco.')]),
              ('DAY 3', 'The seawall & home', [('Morning', 'Bike the seawall at sunrise.'), ('Before leaving', 'Allow time at the FBO.'), ('Fly home', 'Summer storms build in the afternoon; leave early.')])]),
    know=[('Book in this order', 'Lodging first, then dinners.'),
          ('Airspace', 'Brief Houston’s Class B.'),
          ('Long flight', 'About 860 nm. Plan a fuel stop and extra nights.'),
          ('Hurricane season', 'June through November. Keep plans flexible.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
