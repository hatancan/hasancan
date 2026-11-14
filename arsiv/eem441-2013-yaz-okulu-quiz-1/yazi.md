---
baslik: EEM441 Haberleşme I: 2013 yaz okulu Quiz I (23 Temmuz 2013) ve çözümleri
ozet: Faz ayırma yöntemiyle USSB sinyali için en büyük taşıyıcı frekansı ve dengesiz genlik modülatörlerinin çıkış ifadesi; el yazısı çözümlerle.
---

Başkent Üniversitesi EEM 441 Haberleşme I yaz okulu Quiz I (23 Temmuz 2013, süre 1 saat) sorularının ve el yazısı çözümlerinin metne aktarımı. Sınav kâğıdı ve çözümler fotoğraflanmış sayfalardan metne aktarıldı; fotoğraflar yayınlanmamıştır. Bu nedenle indirilebilir orijinal dosya yoktur. Kişisel bilgiler (öğrenci numarası, ad) çıkarılmıştır. Aynı klasörde bulunan, bir ders kitabına ait çözüm sayfası fotoğrafı yayınlanmamıştır.

## Sorular

1. Birinci BPF'nin alt kesim frekansı f₁ ve ikinci BPF'nin alt kesim frekansı f₂ olan, f_c = f₁ + f₂ taşıyıcılı USSB sinyali için faz ayırma yönteminin kullanıldığını varsayın. x(t), 200 Hz < |f| < 3200 Hz dışında ihmal edilebilir frekans bileşenine sahip ses sinyalini göstermektedir. BPF'nin 2β ≥ 0,01 f_LO geçiş bölgesine sahip olması durumunda f_c'nin en büyük değerini hesaplayın. Gerekli grafikleri çizerek spektrum üzerinde hesaplayın.
2. Şekildeki genlik modülatörleri dengesiz olduğunda bir eğrisel eleman V_out = a₁V_in + a₂V_in² + a₃V_in³ iken diğeri V_out = b₁V_in + b₂V_in² + b₃V_in³ olmaktadır. Bu durumda çıkış sinyalini hesaplayın. (Şekiller: dengeli modülatör — girişleri +½x(t) ve −½x(t) olan iki AM modülatör, taşıyıcı A_c cos ω_c t, çıkışlar toplayıcıda çıkarılır; AM modülatör — ½x(t) ile A_c cos ω_c t toplanıp doğrusal olmayan elemandan ve BPF'den geçirilir.)

## Çözüm 1

Sistem: x(t) → karıştırıcı (f₁) → BPF₁ → karıştırıcı (f₂) → BPF₂ → s(t), f_c = f₁ + f₂. Ses spektrumu f_ℓ = 200 Hz ile f_m = 3200 Hz arasındadır.

BPF₁: iki yan bant arasındaki boşluk 2f_ℓ = 400 Hz olduğundan geçiş bölgesi 2β = 400 Hz'dir. Koşul 2β ≥ 0,01 f₁ olduğundan 400 ≥ 0,01 f₁ ve f₁ ≤ 40 kHz.

BPF₂: ilk karıştırıcı çıkışında yan bantlar arası boşluk 2f₁ + 400 Hz'dir; 2f₁ + 400 ≥ 0,01 f₂ olur. En büyük f₁ = 40 kHz için f₂ ≤ 100(2f₁ + 400) = 100 × 80,4 kHz = 8,04 MHz.

Sonuç: f_c = f₁ + f₂ < 8,08 MHz (f_c,max ≈ 8,08 MHz).

## Çözüm 2

V_out+ = a₁(A_c cos ω_c t + ½x) + a₂(A_c cos ω_c t + ½x)² + a₃(A_c cos ω_c t + ½x)³
V_out− = b₁(A_c cos ω_c t − ½x) + b₂(A_c cos ω_c t − ½x)² + b₃(A_c cos ω_c t − ½x)³

Açılımlar: cos²ω_c t = ½ + ½cos 2ω_c t; cos³ω_c t = ¾ cos ω_c t + ¼ cos 3ω_c t. BPF'ler f_c − W < |f| < f_c + W dışını reddeder; x_c(t) = V_out+|BPF − V_out−|BPF olur. Kâğıttaki sonuç:

x_c(t) = (a₁ + ¾a₃ − b₁ − ¾b₃) cos ω_c t + 2(a₂ + b₂) x(t) cos ω_c t + 3(a₃ − b₃) x²(t) cos ω_c t

Sonuç: bastırılmamış taşıyıcı ve (ikinci dereceden terim nedeniyle) bozulma vardır; yani iki eğrisel eleman birbirinin aynı değilse dengeli modülatör taşıyıcıyı tam bastıramaz.

*Not: Kâğıttaki katsayılar A_c çarpanlarını yazmaz. ½x girişiyle yapılan kendi açılımımızda çapraz terimin katsayısı (a₂ + b₂)A_c, x² teriminin katsayısı ¾(a₃ − b₃)A_c ve taşıyıcı teriminin katsayısı (a₁ + ¾a₃A_c² − b₁ − ¾b₃A_c²) çıkar. Sonucun niteliği (bastırılamayan taşıyıcı ve bozulma) değişmez.*
