"""Generate docs/plymouth/index.html."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = {
    'slug': 'plymouth', 'name': 'Plymouth', 'state': 'Massachusetts', 'number': 301, 'reviewed': 'November 10, 2026',
    'researched': 'November 10, 2026',
    'airport': 'KPYM', 'nm': 628, 'flight_time': '~4 hr 27 <small>min</small>', 'style': 'Uber or rental car',
    'place': 'Plymouth, Massachusetts',
    'description': 'A curated Plymouth getaway for GA pilots and their partners, from KMYR to KPYM. America’s Hometown on the South Shore: the Mayflower II, Plymouth Rock, Plimoth Patuxet, a harbor full of seafood and a Forbes Four-Star spa.',
    'lede': 'America’s Hometown: the Mayflower II, the harbor and a spa in the pines.',
    'intro': 'Plymouth sits on Cape Cod Bay between Boston and the Cape, where the Pilgrims landed in 1620. Walk the waterfront from Plymouth Rock to the Mayflower II, spend a morning at Plimoth Patuxet, eat seafood on the harbor and finish at a spa resort in The Pinehills.',
    'pills': ['History', 'Harbor & seafood', 'Spa resort'],
    'flight': {
        'title': 'Land in Plymouth.',
        'intro': 'KPYM, Plymouth Municipal Airport, is a non-towered field with two paved runways (06/24, 4,650 ft, and 15/33, 4,350 ft), about 5 miles from the waterfront. Plane Jane’s Place, a breakfast-and-lunch diner, is on the field.',
        'fbo': ['Plymouth Municipal Airport', '246 South Meadow Road, Plymouth, MA · 100LL and Jet A', '508-746-2020', 'https://www.pymairport.com/'],
        'notes': ['Confirm FBO hours, fees and ground transportation. No live fuel price is shown.',
                  'Watch for coastal fog and low ceilings off Cape Cod Bay. About 630 nm from Myrtle Beach: plan a fuel stop and two or three nights.'],
        'around_title': 'Uber or a rental car.',
        'around': 'Downtown and the waterfront are walkable; take an Uber or a rental car from the airport and to Plimoth Patuxet or The Pinehills.',
    },
    'stay': {
        'title': 'On the harbor, downtown or a spa in the pines.',
        'intro': 'Rates and availability need travel dates. Thanksgiving weekend and summer book early.',
        'cards': [
            ('The Pinehills · Spa resort', 'Mirbeau Inn & Spa Plymouth', 'A Forbes Four-Star spa resort on the Village Green in The Pinehills, a short drive from downtown.', 'https://www.plymouth.mirbeau.com/'),
            ('Waterfront · Hotel', 'Hotel 1620 Plymouth Harbor', 'Across from Plymouth Harbor, with an indoor pool and a walk to the waterfront.', 'https://www.hotel1620.com/'),
            ('Downtown · Inn & spa', 'John Carver Inn & Spa', 'A downtown inn with a spa and an indoor pool, steps from Plymouth Rock and the Mayflower II.', 'https://www.johncarverinn.com/'),
        ],
    },
    'eat': {
        'title': 'Seafood on the harbor, breakfast on the field.',
        'intro': 'Reserve weekend dinners on the waterfront.',
        'cards': [
            ('Friday dinner · Waterfront', 'East Bay Grille', 'Seafood, steaks and a raw bar on the Plymouth waterfront.', 'https://www.eastbaygrille.com/'),
            ('Saturday dinner · On the wharf', 'Tavern on the Wharf', 'A harbor-side restaurant and bar with views of the water.', 'https://www.tavernonthewharf.com/'),
            ('Breakfast or lunch · On the field', 'Plane Jane’s Place', 'A diner at the airport since 1996, open early for breakfast and lunch. Reported cash only.'),
        ],
    },
    'explore': {
        'title': 'The Pilgrim story, the harbor and the bay.',
        'intro': 'History in the morning, the waterfront in the afternoon.',
        'items': [
            ('Plimoth Patuxet Museums', 'An open-air museum with the Historic Patuxet Homesite and a 17th-century English village, plus the Mayflower II on the waterfront.', 'https://plimoth.org/', 'Plimoth Patuxet'),
            ('Plymouth Rock & the waterfront', 'Plymouth Rock in Pilgrim Memorial State Park, the harbor walk and the town wharf.', 'https://seeplymouth.com/', 'See Plymouth'),
            ('Pilgrim Hall Museum', 'Pilgrim possessions, art and history on Court Street, with tours of Burial Hill.', 'https://www.pilgrimhall.org/', 'Pilgrim Hall'),
            ('Whale watching', 'Naturalist-guided whale watches from Plymouth in season (spring to fall).', 'https://www.captjohn.com/whale-watching/', 'Captain John Boats'),
            ('Mayflower Brewing', 'A local brewery with a taproom and tours.', 'https://www.mayflowerbrewing.com/', 'Mayflower Brewing'),
        ],
    },
    'events': {
        'url': 'https://seeplymouth.com/', 'button': 'Browse Plymouth events',
        'cards': [
            ('November 21, 2026', 'America’s Hometown Thanksgiving Celebration', 'A parade, concerts and waterfront events the weekend before Thanksgiving.', 'https://usathanksgiving.com/', 'USA Thanksgiving'),
            ('Spring to fall', 'Whale season', 'Whale watches run from the harbor in season.'),
            ('September & October', 'Best seasons', 'Mild weather, cranberry harvest season in the area and fewer crowds than summer.'),
        ],
    },
    'itinerary': {
        'intro': 'A sample weekend: the waterfront, Plimoth Patuxet and the spa. No bookings or availability confirmed.',
        'days': [
            ('DAY 1', 'Arrive & the waterfront', [
                ('Arrival', 'Land at KPYM, subject to weather, your fuel stop and your actual flight plan.'),
                ('Afternoon', 'Plymouth Rock, the Mayflower II and the harbor walk.'),
                ('Evening', 'Dinner at East Bay Grille.')]),
            ('DAY 2', 'Plimoth Patuxet & the harbor', [
                ('Morning', 'Plimoth Patuxet Museums.'),
                ('Afternoon', 'Pilgrim Hall Museum or a whale watch in season.'),
                ('Evening', 'Dinner at Tavern on the Wharf.')]),
            ('DAY 3', 'Spa & home', [
                ('Morning', 'The spa at Mirbeau, or breakfast at Plane Jane’s on the field.'),
                ('Before leaving', 'Allow time at the airport.'),
                ('Fly home', 'Watch for coastal fog.')]),
        ],
    },
    'know': [
        ('Book in this order', 'Lodging first, then Plimoth Patuxet tickets and dinner reservations.'),
        ('Two runways', 'Runways 06/24 (4,650 ft) and 15/33 (4,350 ft), both paved. Confirm fuel and parking.'),
        ('Long flight', 'About 630 nm from Myrtle Beach. Plan a fuel stop and extra nights.'),
        ('Best seasons', 'May to October, plus the Thanksgiving weekend celebration.'),
    ],
    'spa': {'title': 'The spa at Mirbeau', 'body': 'A full-service spa resort in The Pinehills, rated Forbes Four-Star every year since 2023.'},
}

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
