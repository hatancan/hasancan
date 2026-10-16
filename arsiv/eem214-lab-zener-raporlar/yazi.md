---
baslik: EEM214 Elektronik I: Zener Diyot Karakteristikleri ve Zener Regülatörü, Öğrenci Raporları (2006–2012)
ozet: EEM214 Elektronik I laboratuvarının Zener diyot deneyine ait öğrenci ön çalışma ve raporları: BZX55C (6.2 V) ileri ve ters yön ölçüm tabloları, Zener direnci, 15 V ve 8 V beslemeli Zener regülatöründe farklı seri ve yük dirençleriyle çıkış gerilimleri ve Zener akımları.
---

Bu yazı, Başkent Üniversitesi **EEM 214 Electronics I** laboratuvarının **Zener Diode Characteristics** deneyi için farklı yıllarda hazırlanmış öğrenci ön çalışma ve raporlarını bir araya getiriyor. Hepsi arkadaşların çalışması; ad ve öğrenci numaraları kapatıldı. Deneyde DMM ile Zener testi, BZX55C Zener diyotun ileri ve ters yön karakteristiği ve bir Zener regülatörünün farklı seri direnç (R_s) ve yük (R_L) değerlerinde davranışı inceleniyor. Kişisel bilgileri kapatılmış PDF kopyaları yazının sonunda ZIP olarak indirilebilir.

## Ön çalışmalar

- **2009 ön çalışması:** Devre PSpice'ta kurulup V_in −10 V ile 6 V arasında DC sweep ile Zener'in i–v karakteristiği çizilmiş. Zener diyot şöyle anlatılıyor: ileri yönde normal diyot gibi iletir (silisyumda yaklaşık 0.6 V düşüm); ters yönde gerilim kırılma gerilimini (Zener gerilimini) aşınca akım geçirir ve üzerindeki gerilimi bu değerde tutar. Yoğun katkılı p-n ekleminde elektronlar p bölgesinin değerlik bandından n bölgesinin iletim bandına tünelleme yapar; kırılma gerilimi katkılama ile hassas biçimde ayarlanabilir (yaygın toleranslar %5 ve %10). Referans gerilimi üretmede ve düşük akımlı uygulamalarda gerilim sabitleyici olarak kullanılır.
- **2008 ön çalışması:** PSpice ile V(D1) – I(D1) eğrisi (−20 V ile 10 V); Zener diyot "ters bağlandığında üzerinde yazılı gerilimi aşan gerilimi geçiren ve üzerindeki gerilimi o değerde sabit tutan diyot" olarak tanımlanmış, normal diyot ve Zener i–v karakteristikleri karşılaştırılmış (normal diyot için kapalıyken eğim 0, iletimde sonsuz; Zener'de ayrıca ters yönde −V_Z'de iletim).
- **2012 ön çalışması:** 10 V kaynak, 1 kΩ ve D1N750 Zener ile PSpice simülasyonları.

## Zener diyot testi

DMM'nin diyot kademesinde ileri yönde 0.7615 V, 0.7756 V; ters yönde "1" (aralık dışı) okunmuş; diyotlar sağlam. Bir raporda ohmmetreyle ileri yönde 710.2 Ω, ters yönde ölçülemeyecek kadar büyük direnç bulunmuş.

## İleri ve ters yön karakteristiği (BZX55C)

**İleri yön:**

| v_D (V) | 2006 rapor A | 2006 rapor B |
|---|---|---|
| 0.35 | 0.25 µA | 0.25 µA |
| 0.45 | 2.18 µA | 1.9 µA |
| 0.55 | 20.94 µA | 19.9 µA |
| 0.60 | 52.21 µA | 63.6 µA |
| 0.65 | 143.2 µA | 248 µA |
| 0.70 | 1.016 mA | 0.969 mA |
| 0.75 | 5.654 mA | 5.291 mA |
| 0.80 | 31.01 mA | 31.44 mA |
| 0.85 | – | 69.72 mA |

İleri yönde Zener diyot normal bir silisyum diyot gibi davranıyor; yaklaşık 0.7 V'tan sonra iletime geçiyor.

**Ters yön:**

| V_uygulanan (V) | V_Z (A) | I_Z (A) | V_Z (B) | I_Z (B) | V_Z (2008) | I_Z (2008) |
|---|---|---|---|---|---|---|
| 2 | 2.064 V | ≈ 0 | 2.07 V | ≈ 0 | – | – |
| 4 | 4.079 V | 1.8 µA | 4.10 V | 0.85 µA | – | – |
| 6 | 5.83 V | 373 µA | 5.80 V | 0.75 mA | 5.998 V | 1.763 mA |
| 8 | 5.95 V | 6.46 mA | 5.94 V | 6.34 mA | 6.071 V | 5.655 mA |
| 10 | 5.99 V | 12.33 mA | 5.95 V | 12.62 mA | 6.109 V | 11.50 mA |
| 12 | 6.00 V | 18.34 mA | 5.96 V | 18.85 mA | 6.150 V | 17.31 mA |
| 14 | 6.00 V | 24.26 mA | 5.97 V | 24.92 mA | 6.200 V | 24.11 mA |

Zener gerilimi yaklaşık **6 V**; bu değerden sonra gerilim neredeyse sabit kalıyor ve akım hızla artıyor. 2008'deki başka bir raporda (Türkçe) Zener gerilimi 6.3 V civarı bulunmuş.

Raporlardan birinde Zener empedansı Z_Z = V_Z / I_Z olarak 8 V için 5.95 V / 6.46 mA = 921 Ω, 12 V için 6.00 V / 18.34 mA = 327 Ω hesaplanmış.

*Not: V_Z / I_Z bir "statik" orandır. Regülasyonda önemli olan dinamik direnç r_Z = ΔV_Z / ΔI_Z'dir; aynı ölçümlerle (6.00 − 5.95) V / (18.34 − 6.46) mA ≈ 4.2 Ω bulunur.*

## Zener regülatörü

Çıkış gerilimi V_out (2006 rapor A):

| R_s | V_s = 15 V, R_L = 1.8 kΩ | V_s = 15 V, R_L = 470 Ω | V_s = 8 V, R_L = 1.8 kΩ | V_s = 8 V, R_L = 470 Ω |
|---|---|---|---|---|
| 390 Ω | 5.98 V | 5.97 V | 5.92 V | 4.30 V |
| 220 Ω | 6.01 V | 6.01 V | 5.94 V | 5.42 V |
| 150 Ω | 6.05 V | 6.02 V | 5.96 V | 5.91 V |
| 100 Ω | 6.13 V | 6.07 V | 5.97 V | 5.98 V |

Akımlar I_L = V_out / R_L, I_s = (V_s − V_out) / R_s, I_Z = I_s − I_L ile hesaplanmış. Örneğin V_s = 15 V, R_L = 1.8 kΩ, R_s = 390 Ω için I_L = 3.32 mA, I_s = 23.1 mA, I_Z = 19.78 mA; V_s = 8 V, R_L = 470 Ω, R_s = 390 Ω için I_L = 9.14 mA, I_s = 9.49 mA ve I_Z yalnızca 0.35 mA, bu yüzden çıkış 4.30 V'a düşüyor (Zener regülasyon bölgesinden çıkmış). Rapor B'deki değerler çok benzer (örneğin 15 V / 1.8 kΩ / 390 Ω için 5.99 V, 8 V / 470 Ω / 390 Ω için 4.40 V).

*Not: Raporda V_s = 8 V, R_L = 1.8 kΩ, R_s = 100 Ω satırı için bir önceki satırın (150 Ω) hesabı tekrar yazılmış. Doğrusu I_s = (8 − 5.97) / 0.1 = 20.3 mA, I_L = 3.32 mA, I_Z ≈ 17.0 mA olmalıdır.*

2008 raporunda 12 V ve 8 V kaynak, R_L = 820 Ω ve 330 Ω, R_s = 620, 390, 100 Ω ile ölçümler yapılmış: örneğin 12 V'ta R_s = 620 Ω iken çıkış 3.84 V'ta kalırken, R_s = 100 Ω'da 6.41 V'a çıkıyor; 8 V'ta tüm durumlarda çıkış 3.5–4.3 V arasında kalıyor.

## İndirme

ZIP dosyası yıllara göre klasörlenmiş yedi ön çalışma ve raporun kişisel bilgileri kapatılmış PDF kopyalarını içeriyor.
