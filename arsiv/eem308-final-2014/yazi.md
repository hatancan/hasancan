---
baslik: EEM308 Sinyaller ve Sistemler II: Haziran 2014 Sınavı (Final) Soruları ve Çözümleri
ozet: EEM308 Sinyaller ve Sistemler II dersinin Haziran 2014 sınav soruları ve bir öğrencinin puanlanmış çözümleri: iki taraflı z-dönüşümü, G(s) = H(1/s) dönüşümü ve süzgeç tipi, ideal bant geçiren süzgecin dürtü yanıtı, Bode genlik diyagramı, örnekleme hızını değiştirme ve tek taraflı z-dönüşümünde öteleme.
---

Bu yazı, Başkent Üniversitesi **EEM 308 Sinyaller ve Sistemler II** dersinin **Yrd. Doç. Dr. Selda Güney** tarafından hazırlanan, 12 Haziran 2014 tarihli fotoğraflarla saklanmış beş soruluk sınavını (dönem sonu sınavı olduğu anlaşılıyor) ve bir öğrencinin **puanlanmış çözüm kâğıdını** aktarıyor. Çözüm sayfalarında ad veya numara görünmüyor. Daire içindeki kırmızı sayılar alınan puanları gösteriyor. Sorular ve çözümler metin olarak aktarıldı; fotoğrafların kendisi arşivde saklanıyor, yayınlanmıyor.

## Sorular

**1.** Aşağıda verilen bilgiler ışığında X(z) ve x[n]'i bulunuz.

1. x[n] çift yanlıdır ve kararlıdır.
1. X(z)'in iki kutbundan biri z = 1/8'de bulunmaktadır.
1. X(1) = 19/7
1. x[−3] = −3/8, x[−5] = −3/32

**2.** H(s) ve G(s) arasındaki ilişki G(s) = H(1/s) ise:

- a) H(s) = 1/(s + ½) için |H(jω)| ve |G(jω)|'yı hesaplayarak çiziniz ve transfer fonksiyonu için süzgeç tipini belirleyiniz.
- b) Cebirsel hesaplanan genlik fonksiyonlarında ω = 2 için elde edilen değer ile kutup-sıfır diyagramından vektörel hesaplama ile elde edilen değerlerin aynı olduğunu kanıtlayınız.
- c) H(s) ve G(s) ile ilişkili doğrusal sabit katsayılı diferansiyel denklemi belirleyiniz.

**3.** İdeal bir bant geçiren süzgecin frekans tepkisi H(jω) şekilde verildiği gibidir: ω₀ − W/2 < |ω| < ω₀ + W/2 aralığında genliği 1, diğer frekanslarda 0.

- a) Bu süzgecin h(t) dürtü tepkisi nedir? (İpucu: ideal alçak geçiren bir süzgecin dürtü tepkisi h_c(t) = sin(ω_c t)/(πt))
- b) İdeal bant geçiren süzgeç, birinci dereceden alçak geçiren ve birinci dereceden yüksek geçiren süzgecin seri bağlanmasıyla elde edilebilir. H₁ = 10³/(10³ + jω) ve H₂ = jω/(100 + jω) transfer fonksiyonlarının seri bağlanmasıyla elde edilen transfer fonksiyonunun Bode genlik diyagramını çiziniz.

**4.** Gerçel değerli ayrık zaman sinyali x[n]'in, 3π/14 ≤ |ω| ≤ π aralığında değeri sıfır olan bir Fourier dönüşümü X(e^{jω}) mevcuttur. Fourier dönüşümünün bir periyodunun sıfırdan farklı olan kısmını |ω| ≤ π aralığını kapsayacak şekle getirmek için x[n] nasıl bir sistemden geçmelidir? Blok şemayla açıklayınız; sistemin her adımındaki işaretin Fourier dönüşümünün şeklini de çizerek gösteriniz.

**5.** Eğer X(z), x[n]'nin tek taraflı z dönüşümünü gösteriyorsa, aşağıdakilerin tek taraflı z dönüşümlerini X(z) cinsinden bulunuz: a) x[n + 3], b) x[n − 3].

## Öğrenci çözümü

### Soru 1: İki taraflı z-dönüşümü

İki taraflı ve kararlı dizi için biçim: x[n] = A(1/8)ⁿ u[n] − B·Cⁿ u[−n − 1].

- x[−3] = −B·C⁻³ = −3/8 ⇒ B = (3/8)C³
- x[−5] = −B·C⁻⁵ = −3/32 ⇒ (3/8)C⁻² = 3/32 ⇒ C² = 4 ⇒ **C = 2**, **B = 3**
- X(z) = A/(1 − ⅛z⁻¹) + 3/(1 − 2z⁻¹) ⇒ X(1) = 8A/7 − 3 = 19/7 ⇒ 8A/7 = 40/7 ⇒ **A = 5**

**X(z) = 5/(1 − ⅛z⁻¹) + 3/(1 − 2z⁻¹)**, 1/8 < |z| < 2

**x[n] = 5(1/8)ⁿ u[n] − 3·2ⁿ u[−n − 1]**

### Soru 2: G(s) = H(1/s)

**a)** G(s) = H(1/s) = 1/(1/s + ½) = 2s/(s + 2).

- H(jω) = 1/(jω + ½), |H(jω)| = 1/√(ω² + ¼): **alçak geçiren** (kutup −½'de).
- G(jω) = 2jω/(jω + 2), |G(jω)| = 2|ω|/√(ω² + 4): **yüksek geçiren** (sıfır orijinde, kutup −2'de).

**b)** ω = 2 için cebirsel hesap: |H(j2)| = 1/√(4 + ¼) ≈ 0,485, |G(j2)| = 4/√(4 + 4) ≈ 1,414. Kutup-sıfır diyagramında j2 noktasına çizilen vektörlerle: H için kutup vektörü |r| = √((½)² + 4), K = 1 ⇒ |H(j2)| = 1/|r| ≈ 0,485; G için sıfır vektörü |s| = 2, kutup vektörü |r| = √(4 + 4), K = 2 ⇒ |G(j2)| = 2·2/√8 ≈ 1,414. İki yöntem aynı sonucu veriyor.

**c)** Diferansiyel denklemler:

- H(s) = Y(s)/X(s) = 1/(s + ½) ⇒ **dy/dt + ½y(t) = x(t)**
- G(s) = 2s/(s + 2) ⇒ **dy/dt + 2y(t) = 2 dx/dt**

### Soru 3: Bant geçiren süzgeç

**a)** Bant geçiren süzgeç, kesim frekansı ω_c = W/2 olan alçak geçiren süzgecin ±ω₀'a kaydırılmasıdır: H(jω) = H₁(j(ω − ω₀)) + H₁(j(ω + ω₀)), h₁(t) = sin(Wt/2)/(πt). Çözümde sonuç h(t) = [sin(Wt/2)/(πt)]·cos ω₀t olarak verilmiş (10 puan).

*Not: Frekansta ±ω₀ kaydırma, zamanda e^{jω₀t} + e^{−jω₀t} = 2cos ω₀t ile çarpmaya karşılık geldiğinden doğrusu h(t) = 2 sin(Wt/2) cos(ω₀t)/(πt)'dir; çözümde 2 çarpanı eksik.*

**b)** H₁(jω) = 1/(1 + jω/10³), H₂(jω) = (jω/10²)/(1 + jω/10²). H = H₁H₂ için:

20 log|H(jω)| = −20 log|1 + jω/10³| − 40 + 20 log|ω| − 20 log|1 + jω/10²|

Kırılma frekansları ω₁ = 10³ ve ω₂ = 10². Asimptotik değerler:

| ω (rad/s) | 10 | 10² | 10³ | 10⁴ | 10⁵ | 10⁶ |
|---|---|---|---|---|---|---|
| Sabit | −40 | −40 | −40 | −40 | −40 | −40 |
| LP kutbu (10³) | 0 | 0 | 0 | −20 | −40 | −60 |
| Orijindeki sıfır | 20 | 40 | 60 | 80 | 100 | 120 |
| HP kutbu (10²) | 0 | 0 | −20 | −40 | −60 | −80 |
| **Toplam (dB)** | −20 | 0 | 0 | −20 | −40 | −60 |

Genlik 10²–10³ rad/s arasında 0 dB, altında +20 dB/dekad yükselen, üstünde −20 dB/dekad düşen bir eğri.

*Not: Çözümün kenarına "bant durduran süzgeç" yazılmış; tabloda da görüldüğü gibi sistem 100–1000 rad/s bandını geçiren bir **bant geçiren** süzgeçtir.*

### Soru 4: Spektrumu |ω| ≤ π'ye yaymak

X(e^{jω})'nın bant genişliği 3π/14; bunu π'ye çıkarmak için örnekleme hızı 14/3 oranında azaltılmalı. Oran tam sayı olmadığından önce 3 ile ara değerleme, sonra 14 ile ondalıklama yapılıyor:

x[n] → **sıfır yerleştirme** → w[n] → **alçak geçiren süzgeç** (kesim ±π/14) → p[n] → **ondalıklama** → y[n]

- Sıfır yerleştirme: w[n] = x[n/3] (n = 0, ±3, ±6, …), aksi takdirde 0. W(e^{jω}) = X(e^{j3ω}): ana bant ±π/14'e daralır, ±2π/3 çevresinde (25π/42–31π/42) kopyalar oluşur.
- Süzgeç kopyaları atar; P(e^{jω}) yalnız |ω| ≤ π/14 bandını içerir.
- Ondalıklama: y[n] = p[14n]; spektrum 14 kat genişler ve Y(e^{jω}) tüm (−π, π) aralığını kaplar.

*Not: Çözümde w[n] = x[n/2] yazılmış; n = 0, ±3, ±6 örnekleriyle tutarlı olan ifade x[n/3]'tür.*

### Soru 5: Tek taraflı z-dönüşümünde öteleme

**a)** y[n] = x[n + 3]:

Y(z) = Σₙ₌₀^∞ x[n + 3] z⁻ⁿ = z³ Σₙ₌₃^∞ x[n] z⁻ⁿ

**Y(z) = z³X(z) − x[0]z³ − x[1]z² − x[2]z**

**b)** y[n] = x[n − 3]:

Y(z) = Σₙ₌₀^∞ x[n − 3] z⁻ⁿ = z⁻³X(z) + (n = 0, 1, 2 için gelen x[−3], x[−2], x[−1] terimleri)

**Y(z) = z⁻³X(z) + x[−1]z⁻² + x[−2]z⁻¹ + x[−3]**

## Çözüm sayfaları

