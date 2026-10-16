---
baslik: EEM311 Elektronik II: Ocak 2016 Final Sınavı ve Diğer Sınav Soruları, Çözümleriyle
ozet: EEM311 Elektronik II dersinin 4 Ocak 2016 tarihli final sınavı (op-amp köprü yük sürücü, transkondüktans geri beslemeli yükselteç, BJT frekans cevabı, fark yükselteci, EKG filtresi) ve tarihi belirsiz sınavlardan faz dedektörü filtresi, dalga şekli üreteci, ortak geçitli yükselteç ve MOSFET frekans cevabı soruları, çözümleriyle.
---

Bu yazı, Başkent Üniversitesi Elektrik-Elektronik Mühendisliği **EEM 311 Elektronik II** dersinin **2015-2016 güz yarıyılı final sınavını** (04.01.2016) ve aynı fotoğraf grubunda yer alan, hangi sınava ait olduğu kâğıtta yazmayan başka sınav sorularını aktarıyor. Kaynak, arkadaşların paylaştığı ve konu konu derlediği sınav kâğıdı fotoğraflarıdır (fotokopi cevap anahtarları, öğrenci çözümleri ve puanlanmış kâğıtlar). Kişisel bilgiler çıkarıldı. Sorular ve çözümlerin ana adımları fotoğraflanmış sayfalardan metne aktarıldı; fotoğrafların kendisi yayınlanmıyor.

## 4 Ocak 2016 final sınavı

Kâğıdın başındaki puan tablosu ve tarih (04.01.2016) yalnızca 1. sorunun sayfasında görünüyor. Sınav 150 dakika sürmüş:

| Soru | 1 | 2 | 3 | 4 | 5 | Toplam |
|---|---|---|---|---|---|---|
| Puan | 20 | 25 | 20 | 20 | 15 | 100 |

Aşağıdaki 2–5. sorular, soru numaraları ve puanları bu tabloyla birebir örtüştüğü ve aynı kâğıt destesinin fotoğraflarında yer aldıkları için bu sınava atfedildi; sayfalarında tarih yok.

### Soru 1: İki op-amp'lı köprü yük sürücü (20p)

Aşağıdaki devrede:

- a) Gerilim kazancının (A_v = V_L / V_I) ifadesini çıkarınız. (10p)
- b) R₁ = 50 kΩ alarak |V_O1| = |V_O2| ve A_v = 10 olacak şekilde devreyi tasarlayınız (bilinmeyen direnç değerlerini belirleyiniz). (5p)
- c) R_L = 20 Ω ve bu yük direnci üzerinde harcanan güç 10 W ise |V_O1| = |V_O2| gerilimlerinin tepe (peak) değerini ve yük üzerinden geçen akımın tepe (peak) değerini bulunuz. (5p)

*Devre:* Birinci op-amp'ın evirmeyen girişine v_I uygulanıyor; çıkışı v_O1. v_O1'den birinci op-amp'ın eviren girişine R₂ bağlı; bu düğümden R₁, ikinci op-amp'ın eviren girişine (sanal toprak) gidiyor. İkinci op-amp'ın evirmeyen girişi toprakta, geri beslemesinde R₃ var, çıkışı v_O2. Yük R_L iki çıkışın arasında, v_L = v_O1 − v_O2.

**Çözüm (cevap anahtarı):**

**a)** R₁'den geçen akım i = v_I / R₁ (ikinci op-amp'ın eviren girişi sanal toprak).

v_O1 = i R₂ + v_I = v_I (1 + R₂/R₁)

v_O2 = −i R₃ = −v_I (R₃/R₁)

v_L = v_O1 − v_O2 = v_I (1 + R₂/R₁) + v_I (R₃/R₁) ⇒ **A_v = v_L / v_I = 1 + R₂/R₁ + R₃/R₁**

**b)** A_v = 10 ⇒ R₂/R₁ + R₃/R₁ = 9. |v_O1| = |v_O2| için 1 + R₂/R₁ = R₃/R₁. Bu ikisinden R₂/R₁ = 4 ve R₃/R₁ = 5 bulunur. R₁ = 50 kΩ ⇒ **R₂ = 200 kΩ, R₃ = 250 kΩ**.

**c)** P̄ = ½ V_P² / R_L ⇒ V_P = √(2 R_L P̄) = √(2 · 20 · 10) = 20 V

|v_O1| = |v_O2| = **10 V** (tepe); yük akımının tepe değeri = 20 V / 20 Ω = **1 A**.

### Soru 2: Transkondüktans geri beslemeli yükselteç (25p)

Aşağıda geri beslemeli bir yükseltecin transistör modellemesi yapılmamış ac eşdeğeri verilmiştir. Devrenin DC analizi sonunda elde edilen kolektör akımları I_C1 = 0,5 mA, I_C2 = 1 mA ve I_C3 = 2 mA'dir. Tüm transistörler için β = 120, V_T = 26 mV ve r_o = ∞ olarak verildiğine göre, devrenin transkondüktans transfer fonksiyonunu bulunuz: A_gf = I_o / V_s. (25p)

*Devre:* Üç kaskat BJT. Q₁'in bazına V_s uygulanıyor; R_C1 = 5 kΩ, emetöründe R_E1 = 0,1 kΩ. Q₂'nin bazı Q₁'in kolektörüne bağlı, emetörü topraklı, R_C2 = 2 kΩ. Q₃'ün bazı Q₂'nin kolektörüne bağlı, R_C3 = 1 kΩ (I_o bu dirençten akan çıkış akımı), emetöründe R_E3 = 0,1 kΩ. Geri besleme direnci R_F = 0,8 kΩ, Q₁ ile Q₃'ün emetörleri arasında (seri-seri geri besleme).

**Çözüm (cevap anahtarı, basılı İngilizce çözüm):**

Küçük sinyal parametreleri: g_m = I_C / V_T ve r_π = β / g_m

- g_m1 = 19,23 mA/V, g_m2 = 38,46 mA/V, g_m3 = 76,92 mA/V
- r_π1 = 6,24 kΩ, r_π2 = 3,12 kΩ, r_π3 = 1,56 kΩ

Düğüm denklemleri (V_e1 ve V_e3 iki emetör düğümünün gerilimi):

1. V_s = V_π1 + V_e1
1. V_π1 / r_π1 + g_m1 V_π1 = V_e1 / R_E1 + (V_e1 − V_e3) / R_F
1. V_π2 = −g_m1 V_π1 (R_C1 ‖ r_π2)
1. g_m2 V_π2 + (V_π3 + V_e3) / R_C2 + V_π3 / r_π3 = 0
1. V_π3 / r_π3 + g_m3 V_π3 = V_e3 / R_E3 + (V_e3 − V_e1) / R_F

Sayısal değerler yerine konup V_π1, V_π2 ve V_e'ler yok edildiğinde −V_s(517,5) + V_π3(405,95) = 0 elde ediliyor. Çıkış akımı I_o = g_m3 V_π3 = 76,92 V_π3, yani V_π3 = I_o(0,0130):

−V_s(517,5) + I_o(0,0130)(405,95) = 0 ⇒ **A_gf = I_o / V_s ≅ 98,05 mA/V**

Aynı devre, 2016 yaz okulu notlarında da örnek soru olarak ele alınmış.

### Soru 3: BJT yükseltecin frekans cevabı (20p)

β = 120, r_o = ∞, g_m = 29,2 mA/V, r_π = 4,12 kΩ ve C = 165 pF (kapasitenin simgesi fotoğrafta seçilemiyor) parametrelerine sahip bir transistörün kullanıldığı aşağıdaki yükselteç devresinde C_C2 ve C_E kapasitelerinin değeri çok büyüktür (sonsuz kabul ediniz). Devrenin:

- a) Alt ve üst kesim frekanslarını bulunuz. (10p)
- b) Orta band kazancını bulunuz (A_v = V_o / V_s) ve toplam frekans cevabını çiziniz. (10p)

*Devre:* +10 V beslemeli ortak emetörlü yükselteç. Kaynak, R_S = 0,5 kΩ ve C_C1 = 4,7 µF üzerinden baza bağlı; baz polarması R₁ = 40 kΩ ve R₂ = 5 kΩ. R_C = 5 kΩ; emetörde R_E = 0,5 kΩ, C_E ile köprülü. Çıkış C_C2 üzerinden R_L = 2,5 kΩ'a.

**Çözüm (cevap anahtarı, basılı İngilizce çözüm):**

**a)** Üst kesim frekansı için:

τ_H = R_eq (C_π + C_M), R_eq = r_π ‖ R₁ ‖ R₂ ‖ R_S = 4,12 ‖ 40 ‖ 5 ‖ 0,5 ⇒ R_eq = 0,405 kΩ

τ_H = (0,405 × 10³)(15,6 + 149) × 10⁻¹² = 6,67 × 10⁻⁸ s ⇒ **f_H = 1 / (2π τ_H) = 2,39 MHz**

Alt kesim frekansı için:

τ_L = R_eq C_C1, R_eq = R_S + R₁ ‖ R₂ ‖ r_π = 0,5 + 40 ‖ 5 ‖ 4,12 ⇒ R_eq = 2,64 kΩ

τ_L = (2,64 × 10³)(4,7 × 10⁻⁶) = 1,24 × 10⁻² s ⇒ **f_L = 12,8 Hz**

**b)** V_o = −g_m V_π (R_C ‖ R_L)

V_π = [ (R₁ ‖ R₂ ‖ r_π) / (R₁ ‖ R₂ ‖ r_π + R_S) ] V_s = [ 2,14 / (2,14 + 0,5) ] V_s = 0,8106 V_s

|A_v| = (29,2)(0,8106)(5 ‖ 2,5) ⇒ **|A_v| = 39,4**

Frekans cevabı: f_L = 12,8 Hz ile f_H = 2,39 MHz arasında |A_v| ≅ 39,4 düz; iki uçta düşen trapez biçimli eğri.

*Not: Çözümdeki 149 pF, Miller kapasitesidir: C_M = C_μ (1 + g_m R_L′), R_L′ = R_C ‖ R_L = 1,67 kΩ için 1 + g_m R_L′ ≅ 49,7 olduğundan C_μ ≅ 3 pF'a karşılık gelir.*

### Soru 4: Emetör dirençli fark yükselteci (20p)

Aşağıdaki devrede yer alan transistörler özdeştir ve β = 100, r_o = ∞, |V_BE| = 0,7 V olarak verilmektedir.

- a) v₁ = v₂ = 0 için I_E, I_C1, I_C2, V_CE1, V_CE2 değerlerini bulunuz. (7p)
- b) Devre iki girişin farkını yükseltecek biçimde farksal modda çalıştırıldığında, yani v_d = v₁ − v₂ olan farksal bir ac giriş sinyali uygulandığında, devrenin ac eşdeğer devresini çizerek Q₂ transistörünün kolektöründen alınacak olan çıkış için farksal mod kazancının (A_d = v_o2 / v_d) ifadesini çıkarınız ve hesaplayınız. (13p)

*Devre:* ±5 V beslemeli fark yükselteci. Kolektör dirençleri R_C = 100 kΩ; iki emetörde birer 2 kΩ direnç, ortak düğümden R_E = 85 kΩ ile −5 V'a.

**Çözüm (cevap anahtarı):**

**a)** 0 = 0,7 + (I_E/2)(2) + I_E(85) − 5 ⇒ I_E = (5 − 0,7) / (85 + 1) ⇒ **I_E = 0,050 mA**

I_C1 = I_C2 = (β / (1+β)) (I_E / 2) = (100/101)(0,050/2) ⇒ **I_C1 = I_C2 = 0,0248 mA**

V_CE1 = V_CE2 = 5 − I_C1(100) − (−0,7) ⇒ **V_CE1 = V_CE2 = 3,22 V**

**b)** Farksal modda ortak emetör düğümü ac toprak gibi davranır; yarım devre için:

−v_d/2 = V_π + (V_π / r_π + g_m V_π) R_E = V_π [1 + (1+β) R_E / r_π] (burada R_E = 2 kΩ emetör direnci)

V_π = −(v_d/2) / [1 + (1+β) R_E / r_π]

v_o = −g_m V_π R_C ⇒ A_d = ½ · β R_C / [r_π + (1+β) R_E]

r_π = β V_T / I_CQ = (100)(0,026) / 0,0248 = 105 kΩ

A_d = ½ · (100)(100) / [105 + (101)(2)] ⇒ **A_d ≅ 16,3**

### Soru 5: EKG sinyali için filtre tasarımı (15p)

Bir EKG ölçüm sisteminde yer alan enstrümantasyon yükseltecinin çıkışındaki EKG sinyallerinin 1 Hz – 150 Hz aralığındaki bileşenlerinin ikinci derece geniş bantlı bir filtre devresi ile alınması, ancak 50 Hz'lik şehir şebeke frekansına ait bileşenlerin de 48 Hz – 52 Hz aralığında birinci derece bir filtre ile bastırılması istenmektedir. İstenen devreleri çiziniz ve gerekli eleman değerlerini bularak tasarlayınız. (15p)

**Puanlanmış bir öğrenci çözümü:**

- Bant geçiren filtre (BGF): ikinci derece Butterworth alçak geçiren filtre (AGF, f_AGF = 150 Hz, R₁ = R₂ = 1 / (2π√2 · 150 Hz · C)) ile ikinci derece yüksek geçiren filtrenin (YGF, f_YGF = 1 Hz, R = 1 / (2π√2 · 1 Hz · C)) kaskat bağlanması; C değeri seçilecek.
- Bant durduran (çentik) filtre: birinci derece AGF (R_a, C_a) ile birinci derece YGF'nin (C_b, R_b) çıkışları bir eviren toplayıcıda (eşit R'ler) toplanıyor; çözümde f_AGF = 52 Hz (R_a = 1 / (2π · 52 Hz · C_a)) ve f_YGF = 48 Hz (R_b = 1 / (2π · 48 Hz · C_b)) alınmış.
- Kâğıtta kırmızıyla puanlar işaretlenmiş; iki filtrenin birbirine bağlantısı eksik bulunarak 2 puan kırılmış.

*Not: Paralel AGF + YGF toplamıyla bant durduran filtre kurulurken AGF'nin kesim frekansı bandın altında (48 Hz), YGF'ninki üstünde (52 Hz) olmalıdır. Çözümdeki gibi AGF 52 Hz, YGF 48 Hz seçilirse iki filtrenin geçirme bantları üst üste biner ve 50 Hz bastırılmaz.*

## Tarihi belirsiz sınavlardan sorular

Aşağıdaki sorular aynı fotoğraf grubunda yer alıyor ama sayfalarında sınav adı ve tarih yok. Soru numaraları birbiriyle çakıştığından (iki ayrı "4." soru var) en az iki farklı sınava ait oldukları anlaşılıyor.

### Soru 2: İki op-amp'lı yükselteç tasarımı (20p)

2013 güz ara sınavının 4. sorusuyla aynı: iki ideal op-amp'lı devrede a) A_v = V_L / V₁ ifadesini çıkarınız (12p), b) devreyi A_v = 15 ve |V_o1| = |V_o2| olacak şekilde tasarlayınız (8p).

**Öğrenci çözümü:** Birinci op-amp'ta V₊ = V₋ = V₁ ⇒ A_f1 = v_o1 / v₁ = 1 + R₂/R₁. İkinci op-amp'ta V₋ = V₊ = 0 ⇒ v_o1/R₃ = −v_o2/R₄ ⇒ A_f2 = v_o2 / v_o1 = −R₄/R₃.

A_f = (v_o1 − v_o2) / v₁ = (1 + R₂/R₁)(1 + R₄/R₃)

b) |v_o1| = |v_o2| ve A_f = 15 ⇒ v_o1 − v_o2 = 15 v₁, her biri 7,5 v₁. R₄/R₃ = 1 olmalı (R₃ = R₄ = 10 kΩ); 1 + R₂/R₁ = 7,5 ⇒ R₂/R₁ = 6,5 ⇒ R₂ = 13 kΩ, R₁ = 2 kΩ.

### Soru 3: Faz dedektörü çıkışı için filtre (20p)

Faz dedektörü iki girişindeki sinyali çarpar; çıkışındaki sinyal bu giriş sinyallerinin toplam ve fark frekanslı bileşenlerine sahiptir. Dolayısıyla faz dedektörü çıkışındaki sinyalin sahip olduğu frekans bileşenlerinden biri (f_in + f_osc), diğeri (f_in − f_osc)'dir.

Aşağıdaki devrede:

- Faz dedektörünün girişindeki sinyal V_in(t) = 5 sin 34540t ile V_in(t) = 5 sin 62800t arasında değişmektedir (genliği değişmemekte fakat frekansı bu aralıkta değişim göstermektedir).
- Osilatör ise sabit bir frekansta sinyal üretmektedir ve V_osc(t) = 1 sin 31400t'dir.

Devrenin çıkışından (V_out(t)), faz dedektörü çıkışındaki fark frekanslı sinyal bileşeninin (f_in − f_osc) alınması ve bunların dışındaki frekanslara sahip sinyallerin 1/100 oranında zayıflatılması istendiğine göre, devrede soru işareti ile gösterilen yer için uygun olan devreyi tasarlayınız (π = 3,14 alınız). (20p)

*Blok şema:* V_in(t) → Faz Dedektörü (osilatör çıkışı V_osc(t) ikinci girişte) → (f_in − f_osc), (f_in + f_osc) → [?] → (f_in − f_osc) → V_out(t)

**Puanlanmış çözüm:**

- f_in1 = 34540 / 2π = 5500 Hz, f_in2 = 62800 / 6,28 = 10 000 Hz, f_osc = 31400 / 2π = 5000 Hz
- f_in1 − f_osc = 500 Hz, f_in2 − f_osc = 5000 Hz: 500 Hz – 5000 Hz arası geçmeli, toplam frekanslar (10,5–15 kHz) geçmemeli.
- 20 log(1/100) = −40 dB ⇒ ikinci derece filtre ⇒ ikinci derece bant geçiren filtre tasarımı gerekli.
- YGF (f_YGF = 500 Hz): C₁ = C₂ = C = 5 nF, R₁ = R, R₂ = 2R. 500 Hz = 1 / (2π · 5 nF · √(R₁R₂)) ⇒ R = 1 / (2π · 5 nF · √2 · 500 Hz) = 45,173 kΩ ⇒ R₁ = 45,173 kΩ, R₂ = 90,346 kΩ
- AGF (f_AGF = 5000 Hz): C₄ = C = 1 µF, C₃ = 2C = 2 µF, R₃ = R₄ = R. R = 1 / (2π · 1 µF · √2 · 5000 Hz) ⇒ R₃ = R₄ = 22,5 Ω

### Soru 4: MOSFET yükseltecin yüksek frekans analizi (15p)

2014 Ocak finalinin 1. sorusunun farklı değerlerle sorulmuş hâli: A_vmid = −40; R_D = 40 kΩ, R_S = 2 kΩ, C_gd = 0,5 pF, C_gs = 1 pF, g_m = 1 mS, r_o = r_ds = ∞.

- a) Yüksek frekans ac eşdeğer devresini çiziniz ve kesim frekanslarını bulunuz. (7p)
- b) Devrenin toplam frekans cevabını (Bode plot) çiziniz, üst kesim frekansını belirtiniz. (3p)
- c) Devreye frekansı 1 kHz, genliği 100 mV_pp bir sinyal uygulanırsa çıkıştan alınacak sinyalin genliği V_opp ne olur? (2p)
- d) Devreye frekansı 5 MHz, genliği 100 mV_pp bir sinyal uygulanırsa çıkıştan alınacak sinyalin genliği V_opp ne olur? (3p)

**Puanlanmış öğrenci çözümü:**

- a) C_Mi = 41 · 0,5 pF = 20,5 pF, C_Mo ≅ 0,5 pF; f_giriş = 1 / [2π (C_Mi + C_gs) R_S] = 3,7 MHz, f_çıkış = 1 / [2π C_Mo R_D] = 7,96 MHz
- b) Orta bandda ≅ 32 dB; 3,7 MHz'den sonra −20 dB/dekad, 7,96 MHz'den sonra −40 dB/dekad. f_üst = 3,7 MHz.
- c) 1 kHz orta bandda: A_v = −40 ⇒ V_opp = 40 · 100 mV_pp = 4 V_pp
- d) A_v(5 MHz) = 40 / √(1 + (5/3,7)²) = 23,79 ⇒ V_opp = 23,79 · 100 mV_pp ≅ 2,3 V_pp

### Soru 4: Ortak geçitli yükseltecin yüksek frekans cevabı (15p)

g_m = 2,1 mA/V, C_gs = 15 pF, C_gd = 4 pF, r_o = ∞ parametrelerine sahip bir transistörün kullanıldığı aşağıdaki ortak geçitli (common gate) yükselteç devresinin:

- a) Orta band kazancını (A_vmid) bulunuz. (5p)
- b) Yüksek frekans eşdeğer devresini çizerek dominant üst kesim frekansını bulunuz ve kazancın dB olarak gösterildiği yüksek frekans cevabını çiziniz. (10p)

*Devre:* Kaynak V_i, R_i = 2 kΩ ve C_C1 = 1 µF üzerinden MOSFET'in kaynak ucuna bağlı; kaynak ucu R_S = 10 kΩ ile V⁻ = −5 V'a. Geçit topraklı. Savak R_D = 5 kΩ ile V⁺ = +5 V'a; çıkış C_C2 = 2 µF üzerinden R_L = 4 kΩ'a.

**Bir öğrencinin çözümü:**

- a) A_vmid = V_o / V_gs = g_m (5 k ‖ 4 k) ≅ 4,66
- b) Çıkış kutbu: R_eq = 5 k ‖ 4 k = 2,2 kΩ, C = C_gd = 4 pF ⇒ f = 1 / (2π · 2,2 k · 4 pF) ≅ 18 MHz. Giriş kutbu: R_eq = 2 k ‖ 10 k = 1,66 kΩ, C = C_gs = 15 pF ⇒ f ≅ "63 MHz".

*Not: 1 / (2π · 1,66 kΩ · 15 pF) ≅ 6,4 MHz eder, 63 MHz değil. Ayrıca ortak geçitli devrede kaynak ucundan bakan direnç 1/g_m ≅ 0,48 kΩ'dur ve R_i ‖ R_S ile paralel alınmalıdır: R_eq ≅ 0,37 kΩ ⇒ f_giriş ≅ 28,7 MHz. Bu durumda dominant üst kesim frekansı çıkıştaki ≅ 17,9 MHz'lik kutup olur.*

### Soru 5: Dalga şekli üreten sistem tasarımı (20p)

Giriş sinyali V_in = 20 sin 100πt olan ve ±30 volt DC kaynağa sahip bir sistemden aşağıda ifade edilen iki çıkış sinyali elde edilmek istenmektedir:

- V_out1 = 6 + 5 sin 100πt − 30 sin 100πt
- V_out2 = f = 50 Hz, genliği tepeden tepeye 30 volt ve T_pozitif = T_negatif olan bir kare dalga

İstenen çıkışları verecek sistemi tasarlayınız. Tasarımlarınızdaki tüm hesaplamaları gösteriniz. Kullanacağınız devre ya da elemanların çalışması için gerekli DC gerilimleri, verilen DC kaynakları kullanarak elde ediniz.

**Puanlanmış çözüm:**

- V_in = 20 sin 100πt ⇒ 2πf = 100π ⇒ f = 50 Hz
- (a) Eviren yükselteç, 2 kΩ giriş / 3 kΩ geri besleme: A_v = −3/2 = −1,5 ⇒ V_a = −1,5 · 20 sin 100πt = −30 sin 100πt
- (b) Eviren yükselteç, 8 kΩ giriş / 2 kΩ geri besleme: A_v = −2/8 = −0,25 ⇒ V_b = −0,25 · 20 sin 100πt = −5 sin 100πt
- (c) Eviren yükselteç, 1 kΩ / 1 kΩ: A_v = −1 ⇒ V_c = 5 sin 100πt
- (d) +30 V'tan 4 kΩ – 1 kΩ gerilim bölücü: V_d = 30 · 1k / 5k = 6 V
- Bu gerilimler toplanarak V_out1 elde ediliyor (toplama bağlantısının ayrıntısı fotoğrafta tam seçilemiyor).
- V_out2 için sıfır referanslı karşılaştırıcı: V_in > V_REF = 0 ⇒ V_o = +15 V, V_in < 0 ⇒ V_o = −15 V. Karşılaştırıcının ±15 V beslemesi ±30 V'tan 10 kΩ – 10 kΩ gerilim bölücülerle elde ediliyor. Çıkış 50 Hz, 30 V_pp, T₁ = T₂ olan kare dalga.

### Soru 6: Op-amp'lı gerilim regülatörü (20p)

2014 Ocak finalinin 5. sorusuyla aynı soru (bu sınavda 20 puan; "NOT: İdeal op-amp eşdeğer devresinden yararlanınız." uyarısı eklenmiş): V_Z = 6,3 V, A_OL = 1000, R₁ = 4 kΩ, 10 kΩ – 10 kΩ geri besleme, R_o = 0,5 kΩ, I_ONL = 1 mA, I_OFL = 100 mA için % yük regülasyonu.

**Çözüm (cevap anahtarı):** V₁ = V_o/2; çıkış düğümünden V_o(1002,05) + I_o = 12 600 ⇒ V_o(NL) = 12,5732 V, V_o(FL) = 12,4744 V ⇒ **yük regülasyonu ≅ %0,79**.
