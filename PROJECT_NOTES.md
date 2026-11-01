# WingAway Weekends — Project Notes

Updated: November 1, 2026.

## Goals and agreed direction

WingAway Weekends helps general aviation pilots and their travel companions discover worthwhile short getaways. The experience connects an appealing destination with practical arrival, lodging, dining and activity information, with an initial emphasis on couples.

The agreed MVP is a curated discovery homepage with 5–10 handpicked destinations from KMYR and only 1–2 developed guides. The current source contains ten destination cards and one developed guide, Savannah. Automatic recommendations for every airport are outside the current MVP.

The design uses navy, cream and gold, an aspirational destination hero photograph, the headline “Where will your wings take you this weekend?”, prominent airport and flight-time controls, and destination cards. ForeFlight remains the pilot’s operational flight-planning tool; WingAway provides destination discovery rather than weather, routing or dispatch decisions.

## Current source and publication status

- Latest completed review package in this conversation: `WingAwayWeekends_Four_Photos_Replaced.zip`.
- Package link: https://chatgpt.com/library?file_id=libfile_da2559eb2d9081918c21a22800cb2818&account_id=personal
- This package was made from the user-supplied `WingAwayWeekends_Photos_Fixed_Review.zip` and contains actual modified website files.
- Existing website: https://wingaway-savannah.ramorganmd.chatgpt.site
- Hosting project ID: `appgprj_6abe9d437ef8819196353f64245055a8`.
- Hosting configuration: static files served from `dist`.
- Last deployment confirmed in this conversation: version 7, containing the discovery homepage and Nashville using KJWN. Hosting state has not been rechecked for this notes document.
- The ten-photo work and subsequent four-photo replacements were prepared for review and have **not been published**. The latest review ZIP is ahead of the last confirmed live version.
- Keep the existing project ID, website address, sharing access and Savannah guide. Do not create another site. Publication requires a new user instruction because the latest requested work explicitly said not to publish.

## Features built

### Discovery homepage

- Responsive hero and destination-card grid, with layouts for desktop, tablet and mobile.
- Departure airport input; calculations currently support KMYR only. Other entries show an explanatory empty state.
- Maximum estimated flight-time options: 2, 3 and 3½ hours.
- Interest checkboxes: Romance, Boutique stays, Spa, Dining, Wine, History, Outdoors and Golf.
- Multiple selected interests use AND matching: a destination must have every selected tag.
- Live result count and an empty-state message when nothing matches.
- A trip-length selector offers Weekend, Day trip and Longer stay, but does not change results yet.
- Savannah links to its guide. The other nine cards display “Guide coming soon.”

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

The estimate is great-circle distance in nautical miles divided by 150 knots, plus 0.25 hour. It has no wind, route, terrain, altitude, aircraft-specific climb/descent or ATC adjustment. Filtering uses the unrounded estimate; card labels round to one decimal place.

Nashville uses John C. Tune (KJWN), as requested. Its estimate is about 3.046 hours: excluded at 2 and 3 hours, included at 3½ hours. The earlier request to include Nashville at 3 hours was superseded by the decision to use KJWN and keep the strict cutoff.

Key West estimates about 4 hours and therefore does not appear under any current maximum-time option. It remains in the destination data and appears on the all-ten photo-review page.

### Savannah guide

The developed guide covers FBO comparisons, arrival/ground transport, hotels, restaurants, attractions and boat outings, spa options, shopping, wine, breweries, sports/events links, a suggested weekend itinerary and practical booking considerations. It contains official-source links and explanatory notes, but no live pricing, availability or booking functionality. It was preserved through the photo updates.

### Photography and review tools

All ten cards have downloaded destination photographs with recorded commercial reuse licenses. The last update replaced only Asheville, Key West, Pinehurst and Greenville. The other six photo sets were verified byte-for-byte unchanged against the attached source ZIP.

Images use WebP with JPEG fallbacks, responsive `srcset`, descriptive alternative text, lazy loading and asynchronous decoding. All cards have 480px and 960px image versions; the four replacement sets also have 1600px versions. Credits record photographer, title, source links, license requirements, modification notes, file sizes and checksums. ShareAlike photo adaptations retain their source license. None of the four selected replacement licenses was left unverified.

`photo-review.html` shows all ten cards for visual review, intentionally bypassing discovery filtering on that page only. A mobile-review page displays the review in a narrow iframe. These are review tools, not additional destination guides.

## Tech stack

- Buildless static HTML5, CSS and vanilla JavaScript; no application framework, bundler, dependency installation or build step is required for the current package.
- Destination records, interest tags, photograph mappings, distance calculation and DOM rendering are embedded in the discovery HTML.
- Shared `style.css` plus page-specific inline styles.
- Local WebP/JPEG assets and JSON attribution records; Wikimedia Commons supplies the source imagery and file-specific license evidence.
- ChatGPT Sites hosts the existing static site. `.openai/hosting.json` retains its identity and document-root configuration.
- The existing hosted source workflow uses Git and deployment archives. The latest review ZIP is a portable source snapshot, not a Git checkout, and has not been pushed or deployed.
- Python/Pillow were used as development tools for image resizing/conversion and archive checks. They are not browser runtime dependencies.
- No application backend, database, user accounts, payments, saved trips, live aviation data, booking API or ForeFlight integration is implemented. The hosting access gate is separate from application functionality.

## File structure of the latest review ZIP

| Path | Purpose |
| --- | --- |
| `.openai/hosting.json` | Existing project ID and static directory configuration |
| `README.md` | Package status, opening instructions and scope |
| `VALIDATION.md` | Checks documented for the replacement package |
| `photo-review.html` | Convenience entry point redirecting to the review inside `dist` |
| `PHOTO_CREDITS.md` | Human-readable sources, photographers, licenses and requirements |
| `PHOTO_CREDITS.json` | Detailed attribution and image-file records |
| `licenses/commons-imageinfo-evidence.json` | Earlier Commons evidence, retained for provenance and the six unchanged photos |
| `licenses/replacement-imageinfo-evidence.json` | Current file-specific evidence for the four replacements |
| `dist/index.html` | Actual discovery homepage, data, filters and rendering logic |
| `dist/style.css` | Shared site styling |
| `dist/savannah/index.html` | Existing Savannah destination guide |
| `dist/savannah.jpg` | Existing hero/guide photograph, preserved |
| `dist/assets/destinations/` | 48 image files: six destinations × four variants, plus four replacements × six variants |
| `dist/photo-credits.json` | Attribution records accessible from the website |
| `dist/photo-review.html` | All-ten visual review with updated photographs and credits |
| `dist/mobile-review.html` | Narrow iframe for mobile layout inspection |

Extract the whole ZIP before opening `photo-review.html`; the pages depend on the adjacent asset folders. The local preview works best on a desktop browser or static server. iPhone file previews may not execute the complete HTML experience reliably.

## Open issues and limitations

1. **Latest photos are not live.** Review and publication are still outstanding.
2. **Only one developed guide.** Nine cards remain editorial summaries with no detailed guide.
3. **Departure airport is limited to KMYR.** The editable field does not support arbitrary airports yet.
4. **Trip length is inactive.** It is displayed but has no effect on matching.
5. **Time labels can obscure cutoff behavior.** Nashville displays approximately “3 hr” while being excluded at the strict 3-hour cutoff. A minutes-based label or clearer rounding would help without changing the agreed filter.
6. **Key West is beyond the selector range.** Decide whether to offer a longer flight-time option or keep it solely for later expansion; do not silently alter the current limits.
7. **Savannah content needs refresh.** The guide includes October 2026 trip dates, older verification dates and example spa pricing. It needs editorial revalidation before broader use.
8. **Pinehurst imagery is archival.** The chosen sharp golf photograph dates to 2010 and should not be treated as a current course-layout reference.
9. **Review and homepage code are duplicated.** A future cleanup could share destination data and rendering to reduce drift, while preserving the simple static architecture.
10. **No live planning or commerce.** Weather, NOTAMs, fuel prices, hotel rates, events availability, reservations, ticket purchases and operational flight plans are not supplied.
11. **Photo approval remains pending.** Browser inspection confirmed that all ten images loaded. Local image links, JavaScript syntax, unchanged feature logic and preservation checks passed; comprehensive accessibility and cross-device testing is not documented for the latest package.
12. **Prior deployment mismatch.** An earlier archive accidentally retained the Savannah guide as the root page. That was corrected in version 5 and the published root/guide routes were directly verified. Future publication should inspect the actual deployment archive and verify the live homepage, not rely solely on a successful deployment status.

## Recommended next steps

1. Review the latest ZIP’s all-ten photo preview and approve or request specific visual changes.
2. Resolve the flight-time label and Key West range questions; decide whether to activate or simplify trip-length selection.
3. Refresh the Savannah guide’s dates, prices and source checks. Choose the next full guide without expanding beyond the curated MVP prematurely.
4. Once the user authorizes publication, open the existing project’s current source, reconcile the approved review files with any newer work, preserve its manifest/access settings, check the deployment archive, then publish to the same address.
5. Verify the live discovery headline, all image files, Nashville cutoff behavior, interest filtering and `/savannah/` after publication.
6. Test the experience with Ross, Diana and a small pilot/couples group; use their feedback to judge destination appeal and ease of choosing a getaway.
7. Maintain one current source package and this project summary. Treat older ZIPs and chats as history, not competing implementation baselines.

## Evidence used for these notes

The current local copy of `WingAwayWeekends_Four_Photos_Replaced.zip`, its README/validation records, actual discovery HTML, Savannah guide, hosting configuration, photo-credit records and file listing were inspected. Its Library identity was confirmed against the saved package. Project decisions and deployment history come from this conversation. This notes task does not modify or publish the website.
