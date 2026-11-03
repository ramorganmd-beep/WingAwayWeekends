"""Generate docs/dayton/index.html (Dayton, Ohio - Birthplace of Aviation)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='dayton', name='Dayton', state='Ohio', number=45, reviewed='November 3, 2026',
    airport='KMGY', nm=437, flight_time='~3 hr 10 <small>min</small>', style='Rental car',
    place='Dayton, Ohio',
    description='A curated two-night Dayton getaway for GA pilots and their partners, from KMYR to KMGY. The National Museum of the U.S. Air Force, the Wright brothers’ workshops and flying field, and Yellow Springs.',
    lede='The birthplace of aviation.',
    intro='Dayton is where Wilbur and Orville Wright built their airplanes and learned to fly them. Spend a day in the four enormous hangars of the National Museum of the U.S. Air Force, stand on the field where the Wrights perfected practical flight, see the original 1905 Wright Flyer III, and spend an afternoon in artsy Yellow Springs.',
    pills=['Air Force Museum', 'Wright brothers', 'Small-town afternoons'],
    flight=dict(
        title='Land at the airport named for the Wrights.',
        intro='KMGY, Dayton–Wright Brothers Airport, is a towered field south of the city, about 25 minutes from downtown and 30 from the Air Force museum.',
        fbo=('First Flight Aviation', '10600 Springboro Pike, Miamisburg, OH 45342', '937-885-5580'),
        notes=['Directories list hours of 7 a.m. to 8 p.m. daily. Ask about rental cars, parking and fees. No live fuel price is shown.',
               'Dayton International’s Class C airspace lies to the north, and Wright-Patterson Air Force Base has restricted airspace to the east. Review the sectional and current NOTAMs.'],
        around_title='You’ll need a car.',
        around='The museums, downtown and Yellow Springs are spread around the Miami Valley.'),
    stay=dict(title='Downtown or in Yellow Springs.', intro='Rates and availability need travel dates.',
        cards=[('Downtown · Water Street', 'AC Hotel Dayton', 'A modern hotel in the riverside Water Street District, a walk from restaurants and the ballpark.', 'https://www.marriott.com/en-us/hotels/dayac-ac-hotel-dayton/overview/'),
               ('Yellow Springs · Boutique', 'Mills Park Hotel', 'A small, stylish hotel in the arts village of Yellow Springs, about 30 minutes east.', 'https://www.millsparkhotel.com/'),
               ('Explore more', 'Destination Dayton', 'More hotels near the museum and downtown from the area visitor bureau.', 'https://www.destinationdayton.org/')]),
    eat=dict(title='Two dinners. One ice-cream stop.', intro='Reserve weekend dinners.',
        cards=[('Friday dinner · Oregon District', 'Lily’s Bistro', 'Seasonal cooking in the historic Oregon District.', 'https://www.lilysdayton.com/'),
               ('Saturday dinner · Peruvian', 'Salar', 'Peruvian-inspired cooking and pisco cocktails in the Oregon District.', 'https://salarrestaurant.com/'),
               ('Afternoon · Farm', 'Young’s Jersey Dairy', 'A farm dairy near Yellow Springs famous for homemade ice cream.', 'https://youngsdairy.com/')]),
    explore=dict(title='Where flight began.', intro='Plan a full day for the Air Force museum.',
        items=[('National Museum of the U.S. Air Force', 'The world’s largest military aviation museum: more than 350 aircraft in four huge hangars, including presidential aircraft. Free; check current visitor entry rules.',
            'https://www.nationalmuseum.af.mil/', 'Museum information'),
               ('Dayton Aviation Heritage National Historical Park', 'The Wright Cycle Company shop and the Wright-Dunbar Interpretive Center.', 'https://www.nps.gov/daav/', 'Park information'),
               ('Huffman Prairie Flying Field', 'The pasture where the Wrights learned to fly in 1904–05, part of the national park.'),
               ('Carillon Historical Park', 'See the original 1905 Wright Flyer III, which Orville called the first practical airplane.', 'https://daytonhistory.org/', 'Visit information'),
               ('Yellow Springs & Glen Helen', 'An artsy village and a nature preserve with trails and a waterfall.', 'https://glenhelen.org/', 'Glen Helen')]),
    events=dict(url='https://www.destinationdayton.org/', button='Browse Dayton events',
        cards=[('Summer', 'Dayton Air Show', 'One of the country’s big air shows, usually in June or July. Expect TFRs and busy airspace.'),
               ('August', 'Wright Brothers’ birthday season', 'Orville’s birthday, August 19, is National Aviation Day.'),
               ('Fall', 'Color in the Miami Valley', 'Quiet trails and fall foliage around Yellow Springs.')]),
    itinerary=dict(intro='A sample Friday–Sunday weekend: the Air Force museum, the Wrights’ Dayton and two good dinners. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & the Wrights', [('Arrival', 'Land at KMGY, subject to weather and your actual flight plan, and pick up the car.'), ('Afternoon', 'Carillon Historical Park and the Wright Flyer III.'), ('Evening', 'Dinner at Lily’s Bistro.')]),
              ('SAT', 'The Air Force museum', [('All day', 'The National Museum of the U.S. Air Force. Start early.'), ('Late afternoon', 'Huffman Prairie Flying Field.'), ('Evening', 'Dinner at Salar.')]),
              ('SUN', 'Yellow Springs & home', [('Morning', 'Glen Helen and the village, then ice cream at Young’s.'), ('Before leaving', 'Return the car and allow time at the FBO.'), ('Fly home', 'Let weather and your flight plan set the departure.')])]),
    know=[('Book in this order', 'A car and lodging first, then dinners.'),
          ('Museum entry', 'The Air Force museum is on an active base; check current visitor requirements before you go.'),
          ('Airspace', 'Brief Dayton’s Class C and Wright-Patterson’s restricted areas.'),
          ('Air show weekend', 'The Dayton Air Show brings TFRs and crowds.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
