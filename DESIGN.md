# hasancan.net — Tasarım Notları

Bu dosya sitenin tasarım çerçevesidir. **Sonraki bütün tasarım işleri bu çerçevede yapılır.**
Yeni bir bölüm, sayfa ya da bileşen eklerken önce burayı oku.

## Ruh: 2005–2010 Türkiye interneti

Hasan Can'ın (X: [@pahrguard](https://x.com/pahrguard)) 2000'lerin başından beri bu işlerin
meraklısı. Hayatına iz bırakan dönem özellikle **2005–2010**:

- **Facebook** yeni çıkıyordu: lacivert üst bar, beyaz kutular, ince gri çerçeveler, "Durum:" satırı
- **Yonja.com**: profil kartları, "göz kırp", renkli, sıcak, Türkçe sosyal ağ
- **Hattrick.org**: tablolar, yeşil tonlar, yetenek seviyesi kelimeleri ("mükemmel", "dünya klası"), istatistik kutuları
- **Knight Online**: karakter kartı, level, XP barı, koyu/altın tonlar
- Dönemin genel dokusu: MSN Messenger durumu, Winamp, ziyaretçi sayacı, ziyaretçi defteri / shoutbox,
  88×31 rozetler, "Beta" yıldız etiketi, "1024×768'de en iyi görünür", forumlar, IRC (#webmasters),
  LAN partileri, disketler, "my_project v1.0"

X kapak görseli de aynı hikâyeyi anlatıyor: CRT monitör, `ping localhost`, mIRC, Apache rozeti,
"THINGS TO BUILD: Personal Website, Forum, Guestbook, File Upload, Chat System, CMS…",
"1999 — no Google, no Facebook, no YouTube, just imagination".

## Görsel dil ("Web 2.0")

| Öğe | Kural |
|---|---|
| Yerleşim | Ortalanmış sabit genişlik (en fazla **960px**), 3 sütun: sol profil, orta içerik, sağ yan bilgi. Mobilde tek sütuna iner. |
| Fontlar | Sistem fontları, dönemin kendileri: `Tahoma, Verdana, "Lucida Grande", "Trebuchet MS"` (başlıklarda Trebuchet). Temel boyut 12–13px hissi; mobilde okunur kalacak kadar büyür. |
| Renk | Facebook laciverti `#3b5998` (ana), Hattrick yeşili `#5a8f29` (vurgu/başarı), Yonja turuncu/pembesi `#ff6600` / `#e0457b` (sıcak vurgu), Knight altını `#c9a227` (oyun öğeleri). Zemin açık mavi-gri, ince çizgili desen. |
| Parlaklık | Butonlar ve başlık barları **parlak (glossy)** gradyan: üst yarı açık, alt yarı koyu, 1px iç beyaz çizgi. Yuvarlak köşe 4–6px. |
| Kutular | Beyaz kutu, 1px `#c3cddf` çerçeve, renkli başlık şeridi. Facebook profil kutuları gibi. |
| Detaylar | "BETA" yıldız rozeti, yansımalı logo, sekmeli menü, kayan "son dakika" şeridi, 88×31 rozetler, ziyaretçi sayacı rakamları, çevrimiçi yeşil noktası. |
| Yasak | Modern düz (flat) tasarım, devasa hero görseller, tam ekran bölümler, glassmorphism, büyük yuvarlak kartlar, emoji ağırlıklı arayüz. |

Nostalji **sevgiyle** yapılır, parodiye kaçmaz: okunurluk, erişilebilirlik ve mobil uyum korunur.
Hareketli öğeler `prefers-reduced-motion`'a saygı duyar. Sahte veri yok: sayaç gibi gerçek bir
kaynağa bağlanmamış öğeler yer tutucu olarak işaretli kalır.

## Diller

Site 3 dilde: **Türkçe (varsayılan)**, İngilizce, Almanca. Metinler `assets/lang/{tr,en,de}.js`
içinde, sayfadaki öğeler `data-i18n="anahtar"` ile bağlanır. Yeni metin eklerken **üç dile birden**
ekle. Dil seçimi: `?lang=` → tarayıcıda kayıtlı seçim → tarayıcı dili → Türkçe.

## İçerik doldurma

Henüz doldurulmamış alanlar sarı, kesik çizgili **yer tutucu** kutularıyla görünür
(`class="yer-tutucu"`, metin `[İÇERİK: …]`). Doldurulan alandan bu sınıf kaldırılır.
