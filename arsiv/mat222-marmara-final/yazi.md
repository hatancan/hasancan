---
baslik: MAT222 Diferansiyel Denklemler: 2005 Finali ve Çözümleri (Marmara Üniversitesi, Faruk Uçar)
ozet: Marmara Üniversitesi MAT232 finalinin A ve B grupları: Bessel integrali, lineer sistemler, Laplace dönüşümleri ve başlangıç değer problemi.
---

Bu yazı, **Marmara Üniversitesi Fen Edebiyat Fakültesi Matematik Bölümü MAT232 Diferansiyel Denklemler II** dersinin **7 Haziran 2005** final sorularını ve çözümlerini içeriyor. PDF üst verisindeki yazar Faruk Uçar'dır. Başkent MAT222 arşivinde saklanan bu iki dosyanın orijinalleri yazının sonunda ZIP olarak indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Ortak soru 1: Bessel integrali

Jₚ, p. mertebeden birinci tür Bessel fonksiyonu olmak üzere d[tⁿJₙ(t)]/dt = tⁿJₙ₋₁(t) eşitliğini kullanarak şu sonucu ispatlayınız:

∫₀² tJ₀(λt) dt = 2J₁(2λ)/λ.

Çözümde n = 1 alınır. Zincir kuralı d[tJ₁(λt)]/dt = λtJ₀(λt) verir. Sınırlar uygulanınca istenen sonuç bulunur.

*Not: Bölme içeren ifade λ ≠ 0 içindir. λ = 0 durumunda integral 2 olur; sağ tarafın λ → 0 limiti de 2'dir.*

## A grubu soru 2: lineer sistem

x₁′ = x₁ + x₂, x₂′ = 4x₁ − 2x₂ sistemini çözünüz.

Katsayı matrisi A = [[1, 1], [4, −2]]. det A = −6, tr A = −1. Karakteristik denklem λ² + λ − 6 = (λ + 3)(λ − 2) olduğundan özdeğerler −3 ve 2'dir. Birinci denklemden x₂ = x₁′ − x₁ bulunur.

- x₁(t) = K₁e⁻³ᵗ + K₂e²ᵗ
- x₂(t) = −4K₁e⁻³ᵗ + K₂e²ᵗ

## B grubu soru 2: lineer sistem

x₁′ = −x₁ + 4x₂, x₂′ = x₁ + 2x₂ sistemini çözünüz.

A = [[−1, 4], [1, 2]], det A = −6, tr A = 1. Karakteristik denklem (λ − 3)(λ + 2) = 0. Kaynakta verilen sonuç:

- x₁(t) = 4K₁e⁻²ᵗ + K₂e³ᵗ
- x₂(t) = −K₁e⁻²ᵗ + K₂e³ᵗ

*Not: B grubu çözümünün ara satırında x₂ = ψ′ − ψ yazıyor. Bu sistem için doğru bağıntı x₂ = (ψ′ + ψ)/4'tür. Sonuçta verilen iki çözüm vektörü ise sistemi sağlıyor.*

## A grubu soru 3: sinüs ve hiperbolik sinüs

L{sin(at)sinh(at)} hesaplanıyor. sinh(at) = (eᵃᵗ − e⁻ᵃᵗ)/2 ve F(s) = a/(s² + a²) kullanılır:

L{sin(at)sinh(at)} = [F(s − a) − F(s + a)]/2 = 2a²s/(s⁴ + 4a⁴).

## B grubu soru 3: kosinüs ve hiperbolik kosinüs

L{cos(at)cosh(at)} için F(s) = s/(s² + a²) alınır:

L{cos(at)cosh(at)} = [F(s − a) + F(s + a)]/2.

Kaynakta son satır a(s² + 2a²)/(s⁴ + 4a⁴) olarak yazılmıştır.

*Not: Kesirler ortak paydada toplandığında doğru pay s(s² + 2a²) olur. Dolayısıyla sonuç s(s² + 2a²)/(s⁴ + 4a⁴)'tür. Her iki dönüşüm için gerçek a ve s > |a| yeterlidir.*

## Ortak soru 4: başlangıç değer problemi

y″ − 3y′ + 2y = 4e²ᵗ, y(0) = −3, y′(0) = 5 denklemini Laplace dönüşümüyle çözünüz.

(s² − 3s + 2)Y(s) = 4/(s − 2) + 14 − 3s.

Basit kesirlere ayırma sonucu:

Y(s) = −7/(s − 1) + 4/(s − 2) + 4/(s − 2)².

Ters dönüşüm:

y(t) = −7eᵗ + 4e²ᵗ + 4te²ᵗ.

Bu sonuç denklemi ve iki başlangıç koşulunu sağlar. İki lineer sistemin çözüm vektörleri de türev alınarak kontrol edildi.
