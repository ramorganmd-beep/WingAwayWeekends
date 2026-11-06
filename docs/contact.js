/* WingAway Weekends: reliable "email us" links.
   A plain mailto: link does nothing on devices without a default email app
   (common on desktop browsers and for people who use webmail). This turns every
   mailto link into a small chooser: email app, Gmail, Outlook, or copy the address. */
(function () {
  'use strict';
  var css = '' +
    '.wa-mail-back{position:fixed;inset:0;background:rgba(16,45,64,.45);z-index:9999;display:flex;align-items:center;justify-content:center;padding:16px}' +
    '.wa-mail{background:#fff;color:#102d40;border-radius:8px;max-width:360px;width:100%;padding:22px 22px 16px;box-shadow:0 12px 40px rgba(0,0,0,.25);font:15px/1.45 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}' +
    '.wa-mail h2{font:600 18px/1.3 Georgia,serif;margin:0 0 4px}' +
    '.wa-mail p{margin:0 0 14px;color:#526471;font-size:14px;word-break:break-word}' +
    '.wa-mail a,.wa-mail button{display:block;width:100%;box-sizing:border-box;text-align:center;margin:0 0 8px;padding:11px 12px;border-radius:5px;border:1px solid #bac9d4;background:#fff;color:#102d40;font:600 15px system-ui,sans-serif;text-decoration:none;cursor:pointer}' +
    '.wa-mail a.primary{background:#102d40;border-color:#102d40;color:#fff}' +
    '.wa-mail .wa-close{border:0;background:none;color:#526471;font-weight:500;margin:4px 0 0}';
  var styled = false, back = null;

  function parse(href) {
    var m = /^mailto:([^?]*)\??(.*)$/i.exec(href) || [];
    var to = decodeURIComponent(m[1] || ''), subject = '';
    (m[2] || '').split('&').forEach(function (kv) {
      var p = kv.split('=');
      if ((p[0] || '').toLowerCase() === 'subject') subject = decodeURIComponent((p[1] || '').replace(/\+/g, ' '));
    });
    return { to: to, subject: subject };
  }

  function close() { if (back) { back.remove(); back = null; } }

  function copy(text, btn) {
    function done() { btn.textContent = 'Copied: ' + text; }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done, fallback);
    } else { fallback(); }
    function fallback() {
      var t = document.createElement('textarea'); t.value = text; t.setAttribute('readonly', '');
      t.style.position = 'fixed'; t.style.opacity = '0'; document.body.appendChild(t); t.select();
      try { document.execCommand('copy'); done(); } catch (e) { btn.textContent = text; }
      t.remove();
    }
  }

  function open(href) {
    if (!styled) { var s = document.createElement('style'); s.textContent = css; document.head.appendChild(s); styled = true; }
    close();
    var d = parse(href), enc = encodeURIComponent;
    var gmail = 'https://mail.google.com/mail/?view=cm&fs=1&to=' + enc(d.to) + '&su=' + enc(d.subject);
    var outlook = 'https://outlook.live.com/mail/0/deeplink/compose?to=' + enc(d.to) + '&subject=' + enc(d.subject);
    back = document.createElement('div'); back.className = 'wa-mail-back';
    back.innerHTML = '<div class="wa-mail" role="dialog" aria-modal="true" aria-labelledby="wa-mail-h">' +
      '<h2 id="wa-mail-h">Email WingAway Weekends</h2><p>' + d.to + (d.subject ? '<br>Subject: ' + d.subject.replace(/</g, '&lt;') : '') + '</p>' +
      '<a class="primary" data-mail href="' + href.replace(/"/g, '&quot;') + '">Open my email app</a>' +
      '<a href="' + gmail + '" target="_blank" rel="noopener">Write in Gmail</a>' +
      '<a href="' + outlook + '" target="_blank" rel="noopener">Write in Outlook.com</a>' +
      '<button type="button" data-copy>Copy the email address</button>' +
      '<button type="button" class="wa-close" data-close>Close</button></div>';
    back.addEventListener('click', function (e) {
      if (e.target === back || e.target.hasAttribute('data-close')) { close(); return; }
      if (e.target.hasAttribute('data-copy')) { copy(d.to, e.target); return; }
      if (e.target.tagName === 'A') { setTimeout(close, 300); }
    });
    document.body.appendChild(back);
    back.querySelector('[data-mail]').focus();
  }

  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href^="mailto:"]');
    if (!a || a.hasAttribute('data-mail')) return;
    e.preventDefault();
    open(a.getAttribute('href'));
  });
})();
