/* hasancan.net — dil seçimi ve küçük dönem süsleri.
   Metinler assets/lang/{tr,en,de}.js içinde; öğeler data-i18n="anahtar" ile bağlanır.
   data-i18n-attr="aria-label:anahtar;title:anahtar" öznitelikleri çevirir. */
(function () {
  var DILLER = ['tr', 'en', 'de'];
  var VARSAYILAN = 'tr';
  var sozluk = window.I18N || {};
  var basla = (window.performance && performance.now) ? performance.now() : 0;
  var mevcut = VARSAYILAN;

  function kayitliDil() {
    try { return localStorage.getItem('dil'); } catch (e) { return null; }
  }
  function dilKaydet(dil) {
    try { localStorage.setItem('dil', dil); } catch (e) { /* özel pencere vb. */ }
  }

  function dilSec() {
    var p = new URLSearchParams(location.search).get('lang');
    if (DILLER.indexOf(p) > -1) return p;
    var k = kayitliDil();
    if (DILLER.indexOf(k) > -1) return k;
    var t = (navigator.language || '').slice(0, 2).toLowerCase();
    return DILLER.indexOf(t) > -1 ? t : VARSAYILAN;
  }

  function metin(dil, anahtar) {
    var s = sozluk[dil] || {};
    if (anahtar in s) return s[anahtar];
    var v = sozluk[VARSAYILAN] || {};
    return anahtar in v ? v[anahtar] : anahtar;
  }

  function uygula(dil) {
    mevcut = dil;
    document.documentElement.lang = dil;
    document.title = metin(dil, 'meta.title');
    var md = document.querySelector('meta[name="description"]');
    if (md) md.setAttribute('content', metin(dil, 'meta.desc'));

    // Sözlükler kendi statik dosyalarımız, kullanıcı girdisi yok: küçük HTML (<b>, <a>) serbest.
    document.querySelectorAll('[data-i18n]').forEach(function (el) {
      el.innerHTML = metin(dil, el.getAttribute('data-i18n'));
    });
    document.querySelectorAll('[data-i18n-attr]').forEach(function (el) {
      el.getAttribute('data-i18n-attr').split(';').forEach(function (cift) {
        var p = cift.split(':');
        if (p.length === 2) el.setAttribute(p[0].trim(), metin(dil, p[1].trim()));
      });
    });
    document.querySelectorAll('[data-dil]').forEach(function (b) {
      b.setAttribute('aria-pressed', b.getAttribute('data-dil') === dil ? 'true' : 'false');
    });
    sureyiYaz();
  }

  function sureyiYaz() {
    var el = document.getElementById('olusturma');
    if (!el || !basla) return;
    var sn = ((performance.now() - basla) / 1000).toFixed(4);
    el.innerHTML = metin(mevcut, 'footer.gen').replace('{s}', sn);
  }

  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-dil]');
    if (!b) return;
    var dil = b.getAttribute('data-dil');
    dilKaydet(dil);
    var u = new URL(location.href);
    u.searchParams.set('lang', dil);
    history.replaceState(null, '', u);
    uygula(dil);
  });

  // Yonja usulü "göz kırp"
  var goz = document.getElementById('goz-kirp');
  if (goz) goz.addEventListener('click', function () {
    goz.innerHTML = metin(mevcut, 'profile.winked');
    goz.classList.remove('goz-kirpildi');
    void goz.offsetWidth;
    goz.classList.add('goz-kirpildi');
  });

  // Sekmelerde etkin olanı kaydırmaya göre işaretle
  var sekmeler = document.querySelectorAll('.sekmeler a');
  function aktifSekme() {
    var h = location.hash || '#ana';
    sekmeler.forEach(function (a) { a.classList.toggle('aktif', a.getAttribute('href') === h); });
  }
  window.addEventListener('hashchange', aktifSekme);

  var yil = document.getElementById('yil');
  if (yil) yil.textContent = new Date().getFullYear();

  uygula(dilSec());
  aktifSekme();
})();
