// "Is the weather good this weekend?" for the homepage.
// For the home airport and every destination card shown, rates each weekend day's daytime weather
// Good, Mixed or Poor from NOAA's National Blend of Models (the same hourly files the weather page uses).
// A card's day is only as good as the worse end of the trip: home or destination.
// A planning outlook only, never a weather briefing.
(function () {
  const LIVE = 'https://ramorganmd-beep.github.io/WingAwayWeekends/wx/data/', LOCAL = 'wx/data/';
  const AP = window.WINGAWAY_AIRPORTS || [], DEST = window.WINGAWAY_DESTINATIONS || [];
  const H = 3600e3, DAY = 24 * H, NAMES = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  const RANK = { good: 0, mixed: 1, poor: 2 }, WORD = { good: 'Good', mixed: 'Mixed', poor: 'Poor' };
  const cards = document.getElementById('cards');
  if (!cards) return;

  const css = document.createElement('style');
  css.textContent = '.wk-box{grid-column:1/-1;margin:4px 0 10px;padding:14px 18px;background:#fff;border:1px solid #dbe3e9;border-left:4px solid #efbd70;border-radius:3px;font-size:.95rem;color:#33475a}' +
    '.wk-box h3{margin:0 0 6px;font-size:1.05rem;color:#102d40}.wk-box p{margin:4px 0}.wk-box .wk-fine{font-size:.8rem;color:#647784}' +
    '.wk-box a{font-weight:600}.wk-line{margin:6px 0 0;font-size:.85rem;color:#33475a;display:flex;flex-wrap:wrap;gap:4px 6px;align-items:center}' +
    '.wk{display:inline-block;padding:1px 8px;border-radius:999px;font-size:.8rem;font-weight:600;border:1px solid}' +
    '.wk.good{background:#e8f4ec;border-color:#9fcdb0;color:#24603a}.wk.mixed{background:#fdf3e2;border-color:#e9c98d;color:#7a5414}' +
    '.wk.poor{background:#fbe9e7;border-color:#e3aaa2;color:#8a2c20}.wk-line a{font-size:.8rem;margin-left:auto;position:relative;z-index:6;padding:6px 0}';
  document.head.appendChild(css);

  // ---------- data ----------
  let RUN = null, BASE = LIVE;
  const files = {};
  const getJSON = u => fetch(u).then(r => { if (!r.ok) throw new Error(r.status); return r.json(); });
  const ready = getJSON(LIVE + 'run.json').catch(() => { BASE = LOCAL; return getJSON(LOCAL + 'run.json'); })
    .then(r => { RUN = r; return Date.now() - Date.parse(r.run) < 30 * H; }).catch(() => false);
  const bucket = id => id.length === 4 && id[0] === 'K' ? id.slice(0, 3) : id.slice(0, 2);
  const load = b => files[b] || (files[b] = getJSON(BASE + 'st/' + b + '.json').catch(() => ({})));
  const station = async id => (await load(bucket(id)))[id] || null;
  const rad = x => x * Math.PI / 180;
  const nm = (a, b, c, d) => { const h = Math.sin(rad(c - a) / 2) ** 2 + Math.cos(rad(a)) * Math.cos(rad(c)) * Math.sin(rad(d - b) / 2) ** 2; return 6880.13 * Math.asin(Math.sqrt(h)); };
  const found = {};
  // The forecast station for an airport, or the nearest one within 30 nm.
  function stationFor(code, lat, lon) {
    if (found[code]) return found[code];
    return (found[code] = (async () => {
      const ids = [code, code.length === 3 ? 'K' + code : ''].filter(Boolean);
      for (const id of ids) { const s = await station(id); if (s) return s; }
      if (lat == null) { const a = AP.find(x => x[0] === code || x[1] === code); if (!a) return null; lat = a[5]; lon = a[6]; }
      const near = AP.map(a => [a, nm(lat, lon, a[5], a[6])]).filter(x => x[1] > 0.5 && x[1] <= 30).sort((a, b) => a[1] - b[1]).slice(0, 6);
      for (const [a] of near) for (const id of [a[0], a[1]].filter(Boolean)) { const s = await station(id); if (s) return s; }
      return null;
    })());
  }

  // ---------- weekend days (local time, from the airport's longitude) ----------
  const local = (t, lon) => new Date(t + lon / 15 * H); // read with getUTC*
  function weekend(lon) {
    const now = local(Date.now(), lon), dow = now.getUTCDay();
    const mid = Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate());
    const offs = dow === 0 ? [0] : dow === 6 ? [0, 1] : [5 - dow, 6 - dow, 7 - dow];
    // Skip today once most of the flying day has passed.
    return offs.filter(o => o > 0 || now.getUTCHours() < 15).map(o => ({ key: new Date(mid + o * DAY).toISOString().slice(0, 10), name: NAMES[(dow + o) % 7], today: o === 0 }));
  }

  // ---------- rating ----------
  function ratePoint(p, short) {
    const gust = Math.max(p.gst || 0, p.wsp || 0);
    if (short) {
      const c = p.cig == null || p.cig < 0 ? Infinity : p.cig * 100, v = p.vis == null ? 10 : p.vis / 10;
      if (c < 1000 || v < 3) return ['poor', 'low clouds or poor visibility'];
      if (p.tstm >= 40) return ['poor', 'thunderstorms likely'];
      if (c <= 3000 || v <= 5) return ['mixed', 'marginal ceilings'];
      if (p.tstm >= 15) return ['mixed', 'storms possible'];
      if (gust >= 25) return ['mixed', 'gusty winds'];
      if (p.rain >= 60) return ['mixed', 'rain likely'];
      return ['good', ''];
    }
    if (p.tstm >= 40) return ['poor', 'thunderstorms likely'];
    if (p.rain >= 70) return ['poor', 'rain likely'];
    if (p.tstm >= 15) return ['mixed', 'storms possible'];
    if (p.rain >= 40) return ['mixed', 'chance of rain'];
    if (gust >= 25) return ['mixed', 'gusty winds'];
    return ['good', ''];
  }
  // Daytime (8 a.m.–7 p.m. local) on one day: the 3-hourly forecast where it reaches, else the 12-hour outlook
  // ending that evening. Good when two thirds of the hours are good, Poor when two thirds are poor.
  function rateDay(rec, lon, day) {
    const r0 = Date.parse(RUN.run), now = Date.now(), pts = [];
    const onDay = (t, h0, h1) => { const d = local(t, lon); return d.toISOString().slice(0, 10) === day.key && d.getUTCHours() >= h0 && d.getUTCHours() <= h1; };
    if (rec.s) RUN.fhrS.forEach((f, i) => {
      const t = r0 + f * H; if (t < now - 2 * H || !onDay(t, 8, 19)) return;
      const s = rec.s, at = k => (s[k] || [])[i];
      pts.push(ratePoint({ cig: at('CIG'), vis: at('VIS'), wsp: at('WSP'), gst: at('GST'), tstm: at('T03'), rain: (s.P06 || [])[i] != null ? s.P06[i] : (s.P06 || [])[i + 1] }, true));
    });
    let outlook = false;
    if (!pts.length && rec.e) RUN.fhrE.forEach((f, i) => {
      const t = r0 + f * H; if (!onDay(t, 16, 23)) return;
      const e = rec.e, at = k => (e[k] || [])[i];
      pts.push(ratePoint({ wsp: at('WSP'), gst: at('GST'), tstm: at('T12'), rain: at('P12') }, false)); outlook = true;
    });
    if (!pts.length) return null;
    const n = k => pts.filter(p => p[0] === k).length;
    const level = n('good') >= pts.length * 2 / 3 ? 'good' : n('poor') >= pts.length * 2 / 3 ? 'poor' : 'mixed';
    const why = (pts.find(p => p[0] === 'poor') || pts.find(p => p[0] === 'mixed') || ['', ''])[1];
    return { level, why: level === 'good' ? '' : why, outlook };
  }
  const worse = (a, b) => !a ? b : !b ? a : RANK[b.level] > RANK[a.level] ? b : a;

  // ---------- page ----------
  let token = 0;
  async function update() {
    const my = ++token, home = cards.dataset.home || '';
    let box = document.getElementById('wk-box');
    const list = [...cards.querySelectorAll('.destination-card[data-apt]')];
    if (!home || !list.length || !(await ready)) { if (box) box.remove(); return; }
    const ha = AP.find(a => a[0] === home);
    if (!ha) return;
    const days = weekend(ha[6]);
    const hrec = await stationFor(home, ha[5], ha[6]);
    if (my !== token) return;
    const hdays = days.map(d => hrec ? rateDay(hrec, ha[6], d) : null);
    const best = days.map(() => []);
    await Promise.all(list.map(async card => {
      const apt = card.dataset.apt, lat = +card.dataset.lat, lon = +card.dataset.lon;
      const rec = await stationFor(apt, lat, lon);
      if (my !== token || !rec) return;
      const res = days.map((d, i) => { const r = worse(hdays[i], rateDay(rec, lon, d)); if (r && r.level === 'good') best[i].push(card); return r; });
      if (!res.some(Boolean)) return;
      const old = card.querySelector('.wk-line'); if (old) old.remove();
      const p = document.createElement('p'); p.className = 'wk-line';
      p.append('This weekend:');
      res.forEach((r, i) => {
        if (!r) return;
        const s = document.createElement('span'); s.className = 'wk ' + r.level;
        s.textContent = (days[i].today ? 'Today' : days[i].name) + ' · ' + WORD[r.level];
        s.title = (r.why ? r.why[0].toUpperCase() + r.why.slice(1) : 'Good both ends') + (r.outlook ? ' (early outlook)' : '');
        p.append(' ', s);
      });
      const a = document.createElement('a');
      a.href = 'wx/?from=' + encodeURIComponent(home) + '&to=' + encodeURIComponent((card.dataset.guide || apt).replace(/\/$/, ''));
      a.textContent = 'Best times to fly →';
      p.append(a);
      const meta = card.querySelector('.card-meta'); if (meta) meta.after(p);
    }));
    if (my !== token) return;
    if (!box) { box = document.createElement('div'); box.id = 'wk-box'; box.className = 'wk-box'; box.setAttribute('aria-live', 'polite'); }
    const chips = days.map((d, i) => hdays[i] ? '<span class="wk ' + hdays[i].level + '" title="' + (hdays[i].why || 'Good') + '">' + (d.today ? 'Today' : d.name) + ' · ' + WORD[hdays[i].level] + '</span>' : '').join(' ');
    const why = hdays.map((r, i) => r && r.why ? days[i].name + ': ' + r.why : '').filter(Boolean).join('; ');
    let picks = '';
    best.forEach(b => b.sort((x, y) => list.indexOf(x) - list.indexOf(y)));
    const di = best.map((b, i) => [b.length, i]).sort((a, b) => b[0] - a[0] || a[1] - b[1])[0];
    if (di && di[0]) {
      const names = best[di[1]].slice(0, 4).map(c => '<a href="#' + c.id + '">' + c.querySelector('h3').textContent + '</a>');
      picks = '<p>Good at both ends ' + (days[di[1]].today ? 'today' : 'on ' + { Fri: 'Friday', Sat: 'Saturday', Sun: 'Sunday' }[days[di[1]].name]) + ': ' + names.join(', ') + (best[di[1]].length > 4 ? ' and ' + (best[di[1]].length - 4) + ' more below' : '') + '.</p>';
    } else picks = '<p>No destination in this list looks good at both ends this weekend. Try a different flight time or region, or check back: forecasts update every hour.</p>';
    box.innerHTML = '<h3>Is the weather good this weekend?</h3><p>At ' + home + ': ' + chips + (why ? ' <span class="wk-fine">(' + why + ')</span>' : '') + '</p>' + picks +
      '<p class="wk-fine">Daytime outlook from NOAA’s National Blend of Models, updated hourly. Each card’s rating is the worse of your airport and the destination. Not a weather briefing: always get an official briefing before you fly.</p>';
    if (!box.isConnected) cards.prepend(box);
  }
  let timer = null;
  new MutationObserver(muts => {
    if (muts.every(m => [...m.addedNodes, ...m.removedNodes].every(n => n.id === 'wk-box'))) return;
    clearTimeout(timer); timer = setTimeout(update, 250);
  }).observe(cards, { childList: true });
  update();
})();
