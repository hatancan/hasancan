---
baslik: MAT222 Diferansiyel Denklemler: Çözümlü Çalışma Soruları 1–2 (Kurum belirtilmemiş)
ozet: 2006–2007 güz döneminden 22 çözümlü soru: birinci mertebe, Bernoulli, Clairaut, Riccati, sabit katsayılı denklemler ve parametrelerin değişimi.
---

Bu yazı, **2006–2007 güz dönemi Diferansiyel Denklemler Çalışma Soruları 1 ve 2** föylerini içeriyor. PDF oluşturulma tarihleri 13 ve 15 Kasım 2006; üst veride yalnız “SerdarB” hesap adı var. Belgede kurum veya açık yazar adı bulunmuyor; Ege Üniversitesi kaynaklığı doğrulanamadı. Sorular ve çözüm sonuçları metne aktarıldı; toplam 17 sayfalık iki orijinal PDF yazının sonunda ZIP olarak indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Çalışma Soruları 1

### Lineer denklemler: 1–3

1. y′ + 2y = sin t. İntegrasyon çarpanı e²ᵗ; sonuç y = (2 sin t − cos t)/5 + Ce⁻²ᵗ.
2. (4 + t)y′ + y = 6 + 2t. Kaynak µ = 1/(4 + t) ve son satırda y = 6t + t² + C(4 + t) yazıyor.
3. y′ − 3y = 7, y(0) = 15. Sonuç y = −7/3 + (52/3)e³ᵗ.

*Not: İkinci sorunun doğru çarpanı µ = t + 4'tür. [(t + 4)y]′ = 6 + 2t olduğundan y = (t² + 6t + C)/(t + 4), t ≠ −4. Kaynaktaki çözüm genel olarak denklemi sağlamaz.*

### Homojen ve Bernoulli denklemleri: 4–5

**4.** y′ = (2xy + 3y²)/(2xy + x²). y = vx dönüşümüyle dx/x = (2v + 1)dv/(v + v²). Kaynakta x³/(xy + y²) sabit olarak bulunuyor. Bölme dışında kalan y = 0 ve y = −x ayrıca denetlenmelidir.

**5.** xy − y′ = y³e⁻ˣ². u = y⁻² dönüşümü u′ + 2xu = 2e⁻ˣ² verir. Sonuç y⁻² = (2x + C)e⁻ˣ².

*Not: Beşinci sorunun alternatif çözümünün son satırında u yerine y yazılmıştır. Bulunan (2x + C)e⁻ˣ² ifadesi y değil y⁻²'dir. Ayrıca y = 0 çözümü dönüşüm sırasında dışarıda kalır.*

### Tamlık ve integrasyon çarpanı: 6–8

**6.** x dy − y dx = x²eˣ dx için x'e bağlı integrasyon çarpanı µ = x⁻². Sonuç y/x − eˣ = C veya y = Cx + xeˣ.

**7.** sin x cos y dx + cos x sin y dy = 0 tamdır; −cos x cos y = C.

**8.** (yeˣ + y) dx + (eˣ + x) dy = 0 tamdır; yeˣ + xy = C.

### Clairaut ve Riccati: 9–10

**9.** y = xy′ + (y′)³. Genel aile y = Cx + C³. Zarf için x = −3C², y = −2C³; dolayısıyla y² = −4x³/27.

**10.** y′ = 2 tan x sec x − y² sin x, bilinen çözüm y₁ = sec x. y = sec x + 1/u dönüşümü u′ − 2u tan x = sin x verir. Kaynaktaki sonuç:

y = sec x + 3cos²x/(C − cos³x).

Bu ifade tanımlı olduğu aralıkta denklemi sağlar; bilinen y = sec x çözümü de ayrıca korunur.

## Çalışma Soruları 2

### Mertebe düşürme: 1–2

**1.** (1 + x²)y″ + (y′)² + 1 = 0. Kaynak p = y′ seçip dp/(1 + p²) = −dx/(1 + x²) buluyor; ardından p = −x/C ve y = −x²/(2C) + C₁ yazıyor.

*Not: İntegrasyon arctan p = −arctan x + C verir; arktanjantların oranı alınamaz. Genel p ifadesi tan(C − arctan x)'tir. Kaynaktaki parabol, keyfi C için çözüm değildir.*

**2.** xy″ = √(1 + (y′)²). p = y′ ile ∫dp/√(1 + p²) = ∫dx/x. Kaynak x > 0 bölgesinde y = Cx²/4 − ln x/(2C) + C₁ sonucunu veriyor; kare alma öncesindeki Cx = p + √(1 + p²) koşulu nedeniyle burada C > 0 alınmalıdır.

### Homojen ve zorlanmış denklemler: 3–7

**3.** y″ + 6y = 0. Çözüm C₁ cos(√6x) + C₂ sin(√6x). Wronskiyen √6 ≠ 0.

**4.** y″ + 3y′ + 2y = 0, y(0) = 2, y′(0) = 1. Çözüm 5e⁻ˣ − 3e⁻²ˣ.

**5.** y″ − 7y′ + 10y = 6t + 8e²ᵗ. Kaynak C₁e²ᵗ + C₂e⁵ᵗ + 2te²ᵗ + 3t/5 + 21/50 yazıyor.

*Not: L{Dte²ᵗ} = −3De²ᵗ olduğundan D = −8/3 olmalıdır. Doğru özel çözüm −(8/3)te²ᵗ + 3t/5 + 21/50'dir.*

**6.** y″ + 7y′ + 12y = sin 2x + e⁻³ˣ + 4. Kaynağın sonucu C₁e⁻³ˣ + C₂e⁻⁴ˣ − (7/30)cos 2x + (4/30)sin 2x + xe⁻³ˣ + 1/3.

*Not: Trigonometrik katsayılar yanlış hesaplanmış. −14A + 8B = 1, 8A + 14B = 0 sisteminden A = −7/130, B = 2/65 çıkar. Diğer özel çözüm terimleri doğrudur.*

**7.** y″ − 5y′ + 4y = −4(x² + 1)e³ˣ. Kaynağın sonucu C₁eˣ + C₂e⁴ˣ + (2x² + 2x + 5)e³ˣ; yerine koyma kontrolünü sağlar.

### Parametrelerin değişimi: 8–10

**8.** y″ + y = sin x. Kaynak u₁′ = −sin²x ve u₂′ = sin x cos x ile parametrelerin değişimini uyguluyor.

*Not: Sonuç satırında sin(2x)cos x teriminin işareti önceki integralle uyuşmuyor. Sadeleşmiş doğru genel çözüm C₁ cos x + C₂ sin x − (x/2)cos x'tir.*

**9.** (2 − t)y‴ + (2t − 3)y″ − ty + y = 0 için y₁ = eᵗ biliniyor; mertebe düşürerek başka bir çözüm bulunması isteniyor. Föy bu soruyu tekrar ediyor, çözüm vermiyor. Soru metnindeki −ty terimi burada aynen korunmuştur.

**10.** y‴ + y′ = 1/sin x, 0 < x < π. Kaynak sonucu:

y = C₁ + C₂ cos x + C₃ sin x − ln(csc x + cot x) − cos x ln(sin x) − x sin x.

*Not: Çözümde kullanılan negatif logaritma doğrudur. Ancak sayfa altındaki hatırlatma formülünde eksi işareti eksik: ∫csc(ax)dx = −ln|csc(ax) + cot(ax)|/a + C olmalıdır.*

### Belirsiz katsayılar: 11–12

**11.** y‴ − 4y″ + y′ + 6y = sin 4x. Homojen kökler −1, 2, 3. Kaynak özel çözümü (12/1565)cos 4x + (13/1565)sin 4x olarak veriyor.

*Not: Yerine koyma 70A − 60B = 0, 60A + 70B = 1 verir. Doğru özel çözüm (3/425)cos 4x + (7/850)sin 4x'tir.*

**12.** Soru sayfasındaki ifade y‴ − 2y″ + 17 = 8 + e²ˣ cos 5x + x²eˣ sin 4x + (x + 1). Çözüm sayfası ise y‴ − 2y″ + 17y′ denklemini ele alıyor. Bu ikinci ifadeye göre homojen çözüm C₁ + eˣ(C₂ cos 4x + C₃ sin 4x).

Özel çözümün biçimi için kaynak; Ax, e²ˣ(B cos 5x + C sin 5x), rezonanslı trigonometrik polinom ve x(Kx + L) terimlerini kullanıyor.

*Not: Soru sayfasında 17'nin yanındaki y′ eksik. Çözümdeki rezonanslı terimde ise sinüslü polinomun önündeki x eksik bırakılmış. Uygun biçim xeˣ[(a₂x² + a₁x + a₀)cos 4x + (b₂x² + b₁x + b₀)sin 4x]'tir. Ax terimi x(Kx + L) içinde zaten temsil edilebilir.*
