---
baslik: EEM311 Elektronik II: 2010 Laboratuvar Ön Çalışma ve Raporları, Deney 5–7 (Akım Aynası, Aktif Yük, Fark Yükselteci)
ozet: EEM311 Elektronik II laboratuvarının 2010 güz dönemi öğrenci ön çalışma ve raporları, Deney 5–7: CD4007 akım aynasında Io–Vcc2 ölçümü ve 80 kΩ çıkış direnci, aktif yüklü CMOS yükselteç kazancı ve 2N3904 fark yükselteci ölçümleri (CMRR ≈ 41 400).
---

Bu yazı, Başkent Üniversitesi Elektrik-Elektronik Mühendisliği **EEM311 Elektronik II** laboratuvarının **2010 güz dönemi** 5., 6. ve 7. deneylerine ait öğrenci çalışmalarını içeriyor (Aralık 2010): PSpice ön çalışmaları ve deney raporları. **Bir arkadaşın çalışması; kişisel bilgiler çıkarıldı.** 2010 programında Deney 8 (frekans cevabı) yapılmamıştı. Deney föyleri arşivde ayrı yazılarda (Deney 5–6 ve Deney 7–8) yer alıyor. Kişisel bilgilerden arındırılmış PDF kopyalar yazının sonunda ZIP olarak indirilebilir.

## Deney 5: MOSFET akım aynası

### Ön çalışma (PSpice)

DC analizde I_REF = 1.434 mA, I_O = 1.444 mA, V_GS1 = V_DS1 = V_GS2 = 3.566 V, V_DS2 = 5 V; öğrenci bu değerlerin ön çalışmadaki el hesaplarına çok yakın olduğunu not etmiş. V_CC2'nin 0–8 V taramasında I_O yaklaşık 1.5 V'tan sonra 1.4 mA civarında sabitleniyor.

### Rapor

Rapor akım aynasını şöyle tanımlıyor: girişine uygulanan referans akımını diğer kollara aynı ölçüde ya da belli oranlarda kopyalayan bir devre; teoride bir akım kaynağı gibi düşünülür ama pratikte her zaman öyle değildir. Kullanılan **CD4007** (Dual Complementary Pair Plus Inverter) üçer n ve p kanallı zenginleştirmeli MOS transistör içeriyor ve 14 bacaklı; girişleri statik yüke karşı diyotlarla korunmalı. Devre CD4007, 1 kΩ direnç ve ince kablolarla kurulup iki kaynak 5 V'a ayarlanmış.

1. V_D1 = 3.450 V, V_G1 = 3.408 V, I_D1 = 1.630 mA, I_REF = 1.617 mA; V_D2 = 5.085 V, V_G2 = 3.420 V, I_D2 = 1.650 mA, I_O = 1.623 mA.
1. V_CC2 0–8 V arasında değiştirilerek I_O ölçülmüş; 1.25 V'tan sonra akım sabit bir değere yaklaşıyor:

| V_CC2 | I_O | V_CC2 | I_O |
|---|---|---|---|
| 0 V | 0 mA | 3.25 V | 1.689 mA |
| 0.25 V | 0.570 mA | 3.5 V | 1.692 mA |
| 0.5 V | 1.041 mA | 3.75 V | 1.697 mA |
| 0.75 V | 1.270 mA | 4 V | 1.698 mA |
| 1 V | 1.550 mA | 4.5 V | 1.706 mA |
| 1.25 V | 1.594 mA | 5 V | 1.712 mA |
| 1.5 V | 1.640 mA | 5.5 V | 1.718 mA |
| 1.75 V | 1.650 mA | 6 V | 1.723 mA |
| 2 V | 1.660 mA | 6.5 V | 1.727 mA |
| 2.25 V | 1.665 mA | 7 V | 1.732 mA |
| 2.5 V | 1.674 mA | 8 V | 1.741 mA |
| 2.75 V | 1.680 mA | | |
| 3 V | 1.685 mA | | |

- **3. madde:** Çıkış direnci: R_O = (6 − 4) V / [(1.723 − 1.698) mA] = **80 kΩ**. Çıkış akımı V_DS ile değiştiği için akım kaynağı, paralelinde dirençli bir eleman varmış gibi davranıyor.

*Not: Raporun 2. maddesinde MOSFET'in bu ölçümde "triyot (lineer) bölgede" çalıştığı yazıyor; bu yalnız akımın hızla arttığı küçük gerilimler (≈ 1.25 V'a kadar) için doğru, akımın sabitlendiği bölgede M2 doymada çalışıyor.*

## Deney 6: Aktif yüklü CMOS ortak kaynaklı yükselteç

### Ön çalışma (PSpice)

R_REF = 25 kΩ ile: transistör akımları 0.566 mA, 0.566 mA ve 0.509 mA; ilgili V_DS değerleri 2.764 V, −12.236 V ve −2.29 V; geçici simülasyonda kazanç **−41.456**. R_REF yerine NMOS (Q4) konunca bütün kollardan 12.61 mA akıyor, V_DS değerleri 7.756 V, −7.244 V, −7.244 V; kazanç **−19.632**. Her durumda hangi transistörün triyot, hangisinin doyum bölgesinde olduğu işaretlenmiş.

*Not: Ön çalışmanın e şıkkında "R_REF yerine NMOS koyunca kazançta artış gözlendi" yazıyor; sonuçlara göre kazanç −41.5'ten −19.6'ya düşüyor.*

### Rapor

Devre CD4007, 1 MΩ ve 100 kΩ dirençler, 100 kΩ'luk pot ve iki 10 µF kapasitörle kurulmuş; kaynak 15 V, sinyal 5 kHz, 50 mV.

1. R_REF pot ile ayarlanmış: **R_REF = 25 kΩ**, I_O = I_D = 0.82 mA, V_A = 13.01 V, V_G = 2.67 V, V_D = 2.80 V. Ön çalışmaya çok yakın; farklar direnç toleransı ve ölçüm hassasiyetinden.
1. Osiloskop ölçümü: A_v = v_out / v_in = 1.47 V / 48.4 mV ≈ **−29.7** (giriş tam 50 mV'a ayarlanamamış; giriş ve çıkış ters fazlı).
1. Pot yöntemiyle **R_in = 58.3 kΩ**.
1. Aktif yükün avantajı: çıkış direnci yüksek olduğu için daha büyük kazanç elde ediliyor; ayrıca direnç kullanılmadığından entegre devrelerde büyük dirençlerin kaplayacağı alandan kazanılıyor.

*Not: 1.47 V / 48.4 mV ≈ 30.4; raporda 29.7 yazıyor.*

## Deney 7: BJT fark yükselteci

### Ön çalışma (PSpice)

R_REF = 5 kΩ, R_C = 9.7 kΩ, R_E = 250 Ω, R_A = R_B = 2.2 kΩ, V_CC = 15 V, V_EE = −15 V:

| Büyüklük | Değer |
|---|---|
| I_CQ1,2 | 0.978 mA |
| I_CQA,B | 1.980 mA |
| V_CE1,2 | 6.181 V |
| A_vdm-diff | −34.372 |
| A_vdm-se1 / A_vdm-se2 | −18.226 / 18.226 |
| v_idm (p-p) | 99.046 mV |
| A_vcm-se1 = A_vcm-se2 | −3.8495 |

*Not: Ortak mod kazancı için kullanılan PSpice ifadesinde iki çıkış çarpılmış (V(RC1:1)*V(RC2:1)); −3.85 sonucu bu yüzden anlamsız, deneyde ölçülen değer 0.0005 civarında. Ayrıca belgede v_out1,2 için 7.2055 Vp-p, v_odm için 3.3976 Vp-p okunmuş; A_vdm-diff = −34.4 ve v_idm ≈ 99 mV ile v_odm ≈ 3.40 V, tek uçlu çıkışlar ise bunun yarısı (≈ 1.7 Vp-p) olmalı, yani 7.2055 V değeri tutarsız.*

### Rapor

Rapor fark yükseltecini şöyle anlatıyor: iki giriş ve iki çıkışı var; giriş sinyalleri iki transistörün bazına uygulanıyor, çıkışlar kolektörlerden alınıyor. R_E her iki transistörün ortak emetör direnci; R_C1 ve R_C2 kolektör yük dirençleri, bunlar olmasa kolektörden yükseltilmiş sinyal yerine hep +V_CC alınırdı. PNP transistörler kullanılsaydı +V_CC ve −V_EE'nin işaretleri yer değiştirirdi. Devre dört 2N3904, iki 100 µF kapasitör, iki 2.2 kΩ direnç, 500 Ω ve 10 kΩ potlarla kurulmuş; R_C için 10 kΩ kullanılmış, kaynaklar ±15 V.

1. DC (girişler topraklı, kapasitörler sökülü; R_POT, V_CE1,2 ≈ 6 V olacak biçimde ayarlı): I_CQA = I_CQB = 2.01 mA, V_CE1 = 5.651 V, V_CE2 = 5.652 V, I_CQ1 = 1.05 mA, I_CQ2 = 1.03 mA, V_C1 = 4.973 V, V_C2 = 4.974 V.
1. v_in2 topraklı, Q1'e 100 mVp-p, 1 kHz: v_out1 = −2.07 V, v_out2 = 2.07 V → A_vdm-se1 = **−20.7**, A_vdm-se2 = **20.7**.
1. v_in1 topraklı, Q2'ye aynı sinyal: v_out1 = 2.07 V, v_out2 = −2.07 V → A_vdm-se1 = 20.7, A_vdm-se2 = −20.7.
1. Osiloskobun Math menüsüyle CH1 − CH2: v_odm = −4.09 V → **A_vdm-diff = −40.9**.
1. İki girişe 8 Vp-p, 1 kHz: v_out1 = v_out2 = 4 mV → A_vcm-se1 = A_vcm-se2 = 4 mV / 8 V = **0.0005**.
1. **CMRR = A_vdm-se / A_vcm-se = 20.7 / 0.0005 = 41.4 k** (≈ 41 400).
1. Ölçümlerle hesaplar arasındaki farkların nedeni: deneydeki transistörlerin β'sının simülasyondakinden farklı olması ve R_E'nin potansiyometreyle iki tarafta tam 250 Ω yapılamaması (transistörlerden birinden muhakkak daha fazla akım geçiyor).

| | Ön çalışma | Deney |
|---|---|---|
| A_vdm-se1 / A_vdm-se2 | −18.226 / 18.226 | −20.7 / 20.7 |
| A_vdm-diff | −34.372 | −40.9 |
| A_vcm-se | −3.8495 | 0.0005 |

## Yayınlanmayan dosyalar

Bu dönemin PSpice proje dosyaları klasörde yoktu; yalnızca Word belgeleri vardı.
