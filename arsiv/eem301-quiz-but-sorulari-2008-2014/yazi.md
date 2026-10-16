---
baslik: EEM301 Sinyaller ve Sistemler I: 2008–2016 Kısa Sınav, Bütünleme ve Sınav Sorusu Çözümleri
ozet: EEM301 Sinyaller ve Sistemler I dersinin 2008 tahtaya yazılmış quiz soruları, 2013–2014 Kısa Sınav 1 ve 2, 27.01.2014 bütünleme sınavı ve Ocak 2016 tarihli iki sınav sorusunun çözümleri: konvolüsyon, q- ve p-operatörü, Fourier serisi, frekans yanıtı ve Fourier dönüşümü.
---

Bu yazı, Başkent Üniversitesi **EEM301 Sinyaller ve Sistemler I** dersinin farklı yıllarına ait kısa sınav ve bütünleme sorularını bir araya getiriyor: 2008 güzünde tahtaya yazılmış iki quiz, 2013–2014 güz dönemi Kısa Sınav 1 ve 2 (Prof. Dr. Alper Uraz) , 27 Ocak 2014 bütünleme sınavı ve Ocak 2016 tarihli iki Fourier dönüşümü sorusunun çözümü. Sorular ve çözümler fotoğraflanmış sayfalardan (tahta, sınav kâğıdı ve çözüm kâğıtları) metne aktarıldı; fotoğraflar yayınlanmadı, bu yüzden indirilebilir dosya yok. Öğrenci kâğıtlarındaki kişisel bilgiler aktarılmadı.

## Quiz 2 (13 Kasım 2008)

Tahtaya yazılan soru:

- x[n] = u[n + 10] − 2u[n] + u[n − 4], h[n] = u[n − 2]
- y[n] = x[n] ∗ h[n] = ?

*Not: Tahtadaki soruyla birlikte çözüm yazılmamış. h[n] = u[n − 2] olduğundan y[n] = Σ_{k=−∞}^{n−2} x[k], yani x'in n − 2'ye kadarki birikimli toplamıdır: n < −8 için 0, −8 ≤ n ≤ 1 için n + 9, 2 ≤ n ≤ 5 için 10 − (n − 1) = 11 − n, n ≥ 6 için 6.*

## Quiz 3 (4 Aralık 2008)

1. Sürekli zamanlı nedensel LTI sistem dy(t)/dt + 4y(t) = x(t). x(t) = cos 2πt için y(t) = ? (İpucu: y(t) = Σ a_k H(jkω₀) e^(jkω₀t).)
1. T = 1/2 periyotlu x(t) = cos 4πt, y(t) = sin 4πt ve z(t) = x(t)y(t) sinyalleri için: (a) x(t) ⟷ a_k = ?, (b) y(t) ⟷ b_k = ?, (c) çarpım özelliğini kullanarak z(t) ⟷ c_k = ?

*Not: Tahtada çözüm yok. 1. soruda H(jω) = 1/(jω + 4) ve a₁ = a₋₁ = 1/2 olduğundan y(t) = |H(j2π)| cos(2πt + ∠H(j2π)) = cos(2πt − tan⁻¹(π/2)) / √(16 + 4π²) olur. 2. soruda a₁ = a₋₁ = 1/2, b₁ = 1/(2j), b₋₁ = −1/(2j); c_k = Σ a_l b_(k−l) ⇒ c₂ = 1/(4j), c₋₂ = −1/(4j), diğerleri 0 (z(t) = ½ sin 8πt).*

## 2013–2014 Kısa Sınav 1 (25.10.2013)

q-operatörü yaklaşımını kullanarak y(n + 2) − 5y(n + 1) + 6y(n) = 15(0.5)ⁿ denkleminin tümleyen, özel ve tam çözümlerini y(0) = 1, y(1) = 0 başlangıç değerleri için elde ediniz.

**Çözüm (cevap anahtarı):**

- D(q) = q² − 5q + 6 = (q − 2)(q − 3) = 0 ⇒ q₁ = 2, q₂ = 3
- Tümleyen çözüm: y_c(n) = A(2)ⁿ + B(3)ⁿ
- Özel çözüm: y_p(n) = 1/D(q)|_(q=0.5) × 15(0.5)ⁿ = (1/3.75) × 15(0.5)ⁿ = 4(0.5)ⁿ
- Tam çözüm: y(n) = A(2)ⁿ + B(3)ⁿ + 4(0.5)ⁿ; y(0) = A + B + 4 = 1, y(1) = 2A + 3B + 2 = 0 ⇒ A = −7, B = 4
- **y(n) = −7(2)ⁿ + 4(3)ⁿ + 4(0.5)ⁿ**

## 2013–2014 Kısa Sınav 2 (08.11.2013)

Bir LTI sistem y″(t) + 3y′(t) + 2y(t) = 5x′(t) + 2x(t) olarak tanımlanmaktadır. Dürtü (impulse) yanıtı h(t)'yi elde ediniz.

**Çözüm (cevap anahtarı):**

- (p² + 3p + 2)z(t) = δ(t), y(t) = (5p + 2)z(t); kökler p₁,₂ = −1, −2; z′(0) = 1, z(0) = 0
- z_c(t) = Ae^(−t) + Be^(−2t); A + B = 0, −A − 2B = 1 ⇒ A = 1, B = −1 ⇒ z(t) = e^(−t) − e^(−2t)
- h(t) = 5z′(t) + 2z(t) = 5[−e^(−t) + 2e^(−2t)] + 2e^(−t) − 2e^(−2t) = **−3e^(−t) + 8e^(−2t)** (t ≥ 0)

## 2013–2014 Bütünleme Sınavı (27.01.2014)

100 dakika, her soru 10 puan.

### Soru 1

x(t) = u(t + 1) − u(t − 1), h(t) = δ(t) + δ(t − 1) + δ(t + 1) için y(t) = x(t) ∗ h(t)'yi hesaplayıp ara adımlarla çiziniz.

**Çözüm:** y(t) = x(t) + x(t − 1) + x(t + 1). Üç dikdörtgen üst üste toplanınca basamaklı bir sinyal çıkar: −2 < t < −1'de 1, −1 < t < 1'de 2, 1 < t < 2'de 1, diğer yerlerde 0.

### Soru 2

Periyodu T = 2 olan x(t) (0 ≤ t ≤ 1'de t, 1 ≤ t ≤ 2'de 2 − t; üçgen dalga) ve g(t) = dx(t)/dt (±1 arasında kare dalga). x(t) ⟷ a_k ve g(t) ⟷ b_k. a₀'ı doğrudan bulun; sonra b_k'yı bulup FS özelliklerinden kalan a_k'ları elde edin.

**Çözüm:**

- a₀ = ½∫₀² x(t) dt = 1/2
- b₀ = 0; b_k = (1/2)[∫₀¹ e^(−jπkt) dt − ∫₁² e^(−jπkt) dt] = (1 − e^(−jπk))²/(2jπk): tek k için 2/(jπk), çift k için 0
- g(t) = dx/dt ⇒ b_k = jkπ a_k ⇒ **a_k = b_k/(jkπ) = −(1/(π²k²))[1 − e^(−jπk)]**, yani tek k için −2/(π²k²), çift k (k ≠ 0) için 0

### Soru 3

x[n] = (1/2)ⁿu[n] ve h[n] = u[n − 2] için y[n] = x[n] ∗ h[n] katlamasını (convolution sum) hesaplayınız.

**Çözüm:** n − 2 < 0 için y[n] = 0; n ≥ 2 için y[n] = Σ_{k=0}^{n−2} (1/2)^k = (1 − (1/2)^(n−1))/(1 − 1/2) = **2 − 4(1/2)ⁿ**.

### Soru 4

Nedensel LTI sistem y[n] + ½y[n − 1] = x[n].

1. Frekans yanıtı H(e^(jω)), |H(e^(jω))| ve ∠H(e^(jω))?
1. x[n] = δ[n] + ½δ[n − 1] girişi için çıkış y[n]?

**Çözüm:**

- H(e^(jω)) = 1/(1 + ½e^(−jω)) = 1/(1 + ½cos ω − j½sin ω)
- |H(e^(jω))| = 1/√((1 + ½cos ω)² + (½ sin ω)²)
- ∠H(e^(jω)) = tan⁻¹(½ sin ω / (1 + ½ cos ω))
- X(e^(jω)) = 1 + ½e^(−jω) ⇒ Y(e^(jω)) = X(e^(jω))H(e^(jω)) = 1 ⇒ **y[n] = δ[n]**

### Soru 5

Fourier dönüşümü tanımlarını kullanarak:

1. x(t) = e^(−|t|) ise X(jω) = ? **Çözüm:** X(jω) = 1/(1 − jω) + 1/(1 + jω) = **2/(1 + ω²)**
1. X(jω) = 2πδ(ω − 2) ise x(t) = ? **Çözüm:** x(t) = (1/2π)∫2πδ(ω − 2)e^(jωt) dω = **e^(j2t)**
1. (b)'yi kullanarak x(t) = cos²(t)'nin Fourier dönüşümü: cos²t = ½ + ¼e^(j2t) + ¼e^(−j2t) ⟷ **πδ(ω) + (π/2)δ(ω − 2) + (π/2)δ(ω + 2)**

## Ocak 2016: Fourier dönüşümü sorularının çözümleri

Ocak 2016 tarihli iki çözüm kâğıdında (fotoğraflardan aktarıldı) sürekli zamanlı Fourier dönüşümü soruları çözülmüş:

**1.** h(t), −1 ile 1 arasında genliği 1 olan dikdörtgen ⇒ H(jω) = 2 sin ω / ω. Giriş X(jω) = δ(ω) + δ(ω − π) + δ(ω − π/6) + δ(ω − 7π). Konvolüsyon özelliğiyle Y(jω) = H(jω)X(jω); f(ω)δ(ω − ω₀) = f(ω₀)δ(ω − ω₀) olduğundan sin π = sin 7π = 0 terimleri düşer, lim_{ω→0} 2 sin ω/ω = 2 ve 2 sin(π/6)/(π/6) = 6/π:

- Y(jω) = 2δ(ω) + (6/π)δ(ω − π/6)
- **y(t) = 1/π + (3/π²)e^(jπt/6)**

**2.** x₁(t) = αe^(−βt)u(t) ve x₂(t) = sin(ω₀t) için x(t) = x₁(t)x₂(t)'nin dönüşümü çarpma özelliğiyle: X₁(jω) = α/(β + jω), X₂(jω) = (π/j)[δ(ω − ω₀) − δ(ω + ω₀)],

- X(jω) = (1/2π) X₁ ∗ X₂ = (α/2j)[1/(β + j(ω − ω₀)) − 1/(β + j(ω + ω₀))]
- **X(jω) = αω₀ / ((β + jω)² + ω₀²)**
