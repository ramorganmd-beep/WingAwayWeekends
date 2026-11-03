"""Generate docs/gettysburg/index.html (Gettysburg, Pennsylvania)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='gettysburg', name='Gettysburg', state='Pennsylvania', number=35, reviewed=None,
    airport='KW05', nm=378, flight_time='~2 hr 47 <small>min</small>', style='Courtesy or rental car',
    place='Gettysburg, Pennsylvania',
    description='A curated two-night Gettysburg getaway for GA pilots and their partners, from KMYR to KW05. A private battlefield guide, Eisenhower’s farm, a colonial tavern and Adams County orchards and wineries.',
    lede='Hallowed ground, colonial taverns and apple country.',
    intro='In July 1863, the largest battle of the Civil War was fought in the fields around this small Pennsylvania town, and Lincoln gave his Gettysburg Address here that November. Tour the battlefield with a licensed guide in your own car, visit Eisenhower’s farm, and dine by candlelight in a 1776 tavern.',
    pills=['Civil War history', 'Battlefield guides', 'Orchards & wineries'],
    flight=dict(
        title='Land three miles from the battlefield.',
        intro='KW05, Gettysburg Regional Airport, is a small field just west of town, a few minutes from the battlefield and downtown.',
        fbo=('Blouch Aircraft Services', '1150 Chambersburg Road, Gettysburg, PA 17325', '717-357-5958'),
        notes=['Directories list a courtesy car and rental cars; taxis and rideshares are scarce, so arrange a car ahead. Confirm the address, hours, parking and fees with the FBO. No live fuel price is shown.',
               'Camp David’s prohibited area P-40 lies about 15 nm southwest, and the Washington, DC SFRA is farther south. Brief both, check TFRs before every flight, and review the sectional and current NOTAMs.'],
        around_title='A car makes it easy.',
        around='Battlefield tours are done in your own car with a guide, and downtown is walkable once you park.'),
    stay=dict(title='In town or on the edge of history.', intro='Rates and availability need travel dates.',
        cards=[('Lincoln Square · Historic', 'Hotel Gettysburg', 'A landmark hotel on Lincoln Square, steps from the David Wills House, where Lincoln finished the Gettysburg Address.', 'https://hotelgettysburg.com/'),
               ('Downtown · Boutique', 'Federal Pointe Inn', 'A boutique hotel in a restored 1897 schoolhouse, a short walk from Lincoln Square.', 'https://www.federalpointeinn.com/'),
               ('Historic district · B&B', 'Brickhouse Inn', 'A welcoming bed-and-breakfast in two 19th-century houses, with a garden and homemade breakfasts.', 'https://brickhouseinn.com/')]),
    eat=dict(title='Two dinners. One by candlelight.', intro='History and comfort food. Reserve weekend dinners.',
        cards=[('Friday dinner · 1776 tavern', 'Dobbin House Tavern', 'Candlelit colonial dining in the oldest building in Gettysburg, with a cozy tavern downstairs.', 'https://www.dobbinhouse.com/'),
               ('Saturday dinner · 1810 house', 'Farnsworth House Inn', 'Dinner in a house still marked by bullet holes from the battle, with period dining rooms and Sweney’s Tavern.', 'https://farnsworthhouseinn.com/'),
               ('Lunch · Lincoln Square', 'The Pub & Restaurant', 'A lively, long-running spot on the square for sandwiches, salads and local beer.', 'https://www.the-pub.com/')]),
    explore=dict(title='Hallowed ground.', intro='Start at the Museum and Visitor Center, then see the battlefield with a guide.',
        items=[('Museum and Visitor Center', 'The film, the museum and the restored Gettysburg Cyclorama, a 377-foot painting of Pickett’s Charge. Allow two to three hours.', 'https://www.nps.gov/gett/', 'Park information'),
               ('A licensed battlefield guide', 'A two-hour private tour in your car with a Licensed Battlefield Guide, the best way to understand the three days. Book ahead through the Gettysburg Foundation.'),
               ('Little Round Top & the High Water Mark', 'Two of the battle’s most famous places, with sweeping views across the fields.'),
               ('Eisenhower National Historic Site', 'Ike’s farm and weekend retreat, reached by shuttle from the Visitor Center.', 'https://www.nps.gov/eise/', 'Shuttle and tours'),
               ('Adams County orchards and wineries', 'Apple country and small wineries just outside town. Taste on the non-flying day.')]),
    events=dict(url='https://www.nps.gov/gett/planyourvisit/calendar.htm', button='Browse park events',
        cards=[('July 1–3', 'Battle anniversary', 'Ranger programs and living history on the anniversary of the battle. Busy; book early.'),
               ('October', 'Apple Harvest Festival', 'Adams County’s big fall festival, in nearby Arendtsville.'),
               ('November', 'Remembrance Day & Dedication Day', 'Commemorations of Lincoln’s Gettysburg Address, given November 19, 1863.')]),
    itinerary=dict(intro='A sample Friday–Sunday weekend: the museum, a guided battlefield tour and two historic dinners. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & the museum', [('Arrival', 'Land at KW05, subject to weather and your actual flight plan, and pick up the car.'), ('Afternoon', 'The Museum and Visitor Center and the Cyclorama.'), ('Evening', 'Dinner at Dobbin House Tavern.')]),
              ('SAT', 'The battlefield', [('Morning', 'A two-hour tour with a Licensed Battlefield Guide.'), ('Afternoon', 'Lunch on Lincoln Square, then Eisenhower’s farm.'), ('Evening', 'Dinner at the Farnsworth House Inn.')]),
              ('SUN', 'An easy departure', [('Morning', 'A drive to Little Round Top at first light, or an orchard stop.'), ('Before leaving', 'Return the car and allow time at the FBO.'), ('Fly home', 'Check TFRs again before departure.')])]),
    know=[('Book in this order', 'A car and lodging first, then a battlefield guide and dinners.'),
          ('Airspace', 'P-40 (Camp David) is close by and can expand with little notice. Check TFRs before every flight.'),
          ('Busy weekends', 'Early July and fall weekends are busiest.'),
          ('Dates come next', 'Rates and restaurant hours are date-dependent. No availability or live price is implied here.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
