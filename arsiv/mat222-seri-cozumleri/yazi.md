---
baslik: MAT222 Diferansiyel Denklemler: Kuvvet Serileri ve Frobenius Çözümleri (Ufuk Özerman, kurum belirtilmemiş)
ozet: 2006 tarihli seri çözümü notları ve dokuz çözümlü soru: yakınsaklık, adi ve tekil noktalar, Euler denklemleri, Frobenius yöntemi ve Bessel fonksiyonları.
---

Bu yazı, **Ufuk Özerman** imzalı 27 sayfalık “İkinci Derece Denklemlerin Seri Çözümü” notunu ve **12 Aralık 2006** tarihli 10 sayfalık çözüm föyünü bir araya getiriyor. İlk dosya 29 Kasım 2006 tarihli; basılı sayfa numaraları 79–105. Üniversite adı belgelerde yok, bu nedenle Ege Üniversitesi aidiyeti doğrulanmış değildir. Konular, temel bağıntılar ve örnek sonuçları metne aktarıldı; iki orijinal PDF yazının sonunda ZIP olarak indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Kuvvet serisi ve yakınsaklık

y = Σ_(n=0)^∞ aₙ(x − x₀)ⁿ.

Kısmi toplamların limiti varsa seri yakınsaktır. Yakınsaklık yarıçapı ρ için |x − x₀| < ρ bölgesinde mutlak yakınsaklık, |x − x₀| > ρ bölgesinde ıraksaklık vardır. Uç noktalar ayrı incelenir. Yalnız merkezde yakınsaklık durumunda ρ = 0; her x için yakınsaklıkta ρ = ∞.

Oran testinde L = lim |aₙ₊₁/aₙ|·|x − x₀| alınır. L < 1 yakınsaklık, L > 1 ıraksaklık verir; L = 1 karar verdirmez.

- Σ_(n=1)^∞ (−1)ⁿ⁺¹n(x − 2)ⁿ: 1 < x < 3 için yakınsak; iki uçta da genel terim sıfıra gitmediğinden ıraksak.
- Σ (x + 1)ⁿ/(n2ⁿ): −3 < x < 1 içinde mutlak yakınsak; x = −3'te alternatif harmonik seri olarak koşullu yakınsak, x = 1'de ıraksak.

*Not: İkinci örneğin ilk yazımında toplam n = 0'dan başlatılmış; paydada n bulunduğu için başlangıç n = 1 olmalıdır. İlk sayfadaki mutlak yakınsaklık tanımında ise mutlak değer işaretleri eksiktir: mutlak yakınsaklık, terimlerin mutlak değerleri toplamının yakınsaklığıdır.*

## Seri işlemleri ve Taylor açılımı

Ortak yakınsaklık bölgesinde toplama, çıkarma ve çarpma yapılır; bölüm için paydanın sıfır olmaması gerekir. Türevler terim terim alınır:

- y′ = Σ_(n=1)^∞ naₙ(x − x₀)ⁿ⁻¹.
- y″ = Σ_(n=2)^∞ n(n − 1)aₙ(x − x₀)ⁿ⁻².
- İndis kaydırma: Σ_(n=2)^∞ aₙxⁿ = Σ_(n=0)^∞ aₙ₊₂xⁿ⁺².

Sıfır fonksiyonunu veren kuvvet serisinin tüm katsayıları sıfırdır. Bu, diferansiyel denklemden yineleme bağıntısı çıkarmayı sağlar.

*Not: Notta Taylor katsayısı f⁽ⁿ⁾(x₀)/n olarak basılmış; doğru payda n!'dir. Kuvvet serisinin iç bölgede terim terim türevlenebilmesi, sıradan bir sürekli fonksiyonun tüm türevlerinin var olduğu anlamına gelmez.*

## Adi nokta ve tekil nokta

P(x)y″ + Q(x)y′ + R(x)y = 0 için p = Q/P, q = R/P tanımlanır. Polinom katsayılı örneklerde P(x₀) ≠ 0 ise x₀ adi noktadır. Tekil noktada (x − x₀)p(x) ve (x − x₀)²q(x) analitik uzanabiliyorsa nokta düzgün tekildir. Notun rasyonel katsayılı örneklerinde bu koşul ilgili limitlerin sonlu olmasıyla kontrol ediliyor.

Örnekler:

- (x² − 4)y″ + 2xy′ + ay = 0: tekil noktalar ±2.
- x²y″ + xy′ + (x² − 1)y = 0: tekil nokta 0.
- Legendre: (1 − x²)y″ − 2xy′ + α(α + 1)y = 0.
- Airy biçimi: y″ − λxy = 0.
- Hermite: y″ − 2xy′ + 2ny = 0.
- Bessel: x²y″ + xy′ + (x² − ν²)y = 0.

## Adi nokta çevresinde çözüm

**y″ + y = 0:** aₙ₊₂ = −aₙ/[(n + 2)(n + 1)]. Çift katsayılar kosinüs, tek katsayılar sinüs serisini verir:

y = a₀ cos x + a₁ sin x.

**y″ − xy = 0:** a₂ = 0 ve aₙ₊₂ = aₙ₋₁/[(n + 2)(n + 1)] (n ≥ 1). Sonuç:

y = a₀(1 + x³/6 + x⁶/180 + …) + a₁(x + x⁴/12 + x⁷/504 + …).

Analitik p ve q için yakınsaklık yarıçapının alt sınırı, merkezden kompleks düzlemde en yakın katsayı tekilliğine olan uzaklıkla bulunur. Örneğin (1 + x²)y″ + 2xy′ + 4x²y = 0 için ±i noktalarına uzaklık, x₀ = 0'da 1; x₀ = 1/2'de √5/2'dir.

## Euler denklemleri

x²y″ + αxy′ + βy = 0 için y = xʳ seçimi r(r − 1) + αr + β = 0 verir.

- Ayrık gerçek kökler: C₁xʳ¹ + C₂xʳ².
- Katlı kök: xʳ(C₁ + C₂ ln x), x > 0.
- r = λ ± iµ: x^λ[C₁ cos(µ ln x) + C₂ sin(µ ln x)], x > 0.

Nottaki örnek sonuçlar:

- x²y″ + xy′ − 4y = 0 → C₁x⁻² + C₂x².
- 2x²y″ + 3xy′ − y = 0 → C₁√x + C₂/x.
- x²y″ + xy′ + 2y = 0 → C₁ cos(√2 ln x) + C₂ sin(√2 ln x).

## Frobenius yöntemi

Düzgün tekil nokta x = 0 çevresinde çözüm y = xʳΣ_(n=0)^∞ aₙxⁿ, a₀ ≠ 0 biçiminde aranır. p₀ = lim xp(x), q₀ = lim x²q(x) için indis denklemi:

F(r) = r(r − 1) + p₀r + q₀ = 0.

En küçük kuvvetin katsayısı indis denklemini; sonraki kuvvetler yineleme bağıntısını verir. Ayrık kökler arasındaki fark tam sayı değilse iki Frobenius serisi bulunur. Katlı kökte ikinci çözümde ln x terimi oluşur. Pozitif tam sayı farkında ikinci çözüm bir logaritma terimi içerebilir; katsayısı sıfır da olabilir.

**Örnek:** 2x²y″ − xy′ + (1 + x)y = 0 için F(r) = 2r(r − 1) − r + 1; kökler 1 ve 1/2. Yineleme bağıntısı aₙ = −aₙ₋₁/[2(r + n)(r + n − 1) − (r + n) + 1].

## Yarım mertebeli Bessel denklemi

x²y″ + xy′ + (x² − 1/4)y = 0 için indis kökleri ±1/2'dir. İki çözüm sin x/√x ve cos x/√x ile ifade edilir:

- J_(1/2)(x) = √(2/(πx)) sin x.
- J_(−1/2)(x) = √(2/(πx)) cos x.

Kök farkı 1 olmasına rağmen bu örneğin bağımsız çözümlerinde logaritma gerekmez.

## Çözüm föyü: dokuz soru

### 1. y″ − xy′ − y = 0

aₙ₊₂ = aₙ/(n + 2).

y = a₀(1 + x²/2 + x⁴/8 + …) + a₁(x + x³/3 + x⁵/15 + …).

### 2. 2y″ + xy′ + 3y = 0

aₙ₊₂ = −(n + 3)aₙ/[2(n + 1)(n + 2)].

y = a₀(1 − 3x²/4 + 15x⁴/96 + …) + a₁(x − x³/3 + x⁵/20 + …).

### 3. (1 − x)y″ + xy′ − y = 0

aₙ₊₂ = [n(n + 1)aₙ₊₁ − (n − 1)aₙ]/[(n + 1)(n + 2)].

y = a₀(1 + x²/2! + x³/3! + …) + a₁x. İlk seri eˣ − x'tir.

### 4. (1 + x²)y″ − 4xy′ + 6y = 0

aₙ₊₂ = −(n² − 5n + 6)aₙ/[(n + 1)(n + 2)]. Seriler sonlanır:

y = a₀(1 − 3x²) + a₁(x − x³/3).

### 5. x²(1 − x²)y″ − 2xy′ + 4y = 0

Tekil noktalar 0, 1, −1'dir; üçü de düzgün tekildir. 0 için limitler −2 ve 4; ±1 için 1 ve 0'dır.

### 6. 2x²y″ + 3xy′ − y = 0

İndis denklemi 2r² + r − 1 = 0; çözüm C₁√x + C₂/x.

### 7. x²y″ − 2xy′ + 2y = 2x ln x

Homojen çözüm C₁x² + C₂x. Parametrelerin değişimiyle kaynakta verilen sonuç:

y = K₁x² + K₂x − x(ln x)² − 2x ln x.

*Not: Sonuç doğrudur; ancak ara integral satırları eksik/hatalıdır. ∫2 ln x/x² dx = −2(ln x + 1)/x + C ve ∫−2 ln x/x dx = −(ln x)² + C olmalıdır. İlk integraldeki ek −2x terimi son çözümde homojen sabite katılır.*

### 8. x²y″ + xy′ + (x − 2)y = 0

p₀ = 1, q₀ = −2; indis kökleri ±√2. Katsayılar aₙ = −aₙ₋₁/[(r + n)² − 2] ile bulunur. Her iki r için y_r = xʳ[1 − x/(1 + 2r) + x²/((1 + 2r)(4 + 4r)) + …].

*Not: Föyde limit hesabından sonraki cümlede q₀ = 0 yazıyor; aynı sayfadaki limit ve kullanılan indis denklemi q₀ = −2 olduğunu gösteriyor.*

### 9. x²y″ + xy′ + x²y = 0

r² = 0 katlı indis kökü, a₁ = 0, aₙ = −aₙ₋₂/(r + n)².

y₁ = 1 − x²/4 + x⁴/64 − x⁶/2304 + … = J₀(x).

İkinci çözüm, r'ye göre türevle y₂ = y₁ ln x + x²/4 − 3x⁴/128 + … biçiminde elde ediliyor. Genel çözüm C₁y₁ + C₂y₂'dir.

Yineleme bağıntılarının ilk katsayıları ve sonlanan polinom çözümleri denklemde yerine koyularak kontrol edildi.
