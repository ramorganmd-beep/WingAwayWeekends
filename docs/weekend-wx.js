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
    '.wk-seg{float:right;display:inline-flex;border:1px solid #102d40;border-radius:999px;overflow:hidden;margin:0 0 6px 10px}.wk-seg button{font:inherit;font-size:13px;font-weight:600;padding:5px 12px;border:0;background:#fff;color:#102d40;cursor:pointer}.wk-seg button+button{border-left:1px solid #102d40}.wk-seg button[aria-pressed=true]{background:#102d40;color:#fff}@media(max-width:560px){.wk-seg{float:none;margin:0 0 8px}}' +
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
  // The days that matter for the trip length chosen on the homepage:
  // Day trip = Saturday; Weekend = Fri–Sun; Longer stay = Thu–Mon. Once most of today's flying day has passed
  // (3 p.m. local), count from tomorrow, so late Sunday rolls to next weekend.
  const FULL = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  function weekend(lon, trip, next) {
    const now = local(Date.now(), lon), shift = now.getUTCHours() >= 15 ? 1 : 0;
    let dow = (now.getUTCDay() + shift) % 7, mid = Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate()) + shift * DAY, base = shift;
    const range = (a, b) => Array.from({ length: b - a + 1 }, (_, i) => a + i);
    const pick = d => trip === 'Day trip' ? (d === 0 || d === 6 ? [0] : [6 - d])
      : trip === 'Longer stay' ? (d === 0 ? [0, 1] : range(Math.max(0, 4 - d), 8 - d))
      : (d === 0 ? [0] : range(Math.max(0, 5 - d), 7 - d));
    let offs = pick(dow);
    if (next) {
      // The following weekend: count from the Monday after this one ends.
      const last = offs[offs.length - 1], lastDow = (dow + last) % 7, toMon = ((8 - lastDow) % 7) || 7;
      mid += (last + toMon) * DAY; base += last + toMon; dow = 1; offs = pick(1);
    }
    return offs.map(o => ({ key: new Date(mid + o * DAY).toISOString().slice(0, 10), name: NAMES[(dow + o) % 7], full: FULL[(dow + o) % 7], today: o + base === 0 }));
  }
  let NEXT = false; try { NEXT = localStorage.getItem('wingaway-wk') === 'next'; } catch (e) {}
  cards.addEventListener('click', e => {
    const b = e.target.closest && e.target.closest('[data-wk]'); if (!b) return;
    NEXT = b.dataset.wk === 'next'; try { localStorage.setItem('wingaway-wk', NEXT ? 'next' : 'this'); } catch (x) {}
    update();
  });

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
    const trip = (document.getElementById('trip') || {}).value || 'Weekend', days = weekend(ha[6], trip, NEXT);
    const LABEL = NEXT ? ({ 'Day trip': ['Next Saturday:', 'for a day trip next Saturday'], 'Longer stay': ['Next long weekend:', 'for a long weekend next week'] }[trip] || ['Next weekend:', 'next weekend'])
      : ({ 'Day trip': ['Day trip:', 'for a day trip'], 'Longer stay': ['Long weekend:', 'for a long weekend'] }[trip] || ['This weekend:', 'this weekend']);
    // Open the weather page on these same days: leave the first morning (or in an hour or two today), back the last afternoon.
    const MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    const span = ds => { const a = ds[0].key.split('-').map(Number), b = ds[ds.length - 1].key.split('-').map(Number);
      return MON[a[1] - 1] + ' ' + a[2] + (ds.length > 1 ? '–' + (b[1] !== a[1] ? MON[b[1] - 1] + ' ' : '') + b[2] : ''); };
    const SEG = '<div class="wk-seg" role="group" aria-label="Which weekend"><button type="button" data-wk="this" aria-pressed="' + !NEXT + '">' + span(weekend(ha[6], trip, false)) + '</button><button type="button" data-wk="next" aria-pressed="' + NEXT + '">' + span(weekend(ha[6], trip, true)) + '</button></div>';
    const nowH = local(Date.now(), ha[6]).getUTCHours(), first = days[0], last = days[days.length - 1];
    const depH = first.today ? Math.min(Math.max(nowH + 2, 10), 16) : 10, retH = last === first ? Math.max(depH + 4, 16) : 14;
    const pad = n => String(n).padStart(2, '0');
    const when = '&dep=' + encodeURIComponent(first.key + 'T' + pad(depH) + ':00') + '&ret=' + encodeURIComponent(last.key + 'T' + pad(Math.min(retH, 20)) + ':00');
    const hrec = await stationFor(home, ha[5], ha[6]);
    if (my !== token) return;
    const hdays = days.map(d => hrec ? rateDay(hrec, ha[6], d) : null);
    const best = days.map(() => []);
    await Promise.all(list.map(async card => {
      const apt = card.dataset.apt, lat = +card.dataset.lat, lon = +card.dataset.lon;
      const rec = await stationFor(apt, lat, lon);
      if (my !== token || !rec) return;
      const res = days.map((d, i) => { const r = worse(hdays[i], rateDay(rec, lon, d)); if (r && r.level === 'good') best[i].push(card); return r; });
      const old = card.querySelector('.wk-line'); if (old) old.remove();
      if (!res.some(Boolean)) return;
      const p = document.createElement('p'); p.className = 'wk-line';
      p.append(LABEL[0]);
      res.forEach((r, i) => {
        if (!r) return;
        const s = document.createElement('span'); s.className = 'wk ' + r.level;
        s.textContent = (days[i].today ? 'Today' : days[i].name) + ' · ' + WORD[r.level];
        s.title = (r.why ? r.why[0].toUpperCase() + r.why.slice(1) : 'Good both ends') + (r.outlook ? ' (early outlook)' : '');
        p.append(' ', s);
      });
      const a = document.createElement('a');
      a.href = 'wx/?from=' + encodeURIComponent(home) + '&to=' + encodeURIComponent((card.dataset.guide || apt).replace(/\/$/, '')) + when + '#out';
      a.textContent = 'Best times to fly →';
      p.append(a);
      const meta = card.querySelector('.card-meta'); if (meta) meta.after(p);
    }));
    if (my !== token) return;
    if (!box) { box = document.createElement('div'); box.id = 'wk-box'; box.className = 'wk-box'; box.setAttribute('aria-live', 'polite'); }
    const chips = days.map((d, i) => hdays[i] ? '<span class="wk ' + hdays[i].level + '" title="' + (hdays[i].why || 'Good') + '">' + (d.today ? 'Today' : d.name) + ' · ' + WORD[hdays[i].level] + '</span>' : '').join(' ');
    const why = hdays.map((r, i) => r && r.why ? days[i].name + ': ' + r.why : '').filter(Boolean).join('; ');
    const none = !hdays.some(Boolean);
    let picks = '';
    best.forEach(b => b.sort((x, y) => list.indexOf(x) - list.indexOf(y)));
    const di = best.map((b, i) => [b.length, i]).sort((a, b) => b[0] - a[0] || a[1] - b[1])[0];
    if (di && di[0]) {
      const names = best[di[1]].slice(0, 4).map(c => '<a href="#' + c.id + '">' + c.querySelector('h3').textContent + '</a>');
      picks = '<p>Good at both ends ' + (days[di[1]].today ? 'today' : 'on ' + days[di[1]].full) + ': ' + names.join(', ') + (best[di[1]].length > 4 ? ' and ' + (best[di[1]].length - 4) + ' more below' : '') + '.</p>';
    } else picks = '<p>No destination in this list looks good at both ends ' + LABEL[1] + '. Try a different flight time or region, or check back: forecasts update every hour.</p>';
    if (none) {
      box.innerHTML = SEG + '<h3>Is the weather good ' + (trip === 'Day trip' ? 'for a day trip, ' : trip === 'Longer stay' ? 'for a long weekend, ' : 'for the weekend of ') + span(days) + '?</h3>' +
        '<p>' + days.map(d => d.full).join(', ').replace(/, ([^,]*)$/, ' and $1') + ' ' + (days.length > 1 ? 'are' : 'is') + ' beyond NOAA’s 7-day forecast. Check back closer to the weekend.</p>';
    } else {
      box.innerHTML = SEG + '<h3>Is the weather good ' + (trip === 'Day trip' ? 'for a day trip, ' : trip === 'Longer stay' ? 'for a long weekend, ' : 'for the weekend of ') + span(days) + '?</h3><p>At ' + home + ': ' + chips + (why ? ' <span class="wk-fine">(' + why + ')</span>' : '') + '</p>' + picks +
        '<p><a href="weekend-map/?from=' + encodeURIComponent(home) + '&trip=' + encodeURIComponent(trip) + (NEXT ? '&wk=next' : '') + (document.getElementById('region') && document.getElementById('region').value ? '&region=' + encodeURIComponent(document.getElementById('region').value) : '') + '">See the weekend weather map →</a></p>' + '<p class="wk-fine">Daytime outlook from NOAA’s National Blend of Models, updated hourly. Each card’s rating is the worse of your airport and the destination. Not a weather briefing: always get an official briefing before you fly.</p>';
    }
    if (!box.isConnected) cards.prepend(box);
  }
  let timer = null;
  new MutationObserver(muts => {
    if (muts.every(m => [...m.addedNodes, ...m.removedNodes].every(n => n.id === 'wk-box'))) return;
    clearTimeout(timer); timer = setTimeout(update, 250);
  }).observe(cards, { childList: true });
  update();
})();
