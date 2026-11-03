"""Generate docs/portsmouth/index.html (Portsmouth, New Hampshire)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='portsmouth', name='Portsmouth', state='New Hampshire', number=39, reviewed=None,
    airport='KPSM', nm=680, flight_time='~4 hr 48 <small>min</small>', style='Rental car + walks',
    place='Portsmouth, New Hampshire',
    description='A curated two-night Portsmouth getaway for GA pilots and their partners, from KMYR to KPSM. A 400-year-old harbor town, a grand seaside hotel, Strawbery Banke, a submarine museum and great seafood.',
    lede='A colonial harbor town with a great food scene.',
    intro='Founded in 1623, Portsmouth is one of America’s oldest towns, with brick streets running down to a working harbor. Walk the historic houses of Strawbery Banke, eat oysters and tapas downtown, cruise out to the Isles of Shoals and stay at a grand 1874 hotel by the sea.',
    pills=['Historic harbor', 'Food town', 'Grand hotel'],
    flight=dict(
        title='Land at a former Air Force base.',
        intro='KPSM, Portsmouth International at Pease, is a towered former Air Force base with a long runway, about 10 minutes from downtown.',
        fbo=('Port City Air', '104 Grafton Drive, Portsmouth, NH 03801', '603-430-1111', 'https://www.portcityair.com/'),
        notes=['Port City Air is open 24 hours. Ask about rental cars, parking and fees. No live fuel price is shown.',
               'Boston’s Class B airspace lies to the south. Coastal fog is common. About 680 nm from Myrtle Beach, so plan a fuel stop. Review the sectional and current NOTAMs.'],
        around_title='Walk downtown.',
        around='Market Square, the harbor, Strawbery Banke and Prescott Park are all walkable. Use a car for New Castle and the coast.'),
    stay=dict(title='Downtown or by the sea.', intro='Rates and availability need travel dates.',
        cards=[('New Castle · Grand hotel', 'Wentworth by the Sea', 'A restored 1874 grand hotel on an island at the harbor mouth, with a spa and ocean views. The romantic splurge.', 'https://www.opalcollection.com/wentworth/'),
               ('Downtown · Boutique', 'The Hotel Portsmouth', 'A boutique hotel in an 1881 Queen Anne mansion, a short walk from Market Square.', 'https://www.larkhotels.com/new-hampshire/portsmouth/the-hotel-portsmouth'),
               ('Waterfront · Casual', 'Ale House Inn', 'A small, modern inn in an old brewery warehouse, next to Strawbery Banke.', 'https://www.larkhotels.com/hotels/ale-house-inn')]),
    eat=dict(title='Two dinners. One seafood lunch.', intro='Portsmouth has more good restaurants than most cities its size. Reserve weekends.',
        cards=[('Friday dinner · Tapas', 'Moxy', 'Inventive small plates of New England ingredients, a downtown favorite.', 'https://www.moxyportsmouth.com/'),
               ('Saturday dinner · Oysters', 'Row 34', 'Oysters, lobster and craft beer in a lively room by the river.', 'https://www.row34.com/'),
               ('Lunch · Seafood', 'Jumpin’ Jay’s Fish Café', 'A small downtown fish café with a changing daily menu.', 'https://jumpinjays.com/')]),
    explore=dict(title='Four centuries by the harbor.', intro='Walk, eat, and get out on the water.',
        items=[('Strawbery Banke Museum', 'Ten acres of historic houses and gardens from four centuries of the neighborhood’s life. Seasonal.', 'https://www.strawberybanke.org/', 'Museum information'),
               ('Prescott Park & Market Square', 'Waterfront gardens, summer arts festival and the shops and cafés of the old town center.'),
               ('USS Albacore', 'A sleek 1950s experimental submarine you can walk through, a few minutes from downtown.', 'https://www.ussalbacore.org/', 'Visit information'),
               ('Isles of Shoals cruise', 'Harbor and island cruises leave from downtown in season, past lighthouses and forts.'),
               ('New Castle & the coast', 'A drive over the bridges to New Castle, Fort Constitution and Odiorne Point.')]),
    spa=dict(title='The spa at Wentworth by the Sea', body='The grand hotel’s spa offers couples treatments with views of the harbor and the sea.'),
    events=dict(url='https://www.goportsmouthnh.com/', button='Browse Portsmouth events',
        cards=[('Summer', 'Prescott Park Arts Festival', 'Outdoor concerts and shows on the waterfront.'),
               ('October', 'Fall color & harvest', 'Crisp days, quieter streets and seafood season.'),
               ('December', 'Candlelight Stroll', 'Strawbery Banke’s holiday evenings of candlelit historic houses.')]),
    itinerary=dict(intro='A sample Friday–Sunday weekend: history, the harbor and two excellent dinners. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & downtown', [('Arrival', 'Land at KPSM, subject to weather, your fuel stop and your actual flight plan, and pick up the car.'), ('Afternoon', 'Check in and walk Market Square and Prescott Park.'), ('Evening', 'Dinner at Moxy.')]),
              ('SAT', 'History & the water', [('Morning', 'Strawbery Banke.'), ('Afternoon', 'Lunch at Jumpin’ Jay’s, then a harbor cruise or the spa.'), ('Evening', 'Oysters and dinner at Row 34.')]),
              ('SUN', 'The coast & home', [('Morning', 'USS Albacore, or a drive to New Castle.'), ('Before leaving', 'Return the car and allow time at the FBO.'), ('Fly home', 'Let weather and your flight plan set the departure.')])]),
    know=[('Book in this order', 'Lodging and a car first, then dinners.'),
          ('Fuel stop', 'Plan a fuel stop for most piston aircraft.'),
          ('Seasons', 'Strawbery Banke and harbor cruises are seasonal.'),
          ('Coastal weather', 'Fog and sea breezes are common. Keep a backup day.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
