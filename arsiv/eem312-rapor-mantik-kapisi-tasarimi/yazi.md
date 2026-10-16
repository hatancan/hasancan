---
baslik: EEM312 Sayısal Elektronik: Mantık Kapısı Tasarımı Raporları, Pass Transistör XOR ile CMOS NAND/NOR (2005–2017)
ozet: EEM312 Sayısal Elektronik yazılım laboratuvarının mantık kapısı tasarımı deneyi için 2005–2017 arası öğrenci raporları: altı transistörlü pass transistör XOR kapısında girişe göre değişen source/drain bağlantıları, en az transistörlü iki ve üç girişli CMOS NAND/NOR, doğruluk tabloları ve gecikme karşılaştırması.
---

Bu yazı, Başkent Üniversitesi **EEM312 Sayısal Elektronik** yazılım laboratuvarının **mantık kapısı tasarımı** deneyi için yazılmış raporları bir araya getiriyor. Deney 2005–2006'da **Y8**, 2011 föylerinde **Y6**, 2014'te "Deney 10" adıyla yapılmış. Raporlar: 2005'ten iki (A, B), 2006'dan iki (C, D), 2011'den iki ön çalışma ve rapor (E, F), 2014'ten bir ön çalışma ve rapor (G); bunlar arkadaşların çalışmaları, **kişisel bilgileri çıkarıldı**. Ayrıca **Hasan Can Öztürk**'ün 2017'de hazırladığı XOR benzetimleri de ZIP'te (öğrenci numarası kapatıldı). Föyler [EEM312 yazılım laboratuvarı föyleri Y4–Y8](/arsiv/eem312-yazilim-deneyleri-y4-y8/) yazısında (Y6 ve Y8 bölümleri). Raporların PDF'leri, temizlenmiş SPICE ağ listeleri ve 2017 ekran görüntüleri yazının sonundaki ZIP'te.

## 1. Pass transistör XOR kapısı

Föydeki XOR kapısı altı transistörlü: bir CMOS tersleyici A'nın tümleyenini (−A) üretiyor, B girişine bağlı bir tersleyici benzeri yapı ve B ile sürülen bir iletim kapısı da A ya da −A'yı çıkışa aktarıyor. Raporların ortak gözlemi: **B girişinin değerine göre iletim kapısındaki transistörlerin (raporlara göre P2/N2 ya da M3/M6) source ve drain uçları yer değiştiriyor**; Spice'ta gövde (bulk) source'a bağlı yazıldığı için her giriş birleşimi (A, B = 00, 01, 10, 11) için ayrı bir ağ listesi hazırlanmış. Örnek (E raporunda A = 0, B = 0 için; düğüm 2 = A, 3 = −A, 4 = B, 5 = çıkış, model satırları çıkarıldı):

```
*  D G S B
M1 3 2 0 0 MOSN W=1.8u L=1.2u
M2 3 4 5 5 MOSN W=1.8u L=1.2u
M3 5 3 4 4 MOSN W=1.8u L=1.2u
M4 3 2 1 1 MOSP W=3.6u L=1.2u
M5 2 4 5 5 MOSP W=3.6u L=1.2u
M6 4 2 5 5 MOSP W=3.6u L=1.2u
vdd 1 0 5V
v2 2 0 0v
v4 4 0 0v
.control
tran 0.05n 500n
plot v(2) v(4) v(5)
.endc
.end
```

G raporunun ön çalışması A = B = 0 durumunu adım adım açıklıyor: A düşük olduğu için tersleyicinin PMOS'u iletime geçip −A = 1 üretiyor; B düşük olduğundan B'ye bağlı PMOS iletimde, NMOS kesimde ve source'undaki A değeri (0) çıkışa aktarılıyor. 2014 raporu ise tek bir ağ listesinde iki darbe kaynağıyla (A: 100 ns, B: 200 ns yarı periyot) dört durumu art arda göstermiş.

| A | B | A ⊕ B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

Tüm benzetimler doğruluk tablosunu sağlıyor. E raporu, çıkış 0 olması gereken durumlarda grafikte görülen küçük değerlerin nanovolt mertebesinde olduğunu, üst üste binen dalgaları ayırmak için sinyallere 0.1 V eklendiğini not ediyor. A raporu XOR çıkışında yükselme gecikmesini 0.27 ns, düşme gecikmesini 0.268 ns bulmuş.

## 2–3. En az transistörlü NAND ve NOR

İstenen, en az sayıda transistörle CMOS NAND ve NOR kapısı: N girişli kapıda N NMOS ve N PMOS (2 girişte 4, 3 girişte 6 transistör). NAND'da NMOS'lar seri, PMOS'lar paralel; NOR'da tersi.

- **2005 (A, B):** üç girişli NAND ve NOR (çıkışta 1 fF yük). NAND yalnız üç giriş de 1 iken 0, NOR yalnız üç giriş de 0 iken 1 veriyor.
- **2006 ve sonrası (C–G):** iki girişli NAND ve NOR; doğruluk tablolarıyla benzetim sonuçları uyuşuyor. F'nin ön çalışması iki girişli NAND'ın iki pass transistör ve bir tersleyiciyle de kurulabileceğini, NOR için de alternatif bir yapı olduğunu gösteriyor.

## 4–5. Gecikme karşılaştırması

| Rapor | Kapı | Düşükten yükseğe | Yüksekten düşüğe |
|---|---|---|---|
| A (2005) | XOR (2 giriş) | 0.27 ns | 0.268 ns |
| A (2005) | NAND (3 giriş) | 1.03 ns | 2.35 ns |
| A (2005) | NOR (3 giriş) | 1.95 ns | 3.15 ns |
| D (2006) | NAND (2 giriş), en kötü durum | 1.135 ns | |
| D (2006) | NOR (2 giriş), en kötü durum | 1.623 ns | |

A raporu, XOR'un iki, diğerlerinin üç girişli olduğunu hatırlatıp asıl karşılaştırmanın NAND ile NOR arasında yapılması gerektiğini söylüyor; iki raporda da (A, D) NOR, NAND'dan yavaş. C, E ve F raporları ise "en kötü gecikmesi en küçük kapının NOR olduğu" sonucuna varmış. F raporu ayrıca diferansiyel yapıya yakın tasarımlarda çıkıştaki değişimin daha erken görüldüğünü yazıyor.

*Not: NOR kapısında PMOS'lar seri bağlıdır ve PMOS'un taşıyıcı hareketliliği (modelde KP = 2.7E−5) NMOS'unkinden (8.0E−5) yaklaşık üç kat küçüktür; bu yüzden aynı boyutlarla NOR'un yükselme gecikmesi NAND'dan büyük çıkar. A ve D raporlarının sayısal sonuçları bununla uyumlu. A raporundaki "NOR'da transistörler paralel bağlandığından gecikme fazla" açıklaması ise eksik: gecikmeyi artıran, çıkışı yukarı çeken seri PMOS zinciridir. C, E ve F'deki "NOR en hızlı" sonucu da bu beklentiyle çelişiyor; raporlarda en kötü durum gecikmeleri sayısal olarak verilmemiş.*

*Not: A raporunun NOR doğruluk tablosunun sütun başlığında yanlışlıkla "NAND" yazıyor; tablo değerleri NOR'a ait ve doğru. F'nin ön çalışmasının başlığında da ders kodu "EEM332" diye yazılmış.*

## Klasördeki diğer dosyalar

Aynı deneye ait başka öğrencilerin ağ listesi klasörleri (her giriş birleşimi için ayrı dosyalar, üç girişli kapı denemeleri) ve iki rapor kopyası daha vardı: biri A raporunun başlıksız aynısı, diğeri C raporuyla neredeyse aynı metne sahip. Bunlar ayrıca alınmadı. ZIP'te E raporunun ağ listeleri (`2011_…`) ile 2017 çalışmasına ait XOR ağ listeleri ve WinSPICE ekran görüntüleri var.
