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
  // Forecast files: published every 3 hours by the "Weather data (NBM)" GitHub Action. The copy in
  // data/ next to this page is a fallback snapshot, used only if the live files can't be reached.
  const LIVE = 'https://ramorganmd-beep.github.io/WingAwayWeekends/wx/data/';
  let BASE = LIVE, RUN = null; const cache = {};
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
  const run0 = () => Date.parse(RUN.run);
  // Forecast closest to time t: the 3-hourly short range (ceiling and visibility) when it reaches, else the 12-hourly outlook.
  function point(rec, t) {
    const r0 = run0(), fs = RUN.fhrS, fe = RUN.fhrE;
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
  function assess(apt, p, mins, limit) {
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
    if (p.tstm >= 40) { worse('below'); notes.push(p.tstm + '% thunderstorm chance'); }
    else if (p.tstm >= 15) { worse('check'); notes.push(p.tstm + '% thunderstorm chance'); }
    return { level, cat, x, notes };
  }

  // ---------- formatting ----------
  const fmtT = t => new Date(t).toLocaleString([], { weekday: 'short', hour: 'numeric', minute: '2-digit' });
  const fmtDay = t => new Date(t).toLocaleDateString([], { weekday: 'long', month: 'short', day: 'numeric' });
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

  async function leg(title, from, to, depT, win, prof, mins, limit) {
    const [sf, st] = await Promise.all([stationFor(from), stationFor(to)]);
    const dist = nm(from, to), est = A.estimate(dist, prof), blockH = est.hours;
    const rows = [];
    for (let o = -win; o <= win; o++) {
      const dep = depT + o * H, arr = dep + blockH * H;
      const pd = sf && point(sf.rec, dep), pa = st && point(st.rec, arr);
      const ad = pd ? assess(from, pd, mins, limit) : null, aa = pa ? assess(to, pa, mins, limit) : null;
      const order = ['good', 'outlook', 'check', 'below'];
      const lvl = !ad || !aa ? null : order[Math.max(order.indexOf(ad.level), order.indexOf(aa.level))];
      rows.push({ o, dep, arr, pd, pa, ad, aa, lvl });
    }
    const plan = rows.find(r => r.o === 0);
    let verdict;
    if (!plan.lvl) verdict = 'The forecast doesn’t reach this time yet. NBM station forecasts run about 8 days ahead; check back closer to the trip.';
    else if (plan.lvl === 'good') verdict = 'Your planned time looks good at both ends.';
    else if (plan.lvl === 'outlook') verdict = 'Too far out for ceilings and visibility, which are forecast within 3 days. Wind, gusts, rain and storm chances are shown as an early outlook.';
    else {
      const alt = rows.filter(r => r.lvl === 'good').sort((a, b) => Math.abs(a.o) - Math.abs(b.o))[0];
      verdict = (plan.lvl === 'below' ? 'Your planned time is outside your settings.' : 'Your planned time needs a closer look.') + (alt ? ' Better: leave ' + fmtT(alt.dep) + ' (' + Math.abs(alt.o) + ' hr ' + (alt.o < 0 ? 'earlier' : 'later') + ').' : ' No time in this window looks better.');
    }
    const src = (s, apt) => !s ? ' <span class="wx-src">no forecast within 30 nm</span>' : s.dist ? ' <span class="wx-src">using ' + esc(s.id) + ', ' + Math.round(s.dist) + ' nm away</span>' : '';
    let h = '<section class="wx-leg"><h2>' + esc(title) + ': ' + esc(from.code) + ' → ' + esc(to.code) + '</h2>';
    h += '<p class="wx-meta">' + esc(fmtDay(depT)) + ' · ~' + Math.round(dist) + ' nm · about ' + A.formatTime(blockH) + ' with ' + esc(prof ? prof.label : 'the default 150 kt estimate') + '</p>';
    h += '<p class="wx-verdict wx-v-' + (plan.lvl || 'none') + '">' + esc(verdict) + '</p>';
    h += '<div class="wx-table" role="table"><div class="wx-row wx-head" role="row"><div role="columnheader">Leave</div><div role="columnheader">At ' + esc(from.code) + src(sf) + '</div><div role="columnheader">Land</div><div role="columnheader">At ' + esc(to.code) + src(st) + '</div><div role="columnheader">Overall</div></div>';
    rows.forEach(r => {
      const L = r.lvl ? LEVEL[r.lvl] : ['No forecast yet', 'wx-outlook'];
      h += '<div class="wx-row' + (r.o === 0 ? ' wx-plan' : '') + '" role="row"><div class="wx-time">' + esc(fmtT(r.dep)) + (r.o === 0 ? '<span class="wx-tag">Planned</span>' : '') + '</div>' + cell(from, r.pd, r.ad || { notes: [] }) + '<div class="wx-time">' + esc(fmtT(r.arr)) + '</div>' + cell(to, r.pa, r.aa || { notes: [] }) + '<div><span class="wx-level ' + L[1] + '">' + L[0] + '</span></div></div>';
    });
    return h + '</div></section>';
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
    const mins = { cig: Math.max(0, +$('mcig').value || 0), vis: Math.max(0, +$('mvis').value || 0) }; saveMins(mins);
    const limit = A.saveXwind($('xw').value); $('xw').value = limit;
    const prof = selectedProfile(), win = +$('win').value, dep = Date.parse($('dep').value), ret = Date.parse($('ret').value);
    const q = new URLSearchParams({ from: from.code, to: to.guide ? to.guide.replace(/\/$/, '') : to.code, dep: $('dep').value, ret: $('ret').value, win, ac: $('ac').value });
    history.replaceState(null, '', '?' + q);
    out.innerHTML = '<p class="wx-meta">Loading forecast…</p>';
    let h = '';
    if (isFinite(dep)) h += await leg('Going', from, to, dep, win, prof, mins, limit);
    if (isFinite(ret)) h += await leg('Coming home', to, from, ret, win, prof, mins, limit);
    if (to.guide) h += '<p class="wx-meta"><a href="../' + esc(to.guide) + '">Open the ' + esc(to.town) + ' guide</a></p>';
    out.innerHTML = h;
  }

  async function init() {
    for (const base of [LIVE, 'data/']) {
      try { const r = await fetch(base + 'run.json', { cache: 'no-cache' }); if (r.ok) { RUN = await r.json(); BASE = base; break; } } catch (e) {}
    }
    if (!RUN) { $('out').innerHTML = '<p class="wx-verdict">The forecast data could not be loaded.</p>'; return; }
    $('run').textContent = new Date(RUN.run).toLocaleString([], { weekday: 'short', month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit' }) + ' (NBM ' + RUN.run.slice(11, 13) + 'Z run' + (BASE === LIVE ? ', updated every 3 hours)' : ', saved copy)');
    $('dl').innerHTML = DEST.map(d => '<option value="' + esc(destLabel(d)) + '">').join('');
    if (window.WingAwaySuggest) WingAwaySuggest($('from'), $('fromlist'), AP);
    const p = new URLSearchParams(location.search), [d0, r0] = defaults(), m = readMins();
    let home = ''; try { home = localStorage.getItem('wingaway-home') || ''; } catch (e) {}
    $('from').value = p.get('from') || home || 'KMYR';
    const tg = p.get('to'), td = tg && DEST.find(d => d.guide === tg.replace(/\/?$/, '/'));
    $('to').value = td ? destLabel(td) : tg || destLabel(DEST.find(d => d.guide === 'charleston/') || DEST[0]);
    $('dep').value = p.get('dep') || d0; $('ret').value = p.has('ret') ? p.get('ret') : r0; $('win').value = p.get('win') || '3';
    $('mcig').value = m.cig; $('mvis').value = m.vis; $('xw').value = A.loadXwind();
    // Aircraft: the profile saved on the homepage, any preset, or the default estimate. Picking one here
    // only sets the flight time on this page; the homepage panel still owns the saved profile.
    const saved = A.load(), ac = $('ac');
    ac.innerHTML = (saved ? '<option value="saved">' + esc(saved.label) + ' (my saved numbers)</option>' : '') +
      A.PRESETS.filter(x => !x.gear || x.gear === 'land').map(x => '<option value="' + esc(x.id) + '">' + esc(x.label) + '</option>').join('') +
      '<option value="default">Default estimate (150 kt)</option>';
    ac.value = p.get('ac') && ac.querySelector('option[value="' + p.get('ac') + '"]') ? p.get('ac') : saved ? 'saved' : 'default';
    ['from', 'to', 'dep', 'ret', 'win', 'mcig', 'mvis', 'xw', 'ac'].forEach(id => $(id).addEventListener('change', draw));
    draw();
  }
  init();
})();
