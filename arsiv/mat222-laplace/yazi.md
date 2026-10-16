---
baslik: MAT222 Diferansiyel Denklemler: Laplace Dönüşümü (Ufuk Özerman, kurum belirtilmemiş)
ozet: Ufuk Özerman'ın 2006 tarihli notu: Laplace tanımı, başlangıç değer problemleri, basamak ve dürtü fonksiyonları, öteleme ve konvolüsyon.
---

Bu yazı, **Ufuk Özerman** imzalı **29 Kasım 2006** tarihli “Laplace Dönüşümü” notunun konularını, temel bağıntılarını ve örnek sonuçlarını metne aktarıyor. Belge 106–117 numaralı 12 sayfadan oluşuyor. Kurum adı yazmıyor; saklandığı `ege_notlari` klasörünün adı tek başına Ege Üniversitesi kaynaklığı göstermiyor. Orijinal PDF yazının sonunda indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## İntegral dönüşümü ve yakınsaklık

Bir integral dönüşümü F(s) = ∫_α^β K(s,t)f(t)dt biçimindedir. K çekirdektir. Laplace dönüşümünde K(s,t) = e⁻ˢᵗ ve sınırlar 0 ile ∞ olur:

L{f(t)} = F(s) = ∫₀^∞ e⁻ˢᵗf(t)dt.

Bu bir genelleştirilmiş integraldir: ∫ₐ^∞ f(t)dt = lim_(A→∞) ∫ₐᴬ f(t)dt. Örneğin ∫₀^∞ eᶜᵗdt, c < 0 için yakınsak; c ≥ 0 için ıraksaktır. Parçalı sürekli fonksiyonlar için karşılaştırma testi kullanılabilir: |f| ≤ g ve g'nin integrali yakınsaksa f'ninki mutlak yakınsaktır.

Kaynağın varlık teoreminde, her sonlu aralıkta parçalı süreklilik ve büyük t için |f(t)| ≤ Keᵃᵗ koşulları verildikten sonra dönüşümün “s > 0 için” var olduğu yazılmış.

*Not: Üstel büyüme sınırı Keᵃᵗ ise yeterli koşul s > a'dır. s > 0 koşulu genel bir a için yeterli değildir.*

## Temel dönüşümler

| f(t) | L{f(t)} |
|---|---|
| 1 | 1/s |
| t | 1/s² |
| t² | 2/s³ |
| t³ | 6/s⁴ |
| eᵃᵗ | 1/(s − a) |
| sin(at) | a/(s² + a²) |
| cos(at) | s/(s² + a²) |
| sinh(at) | a/(s² − a²) |
| cosh(at) | s/(s² − a²) |

Polinomlar ve trigonometrik fonksiyonlar için s > 0, eᵃᵗ için s > a, hiperbolik fonksiyonlarda gerçek a için s > |a| yeterlidir. Dönüşüm lineerdir: L{c₁f₁ + c₂f₂} = c₁F₁ + c₂F₂.

## Türevlerin dönüşümü

- L{y′} = sY(s) − y(0).
- L{y″} = s²Y(s) − sy(0) − y′(0).
- L{y⁽ⁿ⁾} = sⁿY(s) − sⁿ⁻¹y(0) − … − y⁽ⁿ⁻¹⁾(0).

Uygulama sırası: denklemin dönüşümünü al, başlangıç koşullarını yerleştir, Y(s)'yi yalnız bırak, basit kesirlere ayır ve ters dönüşüm uygula.

**Örnek:** y″ + y = sin 2t, y(0) = 2, y′(0) = 1.

(s² + 1)Y = 2s + 1 + 2/(s² + 4).

Y = 2s/(s² + 1) + (5/3)/(s² + 1) − (2/3)/(s² + 4).

y(t) = 2 cos t + (5/3)sin t − (1/3)sin 2t.

Sonuç hem denklemi hem başlangıç koşullarını sağlıyor.

## Basamak fonksiyonu ve öteleme

u_c(t), t < c için 0; t ≥ c için 1'dir. c ≥ 0 için L{u_c} = e⁻ᶜˢ/s.

- L{u_c(t)f(t − c)} = e⁻ᶜˢF(s).
- L{eᶜᵗf(t)} = F(s − c).

**Örnek:** f(t) = sin t + u_(π/4)(t)cos(t − π/4) için F(s) = [1 + se^(−πs/4)]/(s² + 1).

**Örnek:** (1 − e⁻²ˢ)/s² ifadesinin ters dönüşümü t − u₂(t)(t − 2)'dir. Bu fonksiyon 0 ≤ t < 2 için t, t ≥ 2 için 2'dir.

**Örnek:** 1/(s² − 4s + 5) = 1/[(s − 2)² + 1] ifadesinin ters dönüşümü e²ᵗ sin t'dir.

## Süreksiz kuvvet

2y″ + y′ + 2y = u₅(t) − u₂₀(t), y(0) = y′(0) = 0.

Y(s) = (e⁻⁵ˢ − e⁻²⁰ˢ)H(s), H(s) = 1/[s(2s² + s + 2)].

H(s) = 1/(2s) − (s + 1/2)/(2s² + s + 2).

Buna göre y(t) = u₅(t)h(t − 5) − u₂₀(t)h(t − 20). Kaynaktaki ters dönüşüm:

h(t) = 1/2 − (1/2)e^(−t/4)[cos(√15·t/4) + (1/√15)sin(√15·t/4)].

## Dürtü fonksiyonları

Dirac delta için t₀ > 0 olduğunda L{δ(t − t₀)} = e⁻ˢᵗ⁰.

Kaynak g(t) = 2δ(t − 7) + 5δ(t + 3) örneği için 2e⁻⁷ˢ + 5e³ˢ yazıyor; ara satırda ayrıca δ(t + 2) geçiyor.

*Not: Bu notta tanımlanan tek taraflı Laplace dönüşümünde t = −3'teki dürtü integral aralığı dışındadır. Verilen g için dönüşüm 2e⁻⁷ˢ olur. e³ˢ terimi iki taraflı dönüşümle ilgilidir; δ(t + 2) ara satırı da başlangıçtaki ifadeyle tutarsızdır.*

**Örnek:** y″ + y′ + y = δ(t − 2), y(0) = y′(0) = 0 için Y(s) = e⁻²ˢ/(s² + s + 1).

Tam kareye tamamlama s² + s + 1 = (s + 1/2)² + 3/4 verir.

Kaynakta verilen dürtü cevabı, kökler sadeleştirildiğinde y(t) = u₂(t)(2/√3)e^(−(t−2)/2)sin[√3(t − 2)/2] olur.

Ödev olarak 2y″ + y′ + 2y = δ(t − 5), y(0) = y′(0) = 0 verilmiş.

## Konvolüsyon

(f ∗ g)(t) = ∫₀ᵗ f(t − τ)g(τ)dτ = ∫₀ᵗ f(τ)g(t − τ)dτ.

L{f ∗ g} = F(s)G(s).

*Not: Kaynaktaki giriş cümlesi F(s)G(s)'yi f ve g'nin “çarpımının” dönüşümü diye tanımlıyor. Burada kastedilen noktasal çarpım değil, konvolüsyondur; hemen sonraki integral tanımı doğrudur.*

- f(t) = cos t için (f ∗ 1)(t) = sin t; sonuç f(t)'ye eşit değildir.
- L⁻¹{a/[s²(s² + a²)]} = ∫₀ᵗ (t − τ)sin(aτ)dτ = (at − sin at)/a².
- Kaynak, L⁻¹{1/[s(s² + 16)]} = (1 − cos 4t)/4 yazıyor.

*Not: Son integralde ikinci bir 1/4 çarpanı eksik. ∫₀ᵗ (1/4)sin(4τ)dτ = (1 − cos 4t)/16 olmalıdır.*

Son örnek, genel bir g(t) ile y″ + 4y = g(t), y(0) = 3, y′(0) = −1 problemidir:

y(t) = 3 cos 2t − (1/2)sin 2t + (1/2)∫₀ᵗ sin[2(t − τ)]g(τ)dτ.
