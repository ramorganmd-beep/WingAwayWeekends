"""Generate docs/golden-isles/index.html (Golden Isles, Georgia)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='golden-isles', name='Golden Isles', state='Georgia', number=79, reviewed=None,
    airport='KSSI', nm=196, flight_time='~1 hr 33 <small>min</small>', style='Rental car or bikes',
    place='St. Simons Island, Georgia',
    description='A curated Golden Isles getaway for GA pilots and their partners, from KMYR to KSSI. St. Simons, Sea Island and Jekyll Island: a historic lighthouse, Driftwood Beach, the Jekyll Island Club and live-oak marshes.',
    lede='Live oaks, marshes and three barrier islands.',
    intro='Georgia’s Golden Isles are a quieter, older-feeling coast, with live oaks draped in Spanish moss and wide salt marshes. Land right on St. Simons Island, bike to the 1872 lighthouse, walk Driftwood Beach on Jekyll Island, stay at the Gilded Age Jekyll Island Club or the Cloister at Sea Island and eat shrimp fresh from the boats.',
    pills=['Island airport', 'Historic resorts', 'Beaches & marshes'],
    flight=dict(
        title='Land on the island.',
        intro='KSSI, McKinnon St. Simons Island Airport, is a non-towered field on the island, a few minutes from the village, the pier and the lighthouse.',
        fbo=('Velocity FBO St. Simons Island', '115 Terminal Way, St. Simons Island, GA 31522', '912-638-8617'),
        notes=['The FBO lists daily hours of 6 a.m. to 9 p.m. Confirm fees, cars and parking. No live fuel price is shown.',
               'A short flight of about 200 nm. Summer brings afternoon storms, and hurricane season runs June to November.'],
        around_title='Bikes and a car.',
        around='St. Simons is great by bike; a car covers Jekyll Island and Sea Island.'),
    stay=dict(title='A Gilded Age club or an island classic.', intro='Rates and availability need travel dates.',
        cards=[('Jekyll Island · Historic', 'Jekyll Island Club Resort', 'The 1887 winter retreat of America’s richest families, now a resort.', 'https://www.jekyllclub.com/'),
               ('Sea Island · Luxury', 'The Cloister at Sea Island', 'A Forbes Five-Star resort with a spa, golf and a private beach.', 'https://www.seaisland.com/'),
               ('St. Simons · Oceanfront', 'The King and Prince', 'A 1935 beachfront resort on St. Simons.', 'https://www.kingandprince.com/')]),
    eat=dict(title='Shrimp, barbecue and island dinners.', intro='Reserve weekend dinners.',
        cards=[('Saturday dinner · Fine dining', 'Halyards', 'A long-time St. Simons favorite for seafood and steaks.', 'https://halyardsrestaurant.com/'),
               ('Friday dinner · Seafood', 'Georgia Sea Grill', 'Fresh local seafood in the village.', 'https://www.georgiaseagrill.com/'),
               ('Lunch · Barbecue', 'Southern Soul Barbeque', 'Celebrated barbecue in a converted gas station.', 'https://www.southernsoulbbq.com/')]),
    explore=dict(title='Lighthouses, oaks and Driftwood Beach.', intro='Easy days by bike and beach.',
        items=[('St. Simons Lighthouse Museum', 'Climb the 1872 lighthouse for island views.', 'https://www.coastalgeorgiahistory.org/', 'Lighthouse'),
               ('Driftwood Beach', 'Bleached trees on the sand at Jekyll Island, best at sunrise.'),
               ('Jekyll Island Historic District', 'Gilded Age “cottages” and tours by tram.', 'https://www.jekyllisland.com/', 'Jekyll Island'),
               ('Georgia Sea Turtle Center', 'A sea turtle hospital you can visit.', 'https://gstc.jekyllisland.com/', 'Turtle Center'),
               ('Fort Frederica National Monument', 'Ruins of a 1736 British colonial town.', 'https://www.nps.gov/fofr/', 'Fort Frederica')]),
    spa=dict(title='The spa at Sea Island', body='Sea Island’s spa offers couples treatments near the beach.'),
    events=dict(url='https://www.goldenisles.com/', button='Browse Golden Isles events',
        cards=[('Spring & fall', 'Best seasons', 'Warm days, cool evenings and fewer crowds.'),
               ('May–October', 'Sea turtle season', 'Turtles nest on the beaches; follow lighting rules.'),
               ('November', 'RSM Classic', 'A PGA Tour event at Sea Island.')]),
    itinerary=dict(intro='A sample weekend: bikes, beaches and a Gilded Age club. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & the village', [('Arrival', 'Land at KSSI, subject to weather and your actual flight plan.'), ('Afternoon', 'Bike to the pier and lighthouse.'), ('Evening', 'Dinner at Georgia Sea Grill.')]),
              ('DAY 2', 'Jekyll Island', [('Morning', 'Driftwood Beach at sunrise.'), ('Afternoon', 'The historic district and the Turtle Center.'), ('Evening', 'Dinner at Halyards.')]),
              ('DAY 3', 'History & home', [('Morning', 'Fort Frederica.'), ('Before leaving', 'Barbecue at Southern Soul.'), ('Fly home', 'A short flight; leave before afternoon storms.')])]),
    know=[('Book in this order', 'Lodging first, then dinners.'),
          ('Getting around', 'Rent bikes on St. Simons; a car for Jekyll.'),
          ('Jekyll Island', 'A daily parking fee applies to cars entering the island.'),
          ('Hurricane season', 'June through November. Keep plans flexible.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
