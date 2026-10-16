---
baslik: EEM214 Elektronik I: EEM311 Laboratuvarı İçin Öğrenci Raporları ve Ön Çalışmalar (2011–2012)
ozet: EEM214 Elektronik I klasöründe saklanan EEM311 Elektronik II laboratuvar çalışmaları: 2011 güz döneminin sekiz Proteus raporu (BJT ve FET yükselteçleri, iki katlı yükselteç, akım aynası, aktif yük, fark yükselteci, frekans cevabı) ve 2012 güz döneminin PSpice ön çalışmaları (fark yükselteci, op-amp, aktif filtre).
---

Bu yazı, EEM214 Elektronik I dersinin laboratuvar klasöründe saklanmış ama aslında bir sonraki dönemin dersi **EEM311 Elektronik II** laboratuvarı için hazırlanmış öğrenci çalışmalarını bir araya getiriyor. 2011 güz dönemine ait sekiz rapor, laboratuvarda yapılan ölçümlerin Proteus simülasyonlarıyla karşılaştırıldığı Türkçe raporlar; 2012 güz dönemine ait dosyalar ise çoğunlukla PSpice ön çalışmaları. Hepsi arkadaşların çalışması; ad ve öğrenci numaraları kapatıldı. Deneylerin föyleri arşivdeki EEM311 yazılarında bulunuyor: [Deney 1–2](/arsiv/eem311-deney-1-2-bjt-yukselteci/), [Deney 3–4](/arsiv/eem311-deney-3-4-mosfet-iki-katli/), [Deney 5–6](/arsiv/eem311-deney-5-6-akim-aynasi-aktif-yuk/), [Deney 7–8](/arsiv/eem311-deney-7-8-fark-frekans-cevabi/). Kişisel bilgileri kapatılmış PDF kopyaları yazının sonunda ZIP olarak indirilebilir.

## 2011 güz raporları

### Rapor 1: Ortak emetörlü BJT yükselteci, küçük sinyal parametreleri

DC analizde I_BQ = 31 µA, I_CQ = 8.396 mA, V_CEQ = 6.24 V; **β = 8.396 mA / 31 µA ≈ 270.6**. 1 kHz, 40 mV(pp) girişle ölçülen v_be'den r_π = 606.66 Ω ve n = 0.7279 hesaplanmış; ölçülen V_out = 4.48 V ile g_m = 0.288 S, r_o ≈ 25 kΩ ve V_A ≈ 199 V bulunmuş. Proteus'ta 2 mV(pp) girişte v_be = 7.3 mV(pp), bozulmasız en büyük çıkış 12.8 V(pp); 20, 140 ve 500 mV(pp) girişlerde çıkışın kırpılması gösterilmiş.

### Rapor 2: BJT yükseltecinde kazanç, kırpılma ve giriş direnci

I_CQ = 3.00 mA, V_CEQ = 1.80 V. 5 kHz, 100 mV(pp) girişte A_v = 1489.4 mV / 100 mV ≈ **14.9**. 1 V(pp) girişte çıkış 3.25 V ve −4.75 V'ta, 6 V(pp) girişte 2.25 V ve −8.00 V'ta kırpılıyor; kırpılma yaklaşık 150 mV(pp) girişte başlıyor (Proteus'ta üçgen dalga olmadığı için sinüsle bakılmış). Girişe 10 kΩ seri dirençle V_out = 44 mV'tan **R_in ≈ 7.86 kΩ**.

### Rapor 3: FET'li ortak kaynaklı yükselteç

V_G = 3.72 V, V_D = 8.61 V, V_S = 1.70 V. 1 kHz, 6 mV(pp) girişte V_out = 480 mV, **A_v = 80**; C_d ve R_L çıkarılınca ve C_S çıkarılınca kazancın nasıl değiştiği simüle edilmiş (kullanılması gereken FET Proteus'ta olmadığı için değerler farklı çıkmış). Giriş 20 mV(pp)'de çıkış kırpılıyor. 20 kΩ potansiyometreyle R_in ≈ 26.15 kΩ ve R_out ≈ 60 kΩ hesaplanmış.

### Rapor 4: İki katlı (FET + BJT) yükselteç

12 V'ta V_G = 0 V, V_D = 5.87 V, V_S = 2.02 V; V_B = 6.98 V, V_C = 9.16 V, V_E = 6.29 V; I_C = 2.84 mA, I_D = 6.13 mA. 1 kHz girişte birinci kat kazancı 8, ikinci kat 88.75, **toplam kazanç 710**. Giriş 360 mV(pp)'de kırpılma; 500 kΩ seri dirençle **R_in ≈ 0.97 MΩ ≈ 1 MΩ**, çıkışa 1 kΩ ile **R_out ≈ 0.96 kΩ ≈ 1 kΩ**.

### Rapor 5: MOSFET akım aynası

V_CC1 = V_CC2 = 5 V, R = 1 kΩ. CD4007 Proteus'ta olmadığı için BUK445 kullanılmış: simülasyonda I_REF = I_O = 2.89 mA, ölçümde I_REF = 1.86 mA, I_O = 1.68 mA. V_CC2 taramasında I_O, V_CC2 = 25 mV'ta 1.18 mA, 100 mV'ta 2.87 mA ve 110 mV'tan sonra 2.89 mA'de sabit; çıkış direnci değerlendirilmiş.

### Rapor 6: Akım aynası yüklü (aktif yüklü) yükselteç

I_REF = 0.6 mA için R_REF = 22 kΩ (ölçülen I_REF = 0.67 mA). Simülasyonda 50 mV(pp), 5 kHz girişte ilk devrede kazanç elde edilemediği, düzenlenen devrede V_out = 920 mV ile **A_v = 18.4** bulunduğu yazılmış. R_in ≈ 28 kΩ (deneyde 50 kΩ).

### Rapor 7: BJT fark yükselteci

R_REF = 4.70 kΩ, R_POT = 310 Ω. Ölçümde I_CQA = I_CQB = 2 mA, V_CE1 = 4.58 V, V_CE2 = 6.252 V, I_CQ1 = 1.213 mA, I_CQ2 = 0.916 mA; simülasyonda iki taraf dengeli (I_CQ1,2 = 1.03 mA, V_CE1,2 = 5.39 V).

| | Deney | Simülasyon |
|---|---|---|
| v_in1 = 100 mV(pp): A_vdm-se1 / A_vdm-se2 | 27.0 / 121.0 | 15.2 / 0 |
| v_in2 = 100 mV(pp): A_vdm-se1 / A_vdm-se2 | 120.0 / 26.0 | 0 / 15.2 |
| A_vdm-diff | 96.3 | 29 |
| Ortak mod çıkışları | 9.46 V | 7.19 V |

Raporda simülasyonda CMRR = ∞, deneyde CMRR = 0.092 bulunduğu yazılmış.

*Not: Raporda A_vdm-diff = 9.3 V / 100 mV = "96.3" yazılmış; 9.3 V / 0.1 V = 93'tür. Ortak mod kazancı da "vout1·vout2/((vout1 + vout2)/2)" gibi hatalı bir ifadeyle hesaplanmış; tek uçlu ortak mod kazancı A_vcm-se = v_out / v_icm'dir ve CMRR = A_vdm-se / A_vcm-se oranı 1'den büyük olmalıdır.*

### Rapor 8: Ortak emetörlü yükseltecin frekans cevabı

Devre: V_CC = 12 V, R1 = 8.2 kΩ, R2 = 3.9 kΩ, R_C = 6.3 kΩ, R_E = 3.3 kΩ, R_S = 3 kΩ, R_L = 3.9 kΩ, C1 = 10 µF, C2 = 1 µF, C_E = 10 µF, 2N3904. Deneyde I_CQ = 0.81 mA, V_CEQ = 3.06 V (simülasyonda 0.96 mA, 2.76 V). 20 mV(pp), 1 kHz girişte orta bant kazancı deneyde **25.81**, simülasyonda **31**. Frekans taramasında (30 Hz – 1.5 MHz) **f_L = 3.87 Hz, f_H = 425 kHz** bulunmuş; simülasyonda kazanç 30 Hz'te 15, 300 Hz – 20 kHz arasında yaklaşık 31, 500 kHz'te 18.5, 1.5 MHz'te 7.25.

## 2012 güz ön çalışmaları

- **Deney 3 ön çalışmaları:** JFET ve BJT'li iki katlı devrenin PSpice çizimleri (I_C, I_B, I_D, I_E dalga şekilleri).
- **Deney 5 ön çalışması:** MOSFET akım aynalı devrenin DC ve AC analizi (PSpice).
- **Deney 6 ön çalışması:** 2N3904/2N3906'lı aktif yüklü yükseltecin PSpice bias noktası değerleri ve dalga şekilleri (aynı dosyanın iki kopyası vardı, biri alındı).
- **Deney 7:** ortak emetörlü yükseltecin frekans taraması (örneğin 30 Hz'te V_out = 288.6 mV).
- **Deney 8 – "Introduction to Opamps" (03.12.2012):** BJT fark yükseltecinin simülasyonu.
- **Deney 9 – Operational Amplifiers:** 1 kΩ girişli eviren yükselteçte R_f = 4.7 kΩ, 10 kΩ ve 1 MΩ için 100 mV, 1 kHz sinüs simülasyonları; giriş işareti op-amp'in (−) girişine uygulandığı için devrenin "eviren yükselteç" olduğu, kare dalganın integralinin üçgen dalga olduğu yorumları.
- **Experiment 8 – Active Filters ön çalışması:** 3 kHz alçak geçiren ve 300 Hz yüksek geçiren filtre şemaları; C = 10 µF ile 3 kHz için R = 375.131 kΩ, 300 Hz için R = 53.05 Ω hesaplanmış.
- **RC osilatör:** 741 op-amp'li RC faz kaydırmalı osilatörün Multisim şeması ve osiloskop ekranı (yaklaşık 2.19 kHz).

*Not: f = 1/(2πRC) ile C = 10 µF için 300 Hz'te R ≈ 53 Ω doğru, ancak 3 kHz'te R ≈ 5.3 Ω olmalıdır (375 kΩ değil). Bu kadar küçük dirençler pratik olmadığından genellikle nF mertebesinde kondansatör seçilir.*

## İndirme

ZIP dosyasında 2011 dönemine ait sekiz raporun ve 2012 dönemine ait dokuz ön çalışma/raporun kişisel bilgileri kapatılmış PDF kopyaları bulunuyor.
