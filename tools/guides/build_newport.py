"""Generate docs/newport/index.html (Newport, Rhode Island)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='newport', name='Newport', state='Rhode Island', number=30, reviewed='November 3, 2026',
    airport='KUUU', nm=595, flight_time='~4 hr 13 <small>min</small>', style='Rental car + walks',
    place='Newport, Rhode Island',
    description='A curated two-night Newport getaway for GA pilots and their partners, from KMYR to KUUU. Gilded Age mansions, the Cliff Walk, sailing, oceanfront inns and harbor dinners.',
    lede='Mansions, sailboats and the Cliff Walk.',
    intro='Newport is where Gilded Age families built their summer “cottages” above the Atlantic, and where America’s Cup sailors raced for more than 50 years. Walk the Cliff Walk past the mansions, tour The Breakers, sail on the harbor at sunset, and end with dinner at an oceanfront inn.',
    pills=['Gilded Age mansions', 'Sailing', 'Oceanfront inns'],
    flight=dict(
        title='Land five minutes from town.',
        intro='KUUU, Newport State Airport, is a small, non-towered field in Middletown, about 10 minutes from downtown Newport.',
        fbo=('FlightLevel Aviation · Newport', '211 Airport Access Road, Middletown, RI 02842', '401-846-9400', 'https://flightlevelaviation.com/?p=1084'),
        notes=['FlightLevel lists hours of 8 a.m. to 4 p.m. and rental cars through Enterprise with prior arrangement. Ask about weekend tie-downs and fees. No live fuel price is shown.',
               'At about 600 nm from Myrtle Beach, most piston aircraft will need a fuel stop. Coastal fog is common, and Providence’s Class C airspace lies to the north. Review the sectional and current NOTAMs.'],
        around_title='Walk once you arrive.',
        around='Downtown, the harbor and Bellevue Avenue are walkable or a short ride apart. A car helps for Ocean Drive and Castle Hill.'),
    stay=dict(title='Choose your view of the water.', intro='An oceanfront inn, a Cliff Walk mansion or a harbor-view hideaway. Rates and availability need travel dates.',
        cards=[('Ocean Drive · Relais & Châteaux', 'Castle Hill Inn', 'A Victorian mansion on a point at the mouth of Narragansett Bay, with beach cottages, a lawn made for sunsets and one of Newport’s best dining rooms.', 'https://www.castlehillinn.com/'),
               ('Cliff Walk · Luxury', 'The Chanler at Cliff Walk', 'An 1870s mansion turned boutique hotel at the start of the Cliff Walk, with themed rooms and ocean views.', 'https://www.thechanler.com/'),
               ('Downtown · Auberge', 'The Vanderbilt', 'A restored 1909 Vanderbilt mansion in the middle of town, with a rooftop terrace and a spa. Walk to the harbor.', 'https://auberge.com/vanderbilt/')]),
    eat=dict(title='Two dinners. One by the harbor.', intro='Seafood, history and water views. Reserve weekend dinners, especially in summer.',
        cards=[('Friday dinner · Historic', 'White Horse Tavern', 'One of the oldest taverns in America, first licensed in 1673, with candlelit rooms and polished New England cooking.', 'https://whitehorsenewport.com/'),
               ('Saturday dinner · Ocean views', 'Castle Hill Inn', 'Refined dining looking out over the Bay. Have a drink on the lawn at sunset first.', 'https://www.castlehillinn.com/'),
               ('Lunch · Waterfront', 'The Mooring', 'Seafood and chowder on Sayer’s Wharf, overlooking the harbor’s sailboats.', 'https://www.mooringrestaurant.com/')]),
    explore=dict(title='Mansions, cliffs and the sea.', intro='Choose one big outing a day and leave time for the water.',
        items=[('The Newport Mansions', 'Tour The Breakers, the Vanderbilts’ 70-room summer “cottage,” and one or two others, such as Marble House or The Elms.', 'https://www.newportmansions.org/', 'Mansion tickets'),
               ('The Cliff Walk', 'A 3.5-mile path along the cliffs between the mansions and the ocean. The northern half from Memorial Boulevard is the easiest walk.'),
               ('Ocean Drive', 'A 10-mile coastal drive past rocky coves, Brenton Point and grand houses. Best in the late afternoon.'),
               ('A sail on the harbor', 'Sunset sails on classic schooners and America’s Cup yachts leave from the downtown wharves in season.'),
               ('Fort Adams & Bowen’s Wharf', 'A huge 19th-century fort at the harbor mouth, then shops and raw bars along the wharves.')]),
    spa=dict(title='The spa at The Vanderbilt', body='The Vanderbilt’s spa offers treatments in a restored mansion a short walk from the harbor.'),
    events=dict(url='https://www.discovernewport.org/', button='Browse Newport events',
        cards=[('July & August', 'Newport Jazz and Folk festivals', 'Two famous music festivals at Fort Adams. Tickets and lodging sell out early.'),
               ('September', 'Newport International Boat Show', 'One of the country’s big in-water boat shows, on the downtown waterfront.'),
               ('December', 'Christmas at the Newport Mansions', 'The Breakers and other mansions decorated for the holidays.')]),
    itinerary=dict(intro='A sample Friday–Sunday weekend: the mansions, the Cliff Walk and two seaside dinners. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & the harbor', [('Arrival', 'Land at KUUU, subject to weather, your fuel stop and your actual flight plan, and pick up the car.'), ('Afternoon', 'Check in and walk Bowen’s Wharf.'), ('Evening', 'Dinner at White Horse Tavern.')]),
              ('SAT', 'Mansions & the sea', [('Morning', 'The Breakers, then the Cliff Walk.'), ('Afternoon', 'Lunch at The Mooring, then Ocean Drive or a sail.'), ('Evening', 'Sunset on the lawn and dinner at Castle Hill Inn.')]),
              ('SUN', 'An easy departure', [('Morning', 'Fort Adams or a last walk by the water.'), ('Before leaving', 'Return the car and allow time at the FBO.'), ('Fly home', 'Morning fog is common on the coast; let weather set the departure.')])]),
    know=[('Book in this order', 'Lodging and a car first, then dinners, mansion tickets and a sail.'),
          ('Fuel stop', 'Plan a fuel stop on the way for most piston aircraft.'),
          ('Summer', 'July and August are busy and pricey. Spring and fall are easier.'),
          ('Coastal weather', 'Fog and sea breezes are common. Keep a backup day.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
