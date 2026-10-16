---
baslik: EEM311 Elektronik II: 2014 Ocak Final (Yarıyıl Sonu) Sınavı Soruları ve Cevap Anahtarı
ozet: EEM311 Elektronik II dersinin 6 Ocak 2014 tarihli yarıyıl sonu sınavı ve cevap anahtarı: MOSFET yükseltecin Miller etkisiyle yüksek frekans analizi, üç transistörlü seri-şönt geri beslemeli yükselteç, köprü ve enstrümantasyon yükselteci, faz dedektörü için bant geçiren filtre ve op-amp'lı regülatörün yük regülasyonu.
---

Bu yazı, Başkent Üniversitesi Elektrik-Elektronik Mühendisliği **EEM 311 Elektronik II** dersinin **2013-2014 güz yarıyılı yarıyıl sonu (final) sınavını** (06.01.2014) aktarıyor. Kaynak, bir arkadaşın paylaştığı fotoğraflardır: ilk sayfanın üstüne elle "CEVAP ANAHTARI" yazılmış; çözümlerin bir kısmı basılı (İngilizce), bir kısmı el yazısı, yanlarında kırmızıyla puanlar var. Soru 2 için cevap anahtarının yalnız sonucu okunabildiğinden, ara adımlar bir öğrencinin el yazısı çalışmasından alındı. Kişisel bilgiler çıkarıldı. Sorular ve çözümlerin ana adımları fotoğraflanmış sayfalardan metne aktarıldı; fotoğrafların kendisi yayınlanmıyor.

Sınav 120 dakika sürmüş, puan dağılımı şöyle:

| Soru | 1 | 2 | 3 | 4 | 5 | Toplam |
|---|---|---|---|---|---|---|
| Puan | 22 | 28 | 16 | 19 | 15 | 100 |

## Soru 1: MOSFET yükseltecin yüksek frekans analizi (22p)

Aşağıdaki yükseltecin orta band kazancı A_vmid = −40 olarak verilmiştir. Devrenin yüksek frekans analizini yaparak:

- a) Yüksek frekans ac eşdeğer devresini çiziniz ve kesim frekanslarını bulunuz. (12p)
- b) Devrenin toplam frekans cevabını (Bode plot) çiziniz, üst kesim frekansını belirtiniz. (4p)
- c) Devreye frekansı 2 MHz, genliği 10 mV_pp bir sinyal uygulanırsa çıkıştan alınacak sinyalin genliği V_opp ne olur? (2p)
- d) Devreye frekansı 8 MHz, genliği 10 mV_pp bir sinyal uygulanırsa çıkıştan alınacak sinyalin genliği V_opp ne olur? (4p)

R_D = 40 kΩ, R_S = 2 kΩ, C_gd = 0,5 pF, C_gs = 1 pF, g_m = 1 mS, r_o = r_ds = ∞ alınız.

*Devre:* +5 V / −5 V beslemeli ortak kaynaklı n-kanallı MOSFET yükselteç. Kaynak (sinyal) R_S üzerinden geçide bağlı; savak R_D ile +5 V'a, kaynak ucu −5 V'a bağlı; çıkış savaktan alınıyor.

### Çözüm (cevap anahtarı)

Miller teoremiyle C_gd ikiye ayrılır:

C_Mi = (|A_v| + 1) C_gd = 41 · 0,5 pF = 20,5 pF

C_Mo = ((|A_v| + 1) / |A_v|) C_gd = (41/40) · 0,5 pF ≅ 0,5 pF

Giriş kutbu: f_giriş = 1 / [2π (C_Mi + C_gs) R_S] = **3,7 MHz**

Çıkış kutbu: f_çıkış = 1 / [2π C_Mo R_D] = **7,96 MHz**

Eşdeğer devrede girişte R_S, ardından paralel C_gs ve C_Mi; çıkışta g_m·v_gs bağımlı akım kaynağı, C_Mo ve R_D = 40 kΩ var.

**b)** Bode genlik diyagramı: orta band kazancı 20 log 40 ≅ 32 dB; 3,7 MHz'den sonra −20 dB/dekad, 7,96 MHz'den sonra −40 dB/dekad eğimle düşer. Üst kesim frekansı (baskın kutup) **f_H ≅ 3,7 MHz**.

**c)** Anahtarda 2 MHz'in baskın kesim frekansının altında kaldığı, bu yüzden kazancın orta band değerinde alınabileceği yazılmış: V_opp = 40 · V_ipp = **400 mV_pp**.

*Not: Tam hesapla |A_v| = 40 / √(1 + (2/3,7)²) ≅ 35,2 ve V_opp ≅ 352 mV_pp olur; anahtar orta band yaklaşımını kullanıyor.*

**d)** Anahtarda kazanç iki adımda hesaplanmış:

A_v(7,96 MHz) = 40 / √(1 + (7,96/3,7)²)

A_v(8 MHz) = A_v(7,96 MHz) / √(1 + (8/7,96)²)

*Not: Anahtarda sayısal sonuç fotoğrafta görünmüyor; bu ifadeler hesaplanırsa A_v(7,96 MHz) ≅ 16,9, A_v(8 MHz) ≅ 11,9 ve V_opp ≅ 119 mV_pp bulunur.*

## Soru 2: Üç transistörlü geri beslemeli yükselteç (28p)

Aşağıdaki geri beslemeli yükselteç devresinde tüm transistörler için β = 120 ve r_o = ∞ olarak verilmektedir. Ayrıca Q₁, Q₂ ve Q₃ transistörlerinin küçük sinyal parametreleri r_π1 = 3,66 kΩ, r_π2 = 6,28 kΩ, r_π3 = 1,54 kΩ, g_m1 = 32,81 mS, g_m2 = 19,12 mS ve g_m3 = 78,08 mS'dir. Devrenin geri beslemeli küçük sinyal gerilim kazancını bulunuz: A_vf = v_o / v_i. (28p)

(Soru metni fotoğrafta bulanık; r_π değerleri öğrenci çözümünden alındı ve r_π = β/g_m ile tutarlı.)

*Devre:* V_CC = 10 V. Q₁ ortak emetörlü; baz polarması R₁ = 400 kΩ ve R₂ = 75 kΩ, girişi C_C → ∞ üzerinden v_i; kolektör direnci R_C1 = 8,8 kΩ, emetör direnci R_E1 = 0,5 kΩ (köprülenmemiş). Q₂ ortak emetörlü; R_C2 = 13 kΩ, R_E2 = 3,6 kΩ (C_E → ∞ ile köprülü). Q₃ emetör izleyici; emetör direnci R_E3 = 1,4 kΩ, çıkış v_o Q₃'ün emetöründen. Geri besleme direnci R_F = 10 kΩ (seri C_F → ∞ ile) çıkıştan Q₁'in emetörüne bağlı.

### Öğrenci çözümü

Geri besleme türü **seri-şönt** (gerilim örnekleme, seri karışım). Geri besleme devresinin yükleme etkisi için: girişe yansıyan direnç bulunurken çıkış kısa devre edilir, çıkışa yansıyan direnç bulunurken giriş tarafı açık devre edilir:

- R₁₁ = R_E1 ‖ R_F (Q₁'in emetöründe görülen)
- R₂₂ = R_F + R_E1 (çıkışta, R_E3 ile paralel)

Geri beslemesiz (yüklenmiş) kazanç, üç katın kazançlarının çarpımı olarak yazılmış:

A′ = [−β I_b1 (R_C1 ‖ β r_e2) / (I_b1 (β r_e1 + β R₁₁))] · [−β I_b2 (R_C2 ‖ β(r_e3 + R_E3 ‖ R₂₂)) / (I_b2 β r_e2)] · [β I_b3 (R₂₂ ‖ R_E3) / (I_b3 β(r_e3 + R_E3 ‖ R₂₂))]

A′ = (−7,23) · (−228,55) · 0,98

Geri besleme oranı: β_f = R_E1 / (R_E1 + R_F) = 0,5 k / 10,5 k = 1/21

A_vf = A′ / (1 + A′β_f)

Öğrenci çözümü burada "yerine koy" diye bırakılmış: A′ ≅ 1619 olduğundan A_vf = 1619 / (1 + 1619/21) ≅ 20,7 bulunur.

**Cevap anahtarı** (basılı İngilizce çözüm, fotoğrafı çok bulanık): devre transistör modelleriyle çizilip beş düğüm denklemi yazılarak çözülmüş; sonuç **v_o / v_i = 20,73**. Döngü kazancı büyük olduğundan sonuç ideal değer 1/β_f = 21'e çok yakındır.

## Soru 3: Köprü ve enstrümantasyon yükselteci tasarımı (16p)

Aşağıdaki devredeki op-amp'lar ±10 V ile beslenmektedir. Devrede yer alan köprünün çıkış geriliminin ifadesi v_O1 = (δ/4) V⁺ olarak verilmektedir ve δ = 0,01 için devre çıkışında v_O = +5 V olması istenmektedir. Buna göre bilinmeyen direnç değerlerini (R₁, R₂, R₃, R₄) bularak devreyi tasarlayınız. (16p)

*Devre:* Köprünün besleme gerilimi V⁺, V_S = 18 V'tan bir zener diyot (V_Z = 5,6 V, I_Z = 0,25 mA) ile kurulan referansın bir evirmeyen op-amp (200 kΩ ve 67,86 kΩ dirençleri) ile yükseltilmesiyle elde ediliyor. Köprünün üç kolu 200 kΩ, dördüncü kolu 200(1+δ) kΩ. Köprü çıkışı, üç op-amp'lı bir enstrümantasyon yükseltecine (giriş katında R₁ ve R₂, fark katında R₃ ve R₄) uygulanıyor.

### Çözüm (cevap anahtarı)

V⁺ = 5,6 V · (1 + 67,86/200) ≅ 7,5 V'tur. V⁺ = 7,5 V ve δ = 0,01 için köprünün en büyük çıkışı:

v_O1 = (δ/4) V⁺ = 0,01875 V

Yükselteç çıkışının +5 V olması için enstrümantasyon yükseltecinin kazancı 5 / 0,01875 = **266,7** olmalı. Enstrümantasyon yükseltecinin çıkışı:

v_O / v_O1 = (R₄/R₃)(1 + 2R₂/R₁) = 266,7

R₄/R₃ ve R₂/R₁ oranlarının aynı mertebede olması istenir. R₃ = 15,0 kΩ ve R₄ = 187,0 kΩ seçilirse R₄/R₃ = 12,467 ve R₂/R₁ = 10,195 olur. R₂ = 200,0 kΩ seçilirse **R₁ = 19,62 kΩ**.

Kontrol: 12,467 × (1 + 2 × 10,195) = 12,467 × 21,39 ≅ 266,7.

## Soru 4: Faz dedektörü ve RC faz kaydırmalı osilatör (19p)

Faz dedektörü iki girişindeki sinyali çarparak, çıkışında bu sinyallerin toplam ve fark frekanslı bileşenlerine sahip bir sinyal verir. Aşağıdaki devre için faz dedektörü çıkışındaki bu bileşenlerden birinin frekansı (f_in + f_osc), diğerininki (f_in − f_osc)'dir.

Aşağıdaki devrede:

- Faz dedektörünün girişindeki sinyal V_in(t) = 5 sin 37680t'dir.
- Osilatörün ürettiği sinyal ise V_osc(t) = 1 sin 9420t ile 1 sin 32028t arasında değişmektedir (genliği değişmemekte fakat frekansı değişim göstermektedir).

Devrenin çıkışından (V_out(t)), faz dedektörü çıkışındaki fark frekanslı sinyal bileşeninin (f_in − f_osc) alınması ve bunların dışındaki frekanslara sahip sinyallerin −40 dB/decade oranında zayıflatılması istendiğine göre:

- a) Devrede soru işareti ile gösterilen yer için uygun olan devreyi tasarlayınız (π = 3,14 alınız). (15p)
- b) Osilatörün belirtilen aralıkta sinyal üretmesi için R değerinin değişim aralığını bulunuz. (4p)

*Devre:* V_in(t) → Faz Dedektörü → (f_in − f_osc), (f_in + f_osc) → [?] → (f_in − f_osc) → V_out(t). Osilatör, op-amp'lı RC faz kaydırmalı osilatördür: eviren yükseltecin geri beslemesinde 30 kΩ, girişinde üç kademeli C–R ağı (C = 0,1 µF, üç ayarlı R); f_osc = 1 / (2π R C √6).

### Çözüm (cevap anahtarı)

**a)** f_in = 37680 / 2π = 6000 Hz; f_osc1 = 9420 / 2π = 1500 Hz, f_osc2 = 32028 / 2π = 5100 Hz

f_in − f_osc1 = 6000 − 1500 = 4500 Hz, f_in − f_osc2 = 6000 − 5100 = 900 Hz ⇒ 900 Hz – 4500 Hz arası geçmeli: **ikinci derece bant geçiren filtre** (−40 dB/dekad).

- İkinci derece YGF (f_c = 900 Hz): iki 5 nF kapasite, 25 kΩ ve 50 kΩ dirençler
- İkinci derece AGF (f_c = 4500 Hz): iki 5 kΩ direnç, 10 nF ve 5 nF kapasiteler

Kontrol: 1 / (2π · 25 kΩ · 5 nF · √2) ≅ 900 Hz; 1 / (2π · 5 kΩ · 5 nF · √2) ≅ 4500 Hz.

**b)** Fotoğrafta bu şıkkın çözümü görünmüyor.

*Not: f_osc = 1 / (2π R C √6) ve C = 0,1 µF ile, 1500 Hz için R ≅ 433 Ω, 5100 Hz için R ≅ 127 Ω bulunur; R yaklaşık 127 Ω – 433 Ω arasında değişmelidir.*

## Soru 5: Op-amp'lı gerilim regülatörü (15p)

Aşağıdaki gerilim regülatörü devresinde zener diyot ve op-amp'ın ideal olduğu kabul edilmektedir. Zener gerilimi V_Z = 6,3 V, op-amp'ın açık çevrim (open-loop) gerilim kazancı A_OL = V_o/V_d = 1000 olarak verilmektedir (V_d = V₊ − V₋). Devrenin çıkış akımı, devre yüksüzken 1 mA, tam yüklü durumda ise 100 mA olmaktadır. Devrenin % yük regülasyonunu hesaplayınız. (15p)

*Devre:* Zener diyot R₁ = 4 kΩ üzerinden V⁺'dan beslenir ve V_Z'yi op-amp'ın evirmeyen girişine verir. Op-amp eviren girişinden toprağa 10 kΩ, çıkış düğümüne 10 kΩ geri besleme direnci bağlı. Op-amp'ın çıkış direnci R_o = 0,5 kΩ; çıkış V_o, I_o akımını R_L yüküne verir.

### Çözüm (cevap anahtarı)

Op-amp, A_OL(V_Z − V₁) değerli bir bağımlı gerilim kaynağı ve seri R_o ile modellenir.

Eviren giriş düğümü: V₁/10 = (V_o − V₁)/10 ⇒ V₁(1/10 + 1/10) = V_o/10 ⇒ V_o = 2V₁, yani V₁ = V_o/2

Çıkış düğümü: (V_o − V₁)/10 + V_o/R_L + [V_o − A_OL(V_Z − V₁)]/R_o = 0

I_o = V_o/R_L yazılıp V₁ = V_o/2 yerine konunca (akımlar mA, dirençler kΩ):

V_o/20 + I_o + V_o/0,5 − 1000(6,3)/0,5 + 1000 V_o/(2 · 0,5) = 0

V_o(0,05 + 2 + 1000) + I_o = 12 600 ⇒ V_o(1002,05) + I_o = 12 600

- I_o = 1 mA (yüksüz) ⇒ V_o = 12,5732 V
- I_o = 100 mA (tam yük) ⇒ V_o = 12,4744 V

Yük regülasyonu = [V_o(NL) − V_o(FL)] / V_o(FL) × %100 = (12,5732 − 12,4744) / 12,4744 × %100 ⇒ **Yük regülasyonu ≅ %0,79**
