---
baslik: EEM214 Elektronik I: 2006 Ödev Çözümleri, Fazla Taşıyıcı Difüzyonu ve Işıkla Aydınlatılan Yarıiletken Çubuk
ozet: EEM214 Elektronik I dersinin 2006 bahar dönemi ödev çözümlerinin el yazısı kısımları: sürekli enjeksiyonda fazla deliklerin difüzyon denklemi ve δp(x) = Δp·e^(−x/L_p) çözümü; ışık kesildikten sonra fazla taşıyıcıların sönümü, karanlık direnci ve zamana bağlı direnç R(t).
---

Bu yazı, Başkent Üniversitesi **EEM214 Elektronik I** dersinin 2006 bahar dönemine ait Homework I ve Homework II çözüm dosyalarının (parolalı PDF'ler) yalnızca el yazısıyla çözülmüş kısımlarını aktarıyor. Çözüm dosyalarının geri kalanı ve Homework 3 çözümleri ders kitabının (Jaeger, *Microelectronic Circuit Design*) çözüm kılavuzundan alınmış sayfalar olduğu için yayınlanmadı. El yazısı sayfalar dersin asistanı tarafından hazırlanmış görünüyor. Bu üç sayfa yazının sonunda PDF olarak indirilebilir. Aynı dönemin quiz ve ara sınav çözümleri arşivde ayrı yazılarda bulunuyor.

## Homework I – Soru 6: Sürekli enjeksiyonda fazla delikler

**Verilenler:** δp(0) = Δp, enjeksiyon noktasındaki fazla delik yoğunluğu; δp(W) = 0, x = W'deki fazla delik yoğunluğu; τ_p, deliklerin yeniden birleşme ömrü; W >> L_p. İstenen: δp(x).

**Çözüm:** Süreklilik denklemi

∂p(x,t)/∂t = −(1/q)·∂J_p/∂x − δp/τ_p

Delik difüzyon akımı J_p = −q·D_p·∂p/∂x; p = p₀ + δp(x) olduğundan ∂p/∂x = ∂δp(x)/∂x ve J_p = −q·D_p·∂δp(x)/∂x. Böylece

∂p(x,t)/∂t = D_p·∂²δp/∂x² − δp/τ_p

Kararlı durumda sol taraf sıfırdır:

∂²δp/∂x² = δp/(D_p·τ_p) = δp/L_p², L_p = √(D_p·τ_p)

Çözüm δp(x) = C₁·e^(x/L_p) + C₂·e^(−x/L_p) biçimindedir. Sınır koşulları: x = 0'da δp(0) = Δp = C₁ + C₂; x = W'de δp(W) = 0 = C₁·e^(W/L_p) + C₂·e^(−W/L_p). W >> L_p olduğundan e^(−W/L_p) → 0 ve C₁·e^(W/L_p) = 0 olmalı, yani C₁ = 0, C₂ = Δp:

**δp(x) = Δp·e^(−x/L_p)**

Fazla delik yoğunluğu enjeksiyon noktasından üstel olarak azalır; x = L_p'de Δp·0.3679 değerine iner. Burada L_p deliklerin **ortalama difüzyon uzunluğudur**.

## Homework II – Soru 5: Işıkla aydınlatılan yarıiletken çubuk

**a)** Çubuk düzgün aydınlatıldığından ∂J_p/∂x = 0: difüzyon akımı yoktur; elektrik alan sıfır olduğundan sürüklenme akımı da yoktur. Süreklilik denklemi

∂δp(t)/∂t = −δp(t)/τ_p ⇒ δp(t) = δp(0)·e^(−t/τ_p)

ve δp(0) = Δp ile **δp(t) = Δp·e^(−t/τ_p)** (cm⁻³).

**b)** İletkenlik σ = q(n·µ_n + p·µ_p). t = 5τ_p'de δp(t) neredeyse sıfıra iner ve ihmal edilebilir; bu durumda σ = q(n₀µ_n + p₀µ_p), ρ = 1/σ. n₀ ≅ N_D ve p₀ = n_i²/N_D olduğundan karanlık direnci

R_dark = ρL/(w·d) = L / [q·w·d·(N_D·µ_n + (n_i²/N_D)·µ_p)]

**c)** Zamana bağlı direnç R(t) = ρL/(w·d) = L / [q(n·µ_n + p·µ_p)·w·d]; burada n = n₀ + δn, p = p₀ + δp, Δp = Δn ve τ_p = τ_n alınarak n = N_D + Δp·e^(−t/τ_p), p = n_i²/N_D + Δp·e^(−t/τ_p) ve

**R(t) = L / {q·w·d·[(N_D + Δp·e^(−t/τ_p))·µ_n + (n_i²/N_D + Δp·e^(−t/τ_p))·µ_p]}**

## İndirme

PDF dosyası Homework I'in iki ve Homework II'nin bir el yazısı çözüm sayfasını içeriyor (kitap çözüm kılavuzundan alınan kısımlar çıkarıldı).
