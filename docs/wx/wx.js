// WingAway Weekends weather outlook (preview).
// Reads NOAA National Blend of Models station guidance (data/run.json + data/st/<bucket>.json, made by
// tools/wx/nbm.py) and FAA runway headings (runways.js, made by tools/wx/runways_wx.py). For each departure
// time in a window around the planned one, it checks the departure airport at take-off and the arrival
// airport at the estimated landing time: flight category, the pilot's ceiling and visibility minimums,
// the crosswind on the best runway against the pilot's limit, and thunderstorm chances.
// A planning outlook only, never a weather briefing.
(function () {
  const $ = id => document.getElementById(id);
  const AP = window.WINGAWAY_AIRPORTS || [], RW = window.WINGAWAY_RWYS || {}, A = window.WingAwayAircraft;
  const DEST = (window.WINGAWAY_DESTINATIONS || []).filter(d => !d.draft);
  const R = 3440.065, rad = x => x * Math.PI / 180, H = 3600e3;
  const nm = (a, b) => { const h = Math.sin(rad(b.lat - a.lat) / 2) ** 2 + Math.cos(rad(a.lat)) * Math.cos(rad(b.lat)) * Math.sin(rad(b.lon - a.lon) / 2) ** 2; return 2 * R * Math.asin(Math.sqrt(h)); };
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const MINS_KEY = 'wingaway-wxmins';

  // ---------- airports ----------
  const byCode = {};
  AP.forEach(a => { byCode[a[0]] = a; if (a[1] && !byCode[a[1]]) byCode[a[1]] = a; });
  const fromRow = a => ({ code: a[0], alt: a[1] || '', name: a[2], place: a[3] + (a[4] ? ', ' + a[4] : ''), lat: a[5], lon: a[6] });
  const destLabel = d => d.name + ', ' + (d.stateCode || d.state) + ' (' + d.airport + ')';
  function findAirport(text) {
    const t = (text || '').trim();
    if (!t) return null;
    const d = DEST.find(x => destLabel(x).toLowerCase() === t.toLowerCase() || x.guide === t.replace(/\/?$/, '/') || x.name.toLowerCase() === t.toLowerCase());
    const code = (d ? d.airport : (t.match(/\(([A-Z0-9]{3,4})\)\s*$/) || [, t])[1]).toUpperCase();
    const row = byCode[code] || byCode['K' + code] || (code.length === 4 && code[0] === 'K' ? byCode[code.slice(1)] : null);
    if (row) return Object.assign(fromRow(row), { guide: d ? d.guide : null, town: d ? d.name : null });
    if (d) return { code: d.airport, alt: '', name: d.name, place: d.state, lat: d.lat, lon: d.lon, guide: d.guide, town: d.name };
    return null;
  }
  function runways(apt) {
    const keys = [apt.code, apt.alt, apt.code.length === 4 && apt.code[0] === 'K' ? apt.code.slice(1) : ''];
    for (const k of keys) if (k && RW[k]) return RW[k];
    return null;
  }

  // ---------- forecast data ----------
  // Forecast files: published every hour by the "Weather data (NBM)" GitHub Action. The copy in
  // data/ next to this page is a fallback snapshot, used only if the live files can't be reached.
  const LIVE = 'https://ramorganmd-beep.github.io/WingAwayWeekends/wx/data/';
  let BASE = LIVE, RUN = null; const cache = {};
  // Older runs (12 and 24 hours before the current one) for the trend; each has its own files and cache.
  let PREV = [];
  const bucket = id => id.length === 4 && id[0] === 'K' ? id.slice(0, 3) : id.slice(0, 2);
  function loadBucket(b) {
    if (!cache[b]) cache[b] = fetch(BASE + 'st/' + b + '.json').then(r => r.ok ? r.json() : {}).catch(() => ({}));
    return cache[b];
  }
  async function station(id) { const d = await loadBucket(bucket(id)); return d[id] || null; }
  // The NBM station for an airport, or the nearest one within 30 nm that has a forecast.
  async function stationFor(apt) {
    const ids = [apt.code, apt.alt, apt.code.length === 3 ? 'K' + apt.code : '', apt.alt && apt.alt.length === 3 ? 'K' + apt.alt : ''].filter(Boolean);
    for (const id of ids) { const s = await station(id); if (s) return { id, dist: 0, rec: s }; }
    const near = AP.map(a => [a, nm(apt, { lat: a[5], lon: a[6] })]).filter(x => x[1] > 0.5 && x[1] <= 30).sort((a, b) => a[1] - b[1]).slice(0, 8);
    for (const [a, d] of near) for (const id of [a[0], a[1]].filter(Boolean)) { const s = await station(id); if (s) return { id, dist: d, rec: s }; }
    return null;
  }

  // Forecast closest to time t: the 3-hourly short range (ceiling and visibility) when it reaches, else the 12-hourly outlook.
  function point(rec, t, R) {
    R = R || RUN;
    const r0 = Date.parse(R.run), fs = R.fhrS, fe = R.fhrE;
    const nearest = (f, slack) => { let best = -1, bd = Infinity; f.forEach((h, i) => { const d = Math.abs(r0 + h * H - t); if (d < bd) { bd = d; best = i; } }); return bd <= slack * H ? best : -1; };
    if (rec.s) {
      const i = nearest(fs, 3);
      if (i >= 0) {
        const s = rec.s, at = k => (s[k] || [])[i], near6 = k => { const v = s[k] || []; return v[i] != null ? v[i] : v[i + 1] != null ? v[i + 1] : v[i - 1]; };
        return { kind: 's', when: r0 + fs[i] * H, cig: at('CIG'), vis: at('VIS'), ifr: Math.max(at('IFC') || 0, at('IFV') || 0), sky: at('SKY'), wdr: at('WDR'), wsp: at('WSP'), gst: at('GST'), tstm: at('T03'), rain: near6('P06'), tmp: at('TMP') };
      }
    }
    if (rec.e) {
      const i = nearest(fe, 6);
      if (i >= 0) { const e = rec.e, at = k => (e[k] || [])[i]; return { kind: 'e', when: r0 + fe[i] * H, sky: at('SKY'), wdr: at('WDR'), wsp: at('WSP'), gst: at('GST'), tstm: at('T12'), rain: at('P12'), tmp: at('TMP') }; }
    }
    return null;
  }

  // ---------- checks ----------
  function category(p) {
    const c = p.cig == null || p.cig < 0 ? Infinity : p.cig * 100, v = p.vis == null ? 10 : p.vis / 10;
    if (c < 500 || v < 1) return 'LIFR';
    if (c < 1000 || v < 3) return 'IFR';
    if (c <= 3000 || v <= 5) return 'MVFR';
    return 'VFR';
  }
  // Best runway end for the wind: the one with a headwind (or no tailwind) and the least gust crosswind.
  function crosswind(apt, p) {
    const rws = runways(apt);
    if (!rws || p.wdr == null || p.wsp == null) return null;
    const spd = p.wsp, gst = Math.max(p.gst || 0, spd), dir = p.wdr * 10;
    if (spd < 3 && gst < 8) return { calm: true };
    let best = null;
    rws.forEach(r => [[r[0].split('/')[0], r[3]], [r[0].split('/')[1], r[4]]].forEach(([end, hdg]) => {
      const a = rad(dir - hdg), head = spd * Math.cos(a), xs = Math.abs(spd * Math.sin(a)), xg = Math.abs(gst * Math.sin(a));
      const c = { rwy: end, len: r[1], surf: r[2], xs: Math.round(xs), xg: Math.round(xg), tail: head < -1 };
      if (!best || (best.tail && !c.tail) || (best.tail === c.tail && c.xg < best.xg)) best = c;
    }));
    return best;
  }
  function assess(apt, p, M) {
    const mins = M, limit = M.xw;
    const notes = []; let level = p.kind === 's' ? 'good' : 'outlook';
    const worse = l => { const o = ['good', 'outlook', 'check', 'below']; if (o.indexOf(l) > o.indexOf(level)) level = l; };
    let cat = null;
    if (p.kind === 's') {
      cat = category(p);
      const cft = p.cig == null || p.cig < 0 ? null : p.cig * 100, vsm = p.vis == null ? null : p.vis / 10;
      if ((cft != null && cft < mins.cig) || (vsm != null && vsm < mins.vis)) { worse('below'); notes.push('Below your minimums (' + mins.cig.toLocaleString() + ' ft, ' + mins.vis + ' mi)'); }
      else if (cat !== 'VFR') { worse('check'); }
      if (p.ifr >= 30 && level === 'good') { worse('check'); notes.push(p.ifr + '% chance of IFR'); }
    }
    const x = crosswind(apt, p);
    if (x && !x.calm) {
      if (x.xg > limit) { worse('below'); notes.push('Crosswind ' + x.xg + ' kt in gusts, above your ' + limit + ' kt limit'); }
      else if (x.xg > limit - 3) { worse('check'); notes.push('Crosswind near your ' + limit + ' kt limit'); }
      if (x.tail) notes.push('Tailwind on every runway');
    }
    const gust = Math.max(p.gst || 0, p.wsp || 0);
    if (M.gust && gust > M.gust) { worse('below'); notes.push('Gusts ' + gust + ' kt, above your ' + M.gust + ' kt limit'); }
    else if (M.gust && gust > M.gust - 3 && gust >= 10) { worse('check'); notes.push('Gusts near your ' + M.gust + ' kt limit'); }
    if (p.tstm >= 40) { worse('below'); notes.push(p.tstm + '% thunderstorm chance'); }
    else if (p.tstm >= 15) { worse('check'); notes.push(p.tstm + '% thunderstorm chance'); }
    return { level, cat, x, notes };
  }

  // ---------- formatting ----------
  // ---------- time zones: every time is read and shown in the local time of its airport ----------
  const TZ = window.WINGAWAY_TZ || { z: [], a: {} }, HOME_TZ = Intl.DateTimeFormat().resolvedOptions().timeZone;
  function zoneOf(apt) {
    for (const k of [apt.code, apt.alt, apt.code.length === 4 && apt.code[0] === 'K' ? apt.code.slice(1) : '', apt.code.length === 3 ? 'K' + apt.code : ''])
      if (k && TZ.a[k] != null) return TZ.z[TZ.a[k]];
    return HOME_TZ;
  }
  const dtf = {};
  function parts(t, tz) {
    const f = dtf[tz] || (dtf[tz] = new Intl.DateTimeFormat('en-US', { timeZone: tz, hourCycle: 'h23', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit' }));
    const o = {}; f.formatToParts(t).forEach(x => { o[x.type] = +x.value; }); return o;
  }
  const offset = (t, tz) => { const q = parts(t, tz); return Date.UTC(q.year, q.month - 1, q.day, q.hour % 24, q.minute, q.second) - Math.floor(t / 1000) * 1000; };
  // "2026-11-13T14:00" read as local time at the airport's time zone -> UTC milliseconds.
  function toUTC(str, tz) {
    const m = /^(\d{4})-(\d\d)-(\d\d)T(\d\d):(\d\d)/.exec(str || ''); if (!m) return NaN;
    const g = Date.UTC(+m[1], m[2] - 1, +m[3], +m[4], +m[5]); let t = g - offset(g, tz); t = g - offset(t, tz); return t;
  }
  const fmtT = (t, tz) => new Date(t).toLocaleString([], { timeZone: tz, weekday: 'short', hour: 'numeric', minute: '2-digit', timeZoneName: 'short' });
  const fmtDay = (t, tz) => new Date(t).toLocaleDateString([], { timeZone: tz, weekday: 'long', month: 'short', day: 'numeric' });
  const fmtClock = (t, tz) => new Date(t).toLocaleTimeString([], { timeZone: tz, hour: 'numeric', minute: '2-digit' });

  // ---------- daylight: sunrise, sunset and civil twilight (NOAA-style approximation, within a minute or two) ----------
  function sun(apt, t, tz) {
    const q = parts(t, tz), JD = Date.UTC(q.year, q.month - 1, q.day, 12) / 864e5 + 2440587.5;
    const n = Math.round(JD - 2451545 + 0.0008), Js = n - apt.lon / 360;
    const M = (357.5291 + 0.98560028 * Js) % 360, Mr = rad(M);
    const C = 1.9148 * Math.sin(Mr) + 0.02 * Math.sin(2 * Mr) + 0.0003 * Math.sin(3 * Mr);
    const lam = rad((M + C + 180 + 102.9372) % 360);
    const Jt = 2451545 + Js + 0.0053 * Math.sin(Mr) - 0.0069 * Math.sin(2 * lam);
    const sd = Math.sin(lam) * Math.sin(rad(23.4397)), cd = Math.cos(Math.asin(sd)), phi = rad(apt.lat);
    const ev = z => { const c = (Math.cos(rad(z)) - Math.sin(phi) * sd) / (Math.cos(phi) * cd); if (c < -1 || c > 1) return null; const w = Math.acos(c) * 180 / Math.PI; return [(Jt - w / 360 - 2440587.5) * 864e5, (Jt + w / 360 - 2440587.5) * 864e5]; };
    const a = ev(90.833), b = ev(96);
    return a && b ? { rise: a[0], set: a[1], dawn: b[0], dusk: b[1] } : null;
  }
  function daylight(apt, t, tz, what) {
    const s = sun(apt, t, tz); if (!s) return null;
    if (t > s.dusk) return { night: true, note: what + ' after dark (civil twilight ends ' + fmtClock(s.dusk, tz) + ')' };
    if (t < s.dawn) return { night: true, note: what + ' before first light (' + fmtClock(s.dawn, tz) + ')' };
    if (t > s.set) return { note: what + ' after sunset (' + fmtClock(s.set, tz) + ')' };
    if (t < s.rise) return { note: what + ' before sunrise (' + fmtClock(s.rise, tz) + ')' };
    return null;
  }
  const LEVEL = { good: ['Looks good', 'wx-good'], check: ['Check closely', 'wx-check'], below: ['Outside your settings', 'wx-below'], outlook: ['Outlook only', 'wx-outlook'] };
  const skyWord = s => s == null ? '' : s < 10 ? 'Clear' : s < 30 ? 'Mostly clear' : s < 60 ? 'Partly cloudy' : s < 90 ? 'Mostly cloudy' : 'Overcast';
  function wind(p) {
    if (p.wdr == null || p.wsp == null) return '';
    if (p.wsp < 3 && (p.gst || 0) < 8) return 'Wind calm';
    const d = String((p.wdr * 10) % 360 || 360).padStart(3, '0');
    return 'Wind ' + d + '° ' + p.wsp + (p.gst > p.wsp + 4 ? 'G' + p.gst : '') + ' kt';
  }
  function cell(apt, p, a) {
    if (!p) return '<div class="wx-cell wx-none">No forecast for this time yet</div>';
    const bits = [];
    if (p.kind === 's') {
      bits.push('<span class="wx-cat wx-' + a.cat.toLowerCase() + '">' + a.cat + '</span>');
      bits.push(p.cig == null || p.cig < 0 ? 'No ceiling' : 'Ceiling ' + (p.cig * 100).toLocaleString() + ' ft');
      bits.push('Vis ' + (p.vis >= 100 ? '10+' : (p.vis / 10).toFixed(p.vis % 10 ? 1 : 0)) + ' mi');
    } else {
      bits.push(skyWord(p.sky));
      if (p.rain != null) bits.push(p.rain + '% rain');
    }
    const w = wind(p); if (w) bits.push(w);
    if (a.x && !a.x.calm) bits.push('Rwy ' + esc(a.x.rwy) + ': ' + (a.x.xg < 1 ? 'little or no crosswind' : a.x.xs + (a.x.xg > a.x.xs ? '–' + a.x.xg : '') + ' kt crosswind'));
    else if (!a.x && !runways(apt)) bits.push('No runway data');
    return '<div class="wx-cell"><div class="wx-bits">' + bits.join(' · ') + '</div>' + (a.notes.length ? '<div class="wx-notes">' + a.notes.map(esc).join(' · ') + '</div>' : '') + '</div>';
  }

  // ---------- page ----------
  // ---------- personal minimums by trip type (suggested by Logan Greenlee) ----------
  // Three sets the pilot fills in once: flying alone or with an experienced copilot, with family, and with family
  // into an airport they haven't flown into before. "New airport" applies only at an airport that is new to them:
  // never their home (the From airport), and not one they've ticked "I've flown into it before".
  const SETS_KEY = 'wingaway-minsets', WHO_KEY = 'wingaway-who', SEEN_KEY = 'wingaway-flown';
  const SET_NAMES = { me: 'Me / experienced copilot', fam: 'With family', famnew: 'Family + new airport' };
  const FIELDS_M = ['cig', 'vis', 'xw', 'gust', 'day'];
  function defaultSets() {
    const xw = A.loadXwind();
    return { me: { cig: 1500, vis: 3, xw, gust: 25, day: false }, fam: { cig: 3000, vis: 5, xw: Math.min(xw, 12), gust: 20, day: true },
      famnew: { cig: 3500, vis: 7, xw: Math.min(xw, 10), gust: 15, day: true } };
  }
  function readSets() {
    const d = defaultSets();
    try { const s = JSON.parse(localStorage.getItem(SETS_KEY) || 'null'); if (s) Object.keys(d).forEach(k => { if (s[k]) Object.assign(d[k], s[k]); }); } catch (e) {}
    return d;
  }
  function saveSets(S) { try { localStorage.setItem(SETS_KEY, JSON.stringify(S)); } catch (e) {} }
  function flown() { try { return JSON.parse(localStorage.getItem(SEEN_KEY) || '[]'); } catch (e) { return []; } }
  function setFlown(code, yes) { const f = flown().filter(c => c !== code); if (yes) f.push(code); try { localStorage.setItem(SEEN_KEY, JSON.stringify(f)); } catch (e) {} }
  function setFor(S, who, apt, home) {
    if (who !== 'famnew') return Object.assign({ label: who === 'me' ? 'your own minimums' : 'family minimums' }, S[who]);
    const known = apt.code === home.code || flown().includes(apt.code);
    return known ? Object.assign({ label: 'family minimums (familiar airport)' }, S.fam) : Object.assign({ label: 'family + new airport minimums' }, S.famnew);
  }
  let WHO = 'me';
  function minsTable(S) {
    const row = (f, lab, step) => '<tr><th>' + lab + '</th>' + Object.keys(SET_NAMES).map(k => f === 'day'
      ? '<td><select data-m="' + k + '.day"><option value="0"' + (S[k].day ? '' : ' selected') + '>OK</option><option value="1"' + (S[k].day ? ' selected' : '') + '>Daylight only</option></select></td>'
      : '<td><input data-m="' + k + '.' + f + '" type="number" inputmode="decimal" min="0" step="' + step + '" value="' + S[k][f] + '"></td>').join('') + '</tr>';
    return '<table class="wx-mins"><tr><th></th>' + Object.values(SET_NAMES).map(n => '<th>' + n + '</th>').join('') + '</tr>' +
      row('cig', 'Min ceiling (ft)', 100) + row('vis', 'Min visibility (mi)', 0.5) + row('xw', 'Max crosswind (kt)', 1) + row('gust', 'Max gusts (kt)', 1) + row('day', 'Night', 1) + '</table>';
  }
  function readMins() { try { const m = JSON.parse(localStorage.getItem(MINS_KEY) || 'null'); if (m && m.cig >= 0 && m.vis >= 0) return m; } catch (e) {} return { cig: 3000, vis: 5 }; }
  function saveMins(m) { try { localStorage.setItem(MINS_KEY, JSON.stringify(m)); } catch (e) {} }
  const pad = n => String(n).padStart(2, '0');
  const localInput = t => { const d = new Date(t); return d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate()) + 'T' + pad(d.getHours()) + ':00'; };
  function defaults() {
    const d = new Date(); d.setHours(14, 0, 0, 0);
    const toFri = (5 - d.getDay() + 7) % 7 || (new Date().getHours() < 12 ? 0 : 7);
    d.setDate(d.getDate() + toFri);
    const r = new Date(d); r.setDate(r.getDate() + 2);
    return [localInput(d), localInput(r)];
  }

  // ---------- trend: how the forecast for the same time has changed over the last runs ----------
  async function prevPoint(P, id, t) {
    if (!P.cache[bucket(id)]) P.cache[bucket(id)] = fetch(P.base + 'st/' + bucket(id) + '.json').then(r => r.ok ? r.json() : {}).catch(() => ({}));
    const rec = (await P.cache[bucket(id)])[id];
    return rec ? point(rec, t, P.run) : null;
  }
  // Compare the current forecast for one airport and time with an older run's. Returns change phrases.
  function changes(now, was, apt) {
    const out = [], cats = ['LIFR', 'IFR', 'MVFR', 'VFR'];
    if (now.kind === 's' && was.kind === 's') {
      const a = category(now), b = category(was);
      if (a !== b) out.push((cats.indexOf(a) < cats.indexOf(b) ? 'worse: ' : 'better: ') + b + ' → ' + a);
    }
    const g = p => Math.max(p.gst || 0, p.wsp || 0);
    if (now.wsp != null && was.wsp != null && Math.abs(g(now) - g(was)) >= 5) out.push('gusts ' + (g(now) > g(was) ? 'up' : 'down') + ' ' + Math.abs(g(now) - g(was)) + ' kt (' + g(was) + ' → ' + g(now) + ')');
    const xa = crosswind(apt, now), xb = crosswind(apt, was);
    if (xa && xb && !xa.calm && !xb.calm && Math.abs(xa.xg - xb.xg) >= 4) out.push('crosswind ' + (xa.xg > xb.xg ? 'up' : 'down') + ' ' + Math.abs(xa.xg - xb.xg) + ' kt (' + xb.xg + ' → ' + xa.xg + ')');
    if (now.tstm != null && was.tstm != null && Math.abs(now.tstm - was.tstm) >= 15) out.push('storm chance ' + was.tstm + '% → ' + now.tstm + '%');
    if (now.rain != null && was.rain != null && Math.abs(now.rain - was.rain) >= 25) out.push('rain chance ' + was.rain + '% → ' + now.rain + '%');
    if (now.kind === 'e' && was.kind === 'e' && now.sky != null && was.sky != null && Math.abs(now.sky - was.sky) >= 35) out.push(skyWord(was.sky).toLowerCase() + ' → ' + skyWord(now.sky).toLowerCase());
    return out;
  }
  async function trend(from, sf, depT, to, st, arrT) {
    if (!PREV.length || !sf || !st) return '';
    const parts = [];
    for (const P of PREV) {
      const nowD = point(sf.rec, depT), nowA = point(st.rec, arrT);
      const wasD = await prevPoint(P, sf.id, depT), wasA = await prevPoint(P, st.id, arrT);
      if (!nowD || !nowA || !wasD || !wasA) continue;
      const cd = changes(nowD, wasD, from), ca = changes(nowA, wasA, to);
      parts.push({ hrs: P.hrs, txt: [cd.length ? esc(from.code) + ' ' + cd.join(', ') : '', ca.length ? esc(to.code) + ' ' + ca.join(', ') : ''].filter(Boolean).join('; ') });
    }
    if (!parts.length) return '';
    const p24 = parts.find(x => x.hrs === 24), p12 = parts.find(x => x.hrs === 12);
    const steady = parts.every(x => !x.txt);
    let h = '<p class="wx-trend"><strong>Forecast trend for your planned time:</strong> ';
    if (steady) h += 'steady. The ' + parts.map(x => x.hrs + '-hour-old').join(' and ') + ' forecast' + (parts.length > 1 ? 's' : '') + ' looked about the same.';
    else h += parts.map(x => 'since ' + x.hrs + ' hours ago: ' + (x.txt || 'about the same')).join(' · ') + '.';
    return h + '</p>';
  }

  // ---------- advisories along the route (AIRMETs, SIGMETs, CWAs, PIREPs) ----------
  let ADV = null, STATES = null;
  const SEV = { LGT: 'light', 'LGT-MOD': 'light to moderate', MOD: 'moderate', 'MOD-SEV': 'moderate to severe', SEV: 'severe' };
  const ft = v => typeof v === 'number' ? (v === 0 ? 'surface' : v.toLocaleString() + ' ft') : v === 'SFC' ? 'surface' : v === 'FZL' ? 'the freezing level' : v;
  function band(a) {
    if (a.base == null && a.top == null) return '';
    if (a.base === 'FZL' && a.fzl && a.fzl[0] != null) return ', freezing level (' + ft(a.fzl[0]) + (a.fzl[1] != null && a.fzl[1] !== a.fzl[0] ? '–' + ft(a.fzl[1]) : '') + ') to ' + ft(a.top);
    if (a.base == null) return ', up to ' + ft(a.top);
    if (a.top == null) return ', from ' + ft(a.base);
    return ', ' + ft(a.base) + ' to ' + ft(a.top);
  }
  function advLabel(a) {
    const sev = SEV[a.sev] ? SEV[a.sev] + ' ' : '';
    if (a.k === 'gairmet') {
      const L = { ICE: ['AIRMET', sev + 'icing'], 'TURB-LO': ['AIRMET', sev + 'turbulence'], 'TURB-HI': ['AIRMET', sev + 'turbulence at high altitude'],
        IFR: ['AIRMET', 'IFR conditions' + (a.due ? ' (' + a.due.replace('CIG BLW 010', 'ceiling below 1,000 ft').replace('VIS BLW 3SM', 'visibility below 3 mi').toLowerCase() + ')' : '')],
        MT_OBSC: ['AIRMET', 'mountains obscured'], LLWS: ['AIRMET', 'low-level wind shear'], SFC_WND: ['AIRMET', 'sustained surface winds over 30 kt'] }[a.hz] || ['AIRMET', a.hz];
      return { kind: L[0], text: L[1].charAt(0).toUpperCase() + L[1].slice(1) + (a.hz === 'IFR' || a.hz === 'MT_OBSC' ? '' : band(a)), rank: 3 };
    }
    if (a.k === 'cwa') return { kind: 'Center Weather Advisory' + (a.by ? ' (' + a.by + ' Center)' : ''), text: (a.hz === 'TS' ? 'Thunderstorms' : a.hz === 'IFR' ? 'IFR conditions' : a.hz === 'TURB' ? 'Turbulence' : a.hz === 'ICE' ? 'Icing' : a.hz) + band(a), rank: 2 };
    if (a.hz === 'CONVECTIVE') return { kind: 'Convective SIGMET', text: 'Thunderstorms' + (a.top ? ', tops to ' + ft(a.top) : ''), rank: 1 };
    return { kind: 'SIGMET', text: (a.hz === 'ICE' ? 'Severe icing' : a.hz === 'TURB' ? 'Severe turbulence' : a.hz) + band(a), rank: 1 };
  }
  // Route geometry in a local flat projection (nautical miles); fine for a 25 nm corridor check.
  function routeSamples(from, to) {
    const n = Math.max(2, Math.ceil(nm(from, to) / 10));
    return Array.from({ length: n + 1 }, (_, i) => ({ lat: from.lat + (to.lat - from.lat) * i / n, lon: from.lon + (to.lon - from.lon) * i / n, f: i / n }));
  }
  function inPoly(pt, P) {
    let inside = false;
    for (let i = 0, j = P.length - 1; i < P.length; j = i++) {
      const [yi, xi] = P[i], [yj, xj] = P[j];
      if ((yi > pt.lat) !== (yj > pt.lat) && pt.lon < (xj - xi) * (pt.lat - yi) / (yj - yi) + xi) inside = !inside;
    }
    return inside;
  }
  function distToPoly(pt, P) {
    const k = Math.cos(rad(pt.lat)) * 60, X = p => [(p[1] - pt.lon) * k, (p[0] - pt.lat) * 60];
    let best = Infinity;
    for (let i = 0; i < P.length; i++) {
      const a = X(P[i]), b = X(P[(i + 1) % P.length]), dx = b[0] - a[0], dy = b[1] - a[1], L = dx * dx + dy * dy;
      const t = L ? Math.max(0, Math.min(1, -(a[0] * dx + a[1] * dy) / L)) : 0;
      best = Math.min(best, Math.hypot(a[0] + t * dx, a[1] + t * dy));
    }
    return best;
  }
  function where(fs, from, to) {
    const lo = Math.min(...fs), hi = Math.max(...fs);
    if (lo <= 0.15 && hi >= 0.85) return 'along most of the route';
    if (hi <= 0.35) return 'near ' + from.code;
    if (lo >= 0.65) return 'near ' + to.code;
    return lo < 0.35 ? 'over the first part of the route' : hi > 0.65 ? 'over the last part of the route' : 'over the middle of the route';
  }
  function routeAdvisories(from, to, dep, arr) {
    const now = Date.now(), out = { items: [], pireps: [], shapes: [] };
    if (!ADV || dep - now > 13 * H || arr < now - H) return null;
    const S = routeSamples(from, to);
    const groups = {};
    ADV.adv.forEach(a => {
      if (a.t1 < dep || a.t0 > arr || a.p.length < 3) return;
      const hit = S.filter(pt => inPoly(pt, a.p) || distToPoly(pt, a.p) <= 25).map(pt => pt.f);
      if (!hit.length) return;
      const L = advLabel(a), key = L.kind + '|' + L.text;
      (groups[key] = groups[key] || { L, fs: [], a }).fs.push(...hit);
      out.shapes.push(a);
    });
    out.items = Object.values(groups).sort((x, y) => x.L.rank - y.L.rank).map(g => ({ kind: g.L.kind, text: g.L.text, where: where(g.fs, from, to), rank: g.L.rank }));
    out.pchk = Math.abs(dep - now) <= 3 * H;
    if (out.pchk) out.pireps = ADV.pireps.filter(r => S.some(pt => nm(pt, r) <= 25)).sort((a, b) => b.t - a.t).slice(0, 6);
    return out;
  }
  function advMap(from, to, shapes, pireps) {
    if (!window.d3 || !STATES) return '';
    const W = 640, Hh = 300, route = { type: 'LineString', coordinates: [[from.lon, from.lat], [to.lon, to.lat]] };
    const pad = Math.max(1.2, nm(from, to) / 60 * 0.35);
    const box = { type: 'MultiPoint', coordinates: [[Math.min(from.lon, to.lon) - pad, Math.min(from.lat, to.lat) - pad], [Math.max(from.lon, to.lon) + pad, Math.max(from.lat, to.lat) + pad]] };
    const proj = d3.geoMercator().fitExtent([[10, 10], [W - 10, Hh - 10]], box), path = d3.geoPath(proj);
    const col = a => a.k === 'gairmet' ? (a.hz === 'ICE' ? '#2a5d9f' : a.hz.startsWith('TURB') ? '#b7791f' : a.hz === 'IFR' ? '#a33a1f' : '#6b5b95') : '#a33a1f';
    let g = STATES.map(f => '<path d="' + path(f) + '" fill="#f1eee7" stroke="#fff" stroke-width="1"/>').join('');
    // Advisory areas drawn as flat polygons from projected corners (avoids spherical winding surprises).
    g += shapes.map(a => { const c = col(a); return '<polygon points="' + a.p.map(q => proj([q[1], q[0]]).map(v => v.toFixed(1)).join(',')).join(' ') + '" fill="' + c + '" fill-opacity=".14" stroke="' + c + '" stroke-width="1.2"/>'; }).join('');
    g += '<path d="' + path(route) + '" fill="none" stroke="#102d40" stroke-width="2.5" stroke-dasharray="6 4"/>';
    g += pireps.map(r => { const [x, y] = proj([r.lon, r.lat]); return '<circle cx="' + x + '" cy="' + y + '" r="4" fill="#fff" stroke="#102d40" stroke-width="1.5"/>'; }).join('');
    [from, to].forEach(a => { const [x, y] = proj([a.lon, a.lat]); g += '<circle cx="' + x + '" cy="' + y + '" r="5" fill="#ba7d2f" stroke="#fff" stroke-width="2"/><text x="' + (x + 8) + '" y="' + (y - 8) + '" font-size="12" font-weight="700" fill="#102d40" paint-order="stroke" stroke="#fff" stroke-width="3">' + esc(a.code) + '</text>'; });
    return '<svg class="wx-map" viewBox="0 0 ' + W + ' ' + Hh + '" role="img" aria-label="Route with advisory areas"><defs><clipPath id="wxclip"><rect width="' + W + '" height="' + Hh + '"/></clipPath></defs><g clip-path="url(#wxclip)">' + g + '</g></svg>' +
      '<p class="wx-key"><span style="color:#2a5d9f">■</span> icing <span style="color:#b7791f">■</span> turbulence <span style="color:#a33a1f">■</span> IFR, storms, SIGMETs <span style="color:#6b5b95">■</span> other · ○ pilot report · dashed line: straight-line route</p>';
  }
  function advHTML(from, to, dep, arr, tz) {
    const r = routeAdvisories(from, to, dep, arr);
    let h = '<div class="wx-adv"><h3>Advisories near your route</h3>';
    if (!ADV) return h + '<p class="wx-meta">Advisories could not be loaded right now.</p></div>';
    if (!r) return h + '<p class="wx-meta">AIRMETs, SIGMETs and pilot reports along the straight-line route show here from about 12 hours before departure.</p></div>';
    if (!r.items.length && !r.pireps.length) h += '<p class="wx-meta">No AIRMETs, SIGMETs or Center Weather Advisories within 25 nm of the straight-line route for your flight time' + (r.pchk ? ', and no recent icing or turbulence reports.' : '.') + '</p>';
    else {
      h += '<ul class="wx-advlist">' + r.items.map(i => '<li class="wx-r' + i.rank + '"><b>' + esc(i.kind) + ':</b> ' + esc(i.text) + ' <span>' + esc(i.where) + '</span></li>').join('') + '</ul>';
      if (r.pireps.length) h += '<p class="wx-meta"><b>Recent pilot reports within 25 nm:</b></p><ul class="wx-advlist">' + r.pireps.map(p => '<li>' + esc(fmtClock(p.t, tz)) + ' · ' + esc(p.ac || 'aircraft') + (p.fl ? ' at ' + (p.fl * 100).toLocaleString() + ' ft' : '') + ': ' + esc([p.ice ? (SEV[p.ice] || p.ice.toLowerCase()) + ' icing' : '', p.turb ? (SEV[p.turb] || p.turb.toLowerCase()) + ' turbulence' : ''].filter(Boolean).join(', ')) + '</li>').join('') + '</ul>';
      h += advMap(from, to, r.shapes, r.pireps);
    }
    return h + '<p class="wx-confirm">Advisories are checked against a straight line, not your filed route, and only within 25 nm of it. Confirm with your flight planning resources and an official briefing.</p></div>';
  }

  // ---------- weather window chart (concept inspired by Logan Greenlee's Weather Window) ----------
  // One bar per departure hour around the planned time (6 hours either side going, 12 coming home). Bars above the line are
  // within the pilot's settings (taller = more margin on crosswind); below the line need a look or are
  // outside them. Runs of 2+ good hours are boxed as windows. Tapping a bar plans that departure time.
  const tzInput = (t, tz) => { const q = parts(t, tz); return q.year + '-' + pad(q.month) + '-' + pad(q.day) + 'T' + pad(q.hour % 24) + ':00'; };
  function score(r, MF, MT) {
    if (!r.lvl) return null;
    if (r.lvl === 'outlook') return { s: 0.7, c: 'out' };
    if (r.lvl === 'check') return { s: -1, c: 'chk' };
    if (r.lvl === 'below') {
      const severe = [r.pd, r.pa].some(p => p && ((p.tstm || 0) >= 40 || (p.kind === 's' && category(p) === 'LIFR')));
      return { s: severe ? -3 : -2, c: severe ? 'sev' : 'bad' };
    }
    const m = [[r.ad.x, MF.xw], [r.aa.x, MT.xw]].map(([x, l]) => x && !x.calm ? Math.max(0, (l - x.xg) / l) : 1);
    return { s: 1 + 2 * Math.min(...m), c: 'ok' };
  }
  function windowChart(rate, from, to, depT, tzF, tzT, MF, MT, field, span, blockH) {
    // Centered on the planned time: 12 hours for the trip out (6 either side), 24 for the trip home (12 either side).
    const half = span, n = 2 * half;
    const start = Math.floor((depT - half * H) / H) * H;
    const bars = Array.from({ length: n }, (_, i) => { const r = rate(start + i * H, null); return Object.assign(r, { sc: score(r, MF, MT), i }); });
    if (!bars.some(b => b.sc)) return '';
    const W = 960, x0 = 36, bw = (W - x0 - 8) / n, mid = 92, u = 22, Hh = 214;
    const col = { ok: '#3f8f4f', out: '#b9c3cb', chk: '#d39a2c', bad: '#c2462b', sev: '#7a3a8c' };
    let g = '';
    // night shading at the departure airport
    bars.forEach(b => { const sn = sun(from, b.dep, tzF); if (sn && (b.dep > sn.dusk || b.dep < sn.dawn)) g += '<rect x="' + (x0 + b.i * bw) + '" y="8" width="' + bw + '" height="' + (Hh - 40) + '" fill="#e6eaee"/>'; });
    g += '<line x1="' + x0 + '" x2="' + (W - 8) + '" y1="' + mid + '" y2="' + mid + '" stroke="#9aa7b2" stroke-width="1"/>';
    // windows: 2+ consecutive good hours
    const wins = []; let cur = null;
    // Boxed windows are daylight only (take-off and landing both before dark); night bars still show their color.
    const dark = b => { const d1 = daylight(from, b.dep, tzF, ''), d2 = daylight(to, b.arr, tzT, ''); return (d1 && d1.night) || (d2 && d2.night); };
    bars.forEach(b => { if (b.sc && b.sc.c === 'ok' && !dark(b)) { if (!cur) wins.push(cur = [b]); else cur.push(b); } else cur = null; });
    const W2 = wins.filter(w => w.length >= 2);
    W2.forEach(w => {
      const a = w[0], z = w[w.length - 1], avg = w.reduce((s, b) => s + b.sc.s, 0) / w.length, xa = x0 + a.i * bw - 1, xz = x0 + (z.i + 1) * bw + 1;
      g += '<rect x="' + xa + '" y="10" width="' + (xz - xa) + '" height="' + (mid + 6 - 10) + '" rx="6" fill="none" stroke="#2a5d9f" stroke-width="1.5"/>';
      g += '<text x="' + ((xa + xz) / 2) + '" y="22" text-anchor="middle" font-size="11" font-weight="700" fill="#2a5d9f">' + (avg >= 2.3 ? 'Great' : 'Good') + '</text>';
    });
    bars.forEach(b => {
      if (!b.sc) return;
      const hgt = Math.abs(b.sc.s) * u, y = b.sc.s > 0 ? mid - hgt : mid, x = x0 + b.i * bw + 1.5;
      const L = LEVEL[b.lvl][0] + ' · leave ' + fmtT(b.dep, tzF) + ', land ' + fmtT(b.arr, tzT) + (b.ad.notes.concat(b.aa.notes).length ? ' · ' + b.ad.notes.concat(b.aa.notes).join(' · ') : '');
      g += '<rect class="wx-bar-h" data-pick="' + field + '" data-t="' + tzInput(b.dep, tzF) + '" x="' + x + '" y="' + y + '" width="' + Math.max(1, bw - (bw > 8 ? 3 : 1)) + '" height="' + Math.max(2, hgt) + '" rx="2" fill="' + col[b.sc.c] + '"><title>' + esc(L) + '</title></rect>';
    });
    // planned departure (🛫) and estimated arrival (🛬) under the time axis
    const arrT = depT + (blockH || 0) * H, xAt = t => x0 + ((t - start) / H + 0.5) * bw, xMax = x0 + n * bw;
    const xd = xAt(depT), xa0 = xAt(arrT), xa = Math.max(xa0, xd + 28);
    // a dashed line through the bars at each time, with a larger marker below the axis so it reads on a phone or iPad
    // The icons sit in HTML over the chart, not inside the SVG, so they keep their size when the chart shrinks on a phone.
    let mk = '';
    const mark = (xl, x, emo, t) => {
      g += '<line x1="' + xl + '" x2="' + xl + '" y1="8" y2="' + (Hh - 46) + '" stroke="#102d40" stroke-width="1.5" stroke-dasharray="4 3" vector-effect="non-scaling-stroke"/>';
      mk += '<span class="wx-mk" style="left:' + (x / W * 100).toFixed(2) + '%" title="' + t + '" aria-hidden="true">' + emo + '</span>';
    };
    if (xd >= x0 && xd <= xMax) mark(xd, xd, '🛫', 'Planned departure');
    if (blockH && xa0 >= x0 && xa0 <= xMax) mark(xa0, xa, '🛬', 'Estimated arrival');
    // hour labels (every hour when zoomed in, else every 2 or 3), day names at midnight
    const step = n <= 12 ? 1 : n <= 24 ? 2 : 3;
    bars.forEach(b => {
      const hr = parts(b.dep, tzF).hour % 24;
      if (hr % step === 0) g += '<text x="' + (x0 + (b.i + 0.5) * bw) + '" y="' + (Hh - 34) + '" text-anchor="middle" font-size="12" fill="#647784">' + (hr === 0 ? '12a' : hr === 12 ? '12p' : hr > 12 ? (hr - 12) + 'p' : hr + 'a') + '</text>';
      if (hr === 0 || (b.i === 0 && hr >= 1 && hr <= 20)) g += '<text x="' + (x0 + b.i * bw) + '" y="' + (Hh - 4) + '" font-size="11" font-weight="700" fill="#102d40">' + esc(new Date(b.dep).toLocaleDateString([], { timeZone: tzF, weekday: 'short', month: 'short', day: 'numeric' })) + '</text>';
    });
    g += '<text x="4" y="' + (mid - 30) + '" font-size="10" fill="#647784">Good</text><text x="4" y="' + (mid + 44) + '" font-size="10" fill="#647784">Look</text>';
    const sum = W2.length ? W2.length + ' window' + (W2.length > 1 ? 's' : '') + ': ' + W2.map(w => fmtT(w[0].dep, tzF) + '–' + new Date(w[w.length - 1].dep + H).toLocaleTimeString([], { timeZone: tzF, hour: 'numeric', minute: '2-digit' })).join(' · ') : 'No departure window within your settings in this range';
    return '<div class="wx-win"><div class="wx-win-head"><strong>Departure windows</strong> <span>🛫 Leave ' + esc(fmtT(depT, tzF)) + ' · 🛬 Land ' + esc(fmtT(arrT, tzT)) + '</span><br><span>' + esc(sum) + '</span></div>' +
      '<div class="wx-svgw"><div class="wx-svgi"><svg viewBox="0 0 ' + W + ' ' + Hh + '" role="img" aria-label="' + esc('Departure window chart from ' + from.code + ' to ' + to.code + '. ' + sum) + '">' + g + '</svg>' + mk + '</div></div>' +
      '<p class="wx-key">Bars are departure hours from ' + esc(from.code) + ': <span style="color:#3f8f4f">▲ within your settings</span> (taller = more crosswind margin) · <span style="color:#d39a2c">▼ check closely</span> · <span style="color:#c2462b">▼ outside your settings</span> · <span style="color:#7a3a8c">▼ storms or LIFR</span> · <span style="color:#8a96a0">▲ outlook only</span> · shaded = dark at ' + esc(from.code) + ' · boxes = daylight windows of 2+ hours · 🛫 planned departure · 🛬 estimated arrival. Tap a bar to plan that time.</p>' +
      '<p class="wx-credit">Weather window concept inspired by Logan Greenlee.</p></div>';
  }

  async function leg(title, from, to, depT, win, prof, MF, MT, span) {
    const [sf, st] = await Promise.all([stationFor(from), stationFor(to)]);
    const tzF = zoneOf(from), tzT = zoneOf(to);
    const dist = nm(from, to), est = A.estimate(dist, prof), blockH = est.hours;
    const rate = (dep, o) => {
      const arr = dep + blockH * H;
      const pd = sf && point(sf.rec, dep), pa = st && point(st.rec, arr);
      const ad = pd ? assess(from, pd, MF) : null, aa = pa ? assess(to, pa, MT) : null;
      const order = ['good', 'outlook', 'check', 'below'];
      // Daylight at take-off and landing: always noted; with "Daylight only" it lowers the rating.
      [[ad, daylight(from, dep, tzF, 'Takes off'), MF], [aa, daylight(to, arr, tzT, 'Lands'), MT]].forEach(([a, d, M]) => {
        if (!a || !d) return;
        a.notes.push(d.note);
        if (M.day) { const l = d.night ? 'below' : 'check'; if (order.indexOf(l) > order.indexOf(a.level)) a.level = l; }
      });
      const lvl = !ad || !aa ? null : order[Math.max(order.indexOf(ad.level), order.indexOf(aa.level))];
      return { o, dep, arr, pd, pa, ad, aa, lvl };
    };
    const rows = [];
    for (let o = -win; o <= win; o++) rows.push(rate(depT + o * H, o));
    const plan = rows.find(r => r.o === 0);
    let verdict;
    if (!plan.lvl) verdict = 'The forecast doesn’t reach this time yet. NBM station forecasts run about 8 days ahead; check back closer to the trip.';
    else if (plan.lvl === 'good') verdict = 'Your planned time looks good at both ends.';
    else if (plan.lvl === 'outlook') verdict = 'Too far out for ceilings and visibility, which are forecast within 3 days. Wind, gusts, rain and storm chances are shown as an early outlook.';
    else {
      const alt = rows.filter(r => r.lvl === 'good').sort((a, b) => Math.abs(a.o) - Math.abs(b.o))[0];
      verdict = (plan.lvl === 'below' ? 'Your planned time is outside your settings.' : 'Your planned time needs a closer look.') + (alt ? ' Better: leave ' + fmtT(alt.dep, tzF) + ' (' + Math.abs(alt.o) + ' hr ' + (alt.o < 0 ? 'earlier' : 'later') + ').' : ' No time in this window looks better.');
    }
    const src = (s, apt) => !s ? ' <span class="wx-src">no forecast within 30 nm</span>' : s.dist ? ' <span class="wx-src">using ' + esc(s.id) + ', ' + Math.round(s.dist) + ' nm away</span>' : '';
    let h = '<section class="wx-leg"><h2>' + esc(title) + ': ' + esc(from.code) + ' → ' + esc(to.code) + '</h2>';
    h += '<p class="wx-meta">' + esc(fmtDay(depT, tzF)) + ' · ~' + Math.round(dist) + ' nm · about ' + A.formatTime(blockH) + ' with ' + esc(prof ? prof.label : 'the default 150 kt estimate') + '</p>';
    h += '<p class="wx-verdict wx-v-' + (plan.lvl || 'none') + '">' + esc(verdict) + '</p>';
    h += '<p class="wx-meta">Minimums: ' + esc(from.code) + ' ' + esc(MF.label) + ' · ' + esc(to.code) + ' ' + esc(MT.label) + '</p>';
    h += await trend(from, sf, depT, to, st, depT + blockH * H);
    h += windowChart(rate, from, to, depT, tzF, tzT, MF, MT, title === 'Going' ? 'dep' : 'ret', title === 'Going' ? 6 : 12, blockH);
    h += '<div class="wx-table" role="table"><div class="wx-row wx-head" role="row"><div role="columnheader">🛫 Leave</div><div role="columnheader">At ' + esc(from.code) + src(sf) + '</div><div role="columnheader">🛬 Land</div><div role="columnheader">At ' + esc(to.code) + src(st) + '</div><div role="columnheader">Overall</div></div>';
    rows.forEach(r => {
      const L = r.lvl ? LEVEL[r.lvl] : ['No forecast yet', 'wx-outlook'];
      h += '<div class="wx-row' + (r.o === 0 ? ' wx-plan' : '') + '" role="row"><div class="wx-time">' + esc(fmtT(r.dep, tzF)) + (r.o === 0 ? '<span class="wx-tag">Planned</span>' : '') + '</div>' + cell(from, r.pd, r.ad || { notes: [] }) + '<div class="wx-time">' + esc(fmtT(r.arr, tzT)) + '</div>' + cell(to, r.pa, r.aa || { notes: [] }) + '<div><span class="wx-level ' + L[1] + '">' + L[0] + '</span></div></div>';
    });
    h += '</div>' + advHTML(from, to, depT, depT + blockH * H, tzF);
    return h + '</section>';
  }

  function selectedProfile() {
    const v = $('ac').value;
    if (v === 'saved') return A.load();
    if (v === 'default') return null;
    return A.PRESETS.find(x => x.id === v) || null;
  }

  async function draw() {
    const from = findAirport($('from').value), to = findAirport($('to').value), out = $('out');
    if (!from || !to) { out.innerHTML = '<p class="wx-verdict">Enter a departure airport and a destination.</p>'; return; }
    const S = readSets();
    try { localStorage.setItem(WHO_KEY, WHO); } catch (e) {}
    const fl = $('flownbox'); fl.hidden = WHO !== 'famnew' || to.code === from.code;
    $('flownlab').textContent = 'I’ve flown into ' + to.code + ' before'; $('flown').checked = flown().includes(to.code);
    const prof = selectedProfile(), win = +$('win').value, dep = toUTC($('dep').value, zoneOf(from)), ret = toUTC($('ret').value, zoneOf(to));
    const q = new URLSearchParams({ from: from.code, to: to.guide ? to.guide.replace(/\/$/, '') : to.code, dep: $('dep').value, ret: $('ret').value, win, ac: $('ac').value, who: WHO });
    history.replaceState(null, '', '?' + q);
    out.innerHTML = '<p class="wx-meta">Loading forecast…</p>';
    let h = '';
    if (isFinite(dep)) h += await leg('Going', from, to, dep, win, prof, setFor(S, WHO, from, from), setFor(S, WHO, to, from), [dep, isFinite(ret) ? ret : dep]);
    if (isFinite(ret)) h += await leg('Coming home', to, from, ret, win, prof, setFor(S, WHO, to, from), setFor(S, WHO, from, from), [isFinite(dep) ? dep : ret, ret]);
    if (to.guide) h += '<p class="wx-meta"><a href="../' + esc(to.guide) + '">Open the ' + esc(to.town) + ' guide</a></p>';
    out.innerHTML = h;
    // On a phone the chart scrolls sideways: open it with the takeoff marker in view.
    out.querySelectorAll('.wx-svgw').forEach(w => { const m = w.querySelector('.wx-mk'); if (m && w.scrollWidth > w.clientWidth) w.scrollLeft = Math.max(0, m.offsetLeft - w.clientWidth / 3); });
  }

  async function init() {
    for (const base of [LIVE, 'data/']) {
      try { const r = await fetch(base + 'run.json', { cache: 'no-cache' }); if (r.ok) { RUN = await r.json(); BASE = base; break; } } catch (e) {}
    }
    if (!RUN) { $('out').innerHTML = '<p class="wx-verdict">The forecast data could not be loaded.</p>'; return; }
    try { const r = await fetch(BASE + 'adv.json', { cache: 'no-cache' }); if (r.ok) ADV = await r.json(); } catch (e) {}
    try { if (window.d3 && window.topojson) { const us = await d3.json('../map/states-10m.json'); STATES = topojson.feature(us, us.objects.states).features; } } catch (e) {}
    for (const hrs of [12, 24]) {
      try { const r = await fetch(BASE + 'prev' + hrs + '/run.json', { cache: 'no-cache' }); if (r.ok) PREV.push({ hrs, base: BASE + 'prev' + hrs + '/', run: await r.json(), cache: {} }); } catch (e) {}
    }
    $('run').textContent = new Date(RUN.run).toLocaleString([], { weekday: 'short', month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit' }) + ' (NBM ' + RUN.run.slice(11, 13) + 'Z run' + (BASE === LIVE ? ', updated hourly)' : ', saved copy)');
    $('dl').innerHTML = DEST.map(d => '<option value="' + esc(destLabel(d)) + '">').join('');
    if (window.WingAwaySuggest) WingAwaySuggest($('from'), $('fromlist'), AP);
    const p = new URLSearchParams(location.search), [d0, r0] = defaults();
    let home = ''; try { home = localStorage.getItem('wingaway-home') || ''; } catch (e) {}
    $('from').value = p.get('from') || home || 'KMYR';
    const tg = p.get('to'), td = tg && DEST.find(d => d.guide === tg.replace(/\/?$/, '/'));
    $('to').value = td ? destLabel(td) : tg || destLabel(DEST.find(d => d.guide === 'charleston/') || DEST[0]);
    $('dep').value = p.get('dep') || d0; $('ret').value = p.has('ret') ? p.get('ret') : r0; $('win').value = p.get('win') || '3';
    try { WHO = localStorage.getItem(WHO_KEY) || 'me'; } catch (e) {}
    if (SET_NAMES[p.get('who')]) WHO = p.get('who');
    if (!SET_NAMES[WHO]) WHO = 'me';
    const paintWho = () => document.querySelectorAll('[data-who]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.who === WHO)));
    paintWho();
    document.querySelectorAll('[data-who]').forEach(b => b.addEventListener('click', () => { WHO = b.dataset.who; paintWho(); draw(); }));
    $('minsbox').innerHTML = minsTable(readSets());
    $('minsbox').addEventListener('change', e => {
      const el = e.target.closest('[data-m]'); if (!el) return;
      const [k, f] = el.dataset.m.split('.'), S = readSets();
      S[k][f] = f === 'day' ? el.value === '1' : Math.max(0, +el.value || 0);
      if (k === 'me' && f === 'xw') A.saveXwind(S.me.xw);
      saveSets(S); draw();
    });
    // Save button: reads every box in the table (the boxes also save as you leave them) and confirms.
    $('minssave').addEventListener('click', () => {
      const S = readSets();
      document.querySelectorAll('#minsbox [data-m]').forEach(el => { const [k, f] = el.dataset.m.split('.'); S[k][f] = f === 'day' ? el.value === '1' : Math.max(0, +el.value || 0); });
      saveSets(S); A.saveXwind(S.me.xw);
      const btn = $('minssave'); btn.textContent = 'Saved ✓'; btn.classList.add('saved'); $('minsmsg').textContent = 'Your minimums are saved in this browser.';
      setTimeout(() => { btn.textContent = 'Save my minimums'; btn.classList.remove('saved'); $('minsmsg').textContent = ''; }, 3000);
      draw();
    });
    $('minsreset').addEventListener('click', () => { try { localStorage.removeItem(SETS_KEY); } catch (e) {} $('minsbox').innerHTML = minsTable(readSets()); draw(); });
    $('flown').addEventListener('change', () => { const t = findAirport($('to').value); if (t) setFlown(t.code, $('flown').checked); draw(); });
    // Aircraft: the profile saved on the homepage, any preset, or the default estimate. Picking one here
    // only sets the flight time on this page; the homepage panel still owns the saved profile.
    const saved = A.load(), ac = $('ac');
    ac.innerHTML = (saved ? '<option value="saved">' + esc(saved.id === 'custom' ? 'Custom aircraft' : saved.label) + ' (my saved numbers)</option>' : '') +
      A.PRESETS.filter(x => !x.gear || x.gear === 'land').map(x => '<option value="' + esc(x.id) + '">' + esc(x.label) + '</option>').join('') +
      (saved && saved.id === 'custom' ? '' : '<option value="custom">Custom aircraft (enter your numbers on the homepage)</option>') +
      '<option value="default">Default estimate (150 kt)</option>';
    ac.value = p.get('ac') && ac.querySelector('option[value="' + p.get('ac') + '"]') ? p.get('ac') : saved ? 'saved' : 'default';
    $('out').addEventListener('click', e => { const b = e.target.closest('[data-pick]'); if (!b) return; $(b.dataset.pick).value = b.dataset.t; draw(); });
    // "Custom aircraft" with no saved numbers yet: open the homepage aircraft panel to enter them.
    ac.addEventListener('change', () => { if (ac.value === 'custom') location.href = '../#aircraft'; });
    ['from', 'to', 'dep', 'ret', 'win', 'ac'].forEach(id => $(id).addEventListener('change', draw));
    draw();
  }
  init();
})();
