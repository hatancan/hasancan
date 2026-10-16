/* hasancan.net canlı bileşenler: ziyaretçi sayacı, ziyaretçi defteri, anket, Winamp.
   Arka uç: /api (api/sunucu.py). Kullanıcı metni her zaman textContent ile yazılır. */
(function () {
  function t(k) {
    var s = window.I18N || {};
    var d = s[document.documentElement.lang] || {};
    return d[k] || (s.tr || {})[k] || k;
  }

  function istek(yol, veri) {
    return fetch('/api' + yol, {
      method: veri ? 'POST' : 'GET',
      headers: veri ? { 'Content-Type': 'application/json' } : {},
      body: veri ? JSON.stringify(veri) : undefined
    }).then(function (r) {
      return r.json().then(function (j) { j._kod = r.status; return j; });
    });
  }

  function depo(islem, ad, deger) {
    try {
      if (islem === 'al') return localStorage.getItem(ad);
      localStorage.setItem(ad, deger);
    } catch (e) { return null; }
  }

  /* ---- sayaç ---- */
  function sayacYaz(n) {
    var el = document.getElementById('sayac');
    if (!el) return;
    el.innerHTML = '';
    String(n).padStart(6, '0').split('').forEach(function (c) {
      var s = document.createElement('span');
      s.textContent = c;
      el.appendChild(s);
    });
    el.setAttribute('aria-label', String(n));
  }

  /* ---- ziyaretçi defteri ---- */
  function tarih(iso) {
    var d = new Date(iso);
    return isNaN(d) ? '' : [d.getDate(), d.getMonth() + 1, d.getFullYear()]
      .map(function (x) { return String(x).padStart(2, '0'); }).join('.');
  }

  function defterYaz(liste) {
    var kap = document.getElementById('defter-liste');
    if (!kap || !liste || !liste.length) return;
    kap.innerHTML = '';
    liste.forEach(function (k) {
      var kayit = document.createElement('div');
      kayit.className = 'defter-kayit';
      var av = document.createElement('span');
      av.className = 'mini-avatar';
      av.setAttribute('aria-hidden', 'true');
      av.textContent = (k.ad || '?').charAt(0).toUpperCase();
      var ic = document.createElement('div');
      var b = document.createElement('b'); b.textContent = k.ad;
      var sm = document.createElement('small'); sm.textContent = ' ' + tarih(k.zaman);
      var p = document.createElement('p'); p.textContent = k.mesaj;
      ic.appendChild(b); ic.appendChild(sm); ic.appendChild(p);
      kayit.appendChild(av); kayit.appendChild(ic);
      kap.appendChild(kayit);
    });
  }

  var form = document.getElementById('defter-form');
  if (form) form.addEventListener('submit', function (e) {
    e.preventDefault();
    var durum = document.getElementById('defter-durum');
    var dugme = form.querySelector('button');
    dugme.disabled = true;
    istek('/defter', { ad: form.ad.value, mesaj: form.mesaj.value, web: form.web.value })
      .then(function (d) {
        if (d._kod === 429) durum.textContent = t('gb.fast');
        else if (d._kod >= 400) durum.textContent = t('gb.empty');
        else {
          durum.textContent = t(d.durum === 'bekliyor' ? 'gb.pending' : 'gb.ok');
          form.mesaj.value = '';
          uygula(d);
        }
      })
      .catch(function () { durum.textContent = t('gb.error'); })
      .then(function () { dugme.disabled = false; });
  });

  /* ---- anket ---- */
  var anket = document.getElementById('anket');
  var anketKimlik = null;

  function anketYaz(a, goster) {
    if (!anket || !a) return;
    anketKimlik = a.kimlik;
    var oyVerdi = depo('al', 'anket-' + a.kimlik);
    if (!goster && !oyVerdi) return;
    var toplam = a.oylar.reduce(function (x, y) { return x + y; }, 0) || 1;
    anket.querySelectorAll('.anket-sonuc').forEach(function (s, i) {
      var oran = Math.round(100 * a.oylar[i] / toplam);
      s.textContent = '%' + oran + ' (' + a.oylar[i] + ')';
      s.parentElement.style.setProperty('--oran', oran + '%');
    });
    anket.classList.add('sonuclu');
    anket.querySelectorAll('input, button').forEach(function (x) { x.disabled = true; });
    if (oyVerdi && oyVerdi !== '-1') {
      var r = anket.querySelector('input[value="' + oyVerdi + '"]');
      if (r) r.checked = true;
    }
  }

  if (anket) anket.addEventListener('submit', function (e) {
    e.preventDefault();
    var secili = anket.querySelector('input[name="secim"]:checked');
    var durum = document.getElementById('anket-durum');
    if (!secili) { durum.textContent = t('poll.pick'); return; }
    istek('/anket', { anket: anketKimlik, secim: parseInt(secili.value, 10) })
      .then(function (d) {
        depo('koy', 'anket-' + anketKimlik, secili.value);
        durum.textContent = t('poll.thanks');
        anketYaz(d.anket, true);
      })
      .catch(function () { durum.textContent = t('gb.error'); });
  });

  function uygula(d) {
    if (!d) return;
    if (typeof d.sayac === 'number') sayacYaz(d.sayac);
    if (d.defter) defterYaz(d.defter);
    if (d.anket) anketYaz(d.anket, false);
  }

  var sayildi = null;
  try { sayildi = sessionStorage.getItem('sayildi'); } catch (e) { /* özel pencere */ }
  istek(sayildi ? '/durum' : '/sayac', sayildi ? null : {})
    .then(function (d) {
      try { sessionStorage.setItem('sayildi', '1'); } catch (e) { /* yok say */ }
      uygula(d);
    })
    .catch(function () { /* arka uç yoksa sayfa yine çalışır */ });

  /* ---- Winamp ---- */
  var ses = document.getElementById('winamp-ses');
  var winamp = document.getElementById('winamp');
  if (ses && winamp) {
    var sure = document.getElementById('winamp-sure');
    var cubuk = document.getElementById('winamp-ilerleme');
    var dk = function (x) {
      x = Math.floor(x || 0);
      return String(Math.floor(x / 60)).padStart(2, '0') + ':' + String(x % 60).padStart(2, '0');
    };
    ses.addEventListener('timeupdate', function () {
      sure.textContent = dk(ses.currentTime);
      if (ses.duration) cubuk.style.width = (100 * ses.currentTime / ses.duration) + '%';
    });
    ses.addEventListener('play', function () { winamp.classList.add('caliyor'); });
    ses.addEventListener('pause', function () { winamp.classList.remove('caliyor'); });
    ses.addEventListener('ended', function () { ses.currentTime = 0; ses.play(); });   // döngü
    winamp.addEventListener('click', function (e) {
      var b = e.target.closest('[data-winamp]');
      if (!b) return;
      var k = b.getAttribute('data-winamp');
      if (k === 'cal') ses.play();
      else if (k === 'duraklat') ses.pause();
      else if (k === 'durdur') { ses.pause(); ses.currentTime = 0; sure.textContent = '00:00'; cubuk.style.width = '0'; }
      else if (k === 'basa') { ses.currentTime = 0; if (ses.paused) ses.play(); }
    });
  }
})();
