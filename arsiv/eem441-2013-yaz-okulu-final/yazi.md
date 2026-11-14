---
baslik: EEM441 Haberleşme I: 2013 yaz okulu final sınavı (14 Ağustos 2013) ve çözümleri
ozet: Başkent Üniversitesi EEM 441 yaz okulu finali: FDM kanal filtresi, FM ton spektrumu ve fazör, VSB zarf ve faz, AM zarf çizimleri; el yazısı çözümlerle.
---

Başkent Üniversitesi EEM 441 Haberleşme Sistemleri I dersinin 14 Ağustos 2013 tarihli yaz okulu final sınavı (süre 110 dakika) ve el yazısı çözümleri. Sınav kâğıdı ve çözümler fotoğraflanmış sayfalardan metne aktarıldı; fotoğraflar yayınlanmamıştır. Bu nedenle indirilebilir orijinal dosya yoktur. Kişisel bilgiler (öğrenci numarası, ad) çıkarılmıştır. Aynı klasördeki üç ek fotoğraf, aynı sayfaların tekrarlarıdır.

## Sorular

1. Bir telefon santralında ses kanalları alıcıda transfer fonksiyonu |H(f)| = 1/√(1 + [2(f − f₀)/B]^(2n)) olan bant geçiren filtrelerle birbirinden ayrılmıştır. Tabanbant ses sinyalinin 300 < |f| < 3300 Hz dışındaki bileşenlerinin ihmal edildiğini kabul ederek grup spektrumundaki üç komşu kanalın spektrumunu çizin. İstenen geçirgenlik bandının dışında |H(f)| ≤ 0,1 alarak B, f₀ ve n'yi hesaplayın.
2. Modülasyon indeksi β = 2 ve bilgi sinyalinin en yüksek bileşeni f_m = 200 Hz olan ton modüleli FM sinyali, merkez frekansı f_c olan 750 Hz bant genişliğine sahip BPF'ye uygulanmaktadır. FM sinyalinin frekans spektrumunu ve fazör şemasını çizin; çıkış sinyalinin zarfını hesaplayın ve grafiğini çizin.
3. Birim genlikli görüntü sinyalleri DSB-SC modülasyonu kullanılarak iletilmektedir. Ton modüleli DSB-SC sinyal için fazör şemasını çizin. Alt yan bandın genişliğinin yarıya düşürülmesi durumunda DSB-SC modüleli sinyalin A(t) zarfını ve φ(t) faz açısını fazör şemasını çizerek hesaplayın.
4. a) f_m ≪ f_c alınarak m(t) = cos(2π f_m t) u(t) bilgi sinyali ile genlik modülasyonu yapılmaktadır. Modülasyonun DSB ve μ < 1 ile μ > 1 değerlerine sahip AM olması durumunda modüleli sinyaller üzerindeki zarfları çizin; genlik değerlerini belirtin. b) Aynı soruyu T ≫ 1/f_c alarak m(t) = 0,5 u(t) − 1,5 u(t − T) bilgi sinyali için tekrarlayın.

Sınavla birlikte Bessel fonksiyonları formül sayfası da verilmiştir (J_n(β) grafikleri; J_n(β) = (−1)ⁿ J₋ₙ(β); β → 0 için J_n ≈ βⁿ/(2ⁿ n!); ΣJ_n² = 1; FM s(t) = A_c Σ J_n(β) cos[2π(f_c + n f_m)t]; SSB s(t) = (A_c/2) m(t) cos ω_c t ∓ (A_c/2) m̂(t) sin ω_c t).

## Çözüm 1: Kanal filtresi

Her kanal tek yan banttır (SSB alt taşıyıcı): ses bandı 300–3300 Hz, taşıyıcı çizgisi ise bandın altındadır. Şekilde komşu alt taşıyıcılar f_i − 4, f_i, f_i + 4 kHz'tedir (4 kHz aralık); her kanalın 3 kHz'lik bandının altında 0,3 kHz ve ikinci kanalla arasında 0,7 kHz'lik boşluk bırakılmıştır (f_i − 3,3 kHz ile f_i − 0,3 kHz arasında bant).

f_i i. alt taşıyıcı olsun. B = 3 kHz alınır ve filtre merkezi f₀ = f_i − 0,3 kHz − B/2 = f_i − 1,8 kHz olur. İstenen: |f − f₀| ≥ B/2 + 1 kHz = 1,5 + 1 = 2,5 kHz için |H(f)|² ≤ 0,01.

|H|² = 1/(1 + [2(2,5)/3]^(2n)) ≤ 0,01 ⇒ (5/3)^(2n) ≥ 99 ⇒ 2n log₁₀(5/3) ≥ log₁₀ 99. log₁₀(5/3) = 0,222 olduğundan n × 0,444 ≥ 2 ve n ≥ 4,5, yani n = 5.

Sonuç: B = 3 kHz, f₀ = f_i − 1,8 kHz, n = 5.

## Çözüm 2: Tek tonlu FM, BPF çıkışı

Kâğıttaki çözüm, ton frekansı f_m = 4 kHz ve β = 2 değerleriyle (J₀(2) ≈ 0,22, J₁(2) ≈ 0,58) çalışılmıştır; BPF taşıyıcı ile ilk yan bantları geçirir (B ≈ 8500 Hz).

- Spektrum: f_c'de 0,22 A_c; f_c + 4000 Hz'de +0,58 A_c; f_c − 4000 Hz'de −0,58 A_c.
- Fazör şeması: 0,22 A_c yatay taşıyıcı fazörü; ona ±ω_m t ile dönen iki 0,58 A_c fazörü eklenir. Yan bant fazörleri zıt yönlü olduğundan toplamları dikey bileşenli 2 × 0,58 = 1,16 A_c'dir.
- Zarf: A_min = 0,22 A_c; A_max = √(0,22² + 1,16²) A_c ≈ 1,18 A_c. A(t), periyodu 1/f_m olan bir eğri olup 0,22 A_c ile 1,18 A_c arasında değişir.

*Not: Çözüm kâğıdındaki sayısal değerler (f_m = 4 kHz, B = 8500 Hz) soru kâğıdındakilerle (f_m = 200 Hz, BPF 750 Hz) uyuşmaz; çözüm başka bir değer takımıyla yazılmıştır, yöntem aynıdır.*

## Çözüm 3: DSB-SC ve alt yan bandı zayıflatılmış sinyal (VSB)

Ton modüleli DSB-SC: x_c(t) = (A_c/2) cos(ω_c − ω_m)t + (A_c/2) cos(ω_c + ω_m)t. Fazör şemasında iki A_c/2 fazörü ±ω_m t ile zıt yönde döner; bileşke yatay ekseni üzerinde A(t) = A_c cos ω_m t'dir.

Alt yan bandın yarıya (genliği A_c/4'e) düşürülmesi: alt yan bant fazörü A_c/4, üst yan bant fazörü A_c/2.

- V_I = (A_c/2) cos ω_m t + (A_c/4) cos ω_m t = (3/4) A_c cos ω_m t
- V_Q = (A_c/2) sin ω_m t − (A_c/4) sin ω_m t = (A_c/4) sin ω_m t
- A(t) = [(3/4 A_c cos ω_m t)² + (A_c/4 sin ω_m t)²]^½ = (A_c/4) √(9cos²ω_m t + sin²ω_m t) = (A_c/4) √(8cos²ω_m t + 1) = (A_c/4) √(5 + 4cos 2ω_m t)
- φ(t) = arctan[(A_c/4) sin ω_m t / (3A_c/4 cos ω_m t)] = arctan(tan ω_m t / 3)

## Çözüm 4: AM ve DSB zarfları

a) m(t) = cos(2π f_m t) u(t): t = 0'da 1 değerine sıçrayan, sonra sinüs gibi salınan bir işaret.

- DSB: taşıyıcının genliği m(t) ile çarpılır; t = 0'da A_c'den başlar, zarf |cos| biçimindedir ve m(t) işaret değiştirdikçe taşıyıcı faz tersler.
- AM, μ < 1: zarf A_c[1 + μ m(t)]; t < 0'da genlik A_c, t > 0'da A_c(1 ± μ) arasında değişir; zarf hiç sıfıra inmez, faz tersi olmaz.
- AM, μ > 1: zarf negatife geçer; zarf sıfır kesişlerinde faz tersi (aşırı modülasyon) oluşur ve zarf bozulur.

b) m(t) = 0,5 u(t) − 1,5 u(t − T): 0 < t < T aralığında 0,5, t > T'de −1 (0,5 − 1,5).

- DSB: 0–T arasında genlik 0,5 A_c, T'den sonra A_c (ve faz 180° döner).
- AM, μ < 1: 0–T arasında A_c(1 + 0,5μ), T'den sonra A_c(1 − μ) (zarf küçülür, faz aynıdır); t < 0'da A_c.
- AM, μ > 1: T'den sonra 1 − μ negatif olduğundan taşıyıcı faz tersler, zarf |1 − μ| A_c'dir; 0–T arasında A_c(1 + 0,5μ).
