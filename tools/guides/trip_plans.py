"""Add trip-length plans (Day trip / Longer stay) to destination guides.

Usage: python3 tools/guides/trip_plans.py docs/*/index.html

Idempotent: removes any previously inserted plans and re-adds them. Marks the
route box's "Weekend style" value so docs/guide-route.js can relabel it, and
inserts two hidden plans into the itinerary section. guide-route.js shows the
one matching the visitor's trip length (?trip=... from the homepage cards, or
the last choice saved on the homepage). Run after building/personalizing a guide.
"""
import re
import sys
from pathlib import Path

PLANS = {
    'savannah': {
        'day': [('Arrive', 'Land at KSAV mid-morning and ride downtown.'),
                ('Midday', 'Walk Forsyth Park and a few squares, then lunch at The Collins Quarter or on River Street.'),
                ('Afternoon', 'Browse Broughton Street, then head back to the FBO for a late-afternoon departure.')],
        'extra': [('Morning', 'A private dolphin tour from Whitemarsh Island, or a sunrise walk along the river.'),
                  ('Afternoon', 'Starland District and a brewery stop at Two Tides or Hop Atomica.'),
                  ('Evening', 'Dinner at Vic’s on the River, or a sunset riverboat dinner cruise.')]},
    'charleston': {
        'day': [('Arrive', 'Land at KCHS mid-morning and ride to Patriots Point.'),
                ('Midday', 'Explore the USS Yorktown and its aircraft, then lunch downtown.'),
                ('Afternoon', 'A walk past Rainbow Row to the Battery, then back to the FBO.')],
        'extra': [('Morning', 'A slow morning on Lower King for antiques and galleries.'),
                  ('Afternoon', 'Fort Sumter by ferry from Liberty Square, then a brewery stop at Edmund’s Oast.'),
                  ('Evening', 'Dinner at Halls Chophouse.')]},
    'asheville': {
        'day': [('Arrive', 'Land at KAVL early and pick up a car.'),
                ('Midday', 'Biltmore House and gardens with a timed entry, plus lunch on the estate.'),
                ('Afternoon', 'Winery tasting for the non-pilot, then back to the airport before mountain afternoon weather builds.')],
        'extra': [('Morning', 'Drive the Blue Ridge Parkway for overlooks and a short walk, if open.'),
                  ('Afternoon', 'The Western North Carolina Air Museum in Hendersonville (open select days), or the River Arts District.'),
                  ('Evening', 'Sunset on the Grove Park Inn terrace and a relaxed dinner downtown.')]},
    'pinehurst': {
        'day': [('Arrive', 'Land at KSOP mid-morning and head to the village.'),
                ('Midday', 'Nine holes at The Cradle or a putting match at Thistle Dhu, then lunch at Pinehurst Brewing Co.'),
                ('Afternoon', 'A drink at The Deuce overlooking No. 2’s 18th green, then fly home.')],
        'extra': [('Morning', 'A second round at Mid Pines or Pine Needles, or a long spa morning.'),
                  ('Afternoon', 'Browse downtown Southern Pines and walk the Reservoir Park loop.'),
                  ('Evening', 'A brewery stop in Southern Pines or Aberdeen, then a quiet dinner in the village.')]},
    'beaufort': {
        'day': [('Arrive', 'Land at KARW mid-morning; borrow the courtesy car or arrange a ride across the river.'),
                ('Midday', 'Lunch on Bay Street, then a horse-drawn carriage tour of the historic district.'),
                ('Afternoon', 'The waterfront park swings, then back to the FBO well before it closes.')],
        'extra': [('Morning', 'The Spanish Moss Trail by bike or on foot.'),
                  ('Afternoon', 'The Parris Island Museum (check base access) or more beach time at Hunting Island.'),
                  ('Evening', 'A sunset boat outing from the downtown marina.')]},
    'st-augustine': {
        'day': [('Arrive', 'Land at KSGJ early and ride into the old city.'),
                ('Midday', 'Castillo de San Marcos, then lunch at The Columbia on St. George Street.'),
                ('Afternoon', 'A San Sebastian Winery tasting or a Flagler College tour, then fly home ahead of afternoon storms.')],
        'extra': [('Morning', 'Beach time on Anastasia Island or a quiet walk at Crescent Beach.'),
                  ('Afternoon', 'The St. Augustine Distillery tour and a wander through Lincolnville.'),
                  ('Evening', 'A sunset cruise on Matanzas Bay, then dinner at the Casa Monica.')]},
    'greenville': {
        'day': [('Arrive', 'Land at KGMU and ride ten minutes to Main Street.'),
                ('Midday', 'Falls Park and Liberty Bridge, then lunch on Main Street.'),
                ('Afternoon', 'A short bike ride on the Swamp Rabbit Trail, then back to the airport.')],
        'extra': [('Morning', 'Rent a car for a Blue Ridge drive: waterfalls, overlooks and small towns under an hour away.'),
                  ('Afternoon', 'Unity Park and The Commons food hall, or a Greenville Drive game in season.'),
                  ('Evening', 'A show at the Peace Center.')]},
    'charlottesville': {
        'day': [('Arrive', 'Land at KCHO early and pick up a car.'),
                ('Midday', 'Monticello with a timed entry, then lunch at a nearby winery.'),
                ('Afternoon', 'A stroll on the Downtown Mall, then back to the airport. Leave tastings to the passenger.')],
        'extra': [('Morning', 'Drive to Skyline Drive or the Blue Ridge Parkway for overlooks.'),
                  ('Afternoon', 'Barboursville Vineyards and its Jefferson-designed ruins, with lunch at the winery.'),
                  ('Evening', 'A relaxed dinner at your estate hotel.')]},
    'nashville': {
        'day': [('A long day', 'At about three hours each way from KMYR, Nashville is a stretch for a day trip; it works better from closer airports.'),
                ('Midday', 'Ryman Auditorium tour and lunch downtown.'),
                ('Afternoon', 'Country Music Hall of Fame, then back to KJWN with daylight to spare.')],
        'extra': [('Morning', 'Brunch and a wander through The Gulch or 12 South.'),
                  ('Afternoon', 'A tour of a historic home or a distillery outside town (you’ll want a car).'),
                  ('Evening', 'A quieter listening room for songwriters, then dinner at The Optimist.')]},
    'key-west': {
        'day': [('Not a day trip', 'At about four hours each way from KMYR, Key West is not a day trip from most of the Southeast.'),
                ('If you are closer', 'From south Florida airports: lunch at First Flight, then a bike loop through Old Town.'),
                ('Afternoon', 'Hemingway Home, then back to the FBO well before it closes.')],
        'extra': [('Morning', 'A snorkel or sail trip on the reef, or a lazy beach morning at Casa Marina.'),
                  ('Afternoon', 'Bike to the Southernmost Point and Fort Zachary Taylor’s beach.'),
                  ('Evening', 'A sunset sail, then a casual dinner in Old Town.')]},
    'outer-banks': {
        'day': [('Arrive', 'Land at KMQI mid-morning and take the courtesy car or a rental.'),
                ('Midday', 'Wright Brothers National Memorial, then lunch on the Manteo waterfront.'),
                ('Afternoon', 'A short climb at Jockey’s Ridge, then fly home before the afternoon winds build.')],
        'extra': [('Morning', 'Drive south through Cape Hatteras National Seashore toward the Cape Hatteras Lighthouse.'),
                  ('Afternoon', 'Beach time, or the North Carolina Aquarium on Roanoke Island.'),
                  ('Evening', 'In summer, The Lost Colony outdoor drama; otherwise a quiet dinner in Duck.')]},
    'amelia-island': {
        'day': [('Arrive', 'Land at KFHB mid-morning and borrow the crew car.'),
                ('Midday', 'Lunch downtown and a stroll up Centre Street to the harbor.'),
                ('Afternoon', 'Fort Clinch and a walk on the beach, then back to the FBO.')],
        'extra': [('Morning', 'A guided horseback ride on the beach.'),
                  ('Afternoon', 'A long spa afternoon at one of the oceanfront resorts.'),
                  ('Evening', 'A sunset river cruise, then dinner at Burlingame.')]},
    'yadkin-valley': {
        'day': [('Arrive', 'Land at KZEF mid-morning and pick up the courtesy car or a rental.'),
                ('Midday', 'Lunch and a tasting for the non-pilot at Elkin Creek Vineyard.'),
                ('Afternoon', 'A glass on the terrace at Raffaldini for the non-pilot, then back to the FBO before it closes.')],
        'extra': [('Morning', 'Hike to the overlooks at Pilot Mountain or Stone Mountain State Park.'),
                  ('Afternoon', 'Downtown Elkin, or a side trip to Mount Airy.'),
                  ('Evening', 'Live music at the Reeves Theater.')]},
    'hunt-country': {
        'day': [('Arrive', 'Land at KJYO (SFRA procedures) or KHWY mid-morning and pick up a car.'),
                ('Midday', 'The Udvar-Hazy Center: the Space Shuttle, the SR-71 and more.'),
                ('Afternoon', 'Lunch and a stroll in Middleburg, with a tasting for the non-pilot, then fly home.')],
        'extra': [('Morning', 'Historic Leesburg and Morven Park.'),
                  ('Afternoon', 'A couples spa afternoon at Salamander.'),
                  ('Evening', 'A splurge dinner at The Inn at Little Washington, with a driver.')]},
    'dahlonega': {
        'day': [('Arrive', 'Land at KGVL mid-morning and pick up the rental car.'),
                ('Midday', 'Lunch on the square and the Gold Museum.'),
                ('Afternoon', 'A tasting-room stop on the square for the non-pilot, then the drive back to the FBO.')],
        'extra': [('Morning', 'Amicalola Falls and its staircase trail.'),
                  ('Afternoon', 'A gold-mine tour and a little panning.'),
                  ('Evening', 'Sunset with a glass at Wolf Mountain, then dinner on the square.')]},
    'gulf-shores': {
        'day': [('Arrive', 'Land at KJKA mid-morning and borrow a crew car.'),
                ('Midday', 'Fried shrimp and gumbo at Doc’s Seafood Shack in Orange Beach.'),
                ('Afternoon', 'An hour on the beach at Gulf State Park, then fly home before the afternoon storms.')],
        'extra': [('Morning', 'A long morning at the National Naval Aviation Museum in Pensacola.'),
                  ('Afternoon', 'Fort Morgan and its quiet beaches.'),
                  ('Evening', 'Live music at the Flora-Bama or dinner at The Wharf.')]},
    'chattanooga': {
        'day': [('Arrive', 'Land at KCHA mid-morning and head downtown.'),
                ('Midday', 'The Incline Railway up Lookout Mountain and lunch at the top.'),
                ('Afternoon', 'A walk across the Walnut Street Bridge, then back to the FBO.')],
        'extra': [('Morning', 'The Tennessee Aquarium.'),
                  ('Afternoon', 'Ruby Falls, or a drive up Signal Mountain for the views.'),
                  ('Evening', 'The tasting menu at Calliope.')]},
    'smoky-mountains': {
        'day': [('Arrive', 'Land at KGKT early and pick up the rental car.'),
                ('Midday', 'A short waterfall walk at Laurel Falls and a picnic in the park.'),
                ('Afternoon', 'Browse the arts and crafts loop, then fly out before mountain afternoon weather.')],
        'extra': [('Morning', 'The Alum Cave trail, or Grotto Falls.'),
                  ('Afternoon', 'Dollywood, or a long lunch at Blackberry Farm.'),
                  ('Evening', 'Sunset from Newfound Gap, if the road is open.')]},
    'lake-lure': {
        'day': [('Arrive', 'Land at KFQD mid-morning and borrow the courtesy car or pick up a rental.'),
                ('Midday', 'Lunch by the lake at Rumbling Bald.'),
                ('Afternoon', 'A look out over the gorge at Chimney Rock, then back to the FBO before it closes.')],
        'extra': [('Morning', 'A longer hike at Rumbling Bald or Bat Cave.'),
                  ('Afternoon', 'A boat on the lake, or an afternoon at the beach.'),
                  ('Evening', 'Dinner at La Strada.')]},
    'lake-keowee': {
        'day': [('Arrive', 'Land at KCEU or KLQK mid-morning and pick up a car.'),
                ('Midday', 'Lunch at the Tiki Hut by Keowee Marina.'),
                ('Afternoon', 'A short pontoon cruise on Lake Keowee, then fly home.')],
        'extra': [('Morning', 'The summit trail at Table Rock State Park.'),
                  ('Afternoon', 'Kayaks on Lake Jocassee, or Whitewater Falls.'),
                  ('Evening', 'A second sunset at The Lighthouse.')]},
    'lake-lanier': {
        'day': [('Arrive', 'Land at KGVL mid-morning and pick up a rental car.'),
                ('Midday', 'A few hours on a rented pontoon.'),
                ('Afternoon', 'A late lunch on Gainesville’s square, then back to the FBO.')],
        'extra': [('Morning', 'A drive to Dahlonega and its Gold Museum.'),
                  ('Afternoon', 'A winery tasting for the non-pilot.'),
                  ('Evening', 'Dinner at Cotto Modern Italian.')]},
    'harpers-ferry': {
        'day': [('Arrive', 'Land at KMRB mid-morning and pick up the crew car or a rental.'),
                ('Midday', 'The lower town and the national historical park, with lunch in town.'),
                ('Afternoon', 'A short walk to Jefferson Rock for the view, then back to the FBO.')],
        'extra': [('Morning', 'A bike ride on the C&O Canal towpath.'),
                  ('Afternoon', 'Antietam National Battlefield, or tubing on the river in summer.'),
                  ('Evening', 'Dinner and a stroll in Shepherdstown.')]},
    'hilton-head': {
        'day': [('Arrive', 'Land at KHXD mid-morning and ride to the beach.'),
                ('Midday', 'Rent bikes and ride the beach at low tide, then lunch near Coligny.'),
                ('Afternoon', 'Harbour Town and the lighthouse, then back to the FBO.')],
        'extra': [('Morning', 'A round at Harbour Town Golf Links or another island course.'),
                  ('Afternoon', 'The ferry to Daufuskie Island for lunch and a golf-cart ramble.'),
                  ('Evening', 'Late-night jazz at The Jazz Corner.')]},
    'highlands-cashiers': {
        'day': [('Arrive', 'Land at K1A5 early and pick up the car.'),
                ('Midday', 'Dry Falls and Bridal Veil Falls on the drive up, then lunch in Highlands.'),
                ('Afternoon', 'Sunset Rock or a stroll on Main Street, then down the mountain before dark.')],
        'extra': [('Morning', 'The Whiteside Mountain loop.'),
                  ('Afternoon', 'A drive to Whitewater Falls, or a spa afternoon at Old Edwards.'),
                  ('Evening', 'Dinner in Cashiers.')]},
    'st-michaels': {
        'day': [('Arrive', 'Land at KESN mid-morning and pick up the car.'),
                ('Midday', 'The Chesapeake Bay Maritime Museum, then crabs at The Crab Claw.'),
                ('Afternoon', 'A stroll around the St. Michaels harbor, then back to the FBO.')],
        'extra': [('Morning', 'Bikes and the Oxford–Bellevue Ferry to Oxford.'),
                  ('Afternoon', 'A sunset sail or a skipjack cruise.'),
                  ('Evening', 'Dinner at a waterfront restaurant on Tilghman Island.')]},
    'cape-may': {
        'day': [('Arrive', 'Land at KWWD mid-morning and walk to the NAS Wildwood Aviation Museum.'),
                ('Midday', 'A ride into Cape May and lunch at The Lobster House.'),
                ('Afternoon', 'A walk through the Victorian district, then back to the FBO.')],
        'extra': [('Morning', 'Birding at Cape May Point State Park and a climb of the lighthouse.'),
                  ('Afternoon', 'A winery tasting for the non-pilot.'),
                  ('Evening', 'Dinner and live music at the Blue Pig Tavern.')]},
    'shenandoah': {
        'day': [('Arrive', 'Land at KLUA early and pick up the car.'),
                ('Midday', 'Luray Caverns, then lunch in Luray.'),
                ('Afternoon', 'A drive up to an overlook on Skyline Drive, then back before afternoon storms.')],
        'extra': [('Morning', 'Hike to Hawksbill, the park’s highest summit.'),
                  ('Afternoon', 'Paddle or float the Shenandoah River.'),
                  ('Evening', 'Stargazing at Big Meadows.')]},
    'homestead': {
        'day': [('Arrive', 'Land at KHSP mid-morning, during FBO hours.'),
                ('Midday', 'A soak at the Warm Springs Pools, booked ahead.'),
                ('Afternoon', 'Lunch and tea at The Homestead, then back up the mountain to fly home.')],
        'extra': [('Morning', 'Fly-fishing or sporting clays at the resort.'),
                  ('Afternoon', 'A drive to Lake Moomaw or Douthat State Park.'),
                  ('Evening', 'A concert at Garth Newel Music Center.')]},
    'greenbrier': {
        'day': [('Arrive', 'Land at KLWB mid-morning and transfer to the resort.'),
                ('Midday', 'The Bunker tour and lunch at the resort.'),
                ('Afternoon', 'A walk around the grounds, then back to the FBO.')],
        'extra': [('Morning', 'A bike ride on the Greenbrier River Trail.'),
                  ('Afternoon', 'Lost World Caverns, or galleries in Lewisburg.'),
                  ('Evening', 'Dinner at The General Lewis Inn in Lewisburg.')]},
    'newport': {
        'day': [('Arrive', 'Land at KUUU mid-morning and pick up the car.'),
                ('Midday', 'The Breakers, then lunch at The Mooring.'),
                ('Afternoon', 'Part of the Cliff Walk, then back to the FBO.')],
        'extra': [('Morning', 'The International Tennis Hall of Fame, or Marble House.'),
                  ('Afternoon', 'A sail on an America’s Cup yacht.'),
                  ('Evening', 'Raw bar and sunset on Bowen’s Wharf.')]},
    'nantucket': {
        'day': [('Arrive', 'Land at KACK early and ride into town.'),
                ('Midday', 'The Whaling Museum and lunch on the wharf.'),
                ('Afternoon', 'Brant Point Lighthouse, then back to the airport before evening fog.')],
        'extra': [('Morning', 'An over-sand tour to Great Point.'),
                  ('Afternoon', 'Cisco Brewers for the non-pilot, and Surfside Beach.'),
                  ('Evening', 'Sunset at Madaket.')]},
    'bar-harbor': {
        'day': [('Arrive', 'Land at KBHB early and pick up the car.'),
                ('Midday', 'The Park Loop Road and popovers at Jordan Pond House.'),
                ('Afternoon', 'Cadillac Mountain, then back to the FBO.')],
        'extra': [('Morning', 'A whale-watch or puffin cruise.'),
                  ('Afternoon', 'The quiet side: Southwest Harbor and Bass Harbor Head Light.'),
                  ('Evening', 'Sunset on the Shore Path.')]},
    'stowe': {
        'day': [('Arrive', 'Land at KMVL early and pick up the car.'),
                ('Midday', 'The gondola up Mount Mansfield and lunch at the von Trapp Bierhall.'),
                ('Afternoon', 'The Recreation Path, then back before mountain afternoon weather.')],
        'extra': [('Morning', 'A hike to Sterling Pond or Stowe Pinnacle.'),
                  ('Afternoon', 'Ben & Jerry’s and Cold Hollow Cider Mill in Waterbury.'),
                  ('Evening', 'A spa evening and dinner at your resort.')]},
    'saratoga': {
        'day': [('Arrive', 'Land at 5B2 mid-morning and ride downtown.'),
                ('Midday', 'Lunch at Hattie’s and a walk on Broadway.'),
                ('Afternoon', 'A soak at the Roosevelt Baths, then back to the FBO.')],
        'extra': [('Morning', 'Saratoga National Historical Park.'),
                  ('Afternoon', 'The Racing Museum, or a day at the track in season.'),
                  ('Evening', 'A SPAC concert in summer.')]},
    'gettysburg': {
        'day': [('Arrive', 'Land at KW05 mid-morning and pick up the car.'),
                ('Midday', 'A Licensed Battlefield Guide tour.'),
                ('Afternoon', 'The Museum and Cyclorama, then back to the FBO.')],
        'extra': [('Morning', 'Eisenhower National Historic Site.'),
                  ('Afternoon', 'Adams County orchards and a winery for the non-pilot.'),
                  ('Evening', 'A ghost tour downtown.')]},
    'lancaster': {
        'day': [('Arrive', 'Land at KLNS mid-morning and pick up the car.'),
                ('Midday', 'Lunch at Central Market (Tue, Fri or Sat), then the Strasburg Rail Road.'),
                ('Afternoon', 'A back-roads drive past Amish farms, then back to the FBO.')],
        'extra': [('Morning', 'Sight & Sound Theatres for a big Biblical stage show.'),
                  ('Afternoon', 'Wineries and the chocolate shops of Lititz.'),
                  ('Evening', 'Dinner in a Lancaster city brewpub.')]},
    'hudson-valley': {
        'day': [('Arrive', 'Land at KPOU early and pick up the car.'),
                ('Midday', 'FDR’s home and lunch at the Culinary Institute.'),
                ('Afternoon', 'The Walkway Over the Hudson, then back to the FBO.')],
        'extra': [('Morning', 'Storm King Art Center.'),
                  ('Afternoon', 'Dia Beacon and a walk along Beacon’s Main Street.'),
                  ('Evening', 'Dinner in Kingston’s historic Stockade District.')]},
    'mystic': {
        'day': [('Arrive', 'Land at KGON mid-morning and pick up the car.'),
                ('Midday', 'Mystic Seaport Museum.'),
                ('Afternoon', 'A lobster roll in Noank, then back to the FBO.')],
        'extra': [('Morning', 'Mystic Aquarium.'),
                  ('Afternoon', 'A sail on the river or Fishers Island Sound.'),
                  ('Evening', 'Dinner in Stonington Borough.')]},
    'portsmouth': {
        'day': [('Arrive', 'Land at KPSM mid-morning and ride downtown.'),
                ('Midday', 'Strawbery Banke and lunch on the harbor.'),
                ('Afternoon', 'Market Square and Prescott Park, then back to the FBO.')],
        'extra': [('Morning', 'A cruise to the Isles of Shoals.'),
                  ('Afternoon', 'The coast road to Rye and Odiorne Point.'),
                  ('Evening', 'Dinner and the spa at Wentworth by the Sea.')]},
    'kennebunkport': {
        'day': [('Arrive', 'Land at KSFM mid-morning and pick up the car.'),
                ('Midday', 'Dock Square and a lobster roll at The Clam Shack.'),
                ('Afternoon', 'Ocean Avenue past Walker’s Point, then back to the FBO.')],
        'extra': [('Morning', 'Nubble Light and the beaches of York.'),
                  ('Afternoon', 'Ogunquit and the Marginal Way cliff walk.'),
                  ('Evening', 'A sunset harbor cruise.')]},
    'berkshires': {
        'day': [('Arrive', 'Land at KPSF mid-morning and pick up the car.'),
                ('Midday', 'The Norman Rockwell Museum and lunch in Stockbridge.'),
                ('Afternoon', 'The Mount, then back to the FBO.')],
        'extra': [('Morning', 'The Clark in Williamstown.'),
                  ('Afternoon', 'MASS MoCA in North Adams.'),
                  ('Evening', 'A summer evening at Jacob’s Pillow dance festival.')]},
    'lake-placid': {
        'day': [('Arrive', 'Land at KLKP mid-morning.'),
                ('Midday', 'The Olympic Center and lunch on Main Street.'),
                ('Afternoon', 'A walk around Mirror Lake, then back to the airport before afternoon mountain weather.')],
        'extra': [('Morning', 'A hike up Mount Jo or Cascade Mountain.'),
                  ('Afternoon', 'A boat tour on Lake Placid.'),
                  ('Evening', 'A spa evening by the fire.')]},
    'marthas-vineyard': {
        'day': [('Arrive', 'Land at KMVY early and ride to Edgartown.'),
                ('Midday', 'Lunch in Edgartown and a walk to the lighthouse.'),
                ('Afternoon', 'Oak Bluffs’ cottages, then back to the airport before evening fog.')],
        'extra': [('Morning', 'A bike ride to South Beach.'),
                  ('Afternoon', 'The Aquinnah Cliffs.'),
                  ('Evening', 'Sunset at Menemsha.')]},
    'bardstown': {
        'day': [('Arrive', 'Land at KBRY mid-morning; arrange a driver ahead.'),
                ('Midday', 'Lunch on the square and the Getz Museum.'),
                ('Afternoon', 'My Old Kentucky Home, then back to the FBO (the non-pilot can taste; the pilot waits for next time).')],
        'extra': [('Morning', 'Jim Beam’s American Stillhouse in Clermont, with a driver.'),
                  ('Afternoon', 'The Abraham Lincoln Birthplace, about 40 minutes away.'),
                  ('Evening', 'A bourbon dinner in Louisville.')]},
    'dayton': {
        'day': [('Arrive', 'Land at KMGY early and pick up the car.'),
                ('Midday', 'The National Museum of the U.S. Air Force.'),
                ('Afternoon', 'Carillon Park and the Wright Flyer III, then back to the FBO.')],
        'extra': [('Morning', 'The Wright Cycle Company and Hawthorn Hill tour.'),
                  ('Afternoon', 'Glen Helen and Clifton Gorge.'),
                  ('Evening', 'Dinner in the Oregon District.')]},
    'mackinac': {
        'day': [('Arrive', 'Land at KMCD mid-morning and take a carriage to town.'),
                ('Midday', 'Fort Mackinac and lunch on Main Street.'),
                ('Afternoon', 'Fudge and the Grand Hotel porch, then back to the airport.')],
        'extra': [('Morning', 'A ferry to St. Ignace or Mackinaw City for the bridge view.'),
                  ('Afternoon', 'A bike ride through the island’s interior trails.'),
                  ('Evening', 'Sunset at Mission Point.')]},
    'french-lick': {
        'day': [('Arrive', 'Land at KFRH mid-morning and take the shuttle.'),
                ('Midday', 'A historic tour of the West Baden dome and lunch at the resort.'),
                ('Afternoon', 'A spa treatment, then back to the airport.')],
        'extra': [('Morning', 'A second round, on the Donald Ross Course.'),
                  ('Afternoon', 'Horseback riding at the resort stables.'),
                  ('Evening', 'Live music at the resort.')]},
    'galena': {
        'day': [('Arrive', 'Land at KDBQ early and drive to Galena.'),
                ('Midday', 'Grant’s home and lunch on Main Street.'),
                ('Afternoon', 'A drive through the hills, then back to Dubuque.')],
        'extra': [('Morning', 'The National Mississippi River Museum in Dubuque.'),
                  ('Afternoon', 'A riverboat cruise.'),
                  ('Evening', 'Dinner overlooking the river.')]},
    'door-county': {
        'day': [('Arrive', 'Land at KSUE early and pick up the car.'),
                ('Midday', 'Fish Creek and Peninsula State Park.'),
                ('Afternoon', 'Lunch in Ephraim, then back to the FBO.')],
        'extra': [('Morning', 'The Washington Island ferry.'),
                  ('Afternoon', 'Wineries and orchards on the lake side.'),
                  ('Evening', 'A sunset cruise from Sister Bay.')]},
    'branson': {
        'day': [('Arrive', 'Land at KBBG mid-morning and pick up the car.'),
                ('Midday', 'Lunch and the nature trail at Top of the Rock.'),
                ('Afternoon', 'Lost Canyon Cave, then back to the FBO.')],
        'extra': [('Morning', 'Silver Dollar City.'),
                  ('Afternoon', 'A pontoon boat on Table Rock Lake.'),
                  ('Evening', 'A live show in town.')]},
    'lake-ozarks': {
        'day': [('Arrive', 'Land at KAIZ mid-morning.'),
                ('Midday', 'Ha Ha Tonka State Park’s castle ruins.'),
                ('Afternoon', 'Lunch by the lake, then back to the airport.')],
        'extra': [('Morning', 'A cave tour.'),
                  ('Afternoon', 'A second day on the water.'),
                  ('Evening', 'Sunset at a lakeside bar.')]},
    'hot-springs': {
        'day': [('Arrive', 'Land at KHOT mid-morning and drive downtown.'),
                ('Midday', 'Bathhouse Row and a thermal soak.'),
                ('Afternoon', 'Lunch at Superior Bathhouse Brewery, then back to the FBO.')],
        'extra': [('Morning', 'Garvan Woodland Gardens.'),
                  ('Afternoon', 'Hot Springs Mountain Tower and trails.'),
                  ('Evening', 'Live music at The Ohio Club.')]},
    'bentonville': {
        'day': [('Arrive', 'Land at KVBT mid-morning; coffee at Airship.'),
                ('Midday', 'Crystal Bridges and lunch at the museum.'),
                ('Afternoon', 'The square, then back to the FBO.')],
        'extra': [('Morning', 'A mountain-bike ride on the forest trails.'),
                  ('Afternoon', 'The Momentary.'),
                  ('Evening', 'Dinner in Rogers or Fayetteville.')]},
    'eureka-springs': {
        'day': [('Arrive', 'Land at 4M1 early and drive to town.'),
                ('Midday', 'Thorncrown Chapel and the historic loop.'),
                ('Afternoon', 'Lunch downtown, then back to the airport.')],
        'extra': [('Morning', 'Turpentine Creek Wildlife Refuge.'),
                  ('Afternoon', 'Beaver Lake.'),
                  ('Evening', 'A ghost tour at the Crescent.')]},
    'duluth': {
        'day': [('Arrive', 'Land at KDLH early and pick up the car.'),
                ('Midday', 'Canal Park and the Aerial Lift Bridge.'),
                ('Afternoon', 'Smoked fish at Northern Waters, then back to the FBO.')],
        'extra': [('Morning', 'Drive farther up the North Shore to Tettegouche State Park.'),
                  ('Afternoon', 'The Great Lakes Aquarium.'),
                  ('Evening', 'A sunset harbor cruise.')]},
    'naples': {
        'day': [('Arrive', 'Land at KAPF mid-morning and pick up the car.'),
                ('Midday', 'Lunch on Fifth Avenue South and the beach.'),
                ('Afternoon', 'The pier, then back to the FBO before afternoon storms.')],
        'extra': [('Morning', 'Corkscrew Swamp Sanctuary.'),
                  ('Afternoon', 'A shelling cruise to Keewaydin Island.'),
                  ('Evening', 'Sunset dinner by the Gulf.')]},
    'sanibel': {
        'day': [('Arrive', 'Land at KFMY early and drive to Sanibel.'),
                ('Midday', '“Ding” Darling and lunch on the island.'),
                ('Afternoon', 'Shelling, then back across the causeway.')],
        'extra': [('Morning', 'A kayak trip through the mangroves.'),
                  ('Afternoon', 'A boat to Cabbage Key for lunch.'),
                  ('Evening', 'Sunset on Captiva.')]},
    'islamorada': {
        'day': [('Arrive', 'Land at KMTH early and drive north.'),
                ('Midday', 'Tarpon at Robbie’s and lunch on the water.'),
                ('Afternoon', 'A swim, then back to Marathon.')],
        'extra': [('Morning', 'A backcountry fishing charter.'),
                  ('Afternoon', 'A boat to Indian Key Historic State Park.'),
                  ('Evening', 'Sunset in the sand at Morada Bay.')]},
    'palm-beach': {
        'day': [('Arrive', 'Land at KLNA mid-morning and drive to the island.'),
                ('Midday', 'Lunch at Ta-boó and Worth Avenue.'),
                ('Afternoon', 'The Flagler Museum, then back to the FBO.')],
        'extra': [('Morning', 'Polo in Wellington in season.'),
                  ('Afternoon', 'The Norton Museum of Art.'),
                  ('Evening', 'Dinner on Clematis Street in West Palm Beach.')]},
    'cedar-key': {
        'day': [('Arrive', 'Land at KCDK mid-morning and pick up a golf cart.'),
                ('Midday', 'Chowder at Tony’s and Dock Street.'),
                ('Afternoon', 'A short kayak, then fly before afternoon storms.')],
        'extra': [('Morning', 'A boat tour of the refuge islands.'),
                  ('Afternoon', 'Bikes around the island.'),
                  ('Evening', 'Sunset on Dock Street.')]},
    '30a': {
        'day': [('Arrive', 'Land at KECP early and pick up the car.'),
                ('Midday', 'Seaside and lunch at a beach café.'),
                ('Afternoon', 'A swim, then back to the airport.')],
        'extra': [('Morning', 'A paddle on a coastal dune lake.'),
                  ('Afternoon', 'Shops in Rosemary and Alys Beach.'),
                  ('Evening', 'Sunset at Grayton Beach.')]},
    'fredericksburg': {
        'day': [('Arrive', 'Land at T82 early.'),
                ('Midday', 'Breakfast at the Airport Diner and the Pacific War museum.'),
                ('Afternoon', 'Main Street, then back to the field.')],
        'extra': [('Morning', 'Johnson City and the LBJ Ranch.'),
                  ('Afternoon', 'A second day on Wine Road 290 for the non-pilot.'),
                  ('Evening', 'Live music in Luckenbach.')]},
    'san-antonio': {
        'day': [('Arrive', 'Land at KSSF early.'),
                ('Midday', 'Mission San José and lunch at Mi Tierra.'),
                ('Afternoon', 'The Alamo, then back to Stinson.')],
        'extra': [('Morning', 'The other missions by bike on the Mission Reach trail.'),
                  ('Afternoon', 'The Pearl and the San Antonio Museum of Art.'),
                  ('Evening', 'A river barge dinner cruise.')]},
    'fort-worth': {
        'day': [('Arrive', 'Land at KFTW mid-morning.'),
                ('Midday', 'The cattle drive and lunch at Joe T. Garcia’s.'),
                ('Afternoon', 'The Vintage Flying Museum, then fly home.')],
        'extra': [('Morning', 'The Kimbell and the Modern Art Museum.'),
                  ('Afternoon', 'The Fort Worth Botanic Garden.'),
                  ('Evening', 'A rodeo night in the Stockyards.')]},
    'new-orleans': {
        'day': [('Arrive', 'Land at KNEW mid-morning.'),
                ('Midday', 'Beignets and Jackson Square, then lunch in the Quarter.'),
                ('Afternoon', 'Preservation Hall’s early set, then back to the FBO.')],
        'extra': [('Morning', 'The National WWII Museum.'),
                  ('Afternoon', 'The St. Charles streetcar and the Garden District.'),
                  ('Evening', 'A jazz dinner cruise on the Steamboat Natchez.')]},
    'natchez': {
        'day': [('Arrive', 'Land at KHEZ mid-morning.'), ('Midday', 'Melrose with a ranger, then lunch downtown.'), ('Afternoon', 'The bluff, then back to the airport.')],
        'extra': [('Morning', 'Longwood.'), ('Afternoon', 'Drive the Natchez Trace to Emerald Mound.'), ('Evening', 'Sunset on the bluff.')]},
    'oxford': {
        'day': [('Arrive', 'Land at KUOX mid-morning.'), ('Midday', 'Lunch on the Square and Square Books.'), ('Afternoon', 'Rowan Oak, then back to the FBO.')],
        'extra': [('Morning', 'The University Museum and Bailey’s Woods.'), ('Afternoon', 'Walk the campus and the Grove.'), ('Evening', 'Thacker Mountain Radio, if it’s on.')]},
    'bay-st-louis': {
        'day': [('Arrive', 'Land at KHSA mid-morning.'), ('Midday', 'INFINITY Science Center.'), ('Afternoon', 'Lunch on the beach in Old Town, then back to the FBO.')],
        'extra': [('Morning', 'The Walter Anderson Museum in Ocean Springs.'), ('Afternoon', 'Galleries in Old Town.'), ('Evening', 'Sunset over the bay.')]},
    'st-francisville': {
        'day': [('Arrive', 'Land at KBTR early and drive north.'), ('Midday', 'Rosedown’s gardens and lunch in town.'), ('Afternoon', 'The historic district, then back to BTR.')],
        'extra': [('Morning', 'The Audubon State Historic Site.'), ('Afternoon', 'A hike in the Tunica Hills.'), ('Evening', 'Dinner at The Myrtles.')]},
    'lafayette': {
        'day': [('Arrive', 'Land at KLFT mid-morning.'), ('Midday', 'Boudin at Johnson’s and Vermilionville.'), ('Afternoon', 'A Lake Martin swamp tour, then back to the FBO.')],
        'extra': [('Morning', 'Zydeco breakfast at Buck & Johnny’s.'), ('Afternoon', 'Avery Island and Tabasco.'), ('Evening', 'Dancing at the Blue Moon Saloon.')]},
    'fairhope': {
        'day': [('Arrive', 'Land at KCQF mid-morning.'), ('Midday', 'Lunch downtown and the pier.'), ('Afternoon', 'Bellingrath Gardens, then back to the FBO.')],
        'extra': [('Morning', 'The USS Alabama.'), ('Afternoon', 'The spa at The Grand.'), ('Evening', 'Sunset on the pier.')]},
    'huntsville': {
        'day': [('Arrive', 'Land at KHSV early.'), ('Midday', 'The U.S. Space & Rocket Center.'), ('Afternoon', 'Lunch downtown, then back to the FBO.')],
        'extra': [('Morning', 'The Botanical Garden.'), ('Afternoon', 'Monte Sano State Park.'), ('Evening', 'Rooftop drinks downtown.')]},
    'lake-martin': {
        'day': [('Arrive', 'Land at KALX mid-morning.'), ('Midday', 'Lunch at Russell Crossroads.'), ('Afternoon', 'A short boat ride, then back to the airport.')],
        'extra': [('Morning', 'The Smith Mountain fire tower.'), ('Afternoon', 'A boat day.'), ('Evening', 'Dinner at SpringHouse.')]},
    'birmingham': {
        'day': [('Arrive', 'Land at KBHM mid-morning.'), ('Midday', 'The Southern Museum of Flight, beside the field.'), ('Afternoon', 'Lunch at Chez Fonfon, then back to the FBO.')],
        'extra': [('Morning', 'The Civil Rights Institute.'), ('Afternoon', 'Barber Vintage Motorsports Museum.'), ('Evening', 'Sunset at Vulcan Park.')]},
    'memphis': {
        'day': [('Arrive', 'Land at KMEM early.'), ('Midday', 'Sun Studio and lunch at Central BBQ.'), ('Afternoon', 'The National Civil Rights Museum, then back to the FBO.')],
        'extra': [('Morning', 'Graceland.'), ('Afternoon', 'Stax Museum.'), ('Evening', 'Beale Street.')]},
    'golden-isles': {
        'day': [('Arrive', 'Land at KSSI mid-morning.'), ('Midday', 'Bike to the lighthouse and lunch in the village.'), ('Afternoon', 'The beach, then back to the FBO.')],
        'extra': [('Morning', 'Driftwood Beach on Jekyll.'), ('Afternoon', 'The Jekyll Island Club and Turtle Center.'), ('Evening', 'Sunset over the marsh.')]},
    'clarksdale': {
        'day': [('Arrive', 'Land at KCKM mid-morning.'), ('Midday', 'The Delta Blues Museum and tamales.'), ('Afternoon', 'Cat Head and the Crossroads, then back to the airport.')],
        'extra': [('Morning', 'A Blues Trail drive.'), ('Afternoon', 'Barbecue at Abe’s.'), ('Evening', 'Red’s Lounge.')]},
    'natchitoches': {
        'day': [('Arrive', 'Land at KIER mid-morning.'), ('Midday', 'Meat pies at Lasyone’s and Front Street.'), ('Afternoon', 'Oakland Plantation, then back to the airport.')],
        'extra': [('Morning', 'Melrose Plantation.'), ('Afternoon', 'A historic-district walk.'), ('Evening', 'Sunset on Cane River Lake.')]},
    'little-rock': {
        'day': [('Arrive', 'Land at KLIT early.'), ('Midday', 'Central High School with a ranger.'), ('Afternoon', 'The River Market, then back to the FBO.')],
        'extra': [('Morning', 'Bike the Big Dam Bridge.'), ('Afternoon', 'Pinnacle Mountain.'), ('Evening', 'Dinner on the river.')]},
    'st-louis': {
        'day': [('Arrive', 'Land at KCPS early.'), ('Midday', 'The Gateway Arch tram.'), ('Afternoon', 'Lunch on The Hill, then back to the FBO.')],
        'extra': [('Morning', 'The Art Museum in Forest Park.'), ('Afternoon', 'The Botanical Garden.'), ('Evening', 'Ted Drewes custard.')]},
    'kansas-city': {
        'day': [('Arrive', 'Land at KMKC mid-morning.'), ('Midday', 'The TWA Museum on the field, then barbecue at Joe’s.'), ('Afternoon', 'The Nelson-Atkins, then back to the FBO.')],
        'extra': [('Morning', 'The WWI Museum.'), ('Afternoon', '18th & Vine.'), ('Evening', 'Jazz at the Blue Room.')]},
    'annapolis': {
        'day': [('Arrive', 'Land at KANP mid-morning.'), ('Midday', 'A Naval Academy tour and lunch at Middleton Tavern.'), ('Afternoon', 'Walk the harbor, then back to the airport.')],
        'extra': [('Morning', 'The State House and Paca House garden.'), ('Afternoon', 'A sail on the Woodwind.'), ('Evening', 'Dinner in Eastport.')]},
    'ocean-city': {
        'day': [('Arrive', 'Land at KOXB mid-morning.'), ('Midday', 'The boardwalk and Thrasher’s fries.'), ('Afternoon', 'The beach, then back to the airport.')],
        'extra': [('Morning', 'Wild horses at Assateague.'), ('Afternoon', 'Berlin’s Main Street.'), ('Evening', 'Sunset at Fager’s Island.')]},
    'deep-creek-lake': {
        'day': [('Arrive', 'Land at 2G4 mid-morning.'), ('Midday', 'Swallow Falls State Park.'), ('Afternoon', 'Lunch by the lake, then back to the airport.')],
        'extra': [('Morning', 'A pontoon on the lake.'), ('Afternoon', 'The mountain coaster at Wisp.'), ('Evening', 'Dinner at Mountain State Brewing.')]},
    'new-river-gorge': {
        'day': [('Arrive', 'Land at KBKW early.'), ('Midday', 'The Canyon Rim Visitor Center and lunch in Fayetteville.'), ('Afternoon', 'Long Point Trail, then back to the airport.')],
        'extra': [('Morning', 'Whitewater rafting.'), ('Afternoon', 'The Bridge Walk.'), ('Evening', 'Pies & Pints.')]},
    'berkeley-springs': {
        'day': [('Arrive', 'Land at KMRB early and drive west.'), ('Midday', 'A Roman bath soak.'), ('Afternoon', 'The Ice House, then back to the airport.')],
        'extra': [('Morning', 'Cacapon Resort State Park.'), ('Afternoon', 'Panorama Overlook.'), ('Evening', 'Dinner at Lot 12.')]},
    'lexington': {
        'day': [('Arrive', 'Land at KLEX early.'), ('Midday', 'Keeneland and the track kitchen.'), ('Afternoon', 'Old Friends Farm, then back to the FBO.')],
        'extra': [('Morning', 'The Kentucky Horse Park.'), ('Afternoon', 'Woodford Reserve.'), ('Evening', 'Dinner at Holly Hill Inn.')]},
    'louisville': {
        'day': [('Arrive', 'Land at KLOU mid-morning.'), ('Midday', 'The Derby Museum and a Hot Brown.'), ('Afternoon', 'Whiskey Row, then back to the FBO.')],
        'extra': [('Morning', 'The Slugger Museum.'), ('Afternoon', 'The Ali Center and Big Four Bridge.'), ('Evening', 'Dinner at Jack Fry’s.')]},
    'paducah': {
        'day': [('Arrive', 'Land at KPAH mid-morning.'), ('Midday', 'The National Quilt Museum.'), ('Afternoon', 'The floodwall murals, then back to the FBO.')],
        'extra': [('Morning', 'LowerTown galleries.'), ('Afternoon', 'The River Discovery Center.'), ('Evening', 'Dinner at Freight House.')]},
    'finger-lakes': {
        'day': [('Arrive', 'Land at KITH early.'), ('Midday', 'Taughannock Falls and lunch in Ithaca.'), ('Afternoon', 'A Cayuga Lake winery, then back to the FBO.')],
        'extra': [('Morning', 'Watkins Glen.'), ('Afternoon', 'Seneca Lake wineries.'), ('Evening', 'Dinner at Gola Osteria.')]},
    'bucks-county': {
        'day': [('Arrive', 'Land at KDYL mid-morning.'), ('Midday', 'New Hope and Lambertville.'), ('Afternoon', 'Washington Crossing, then back to the FBO.')],
        'extra': [('Morning', 'The Mercer Museum.'), ('Afternoon', 'The Michener Art Museum.'), ('Evening', 'A Playhouse show.')]},
    'poconos': {
        'day': [('Arrive', 'Land at KMPO mid-morning.'), ('Midday', 'Bushkill Falls.'), ('Afternoon', 'Lunch, then back to the airport.')],
        'extra': [('Morning', 'The Delaware Water Gap.'), ('Afternoon', 'The Lehigh Gorge train.'), ('Evening', 'Dinner by the fire.')]},
    'camden': {
        'day': [('Arrive', 'Land at KRKD early.'), ('Midday', 'The Owls Head Transportation Museum.'), ('Afternoon', 'Lunch in Rockland, then back to the FBO.')],
        'extra': [('Morning', 'Mount Battie.'), ('Afternoon', 'A windjammer sail.'), ('Evening', 'Lobster by the harbor.')]},
    'portland-maine': {
        'day': [('Arrive', 'Land at KPWM mid-morning.'), ('Midday', 'Lunch at Eventide and the Old Port.'), ('Afternoon', 'Portland Head Light, then back to the FBO.')],
        'extra': [('Morning', 'A Casco Bay ferry.'), ('Afternoon', 'The Portland Museum of Art.'), ('Evening', 'Dinner at Fore Street.')]},
    'chatham': {
        'day': [('Arrive', 'Land at KCQX mid-morning.'), ('Midday', 'Lunch at the fish pier.'), ('Afternoon', 'The lighthouse and beach, then back to the airport.')],
        'extra': [('Morning', 'A seal tour.'), ('Afternoon', 'Bike the rail trail.'), ('Evening', 'Dinner on Main Street.')]},
    'princeton': {
        'day': [('Arrive', 'Land at 39N mid-morning.'), ('Midday', 'Campus and the art museum.'), ('Afternoon', 'Grounds For Sculpture, then back to the airport.')],
        'extra': [('Morning', 'Morven.'), ('Afternoon', 'Lake Carnegie.'), ('Evening', 'A McCarter show.')]},
    'block-island': {
        'day': [('Arrive', 'Land at KBID mid-morning.'), ('Midday', 'Rent bikes and ride to Mohegan Bluffs.'), ('Afternoon', 'The beach, then back to the airport.')],
        'extra': [('Morning', 'North Light and Clay Head Trail.'), ('Afternoon', 'The beach.'), ('Evening', 'Sunset at the Atlantic Inn.')]},
    'providence': {
        'day': [('Arrive', 'Land at KPVD mid-morning.'), ('Midday', 'Walk Benefit Street and College Hill.'), ('Afternoon', 'Federal Hill, then back to the airport.')],
        'extra': [('Morning', 'The RISD Museum.'), ('Afternoon', 'Federal Hill.'), ('Evening', 'Dinner at Oberlin, then WaterFire.')]},
    'watch-hill': {
        'day': [('Arrive', 'Land at KWST mid-morning.'), ('Midday', 'Walk the village and ride the carousel.'), ('Afternoon', 'The spa, then back to the airport.')],
        'extra': [('Morning', 'Napatree Point.'), ('Afternoon', 'The spa.'), ('Evening', 'Dinner at Ocean House.')]},
    'new-haven': {
        'day': [('Arrive', 'Land at KHVN mid-morning.'), ('Midday', 'The Yale University Art Gallery.'), ('Afternoon', 'The Center for British Art, then back to the airport.')],
        'extra': [('Morning', 'The Peabody Museum.'), ('Afternoon', 'The Center for British Art.'), ('Evening', 'Dinner at Union League, then Yale Rep.')]},
    'essex-ct': {
        'day': [('Arrive', 'Land at KSNC mid-morning.'), ('Midday', 'Walk Essex village and the river museum.'), ('Afternoon', 'Gillette Castle, then back to the airport.')],
        'extra': [('Morning', 'The Essex Steam Train and riverboat.'), ('Afternoon', 'Gillette Castle.'), ('Evening', 'A Goodspeed show.')]},
    'litchfield-hills': {
        'day': [('Arrive', 'Land at KOXC mid-morning.'), ('Midday', 'Drive to the inn; walk the grounds.'), ('Afternoon', 'Hopkins Vineyard and Lake Waramaug, then back to the airport.')],
        'extra': [('Morning', 'The spa.'), ('Afternoon', 'Hopkins Vineyard and Lake Waramaug.'), ('Evening', 'Dinner at the Hopkins Inn.')]},
    'asbury-park': {
        'day': [('Arrive', 'Land at KBLM mid-morning.'), ('Midday', 'The boardwalk and Silverball.'), ('Afternoon', 'Spring Lake, then back to the airport.')],
        'extra': [('Morning', 'The beach.'), ('Afternoon', 'Spring Lake.'), ('Evening', 'Pizza at Talula’s.')]},
    'atlantic-city': {
        'day': [('Arrive', 'Land at KACY mid-morning.'), ('Midday', 'The boardwalk at sunset.'), ('Afternoon', 'Absecon Lighthouse, then back to the airport.')],
        'extra': [('Morning', 'The spa.'), ('Afternoon', 'Absecon Lighthouse.'), ('Evening', 'Dinner at the Knife & Fork Inn and a show.')]},
    'woodstock-vt': {
        'day': [('Arrive', 'Land at KLEB early.'), ('Midday', 'Walk the village green and covered bridge.'), ('Afternoon', 'Billings Farm and the national park, then back to the airport.')],
        'extra': [('Morning', 'Billings Farm and the national park.'), ('Afternoon', 'Quechee Gorge and Simon Pearce glassblowing.'), ('Evening', 'Dinner at Simon Pearce.')]},
    'manchester-vt': {
        'day': [('Arrive', 'Land at KDDH early.'), ('Midday', 'Walk Manchester Village and the Northshire Bookstore.'), ('Afternoon', 'Hildene, then back to the airport.')],
        'extra': [('Morning', 'Hildene.'), ('Afternoon', 'Skyline Drive, then the spa.'), ('Evening', 'Dinner at The Silver Fork.')]},
    'burlington-vt': {
        'day': [('Arrive', 'Land at KBTV early.'), ('Midday', 'Church Street and the waterfront.'), ('Afternoon', 'Shelburne Farms, then back to the airport.')],
        'extra': [('Morning', 'Shelburne Farms.'), ('Afternoon', 'The Shelburne Museum.'), ('Evening', 'A sunset cruise, then Honey Road.')]},
    'bretton-woods': {
        'day': [('Arrive', 'Land at KHIE early.'), ('Midday', 'Check in and sit on the veranda.'), ('Afternoon', 'The Cog Railway to the summit, then back to the airport.')],
        'extra': [('Morning', 'The Cog Railway to the summit.'), ('Afternoon', 'The spa.'), ('Evening', 'Dinner at Sugar Hill Inn.')]},
    'lake-winnipesaukee': {
        'day': [('Arrive', 'Land at KLCI early.'), ('Midday', 'Walk Meredith’s waterfront.'), ('Afternoon', 'A cruise on the M/S Mount Washington, then back to the airport.')],
        'extra': [('Morning', 'A cruise on the M/S Mount Washington.'), ('Afternoon', 'Castle in the Clouds.'), ('Evening', 'Dinner at Wolfe’s Tavern.')]},
    'north-conway': {
        'day': [('Arrive', 'Land at KIZG early.'), ('Midday', 'Drive through the covered bridge to Jackson.'), ('Afternoon', 'The Conway Scenic Railroad, then back to the airport.')],
        'extra': [('Morning', 'The Conway Scenic Railroad.'), ('Afternoon', 'The Kancamagus Highway.'), ('Evening', 'Dinner at Moat Mountain.')]},
    'black-hills': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'Drive to Custer State Park.'), ('Afternoon', 'The Wildlife Loop.')],
        'extra': [('Morning', 'The Wildlife Loop.'), ('Afternoon', 'The Needles Highway and Sylvan Lake.'), ('Evening', 'Dinner at Delmonico Grill.')]},
    'deadwood': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'Walk Main Street.'), ('Afternoon', 'Spearfish Canyon waterfalls.')],
        'extra': [('Morning', 'Spearfish Canyon waterfalls.'), ('Afternoon', 'Mount Moriah Cemetery.'), ('Evening', 'Dinner at the Bullock.')]},
    'badlands': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'Drive to the park; sunset on the Loop Road.'), ('Afternoon', 'Sunrise hike on the Door Trail.')],
        'extra': [('Morning', 'Sunrise hike on the Door Trail.'), ('Afternoon', 'The Minuteman Missile site.'), ('Evening', 'Dinner at the lodge.')]},
    'sioux-falls': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'Falls Park.'), ('Afternoon', 'SculptureWalk.')],
        'extra': [('Morning', 'SculptureWalk.'), ('Afternoon', 'The Washington Pavilion.'), ('Evening', 'Dinner at Minervas.')]},
    'medora': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'Drive to Medora.'), ('Afternoon', 'The park’s scenic loop at sunrise.')],
        'extra': [('Morning', 'The park’s scenic loop at sunrise.'), ('Afternoon', 'The Presidential Library.'), ('Evening', 'Dinner at Theodore’s.')]},
    'fargo': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'The Fargo Air Museum, on the field.'), ('Afternoon', 'The Plains Art Museum.')],
        'extra': [('Morning', 'The Plains Art Museum.'), ('Afternoon', 'Walk downtown.'), ('Evening', 'A show at the Fargo Theatre.')]},
    'bismarck': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'The State Capitol.'), ('Afternoon', 'The Heritage Center & State Museum.')],
        'extra': [('Morning', 'The Heritage Center & State Museum.'), ('Afternoon', 'Fort Abraham Lincoln.'), ('Evening', 'Dinner at Pirogue Grille.')]},
    'peace-garden': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'Settle in at the lake.'), ('Afternoon', 'The International Peace Garden.')],
        'extra': [('Morning', 'The International Peace Garden.'), ('Afternoon', 'A paddle on Lake Metigoshe.'), ('Evening', 'Dinner in Bottineau.')]},
    'omaha': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'The Old Market and the pedestrian bridge.'), ('Afternoon', 'The SAC Aerospace Museum.')],
        'extra': [('Morning', 'The SAC Aerospace Museum.'), ('Afternoon', 'Lauritzen Gardens.'), ('Evening', 'Steaks at Gorat’s.')]},
    'lincoln-ne': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'The State Capitol observation deck.'), ('Afternoon', 'The Sheldon Museum of Art.')],
        'extra': [('Morning', 'The Sheldon Museum of Art.'), ('Afternoon', 'The International Quilt Museum.'), ('Evening', 'Dinner in the Haymarket.')]},
    'scottsbluff': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'The Scotts Bluff summit road.'), ('Afternoon', 'Hike the Saddle Rock Trail.')],
        'extra': [('Morning', 'Hike the Saddle Rock Trail.'), ('Afternoon', 'Chimney Rock.'), ('Evening', 'Sunset at the rock.')]},
    'valentine': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'Settle in near the river.'), ('Afternoon', 'Float the Niobrara.')],
        'extra': [('Morning', 'Float the Niobrara.'), ('Afternoon', 'Smith Falls.'), ('Evening', 'Dinner in town.')]},
    'wichita': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'The Kansas Aviation Museum.'), ('Afternoon', 'Botanica.')],
        'extra': [('Morning', 'Botanica.'), ('Afternoon', 'Old Cowtown Museum.'), ('Evening', 'Dinner in Old Town.')]},
    'flint-hills': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'Drive to Cottonwood Falls.'), ('Afternoon', 'Tallgrass Prairie National Preserve.')],
        'extra': [('Morning', 'Tallgrass Prairie National Preserve.'), ('Afternoon', 'The Flint Hills Scenic Byway.'), ('Evening', 'Dinner at Hays House.')]},
    'lawrence': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'Walk Mass Street.'), ('Afternoon', 'The Spencer Museum of Art.')],
        'extra': [('Morning', 'The Spencer Museum of Art.'), ('Afternoon', 'Campus and the overlook.'), ('Evening', 'Dinner at 715, then Liberty Hall.')]},
    'lindsborg': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'Drive to Lindsborg.'), ('Afternoon', 'The Sandzén Gallery and Coronado Heights.')],
        'extra': [('Morning', 'The Sandzén Gallery and Coronado Heights.'), ('Afternoon', 'Drive to Abilene.'), ('Evening', 'Dinner in Abilene.')]},
    'galveston': {
        'day': [('Arrive', 'Land at KGLS mid-morning.'),
                ('Midday', 'The Strand and lunch on the seawall.'),
                ('Afternoon', 'Bishop’s Palace, then back to the FBO.')],
        'extra': [('Morning', 'Moody Gardens.'),
                  ('Afternoon', 'A dolphin boat tour in the harbor.'),
                  ('Evening', 'Sunset on the seawall.')]},
    'south-padre': {
        'day': [('Arrive', 'Land at KPIL early and cross the causeway.'),
                ('Midday', 'Sea Turtle, Inc. and lunch by the bay.'),
                ('Afternoon', 'The beach, then back to the airport.')],
        'extra': [('Morning', 'A fishing charter in the Gulf.'),
                  ('Afternoon', 'Laguna Atascosa National Wildlife Refuge.'),
                  ('Evening', 'A sunset bay cruise.')]},
    'marfa': {
        'day': [('Arrive', 'Land at KMRF early in the cool air.'),
                ('Midday', 'A Chinati tour and lunch in town.'),
                ('Afternoon', 'Prada Marfa, then fly before afternoon heat and winds.')],
        'extra': [('Morning', 'Davis Mountains State Park.'),
                  ('Afternoon', 'Balmorhea State Park’s spring-fed pool.'),
                  ('Evening', 'A second observatory star party.')]},
}
STYLE_RE = re.compile(r'<span>WEEKEND STYLE</span><strong(?: data-style data-transport="[^"]*")?>Two nights <small>· ([^<]+)</small></strong>')


def block(kind, title, eyebrow, items):
    lis = ''.join(f'<li><strong>{t}</strong><p>{p}</p></li>' for t, p in items)
    return (f'<div class="trip-plan" data-trip="{kind}" hidden><span class="eyebrow">{eyebrow}</span>'
            f'<h3>{title}</h3><ol>{lis}</ol></div>')


for path in map(Path, sys.argv[1:]):
    slug = path.parent.name
    if slug not in PLANS:
        print('skip (no plans):', path)
        continue
    s = path.read_text()
    s = re.sub(r'<div class="trip-plan".*?</ol></div>', '', s)
    m = STYLE_RE.search(s)
    if not m:
        sys.exit(f'weekend style not found in {path}')
    s = s.replace(m.group(0), f'<span>WEEKEND STYLE</span><strong data-style data-transport="{m.group(1)}">Two nights <small>· {m.group(1)}</small></strong>', 1)
    p = PLANS[slug]
    day = block('Day trip', 'Just for the day', 'Day trip version', p['day'])
    extra = block('Longer stay', 'With an extra day', 'Longer stay · Add a day', p['extra'])
    i = s.index('<section id="itinerary">')
    j = s.index('<div class="days">', i)
    s = s[:j] + day + s[j:]
    k = s.index('</section>', j)
    s = s[:k] + extra + s[k:]
    path.write_text(s)
    print('trip plans added:', path)
