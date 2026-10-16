---
baslik: EEM311 Elektronik II: 2008 Laboratuvar Ön Çalışma ve Raporları, Deney 1–4 (BJT, MOSFET, İki Katlı Yükselteç)
ozet: EEM311 Elektronik II laboratuvarının 2008 güz dönemi öğrenci ön çalışma ve raporları, Deney 1–4: BC238B ortak emetörlü yükselteç ölçümleri (β, rπ, n, ro, VA), BJT yükselteç tasarımı, CD4007 MOSFET yükselteç PSpice sonuçları ve JFET–BJT iki katlı yükselteç.
---

Bu yazı, Başkent Üniversitesi Elektrik-Elektronik Mühendisliği **EEM311 Elektronik II** laboratuvarının **2008 güz dönemi** ilk dört deneyine ait öğrenci çalışmalarını içeriyor: PSpice ön çalışmaları, deney raporları ve Deney 2'nin el yazısı tasarım hesapları. Hepsi **bir arkadaşın çalışması; kişisel bilgiler çıkarıldı.** Raporlar Türkçe, bilgisayarda hazırlanmış; osiloskop ekranları çoğunlukla elle çizilecek boş ızgaralar olarak bırakılmış. Deney 2'nin ön çalışması fotoğraflanmış sayfalardan metne aktarıldı. Deney föylerinin kendisi arşivde ayrı yazılarda (Deney 1–2 ve Deney 3–4) yer alıyor. Kişisel bilgilerden arındırılmış PDF kopyalar yazının sonunda ZIP olarak indirilebilir.

## Deney 1: Tek katlı BJT yükselteci

### Ön çalışma (PSpice)

Föydeki devre (V_CC = 15 V, R_B1 = 470 kΩ, R_B2 = 1.8 kΩ, R_C = 1 kΩ, R_L = 100 kΩ, C = 10 µF, transistör BC238B) PSpice'ta kurulmuş. Bias noktası analizinin sonuçları:

- V_CQ = 15 V − 5.520 V = 9.480 V, V_EQ = 0 V
- I_BQ = 30.310 µA, I_CQ = 9.480 mA, I_EQ = 9.510 mA

*Not: Belgede I_CQ "9.480 µA" yazılmış; I_C·R_C = 5.52 V düşümünden ve I_E = 9.510 değerinden akımın 9.48 mA olduğu anlaşılıyor.*

1 kHz sinüs girişte, farklı tepeden tepeye genlikler için zaman domeni simülasyonundan bulunan gerilim kazancı:

| Giriş (p-p) | A_v |
|---|---|
| 2 mV | −96.249 |
| 20 mV | −95.834 |
| 140 mV | −64.501 |
| 500 mV | −18.774 |

Giriş büyüdükçe çıkış önce bozulmaya, sonra kırpılmaya başladığı için ölçülen kazanç düşüyor.

### Rapor

Ölçülen çalışma noktası **I_BQ = 30 µA, I_CQ = 7.966 mA, V_CEQ = 7.010 V**; DC yük doğrusu 15 mA ile 15 V arasında çizilmiş ve Q noktası üzerinde işaretlenmiş.

1. β = I_C / I_B = 7.966 mA / 30 µA = **265.53**
1. 1 kHz, 40 mV p-p girişte v_be = 18.2 mV (p-p) ölçülmüş: rπ = v_be / I_BQ = **606.66 Ω**, rπ = n·V_T / I_BQ'dan **n = 0.7279**.
1. 20 mV p-p girişte v_out = 3.7 V: g_m = I_CQ / (n·V_T) = 0.438 S; (r_o ∥ R_L ∥ R_C) = v_out / (g_m·v_be) bağıntısından **r_o = 25 kΩ**, r_o ≅ V_A / I_CQ'dan **V_A = 199.15 V**.
1. Osiloskop ayarları: v_in için 10 mV/div, v_out için 1 V/div, 500 µs/div.
1. Bozulmanın başladığı noktada **v_be = 7.3 mV** (p-p).
1. Kırpılmasız en büyük çıkış salınımı **v_out,undistorted = 12.5 V** (p-p).
1. 20 mV, 140 mV ve 500 mV p-p girişler için çıkış dalga şekilleri çizilmiş; 500 mV'ta çıkış kare dalgaya yakın biçimde kırpılıyor.

*Not: n'nin 1'den küçük çıkması (0.73) fiziksel olarak beklenmez (föyde 1 ≤ n ≤ 2 deniyor); v_be ölçümündeki hata ya da I_BQ'nun yuvarlanması bu sonucu doğurmuş olabilir.*

## Deney 2: Tek katlı BJT yükselteç tasarımı

Bu deneyin raporu klasörde yalnızca boş osiloskop ızgaraları olarak duruyor (raporun kendisi elle doldurulmuş olmalı). Ön çalışmanın el yazısı tasarım hesapları ise fotoğraflanmış dört sayfada:

- İstenen kazanç aralığı: A_v,min = 22 dB = 10^(22/20) = 12.58, A_v,max = 24 dB = 10^(24/20) = 15.85; tasarımda ortalama **A_v = (15.85 + 12.58)/2 = 14.35** hedeflenmiş.
- AC yük doğrusu üzerinde kırpılmasız salınım için x = v_out,undistorted,p-p / 2 = 6/2 = 3 V gerekiyor; güvenlik payıyla **4 V** seçilmiş.
- R_C = R_L = 3.3 kΩ alınarak 4 = I_CQ·(R_C ∥ R_L) = I_CQ·1.65 kΩ'dan **I_CQ = 2.42 mA**; β = 250 için I_BQ = 2.42 mA / 250 = **9.68 µA**.
- A_v = (R_C ∥ R_L) / (rπ/(β+1) + R_E1) bağıntısından 14.35 = 1650 Ω / (…) ile **R_E1 = 104.7 Ω**.
- V_CC = V_CEQ + I_C·R_C + I_C·(R_E1 + R_E2) eşitliğinden **R_E2 = 1140 Ω** (R_E = R_E1 + R_E2 ≈ 1244 Ω); taban direnci bölücüsü **R1 = 39 kΩ, R2 = 13 kΩ**.
- n = 1.4 için rπ = n·V_T / I_BQ = 1.4·0.025 V / 9.68 µA = **3.6 kΩ**.
- Aynı I_BQ ile β = 200 için I_CQ = 1.9 mA, V_CEQ = 6.01 V; β = 250 için I_CQ = 2.42 mA, V_CEQ = 3.56 V hesaplanmış. Son sayfada küçük işaret eşdeğer devresi (R1 ∥ R2, rπ, g_m·v_be = β·i_b, R_E1, R_C, R_L) çizilmiş.

*Not: Fotoğraflanan sayfalardan birinde R_E1 + R_E2 = 1420 Ω, diğerinde R_E = 1244 Ω yazıyor; ayrıca I_BQ sabit tutulunca I_CQ β ile orantılı değiştiği için (1.9 mA → 2.42 mA, yaklaşık %27) föydeki "β ile I_CQ en fazla %3 değişsin" koşulu bu hesapla sağlanmıyor; o koşul için taban bölücüsünün çok daha küçük dirençlerle kurulması gerekir.*

## Deney 3: Tek katlı MOSFET yükselteci (PSpice ön çalışması)

CD4007'nin NMOS transistörüyle kurulan ortak kaynaklı yükselteçte seçilen dirençler: **R1 = 68 kΩ, R2 = 20 kΩ, R_D = 178 kΩ, R_S = 20 kΩ**, C_g = 1 µF, C_S = 10 µF, giriş 50 mV, 1 kHz.

Bias simülasyonu: bölücü akımı 170.5 µA, I_D = **74.01 µA**, V_G = 3.409 V, V_D = 1.826 V, kaynaktan çekilen toplam akım 244.5 µA. Föydeki hedef I_D ≈ 75 µA'e oldukça yakın.

Geçici (transient) simülasyon sonuçları:

| | R_L varken | R_L yokken |
|---|---|---|
| Giriş (Vp-p) | 49.999 mV | 49.999 mV |
| Çıkış (Vp-p) | 188.85 mV | 1.8265 V |
| A_v | −3.777 | −36.53 |

*Not: R_D = 178 kΩ standart bir direnç değeri değil (föy standart değerler ≤ 100 kΩ istiyor). V_D = 1.826 V iken V_S = 74 µA·20 kΩ ≈ 1.48 V olduğundan V_DS ≈ 0.35 V kalıyor ve V_GS − V_t ≈ 1.93 − 1.45 = 0.48 V'tan küçük; yani MOSFET doymada değil, triyot bölgesinde. "R_L yokken" kolonundaki 1.8265 V da çıkış salınımı değil, drenin DC seviyesi olarak okunmuş görünüyor.*

Raporun kendisi klasörde yalnızca boş ızgaralar ve ölçüm şemaları (Şekil 6 ve 7, R_x = 1 kΩ) olarak bulunuyor.

## Deney 4: İki katlı JFET–BJT yükselteç

### Ön çalışma (PSpice)

Föydeki devre (J2N4860 ortak kaynak + Q2N3904 ortak emetör, V_CC = 12 V, R_g = 1 MΩ, R_d = 1 kΩ, R_s = 330 Ω, R1 = 30 kΩ, R2 = 47 kΩ, R_c = 1 kΩ, R_e = 2.2 kΩ, R_L = 100 kΩ) kurulmuş. Föyde iki kapasitöre de "C2" denildiği için C2 = 22 µF, C3 = 100 µF alınmış.

| Bias noktası | Değer |
|---|---|
| V_D | 5.865 V |
| V_G | ≈ 0 V (7.884 fV) |
| V_S | 2.024 V |
| V_B | 6.985 V |
| V_C | 9.158 V |
| V_E | 6.292 V |
| I_D | 6.135 mA |
| I_C | 2.842 mA |
| I_E | 2.860 mA |
| I_B | 18.55 µA |

0.1 mV, 1 kHz girişli geçici simülasyonda v_in = 100 µV (p-p), v_out = 963.7 nV, v_b (p-p) = 6.9851 V okunmuş; buradan birinci kat kazancı 20.744 k, ikinci kat 6.9362 µ, toplam 496.462 m çıkmış.

*Not: Bu kazançlar fiziksel değil: 6.9851 V, ikinci katın tabanındaki DC seviye (V_B); grafiklerde DC seviyesi kuplaj kapasitörünün yanlış tarafından ölçülmüş. Ön çalışmadaki DC değerler ise föydeki devreyle tutarlı.*

### Rapor

Ölçülen gerilimler: V_G ≈ 0 V (0.007 V), V_D = 4.763 V, V_S = 2.488 V, V_B = 6.981 V, V_C = 9.225 V, V_E = 6.175 V. Buradan:

- I_C = (V_CC − V_C)/R_c = (15 − 9.225)/1 kΩ = 5.8 mA
- I_D = (V_CC − V_D)/R_D = (15 − 4.763)/1 kΩ = 10.2 mA

*Not: Devrenin besleme gerilimi 12 V; hesaplarda 15 V kullanılmış. 12 V ile I_C = 2.78 mA ve I_D = 7.24 mA bulunur; I_C, ön çalışmadaki 2.84 mA ile uyumlu. Kaynak direnci üzerinden I_D = V_S/R_s = 2.488/330 ≈ 7.5 mA de aynı sonucu doğruluyor.*

Raporun ikinci bölümünde 70 mV, 1 kHz girişli simülasyon grafikleri (v_in, v_out, v_b) var; kazanç, kırpılmasız salınım, R_in (R_x = 500 kΩ) ve R_out (R_x = 1 kΩ) satırları boş bırakılmış.

## Yayınlanmayan dosyalar

Klasördeki PSpice proje ve simülasyon dosyaları (.opj, .DSN, .DBK, .sim, .out, .dat vb.) bu yazıya alınmadı; Deney 2 ve 3'ün boş rapor şablonları da ZIP'te yok.
