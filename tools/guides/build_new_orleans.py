"""Generate docs/new-orleans/index.html (New Orleans, Louisiana)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='new-orleans', name='New Orleans', state='Louisiana', number=68, reviewed=None,
    airport='KNEW', nm=606, flight_time='~4 hr 18 <small>min</small>', style='Walk, streetcar or rideshare',
    place='New Orleans, Louisiana',
    description='A curated New Orleans getaway for GA pilots and their partners, from KMYR to KNEW. Land at the 1934 Lakefront Airport, then the French Quarter, jazz, Creole dining, the Garden District and the National WWII Museum.',
    lede='Jazz, Creole dining and the French Quarter, from a 1934 lakefront airport.',
    intro='New Orleans may be the best food-and-music weekend in the country, and Lakefront Airport puts you about 15 minutes from the French Quarter. Hear traditional jazz at Preservation Hall, linger over a jazz brunch at Commander’s Palace, ride the St. Charles streetcar through the Garden District and spend a morning at the National WWII Museum.',
    pills=['Jazz & music', 'Creole dining', 'Historic French Quarter'],
    flight=dict(
        title='Land on the lakefront.',
        intro='KNEW, New Orleans Lakefront Airport, is a towered field on a peninsula in Lake Pontchartrain, with an art deco terminal from 1934. It is much closer to the French Quarter than MSY.',
        fbo=('Flightline First', 'New Orleans Lakefront Airport, New Orleans, LA 70126', '504-244-4448'),
        notes=['Skyborne (504-946-3835) is a second FBO on the field. Confirm hours, ramp and overnight fees and courtesy-car availability. No live fuel price is shown.',
               'New Orleans Class B airspace surrounds the field; brief the arrival and the lake procedures. Summer brings afternoon storms, and hurricane season runs June to November. About 610 nm from Myrtle Beach: plan a fuel stop and three nights.'],
        around_title='Leave the car behind.',
        around='The French Quarter is best on foot; the St. Charles streetcar reaches the Garden District, and a rideshare from the airport takes about 15 minutes.'),
    stay=dict(title='A grand hotel or a French Quarter classic.', intro='Rates and availability need travel dates. Book early for festival weekends.',
        cards=[('CBD · Luxury', 'Windsor Court Hotel', 'A refined, art-filled hotel a short walk from the Quarter, with afternoon tea and a spa.', 'https://www.windsorcourthotel.com/'),
               ('French Quarter · Since 1886', 'Hotel Monteleone', 'A family-owned landmark on Royal Street, home of the revolving Carousel Bar.', 'https://www.hotelmonteleone.com/'),
               ('CBD · Historic', 'The Roosevelt New Orleans', 'A gilded 1893 grand hotel with the Sazerac Bar and a spa.', 'https://www.theroosevelthotel.com/')]),
    eat=dict(title='Creole classics and jazz brunch.', intro='Reserve weekend dinners and brunch well ahead; several old-line restaurants keep a dress code.',
        cards=[('Brunch · Garden District', 'Commander’s Palace', 'The famous jazz brunch in a turquoise Victorian, with 25-cent martinis at lunch.', 'https://www.commanderspalace.com/'),
               ('Friday dinner · Since 1905', 'Galatoire’s', 'A Bourbon Street institution for classic French Creole cooking.', 'https://www.galatoires.com/'),
               ('Breakfast · Royal Street', 'Brennan’s', 'The pink-walled home of Bananas Foster, with a courtyard.', 'https://www.brennansneworleans.com/'),
               ('Saturday dinner · Since 1918', 'Arnaud’s', 'Creole dining in the Quarter, with live jazz in the Jazz Bistro.', 'https://www.arnaudsrestaurant.com/')]),
    explore=dict(title='Music, history and the streetcar.', intro='Mix one big museum with long, slow wandering.',
        items=[('Preservation Hall', 'Intimate traditional-jazz sets in a 1750s building. Buy timed tickets ahead.', 'https://www.preservationhall.com/', 'Tickets'),
               ('The National WWII Museum', 'One of the country’s best museums, with aircraft in the US Freedom Pavilion. Allow most of a day.', 'https://www.nationalww2museum.org/', 'Museum'),
               ('St. Charles streetcar & the Garden District', 'Ride the oldest continuously operating streetcar line past oak-shaded mansions.'),
               ('Jackson Square & Café du Monde', 'Beignets and café au lait by the cathedral, then Royal Street’s galleries.'),
               ('Steamboat Natchez', 'A Mississippi River cruise with a live jazz band and a steam calliope.', 'https://www.steamboatnatchez.com/', 'Cruises')]),
    spa=dict(title='The spa at Windsor Court or The Roosevelt', body='Both hotels have full-service spas; ask about couples treatments.'),
    events=dict(url='https://www.neworleans.com/', button='Browse New Orleans events',
        cards=[('Late winter', 'Mardi Gras', 'Parades for weeks before Fat Tuesday. Book months ahead, or avoid it.'),
               ('April', 'French Quarter Festival', 'Free local music on stages across the Quarter.', 'https://www.frenchquarterfest.org/', 'Festival'),
               ('Late April–early May', 'Jazz Fest', 'The New Orleans Jazz & Heritage Festival.', 'https://www.nojazzfest.com/', 'Jazz Fest')]),
    itinerary=dict(intro='A sample long weekend: music, food and the streetcar. Plan three nights for the flight. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & the Quarter', [('Arrival', 'Land at KNEW, subject to weather, your fuel stop and your actual flight plan.'), ('Afternoon', 'Beignets at Café du Monde, then Jackson Square and Royal Street.'), ('Evening', 'Dinner at Galatoire’s, then Preservation Hall.')]),
              ('DAY 2', 'History & the Garden District', [('Morning', 'The National WWII Museum.'), ('Afternoon', 'Ride the streetcar and walk the Garden District.'), ('Evening', 'Dinner at Arnaud’s, with jazz.')]),
              ('DAY 3', 'Brunch & home', [('Morning', 'Jazz brunch at Commander’s Palace.'), ('Before leaving', 'See the 1934 Lakefront terminal and allow time at the FBO.'), ('Fly home', 'Summer storms build in the afternoon; leave early.')])]),
    know=[('Book in this order', 'Lodging first, then brunch and dinners, then Preservation Hall.'),
          ('Airspace', 'Brief the New Orleans Class B and the lakefront arrival.'),
          ('Long flight', 'About 610 nm. Plan a fuel stop and extra nights.'),
          ('Best seasons', 'October to May; summer is hot and humid, and hurricane season runs June to November.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
