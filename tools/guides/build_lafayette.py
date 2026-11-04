"""Generate docs/lafayette/index.html (Lafayette, Louisiana)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='lafayette', name='Lafayette & Cajun Country', state='Louisiana', number=73, reviewed='November 4, 2026',
    airport='KLFT', nm=697, flight_time='~4 hr 53 <small>min</small>', style='Rental car',
    place='Lafayette, Louisiana',
    description='A curated Lafayette getaway for GA pilots and their partners, from KMYR to KLFT. The heart of Cajun Country: dance halls, zydeco breakfast, boudin, swamp tours and Avery Island.',
    lede='Cajun music, zydeco breakfast and swamp sunsets.',
    intro='Lafayette is the capital of Cajun and Creole Louisiana, where French is still spoken and dance floors fill every night of the week. Two-step at the Blue Moon Saloon, dance at a zydeco breakfast in Breaux Bridge, eat boudin for breakfast, paddle among cypress at Lake Martin and tour the Tabasco factory on Avery Island.',
    pills=['Cajun & zydeco music', 'Cajun food', 'Swamps & bayous'],
    flight=dict(
        title='Land in Lafayette.',
        intro='KLFT, Lafayette Regional Airport, is a towered airport about 10 minutes from downtown and River Ranch.',
        fbo=('Signature Aviation', 'Lafayette Regional Airport, Lafayette, LA', '337-234-3100'),
        notes=['Confirm FBO hours, fees and rental-car pickup. No live fuel price is shown.',
               'Summer brings afternoon storms, and hurricane season runs June to November. About 700 nm from Myrtle Beach: plan a fuel stop and three nights.'],
        around_title='Rent a car.',
        around='Breaux Bridge, Lake Martin and Avery Island are spread out; you need a car.'),
    stay=dict(title='A boutique hotel, a guest house or a bayou B&B.', intro='Rates and availability need travel dates. Book early for festival weekends.',
        cards=[('River Ranch · Boutique', 'Carriage House Hotel', 'Twenty-one suites in Lafayette’s River Ranch neighborhood.', 'https://www.thecarriagehousehotel.com/'),
               ('Downtown · Music', 'Blue Moon Saloon & Guest House', 'Simple rooms behind one of the best live-music venues in Louisiana.', 'https://www.bluemoonpresents.com/'),
               ('Breaux Bridge · B&B', 'Maison Madeleine', 'A restored Creole cottage near Lake Martin.', 'https://www.maisonmadeleine.com/')]),
    eat=dict(title='Boudin, crawfish and a dance floor.', intro='Some local favorites keep short hours; check before you go.',
        cards=[('Friday dinner · Live music', 'Prejean’s', 'Cajun dishes with live Cajun music most nights.', 'https://prejeans.com/'),
               ('Breakfast · Boudin', 'Johnson’s Boucanière', 'Boudin, cracklins and smoked meats from a family business.', 'https://johnsonsboucaniere.com/'),
               ('Saturday breakfast · Zydeco', 'Buck & Johnny’s', 'The Saturday-morning zydeco breakfast in Breaux Bridge.', 'https://www.buckandjohnnys.com/', 'Zydeco breakfast')]),
    explore=dict(title='Music, swamps and hot sauce.', intro='Dance at night and get outside in the morning.',
        items=[('Blue Moon Saloon', 'Cajun, zydeco and roots music on a back porch.', 'https://www.bluemoonpresents.com/', 'Shows'),
               ('Vermilionville', 'A living-history village of Cajun, Creole and Native American life.', 'https://bayouvermiliondistrict.org/vermilionville/', 'Vermilionville'),
               ('Lake Martin', 'A cypress swamp and bird rookery near Breaux Bridge; take a guided boat tour.', 'https://www.lafayettetravel.com/', 'Lafayette Travel'),
               ('Avery Island & Tabasco', 'The Tabasco factory tour and Jungle Gardens.', 'https://www.tabasco.com/visit-avery-island/', 'Avery Island')]),
    events=dict(url='https://www.lafayettetravel.com/', button='Browse Lafayette events',
        cards=[('Late April', 'Festival International de Louisiane', 'A free downtown festival of world and Louisiana music.', 'https://festivalinternational.org/', 'Festival'),
               ('October', 'Festivals Acadiens et Créoles', 'A celebration of Cajun and Creole music and food.', 'https://festivalsacadiens.com/', 'Festival'),
               ('Late winter', 'Mardi Gras', 'City parades and rural Courir de Mardi Gras runs.', 'https://www.lafayettetravel.com/mardi-gras/', 'Mardi Gras')]),
    itinerary=dict(intro='A sample long weekend: music, food and the swamp. Plan three nights for the flight. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & dance', [('Arrival', 'Land at KLFT, subject to weather, your fuel stop and your actual flight plan.'), ('Afternoon', 'Vermilionville.'), ('Evening', 'Dinner at Prejean’s, then the Blue Moon Saloon.')]),
              ('DAY 2', 'Zydeco & the swamp', [('Morning', 'Zydeco breakfast at Buck & Johnny’s.'), ('Afternoon', 'A boat tour on Lake Martin.'), ('Evening', 'Dinner and live music downtown.')]),
              ('DAY 3', 'Avery Island & home', [('Morning', 'Boudin at Johnson’s, then Avery Island.'), ('Before leaving', 'Allow time at the FBO.'), ('Fly home', 'Summer storms build in the afternoon; leave early.')])]),
    know=[('Book in this order', 'Lodging first, then a swamp tour.'),
          ('Saturday morning', 'Plan around the zydeco breakfast.'),
          ('Long flight', 'About 700 nm. Plan a fuel stop and extra nights.'),
          ('Best seasons', 'October to May; crawfish season peaks in spring.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
