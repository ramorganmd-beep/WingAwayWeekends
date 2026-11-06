"""Generate docs/louisville/index.html."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='louisville', name='Louisville', state='Kentucky', number=91, reviewed='November 4, 2026',
    airport='KLOU', nm=426, flight_time='~3 hr 05 <small>min</small>', style='Rental car or rideshare',
    place='Louisville, Kentucky',
    description='A curated Louisville getaway for GA pilots and their partners, from KMYR to KLOU. Churchill Downs and the Kentucky Derby Museum, bourbon on Whiskey Row, the Hot Brown at the Brown Hotel and the Muhammad Ali Center.',
    lede='Churchill Downs, Whiskey Row and the Hot Brown.',
    intro='Louisville is home to the Kentucky Derby and the heart of bourbon country. Tour Churchill Downs at the Kentucky Derby Museum, sample on Whiskey Row, eat a Hot Brown where it was invented at the Brown Hotel, swing a bat at the Louisville Slugger Museum, visit the Muhammad Ali Center and walk the Big Four Bridge across the Ohio.',
    pills=['Derby & racing', 'Bourbon', 'Historic hotels'],
    flight=dict(
        title='Land at Bowman Field.',
        intro='KLOU, Bowman Field, is a towered GA airport, one of the oldest in the country, about 15 minutes from downtown.',
        fbo=('Louisville Executive Aviation', 'Bowman Field, Louisville, KY', '502-292-4800'),
        notes=['Confirm FBO hours, fees and cars. No live fuel price is shown.',
               'Bowman sits under the Louisville Class C. Derby week brings very heavy traffic and special procedures. About 425 nm from Myrtle Beach.'],
        around_title='Rideshare downtown.',
        around='Downtown and Whiskey Row are walkable; use a car for Churchill Downs and the Highlands.'),
    stay=dict(title='Grand old hotels and an art hotel.', intro='Rates and availability need travel dates. Derby week is booked a year ahead.',
        cards=[('Downtown · Since 1923', 'The Brown Hotel', 'The grand hotel where the Hot Brown was born.', 'https://www.brownhotel.com/'),
               ('Downtown · Since 1905', 'The Seelbach Hilton', 'A Gilded Age landmark that appears in The Great Gatsby.', 'https://seelbachhilton.com/'),
               ('Whiskey Row · Art hotel', '21c Museum Hotel Louisville', 'Contemporary art and Proof on Main.', 'https://www.21cmuseumhotels.com/louisville/')]),
    eat=dict(title='Hot Browns and bourbon.', intro='Reserve weekend dinners.',
        cards=[('Friday dinner · Art hotel', 'Proof on Main', 'Seasonal cooking and a deep bourbon list at 21c.', 'https://www.proofonmain.com/'),
               ('Saturday dinner · Since 1933', 'Jack Fry’s', 'A classic bistro on Bardstown Road.', 'https://www.jackfrys.com/'),
               ('Dinner · Local', 'The Mayan Cafe', 'Local, seasonal Mayan cooking in NuLu.', 'https://themayancafe.com/'),
               ('Lunch · Classic', 'The Hot Brown at the Brown Hotel', 'Try the original open-faced turkey sandwich.', 'https://www.brownhotel.com/')]),
    explore=dict(title='The Derby, bats and bourbon.', intro='Mix museums with Whiskey Row.',
        items=[('Kentucky Derby Museum & Churchill Downs', 'Museum exhibits and track tours.', 'https://www.derbymuseum.org/', 'Museum'),
               ('Louisville Slugger Museum & Factory', 'See bats being made.', 'https://www.sluggermuseum.com/', 'Museum'),
               ('Muhammad Ali Center', 'The champion’s life and values.', 'https://www.alicenter.org/', 'Ali Center'),
               ('Whiskey Row & the Urban Bourbon Trail', 'Distillery experiences and bourbon bars downtown.', 'https://www.gotolouisville.com/', 'Bourbon trail'),
               ('Big Four Bridge', 'A pedestrian bridge over the Ohio, lit at night.', 'https://ourwaterfront.org/', 'Waterfront Park')]),
    events=dict(url='https://www.gotolouisville.com/', button='Browse Louisville events',
        cards=[('First Saturday in May', 'Kentucky Derby', 'The biggest weekend of the year; book far ahead or avoid.', 'https://www.kentuckyderby.com/', 'Derby'),
               ('Spring & fall', 'Racing at Churchill Downs', 'Spring and fall meets.', 'https://www.churchilldowns.com/', 'Churchill Downs'),
               ('Spring & fall', 'Best seasons', 'Summers are hot and humid.')]),
    itinerary=dict(intro='A sample weekend: the Derby, bourbon and a Hot Brown. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & Whiskey Row', [('Arrival', 'Land at KLOU, subject to weather and your actual flight plan.'), ('Afternoon', 'Whiskey Row and the Slugger Museum.'), ('Evening', 'Dinner at Proof on Main.')]),
              ('DAY 2', 'Derby & Ali', [('Morning', 'The Derby Museum and track tour.'), ('Afternoon', 'The Muhammad Ali Center and the Big Four Bridge.'), ('Evening', 'Dinner at Jack Fry’s.')]),
              ('DAY 3', 'Hot Brown & home', [('Morning', 'A Hot Brown at the Brown Hotel.'), ('Before leaving', 'Allow time at the FBO.'), ('Fly home', 'Summer storms build in the afternoon; leave early.')])]),
    know=[('Book in this order', 'Lodging first, then dinners and distillery tours.'),
          ('Derby week', 'Expect special air traffic procedures and huge crowds.'),
          ('Bourbon', 'Plan rideshares.'),
          ('Best seasons', 'Spring and fall.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
