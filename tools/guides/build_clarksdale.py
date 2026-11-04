"""Generate docs/clarksdale/index.html (Clarksdale, Mississippi)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='clarksdale', name='Clarksdale', state='Mississippi', number=80, reviewed='November 4, 2026',
    airport='KCKM', nm=578, flight_time='~4 hr 06 <small>min</small>', style='Arranged car',
    place='Clarksdale, Mississippi',
    description='A curated Clarksdale getaway for GA pilots and their partners, from KMYR to KCKM. The heart of the Mississippi Delta blues: juke joints, the Delta Blues Museum, the Crossroads, the Shack Up Inn and hot tamales.',
    lede='Juke joints and the Delta blues, where it all began.',
    intro='Clarksdale is a small Delta town with live blues almost every night. Sleep in a sharecropper shack at the Shack Up Inn, hear local players at Ground Zero Blues Club and Red’s Lounge, see Muddy Waters’s cabin at the Delta Blues Museum, browse folk art at Cat Head and stand at the legendary Crossroads.',
    pills=['Live blues', 'Quirky stays', 'Delta history'],
    flight=dict(
        title='Land in the Delta.',
        intro='KCKM, Fletcher Field, is a small non-towered airport a few minutes from downtown Clarksdale.',
        fbo=('Red Panther Aero', 'Fletcher Field, Clarksdale, MS', '662-624-5554'),
        notes=['Fuel is self-service. Confirm hours, parking and how you will get into town before you go. No live fuel price is shown.',
               'The Delta is flat and open; watch for agricultural aircraft and summer storms. About 580 nm from Myrtle Beach: plan a fuel stop.'],
        around_title='Arrange a ride.',
        around='Downtown is walkable, but you will need a ride from the airport and to the Shack Up Inn. Ask your lodging before you go.'),
    stay=dict(title='A shack, a hotel or a loft.', intro='Rates and availability need travel dates. Festival weekends sell out.',
        cards=[('Hopson Plantation · Quirky', 'Shack Up Inn', 'Restored sharecropper shacks and a cotton gin turned into rooms.', 'https://www.shackupinn.com/'),
               ('Downtown · Boutique', 'The Travelers Hotel', 'A small, artist-designed hotel downtown.', 'https://www.stayattravelers.com/'),
               ('Local guide', 'More places to stay', 'Lofts and guest houses above downtown clubs.', 'https://www.visitclarksdale.com/', 'Visit Clarksdale')]),
    eat=dict(title='Tamales, barbecue and the blues.', intro='Hours are short and change; check before you go.',
        cards=[('Dinner · Live blues', 'Ground Zero Blues Club', 'Southern food and live music, co-owned by Morgan Freeman.', 'https://www.groundzerobluesclub.com/'),
               ('Lunch · Since 1924', 'Abe’s Bar-B-Q', 'A barbecue stand at the Crossroads.', 'https://www.abesbbq.com/'),
               ('Lunch · Delta classic', 'Hicks Famous Hot Tamales', 'Delta hot tamales, a local tradition.', 'https://www.visitclarksdale.com/dining-guide')]),
    explore=dict(title='Blues history and juke joints.', intro='Days for history, nights for music.',
        items=[('Delta Blues Museum', 'The state’s oldest music museum, with Muddy Waters’s cabin.', 'https://www.deltabluesmuseum.org/', 'Museum'),
               ('Cat Head Delta Blues & Folk Art', 'A shop for records, folk art and what’s playing tonight.', 'https://www.catheadblues.com/', 'Cat Head'),
               ('Red’s Lounge', 'A classic juke joint; check who’s playing.', 'https://www.catheadblues.com/', 'Who’s playing'),
               ('The Crossroads', 'Highways 61 and 49, tied to the Robert Johnson legend.', 'https://www.visitclarksdale.com/', 'Visit Clarksdale'),
               ('Mississippi Blues Trail', 'Historic markers around town and across the Delta.', 'https://msbluestrail.org/', 'Blues Trail')]),
    events=dict(url='https://www.visitclarksdale.com/', button='Browse Clarksdale events',
        cards=[('April', 'Juke Joint Festival', 'Blues across downtown, the town’s biggest weekend.', 'https://www.jukejointfestival.com/', 'Festival'),
               ('August', 'Sunflower River Blues & Gospel Festival', 'A free downtown blues festival.', 'https://www.sunflowerfest.org/', 'Festival'),
               ('Weekends', 'Live music', 'Several clubs have music Thursday through Saturday.', 'https://www.catheadblues.com/', 'Cat Head')]),
    itinerary=dict(intro='A sample long weekend: museums by day, blues by night. Plan three nights for the flight. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & first set', [('Arrival', 'Land at KCKM, subject to weather, your fuel stop and your actual flight plan.'), ('Afternoon', 'Check in at the Shack Up Inn.'), ('Evening', 'Dinner and music at Ground Zero.')]),
              ('DAY 2', 'Blues history', [('Morning', 'The Delta Blues Museum.'), ('Afternoon', 'Cat Head, tamales and the Crossroads.'), ('Evening', 'Red’s Lounge.')]),
              ('DAY 3', 'Barbecue & home', [('Morning', 'Lunch at Abe’s.'), ('Before leaving', 'Allow time at the airport.'), ('Fly home', 'Summer storms build in the afternoon; leave early.')])]),
    know=[('Book in this order', 'Lodging first, then your ride from the airport.'),
          ('Music schedule', 'Check Cat Head or the clubs for who’s playing.'),
          ('Long flight', 'About 580 nm. Plan a fuel stop and extra nights.'),
          ('Best seasons', 'Spring and fall; summers are hot.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
