---
baslik: MAT222 Diferansiyel Denklemler: Fotoğraflanmış Vize ve Final Çalışma Notları
ozet: 2006–2007 çalışma sayfalarından metin aktarımı: Laplace tablosu, integrasyon çarpanı, homojen ve Riccati denklemleri, final hazırlık soruları.
---

Bu yazı, **fotoğraflanmış sayfalardan metne aktarıldı**. Sayfalardan biri 22 Kasım 2006 tarihli “Vize soru ve çözümleri” başlığını taşıyor; çekim tarihleri EXIF ve görüntü üzerindeki damgada 12 Ocak 2007. Hazırlayanın adı ve kurum belirtilmiyor. Fotoğraflar özel arşivde tutuluyor; bu yazının indirilebilir dosyası yok.

## Laplace dönüşüm tablosu

Fotoğrafta dönüşüm değişkeni p kullanılmıştır. Aşağıdaki tabloda α ve β sabit, n negatif olmayan tamsayıdır; dönüşüm integralinin yakınsadığı p bölgesi esas alınır.

| f(t) | L{f(t)} |
|---|---|
| 1 | 1/p |
| tⁿ | n!/pⁿ⁺¹ |
| eᵅᵗ | 1/(p − α) |
| cos βt | p/(p² + β²) |
| sin βt | β/(p² + β²) |
| cosh βt | p/(p² − β²) |
| sinh βt | β/(p² − β²) |
| tⁿeᵅᵗ | n!/(p − α)ⁿ⁺¹ |
| eᵅᵗ cos βt | (p − α)/[(p − α)² + β²] |
| eᵅᵗ sin βt | β/[(p − α)² + β²] |
| eᵅᵗ cosh βt | (p − α)/[(p − α)² − β²] |
| eᵅᵗ sinh βt | β/[(p − α)² − β²] |
| t cos βt | (p² − β²)/(p² + β²)² |
| t sin βt | 2βp/(p² + β²)² |
| t cosh βt | (p² + β²)/(p² − β²)² |
| t sinh βt | 2βp/(p² − β²)² |
| teᵅᵗ cos βt | [(p − α)² − β²]/[(p − α)² + β²]² |
| teᵅᵗ sin βt | 2β(p − α)/[(p − α)² + β²]² |

Son altı satır, ilgili temel dönüşüme −d/dp uygulanarak kontrol edildi.

## Final hazırlık soruları

El yazısı sayfanın “Finali Soruları” başlığı altında altı soru var; başlığın ilk kısaltması net okunmuyor.

1. (1 + y²) dx = (√(1 + y²) sin y − xy) dy denklemini çözünüz.
2. y″ + y = eˣ denklemini çözünüz.
3. x⁴y⁽⁴⁾ + 6x³y‴ + 7x²y″ + xy′ − y = 0 denklemini çözünüz.
4. f(t) = t sinh(βt) fonksiyonunun Laplace dönüşümünü bulunuz.
5. y′ + 5y = e⁻²ᵗ, y(0) = 1 problemini Laplace dönüşümüyle çözünüz.
6. F(p) = 1/[(p − 1)(p − 2)²] için f(t)'yi bulunuz.

## İlk sorunun el yazısı çözümü

Ayrı sayfada a = √(1 + y²), da = y dy/√(1 + y²) seçilmiş. Denklem a dx + x da = sin y dy biçimine geliyor. Fotoğrafta integral alınırken a ve x sabitmiş gibi davranılarak “ax + xa = −cos y”, ardından “2x√(1 + y²) = −cos y” yazılmış.

*Not: Sol taraf d(ax)'tir; iki bağımsız sabit gibi integre edilemez. Doğru sonuç x√(1 + y²) = −cos y + C'dir. Kaynakta integral sabiti de eksik bırakılmıştır.*

## 22 Kasım 2006: vize soru ve çözümleri

### Eğri ailesinden diferansiyel denklem

3x + y − 2 = Ce^(x + 3y).

Türev alınır: 3 + y′ = (1 + 3y′)(3x + y − 2). Son satırdaki sonuç:

y′ = (−3x − y + 5)/(9x + 3y − 7).

Bu ifade ilk eşitlikten yeniden türetilerek kontrol edildi.

### Değişkenlerine ayırma

(x²y² − x²y) dy − xy² dx = 0.

x²y²'ye bölünerek (1 − 1/y)dy = dx/x elde edilmiş. Sonuç kaynakta y − ln y = ln x + C.

Tanımlı bölgelerde mutlak değerli yazım y − ln|y| = ln|x| + C'dir. Bölme sırasında dışarıda kalan y = 0 ayrıca bir çözümdür.

### Riccati dönüşümü

y′ + xy + x = y², bilinen çözüm y₁ = x + 1. Fotoğrafta y = y₁ + 1/z seçilerek lineer denkleme geçiliyor. Notta ara satır z′ + (x + 2)z = 1 olarak yazılmış; sonraki integralde ise e^(x²/2 + 2x) önünde eksi işareti bulunuyor.

*Not: Yerine koyma z′ + (x + 2)z = −1 verir. Son integraldeki eksi işareti bu doğru denkleme uygundur: z = e^(−x²/2−2x)[C − ∫e^(x²/2+2x)dx].*

### Homojen denklem

(x² + y²) dx − 2xy dy = 0. y = ux ve dy = u dx + x du konulunca (1 − u²)dx − 2xu du = 0 bulunuyor.

dx/x = 2u du/(1 − u²).

ln|x| + ln|1 − u²| = C. Fotoğrafın son satırında (x² + y²)/x = C ve yanında C = 5 yazılmış.

*Not: Önceki integralden (x² − y²)/x = C çıkar; son satırdaki artı işareti yanlıştır. Fotoğrafta C = 5'i belirleyen bir başlangıç koşulu görünmediğinden bu sayı doğrulanamadı.*

Aynı sayfanın iki çekimi ve bir yakın çekimi birlikte okunarak tek kez aktarıldı. Okunmayan veya kadraj dışında kalan ifadeler tamamlanmadı.
