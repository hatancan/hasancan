#!/usr/bin/env python3
"""hasancan.net küçük arka ucu: ziyaretçi sayacı, ziyaretçi defteri, haftanın anketi.

Yalnız Python standart kütüphanesi + SQLite. Caddy, /api/* isteklerini 127.0.0.1:3030'a iletir.

  python3 -I api/sunucu.py            # sunucu
  python3 -I api/sunucu.py liste      # defter kayıtları (onay bekleyenler dahil)
  python3 -I api/sunucu.py onayla ID  # bekleyen mesajı yayınla
  python3 -I api/sunucu.py sil ID     # mesajı sil

Kişisel veri: IP adresi SAKLANMAZ. Kötüye kullanımı sınırlamak için IP, gizli bir tuzla tek yönlü
özetlenir (sha256); sayaç için tuz her gün yenilenir, böylece günler arası iz sürülemez.
"""
import hashlib, json, os, re, secrets, sqlite3, sys, threading, time
from datetime import date, datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

VERI = os.environ.get('HASANCAN_VERI', '/home/hasan/hasancan-veri/site.db')
PORT = int(os.environ.get('HASANCAN_PORT', '3030'))
ANKET = 'ilk-sosyal-ag'          # şu anki anket kimliği
SECENEK_SAYISI = 4
yazma_kilidi = threading.Lock()


def db():
    os.makedirs(os.path.dirname(VERI), exist_ok=True)
    c = sqlite3.connect(VERI, timeout=10)
    c.execute('PRAGMA journal_mode=WAL')
    c.executescript('''
      CREATE TABLE IF NOT EXISTS ayar (ad TEXT PRIMARY KEY, deger TEXT);
      CREATE TABLE IF NOT EXISTS sayac (gun TEXT, ozet TEXT, PRIMARY KEY (gun, ozet));
      CREATE TABLE IF NOT EXISTS defter (id INTEGER PRIMARY KEY, zaman TEXT, ad TEXT, mesaj TEXT,
                                         yayinda INTEGER, ozet TEXT);
      CREATE TABLE IF NOT EXISTS oy (anket TEXT, ozet TEXT, secim INTEGER, PRIMARY KEY (anket, ozet));
    ''')
    return c


def tuz(c, ad):
    r = c.execute('SELECT deger FROM ayar WHERE ad=?', (ad,)).fetchone()
    if r:
        return r[0]
    t = secrets.token_hex(16)
    c.execute('INSERT INTO ayar VALUES (?,?)', (ad, t))
    c.commit()
    return t


def ozet(c, ip, kapsam):
    return hashlib.sha256(f'{tuz(c, kapsam)}|{ip}'.encode()).hexdigest()[:20]


def durum(c):
    toplam = c.execute('SELECT COUNT(*) FROM sayac').fetchone()[0]
    defter = [dict(id=i, zaman=z, ad=a, mesaj=m) for i, z, a, m in
              c.execute('SELECT id, zaman, ad, mesaj FROM defter WHERE yayinda=1 ORDER BY id DESC LIMIT 12')]
    oylar = [0] * SECENEK_SAYISI
    for s, n in c.execute('SELECT secim, COUNT(*) FROM oy WHERE anket=? GROUP BY secim', (ANKET,)):
        if 0 <= s < SECENEK_SAYISI:
            oylar[s] = n
    return {'sayac': toplam, 'defter': defter, 'anket': {'kimlik': ANKET, 'oylar': oylar}}


class Isleyici(BaseHTTPRequestHandler):
    server_version = 'hasancan-api'

    def log_message(self, *a):        # erişim kaydı tutma (IP yazılmasın)
        pass

    def ip(self):
        xff = self.headers.get('X-Forwarded-For', '')
        return (xff.split(',')[0].strip() or self.client_address[0])[:64]

    def cevap(self, kod, veri):
        b = json.dumps(veri, ensure_ascii=False).encode()
        self.send_response(kod)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Cache-Control', 'no-store')
        self.send_header('Content-Length', str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def govde(self):
        n = min(int(self.headers.get('Content-Length') or 0), 4096)
        try:
            return json.loads(self.rfile.read(n) or b'{}')
        except ValueError:
            return {}

    def do_GET(self):
        if self.path.split('?')[0] != '/api/durum':
            return self.cevap(404, {'hata': 'yok'})
        c = db()
        try:
            self.cevap(200, durum(c))
        finally:
            c.close()

    def do_POST(self):
        yol = self.path.split('?')[0]
        veri = self.govde()
        c = db()
        try:
            with yazma_kilidi:
                if yol == '/api/sayac':
                    gun = date.today().isoformat()
                    c.execute('INSERT OR IGNORE INTO sayac VALUES (?,?)', (gun, ozet(c, self.ip(), 'sayac-' + gun)))
                    c.commit()
                    return self.cevap(200, durum(c))
                if yol == '/api/defter':
                    return self.defter(c, veri)
                if yol == '/api/anket':
                    s = veri.get('secim')
                    if not isinstance(s, int) or not 0 <= s < SECENEK_SAYISI or veri.get('anket') != ANKET:
                        return self.cevap(400, {'hata': 'gecersiz'})
                    c.execute('INSERT OR IGNORE INTO oy VALUES (?,?,?)', (ANKET, ozet(c, self.ip(), 'anket'), s))
                    c.commit()
                    return self.cevap(200, durum(c))
            self.cevap(404, {'hata': 'yok'})
        finally:
            c.close()

    def defter(self, c, veri):
        if veri.get('web'):                       # bal küpü alanı: botlar doldurur
            return self.cevap(200, {'durum': 'tamam'})
        ad = re.sub(r'\s+', ' ', str(veri.get('ad', ''))).strip()[:40]
        mesaj = re.sub(r'[ \t]+', ' ', str(veri.get('mesaj', ''))).strip()[:500]
        if not ad or not mesaj:
            return self.cevap(400, {'hata': 'bos'})
        oz = ozet(c, self.ip(), 'defter')
        simdi = time.time()
        son = c.execute('SELECT zaman FROM defter WHERE ozet=? ORDER BY id DESC LIMIT 1', (oz,)).fetchone()
        if son and simdi - datetime.fromisoformat(son[0]).timestamp() < 120:
            return self.cevap(429, {'hata': 'hizli'})
        bugun = c.execute("SELECT COUNT(*) FROM defter WHERE ozet=? AND zaman >= ?",
                          (oz, date.today().isoformat())).fetchone()[0]
        if bugun >= 5:
            return self.cevap(429, {'hata': 'hizli'})
        bekle = bool(re.search(r'https?://|www\.|\[url|<a\s', mesaj + ad, re.I))   # bağlantılı mesaj onaya düşer
        c.execute('INSERT INTO defter (zaman, ad, mesaj, yayinda, ozet) VALUES (?,?,?,?,?)',
                  (datetime.now(timezone.utc).isoformat(timespec='seconds'), ad, mesaj, 0 if bekle else 1, oz))
        c.commit()
        self.cevap(200, {'durum': 'bekliyor' if bekle else 'yayinda', **durum(c)})


def yonet(argv):
    c = db()
    if argv[0] == 'liste':
        for r in c.execute('SELECT id, zaman, yayinda, ad, mesaj FROM defter ORDER BY id DESC'):
            print(f"{r[0]:>4} {r[1]} {'yayında' if r[2] else 'BEKLİYOR'}  {r[3]}: {r[4][:120]}")
    elif argv[0] in ('onayla', 'sil') and len(argv) == 2:
        if argv[0] == 'onayla':
            c.execute('UPDATE defter SET yayinda=1 WHERE id=?', (int(argv[1]),))
        else:
            c.execute('DELETE FROM defter WHERE id=?', (int(argv[1]),))
        c.commit()
        print('tamam')
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        yonet(sys.argv[1:])
    else:
        db().close()
        ThreadingHTTPServer(('127.0.0.1', PORT), Isleyici).serve_forever()
