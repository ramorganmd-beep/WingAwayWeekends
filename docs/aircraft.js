// Aircraft performance profiles for WingAway Weekends.
// A profile is saved in the visitor's browser (localStorage) and used by the
// homepage cards and the destination guides to estimate block time, trip fuel
// and whether a fuel stop is likely. Straight-line, no-wind planning estimates
// only; preset numbers are typical examples, not POH values.
(function () {
  var KEY = 'wingaway-aircraft';

  // [id, label, cruise KTAS, cruise gal/hr, allowance minutes, allowance gallons, usable gal, reserve minutes]
  var PRESETS = [
    ['c172', 'Cessna 172S Skyhawk', 122, 8.5, 15, 2, 53, 45],
    ['pa28', 'Piper PA-28-181 Archer', 125, 10, 15, 2, 48, 45],
    ['sr22', 'Cirrus SR22', 175, 16.5, 15, 3, 92, 45],
    ['a36', 'Beechcraft Bonanza A36', 165, 15, 15, 3, 74, 45],
    ['m20j', 'Mooney M20J 201', 150, 9.5, 15, 2, 64, 45],
    ['tbm960', 'Daher TBM 960 (Jet A)', 300, 55, 20, 15, 291, 45]
  ].map(function (p) {
    return { id: p[0], label: p[1], tas: p[2], gph: p[3], allowMin: p[4], allowGal: p[5], usable: p[6], reserve: p[7] };
  });

  var FIELDS = ['tas', 'gph', 'allowMin', 'allowGal', 'usable', 'reserve'];

  function valid(p) {
    if (!p || typeof p !== 'object') return null;
    var out = { id: String(p.id || 'custom'), label: String(p.label || 'Custom aircraft').slice(0, 60) };
    for (var i = 0; i < FIELDS.length; i++) {
      var v = Number(p[FIELDS[i]]);
      if (!isFinite(v) || v < 0) return null;
      out[FIELDS[i]] = v;
    }
    if (out.tas < 40 || out.tas > 600 || out.gph <= 0 || out.usable <= 0) return null;
    return out;
  }

  function load() {
    try { return valid(JSON.parse(localStorage.getItem(KEY) || 'null')); } catch (e) { return null; }
  }

  function save(p) {
    var v = valid(p);
    try { if (v) localStorage.setItem(KEY, JSON.stringify(v)); else localStorage.removeItem(KEY); } catch (e) {}
    return v;
  }

  // Default model used before a profile is entered: 150 KTAS plus 15 minutes, no fuel.
  function estimate(nm, p) {
    if (!p) return { hours: nm / 150 + 0.25, gal: null, needed: null, stop: false };
    var cruiseH = nm / p.tas;
    var gal = cruiseH * p.gph + p.allowGal;
    var needed = gal + (p.reserve / 60) * p.gph;
    return { hours: cruiseH + p.allowMin / 60, gal: gal, needed: needed, stop: needed > p.usable };
  }

  function formatTime(hours) {
    var mins = Math.ceil(hours * 60), h = Math.floor(mins / 60), m = mins % 60;
    return h ? h + ' hr' + (m ? ' ' + m + ' min' : '') : m + ' min';
  }

  function summary(p) {
    return p ? p.label + ' · ' + p.tas + ' kt · ' + p.gph + ' gal/hr' : 'Default estimate · 150 kt, no fuel';
  }

  window.WingAwayAircraft = { PRESETS: PRESETS, FIELDS: FIELDS, valid: valid, load: load, save: save, estimate: estimate, formatTime: formatTime, summary: summary };
})();
