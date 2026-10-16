---
baslik: MAT222 Diferansiyel Denklemler: Çalışma Soruları ve Örnek Sınavlar (Kurum belirtilmemiş)
ozet: 2006 tarihli üç föy: 32 çalışma sorusu, örnek ara sınav ve final; karışım problemleri, Euler yöntemi, lineer sistemler ve Laplace dönüşümü.
---

Bu yazı, **2006 tarihli** `calismasorulari.pdf`, `sample_test_midterm.pdf` ve `sample_test_final.pdf` föylerini bir araya getiriyor. PDF tarihleri sırasıyla 17 Kasım, 21 Haziran ve 18 Temmuz 2006. Belgelerde yazar veya kurum adı yok; Ege Üniversitesi aidiyeti doğrulanamadı. Çözüm anahtarı bulunmayan üç orijinal PDF yazının sonunda ZIP olarak indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Çalışma soruları: birinci mertebe

1. Kaynaktaki ilk satır “ylnxxlnydx + dy = 0” biçiminde, çarpım ve üs düzeni belirsiz basılmıştır.
2. dr = b(cos θ dr + r sin θ dθ).
3. y′ = (3y − xy)/x, y(1) = 3e⁻¹.
4. y(dx/dy) + 2x = 5y³.
5. (x² + 1)y′ + 4xy = 3x.
6. x dy + (xy + y − 1) dx. Kaynakta eşitliğin sağ tarafı yoktur.
7. (x² + 3y²) dx − 2xy dy = 0, y(2) = 6.
8. y³ dx = 2x³ dy − 2x²y dx, y(1) = 2.
9. (x + √(xy))y′ + x − y = x⁻¹ᐟ²y³ᐟ², y(1) = 1.
10. (x − y cos x) dx − sin x dy = 0.
11. (2xy + eʸ) dx + (x² + xeʸ) dy = 0.
12. (yeˣ + 2eˣ + y²) dx + (eˣ + 2xy) dy = 0, y(0) = 6.
13. 2y² dx + (2x + 3xy) dy = 0.
14. (x² + y² + x) dx + y dy = 0.
15. cos(y)y′ + 2x − 2x sin y = 0.
16. y²(dx/dy) + xy = 2y² + 1.

*Not: 1. sorudaki belirsiz dizgi ve 6. sorudaki eksik eşitlik tahminle tamamlanmadı.*

## Çalışma soruları: yüksek mertebe ve sistemler

**17.** (x³ − x²)y″ − (x³ + 2x² − 2x)y′ + (2x² + 2x − 2)y = 0. f(x) = x² bir çözümse diğerini bulunuz.

**18.** (x² − 1)y″ − 2xy′ + 2y = 1. Homojen denklemin f(x) = x çözümünden yararlanarak özel çözümü bulunuz.

**19.** y″ + y′/x − 4y/x² = 1 − 1/x³, x > 0. Homojen çözüm y₁ = x² yardımıyla tamamlayıcı ve özel çözümleri bulunuz.

**20.** (D² + 1)y = 10e²ˣ, y(0) = y′(0) = 0.

**21.** y″ + 3y′ + 2y = eᵗ, y(0) = 0, y′(0) = 1. Kaynaktaki x/t gösterim farkı korunmuştur.

**22.** (D − 1)²(D + 4)(D² + 4D + 5)y = 2eˣ + x − 3x² − xeˣ − 15 cos 2x. Katsayılarını hesaplamadan özel çözüm biçimini bulunuz.

**23.** x²y″ − 3xy′ + 3y = (ln x)/x, x > 0.

**24.** (x + 1)(2x + 1)y″ + 2xy′ − 2y = 6x(x + 1), x > 0. Homojen çözüm f(x) = 1/(x + 1) verildiğine göre genel çözümü bulunuz.

**25.** y⁽⁴⁾ + 2y‴ + y″ = x² + 4 + e⁻ˣ + e⁻ˣ sin x.

**26.** y″ − 2y′ + y = eˣ sin⁻¹x.

**27.** y″ + y = 1/(1 + sin x).

**28.** y″ + 3y′ + 2y = 1/(1 + eˣ).

**29.** x²y″ + xy′ + y = 1/[1 + sin(ln x)].

**30.** (1 − x)y″ + xy′ − y = 2(x − 1)²e⁻ˣ, 0 < x < 1. Homojen çözümler eˣ ve x veriliyor. Tamamlayıcı çözümü ve özel çözüm biçimini bulunuz.

**31.** −5x₁ − 2x₂ + 2x₃ = 2; x₁ + 5x₂ − 3x₃ = 2; 5x₁ − 3x₂ + x₃ = 2 sistemini Gauss eleme yöntemiyle çözünüz, katsayı matrisinin tersini bulunuz ve ters matrisle tekrar çözünüz.

**32.** y″ − 4y = ln(x − 1) için çözümün var olduğu aralığı belirleyiniz. e²ˣ ve e⁻²ˣ fonksiyonlarının homojen denklemin lineer bağımsız çözümleri olduğunu gösterip tamamlayıcı çözümü yazınız.

Föy, sınava diferansiyel denklemlerin uygulamalarının ve sistemlerin de dahil olduğunu hatırlatıyor.

## Örnek ara sınav: model ve ilk denklemler

1. d²y/ds² − yy⁽⁴⁾ + sy″ = 3s + 7 ve y‴ + 5y′ + tan y = t² + cos t için mertebe, lineerlik, bağımlı ve bağımsız değişkenleri belirleyiniz.
2. Merkezleri x ekseninde olan çember ailesinin diferansiyel denklemini bulunuz.
3. 1600 L havuzda başlangıçta 10 kg tuz var. Giriş 12 L/dak ve 0,5 kg/L; çıkış aynı debide. Tam karışım varsayımıyla tuz miktarının denklemini, çözümünü ve 20 dakika sonraki miktarı bulunuz.
4. u′ = (2t + sec²t)/(2u), u(0) = −5 ve xy′ + y = y², y(1) = −1 başlangıç değer problemlerini çözünüz.
5. y′ = tan(x + y − 3) − 1.
6. [t cos(z/t) − z sin(z/t)]dt + t sin(z/t)dz = 0.
7. [y/(x − 1)]dx + [ln(2x − 2) + 1/y]dy = 0.
8. (y³ + 2eˣy)dx + (eˣ + 3y²)dy = 0 için integrasyon çarpanı bulunuz ve çözünüz.
9. u′ − 2tu = 3t²eᵗ², u(0) = 5; eʸy′ + eʸ(ln x)/x = (ln x)/x, y(1) = 2; xz′ + xz + z = e⁻ˣ, x > 0 problemlerini çözünüz.
10. dz/dt + z sin t + z² sin 2t = 0.
11. x²y″ + 3xy′ + y = 0, x > 0 için y₁ = 1/x biliniyor. Mertebe düşürerek bağımsız ikinci çözümü bulunuz.
12. y′ = x² + y², y(0) = 1 problemini [0,1] üzerinde h = 0,2 ile Euler yöntemiyle çözünüz.

## Örnek ara sınav: 13–14

On üçüncü soruda şu denklemlerin genel çözümleri isteniyor:

- y⁽⁴⁾ − 7y‴ + y″ − 7y′ = e⁻²ˣ.
- x²y″ + xy′ − 4y = x² ln x.
- y⁽⁴⁾ + 2y″ + y = xeˣ.
- y″ − 4y′ + 4y = e²ˣ ln x/x.

On dördüncü sorunun sistemleri:

- x′ = −2x + 2z, y′ = 2x − 4y, z′ = 4x − 2y.
- x₁′ = −2x₁ + x₂ + 2e⁻ᵗ, x₂′ = x₁ − 2x₂ + 3t; x₁(0) = 1, x₂(0) = −1.

## Örnek final

1. y = Ae²ˣ + Bx ailesinin diferansiyel denklemini bulunuz.
2. 800 L havuzda başlangıçta 5 kg tuz var. Giriş 6 L/dak, tuzluluk 0,5 kg/L, çıkış aynı debide. Denklemi ve çözümünü, ayrıca 10 dakika sonraki tuz miktarını bulunuz.
3. dx/dt = x/5 − x²/25, x(0) = 1.
4. y′ − 4y tan x = [sin x/(2cos³x)]y¹ᐟ².
5. y′ = tan(x + y − 3) − 1.
6. (3xeʸ + 2y)dx + (x²eʸ + x)dy = 0 için integrasyon çarpanı bulunuz.
7. [y/(x − 1)]dx + [ln(2x − 2) + 1/y]dy = 0.
8. (1 + 2x²)y″ + xy′ + 2y = 0 için kuvvet serisi çözümü bulunuz.
9. 2x²y″ + 3xy′ − (x² + 1)y = 0 için x = 0 çevresinde seri çözümü bulunuz.
10. z″ − 4z′ + 4z = e²ᵗ ln t/t.
11. x²y″ + 3xy′ + y = 0, x > 0 için y₁ = 1/x yardımıyla ikinci çözümü bulunuz.
12. y′ = 2x² + 3y², y(0) = 1 problemini [0,2] üzerinde h = 0,4 ile Euler yöntemiyle çözünüz.
13. y‴ − 4y″ + 5y′ − 2y = 4 cos x + sin x.
14. x₁′ = x₁ + √3x₂ + eᵗ, x₂′ = √3x₁ − x₂ + √3e⁻ᵗ; x₁(0) = 1, x₂(0) = −1.
15. F(s) = (3s² − 2s + 5)/[(s − 2)(s² + 9)] için ters Laplace dönüşümünü bulunuz.
16. f(t) = te⁻ᵗ cos t için Laplace dönüşümünü bulunuz.
17. Aşağıdaki üç başlangıç değer problemini Laplace yöntemiyle çözünüz.

Son sorunun alt bölümleri:

- y″ + 2y = 4t² + 12; y(0) = 4, y′(0) = 0.
- y″ + y = e⁻²ᵗ sin t; y(0) = y′(0) = 0.
- y″ − y′ − 6y = r(t); y(0) = 1/50, y′(0) = −7/50. r(t) = sin t, 0 < t < 3π; r(t) = 0, t > 3π.

## Kısa hesap kontrolleri

Karışım sorularında tuz miktarı m için giriş eksi çıkış dengesi kullanılır. Ara sınavda m′ = 6 − 0,0075m ve m(t) = 800 − 790e⁻⁰·⁰⁰⁷⁵ᵗ; finalde m′ = 3 − 0,0075m ve m(t) = 400 − 395e⁻⁰·⁰⁰⁷⁵ᵗ. İkinci bağımsız Euler çözümü ln x/x'tir. Bu sonuçlar föydeki cevaplar değil, aktarım sırasında yapılan kontrollerdir.
