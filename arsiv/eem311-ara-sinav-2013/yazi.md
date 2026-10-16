---
baslik: EEM311 Elektronik II: 2013 Güz Ara Sınavı Soruları ve Çözümleri
ozet: EEM311 Elektronik II dersinin 18 Kasım 2013 tarihli ara sınavının beş sorusu ve çözümleri: A sınıfı emetör izleyici (verim), akım kaynaklı fark yükselteci, emetör izleyicinin alt kesim frekansı, iki op-amp'lı köprü çıkışlı yükselteç tasarımı ve Darlington çiftinin akım kazancı.
---

Bu yazı, Başkent Üniversitesi Elektrik-Elektronik Mühendisliği **EEM 311 Elektronik II** dersinin **2013-2014 güz yarıyılı ara sınavını** (18.11.2013) aktarıyor. Kaynak, bir arkadaşın paylaştığı sınav kâğıdı fotoğraflarıdır; kâğıtlarda basılı sorular ve kırmızı puanlarla işaretlenmiş çözümler var. Kişisel bilgiler çıkarıldı. Sorular ve çözümlerin ana adımları fotoğraflanmış sayfalardan metne aktarıldı; fotoğrafların kendisi yayınlanmıyor.

Sınav 100 dakika sürmüş, puan dağılımı şöyle:

| Soru | 1 | 2 | 3 | 4 | 5 | Toplam |
|---|---|---|---|---|---|---|
| Puan | 20 | 20 | 23 | 20 | 17 | 100 |

Kâğıdın başındaki uyarılar: tüm hesaplamaları, kullanılan ifadenin çıkarımını göstererek yapın; cevaplar için soruların altındaki boşlukları ve kâğıdın arkasını kullanın, ek kâğıt istemeyin.

## Soru 1: A sınıfı emetör izleyici (20p)

Aşağıdaki A sınıfı emetör izleyici devredeki DC besleme gerilimleri V⁺ = +12 V, V⁻ = −12 V ve yük direnci R_L = 100 Ω'dur. Transistörlere ait parametreler β = 200, V_BE = 0,7 V'dur. Devreden alınan ac çıkış gerilimi +10 V ile −10 V arasında değişen bir sinüsoidal sinyaldir. Buna göre:

- a) I_Q akımının minimum değeri ne olmalıdır ve bunu sağlayacak R değeri nedir? (8p)
- b) Çıkış gerilimi v₀ = 0 iken devrenin kaynaklardan çektiği DC giriş gücünü bulunuz. (4p)
- c) Devreden alınan ac çıkış gücünü ve devrenin % verimini bulunuz. (8p)

*Devre:* Q₁ emetör izleyicidir (kolektörü V⁺'ya bağlı, girişi v_I). Emetörü hem çıkış (v_O, R_L üzerinden toprağa) hem de I_Q akımını çeken Q₂'ye bağlıdır. Q₂ ile Q₃ bir akım aynasıdır; referans akımı topraktan R direnci üzerinden diyot bağlı Q₃'e akar, emetörler V⁻'ye bağlıdır.

### Çözüm

**a)** I_Q(min) = v_O(max) / R_L = 10 / 0,1 kΩ ⇒ **I_Q(min) = 100 mA**

R = [0 − 0,7 − (−12)] / 100 mA ⇒ **R = 113 Ω**

**b)** P_Q1 = I_Q · V_CE1 = (100 mA)(12 V) ⇒ P_Q1 = 1,2 W

P(kaynak) = 2 I_Q (12 V) = **2,4 W**

**c)** P̄_L = ½ · V_P² / R_L = (10)² / (2 · 100) = **0,5 W**

P̄_S = 1,2 + 2,4 = 3,6 W

η = P̄_L / P̄_S = 0,5 / 3,6 ⇒ **η = %13,9**

## Soru 2: Akım kaynaklı fark yükselteci (20p)

Aşağıdaki devrede yer alan transistörler için V_A = ∞ (Early gerilimi) olarak verilmiştir. DC I_Q akım kaynağı ideal olduğuna göre, devrenin ac (küçük sinyal) eşdeğer devresini çiziniz (6p) ve farksal mod kazancının ifadesini çıkarınız: A_d = V_o / V_d = ? (V_d = V₁ − V₂) (14p)

*Devre:* Q₁ ve Q₂'nin emetörleri birleşik ve I_Q akım kaynağıyla V⁻'ye bağlı. Q₁'in kolektörü doğrudan V⁺'ya, Q₂'nin kolektörü R_C üzerinden V⁺'ya bağlı; çıkış v_O, Q₂'nin kolektöründen alınıyor ve bu düğümde R_L toprağa bağlı. Girişler v₁ (Q₁ bazı) ve v₂ (Q₂ bazı).

### Çözüm

Eşdeğer devrede her transistör r_π ve g_m·V_π bağımlı akım kaynağıyla modellenir; ideal akım kaynağı ac'de açık devredir, R_C ile R_L ac'de paraleldir.

KVL denklemi: v₁ = V_π1 − V_π2 + v₂, yani v₁ − v₂ = V_π1 − V_π2

KCL denklemi (emetör düğümü):

V_π1 / r_π + g_m V_π1 + g_m V_π2 + V_π2 / r_π = 0 ⇒ (V_π1 + V_π2)(1/r_π + g_m) = 0 ⇒ V_π1 = −V_π2

Buradan v₁ − v₂ = −2 V_π2, yani V_π2 = −½ (v₁ − v₂).

v_o = −g_m V_π2 (R_C ‖ R_L) = ½ g_m (R_C ‖ R_L)(v₁ − v₂)

v₁ − v₂ ≡ v_d için: **A_d = v_o / v_d = ½ g_m (R_C ‖ R_L)**

## Soru 3: Emetör izleyicinin frekans cevabı (23p)

Aşağıdaki yükselteç devresinin β = 100, C_o = 1 µF, r_e = 31 Ω, r_o = 143 kΩ (fotoğrafta "r_e" simgesi tam seçilemiyor; çözümde r_π = 3,10 kΩ kullanılmış, bu da (1+β)·31 Ω'a karşılık geliyor):

- a) Alt kesim frekansını bulunuz. (7p)
- b) Devrenin orta band kazancını (A_vmid) R_S ve R_L'yi dikkate alarak hesaplayınız. (6p)
- c) Kazancın dB cinsinden gösterildiği frekans cevabını çiziniz. (5p)
- d) Frekansı 10 Hz olan bir giriş sinyali için devrenin kazancı ne olur, hesaplayınız. (5p)

*Devre:* +10 V ve −10 V ile beslenen emetör izleyici. Kaynak v_s, R_S = 0,5 kΩ üzerinden baza bağlı; baz R_B = 100 kΩ ile toprağa bağlı. Emetör R_E = 10 kΩ üzerinden −10 V'a bağlı; çıkış emetörden C_o kuplaj kapasitesi üzerinden R_L = 10 kΩ yüküne alınıyor.

### Çözüm

**a)** Kuplaj kapasitesinin gördüğü direnç, emetörden bakıldığında çıkış direncidir:

R_o = R_E ‖ r_o ‖ [ (r_π + R_S ‖ R_B) / (1 + β) ]

= 10 ‖ 143 ‖ [ (3,10 + 0,5 ‖ 100) / 101 ] = 10 ‖ 143 ‖ 0,0356 kΩ ⇒ **R_o ≅ 35,5 Ω**

τ_S = (R_o + R_L) C_o = (35,5 + 10⁴)(10⁻⁶) ≅ 1 × 10⁻² s

Buna göre 3 dB frekansı: **f_L = 1 / (2π τ_S) = 1 / [2π(10⁻²)] = 15,9 Hz**

**b)** Orta bandda kapasite kısa devre kabul edilir:

A_v = v_o / v_i = (r_o ‖ R_E ‖ R_L) / [r_e + (r_o ‖ R_E ‖ R_L)], burada r_o ‖ R_E ‖ R_L = 143 k ‖ 5 k = 4,831 kΩ

A_v = 4,831 k / (0,031 k + 4,831 k) = 4,831 / 4,862 ⇒ A_v ≅ 0,9936

Kaynak direnci de hesaba katılınca (girişte R_S ile baza bakan direnç arasındaki bölücü): A_vs = v_o / v_s ≅ 0,9936 × 0,999 ⇒ **A_vmid ≅ 0,992**

**c)** Kazanç eğrisi f_L = 15,9 Hz'in altında 20 dB/dekad eğimle düşen, üstünde ≅ 0,99 (≅ 0 dB) değerinde düzleşen birinci dereceden yüksek geçiren karakteristiktir (çözümde 1 Hz–1000 Hz arasında logaritmik eksende çizilmiş).

**d)** 10 Hz için: A = 0,992 / √(1 + (15,9/10)²)

*Not: Çözüm kâğıdında sonuç yazılmamış; hesaplanırsa √(1 + 1,59²) ≅ 1,88 olduğundan kazanç ≅ 0,53 bulunur.*

## Soru 4: İki op-amp'lı yükselteç tasarımı (20p)

Aşağıda iki ideal op-amp'ın kullanıldığı bir yükselteç devresi yer almaktadır. Devrede:

- a) Devrenin gerilim kazancının ifadesini çıkarınız (A_v = V_L / V₁). (12p)
- b) Devreyi A_v = V_L / V₁ = 15 ve aynı zamanda |V_o1| = |V_o2| olacak şekilde tasarlayınız (gerekli direnç değerleri R₁, R₂, R₃, R₄ nasıl seçilmelidir?). (8p)

*Devre:* Birinci op-amp evirmeyen yükselteçtir (girişi v_I, geri beslemede R₂, eviren giriş ile toprak arasında R₁); çıkışı v_O1. İkinci op-amp eviren yükselteçtir (girişte R₃, geri beslemede R₄) ve v_O1'i girişine alır; çıkışı v_O2. Yük R_L iki çıkışın arasına bağlıdır, v_L = v_O1 − v_O2.

### Çözüm

**a)** v_O1 = (1 + R₂/R₁) v_I

v_O2 = −(R₄/R₃) · v_O1 = −(R₄/R₃)(1 + R₂/R₁) v_I

v_L = v_O1 − v_O2 = (1 + R₂/R₁)(1 + R₄/R₃) v_I

Buna göre: **A_v = (1 + R₂/R₁)(1 + R₄/R₃)**

**b)** |v_O1| = |v_O2| isteniyor ⇒ **R₄ = R₃** olmalı.

O zaman (1 + R₂/R₁)(2) = 15 ⇒ **R₂/R₁ = 6,5**

## Soru 5: Darlington çiftinin akım kazancı (17p)

Aşağıdaki devrede yer alan transistörler için β = 100, V_A = ∞, r_e1 = 2,03 kΩ, r_e2 = 20,2 Ω olarak verildiğine göre, devrenin ac (small signal) eşdeğer devresini çizerek (5p) akım kazancını bulunuz: A_i = I_o / I_i = ? (12p)

*Devre:* V_CC = +10 V. Q₁ ve Q₂ Darlington bağlıdır (Q₁'in emetörü Q₂'nin bazına, iki kolektör birlikte R_C = 2,2 kΩ üzerinden V_CC'ye). Baz polarması R₁ = 335 kΩ (V_CC'ye) ve R₂ = 125 kΩ (toprağa); giriş v_i, C_C kuplaj kapasitesiyle baza bağlı. Q₂'nin emetöründe R_E = 1 kΩ ve paralel köprüleme kapasitesi C_E var. Çıkış akımı I_o, R_C'den akan akımdır.

### Çözüm

I_o = g_m1 V_π1 + g_m2 V_π2 = β₁ I_b1 + β₂ I_b2, burada I_b2 = (β₁ + 1) I_b1

I_o = I_b1 (β₁ + β₂ + β₁β₂) ⇒ I_o / I_b1 = β₁ + β₂ + β₁β₂ ≅ β₁β₂

Girişten görülen direnç: R_ib = β₁ r_e1 + β₁β₂ r_e2 = 100 (2,03 k + 2,02 k) = 100 (4,05 k) ⇒ R_ib = 405 kΩ

R₁ ‖ R₂ = 125 k ‖ 335 k = 91,03 kΩ

Akım bölücü: I_b1 / I_i = (R₁ ‖ R₂) / [(R₁ ‖ R₂) + R_ib] = 91,03 k / (91,03 k + 405 k) ≅ 0,183

A_i = (I_o / I_b1) · (I_b1 / I_i) ≅ β₁β₂ · 0,1835 ⇒ **A_i ≅ 1835**
