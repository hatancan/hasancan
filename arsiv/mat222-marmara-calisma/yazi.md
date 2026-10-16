---
baslik: MAT222 Diferansiyel Denklemler: 30 Çalışma Problemi (Marmara Üniversitesi, Faruk Uçar)
ozet: Marmara MAT232 çalışma föyü: Cauchy–Euler, Taylor ve Frobenius serileri, tekil noktalar ve Bessel bağıntıları; verilen yanıtlarla birlikte.
---

Bu yazı, **Marmara Üniversitesi Fen Edebiyat Fakültesi Matematik Bölümü MAT232 Diferansiyel Denklemler II** çalışma föyünü içeriyor. PDF üst verisi yazarı **Faruk Uçar**, tarihi **8 Nisan 2005** olarak gösteriyor. Altı sayfalık belgedeki 30 ana soru ve temel yanıtlar metne aktarıldı. Orijinal PDF yazının sonunda indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Cauchy–Euler problemleri: 1–9

**1.** t²y″ + 3ty′ + 5y = 0 denklemini t = eˣ dönüşümüyle ve y = tʳ deneyerek çözünüz. Yanıt: y = |t|⁻¹[C₁ cos(2 ln|t|) + C₂ sin(2 ln|t|)].

**2.** t > 0 için aşağıdaki denklemleri çözünüz:

| Denklem | Kaynakta verilen çözüm |
|---|---|
| t²y″ + 2ty′ − 6y = 0 | C₁t⁻³ + C₂t² |
| t²y″ + 9ty′ + 2y = 0 | C₁t^(−4−√14) + C₂t^(−4+√14) |
| t²y″ − 5ty′ + 25y = 0 | t³[C₁ cos(4 ln t) + C₂ sin(4 ln t)] |
| 2t²y″ − ty′ + y = 0 | C₁√t + C₂t |
| t²y″ + 5ty′ + 4y = 0 | t⁻²(C₁ + C₂ ln t) |
| 2t²y″ + ty′ − y = 0 | C₁t⁻¹ᐟ² + C₂t |


**3.** t²y″ − ty′ + y = t ln t. Yanıt: t[C₁ + C₂ ln t + (ln t)³/6].

**4.** t³y‴ − 2t²y″ + 8ty′ − 8y = 0 için C₁t + t²[C₂ cos(2 ln t) + C₃ sin(2 ln t)]; t³y‴ + ty′ − y = 0 için C₁t + C₂t ln t + C₃t(ln t)².

**5.** (t − 1)²y″ + 8(t − 1)y′ + 12y = 0. Yanıt: C₁/(t − 1)³ + C₂/(t − 1)⁴.

**6.** t²y″ − 3ty′ + 4y = t + t² ln t. Yanıt: C₁t² + C₂t² ln t + t + t²(ln t)³/6.

**7.** t²y″ − 2ty′ + 2y = (ln t)² − ln(t²). Yanıt: C₁t + C₂t² + 1/4 + [(ln t) + (ln t)²]/2.

**8.** t²y″ − ty′ + 4y = cos(ln t) + t sin(ln t). Yanıt: C₁t cos(√3 ln t) + C₂t sin(√3 ln t) + t sin(ln t)/2 + [3 cos(ln t) − 2 sin(ln t)]/13.

**9.** t²y″ + 5ty′ + 5y = t⁻³. Yanıt: t⁻²[C₁ cos(ln t) + C₂ sin(ln t)] + 1/(2t³).

## Taylor serileri: 10–19

**10.** y′ = 2ty, y(0) = 1 için t = 0 çevresinde seri bulunuz ve y = eᵗ² olduğunu gösteriniz.

**11.** y″ − ty′ = 0, y(1) = 0, y′(1) = 1 için t = 1 çevresinde seri bulunuz. Kaynak y = (t − 1) + (t − 1)³/6 + (t − 1)⁴/12 + … yazıyor.

*Not: Başlangıç koşulları y″(1) = 1 verir; dolayısıyla ikinci derece terim eksik olamaz. Doğru başlangıç y = s + s²/2 + s³/3 + s⁴/6 + …, s = t − 1'dir.*

**12.** y″ + 4y = 0 → a₀ cos 2t + (a₁/2)sin 2t.

**13.** y″ − 2ty = 0 → a₀(1 + t³/3 + t⁶/45 + …) + a₁(t + t⁴/6 + t⁷/126 + …).

**14.** y″ − 2ty′ + y = 0 için Taylor serisini bulunuz. Katsayı eşitlemesi (n + 2)(n + 1)aₙ₊₂ = (2n − 1)aₙ verir. Kaynaktaki çift seri 1 − t²/2! − … ve tek seri t + … biçiminde yazılmış.

*Not: Kaynağın tek seri toplamı n = 2'den başlatıldığı için t³/6 terimi düşmüş. Tek serinin başlangıcı t + t³/6 + t⁵/24 + … olmalıdır.*

**15.** y″ + 2ty′ + 2y = 0 → a₀(1 − t² + t⁴/2 − t⁶/6 + …) + a₁(t − 2t³/3 + 4t⁵/15 − …). Kaynak bu satırda |t| < 1 yazıyor.

*Not: Bu denklemde katsayılar her yerde analitiktir; iki çözüm serisi de tüm t için yakınsaktır. |t| < 1 geçerli bir alt bölge olsa da gerçek yakınsaklık yarıçapı ∞'dir.*

**16.** (1 − t)y″ + y = 0 → a₀(1 − t²/2 − t³/6 − t⁴/24 − …) + a₁(t − t³/6 − t⁴/12 − …).

**17.** J₀(t) = Σ_(n=0)^∞ (−1)ⁿt²ⁿ/[2²ⁿ(n!)²] fonksiyonunun ty″ + y′ + ty = 0 denklemini sağladığını gösteriniz.

**18.** t³y‴ − 2t²y″ + 4ty′ − 4y = 0 → C₁t + C₂t² + C₃t² ln t.

**19.** y″ − ty′ − y = 0 → a₀Σ t²ⁿ/(2ⁿn!) + a₁Σ [2ⁿn!/(2n + 1)!]t²ⁿ⁺¹. Yakınsaklık yarıçapı ∞.

## Tekil noktalar: 20–23

**20.** Tüm tekil noktaları sınıflandırınız:

- (1 − t²)y″ − 2ty′ + α(α + 1)y = 0: ±1 düzgün tekil.
- 2(t − 2)²ty″ + 2ty′ + (t − 2)y = 0: 0 düzgün tekil, 2 düzgün olmayan tekil.
- (t − π/2)²y″ + cos(t)y′ + sin(t)y = 0: π/2 düzgün tekil.

**21.** Tüm tekil noktaları sınıflandırınız:

- t²y″ + sin(t)y = 0.
- y″ + ln(t)y = 0.
- (t² − 1)y″ + 2ty′ + 6y = 0.
- (t² + 1)y″ + 2ty′ + 6y = 0.
- t²(t + 1)²y″ + (t² − 1)y′ + 2y = 0.
- (t² − 4)²y″ + (t − 2)y′ + y = 0.

Kaynak ilk denklem için 0'ı düzgün tekil; beşincide −1'i düzgün, 0'ı düzgün olmayan tekil olarak veriyor. Dördüncü için “tüm noktalar bayağı” diyor.

*Not: Dördüncü cevap gerçek eksen içindir; kompleks düzlemde ±i tekildir. ln t içeren denklemde t ≤ 0 gerçek katsayılı denklemin tanım alanı dışındadır; bu bölgenin her noktasını aynı türden tekil nokta diye sınıflandırmak uygun değildir.*

**22.** Verilen noktanın türünü belirleyiniz:

- t(t − 2)²y″ + ty′ + y = 0: t = 0 ve t = 2.
- sin(t)y″ + cos(t)y′ + t⁻¹y = 0: t = 0.
- (eᵗ − 1)y″ + ty′ + y = 0: t = 0.
- (1 − t²)y″ + y′/sin(t + 1) + y = 0: t = −1.
- t³y″ + sin(t²)y′ + ty = 0: t = 0.

**23.** Tekil noktaları türleriyle belirleyiniz:

- (t⁵ − t⁴ − 6t³)y″ + t²y′ + (t − 2)y = 0.
- (t² − 3t)y″ + (t + 2)y′ + y = 0.
- (t³ + t²)y″ + (t² − 2t)y′ + 4y = 0.
- (t⁴ − 2t³ + t²)y″ + 2(t − 1)y′ + t²y = 0.

## Frobenius problemleri: 24–29

**24.** t²y″ + 4ty′ + (t − 4)y = 0 için indis kökleri 1 ve −4. Kaynak y₁ = t(1 + Σ aₙtⁿ), y₂ = ay₁ ln t + t⁻⁴(1 + Σ bₙtⁿ) yapısını veriyor.

**25.** 2ty″ − y′ + 2y = 0 için düzgün tekilliği gösterip Frobenius yöntemiyle çözünüz. Verilen seriler t³ᐟ²(1 − 2t/5 + 2t²/35 − 4t³/945 + …) ve 1 + 2t − 2t² + 4t³/9 − ….

**26.** ty″ + 2y′ − ty = 0 → (K₁ sinh t + K₂ cosh t)/t.

**27.** 4ty″ + 2y′ + y = 0 → sin√t ve cos√t.

**28.** t = 0 çevresinde Frobenius yöntemiyle çözünüz:

- t²y″ − ty′ + (2t² + 5/9)y = 0.
- 2t²y″ + ty′ + (2t² − 3)y = 0.
- t²y″ − ty′ + (t² − 3)y = 0.
- ty″ + y′ + 2y = 0.
- t²y″ + (t³ − t)y′ − 3y = 0.

**29.** Kaynakta verilen denklem ve temel çözüm çiftleri:

| Denklem | Çözüm çifti |
|---|---|
| 2ty″ + y′ + 2y = 0 | cos(2√t), sin(2√t) |
| ty″ − y′ + 64t³y = 0 | cos(4t²), sin(4t²) |
| 4ty″ + 2y′ − y = 0 | cosh√t, sinh√t |
| 4t²y″ − 4ty′ + (3 − 4t²)y = 0 | √t cosh t, √t sinh t |
| t²y″ + 6ty′ − (t² − 6)y = 0 | cosh t/t³, sinh t/t³ |

## Bessel bağıntısı: 30

d[tᵖJₚ(t)]/dt = tᵖJₚ₋₁(t) ve d[t⁻ᵖJₚ(t)]/dt = −t⁻ᵖJₚ₊₁(t) bağıntılarından Jₚ₊₁(t) = (2p/t)Jₚ(t) − Jₚ₋₁(t) elde ediniz. J₃(2t)'yi J₀(2t) ve J₁(2t) cinsinden yazınız.

Kontrol: yineleme iki kez uygulanınca J₃(2t) = (2/t² − 1)J₁(2t) − (2/t)J₀(2t), t ≠ 0 bulunur.
