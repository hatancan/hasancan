---
baslik: EEM323 Elektromanyetik II: İletim Hattı Çözümlü Örnekleri (Duran Dalga Oranı, Yük Empedansı, Hat Girişi)
ozet: EEM323 el yazısı çözümlü iletim hattı örnekleri: duran dalga oranı ve ardışık gerilim minimumlarından yansıma katsayısı ile yük empedansı bulma, λ/4 uyumlama; λ/8 hat, giriş empedansı, yük gerilimi ve güç hesabı.
---

Bu yazı, EEM323 Elektromanyetik II dersine ait el yazısı 4 sayfalık **iletim hattı örnekleri** notunun (hazırlayanı ve tarihi belgede yok) metne aktarılmış hâlidir; sayfalar fotoğraflanmış/taranmış kâğıtlardan metne aktarıldı, görseller yayınlanmıyor. Ölçülen Zin değerleri yeniden hesaplanıp doğrulandı.

## Örnek 1: Bilinmeyen yük, duran dalga oranı

**Soru.** Bilinmeyen bir yükle sonlandırılmış kayıpsız 50 Ω'luk iletim hattında duran dalga gerilim oranı 3 ölçülmüştür. Ardışık gerilim minimumları arasındaki mesafe 20 cm, ilk gerilim minimumu yükten 5 cm uzaktadır. (a) Γ yansıma katsayısını, (b) Z_L yük empedansını bulun. (c) Hattın giriş empedansını Z_L yapacak yük direncini ve hat uzunluğunu bulun.

**(a)** İki minimum arası yarım dalga boyudur: λ = 2 × 0,2 = 0,4 m, β = 2π/λ = 5π rad/m. S = 3 olduğundan |Γ| = (S−1)/(S+1) = 2/4 = 1/2. İlk gerilim minimumunda θ_L − 2β·d_min = −π olmalıdır; buradan θ_L = 2 × 5π × 0,05 − π = −0,5π rad. Dolayısıyla Γ = 0,5 e^(−j0,5π) = −j0,5.

**(b)** Z_L = 50 (1 − j0,5)/(1 + j0,5) = 50 (0,60 − j0,80) = **30 − j40 Ω**.

**(c)** İstenen: hattın girişinde Z_in = 30 − j40 görülmesi. Hat, bir gerilim minimumu noktasından itibaren Z₀ = 50 Ω'luk l_m uzunluklu bir hat ve onu sonlandıran R_m direnciyle kurulur:

30 − j40 = 50 (R_m + j50 tan βl_m) / (50 + jR_m tan βl_m)

Yükte gerilim minimumu olduğu kabul edilirse d_min + l_m = λ/2 ve R_m = R₀/S olur: l_m = λ/2 − d_min = 0,2 − 0,05 = **0,15 m**, R_m = 50/3 ≈ **16,7 Ω**.

Yükte gerilim maksimumu olduğu kabul edilirse (d_min + l_m = λ/4 = 0,1): R_m = R₀·S = 50·3 = **150 Ω**, l_m = 0,1 − 0,05 = **0,05 m**. Kontrol: βl_m = 5π × 0,05 = π/4, tan π/4 = 1,

Z_in = 50 (150 + j50)/(50 + j150) = 50 (3 + j)/(1 + j3) = 50 (3 + j)(1 − j3)/10 = 50 (6 − j8)/10 = 30 − j40 Ω.

İstenen değer elde edilir. Çözüm tek değildir: uzunluklara n·λ/2 eklenirse empedans kendini tekrar eder. (Uzunluk sıfır çıkarsa λ/4 + λ/2 alınarak pozitif uzunluk sağlanabilir.)

## Örnek 2: λ/8'lik hat, R ∥ L yük

**Soru.** V_s = 1·cos ωt (ω = 2π × 10⁶ rad/s), iç empedansı Z_s = 100 Ω olan bir kaynak, öz empedansı Z₀ = 100 Ω ve uzunluğu l = λ/8 olan bir iletim hattını besliyor. Hat, paralel R = 100 Ω ve L = 16 µH ile sonlandırılmış. (a) Z_in, (b) V_in, (c) V_L, (d) R'de harcanan güç nedir?

**Çözüm.** jX_L = jωL = j(2π·10⁶)(16·10⁻⁶) ≈ j100 Ω. Yük: Z_L = 100·(j100)/(100 + j100) = 50(1 + j) = 50 + j50 Ω. βl = (2π/λ)(λ/8) = π/4.

**(a)** Z_in = Z₀ (Z_L + jZ₀ tan βl)/(Z₀ + jZ_L tan βl) = 100 [(1+j) + j2] / [2 + j(1+j)] = 100 (1 + j3)/(1 + j) = **100 (2 + j) Ω**.

**(b)** V_in = Z_in/(Z_in + Z_s) · V_s = 100(2+j) / (100(2+j) + 100) ≈ 0,7 + j0,1 = 0,71 e^(j0,14); yani V_in(t) = **0,71 cos(ωt + 0,14)**.

**(c)** Γ_L = (Z_L − Z₀)/(Z_L + Z₀) = (50(1+j) − 100)/(50(1+j) + 100) = −0,2 + j0,4. V_L = V_L⁺(1 + Γ_L) ve V_in = V_L⁺(e^(jβl) + Γ_L e^(−jβl)) olduğundan

V_L = V_in (1 + Γ_L) / (e^(jβl) + Γ_L e^(−jβl)) = (0,7 + j0,1)(0,8 + j0,4) / [(1+j)/√2 + (−0,2 + j0,4)(1−j)/√2] = 0,42 − j0,14 = 0,45 e^(−j0,32)

(e^(−jβl) = e^(−jπ/4) = (1−j)/√2 kullanıldı.) Zamana dönülürse **V_L(t) = 0,45 cos(ωt − 0,32)**.

**(d)** P_d = ½ Re{|V_L|²/Z_L*} = ½ (0,45)² Re{1/(50(1−j))} ≈ **10⁻³ W**. Hat kayıpsız olduğundan aynı güç girişten de bulunur: P_d = ½ Re{|V_in|²/Z_in*} = ½ (0,71)² Re{1/(100(2−j))} ≈ 10⁻³ W.
