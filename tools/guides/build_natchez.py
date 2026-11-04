"""Generate docs/natchez/index.html (Natchez, Mississippi)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='natchez', name='Natchez', state='Mississippi', number=69, reviewed=None,
    airport='KHEZ', nm=637, flight_time='~4 hr 29 <small>min</small>', style='Rental car',
    place='Natchez, Mississippi',
    description='A curated Natchez getaway for GA pilots and their partners, from KMYR to KHEZ. Antebellum mansions on a Mississippi River bluff, historic inns, the Natchez Trace and river sunsets.',
    lede='Antebellum mansions on a bluff above the Mississippi.',
    intro='Founded in 1716, Natchez is the oldest settlement on the Mississippi River, and it has more surviving antebellum homes than anywhere else in the country. Stay in a historic inn, tour Melrose and the octagonal Longwood, walk the bluff at sunset and drive the first miles of the Natchez Trace Parkway.',
    pills=['Historic inns', 'Antebellum homes', 'River bluff sunsets'],
    flight=dict(
        title='A quiet county field.',
        intro='KHEZ, Natchez–Adams County Airport, is a non-towered field northeast of town, a short drive from downtown and the bluff.',
        fbo=('Natchez–Adams County Airport', 'Natchez–Adams County Airport, Natchez, MS', '601-442-3142'),
        notes=['The airport sells fuel and handles parking; confirm hours, overnight fees and ground transportation before you go. No live fuel price is shown.',
               'Summer brings afternoon storms. About 640 nm from Myrtle Beach: plan a fuel stop and three nights.'],
        around_title='Arrange a car ahead.',
        around='Downtown and the bluff are walkable, but you will want a car for the mansions, Longwood and the Trace. Arrange a rental or ride before you land.'),
    stay=dict(title='Sleep in a historic mansion.', intro='Rates and availability need travel dates. Book early for Pilgrimage weeks.',
        cards=[('Historic inn · 1818', 'Monmouth Historic Inn', 'A Greek Revival estate with gardens, cottages and a candlelit dining room.', 'https://monmouthhistoricinn.com/'),
               ('Historic inn · 1856', 'Dunleith Historic Inn', 'A colonnaded mansion on 40 acres, home of the Castle Restaurant.', 'https://www.dunleithhistoricinn.com/'),
               ('Downtown · River views', 'Natchez Grand Hotel', 'A boutique hotel on the bluff, an easy walk to dinner.', 'https://www.natchezgrandhotel.com/')]),
    eat=dict(title='Southern cooking and river views.', intro='Many restaurants close early in the week; check hours.',
        cards=[('Friday dinner · Under-the-Hill', 'Magnolia Grill', 'Seafood and Southern plates below the bluff, with views of the river.', 'https://magnoliagrill.com/'),
               ('Saturday dinner · Historic', 'The Castle Restaurant', 'Dinner in the 1790s carriage house at Dunleith.', 'https://www.dunleithhistoricinn.com/the-castle-restaurant/'),
               ('Lunch · Local favorite', 'Fat Mama’s Tamales', 'Famous tamales and “knock-you-naked” margaritas.', 'https://www.fatmamastamales.com/'),
               ('Lunch · Main Street', 'Biscuits and Blues', 'Southern comfort food with live blues on weekends.', 'https://www.biscuitblues.com/')]),
    explore=dict(title='Mansions, the river and the Trace.', intro='Pick one or two house tours a day and leave time for the bluff.',
        items=[('Natchez National Historical Park', 'Melrose estate and the William Johnson House, the home of a free Black barber and diarist.', 'https://www.nps.gov/natc/', 'Park'),
               ('Longwood', 'A huge octagonal mansion left unfinished when the Civil War began.', 'https://visitnatchez.org/listing/longwood/', 'Longwood'),
               ('The bluff & Natchez Under-the-Hill', 'Walk the bluff-top park at sunset, then visit the old river landing.', 'https://visitmississippi.org/things-to-do/architecture/natchez-under-the-hill-historic-district/', 'Under-the-Hill'),
               ('Natchez Trace Parkway', 'The 444-mile parkway begins here; drive to Emerald Mound, a 600-year-old ceremonial mound.', 'https://www.nps.gov/natr/', 'Parkway'),
               ('Pilgrimage tours', 'Seasonal tours open private historic homes.', 'https://natchezpilgrimage.com/', 'Tours')]),
    events=dict(url='https://visitnatchez.org/', button='Browse Natchez events',
        cards=[('March–April', 'Spring Pilgrimage', 'Historic homes open for tours, the town’s signature event.', 'https://natchezpilgrimage.com/', 'Pilgrimage'),
               ('October', 'Fall Pilgrimage & Balloon Festival', 'Fall home tours and the Natchez Balloon Festival.', 'https://natchezballoonfestival.com/', 'Balloon Festival'),
               ('Spring & fall', 'Best seasons', 'Mild weather; summers are hot and humid.')]),
    itinerary=dict(intro='A sample long weekend: houses, the river and the Trace. Plan three nights for the flight. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & the bluff', [('Arrival', 'Land at KHEZ, subject to weather, your fuel stop and your actual flight plan.'), ('Afternoon', 'Check in and walk downtown and the bluff.'), ('Evening', 'Dinner at Magnolia Grill.')]),
              ('DAY 2', 'Houses & history', [('Morning', 'Melrose with a park ranger.'), ('Afternoon', 'Longwood, then lunch at Fat Mama’s.'), ('Evening', 'Dinner at the Castle Restaurant.')]),
              ('DAY 3', 'The Trace & home', [('Morning', 'Drive the Trace to Emerald Mound.'), ('Before leaving', 'Allow time at the airport.'), ('Fly home', 'Summer storms build in the afternoon; leave early.')])]),
    know=[('Book in this order', 'Lodging first, then Pilgrimage tours and dinners.'),
          ('Ground transport', 'Arrange a car before you land.'),
          ('Long flight', 'About 640 nm. Plan a fuel stop and extra nights.'),
          ('History', 'House tours increasingly include the lives of the enslaved people who built and ran these estates.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
