---
baslik: EEM214 Elektronik I: 2014 Quiz 2 Soruları ve Final Sınavı Cevap Anahtarı (BJT/MOSFET Yükselteçleri)
ozet: EEM214 Elektronik I dersinin 2013–2014 bahar dönemi Quiz 2 soruları (BJT küçük sinyal kazançları, MOSFET kutuplama, MOSFET yükselteç) ve 29 Mayıs 2014 final sınavının cevap anahtarı: Zener regülatörü, MOSFET kaynak izleyicili iki katlı yükselteç, MOSFET kutuplama tasarımı, kaskat BJT yükselteci ve sistem yaklaşımıyla yükselteç modeli.
---

Bu yazı, EEM214 Elektronik I dersinin **2013–2014 bahar** dönemine ait iki sınav belgesini aktarıyor: 12 Mayıs 2014 tarihli **Quiz 2** soru kâğıdı ve 29 Mayıs 2014 tarihli **yarıyıl sonu (final) sınavının cevap anahtarı**. Metin, telefonla fotoğraflanmış sayfalardan metne aktarıldı; fotoğrafların kendisi yayınlanmadı. Cevap anahtarının ilk sayfası bulanık çekildiği için yalnız okunabilen kısmı yazıldı. Konuların kuramı için arşivdeki [Ders 5 – BJT](/arsiv/eem214-ders-05-bjt/) ve [Ders 6 – FET ve MOSFET](/arsiv/eem214-ders-06-fet/) yazılarına bakılabilir.

## Quiz 2 (12.05.2014)

**1. (45 puan)** Devredeki BJT için β = 80 ve V_A = 150 V. Devrenin AC analizini (küçük sinyal analizi) yaparak gerilim kazancını A_v = v_o/v_s ve akım kazancını A_i = i_o/i_s bulunuz. Devre: V⁺ = +5 V'tan kolektöre I_CQ = 0.5 mA'lik akım kaynağı, emetör V⁻ = −5 V'ta, baz R_B = 10 kΩ ile toprağa ve kuplaj kondansatörü üzerinden v_s'ye bağlı, çıkış kolektörden kuplaj kondansatörüyle R_L = 0.5 kΩ'a alınıyor.

**2. (30 puan)** n kanallı MOSFET: V_TN = 2 V, k_n′ = 80 µA/V², W/L = 4, λ = 0. V_DD = +5 V, R_D = 10 kΩ, R_S = 2 kΩ, kaynak −5 V'a; kapı R1 (V_DD'ye) ve R2 (−5 V'a) bölücüsünden besleniyor. I_D = 0.5 mA olması ve R1–R2 üzerinden geçen kutuplama akımının I_D'nin onda biri olması isteniyor. R1 ve R2'yi ve transistörün çalışma bölgesini bulunuz.

**3. (25 puan)** n kanallı MOSFET'li yükseltecin (+9 V, R_S = 1.2 kΩ ve C_S ile köprülenmiş, R_D = 1 kΩ ile −9 V'a, R_G = 100 kΩ, giriş C_C1 ile) küçük sinyal eşdeğer devresini çizerek giriş direncini R_i, çıkış direncini R_o ve gerilim kazancını A_vs = v_o/v_i bulunuz; g_m = 6.04 mS.

## Final sınavı cevap anahtarı (29.05.2014)

Puan dağılımı: 1. soru 13, 2. soru 32, 3. soru 25, 4. soru 20, 5. soru 13 (toplam 100, bulanık sayfadan okunabildiği kadarıyla).

### 1. Zener'li gerilim düzenleyici

Seri dirençli bir Zener regülatöründe I₁ (seri direnç akımı), I_L (yük akımı) ve I_Z = I₁ − I_L akımları bulunuyor; ikinci kısımda Zener üzerinde harcanan gücün P_Zmax = 400 mW'ı aşmaması için yük direncinin alabileceği en küçük değer, I_Z(max) = P_Zmax / V_Z ve I_L(min) = I₁ − I_Z(max) bağıntılarıyla hesaplanıyor. Fotoğraf bulanık olduğundan sayısal değerler okunamadı.

### 2. İki katlı MOSFET yükselteci

M1 (p kanallı, kaynak izleyici girişli) ve M2 (n kanallı, kaynak izleyici çıkışlı) transistörlü yükselteçte (V⁺ = 5 V, V⁻ = −5 V, R1 = 35 kΩ, R2 = 5 kΩ) I₁ ve I₂ kutuplama akımları DC çıkışı 0 V yapacak değerde. K₁ = 0.2 mA/V², K₂ = 0.5 mA/V², V_T1 = −0.8 V, V_T2 = +0.8 V, r_o1 = 485 kΩ, r_o2 = 100 kΩ, λ = 0.01 V⁻¹.

- a) **I₂ = 5 V / 5 kΩ = 1 mA**; V_GS2 = √(1/0.5) + 0.8 = 2.21 V; **I₁ = (2.21 − (−5))/35 kΩ = 0.206 mA**; g_m2 = 2√(K₂I_D2) = **1.414 mA/V**, g_m1 = 2√(K₁I_D1) = **0.406 mA/V**.
- b) Küçük sinyal eşdeğer devresi: M1 için g_m1·v_gs1 akım kaynağı, r_o1 ve R1 paralel; M2 için g_m2·v_gs2 akım kaynağı, r_o2 ve R2.
- c) V_o = g_m2·v_gs2·(R2 ∥ r_o2), v_gs2 = −(g_m1·v_in)(r_o1 ∥ R1) − V_o ⇒ **A_v = −g_m2(R2 ∥ r_o2)·g_m1(r_o1 ∥ R1) / [1 + g_m2(R2 ∥ r_o2)]**. R2 ∥ r_o2 = 5 ∥ 100 = 4.76 kΩ, R1 ∥ r_o1 = 35 ∥ 485 = 32.6 kΩ ile A_v = −(1.414)(4.76)(0.406)(32.6) / [1 + (1.414)(4.76)] **≅ −11.5**.
- d) **R_o = (1/g_m2) ∥ R2 ∥ r_o2 = 0.707 ∥ 4.76 ≅ 0.616 kΩ**.

### 3. MOSFET kutuplama tasarımı

Transistör doyumda; I_DQ = 6 mA, V_GSQ = 2.8 V, V_DSQ = 10 V, V_DD = 18 V, g_m = 2.2 mS, R_L = 1 kΩ, yüklü kazanç A_v = −1, R_in = 100 kΩ. R1, R2, R_S, R_D = ?

- I_DQ = K_n(V_GSQ − V_TN)², g_m = 2√(K_nI_DQ) ⇒ 2.2 = 2√(6K_n) ⇒ **K_n = 0.202 mA/V²**; 6 = 0.202(2.8 − V_TN)² ⇒ **V_TN = −2.65 V**.
- V_DSQ = 18 − I_DQ(R_S + R_D) ⇒ R_S + R_D = (18 − 10)/6 = 1.33 kΩ.
- A_v = −g_m(R_D ∥ R_L)/(1 + g_m·R_S) = −1 ⇒ 2.2R_D² + 0.47R_D − 3.93 = 0 ⇒ **R_D = 1.23 kΩ, R_S = 0.10 kΩ**.
- V_G = V_GS + V_S = 2.8 + 6 × 0.1 = 3.4 V; V_G = (R_in/R1)·V_DD ⇒ **R1 = 100 × 18 / 3.4 ≅ 529 kΩ**; 529·R2/(529 + R2) = 100 ⇒ **R2 ≅ 123 kΩ**.

### 4. Kaskat bağlı BJT yükselteci

Q1 (npn, R1 = 100 kΩ, R2 = 50 kΩ, R_C1 = 5 kΩ, R_E1 = 2 kΩ köprülü) ve Q2 (pnp, R_E2 = 2 kΩ köprülü, R_C2 = 1.5 kΩ), V± = ±5 V, R_S = 0.5 kΩ, R_L = 5 kΩ; β₁ ≠ β₂, r_e1 ≠ r_e2, g_m1 ≠ g_m2, r_o1 ≠ r_o2 (r_o dikkate alınacak).

- a) Küçük sinyal eşdeğer devresi: R_S, R1 ∥ R2, β₁r_e1; β₁I_b1 akım kaynağı, R_C1, r_o1, β₂r_e2; β₂I_b2 akım kaynağı, r_o2, R_C2, R_L.
- b) A_vs = [R_i/(R_i + R_s)] · [−(R_C1 ∥ r_o1 ∥ β₂r_e2)·β₁I_b1 / (β₁r_e1·I_b1)] · [(r_o2 ∥ R_C2 ∥ R_L)·β₂I_b2 / (−I_b2·β₂r_e2)]; değerlerle **A_vs = [(33.33k ∥ β₁r_e1) / (0.5k + 33.33k ∥ β₁r_e1)] · [(5k ∥ r_o1 ∥ β₂r_e2)/r_e1] · [(r_o2 ∥ 1.15k)/r_e2]** (100k ∥ 50k = 33.33 kΩ, 1.5k ∥ 5k ≅ 1.15 kΩ).

### 5. Sistem yaklaşımıyla yükselteç modeli

Yükseltecin girişine V_s = 0.1 V (R_s = 5 kΩ üzerinden) uygulandığında V_i = 80 mV ölçülüyor; R_L = 5 kΩ bağlıyken V_o = 5 V, yük çıkarılınca V_o = 8 V. Giriş ve çıkış dirençleri ile yüksüz kazanç?

- 80 mV = 100 mV·R_i/(5k + R_i) ⇒ **R_i = 20 kΩ**.
- Yüksüz kazanç **A_vo = 8 V / 80 mV = 100**; yüksüz toplam kazanç A_vs = 8 V / 100 mV = 80.
- Yüklü kazanç 5/0.08 = 62.5 = 100 × 5k/(R_o + 5k) ⇒ **R_o = 3 kΩ**.
- Eşdeğer devre: girişte 20 kΩ, çıkışta 100·v_i bağımlı gerilim kaynağı ve seri 3 kΩ.
