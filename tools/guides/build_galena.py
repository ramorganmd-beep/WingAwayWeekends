"""Generate docs/galena/index.html (Galena, Illinois)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='galena', name='Galena', state='Illinois', number=48, reviewed='November 3, 2026',
    airport='KDBQ', nm=763, flight_time='~5 hr 21 <small>min</small>', style='Rental car + walks',
    place='Galena, Illinois',
    description='A curated two-night Galena getaway for GA pilots and their partners, from KMYR to KDBQ. A 19th-century river town of brick shops, Ulysses S. Grant’s home, rolling hills, wineries and the Mississippi.',
    lede='A 19th-century river town in the rolling hills.',
    intro='Galena was a booming lead-mining and steamboat town in the 1850s, and most of its brick downtown survives. Stroll a mile of shops and restaurants on Main Street, tour the house the town gave Ulysses S. Grant after the Civil War, drive the hills to a winery and watch the Mississippi from the bluffs.',
    pills=['Historic Main Street', 'Grant’s home', 'Rolling hills'],
    flight=dict(
        title='Land across the river in Iowa.',
        intro='KDBQ, Dubuque Regional, is a towered airport in Iowa, about 30 minutes from Galena across the Mississippi.',
        fbo=('Dubuque Jet Center', '11000 Airport Road, Dubuque, IA 52003', '563-589-4136'),
        notes=['Ask about rental cars, parking, fees and hours. No live fuel price is shown.',
               'The Mississippi River valley can bring fog and gusty winds. About 760 nm from Myrtle Beach: plan a fuel stop and consider a third night. Review the sectional and current NOTAMs.'],
        around_title='A car, then walk.',
        around='Rent a car at Dubuque. Downtown Galena is walkable; the hills, wineries and Eagle Ridge need a car.'),
    stay=dict(title='Downtown or in the hills.', intro='Rates and availability need travel dates.',
        cards=[('Main Street · Since 1855', 'DeSoto House Hotel', 'Illinois’ oldest operating hotel, on Main Street, where Lincoln and Grant both spoke.', 'https://desotohouse.com/'),
               ('Hills · Golf resort & spa', 'Eagle Ridge Resort & Spa', 'A resort in the hills east of town with golf, a spa and a lake.', 'https://www.eagleridge.com/'),
               ('Explore more', 'Galena inns & B&Bs', 'Galena has dozens of historic inns; browse them on the town visitor site.', 'https://www.visitgalena.org/')]),
    eat=dict(title='Two dinners. One river view.', intro='Reserve weekend dinners.',
        cards=[('Friday dinner · Bistro', 'Fritz & Frites', 'A cozy French-German bistro, a Galena favorite.', 'https://fritzandfrites.com/'),
               ('Saturday dinner · Main Street', 'One Eleven Main', 'Farm-to-table Midwestern cooking in a historic Main Street building.', 'https://www.galenarestaurants.com/one-eleven-main.aspx'),
               ('Lunch · Main Street', 'Main Street cafés', 'Lunch and a wine or chocolate shop or two along Main Street.')]),
    explore=dict(title='History, hills and the river.', intro='Slow down and wander.',
        items=[('Main Street', 'A mile of 19th-century brick buildings full of shops, galleries and wine tasting rooms.'),
               ('Ulysses S. Grant Home', 'The house the people of Galena gave Grant in 1865, with many original furnishings.', 'https://www.granthome.org/', 'Visit information'),
               ('Galena River Trail', 'An easy riverside walk or bike ride from downtown.'),
               ('Wineries & the hills', 'Scenic drives through the Driftless Area hills to small wineries. Taste on the non-flying day.'),
               ('The Mississippi', 'Views from the bluffs, or a riverboat cruise from Dubuque.')]),
    spa=dict(title='The spa at Eagle Ridge', body='Eagle Ridge’s spa offers couples treatments in the hills a few minutes from town.'),
    events=dict(url='https://www.visitgalena.org/', button='Browse Galena events',
        cards=[('October', 'Fall color & Halloween parade', 'The hills turn and Main Street fills up. Book early.'),
               ('Summer', 'Festivals & wineries', 'Outdoor concerts and long evenings.'),
               ('November–December', 'Holiday season', 'Night of the Luminaria and holiday house walks.')]),
    itinerary=dict(intro='A sample weekend: Main Street, Grant’s home, the hills and two good dinners. A third night makes the long flight easier. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & Main Street', [('Arrival', 'Land at KDBQ, subject to weather, your fuel stop and your actual flight plan, and pick up the car.'), ('Afternoon', 'Drive to Galena and walk Main Street.'), ('Evening', 'Dinner at Fritz & Frites.')]),
              ('SAT', 'History & hills', [('Morning', 'Grant’s home.'), ('Afternoon', 'A drive through the hills to a winery, or the spa at Eagle Ridge.'), ('Evening', 'Dinner at One Eleven Main.')]),
              ('SUN', 'An easy departure', [('Morning', 'The Galena River Trail.'), ('Before leaving', 'Drive back to Dubuque and return the car.'), ('Fly home', 'River-valley fog often lifts by mid-morning.')])]),
    know=[('Book in this order', 'Lodging and a car first, then dinners.'),
          ('Long flight', 'About 760 nm. Plan a fuel stop and consider a third night.'),
          ('Across the river', 'The airport is in Iowa, about 30 minutes away.'),
          ('Fall weekends', 'October is beautiful and busy.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
