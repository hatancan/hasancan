---
baslik: EEM441 Haberleşme I: AM, SSB ve FM çözümlü çalışma soruları
ozet: EEM441 Haberleşme I için el yazısıyla çözülmüş AM demodülasyonu, karesel eleman, zarf algılama, SSB ve FM çarpıcı zinciri çalışma soruları, metne aktarılmış hâlde.
---

EEM 441 Haberleşme I için hazırlanmış, el yazısıyla çözülmüş AM, SSB ve FM çalışma soruları. Kaynak, tarayıcıyla taranmış sayfalardır (soru metinleri ve çözümler bir öğrencinin el yazısıdır); sayfalar yayınlanmayıp içerik metne aktarıldı. Çözümler kaynakta bulunduğu biçimde özetlenmiştir. Kişisel bilgi içermez.

## 1. Çarpıcı bindirici ve genlik bindirimli im (Quiz 1)

f(t) = 12cos(2π·3×10³t) V mesajıyla %80 bindirimli GB im için taşıyıcı genliği A_c = A_m/m = 12/0,8 = 15 V'tur. A_c < 12 V olursa m > 1 olur: aşırı bindirim; evre tersliği ve zarf bozukluğu oluşur. f_c = 30 kHz için f_GB(t) = 15cos(2π·30k·t) + 6cos(2π·27k·t) + 6cos(2π·33k·t), bant genişliği 6 kHz; 50 Ω'da taşıyıcı gücü 2,25 W, toplam yan bant gücü 0,72 W. (Aynı soru Temmuz 2009 quizinde de çıkmıştır; sayfanın üstündeki "bize Quiz 3'te aktı" notu bu sorunun sonradan başka bir sınavda yinelendiğini gösterir.)

*Not: Taranmış çözümde de yan bant genliği 72 V ve güç 103,68–109,68 W bulunmuştur; bu, m·f(t) çarpımında mesajın normalleştirilmemesinden kaynaklanan bir hatadır.*

## 2. Girişim taşıyıcılı AM demodülatörü

AM işareti A_c[1 + μx(t)]cos ω_ct, istenmeyen girişim taşıyıcısı x_i(t) = A_i cos(ω_c + Δω)t ile toplanıp cos(ω_ct + φ) ile çarpılır ve alçak geçiren süzgeçten (ω_c bandı) geçirilir (Δf < W). Çıkış:

V_o(t) = (A_c/2)[1 + μx(t)]cos φ + (A_i/2)cos(Δωt − φ).

Mesajı bozulmadan elde etmek için φ ≠ ±π/2 (cos φ ≠ 0) ve Δω = 0 olmalıdır; bu durumda V_o = (A_c/2)(1 + μx)cos φ ve girişim bileşeni sabit bir DC terimine dönüşür.

## 3. Süzgeç ve cos 4πt ile çarpma

s(t), H(f) süzgecinden (H = 3, |f| ≤ 2 Hz; aksi hâlde 0) geçer, ardından cos 4πt ile çarpılır; S(f) üçgendir (tepe 4, |f| ≤ 4 Hz). W(f) = S(f)H(f) ve r(t) = w(t)cos 4πt için R(f) = ½W(f − 2) + ½W(f + 2): −2…2 Hz aralığındaki W(f)'nin ±2 Hz'e kayan iki yarı genlikli kopyasının toplamı, −4…4 Hz aralığında yer alır.

## 4. Kare alıcı – alçak geçiren süzgeç – karekök alıcı

s(t) = A_c[1 + k_am(t)]cos 2πf_ct, |k_am(t)| < 1, f_c > 2W. V₁ = s² = A_c²[1 + k_am]²cos²(2πf_ct) = (A_c²/2)[1 + 2k_am + k_a²m²][1 + cos 4πf_ct]. Alçak geçiren süzgeç 4πf_ct bileşenini atar: V₂ = (A_c²/2)[1 + k_am(t)]². Karekökten V₃ = (A_c/√2)[1 + k_am(t)] elde edilir, yani m(t) geri kazanılır.

## 5. Zarf algılayıcı ve taşıyıcılı SSB (2003 ara sınav sorusu)

s(t) = A_c cos 2πf_ct + m(t)cos 2πf_ct − m̂(t)sin 2πf_ct, taşıyıcılı bir SSB sinyalidir. Zarf: a(t) = √([A_c + m(t)]² + m̂²(t)) = √(A_c² + 2A_cm(t) + m²(t) + m̂²(t)). A_c ≫ |m(t)| olduğunda a(t) ≈ A_c + m(t); zarf algılayıcı iyi bir yaklaşıklıkla mesajı verir (A_c büyüdükçe bozulma azalır).

## 6. Karesel eleman: y = 6x + 4x²

x(t) = m(t) + cos ω_ct (m'in ortalaması sıfır, x(t)'nin en küçük değeri M); y(t) = 6x(t) + 4x²(t) = 2 + 6m + 4m² + 6cos ω_ct + 8m cos ω_ct + 2cos 2ω_ct. a) İzge: 2δ(f), 6M(f), 4M(f)*M(f) (alçak frekans), 3δ(f ∓ f_c) ve 4M(f ∓ f_c) (f_c çevresi), δ(f ∓ 2f_c). b) AM için f_c'de merkezli, bant genişliği > 2W olan BPF gerekir; f_c − W > 2W, yani f_c > 3W olmalıdır. c) g(t) = 6cos ω_ct + 8m(t)cos ω_ct = 6[1 + (4/3)m(t)]cos ω_ct; bindirim göstergesi μ = (4/3)·max|m|, max x = 1 + max m = M ⇒ μ = 0,1 için M = 1,075 (soru verisinden hesaplandı).

## 7. FM çarpıcı zinciri

A_c = 50 V, A_m = 20 V, K = 2356, ω_c = 2π·200 kHz, ω_m = 2π·15 kHz için β = KA_m/ω_m = 0,5: f₁(t) = 50cos(2π·200·10³t + 0,5 sin(2π·15·10³t)) dar bant FM'dir (B = 2f_m = 30 kHz). Zincir ×64 → karıştırıcı (f₀ = 20cos(2π·10 900·10³t)) → BGS (1885–1915 kHz) → ×48: f₅(t) = 100cos(2π·91 200·10³t + 1536 sin(2π·15·10³t)), 50 Ω'da en büyük güç 100²/(4·50) = 50 W. Ayrıntılı çözüm için bkz. 2014 Quiz 2 yazısı.

## 8. Taşıyıcılı SSB (300 kHz, A_c = 100)

x(t) = cos 2000πt + 2sin 2000πt ile 300 kHz taşıyıcıyı (A_c = 100) modülleyen SSB için: a) x̂(t) = sin 2000πt − 2cos 2000πt. b) SSB: x_c(t) = (A_c/2)[x(t)cos 2πf_ct ± x̂(t)sin 2πf_ct]; alt yan band için x_c(t) = (A_c/2)[cos(ω_c − ω_m)t − 2 sin(ω_c − ω_m)t]. c) İzge: X_c(f) = (A_c/4)[(1 + j2)δ(f − f_c + f_m) + (1 − j2)δ(f + f_c − f_m)]; çizgi büyüklüğü (A_c/4)√5 ≈ 55,9, f_c − f_m = 299 kHz'de.

*Not: Çalışma kâğıdının son sayfaları eksik olduğundan 8. soru yalnız yukarıdaki kadarıyla aktarılabildi.*
