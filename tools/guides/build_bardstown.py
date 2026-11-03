"""Generate docs/bardstown/index.html (Bardstown and Kentucky Bourbon Country)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='bardstown', name='Bardstown & Bourbon Country', state='Kentucky', number=44, reviewed='November 3, 2026',
    airport='KBRY', nm=405, flight_time='~2 hr 57 <small>min</small>', style='Courtesy car + a driver',
    place='Bardstown & Bourbon Country, Kentucky',
    description='A curated two-night Bardstown getaway for GA pilots and their partners, from KMYR to KBRY. The Bourbon Capital of the World: distillery tours, a 1779 tavern, Maker’s Mark and My Old Kentucky Home.',
    lede='The Bourbon Capital of the World.',
    intro='Bardstown is the heart of Kentucky bourbon country, with more than a dozen distilleries within a short drive and a historic downtown of brick buildings around the courthouse square. Tour the rickhouses, taste at Heaven Hill and Willett, visit Maker’s Mark in its pretty hollow, and dine in a tavern that has served travelers since 1779.',
    pills=['Bourbon distilleries', 'Historic downtown', 'Kentucky hospitality'],
    flight=dict(
        title='Land five minutes from the square.',
        intro='KBRY, Samuels Field, is a small non-towered airport just outside Bardstown, about five minutes from downtown.',
        fbo=('Samuels Field Aviation', '1924 Boston Road, Bardstown, KY 40004', '502-348-7858'),
        notes=['Directories list hours of 8 a.m. to 5 p.m. Monday to Saturday, unattended on Sunday, and a courtesy car. Confirm the car, parking and fees ahead. No live fuel price is shown.',
               'Bourbon and flying: FAA rules require at least 8 hours from “bottle to throttle” and a blood alcohol level under 0.04%, and many pilots set 12 to 24 hours as a personal minimum. Taste on the non-flying day, and hire a driver or a bourbon tour company; don’t drive between distilleries after tasting.'],
        around_title='Hire a driver for tasting days.',
        around='Downtown Bardstown is walkable. Local tour companies and drivers run distillery days, the safest way to taste.'),
    stay=dict(title='On the square or among the bourbon.', intro='Rates and availability need travel dates; fall weekends fill early.',
        cards=[('Courthouse square · Historic', 'Talbott Tavern & Inn', 'Rooms in a 1913 building beside the Old Talbott Tavern, a stagecoach stop since 1779, right on the square.', 'https://talbotttavern.com/talbott-inn/'),
               ('Countryside · Bourbon-themed', 'Bourbon Manor Bed & Breakfast', 'A restored 1820s mansion with bourbon-themed rooms, a short walk from downtown.', 'https://bourbonmanor.com/'),
               ('Distillery · Stay & dine', 'The Bardstown Bourbon Company', 'A modern distillery with Bottle & Bond Kitchen and Bar and tours, minutes from town.', 'https://www.bardstownbourbon.com/')]),
    eat=dict(title='Two dinners. One distillery lunch.', intro='Reserve weekend dinners.',
        cards=[('Friday dinner · Since 1779', 'Old Talbott Tavern', 'Kentucky classics and a long bourbon list in one of America’s oldest western stagecoach stops.', 'https://talbotttavern.com/'),
               ('Saturday dinner · Distillery', 'Bottle & Bond Kitchen and Bar', 'Seasonal Kentucky cooking and hundreds of bourbons at the Bardstown Bourbon Company.', 'https://www.bardstownbourbon.com/'),
               ('Lunch · My Old Kentucky Home', 'Downtown Bardstown', 'Cafés and lunch spots around the courthouse square, an easy walk from the Getz Museum.')]),
    explore=dict(title='Rickhouses, hollows and history.', intro='Two distilleries a day is plenty.',
        items=[('Heaven Hill Bourbon Experience', 'Tours and tastings at one of the largest family-owned distilleries, just outside town.', 'https://heavenhilldistillery.com/', 'Tours'),
               ('Willett Distillery', 'A family distillery on a hill above Bardstown, with a striking pot still and a lovely setting.', 'https://www.kentuckybourbonwhiskey.com/', 'Tours'),
               ('Maker’s Mark', 'Dip your own bottle in red wax at the distillery’s beautiful campus in Loretto, about 25 minutes away.', 'https://www.makersmark.com/', 'Tours'),
               ('My Old Kentucky Home State Park', 'The 1818 mansion that inspired Stephen Foster’s song, with guided tours in costume.', 'https://parks.ky.gov/explore/my-old-kentucky-home-state-park-7821', 'Park information'),
               ('Oscar Getz Museum of Whiskey History', 'A free museum of bourbon’s colorful past, downtown.', 'https://getzmuseum.com/', 'Museum information')]),
    events=dict(url='https://www.visitbardstown.com/', button='Browse Bardstown events',
        cards=[('September', 'Kentucky Bourbon Festival', 'Bardstown’s big bourbon celebration. Lodging fills a year ahead.'),
               ('October', 'Fall color', 'Beautiful drives between distilleries.'),
               ('Spring', 'Derby season', 'The Kentucky Derby in Louisville, about 45 minutes away, is the first Saturday in May.')]),
    itinerary=dict(intro='A sample Friday–Sunday weekend: distilleries with a driver, the square and two Kentucky dinners. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & the square', [('Arrival', 'Land at KBRY, subject to weather and your actual flight plan.'), ('Afternoon', 'Check in, the Getz Museum and the square.'), ('Evening', 'Dinner at the Old Talbott Tavern.')]),
              ('SAT', 'Bourbon day', [('Morning', 'With a driver: Heaven Hill, then Maker’s Mark.'), ('Afternoon', 'Willett, then a rest.'), ('Evening', 'Dinner at Bottle & Bond.')]),
              ('SUN', 'An easy departure', [('Morning', 'My Old Kentucky Home and a slow breakfast.'), ('Before leaving', 'Mind your bottle-to-throttle time; the FBO is unattended on Sundays.'), ('Fly home', 'Let weather and your flight plan set the departure.')])]),
    know=[('Book in this order', 'Lodging, a driver and distillery tours first, then dinners.'),
          ('Bottle to throttle', 'At least 8 hours and under 0.04% by rule; many pilots use 12 to 24 hours.'),
          ('Sunday', 'The FBO is listed as unattended on Sundays; arrange fuel and the car ahead.'),
          ('Festival weekend', 'The Bourbon Festival in September fills the town.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
