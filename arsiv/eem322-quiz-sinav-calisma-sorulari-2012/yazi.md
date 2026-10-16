---
baslik: EEM322 Denetim Sistemleri: Sınav Tipi Çalışma Soruları ve Defter Çözümleri (2012)
ozet: EEM322 Denetim Sistemleri için beş soruluk sınav tipi çalışma seti ve bir öğrencinin defter çözümleri: denetlenebilirlik ve durum denkleminin çözümü, kök yer eğrisi, hata sabitleri ve kalıcı durum hatası, kazanç ve faz payı, tam Nyquist çizimi.
---

Bu yazı, EEM322 Denetim Sistemleri klasöründeki "denetim sınav" alt klasöründe duran sekiz defter sayfasının metne aktarılmış hâlidir. Sayfalar 30 Mayıs 2012'de fotoğraflanmış: ilk sayfada sınav tipi beş soru, sonraki sayfalarda bir öğrencinin bu sorulara kurşun kalemle yazdığı çözümler var. **Fotoğraflanmış sayfalardan metne aktarıldı**; fotoğraflar yayınlanmadı. Çözümlerde birkaç hata var; aşağıda notlarla belirtildi.

## Sorular

1. ẋ(t) = [−1 1; 0 0]x(t) + [1; 0]u(t), başlangıç koşulu x(0) = [7; 2] (fotoğrafta ilk eleman zor okunuyor). (a) Sistem denetlenebilir mi? (b) Durum denkleminin tam çözümünü bulun (t ≥ 0).
1. G(s) = K(s + 2)/[(s + 1)(s − 3)]. Kapalı döngü kararlılığını irdeleyin; kritik K değerini ve kritik noktaları bulun. Asimptotların merkezi (centroid) ve açıları için kullanılan formülleri verin; kök yer eğrisi çiziminde olası ayrılma noktalarını hesaplayın; 0 ≤ K < ∞ aralığı için tüm ayrıntılarıyla kök yer eğrisini çizin.
1. G(s) = K/[s(s + 1)(s + 4)]: K = 10 için hata sabitlerini (Kp, Kv, Ka) ve birim basamak, rampa ve parabol girişleri için ess'yi bulun.
1. Aynı sistemin K = 10 için kazanç kesim frekansı ωg = 1.38 rad/s'dir. Faz kesim frekansı ωp'yi, kazanç ve evre paylarını (gm, pm) bulun; gm ve pm'ye göre kapalı döngü kararlılığını tartışın.
1. K = 10 için tam Nyquist çizimini elde edin.

## Soru 1: Denetlenebilirlik ve durum denkleminin çözümü

1. (a) Denetlenebilirlik matrisi U = [B AB] = [1 −1; 0 0] ⇒ det U = 0, rank U = 1 ⇒ sistem **denetlenemez**.
1. (b) (sI − A)⁻¹ = [s + 1 −1; 0 s]⁻¹ = (1/(s(s + 1)))·[s 1; 0 s + 1] = [1/(s + 1) 1/(s(s + 1)); 0 1/s], burada 1/(s(s + 1)) = 1/s − 1/(s + 1).
1. Durum geçiş matrisi: **e^(At) = [e^(−t) 1 − e^(−t); 0 1]**.
1. X(s) = (sI − A)⁻¹x(0) + (sI − A)⁻¹B·U(s) = (1/(s(s + 1)))·([s 1; 0 s + 1][7; 2] + [s 1; 0 s + 1][1; 0]·(1/s)).

*Not: Defterde çözüm bu satırda kalmış. Devam ettirilirse X₁(s) = (7s + 3)/[s(s + 1)] = 3/s + 4/(s + 1), X₂(s) = 2/s; yani x₁(t) = 3 + 4e^(−t), x₂(t) = 2 (t ≥ 0) bulunur.*

## Soru 2: Kök yer eğrisi

1. T(s) = G/(1 + G) = K(s + 2)/[s² − 2s − 3 + K(s + 2)].
1. Açık döngü kutupları −1 ve +3 (n = 2), sıfırı −2 (m = 1). Asimptot sayısı n − m = 1; açısı θk = (2k + 1)π/(n − m) = 180°; merkezi σ = (−1 + 3 − (−2))/1 = 4.
1. Δ(s) = s² − 2s − 3 + K(s + 2) = s² + (K − 2)s + 2K − 3. Routh tablosu: s²: 1, 2K − 3; s¹: K − 2; s⁰: 2K − 3. Defterde kritik kazanç Kkr = 3/2 ve s(−2 + 3/2) = 0 ⇒ s = 0 yazılmış.
1. Ayrılma noktaları: K = −(s² − 2s − 3)/(s + 2); dK/ds = 0 ⇒ (2s − 2)(s + 2) − (s² − 2s − 3) = 0 ⇒ s² + 4s − 1 = 0 ⇒ kökler −4.24 ve 0.24.
1. Kök yer eğrisi: +3 ve −1'deki kutuplardan çıkan kollar 0.24'te gerçek eksenden ayrılıp sanal ekseni keserek bir çember çiziyor ve −4.24'te gerçek eksene dönüyor; biri −2'deki sıfıra, diğeri −∞'a gidiyor.

*Not: Routh tablosunun iki koşulu birlikte sağlanmalıdır: K − 2 > 0 ve 2K − 3 > 0, yani kapalı döngü **K > 2** için kararlıdır. Kritik kazanç 3/2 değil **Kc = 2**'dir; o zaman yardımcı denklem s² + 1 = 0 ve kritik noktalar s = ±j olur (eğri sanal ekseni burada keser). K = 3/2'de kutuplardan biri s = 0'dadır ama diğeri hâlâ sağ yarı düzlemdedir (s = 0.5).*

## Soru 3: Hata sabitleri ve kalıcı durum hatası

G(s) = 10/[s(s + 1)(s + 4)] (tip 1):

- Kp = G(0) = ∞, Kv = lim(s→0) sG(s) = 10/4, Ka = lim(s→0) s²G(s) = 0.
- ess = lim(s→0) sR(s)W(s), W(s) = 1/(1 + G(s)) = (s³ + 5s² + 4s)/(s³ + 5s² + 4s + 10).
- R(s) = 1/s ⇒ ess = 0; R(s) = 1/s² ⇒ ess = 4/10; R(s) = 1/s³ ⇒ ess = ∞.

## Soru 4: Kazanç ve faz payı

G(jω) = 10/[jω(jω + 1)(jω + 4)] gerçel ve sanal kısımlarına ayrılmış; sanal kısmı sıfır yapan frekans defterde ω(−ω² + 40) = 0 ⇒ ωp = √40 ≈ 6.4 rad/s olarak bulunmuş. Kazanç payı gm = 1/|G(jωp)| ve 20 log ile dB'ye çevrilmesi, faz payı pm = 180° + ∠G(jωg) = 180° − 90° − tan⁻¹(1.38) − tan⁻¹(1.38/4) biçiminde yazılmış ama sayısal sonuçlar bitirilmemiş.

*Not: Payda açılırken hata yapılmış. G(jω)'nın sanal kısmı ω(4 − ω²) ile orantılıdır, yani **ωp = 2 rad/s**'dir. |G(j2)| = 10/(2·√5·√20) = 0.5 ⇒ **gm = 2 (≈ 6 dB)**. ωg = 1.38'de pm = 90° − 54.1° − 19.0° ≈ **17°**. Her iki pay da pozitif, kapalı döngü kararlıdır (s³ + 5s² + 4s + K için kritik kazanç 20).*

## Soru 5: Nyquist çizimi

1. ω kısmı (s = jω): |G(jω)| = 10/(ω√(ω² + 1)√(ω² + 16)), ∠G(jω) = −90° − tan⁻¹ω − tan⁻¹(ω/4). ω → 0'da ∞∠−90°, ω → ∞'da 0∠−270°.
1. Sonsuz yarıçaplı yay (s = Re^(jψ)): G = 10/(R³e^(j3ψ)) → 0∠−3ψ. Orijindeki kutbun çevresinden dolanan küçük yarım çember (s → 0) G'nin sonsuz yarıçaplı bir yaya dönüşmesini sağlar; s ve G açıları tabloda 90° ↔ −270°, 0° ↔ 0°, −90° ↔ 270° olarak eşleştirilmiş.
1. Defterde çizilen kapalı eğri −1 noktasını kuşatacak biçimde çizilmiş ve N = Z − P ⇒ 2 = Z − 0 ⇒ Z = 2, "kararsız" sonucuna varılmış.

*Not: Bu sonuç Soru 3–4 ile çelişir. K = 10 için eğri negatif gerçek ekseni ω = 2 rad/s'de −0.5 noktasında keser (gm = 2); −1 noktası kuşatılmaz, N = 0, P = 0 ⇒ Z = 0, kapalı döngü **kararlıdır**. Z = 2 durumu ancak K > 20 için ortaya çıkar.*
