# WingAway Weekends — Project Notes

Updated: November 1, 2026 (after migration from ChatGPT to Claude and GitHub Pages).

## Goals and agreed direction

WingAway Weekends helps general aviation pilots and their travel companions discover worthwhile short getaways. The experience connects an appealing destination with practical arrival, lodging, dining and activity information, with an initial emphasis on couples.

The agreed MVP is a curated discovery homepage with 5–10 handpicked destinations from KMYR and only 1–2 developed guides. The current site contains ten destination cards and guides for all twelve destinations. Automatic recommendations for every airport are outside the current MVP.

The design uses navy, cream and gold, an aspirational destination hero photograph, the headline “Where will your wings take you this weekend?”, prominent airport and flight-time controls, and destination cards. ForeFlight remains the pilot’s operational flight-planning tool; WingAway provides destination discovery rather than weather, routing or dispatch decisions.

## Current source and publication status

- **Source of truth:** this GitHub repository, `ramorganmd-beep/WingAwayWeekends` (public). The project moved from ChatGPT to Claude on November 1, 2026. Older ChatGPT ZIPs and chats are history, not competing baselines.
- **Live site:** https://wingawayweekends.com (also www.wingawayweekends.com) — Cloudflare Pages project `wingawayweekends`, connected to this repository: production branch `main`, no build command, output directory `docs`. Any change merged into `main` goes live within a minute or two. The domain is registered with Cloudflare; both custom domains were activated November 1, 2026. Test address: https://wingawayweekends.pages.dev.
- **Backup host:** GitHub Pages (https://ramorganmd-beep.github.io/WingAwayWeekends/) also publishes `docs/` from `main`, unless it has been turned off in the repository settings.
- **Workflow:** Claude makes changes on a separate branch and pushes it; the user reviews and merges the pull request on GitHub. Shorthand: when the owner writes “lg” (“looks good”) about a guide, mark that guide Reviewed. After a merge, a hard refresh (Cmd + Shift + R on Mac; pull down or a Private tab on iPhone/iPad) shows the new version; Cloudflare’s Purge Everything is rarely needed.
- The ten-photo set, including the four replacements (Asheville, Key West, Pinehurst, Greenville), was **approved and published** on November 1, 2026.
- The site is public; the ChatGPT-hosted access gate no longer applies. Review pages (`photo-review.html`, `mobile-review.html`) are marked `noindex`.
- **Former hosting (retired):** ChatGPT Sites at https://wingaway-savannah.ramorganmd.chatgpt.site (project `appgprj_6abe9d437ef8819196353f64245055a8`, last confirmed version 7). It no longer receives updates and can be left or deleted.

## Features built

### Discovery homepage

- Responsive hero and destination-card grid, with layouts for desktop, tablet and mobile.
- Departure airport input (default KMYR) covering 695 public airports in NC, SC, GA, FL, VA, TN and AL, with suggestions as you type. It accepts K-codes (KCHS), codes without the K (CHS) and 3-character FAA IDs (2J9). Airports outside the region show a “coming soon” message. A destination is hidden if it is the home airport or within 40 NM of it.
- Maximum estimated flight time offers 1 to 4½ hours in half-hour steps plus “Any distance” (shows all twelve, added November 2, 2026) for every trip length (changed November 1, 2026 at the owner’s request). Trip length only sets the starting value: Day trip 1½ hours, Weekend 3 hours (page default), Longer stay 4½ hours. Changing trip length resets flight time to that default.
- Interest checkboxes, in this order: Boutique stays, Dining, Wine, Spa, Romance, History, Outdoors, Hiking, Golf and Aviation museums. Aviation museums is currently tagged on Savannah (Mighty Eighth Air Force Museum) Charleston (Patriots Point / USS Yorktown) and Asheville (Western North Carolina Air Museum, Hendersonville); other destinations need review before tagging.
- Multiple selected interests use AND matching: a destination must have every selected tag.
- Live result count and an empty-state message when nothing matches.
- **Review status:** Reviewed by the owner: Charleston, Nashville, Beaufort, Charlottesville, Greenville, Pinehurst, Asheville, Outer Banks, Amelia Island, Yadkin Valley, Virginia Hunt Country, Dahlonega, St. Augustine and Key West (all “Reviewed November 2, 2026”; header “Destination guide”, footer “Couples guide”). All other guides are still “Draft for review”; review them one at a time the same way. To mark a guide reviewed, set `REVIEWED = 'Month D, YYYY'` in its build script and pass `reviewed=REVIEWED` to `page_start` and `page_end` (see `build_nashville.py`), then rerun the pipeline. Charleston, Pinehurst and Asheville have standalone builders, so their header, closing note and footer are edited directly.
- **Hotel and restaurant links (November 2, 2026):** every hotel and restaurant card links out. Picks with a confirmed official site show “Official details”; the rest show “Website & map”, a Google Maps search for the place (website, phone, hours), added by `tools/guides/maplinks.py`. Replace these with official links as each guide is reviewed.
- **Interests (November 2, 2026):** the “What makes a great getaway?” buttons are a uniform grid (5 across on desktop, 3 on tablets, 2 on phones; longer names wrap). Hiking was added and tagged on Asheville, Greenville and Charlottesville.
- **Feedback (November 2, 2026):** hello@wingawayweekends.com is a Cloudflare Email Routing address that forwards to the owner’s Gmail. Every page’s footer has “Help us improve and grow.” with a link to it, directly under the WingAway Weekends name, and each guide’s review note links to it too; each email’s subject names the page. Cloudflare Web Analytics is enabled on the Pages project (Metrics tab).
- **Aircraft profiles (November 1, 2026):** an “Aircraft performance” panel on the homepage, placed right after Departure airport and before flight time and trip length (`docs/aircraft.js`) with example presets (C172S, PA-28-181 Archer, SR22, Bonanza A36, Mooney M20J, TBM 960) and a Custom option. Every field is editable: cruise KTAS, cruise gal/hr, climb/descent/taxi minutes and gallons, usable fuel and reserve (default 45 min). Changes preview on the cards immediately but are only kept when the visitor taps “Save my numbers” (a status line shows unsaved changes); “Use the default estimate” clears the profile. Guides use the saved profile. With a profile, block time = distance ÷ KTAS + allowance; trip fuel = cruise time × gal/hr + allowance gallons; “Fuel stop likely” when trip fuel + reserve exceeds usable fuel. Cards show time and gallons; the flight-time filter uses the profile; guides show time, trip fuel or the fuel-stop warning in the route box. Without a profile, the original 150 KTAS + 15 min model applies and no fuel is shown. Straight-line, no wind; not a flight plan. Possible next steps: winds aloft, a pilot-entered fuel price.
- Every guide has a “Luxury alternatives” row under Where to stay (added November 1, 2026; picks in `tools/guides/luxury.py`, Charleston’s in its build script).
- All twelve cards link to their guides (four rows of three). The whole card is clickable (a stretched link over the card, with a hover lift and keyboard focus ring), not just “Explore destination”.
- Guide links carry the home airport (`?from=KPDK`), and the homepage remembers the last airport used (browser storage). Each guide’s route box then shows the distance and time from that airport, or “Drive instead” within 40 NM. Visitors who never entered an airport see the KMYR figures.
- Trip length also carries into the guides (`&trip=` on card links, and the homepage remembers the last choice). Longer stay relabels the route box “Three nights +” and shows a “With an extra day” plan after the itinerary; Day trip relabels it “Day trip” and shows a “Just for the day” plan above the itinerary. Weekend shows the standard two-night guide.

| Destination | Arrival airport | Photograph in latest review source |
| --- | --- | --- |
| Savannah | KSAV | Forsyth Park fountain |
| Charleston | KCHS | Rainbow Row |
| Asheville | KAVL | Biltmore House mansion |
| Beaufort | KARW | Salt marsh and Intracoastal Waterway |
| St. Augustine | KSGJ | Waterfront/city view from the lighthouse |
| Charlottesville | KCHO | Downtown Mall |
| Greenville | KGMU | Reedy River waterfall and Liberty Bridge |
| Pinehurst | KSOP | Pinehurst No. 4 golf course |
| Nashville | KJWN | Skyline and Cumberland River |
| Key West | KEYW | Duval Street |

### Flight-time behavior

The estimate is great-circle distance in nautical miles divided by 150 knots, plus 0.25 hour. It has no wind, route, terrain, altitude, aircraft-specific climb/descent or ATC adjustment. Filtering uses the unrounded estimate. Card labels show hours and minutes, rounded *up* to the next minute (for example “~3 hr 3 min”), so a label never looks inside a cutoff that excludes the destination.

Nashville uses John C. Tune (KJWN), as requested. Its estimate is about 3.046 hours (label “~3 hr 3 min”): excluded at 2 and 3 hours, included at 3½ hours. The earlier request to include Nashville at 3 hours was superseded by the decision to use KJWN and keep the strict cutoff.

Key West estimates about 4 hours (label “~4 hr 2 min”), so it appears from KMYR only when flight time is set to 4½ hours.

### Savannah guide

The developed guide covers FBO comparisons, arrival/ground transport, hotels, restaurants, attractions and boat outings, spa options, shopping, wine, breweries, sports/events links, a suggested weekend itinerary and practical booking considerations. It contains official-source links and explanatory notes, but no live pricing, availability or booking functionality. Refreshed November 1, 2026: the October 2026 trip dates became a sample Friday–Sunday itinerary; stale spa prices were removed; a note was added that Spa Bleu may be weekday-only, so Saturday appointments need confirming; the unverifiable “Savannah Underground” item was removed; Savannah Steel was updated (UPSHOT League, first season summer 2026); and the flight-time snapshot now uses the discovery page’s model (~1 hr 15 min).

### Charleston guide (draft, added November 1, 2026)

`docs/charleston/` follows the Savannah guide’s structure and styling: KCHS arrival with Atlantic Aviation and Signature, three stays (The Ansonborough, formerly the Ansonborough Inn, replacing Zero George at the user’s request; Wentworth Mansion; The Vendue), plus a “Luxury alternatives” row: The Charleston Place (charlestonplace.com), Hotel Bennett and The Cooper (thecooper.com) (new harborfront hotel, spring 2026; replaced The Dewberry at the owner’s request), FIG (Friday dinner), Rappahannock Oyster Bar (Saturday afternoon happy hour before the sunset sail), Chez Nous (later Saturday dinner) and Husk (Sunday brunch); Rappahannock replaced Leon’s and the slots were swapped at the owner’s request, things to do in the owner’s order (King Street shopping; the Battery, Waterfront Park and Rainbow Row; Patriots Point and the USS Yorktown; Fort Sumter; a foodie walking tour; an evening carriage ride before Friday dinner; Gibbes Museum and Middleton Place removed), Schooner Pride sunset sail, The Spa at The Charleston Place, King Street shopping, wine bars, breweries, RiverDogs / Stingrays / Battery and a sample Friday–Sunday itinerary. The hero uses the existing Rainbow Row card photo (CC0).

Research was done through web search only; the research environment could not open venue websites. Facts confirmed in search results include Patriots Point admission contents and hours, the Fort Sumter ferry departure points and duration, Atlantic Aviation’s CHS address and phone, the Charleston Place spa address and phone, and Schooner Pride’s departure point and sail length. **These official links were written from known domains but not opened, so click-check them:** eatatfig.com (corrected), cheznouschs.com, rroysters.com, huskrestaurant.com, hallschophouse.com, gibbesmuseum.org, middletonplace.org, croghansjewelbox.com, graftchs.com, edmundsoast.com, thevendue.com, wentworthmansion.com, charleston.com/schooner-pride, the Signature CHS page and the Belmond spa page. Signature’s address and phone are omitted because directory listings conflict.

### Asheville guide (draft, added November 1, 2026)

`docs/asheville/` uses the same format. KAVL has one FBO (Signature, 40 Lindbergh Lane, 828-687-7110); the airport is removing some GA hangars for a terminal expansion, so the guide tells pilots to confirm transient parking. The guide recommends a rental car. Picks: Omni Grove Park Inn, The Inn on Biltmore Estate and Kimpton Hotel Arras; Cúrate, Chai Pani and Corner Kitchen; Biltmore Estate and winery; the Western North Carolina Air Museum in Hendersonville (free, limited days); the Blue Ridge Parkway; downtown and the River Arts District; the Grove Park Inn spa; Sierra Nevada in Mills River; and the Asheville Tourists. The guide notes Hurricane Helene recovery: some restaurants (for example Rhubarb) closed permanently, so only places with recent evidence of being open were chosen. Same caveat as Charleston: links were written from known domains but not opened, so click-check them.

### Pinehurst guide (draft, added November 1, 2026)

`docs/pinehurst/` uses the same format. KSOP (Moore County Airport) has one county-run FBO, 910-692-3212, with transient tiedowns, hangars and courtesy cars listed. Ground transport needs arranging ahead because rideshare is scarce. Picks: The Carolina, The Holly Inn and Mid Pines Inn; Villaggio (Friday), Elliotts on Linden (Saturday) and Pinehurst Brewing Co. (lunch); Pinehurst No. 2 (resort guests), The Cradle and Thistle Dhu, the village, downtown Southern Pines, Mid Pines and Pine Needles; The Spa at Pinehurst; The Deuce; Southern Pines Brewing and Railhouse; and the U.S. Open (next in 2029). Several picks have no website link because official addresses could not be confirmed.

### Beaufort, St. Augustine and Greenville guides (drafts, added November 1, 2026)

- **Beaufort photo (November 1, 2026):** the marsh photo was replaced with “Bay Street Downtown Beaufort.JPG” (public domain, 2009), cropped to the storefronts to remove most of the roadway (cropping only, no retouching; some parked cars remain). The homepage card and guide hero use `object-position: 50% 65%` so the storefronts show in wide frames; set per photo with `"pos"` in `destinationPhotos` and `img_style` in the guide builder. License evidence: `licenses/beaufort-bay-street-evidence.json`.
- **Beaufort (`docs/beaufort/`):** KARW is now named Beaufort Executive Airport and runs its own FBO (843-255-2972, courtesy car, shorter weekend hours). Picks: Anchorage 1770, The Rhett House Inn and The Beaufort Inn; Saltus River Grill, Ribaut Social Club and Plums; the historic district and waterfront park, carriage tours, Hunting Island, the Penn Center, the Spanish Moss Trail and the Parris Island Museum (base access rules apply). No spa or brewery picks were verified.
- **St. Augustine (`docs/st-augustine/`):** KSGJ, Atlantic Aviation (904-824-1995) plus self-serve fuel. Picks: Casa Monica (and its spa), The Collector and St. Francis Inn; Collage, The Ice Plant Bar and The Columbia; Castillo de San Marcos, the lighthouse, Flagler College, St. George Street and a Matanzas Bay sunset; San Sebastian Winery and the St. Augustine Distillery; Nights of Lights.
- **Greenville (`docs/greenville/`):** KGMU, Vantage Aviation (formerly Greenville Jet Center, 864-232-7100). Picks: Grand Bohemian Lodge, The Westin Poinsett and Hotel Hartness; Jianna, Scoundrel (Michelin star) and Soby’s; Falls Park, the Swamp Rabbit Trail, Unity Park and Main Street; the Greenville Drive, the Peace Center and Fall for Greenville. No spa section.

### Charlottesville, Nashville and Key West guides (drafts, added November 1, 2026)

- **Charlottesville (`docs/charlottesville/`):** KCHO, Signature (phone listings conflict, so none is shown). Rental car needed. Picks: Keswick Hall, Boar’s Head Resort and Oakhurst Inn; The Alley Light, Oakhart Social and C&O; Monticello, UVA, the Downtown Mall and the Blue Ridge; Barboursville and King Family Vineyards; Foxfield Races.
- **Nashville (`docs/nashville/`):** KJWN, Contour Flight Support (615-350-5000; tower listed 7 AM–9 PM; Atlantic Aviation building a second FBO). Picks: The Hermitage Hotel, Omni Nashville (Mokara Spa) and Germantown Inn; Boqueria (Friday), Locust (Saturday) and Rolf & Daughters as the alternative (changed at the owner’s request); Broadway honky-tonks first, then the Ryman, the Opry, the Country Music Hall of Fame and Germantown; a downtown Shopping section (Fifth + Broadway, Lower Broadway boot shops, Hatch Show Print, The Arcade; Third Man Records nearby); the Predators.
- **Key West (`docs/key-west/`):** KEYW, Signature only (305-296-5422). The guide warns about high fuel and parking fees, the 9 PM closing fee, overwater flying, nearby military airspace and the need for a fuel stop. Picks: The Marquesa, Casa Marina, H2O Suites or Almond Tree; Latitudes, Hot Tin Roof and First Flight (Pan Am’s first ticket office, 301 Whitehead St.); the Dry Tortugas seaplane, Mallory Square and Old Town. Its day-trip plan says plainly that Key West is not a day trip from most of the Southeast.

### Outer Banks and Amelia Island guides (drafts, added November 2, 2026)

- **Outer Banks (`docs/outer-banks/`):** based at KMQI, Dare County Regional (county FBO, 252-475-5575, courtesy and rental cars), at the owner’s request; KFFA at the Wright Brothers National Memorial is offered only as an optional short hop with its caveats (3,000 ft, no fuel, deer, parking limits). Picks: The White Doe Inn, Tranquil House Inn and The Sanderling; 1587, Blue Point and Salt & Cypress; the memorial, Jockey’s Ridge, Manteo’s waterfront, The Lost Colony and Bodie Island Lighthouse. Photo: NASA on The Commons (first-flight boulder and monument), no known copyright restrictions.
- **Amelia Island (`docs/amelia-island/`):** KFHB, Bent Wing Flight Services (904-849-4321, crew car). Picks: The Ritz-Carlton, Omni Amelia Island and Elizabeth Pointe Lodge; David’s, España and Burlingame; Centre Street and the Palace Saloon, Fort Clinch, beach horseback rides and river sunsets. Photo: “Centre Street Businesses” by Upstateherd, CC BY-SA 4.0.
- **Wine destinations (added November 2, 2026), tagged Wine.** Each wine guide has a “Wineries” section and a pilot note on wine and flying (`wine_and_flying()` in `guide_helpers.py`: 14 CFR 91.17's 8 hours and 0.04%, a 12–24 hour personal minimum, taste on the non-flying day). Their hero and card images are **illustrated placeholders** (`*-vineyard-480/960`), drawn by us, until real photos are chosen; `photos.json` marks them `"placeholder": true`.
  - **Yadkin Valley (`docs/yadkin-valley/`, 13):** KZEF Elkin, Yadkin Valley Aviation (336-366-3433, courtesy car, daytime hours). Stay: Elkin Creek Vineyard cabins, The Rockford Inn, Hampton Inn & Suites at Shelton Vineyards. Eat: JOLO, Harvest Grill at Shelton, Elkin Creek pizza. Wineries: Shelton, Raffaldini, JOLO, Jones von Drehle, Elkin Creek, Carolina Heritage. Elkin Vine Line shuttle.
  - **Virginia Hunt Country (`docs/hunt-country/`, 14):** KJYO Leesburg (inside the DC SFRA; Kuhn Jet Center 703-665-3000) with KHWY Warrenton-Fauquier (outside the SFRA; 540-422-8285) as the alternative. Stay: Salamander Middleburg, Red Fox Inn, Goodstone Inn. Eat: Red Fox, The Conservatory at Goodstone, The Inn at Little Washington. Wineries: Boxwood, Cana, Greenhill, 50 West, Chrysalis, Slater Run. Udvar-Hazy Center.
  - **Dahlonega (`docs/dahlonega/`, 15):** KGVL Gainesville, Champion Aviation (770-532-4136; no courtesy car, rent one). Stay: Hall House Hotel, Dahlonega Square Hotel, Dahlonega Resort and Vineyard. Eat: Montaluce, Bourbon Street Grille, Crimson Moon. Wineries: Wolf Mountain, Montaluce, Frogtown, Kaya, Cavender Creek, square tasting rooms. Spa: Mountain Laurel Creek Inn.
  - **Nashville** gained an Arrington Vineyards wine side trip (Things to do #6) and the Wine tag.
- **Alabama and Tennessee guides (added November 2, 2026)**, also with illustrated placeholder images (`gulf-shores-beach`, `chattanooga-river`, `smoky-mountains-ridges`) until photos are chosen:
  - **Gulf Shores (`docs/gulf-shores/`, 16):** KJKA, Gulf Air Center (251-968-5200, crew cars). Stay: The Lodge at Gulf State Park, Turquoise Place, Perdido Beach Resort. Eat: Voyagers, Perch, Doc's Seafood Shack. National Naval Aviation Museum (check base-access rules), Gulf State Park, Fort Morgan. About 3½ hours from KMYR, so it appears with the 3½-hour or longer settings.
  - **Chattanooga (`docs/chattanooga/`, 17):** KCHA (Class C), Wilson Air Center (423-855-2299). Stay: The Edwin, The Read House, The Dwell. Eat: Easy Bistro, St. John's, Calliope. Lookout Mountain, Walnut Street Bridge, Tennessee Aquarium.
  - **Great Smoky Mountains (`docs/smoky-mountains/`, 18):** KGKT Sevierville (865-453-8393; no courtesy car, Enterprise on call); KTYS for Blackberry Farm. Stay: Buckhorn Inn, Old Creek Lodge, Dancing Bear Lodge; luxury Blackberry Farm and Blackberry Mountain. Eat: The Peddler, Dancing Bear Appalachian Bistro, a Cades Cove picnic. Park parking tags required.
- **Lake guides (added November 2, 2026)**, with illustrated placeholders (`lake-lure-gorge`, `lake-jocassee`, `lake-lanier`):
  - **Lake Lure (`docs/lake-lure/`, 19):** KFQD Rutherford County (828-287-0800; courtesy car, daytime hours). Written around Hurricane Helene recovery: lake reopened May 2026 with temporary rules, Chimney Rock State Park reopened 2025, Lake Lure Inn under new owners with renovations through 2026–27. Recheck status when reviewing.
  - **Lake Keowee & Jocassee (`docs/lake-keowee/`, 20):** Photo: Lake Keowee in morning mist by Andy Montgomery, CC BY-SA 2.0, via Wikimedia Commons (`lake-keowee-morning`; Commons file “Lake Keowee (reservoir) in South Carolina.jpg”, 5634 × 2203; cropped from the 3840px Commons rendition). KCEU Clemson (864-882-2959; crew car, Hertz/Enterprise). Lake-house rentals, Devils Fork State Park villas, Fairfield Inn on Keowee; The Lighthouse, Tiki Hut, Copper River Grill; Jocassee waterfall boat tours, Whitewater Falls, Table Rock.
  - **Lake Lanier (`docs/lake-lanier/`, 21):** KGVL (same as Dahlonega; no courtesy car). Lanier Islands Legacy Lodge; Luna's, CHR Steak, Sidney's; pontoon day, Lake Lanier Olympic Park; links to the Dahlonega guide.
- Both photos were supplied by the owner as screenshots of the Commons originals because Commons downloads were rate-limited from the build environment. Builder photo data is in `tools/guides/photos.json`.

### Guide tools

`tools/guides/` (not published) holds the scripts that generate the guide pages: `guide_helpers.py` (shared markup and page template) and `build_<guide>.py` for every guide except Savannah, which is hand-written HTML. After rebuilding a guide, run `python3 tools/guides/personalize.py docs/<guide>/index.html` then `python3 tools/guides/trip_plans.py docs/<guide>/index.html`, then `python3 tools/guides/luxury.py docs/<guide>/index.html`, then `python3 tools/guides/maplinks.py docs/<guide>/index.html`, then `python3 tools/guides/feedback.py docs/<guide>/index.html` to restore the home-airport route box, the trip-length plans the “Luxury alternatives” row, the hotel and restaurant map links and the feedback links (Charleston’s luxury row is in its build script instead). Day-trip and extra-day content for every guide lives in `trip_plans.py`; add an entry there when a new guide is built. Edit the build script rather than the generated HTML, so later rebuilds keep the change.

### Photography and review tools

All ten cards have downloaded destination photographs with recorded commercial reuse licenses. The last update replaced only Asheville, Key West, Pinehurst and Greenville. The other six photo sets were verified byte-for-byte unchanged against the attached source ZIP.

Images use WebP with JPEG fallbacks, responsive `srcset`, descriptive alternative text, lazy loading and asynchronous decoding. All cards have 480px and 960px image versions; the four replacement sets also have 1600px versions. Credits record photographer, title, source links, license requirements, modification notes, file sizes and checksums. ShareAlike photo adaptations retain their source license. None of the four selected replacement licenses was left unverified.

`photo-review.html` shows all ten cards for visual review, intentionally bypassing discovery filtering on that page only. A mobile-review page displays the review in a narrow iframe. These are review tools, not additional destination guides.

## Tech stack

- Buildless static HTML5, CSS and vanilla JavaScript; no application framework, bundler, dependency installation or build step is required for the current package.
- Destination records, interest tags, photograph mappings, distance calculation and DOM rendering are embedded in the discovery HTML.
- Shared `style.css` plus page-specific inline styles.
- Local WebP/JPEG assets and JSON attribution records; Wikimedia Commons supplies the source imagery and file-specific license evidence.
- `docs/airports-southeast.js` holds airport codes, names and coordinates generated from OurAirports (public domain): land airports with a K-prefixed ICAO code or a 3-character FAA ID, which leaves out most private strips.
- Cloudflare Pages hosts the static site from `docs/` on `main` (no build step). GitHub Pages can serve the same folder as a backup; `docs/.nojekyll` makes it serve the files as-is.
- Source is managed in Git on GitHub. The ChatGPT `.openai/hosting.json` manifest was not carried over and is no longer needed.
- Python/Pillow were used as development tools for image resizing/conversion and archive checks. They are not browser runtime dependencies.
- No application backend, database, user accounts, payments, saved trips, live aviation data, booking API or ForeFlight integration is implemented. The hosting access gate is separate from application functionality.

## File structure

| Path | Purpose |
| --- | --- |
| `README.md` | Repository overview and local preview instructions |
| `PROJECT_NOTES.md` | This document |
| `PACKAGE_HISTORY.md` | README of the final ChatGPT package, kept for history |
| `VALIDATION.md` | Checks documented for the four-photo replacement package |
| `PHOTO_CREDITS.md` | Human-readable sources, photographers, licenses and requirements |
| `PHOTO_CREDITS.json` | Detailed attribution and image-file records |
| `licenses/commons-imageinfo-evidence.json` | Commons evidence for the six original photos |
| `licenses/replacement-imageinfo-evidence.json` | File-specific evidence for the four replacements |
| `docs/index.html` | Discovery homepage, destination data, filters and rendering logic |
| `docs/style.css` | Shared site styling |
| `docs/airports-southeast.js` | Southeast departure airports (OurAirports data) |
| `docs/savannah/index.html` | Savannah destination guide |
| `docs/savannah.jpg` | Hero/guide photograph |
| `docs/charleston/index.html` | Charleston destination guide (draft) |
| `docs/asheville/index.html` | Asheville destination guide (draft) |
| `docs/pinehurst/index.html` | Pinehurst destination guide (draft) |
| `docs/beaufort/`, `docs/st-augustine/`, `docs/greenville/`, `docs/charlottesville/`, `docs/nashville/`, `docs/key-west/` | Destination guides (drafts) |
| `docs/guide-route.js` | Personalizes each guide’s route box for the visitor’s home airport |
| `tools/guides/` | Guide build scripts (not published) |
| `docs/sitemap.xml`, `docs/robots.txt` | Search-engine sitemap and crawl rules (review pages excluded). Add new guide URLs to the sitemap. |
| `docs/assets/destinations/` | Destination images (WebP + JPEG, 480/960 and some 1600px) |
| `docs/photo-credits.json` | Attribution records served by the website |
| `docs/photo-review.html` | All-ten visual review (bypasses filters) |
| `docs/mobile-review.html` | Narrow iframe for mobile layout inspection |

To preview locally, open `docs/index.html` in a browser or run `python3 -m http.server -d docs`.

## Open issues and limitations

1. ~~Latest photos are not live.~~ Resolved November 1, 2026: photos approved and published on GitHub Pages.
2. **All ten guides are drafts.** They need a read-through and link check before the “Draft for review” labels come off.
3. **Departure airports cover the Southeast only.** NC, SC, GA, FL, VA, TN and AL as of November 1, 2026. Expanding means regenerating `docs/airports-southeast.js` with more states. Destination guides still show KMYR-based route snapshots.
4. ~~Trip length is inactive.~~ Resolved November 1, 2026: it now sets the flight-time options.
5. ~~Time labels can obscure cutoff behavior.~~ Resolved November 1, 2026: labels now show hours and minutes, rounded up (Nashville “~3 hr 3 min”). The filter is unchanged.
6. ~~Key West is beyond the selector range.~~ Resolved November 1, 2026: every trip length now offers up to 4½ hours, which includes Key West.
7. ~~Savannah content needs refresh.~~ Refreshed November 1, 2026. The Charleston draft’s links still need a click-check (see the Charleston guide section).
8. **Pinehurst imagery is archival.** The chosen sharp golf photograph dates to 2010 and should not be treated as a current course-layout reference.
9. **Review and homepage code are duplicated.** A future cleanup could share destination data and rendering to reduce drift, while preserving the simple static architecture.
10. **No live planning or commerce.** Weather, NOTAMs, fuel prices, hotel rates, events availability, reservations, ticket purchases and operational flight plans are not supplied.
11. **Photos approved; testing is limited.** Browser inspection confirmed that all ten images loaded. Local image links, JavaScript syntax, unchanged feature logic and preservation checks passed; comprehensive accessibility and cross-device testing is not documented for the latest package.
12. **Verify after publishing.** Under ChatGPT hosting, an earlier archive once served the Savannah guide as the home page. After each merge, check the live homepage and `/savannah/` rather than assuming the deploy worked.

## Recommended next steps

1. Click-check the Charleston and Asheville guide links and review the picks with Ross and Diana.
1a. Google Search Console is verified (Domain property) and indexing was requested November 1, 2026. Check the Sitemaps report occasionally.
2. Choose the next full guide only after the first two are reviewed, without expanding beyond the curated MVP prematurely.
3a. Test the experience with Ross, Diana and a small pilot/couples group; use their feedback to judge destination appeal and ease of choosing a getaway.
4. Consider sharing destination data between `index.html` and `photo-review.html` to stop the two drifting apart.
5. Keep this document current as decisions are made.

## History of these notes

Originally written in ChatGPT from the final package `WingAwayWeekends_Four_Photos_Replaced.zip` and the conversation history there. Revised in Claude on November 1, 2026, after the files moved to GitHub, the site was tested in a browser and published on GitHub Pages, the flight-time labels were changed, trip length was activated, Asheville was tagged for aviation museums, Southeast departure airports were added, the site moved to wingawayweekends.com on Cloudflare Pages, the Asheville, Pinehurst, Beaufort, St. Augustine and Greenville guides, home-airport route boxes and search-engine files were added, Google Search Console was verified and the sitemap submitted, the Charleston guide was drafted and the Savannah guide was refreshed.

## Fly to lunch: the $100 hamburger (`docs/fly-to-lunch/`, added November 2, 2026)

A standalone page listing Southeast airports with a well-reviewed restaurant on the field, a short walk away or a short ride away. The `SPOTS` array in the page's own script holds each entry (`code`, `name`, `where`, `meals`, `food`, `desc`, `pilot`, `phone`, `checked`; `lat`/`lon`/`city` only for strips not in `airports-southeast.js`). The page sorts by distance from the home airport (`?from=`, then `wingaway-home`, then KMYR), filters by maximum one-way flight time (default 1½ hours) and meal, uses the saved aircraft profile for times and round-trip fuel, and shows "drive instead" under 40 NM. The homepage links to it with a navy "Short hops" banner between the search filters and "Worth the flight", and every page has a "Fly to lunch" header link (added by `feedback.py`, which also adds it to rebuilt guides; on phones the small header label is hidden to make room). The Fly to lunch page itself is not run through `feedback.py`. Edit the HTML directly; there is no build script.

Entries (16): Pik N Pig (BQ1, formerly 5NC3), Low and Slow Smokehouse (KJNX), Howard's Pub (KW95), Hangar 28 Kitchen & Events (KGMU; replaced Runway Café, July 2026), Hunter-Gatherer Hangar (KCUB), Stanton's BBQ (private strip near Bennettsville), Beacon Drive-In (KSPA), Skull Creek Boathouse (KHXD), Barnstormer's Grill (GA2), Southern Soul BBQ (KSSI), Simply Suzanne's (KMTV), Charly's (KJGG), Lorraine's (KTGI), Airport Restaurant & Gin Mill (KDED), The Hangar (KSPG), Jet Runway Café (KFXE). Left out for now because recent status was unclear: 57 Alpha Café (KFQD; longtime chef left), Crosswind Café (KHKY; possibly closed), The Downwind (KPDK), Pyper Kub (X60), High Jackers/Landing Strip Tavern (KFIN), The Flying Machine (KLZU; mixed reviews). Airport restaurants change often; recheck entries periodically.

**Interest buttons (November 2, 2026):** 12 buttons in rows of four on desktop (three on tablets, two on phones): Boutique stays, Dining, Wine, Spa, History, Outdoors, Hiking, Beach, Lake, Scenic views, Golf, Aviation museums. Romance was removed as a button when Lake was added (it matched nearly every destination, since every guide is a couples getaway); the Romance tags remain in the data, so it can be restored by adding it back to `interests`. Beach: Beaufort, St. Augustine, Outer Banks, Amelia Island, Gulf Shores, Key West. Scenic views: Asheville, Charlottesville, Greenville, Yadkin Valley, Virginia Hunt Country, Dahlonega, Chattanooga, Great Smoky Mountains, Key West. Lake: Lake Lure, Lake Keowee & Jocassee, Lake Lanier.

**FBO details (November 2, 2026):** every guide's FBO box shows the FBO name, full street address and phone (plus an "FBO details" link where one is confirmed). Addresses came from FAA/AirNav/AcuKwik-style listings; Wilson Air Center's (932 Jubilee Drive, Chattanooga) came from a single directory and is worth confirming. Hunt Country's two FBOs carry their airport IDs in the name (KJYO, KHWY).
