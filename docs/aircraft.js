// Aircraft performance profiles for WingAway Weekends.
// A profile is saved in the visitor's browser (localStorage) and used by the
// homepage cards and the destination guides to estimate block time, trip fuel
// and whether a fuel stop is likely. Straight-line, no-wind planning estimates
// only; preset numbers are typical examples, not POH values.
(function () {
  var KEY = 'wingaway-aircraft';

  // [id, label, cruise KTAS, cruise gal/hr, allowance minutes, allowance gallons, usable gal, reserve minutes, gear]
  // gear: 'land' (wheels), 'float' (water only) or 'amphib' (water or runway).
  var PRESETS = [
    ['c172', 'Cessna 172S Skyhawk', 122, 8.5, 15, 2, 53, 45, 'land'],
    ['pa28', 'Piper PA-28-181 Archer', 125, 10, 15, 2, 48, 45, 'land'],
    ['sr20', 'Cirrus SR20', 155, 11, 15, 2, 56, 45, 'land'],
    ['sr22', 'Cirrus SR22', 175, 16.5, 15, 3, 92, 45, 'land'],
    ['sr22t', 'Cirrus SR22T', 190, 18, 15, 3, 92, 45, 'land'],
    ['sf50', 'Cirrus Vision Jet SF50 (Jet A)', 300, 60, 20, 15, 296, 45, 'land'],
    ['a36', 'Beechcraft Bonanza A36', 165, 15, 15, 3, 74, 45, 'land'],
    ['m20j', 'Mooney M20J 201', 150, 9.5, 15, 2, 64, 45, 'land'],
    ['tbm960', 'Daher TBM 960 (Jet A)', 300, 55, 20, 15, 291, 45, 'land'],
    ['pa18f', 'Piper PA-18 Super Cub on floats', 85, 9, 15, 2, 36, 45, 'float'],
    ['c172f', 'Cessna 172 on floats', 100, 8.5, 15, 2, 53, 45, 'float'],
    ['a1cf', 'Aviat Husky A-1C on floats', 100, 9, 15, 2, 50, 45, 'float'],
    ['c185f', 'Cessna 185 on floats', 125, 14, 15, 2, 84, 45, 'float'],
    ['c206a', 'Cessna 206 on amphibious floats', 130, 15, 15, 3, 84, 45, 'amphib'],
    ['la4', 'Lake LA-4-200 Buccaneer (amphibian)', 125, 11, 15, 2, 54, 45, 'amphib'],
    ['icona5', 'ICON A5 (amphibian)', 84, 4.5, 10, 1, 20, 45, 'amphib'],
    ['searey', 'Progressive Aerodyne SeaRey (amphibian)', 85, 5, 10, 1, 25, 45, 'amphib']
  ].map(function (p) {
    return { id: p[0], label: p[1], tas: p[2], gph: p[3], allowMin: p[4], allowGal: p[5], usable: p[6], reserve: p[7], gear: p[8] };
  });

  // Temporary: show only Cirrus models in the aircraft menus (Cirrus presentation).
  // Set to false to bring back the full list.
  var CIRRUS_ONLY = true;
  if (CIRRUS_ONLY) PRESETS = PRESETS.filter(function (p) { return /^Cirrus/.test(p.label); });

  var GEARS = { land: 'Landplane', float: 'Floatplane', amphib: 'Amphibian' };
  var GEAR_KEY = 'wingaway-gear';

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
    if (GEARS[p.gear]) out.gear = p.gear;
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

  // Landing gear is kept separately so it also works with the default estimate.
  function loadGear() {
    if (CIRRUS_ONLY) return 'land';
    try { var g = localStorage.getItem(GEAR_KEY); return GEARS[g] ? g : 'land'; } catch (e) { return 'land'; }
  }

  function saveGear(g) {
    if (!GEARS[g]) g = 'land';
    try { if (g === 'land') localStorage.removeItem(GEAR_KEY); else localStorage.setItem(GEAR_KEY, g); } catch (e) {}
    return g;
  }

  // Crosswind limit (knots) for the weather outlook. Kept apart from the performance profile so it also
  // works with the default estimate. A pilot's own limit, not a POH value.
  var XWIND_KEY = 'wingaway-xwind', XWIND_DEFAULT = 15;
  function loadXwind() {
    try { var v = Number(localStorage.getItem(XWIND_KEY)); return v >= 3 && v <= 50 ? v : XWIND_DEFAULT; } catch (e) { return XWIND_DEFAULT; }
  }
  function saveXwind(v) {
    v = Math.round(Number(v));
    if (!(v >= 3 && v <= 50)) v = XWIND_DEFAULT;
    try { if (v === XWIND_DEFAULT) localStorage.removeItem(XWIND_KEY); else localStorage.setItem(XWIND_KEY, String(v)); } catch (e) {}
    return v;
  }

  window.WingAwayAircraft = { XWIND_DEFAULT: XWIND_DEFAULT, loadXwind: loadXwind, saveXwind: saveXwind, CIRRUS_ONLY: CIRRUS_ONLY, PRESETS: PRESETS, FIELDS: FIELDS, GEARS: GEARS, valid: valid, load: load, save: save, loadGear: loadGear, saveGear: saveGear, estimate: estimate, formatTime: formatTime, summary: summary };
})();
