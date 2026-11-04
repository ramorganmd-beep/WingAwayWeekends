"""Generate docs/oxford/index.html (Oxford, Mississippi)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='oxford', name='Oxford', state='Mississippi', number=70, reviewed=None,
    airport='KUOX', nm=529, flight_time='~3 hr 46 <small>min</small>', style='Rental car or rideshare',
    place='Oxford, Mississippi',
    description='A curated Oxford getaway for GA pilots and their partners, from KMYR to KUOX. A literary college town: the Square, Faulkner’s Rowan Oak, Square Books and some of the South’s best restaurants.',
    lede='Faulkner, a famous bookstore and a celebrated food scene.',
    intro='Oxford is a small college town with an outsized literary and food reputation. Browse Square Books, walk the shaded trail to William Faulkner’s home at Rowan Oak, catch the Thacker Mountain Radio Hour and dine at City Grocery, where chef John Currence helped put Oxford on the culinary map.',
    pills=['Literary town', 'Celebrated dining', 'The Square'],
    flight=dict(
        title='Land at the university airport.',
        intro='KUOX, University–Oxford Airport, is owned by the University of Mississippi and sits a few minutes from the Square.',
        fbo=('General Aviation Services', 'University–Oxford Airport, Oxford, MS', '662-234-2036'),
        notes=['Confirm FBO hours, overnight parking and ground transportation before you go. No live fuel price is shown.',
               'Ole Miss home football weekends bring heavy traffic and booked-out hotels; check the schedule. About 530 nm from Myrtle Beach: plan a fuel stop or a long nonstop leg.'],
        around_title='Walk the Square.',
        around='Stay near the Square and walk to dinner; a rental car or rideshare covers the airport and Rowan Oak.'),
    stay=dict(title='Stay near the Square.', intro='Rates and availability need travel dates. Avoid home football and graduation weekends unless that is the point.',
        cards=[('Campus · Classic', 'The Inn at Ole Miss', 'The university’s hotel, beside the Grove.', 'https://theinnatolemiss.com/'),
               ('Near the Square · Boutique', 'Graduate Oxford', 'A playful, literary-themed hotel with a rooftop bar.', 'https://www.hilton.com/en/hotels/tupgogu-graduate-oxford/'),
               ('On the Square · Boutique', 'The Oliver Hotel', 'A boutique hotel just off the Square, formerly the Chancellor’s House, with a rooftop bar.', 'https://theoliverhotel.com/oxford/')]),
    eat=dict(title='A small town that eats very well.', intro='Reserve weekend dinners.',
        cards=[('Friday dinner · On the Square', 'City Grocery', 'Chef John Currence’s flagship, with a lively upstairs bar.', 'https://www.citygroceryonline.com/'),
               ('Saturday dinner · Oysters', 'Snackbar', 'A North Mississippi brasserie with an oyster bar.', 'https://snackbaroxford.com/'),
               ('Dinner · Italian', 'Saint Leo', 'Wood-fired pizza and handmade pasta.', 'https://eatsaintleo.com/'),
               ('Dinner · Fine dining', 'Lenora’s', 'Modern Southern cooking in a restored house.', 'https://www.lenorasrestaurant.com/')]),
    explore=dict(title='Books, Faulkner and the Grove.', intro='A slow weekend of walking, reading and eating.',
        items=[('Rowan Oak', 'William Faulkner’s home, with his plot outline for A Fable written on the study wall.', 'https://www.rowanoak.com/', 'Rowan Oak'),
               ('Square Books', 'A celebrated independent bookstore with a balcony over the Square.', 'https://squarebooks.com/', 'Square Books'),
               ('Bailey’s Woods Trail', 'A short wooded path between the University Museum and Rowan Oak.', 'https://www.rowanoak.com/about/bailey-woods-trail/', 'Trail'),
               ('University of Mississippi Museum', 'Art and antiquities collections near campus.', 'https://museum.olemiss.edu/', 'Museum'),
               ('Thacker Mountain Radio Hour', 'A live radio show of music and authors, usually on Thursday evenings during the school year.', 'https://www.thackermountain.com/', 'Schedule')]),
    events=dict(url='https://visitoxfordms.com/', button='Browse Oxford events',
        cards=[('Late April', 'Double Decker Arts Festival', 'Music, art and food around the Square.', 'https://doubledeckerfestival.com/', 'Festival'),
               ('Fall', 'Football Saturdays', 'Tailgating in the Grove is a tradition; book far ahead or choose another weekend.', 'https://olemisssports.com/sports/football/schedule', 'Schedule'),
               ('Spring', 'Oxford Conference for the Book', 'Readings and talks with authors.', 'https://oxfordconferenceforthebook.com/', 'Conference')]),
    itinerary=dict(intro='A sample weekend: books, Faulkner and dinner. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & the Square', [('Arrival', 'Land at KUOX, subject to weather and your actual flight plan.'), ('Afternoon', 'Square Books and a walk around the Square.'), ('Evening', 'Dinner at City Grocery.')]),
              ('DAY 2', 'Faulkner & the Grove', [('Morning', 'The University Museum, then Bailey’s Woods to Rowan Oak.'), ('Afternoon', 'Walk the campus and the Grove.'), ('Evening', 'Oysters at Snackbar.')]),
              ('DAY 3', 'Brunch & home', [('Morning', 'A slow brunch near the Square.'), ('Before leaving', 'Allow time at the FBO.'), ('Fly home', 'Summer storms build in the afternoon; leave early.')])]),
    know=[('Book in this order', 'Lodging first, then dinners.'),
          ('Check the calendar', 'Football, graduation and big festival weekends fill every hotel.'),
          ('Long flight', 'About 530 nm. Plan a fuel stop or a long nonstop leg.'),
          ('Best seasons', 'Spring and fall.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
