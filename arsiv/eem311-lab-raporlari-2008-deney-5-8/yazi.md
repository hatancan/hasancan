---
baslik: EEM311 Elektronik II: 2008 Laboratuvar Ön Çalışma ve Raporları, Deney 5–8 (Akım Aynası, Aktif Yük, Fark Yükselteci, Frekans Cevabı)
ozet: EEM311 Elektronik II laboratuvarının 2008 güz dönemi öğrenci ön çalışma ve raporları, Deney 5–8: CD4007 akım aynası Io–Vcc2 ölçümleri ve çıkış direnci, aktif yüklü CMOS yükselteç, 2N3904 fark yükselteci (Avdm, Avcm, CMRR) ve ortak emetörlü yükseltecin frekans cevabı.
---

Bu yazı, Başkent Üniversitesi Elektrik-Elektronik Mühendisliği **EEM311 Elektronik II** laboratuvarının **2008 güz dönemi** son dört deneyine ait öğrenci çalışmalarını içeriyor: PSpice ön çalışmaları, el ile yapılan ön çalışma hesapları ve deney raporları (Kasım–Aralık 2008). Deney 7 ve 8 için iki ayrı öğrencinin çalışması var. Hepsi **arkadaşların çalışmaları; kişisel bilgiler çıkarıldı.** Deney 6, 7 ve 8'in el yazısı ön çalışma sayfaları fotoğraflanmış sayfalardan metne aktarıldı. Deney föyleri arşivde ayrı yazılarda (Deney 5–6 ve Deney 7–8) yer alıyor. Kişisel bilgilerden arındırılmış PDF kopyalar yazının sonunda ZIP olarak indirilebilir.

## Deney 5: MOSFET akım aynası

### Ön çalışma (PSpice)

CD4007 ile kurulan aynada (V_CC1 = V_CC2 = 5 V, R = 1 kΩ) bias simülasyonu ve el hesabı karşılaştırması:

| | PSpice | Ön çalışma (el ile) |
|---|---|---|
| V_D1 | 3.566 V | 3.72 V |
| V_D2 | 5.000 V | 5.000 V |
| V_G1 = V_G2 | 3.566 V | 3.72 V |
| I_D1 = I_REF | 1.434 mA | 1.28 mA |
| I_D2 = I_O | 1.444 mA | 1.29 mA |

V_CC2'nin 0–8 V taraması (DC sweep) yapılmış; I_O birkaç volttan sonra I_REF'e yakın bir değerde sabitleniyor.

### Rapor

Ölçülen değerler: V_D1 = 3.278 V, V_G1 = 3.277 V, I_D1 = I_REF = 1.79 mA; V_D2 = 5.069 V, V_G2 = 3.277 V, I_D2 = I_O = 1.88 mA. V_G1 = V_G2 ve I_REF ≈ I_O olduğu görülüyor.

V_CC2 0'dan 8 V'a değiştirilerek ölçülen çıkış akımı:

| V_CC2 (V) | I_O (mA) | V_CC2 (V) | I_O (mA) |
|---|---|---|---|
| 0.00 | 0.025 | 2.75 | 1.841 |
| 0.25 | 0.745 | 3.00 | 1.845 |
| 0.50 | 1.180 | 3.25 | 1.850 |
| 0.75 | 1.498 | 3.50 | 1.855 |
| 1.00 | 1.665 | 3.75 | 1.860 |
| 1.25 | 1.761 | 4.00 | 1.864 |
| 1.50 | 1.789 | 4.50 | 1.872 |
| 1.75 | 1.811 | 5.00 | 1.880 |
| 2.00 | 1.820 | 6.00 | 1.892 |
| 2.25 | 1.827 | 7.00 | 1.905 |
| 2.50 | 1.833 | 8.00 | 1.915 |

Raporun yorumu: I_O, 1.5–1.75 V'tan sonra sabitlenmeye başlıyor, çünkü M2 bu gerilimden sonra doyuma (saturation) giriyor; daha küçük gerilimlerde transistör triyot bölgesinde olduğu için akım düşüyor.

Çıkış direnci V_CC2 = 4 V ve 6 V ölçümlerinden: R_o = ΔV/ΔI = (6 − 4) V / (1.892 − 1.864) mA; ön çalışmada bu değer **81 kΩ** bulunmuş.

*Not: Raporda sonuç yazılmamış; verilen değerlerle R_o = 2 V / 0.028 mA ≈ 71.4 kΩ çıkıyor.*

## Deney 6: Aktif yüklü CMOS ortak kaynaklı yükselteç

### Ön çalışma

El yazısı sayfalarda (fotoğraflardan aktarıldı) küçük işaret AC eşdeğeri çizilmiş (Q3–Q2 PMOS aynası r_o3, r_o2 dirençleri ve g_m·v_gs kaynaklarıyla, Q1'in g_m1·v_gs1 kaynağı, r_o1, R_g ve R_L) ve kazanç şöyle hesaplanmış:

- v_out = −g_m1·v_gs1·(r_o1 ∥ R_L), v_in = v_gs1
- g_m1 = 2I_D / (V_GS1 − V_TN) = 2·0.64 mA / (3.03 − 1.45) V ≈ 0.81 mA/V
- A_v = −g_m·R_L = −0.81 mA/V × 100 kΩ ≈ **−81**

*Not: Son adımda r_o'lar ihmal edilmiş. λ = 0.01 V⁻¹ ile r_o1 ≈ r_o2 ≈ 100 V / 0.6 mA ≈ 167 kΩ; çıkışta r_o1 ∥ r_o2 ∥ R_L ≈ 45 kΩ alınırsa A_v ≈ −37 bulunur, bu da PSpice sonucuna (−40) çok daha yakın.*

PSpice ön çalışması (V_CC = 15 V, R_REF = 25.42 kΩ, R_g = 1 MΩ, R_L = 100 kΩ, giriş 25 mV tepe, 5 kHz):

- Bias: kaynak akımı 1.058 mA, R_REF akımı 500.5 µA, NMOS akımı 557.4 µA, V_G = V_D = 2.754 V.
- Geçici simülasyon: v_in = 25 mV (tepe), v_out = 1.018 V (tepe), **A_v = −40**.
- R_REF yerine diyot bağlı NMOS Q4 konunca: akım 12.61 mA'e çıkıyor, V_G = V_D = 7.756 V; v_out = 468 mV (tepe), **A_v ≈ 18.7** (büyüklük olarak).

### Rapor

1. R_REF potansiyometreyle I_REF = 0.6 mA'e ayarlanmış: **R_REF = 25.33 kΩ**, I_O = I_D = 0.86 mA, V_A = 13.20 V, V_G = 2.78 V, V_D = 2.79 V.
1. Osiloskop ölçümünden A_v = −2.04 V / 75.2 mV ≈ **−27.2**.
1. R_in (R_x = 50 kΩ pot) satırı ve son tartışma sorusu boş bırakılmış.

## Deney 7: BJT fark yükselteci

### Ön çalışma, birinci öğrenci

El yazısı hesaplar (fotoğraflardan aktarıldı), föydeki Şekil 5 için (V_CC = 15 V, V_EE = −15 V, R_A = R_B = 2.2 kΩ, R_E = 250 Ω, β = 100, V_BE = 0.7 V):

- I_CQA = I_CQB = 2 mA, I_CQ1 = I_CQ2 = 1 mA, V_CE1 = V_CE2 = 6 V hedefi.
- I_CQA·R_REF + V_CEA + I_CQA·R_A = 15 V → 2 mA·R_REF + 0.7 + 4.4 − 15 = 0 → **R_REF = 4.95 kΩ**
- Girişler topraklıyken V_E1 = V_E2 = −0.7 V; V_CE = 6 V için V_C = 5.3 V; 5.3 = 15 − 1 mA·R_C → **R_C = 9.7 kΩ**
- g_m = I_CQ1 / V_T = 1 mA / 25 mV = 0.04 S
- A_vdm-diff = −g_m·R_C / (1 + g_m·R_E) = −0.04·9.7 k / (1 + 0.04·250) = **−35.27**
- A_vdm-se1 = −g_m·R_C / [2(1 + g_m·R_E)] = **−17.64**, A_vdm-se2 = **+17.64**
- V_E = I_CQ1·R_E + I_CQB·R_EE − 15 = −0.7 V'tan **R_EE = 7.025 kΩ**
- A_vcm-se1 = −g_m·R_C / (1 + g_m·R_E + 2g_m·R_EE) = **−0.68**
- CMRR = R_EE / (1/g_m + R_E) = 7.025 k / (25 + 250) = **25.6**
- rπ = β·V_T / I_CQ = 2.5 kΩ; R_idm = 2rπ(1 + g_m·R_E) = 2·2.5 k·11 = **55 kΩ**
- R_icm = v_icm / (2i_b) = rπ(1 + g_m·R_E + g_m·R_EE)/2 = **365 kΩ**

*Not: R_icm hesabında, föyün ilk ifadesindeki gibi paydada g_m·R_EE kullanılmış. İki yarımın akımı R_EE üzerinden birlikte aktığından doğrusu 2g_m·R_EE'dir; o zaman R_icm = 2.5 k·(1 + 10 + 562)/2 ≈ 716 kΩ olur.*

PSpice ile (R_C = 9.7 kΩ, R_REF = 4.95 kΩ):

- Bias: V_CE1 = V_CE2 = 6.11 V, I_CQ1 = I_CQ2 = 991.3 µA ≈ 1 mA, I_CQA = 1.994 mA, I_CQB = 1.995 mA. Rapor, değerlerin ön çalışmadaki hesaplara çok yakın çıktığını ve tasarımın doğru olduğunu söylüyor.
- v_in1 = 50 mV, v_in2 = −50 mV (tepe), 1 kHz: v_out1 ve v_out2 = 3.407 Vp-p (karşıt fazlı), v_odm = 6.813 Vp-p, v_idm = 198.092 mVp-p → **A_vdm-diff = −34.394, A_vdm-se1 = −17.2, A_vdm-se2 = 17.2**.
- Her iki girişe 4 V tepe, 1 kHz (ortak mod): v_out1 = v_out2 = 8.1 mVp-p, v_icm = 7.9238 Vp-p.

*Not: Belgede v_in1 "Vp-p = 99.046 V" diye yazılmış; birimi mV olmalı. Ortak mod kazancı da "7.5153 × 10⁻⁶" diye verilmiş; 8.1 mV / 7.9238 V ≈ 1.0 × 10⁻³ çıkıyor.*

### Ön çalışma, ikinci öğrenci (PSpice)

Standart dirençlerle (R_C = 10 kΩ, R_REF = 5.1 kΩ) ve besleme hatlarına 100 µF kapasitörlerle kurulan devre:

- Bias: V_CE1,2 = 5.359 V − (−0.663 V) = **6.022 V**, I_CQ1,2 = 964.1 µA, I_CQA,B = 1.939 mA.
- ±50 mV tepe girişte: v_out1 = −3.54 Vp-p, v_out2 = 3.54 Vp-p, v_odm = 7.08 Vp-p, v_idm = 200 mVp-p → A_vdm-diff = −35.4, A_vdm-se1 = −17.7, A_vdm-se2 = 17.7.
- 4 V tepe ortak mod girişte: v_out1 = v_out2 = 8.4 mVp-p, v_icm = 7.96 Vp-p → A_vcm-se ≈ −0.001.

El hesaplarıyla karşılaştırma tablosu (el ile R_C = 9.7 kΩ, R_REF = 4.88 kΩ):

| | El hesabı | PSpice |
|---|---|---|
| A_vdm-diff | −36.36 | −35.4 |
| A_vdm-se1 | −18.18 | −17.7 |
| A_vdm-se2 | 18.18 | 17.7 |
| R_EE | 7.025 kΩ | |
| CMRR | 25.5 | |
| A_vcm-se1 | −0.69 | −0.001 |
| R_idm | 55 kΩ | |
| R_icm | 365 kΩ | |

### Rapor, birinci öğrenci

Devre V_CC = 15 V, V_EE = −15 V, R_A = R_B = 2.2 kΩ, C = 100 µF, R_POT = 500 Ω ile kurulmuş; R_C için standart **10 kΩ** kullanılmış.

1. Girişler topraklıyken (kapasitörler takılmadan): I_CQA = 1.979 mA, I_CQB = 2.005 mA, V_CE1 = 6.042 V, V_CE2 = 6.480 V, I_CQ1 = 1.005 mA, I_CQ2 = 0.938 mA, V_C1 = 4.310 V, V_C2 = 5.780 V.
1. v_in1 = 100 mVp-p, 1 kHz, v_in2 topraklı: v_out1 = 1.45 V, v_out2 = 1.52 V → A_vdm-se1 = 14.5, A_vdm-se2 = 15.2.
1. v_in2 = 100 mVp-p, v_in1 topraklı: v_out1 = 1.63 V, v_out2 = 1.50 V → A_vdm-se1 = −16.3, A_vdm-se2 = −15.0.
1. Osiloskobun matematik menüsüyle CH1 − CH2: v_out1 − v_out2 = 2.94 V → **A_vdm-diff = 29.4**.

*Not: Belgede I_CQA'nın birimi "V" yazılmış (mA olmalı). 3. adımın hesabında pay 1.45 yazılmış; −16.3 sonucu v_out1 = 1.63 V ile bulunuyor.*

### Rapor, ikinci öğrenci

1. DC (girişler topraklı): I_CQA = 1.963 mA, I_CQB = 1.971 mA, V_CE1 = 6.045 V, V_CE2 = 6.042 V, I_CQ1 = 0.965 mA, I_CQ2 = 0.967 mA, V_C1 = 5.412 V, V_C2 = 5.411 V.
1. v_in2 topraklı, Q1'e 100 mVp-p, 1 kHz: v_out1 = −1.83 Vp-p, v_out2 = 1.81 Vp-p → A_vdm-se1 = −18.35, A_vdm-se2 = 18.15.
1. v_in1 topraklı, Q2'ye aynı sinyal: v_out1 = 1.83 Vp-p, v_out2 = −1.81 Vp-p → A_vdm-se1 = 18.35, A_vdm-se2 = −18.15.
1. CH1 − CH2 ile v_odm = −3.64 V → **A_vdm-diff = −36.4**.
1. İki girişe 8 Vp-p, 1 kHz: v_out1 = −4.21 mV, v_out2 = −4.18 mV → A_vcm-se1 = −0.000526, A_vcm-se2 = −0.000522.
1. Öğrenci, deneyde CMRR'yi hesaplarken A_vdm-se yerine A_vdm-diff kullandığını rapor hazırlarken fark ettiğini yazıp düzeltmiş: **CMRR = A_vdm-se / A_vcm-se = 18.35 / 0.000526 ≈ 34 886**.
1. Ölçülen akım ve gerilimlerin hesaplananlardan biraz farklı olmasının nedenleri: simülasyondaki ve deneydeki transistörlerin β değerlerinin farklı olması ve R_E'nin potansiyometreyle her iki tarafta tam 250 Ω olarak ayarlanamaması.

| | Ön çalışma (PSpice) | Deney |
|---|---|---|
| A_vdm-se1 / A_vdm-se2 | −17.7 / 17.7 | −18.35 / 18.15 |
| A_vdm-diff | −35.4 | −36.4 |
| A_vcm-se | −0.001 | −0.000526 |

## Deney 8: Ortak emetörlü yükseltecin frekans cevabı

### Ön çalışma, birinci öğrenci (el ile, fotoğraflardan aktarıldı)

Föydeki devre için (V_CC = 12 V, R1 = 8.2 kΩ, R2 = 3.9 kΩ, R_C = 6.3 kΩ, R_E = 3.3 kΩ, R_s = 3 kΩ, R_L = 3.9 kΩ, 2N3904, β = 100):

- V_B = 3.9 k / 12.1 k · 12 = 3.9 V; 3.9 = 0.7 + I_E·3.3 k → I_E = 0.967 mA, I_C = β/(β+1)·I_E = **0.957 mA**, I_B = **9.57 µA**
- 12 = I_C·R_C + V_CE + I_E·R_E → **V_CE = 2.67 V**; Q noktası (0.957 mA, 2.67 V)
- R_B = R1 ∥ R2 = 2.64 kΩ, rπ = β·V_T / I_C = 2.61 kΩ, **R_in = R_B ∥ rπ = 1.31 kΩ**
- r_o = (V_CE + V_A)/I_C = 107.3 kΩ, **R_out = R_C ∥ r_o = 5.95 kΩ**
- A_v-mid = R_in/(R_in + R_s) · (−g_m·(R_C ∥ R_L)) = **−27.3**
- Kısa devre zaman sabitleri: C1 için R_1s = R_s + (R_B ∥ rπ) = 4.2 kΩ → 23.8 rad/s; C2 için R_2s = R_L + (R_C ∥ r_o) = 7.87 kΩ → 127.1 rad/s; C_E için R_3s = R_E ∥ [(rπ + R_th)/(β+1)] = 39.5 Ω → 253.2 rad/s. ω_L = 404.1 rad/s → **f_L = 64.4 Hz**
- Açık devre zaman sabiti: R_eq = [(R_s ∥ R_B) + r_x] ∥ rπ = 0.96 kΩ, C = C_π + C_µ(1 − A_v) = 238.7 pF → ω_H = 4.37 × 10⁶ rad/s, **f_H = 695.9 kHz**
- Bant genişliği **BW = f_H − f_L ≈ 695.8 kHz**

### Ön çalışma, PSpice sonuçları

Birinci öğrencinin simülasyonu (C_E = 10 µF ile, föyün 2005'ten kalan tablo değeri):

- Bias: V_CE = 2.779 V, I_BQ = 7.078 µA, I_CQ = 958.1 µA.
- 1 kHz geçici analiz: v_in = 19.81 mVp-p, v_out = 544.13 mVp-p, A_v = 27.839.
- AC taraması: orta bant ≈ 27.28 dB; 3 dB noktaları **f_L ≈ 41.5 Hz, f_H ≈ 851.1 kHz**.
- C_E sökülünce: v_out = 6.65 mVp-p, A_v = 0.337; işaretçiler 16.1 Hz ve 601.174 M(Hz) gösteriyor.

Raporun yorumu: C_E kaldırılınca kazançta büyük bir düşüş oluyor; alt ve üst kesim frekansları da değişiyor.

*Not: 544.13 / 19.81 ≈ 27.47; belgedeki 27.839 biraz farklı.*

İkinci öğrenci (C_E = 100 µF) aynı bias değerlerini bulmuş; 10 mV tepe girişte v_out = 289.2 mV tepe, **A_v = −28.9**. Karşılaştırma tablosu:

| | El hesabı | PSpice (C_E var) | PSpice (C_E yok) |
|---|---|---|---|
| I_BQ | 9.29 µA | 7.078 µA | |
| I_CQ | 0.929 mA | 958.1 µA | |
| V_CEQ | 3.06 V | 2.78 V | |
| A_mid | −27.26 | −28.9 | −0.32 |
| f_L | 60.2 Hz | 41.5 Hz | 16.1 Hz |
| f_H | 694 kHz | 851.2 kHz | 601.17 kHz |

### Rapor

Devre föydeki Şekil 2'ye göre kurulmuş (raporda C_E = 10 µF yazıyor). Transistör verileri: V_BE(ON) = 0.7 V, V_A = 100 V, r_x = 100 Ω, C_π = 13.9 pF, C_µ = 8 pF, n = 1, V_T = 25 mV.

1. DC ölçümler: I_BQ = 0.071 mA, I_CQ = 0.954 mA, V_CEQ = 3.07 V.
1. v_s = 20 mVp-p, 1 kHz: v_in = 18.8 mV, v_out = 432 mV (10 mV/div ve 200 mV/div, 500 µs/div) → **A_v-mid = 23.0**. Sonraki ölçümlerde gözlem kolaylığı için v_in = 32.8 mV alınmış.
1. Kesim frekansları **f_H = 425 kHz**, f_L = 3.87 Hz olarak yazılmış. Frekans taraması (A_v = v_out / 32.8 mV):

| Frekans | v_out (tepe) | A_v |
|---|---|---|
| 30 Hz | 56.0 mV | 1.707 |
| 40 Hz | 72.0 mV | 2.195 |
| 50 Hz | 96.0 mV | 2.927 |
| 80 Hz | 152 mV | 4.634 |
| 150 Hz | 272 mV | 8.293 |
| 200 Hz | 344 mV | 10.488 |
| 250 Hz | 400 mV | 12.195 |
| 300 Hz | 456 mV | 13.902 |
| 20 kHz | 864 mV | 26.341 |
| 60 kHz | 856 mV | 26.097 |
| 120 kHz | 824 mV | 26.122 |
| 200 kHz | 752 mV | 22.927 |
| 500 kHz | 480 mV | 14.634 |
| 750 kHz | 352 mV | 10.732 |
| 1 MHz | 272 mV | 8.293 |
| 1.3 MHz | 208 mV | 6.342 |
| 1.5 MHz | 184 mV | 5.609 |

Grafik, x ekseni eşit aralıklı "logaritmik" sıra numaralarıyla Excel'de çizilmiş.

- **4. adım:** C_E sökülünce orta bant kazancı büyük ölçüde düşüyor: **A_v-mid = 0.333**, f_H = 722 kHz, f_L = 132 Hz.
- **5. adım:** 5 kΩ'luk potla **R_in = 3.688 kΩ**.
- **6. adım:** 10 kΩ'luk potla **R_out = 6.12 kΩ**.

*Not: 0.954 mA, raporda yazıldığı gibi 95.4 µA değil 954 µA'dir. 120 kHz satırında 824 / 32.8 ≈ 25.12 olmalı. Tablodaki kazanç 300 Hz'de bile orta bant değerinin (≈ 26.3) yarısı kadar olduğundan alt kesim frekansı birkaç yüz hertz civarında; "3.87 Hz" büyük olasılıkla 387 Hz olacaktı.*

## Yayınlanmayan dosyalar

Klasördeki PSpice proje ve simülasyon dosyaları (.opj, .DSN, .DBK, .sim, .out, .dat vb.) yazıya alınmadı; el yazısı ön çalışma fotoğrafları yalnızca metne aktarıldı, indirme dosyasında yok.
