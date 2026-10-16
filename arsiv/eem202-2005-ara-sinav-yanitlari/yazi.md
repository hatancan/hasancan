---
baslik: EEM202 Devre Teorisi II: 2004-2005 Bahar Ara Sınavı Soruları ve Yanıtları
ozet: EEM202 Devre Teorisi II dersinin 2004-2005 bahar ara sınavı ve hocaların yanıt anahtarı: ideal trafolu devrede maksimum güç için Thevenin eşdeğeri, iletim hattında güç ve güç kompanzasyonu, Y-Δ üç fazlı sistem, karşılıklı endüktanslı devrede süperpozisyon.
---

Bu yazı, Başkent Üniversitesi Elektrik-Elektronik Mühendisliği **EEM 202 Devre Teorisi-II** dersinin **2004-2005 Bahar dönemi ara sınavının (midterm)** soru kâğıtlarını ve "YANITLAR" başlıklı cevap anahtarını içeriyor. Sınavı hazırlayanlar Prof. Dr. Turhan Çiftçibaşı ve Öğr. Gör. Mustafa Doğan. Arşivdeki belgeler, kâğıtların fotoğrafları; her sorunun altında soru metni ve yanıt anahtarındaki ana sonuçlar yazıya döküldü. Puanlama: Soru 1 ve 2 yirmişer, Soru 3 ve 4 otuzar puan (toplam 100). Fotoğrafların kendisi arşivde saklanıyor, yayınlanmıyor.

## Soru 1: Thevenin eşdeğeri ve ideal trafo ile maksimum güç (20 puan)

Aşağıdaki kuvvetlendirici devresinin a-b uçlarından görülen **Thévenin** eşdeğerini bulunuz. Bu eşdeğer devrenin çıkışına şekildeki gibi bir **ideal transformatör** bağlandığında Z_y ne olmalıdır ki kuvvetlendirici devresinden **maksimum güç** çekilebilsin? V_s(t) = 10 cos(10000t + 53.13°) olarak verilmiştir. (cos 53.13° ≅ 0.6 ve sin 53.13° ≅ 0.8 olarak alınız.)

Devrede 200 µH bobin, 25 µF kapasitör, 2 Ω direnç, (3/2)i bağımlı akım kaynağı ve 1:5 oranlı ideal trafo var.

- V_s = 10e^(j53.13°) = 10(0.6 + j0.8) = **6 + j8**; bobin j2 Ω, kapasitör −j4 Ω
- V_oc için d düğümünde düğüm denklemi (V_d = V_oc): V_oc/(−j4) + (V_oc − V_s)/(j2) − (3/2)[(V_oc − V_s)/(j2)] = 0 → **V_oc = 3 + j4 = 5e^(j53.13°) V**
- I_sc için (devrede bağımlı kaynak olduğundan): V_d/2 + V_d/(−j4) + (V_d − V_s)/(j2) − (3/2)[(V_d − V_s)/(j2)] = 0 → V_d = (3 + j4)/(1 − j), I_sc = V_d/2 = (3 + j4)/(2 − j2)
- **Z_th = V_oc/I_sc = 2 − j2 Ω**
- Maksimum güç aktarımı için: Z_y′ = Z_th* = 2 + j2 = (1/5)²·Z_y → **Z_y = 50 + j50 Ω**

## Soru 2: İletim hattı ve güç kompanzasyonu (20 puan)

Aşağıdaki devre için (f = 60 Hz, 465 V-rms jeneratör, Z_hat = 4 + j3 Ω, Z_yük = 120 + j90 Ω):

1. Çıkış gerilimini (V_yük), iletim hattı akımını (I_hat) ve ilgili karmaşık güçleri (S_hat, S_yük) bulunuz.
1. Yükteki faz açısını sıfırlamak (güç kompanzasyonu) için yüke paralel bağlanması gereken kapasitans değerini bulunuz, C = ? (İpucu: Z′_yük = Z_C ∥ Z_yük; burada kapasitör dahil edildiğinde Z′_yük'ün reel bir sayı olması gerekir.)
1. Bulunan kapasitör bağlandığında yeni yük empedansını (Z′_yük), buna göre iletim hattı akımını (I′_hat) ve çıkış gerilimini (V′_yük) yeniden bulunuz.

a)

- V_yük = (120 + j90)/(124 + j93)·465 = 150e^(j36.9°)/155e^(j36.9°)·465 = **450 V-rms**
- I_hat = 465/155e^(j36.9°) = **3e^(−j36.9°) A-rms**
- S_hat = |I_hat|²·Z_hat = 3²(4 + j3) = **36 + j27 VA**
- S_yük = V_yük·I_hat* = 450·3e^(j36.9°) = 1350e^(j36.9°) = **1080 + j810 VA**

b) Z′_yük = Z_C ∥ Z_yük, Y′_yük = Y_C + Y_yük. Z′_yük ve Y′_yük reel olduğundan |Y_C| = |Im{Y_yük}| olmalı:

- Y_yük = 1/(120 + j90) = 1/(30(4 + j3)) = (4 − j3)/750 = 4/750 − j·3/750
- 2πfC = |Im{Y_yük}| = 3/750 → C = 3/(750·2π·60) → **C = 10.61 µF**

c)

- Z′_yük = 1/Y′_yük = 750/4 = **187.5 Ω**
- I′_hat = 465/(191.5 + j3) = 465/191.5e^(j0.9°) = **2.43e^(−j0.9°) A-rms**
- V′_yük = I′_hat·Z′_yük = 2.43e^(−j0.9°)·187.5 = **455.6e^(−j0.9°) V**

*Not: 465·187.5/191.52 ≈ 455.3 V çıkıyor; yanıttaki 455.6 V, akımın 2.43'e yuvarlanmasından kaynaklanan küçük bir farktır.*

## Soru 3: Y-Δ üç fazlı sistem (30 puan)

Aşağıdaki 3 fazlı, + sıralı (positive sequence), Y (yıldız) bağlantılı jeneratör (source), iletim hattı üzerinden Δ (üçgen) bağlantılı dengeli (balanced) yüke bağlanmıştır. Tek faz eşdeğerinde V_a = 120 V-rms, Z_hat = 0.5 + j1.4 Ω.

1. Dengeli Δ (üçgen) yükün Y (yıldız) eşdeğerini bulunuz, Z_Y = ?
1. Hat akımlarını bulunuz (I_aA, I_bB, I_cC).
1. Yük üzerindeki faz gerilim (V_AB, V_BC, V_CA) ve akımlarını (I_AB, I_BC, I_CA) bulunuz (önce V_AN bulunacaktır).
1. Jeneratördeki hat gerilimlerini (V_ab, V_bc, V_ca) bulunuz (önce V_an bulunacaktır).
1. Yük tarafından harcanan toplam gerçek gücü (P_T) bulunuz.

- a) Z_Y = Z_Δ/3 = **39.5 + j28.6 = 48.77e^(j35.91°) Ω**
- b) I_aA = 120/(Z_hat + Z_Y) = 120/(40 + j30) = **2.4e^(−j36.87°) A-rms**; I_bB = 2.4e^(−j156.87°), I_cC = 2.4e^(j83.13°) A-rms
- c) V_AN = I_aA·Z_Y = 2.4e^(−j36.87°)(39.5 + j28.6) = **117.04e^(−j0.96°) V-rms**
- V_AB = √3e^(j30°)·V_AN = **202.72e^(j29.04°) V-rms**, V_BC = 202.72e^(−j90.96°), V_CA = 202.72e^(j149.04°) V-rms
- I_AB = (1/√3)e^(j30°)·I_aA = **1.39e^(−j6.87°) A-rms**, I_BC = 1.39e^(−j126.87°), I_CA = 1.39e^(j113.13°) A-rms
- Doğrulama: I_AB = V_AB/Z_Δ = 202.72e^(j29.04°)/(118.5 + j85.8) = 202.72e^(j29.04°)/146.3e^(j35.91°) = 1.39e^(−j6.87°) bulunur.

- d) V_an = 120 V-rms; V_ab = √3e^(j30°)·V_an = 120√3e^(j30°) = **207.85e^(j30°)**, V_bc = 207.85e^(−j90°), V_ca = 207.85e^(j150°)
- e) Yük için S_T = P_T + jQ_T ve Q_T = P_T·tan θ (θ = θ_VAN − θ_IaA)
- P_T = 3|V_AN||I_aA| cos(θ_VAN − θ_IaA) = 3·117.04·2.4·cos(−0.96° + 36.87°) = 3·117.04·2.4·cos(35.91°)
- **P_T = 682.53 W**, Q = P_T·tan(35.91°) = 494.25 VAR → **S = (682.53 + j494.25) VA**

## Soru 4: Süperpozisyon (30 puan)

Aşağıdaki devrede kapasitör üstüne düşen gerilimin anlık değerini (V_c(t)) süperpozisyon yöntemiyle bulunuz. Devrede 5 cos(2t) ve 3 sin(0.5t) kaynakları, 0.5 F kapasitör, 4 H ve 6 H bobinler ve aralarında 2 H karşılıklı endüktans var.

ω = 2 için (kapasitör −j Ω, bobinler j8 ve j12 Ω, karşılıklı endüktans j4 Ω):

- V_L1 = j8(I₁ − I₂) − j4I₂, V_L2 = j12I₂ − j4(I₁ − I₂)
- Göz 1: −5 + (−j)I₁ + V_L1 = 0; göz 2: −V_L1 + V_L2 = 0 → I₂ = (3/7)I₁
- I₁ = −j(35/13), I₂ = −j(15/13)
- V_C1 = (−j)·I₁ = −35/13 → **v_C1(t) = (35/13) cos(2t + 180°)**

ω = 0.5 için (kapasitör −j4 Ω, bobinler j2 ve j3 Ω, karşılıklı endüktans j1 Ω):

- V_L1 = j2(I₁ − I₂) − jI₂, V_L2 = j3I₂ − j(I₁ − I₂)
- Göz 1: (−j4)I₁ + V_L1 = 0 → I₂ = −(2/3)I₁; göz 2: −V_L1 + V_L2 − 3j = 0
- I₁ = −9/23, I₂ = 6/23
- V_C2 = (−j4)I₁ = j(36/23) = (36/23)e^(j90°) → **v_C2(t) = (36/23) cos(0.5t + 90°)**

Sonuç:

**V_c(t) = v_C1(t) + v_C2(t) = (35/13) cos(2t + 180°) + (36/23) cos(0.5t + 90°)**
