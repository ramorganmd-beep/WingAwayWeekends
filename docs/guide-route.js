// Personalizes a destination guide's route box for the visitor's home airport.
// Home airport comes from ?from=CODE (set by the homepage cards) or the last
// airport used on the homepage (localStorage). Falls back to the page's
// built-in KMYR figures when nothing is known.
(function () {
  var box = document.querySelector('.snapshot[data-dest]');
  var airports = window.WINGAWAY_AIRPORTS;
  if (!box || !airports) return;

  var index = new Map();
  airports.forEach(function (a) {
    index.set(a[0], a);
    if (a[1]) index.set(a[1], a);
    if (/^K[A-Z0-9]{3}$/.test(a[0]) && !index.has(a[0].slice(1))) index.set(a[0].slice(1), a);
  });

  var fromLink = '', saved = '';
  try { fromLink = (new URLSearchParams(location.search).get('from') || '').trim().toUpperCase(); } catch (e) {}
  try { saved = localStorage.getItem('wingaway-home') || ''; } catch (e) {}
  var home = (fromLink && index.get(fromLink)) || (saved && index.get(saved));
  if (!home) return;
  try { localStorage.setItem('wingaway-home', home[0]); } catch (e) {}

  var destCode = box.dataset.dest;
  var lat = Number(box.dataset.lat), lon = Number(box.dataset.lon);
  var rad = function (x) { return x * Math.PI / 180; };
  var dLat = rad(lat - home[5]), dLon = rad(lon - home[6]);
  var h = Math.sin(dLat / 2) * Math.sin(dLat / 2) + Math.cos(rad(home[5])) * Math.cos(rad(lat)) * Math.sin(dLon / 2) * Math.sin(dLon / 2);
  var nm = 3440.065 * 2 * Math.asin(Math.sqrt(h));
  var mins = Math.ceil((nm / 150 + 0.25) * 60), hr = Math.floor(mins / 60), mn = mins % 60;

  var route = box.querySelector('[data-route]'), dist = box.querySelector('[data-dist]'), time = box.querySelector('[data-time]');
  route.innerHTML = '';
  route.append(home[0] + ' ');
  var to = document.createElement('span'); to.className = 'route-line'; to.textContent = 'to';
  route.append(to, ' ' + destCode);

  var note = document.getElementById('route-note');
  if (home[0] === destCode || nm < 40) {
    dist.innerHTML = '~' + Math.round(nm) + ' <small>NM</small>';
    time.innerHTML = 'Drive <small>instead</small>';
    note.textContent = 'You’re based at or near ' + destCode + ', so this one is a drive, not a flight. ';
  } else {
    dist.innerHTML = '~' + Math.round(nm) + ' <small>NM</small>';
    time.innerHTML = hr ? '~' + hr + ' hr' + (mn ? ' ' + mn + ' <small>min</small>' : '') : '~' + mn + ' <small>min</small>';
    note.textContent = 'Showing your route from ' + home[0] + ' · ' + home[2] + ', ' + home[3] + ', ' + home[4] + '. ';
  }
  var change = document.createElement('a');
  change.href = '../'; change.textContent = 'Change home airport';
  note.append(change);
  note.hidden = false;
})();
