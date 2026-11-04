"""Generate docs/natchitoches/index.html (Natchitoches, Louisiana)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='natchitoches', name='Natchitoches', state='Louisiana', number=81, reviewed='November 4, 2026',
    airport='KIER', nm=725, flight_time='~5 hr 04 <small>min</small>', style='Rental or arranged car',
    place='Natchitoches, Louisiana',
    description='A curated Natchitoches getaway for GA pilots and their partners, from KMYR to KIER. The oldest town in the Louisiana Purchase: brick-paved Front Street on Cane River Lake, historic B&Bs, meat pies, Creole plantations and a famous Christmas festival.',
    lede='The oldest town in the Louisiana Purchase, on Cane River Lake.',
    intro='Founded in 1714, Natchitoches (say “NACK-a-tish”) is older than New Orleans. Stay in a historic B&B, stroll brick-paved Front Street above Cane River Lake, eat a Natchitoches meat pie, visit the Creole plantations of the Cane River Creole National Historical Park and see the homes made famous by Steel Magnolias.',
    pills=['Historic B&Bs', 'Creole history', 'Small-town charm'],
    flight=dict(
        title='Land at the regional airport.',
        intro='KIER, Natchitoches Regional Airport, is a non-towered field a few minutes from downtown.',
        fbo=('Natchitoches Regional Airport', 'Natchitoches Regional Airport, Natchitoches, LA', '318-352-0994'),
        notes=['The airport runs its own FBO. Confirm hours, fees and ground transportation. No live fuel price is shown.',
               'Summer brings afternoon storms. About 725 nm from Myrtle Beach: plan a fuel stop and three nights.'],
        around_title='Arrange a car.',
        around='The historic district is walkable; you need a car for the Cane River plantations.'),
    stay=dict(title='Sleep in a historic B&B.', intro='Rates and availability need travel dates. The Christmas festival books up a year ahead.',
        cards=[('Historic district · B&B', 'Judge Porter House', 'A 1912 B&B a short walk from Front Street.', 'https://www.judgeporterhouse.com/'),
               ('Historic district · B&B', 'La Maison Louisiane', 'A historic B&B in town.', 'https://lamaisonlouisiane.net/'),
               ('On the river · B&B', 'Andrew Morris House', 'A B&B overlooking Cane River Lake.', 'https://www.andrewmorrishouse.com/')]),
    eat=dict(title='Meat pies and Cane River cooking.', intro='Many restaurants keep short hours; check before you go.',
        cards=[('Lunch · Since 1967', 'Lasyone’s Meat Pie Restaurant', 'The home of the Natchitoches meat pie, plus “Cane River cream pie.”', 'http://lasyones.com/'),
               ('Friday dinner · On the lake', 'Mariner’s Restaurant', 'Seafood and steaks on Sibley Lake.', 'https://www.marinersrestaurant.com/'),
               ('Saturday dinner · Front Street', 'Mayeaux’s Steak & Seafood', 'Steaks and Louisiana seafood downtown.', 'https://downtownnatchitoches.org/downtown-restaurants/'),
               ('Lunch · Front Street', 'Merci Beaucoup', 'Cajun and Creole lunch favorites.', 'https://downtownnatchitoches.org/downtown-restaurants/')]),
    explore=dict(title='Front Street and Cane River.', intro='Small-town strolling and Creole history.',
        items=[('Front Street', 'Brick-paved shops and balconies above Cane River Lake.', 'https://downtownnatchitoches.org/', 'Downtown'),
               ('Cane River Creole National Historical Park', 'Oakland and Magnolia plantations, interpreted by the Park Service.', 'https://www.nps.gov/cari/', 'Park'),
               ('Melrose Plantation', 'Home of the folk artist Clementine Hunter.', 'https://www.melroseplantation.org/', 'Melrose'),
               ('Fort St. Jean Baptiste', 'A replica of the 1716 French fort.', 'https://www.lastateparks.com/historic-sites/fort-st-jean-baptiste-state-historic-site', 'Historic site'),
               ('Steel Magnolias homes', 'See the houses from the 1989 film on a historic-district walk.', 'http://natchitoches.com/', 'Visit Natchitoches')]),
    events=dict(url='http://natchitoches.com/', button='Browse Natchitoches events',
        cards=[('November–January', 'Christmas Festival of Lights', 'Hundreds of thousands of lights along the river; the festival is in early December.', 'https://www.natchitocheschristmas.com/', 'Festival'),
               ('October', 'Natchitoches Pilgrimage', 'Tours of historic homes.', 'http://natchitoches.com/', 'Visit Natchitoches'),
               ('Spring & fall', 'Best seasons', 'Mild weather; summers are hot.')]),
    itinerary=dict(intro='A sample long weekend: Front Street, Cane River and meat pies. Plan three nights for the flight. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & Front Street', [('Arrival', 'Land at KIER, subject to weather, your fuel stop and your actual flight plan.'), ('Afternoon', 'Walk Front Street and the riverbank.'), ('Evening', 'Dinner at Mayeaux’s.')]),
              ('DAY 2', 'Cane River', [('Morning', 'Oakland Plantation with a ranger.'), ('Afternoon', 'Melrose Plantation.'), ('Evening', 'Dinner at Mariner’s.')]),
              ('DAY 3', 'Meat pies & home', [('Morning', 'Lunch at Lasyone’s.'), ('Before leaving', 'Allow time at the airport.'), ('Fly home', 'Summer storms build in the afternoon; leave early.')])]),
    know=[('Book in this order', 'Lodging first, then a car.'),
          ('Pronunciation', '“NACK-a-tish.”'),
          ('Long flight', 'About 725 nm. Plan a fuel stop and extra nights.'),
          ('History', 'The plantation sites tell the history of enslaved and free people of color on the Cane River.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
