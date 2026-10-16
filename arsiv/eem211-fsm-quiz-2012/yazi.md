---
baslik: EEM211 Sayısal Mantık Tasarımı: D Flip-Floplu Sonlu Durum Makinesi Quizi ve Cevap Anahtarı (Aralık 2012)
ozet: İki D flip-floplu sonlu durum makinesinin (FSM) analizi: DA = X'·QB, DB = X ve Z = QA·X denklemleri, durum tablosu ve dört durumlu Mealy durum diyagramı. Başkent Üniversitesi BME 231 Quiz V (21.12.2012) ve BİL 275 2010–2011 güz Quiz-4 cevap anahtarı.
---

Bu yazı, EEM211 Sayısal Mantık Tasarımı dersinin final hazırlığı için 28 Aralık 2012'de telefonla paylaşılmış iki fotoğraftan metne aktarıldı. Fotoğraflarda aynı soru var: Başkent Üniversitesi Biyomedikal Mühendisliği Bölümü **BME 231 Sayısal Mantık Tasarımı Quiz V** kâğıdı (21.12.2012; öğrenci bilgileri alanı fotoğrafta zaten kapatılmış) ve Bilgisayar Mühendisliği **BİL 275 Sayısal Mantık Tasarımı 2010–2011 Güz Quiz-4** sorusunun "cevap anahtarı" yazılı çözümlü kâğıdı. Fotoğraflanmış sayfalardan metne aktarıldı; fotoğrafların kendisi yayınlanmadı.

## Soru

Devrede iki D flip-flop (A ve B), ortak bir saat (Clock) ve bir X girişi var. X bir tümleyiciden geçip, B flip-flopunun çıkışı QB ile birlikte bir AND kapısına giriyor; bu AND'in çıkışı A flip-flopunun D girişini (DA) sürüyor. X doğrudan B flip-flopunun D girişine (DB) bağlı. Z çıkışı, QA ile X'in AND'idir.

> Yukarıda verilen sonlu durum makinesi (FSM) devresini kullanarak aşağıdaki soruları cevaplayınız.
> a. İki flip-flop devresinin ve Z'nin denklemini yazınız. (30 puan)
> b. Durum tablosunu oluşturunuz. (40 puan)
> c. Durum diyagramını çiziniz. (30 puan)

Kâğıtta D flip-flopun tablosu da verilmiş: D = 0 için Q(t+1) = 0, D = 1 için Q(t+1) = 1.

## Cevap anahtarı

**a) Denklemler:**

- DA = X'·QB
- DB = X
- Z = QA·X

**b) Durum tablosu:**

| QA | QB | Sonraki QA QB (X = 0) | Sonraki QA QB (X = 1) | Z (X = 0) | Z (X = 1) |
|---|---|---|---|---|---|
| 0 | 0 | 00 | 01 | 0 | 0 |
| 0 | 1 | 10 | 01 | 0 | 0 |
| 1 | 0 | 00 | 01 | 0 | 1 |
| 1 | 1 | 10 | 01 | 0 | 1 |

*Not: Tablo denklemlerden kontrol edildi; örneğin QA QB = 01 ve X = 0 için DA = 1·1 = 1, DB = 0, sonraki durum 10; QA = 1 ve X = 1 için Z = 1.*

**c) Durum diyagramı** (X/Z etiketli, çıkış girişe bağlı olduğundan Mealy makinesi):

- 00: X = 0 → 00 (0/0), X = 1 → 01 (1/0)
- 01: X = 0 → 10 (0/0), X = 1 → 01 (1/0)
- 10: X = 0 → 00 (0/0), X = 1 → 01 (1/1)
- 11: X = 0 → 10 (0/0), X = 1 → 01 (1/1)

X = 1 geldiğinde makine her durumdan 01'e gider; X = 0 geldiğinde QB'nin değeri QA'ya kayar. Böylece QB bir önceki girişi, QA ise "iki adım önceki giriş 1, bir önceki giriş 0" bilgisini tutar. Z = 1 olması için son üç girişin **1, 0, 1** olması gerekir; yani devre **101 dizisini** (iç içe geçmeye izin vererek) algılar.

*Not: Son paragraftaki dizi yorumu cevap anahtarında yok; durum tablosundan çıkarıldı.*
