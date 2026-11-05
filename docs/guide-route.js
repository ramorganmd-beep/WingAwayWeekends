// Personalizes a destination guide's route box for the visitor's home airport.
// Home airport comes from ?from=CODE (set by the homepage cards) or the last
// airport used on the homepage (localStorage). Falls back to the page's
// built-in KMYR figures when nothing is known.
// Trip length (Weekend / Day trip / Longer stay) from ?trip=... or the
// homepage's last choice: relabels the route box and shows the matching plan.
(function () {
  var trip = '';
  try { trip = new URLSearchParams(location.search).get('trip') || ''; } catch (e) {}
  if (!trip) { try { trip = localStorage.getItem('wingaway-trip') || ''; } catch (e) {} }
  if (trip !== 'Day trip' && trip !== 'Longer stay') return;
  var style = document.querySelector('[data-style]');
  if (style) {
    var small = document.createElement('small');
    small.textContent = '· ' + style.dataset.transport;
    style.textContent = (trip === 'Day trip' ? 'Day trip' : 'Three nights +') + ' ';
    style.append(small);
  }
  var plan = document.querySelector('.trip-plan[data-trip="' + trip + '"]');
  if (plan) plan.hidden = false;
})();

(function () {
  var box = document.querySelector('.snapshot[data-dest]');
  var airports = window.WINGAWAY_AIRPORTS;
  if (!box || !airports) return;

  var index = new Map();
  airports.forEach(function (a) {
    index.set(a[0], a);
    if (a[1]) index.set(a[1], a);
    if (/^K[A-Z0-9]{3}$/.test(a[0]) && !index.has(a[0].slice(1))) index.set(a[0].slice(1), a);
    if (/^[A-Z0-9]{3}$/.test(a[0]) && !index.has('K' + a[0])) index.set('K' + a[0], a);
  });

  var fromLink = '', saved = '';
  try { fromLink = (new URLSearchParams(location.search).get('from') || '').trim().toUpperCase(); } catch (e) {}
  try { saved = localStorage.getItem('wingaway-home') || ''; } catch (e) {}
  var home = (fromLink && index.get(fromLink)) || (saved && index.get(saved));
  var aircraft = window.WingAwayAircraft ? window.WingAwayAircraft.load() : null;
  if (!home && !aircraft) return;
  if (home) { try { localStorage.setItem('wingaway-home', home[0]); } catch (e) {} }
  var homeKnown = !!home;
  home = home || index.get('KMYR');
  if (!home) return;

  var destCode = box.dataset.dest;
  var lat = Number(box.dataset.lat), lon = Number(box.dataset.lon);
  var rad = function (x) { return x * Math.PI / 180; };
  var dLat = rad(lat - home[5]), dLon = rad(lon - home[6]);
  var h = Math.sin(dLat / 2) * Math.sin(dLat / 2) + Math.cos(rad(home[5])) * Math.cos(rad(lat)) * Math.sin(dLon / 2) * Math.sin(dLon / 2);
  var nm = 3440.065 * 2 * Math.asin(Math.sqrt(h));
  var est = window.WingAwayAircraft ? window.WingAwayAircraft.estimate(nm, aircraft) : { hours: nm / 150 + 0.25 };
  var mins = Math.ceil(est.hours * 60), hr = Math.floor(mins / 60), mn = mins % 60;

  var route = box.querySelector('[data-route]'), dist = box.querySelector('[data-dist]'), time = box.querySelector('[data-time]');
  route.innerHTML = '';
  route.append(home[0] + ' ');
  var to = document.createElement('span'); to.className = 'route-line'; to.textContent = 'to';
  route.append(to, ' ' + destCode);
  dist.innerHTML = '~' + Math.round(nm) + ' <small>NM</small>';

  var note = document.getElementById('route-note');
  note.textContent = '';
  if (home[0] === destCode || nm < 40) {
    time.innerHTML = 'Drive <small>instead</small>';
    note.append('You’re based at or near ' + destCode + ', so this one is a drive, not a flight. ');
  } else {
    time.innerHTML = hr ? '~' + hr + ' hr' + (mn ? ' ' + mn + ' <small>min</small>' : '') : '~' + mn + ' <small>min</small>';
    if (homeKnown) note.append('Showing your route from ' + home[0] + ' · ' + home[2] + ', ' + home[3] + ', ' + home[4] + '. ');
    if (aircraft) {
      var fuel = document.createElement('strong');
      fuel.textContent = est.stop
        ? 'Fuel stop likely: about ' + Math.ceil(est.needed) + ' gal needed with your ' + aircraft.reserve + '-min reserve vs ' + aircraft.usable + ' gal usable. '
        : 'About ' + Math.ceil(est.gal) + ' gal for the trip, nonstop with your ' + aircraft.reserve + '-min reserve. ';
      note.append('Your ' + aircraft.label + ' profile (' + aircraft.tas + ' kt, ' + aircraft.gph + ' gal/hr): ', fuel, 'No wind; not a flight plan. ');
    }
  }
  var change = document.createElement('a');
  change.href = '../'; change.textContent = 'Change airport or aircraft';
  note.append(change);
  note.hidden = false;
})();

// Seaplane access boxes show only for floatplane/amphibian pilots (landing gear saved on the homepage).
(function () {
  var gear = 'land';
  try { gear = window.WingAwayAircraft && window.WingAwayAircraft.loadGear ? window.WingAwayAircraft.loadGear() : 'land'; } catch (e) {}
  var water = gear === 'float' || gear === 'amphib';
  Array.prototype.forEach.call(document.querySelectorAll('[data-water]'), function (box) { box.hidden = !water; });
  Array.prototype.forEach.call(document.querySelectorAll('[data-water-toggle]'), function (t) {
    t.hidden = water;
    var b = t.querySelector('button');
    if (b) b.addEventListener('click', function () {
      Array.prototype.forEach.call(document.querySelectorAll('[data-water]'), function (box) { box.hidden = false; });
      t.hidden = true;
    });
  });
})();
