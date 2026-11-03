// Fast airport suggestions: fills a <datalist> with only the best ~10 matches as the user types,
// instead of loading all 5,000+ U.S. airports into it (which made typing slow, especially on iPad).
window.WingAwaySuggest = function (input, list, airports) {
  const rows = airports.map(a => [a, (a[0] + ' ' + (a[1] || '')).toUpperCase(), (a[2] + ' ' + a[3]).toUpperCase()]);
  let timer = 0, last = null;
  function update() {
    const q = input.value.trim().toUpperCase();
    if (q === last) return;
    last = q;
    const out = [];
    if (q.length >= 2) {
      const kq = q.length === 3 ? 'K' + q : '';
      const best = [], good = [], ok = [];
      for (const r of rows) {
        const [a, codes, words] = r;
        if (a[0] === q || a[1] === q || a[0] === kq) best.push(a);
        else if (a[0].startsWith(q) || (a[1] && a[1].startsWith(q)) || (kq && a[0].startsWith(kq))) good.push(a);
        else if (q.length >= 3 && words.includes(q)) ok.push(a);
        if (best.length + good.length >= 10) break;
      }
      out.push(...best, ...good, ...ok);
    }
    list.replaceChildren(...out.slice(0, 10).map(a => { const o = document.createElement('option'); o.value = a[0]; o.label = a[2] + ', ' + a[3] + ', ' + a[4]; o.textContent = o.label; return o; }));
  }
  input.addEventListener('input', () => { clearTimeout(timer); timer = setTimeout(update, 80); });
  input.addEventListener('focus', update);
};
