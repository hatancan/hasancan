---
baslik: EEM441 Haberleşme I: 2013 yaz okulu EEM 442 Haberleşme II ara sınavı (5 Ağustos 2013) ve çözümleri
ozet: EEM 442 Haberleşme II yaz okulu ara sınavı: uyumlu süzgeç, impulse gürültülü ikili sinyalleşme, nicemleme SNR değeri ve 16-PAM telemetri tasarımı; el yazısı çözümlerle.
---

Bu belge EEM 442 Haberleşme II dersine aittir; EEM 441 klasöründe bulunduğu için burada yayımlanmıştır. Başkent Üniversitesi EEM 442 Haberleşme II yaz okulu ara sınavı (5 Ağustos 2013, süre 110 dakika) ve el yazısı çözümleri. Sınav kâğıdı ve çözümler fotoğraflanmış sayfalardan metne aktarıldı; fotoğraflar yayınlanmamıştır. Bu nedenle indirilebilir orijinal dosya yoktur. Kişisel bilgiler (öğrenci numarası, ad) çıkarılmıştır.

## Sorular

1. Verilen s(t) sinyalini göz önüne alın (s(t) = 1: 0–3T arası; −1: 3T–4T; +1: 4T–5T; −1: 5T–7T). a) Uyumlu (matched) süzgeç girişindeki s(t) sinyali için iletim süzgecinin karakteristik fonksiyonu g(t) cinsinden gerekli ifadeyi türetin; g(t) vurumunun enerjisini hesaplayın. b) s(t) için uyumlu süzgecin impulse yanıtını hesaplayın; impulse yanıtı ve t = nT'de örneklenmiş uyumlu süzgecin çıkışını zamanın fonksiyonu olarak çizin. c) Uyumlu süzgecin çıkışının tepe değerini hesaplayın.
2. Bazı anahtarlama devreleri, ortalama gücü σ² ve üstel pdf'i p_n(n) = (1/√(2σ²)) e^(−√2|n|/σ) olan filtrelenmiş beyaz gürültü olarak modellenen impulse gürültüsü üretirler. a) Hata olasılığı P_e için A, σ cinsinden impulse gürültülü iki kutuplu sinyalleşme için bir ifade türetin. b) P_e ≤ 0,001 için Gauss gürültü ile impulse gürültüsünün etkisini karşılaştırın.
3. Bir sayısal iletişim sisteminde ±2 V aralığında tekdüze dağılıma sahip rastgele bir sinyal 256 seviyeli tekdüze nicemleyiciden geçirilmektedir. Nicemleyicinin çıkışındaki sinyal gücünün nicemleme gürültü gücüne oranını hesaplayın.
4. Uydu sistemine ait telemetri devresinde M = 16 sembol seviyesine sahip 16-PAM iletim sistemi kullanılmaktadır. Telemetri devresinin özellikleri: i) maksimum ortalama güç 10 dBm, ii) maksimum anlık tepe güç 30 dBm, iii) maksimum veri hızı 12 M sembol/s. a) 16 iletim seviyesi eşit olasılığa sahip olduğuna göre kullanılabilecek iletim seviyeleri arasındaki en büyük voltaj aralığı nedir? b) En büyük voltaj aralığı telemetri sisteminin tepe veya ortalama güç gereksinimleri tarafından mı sınırlandırılmaktadır? c) Ulaşılabilecek toplam bit iletim hızı nedir? Sistemin bit hızı ortalama güce bağlı mıdır? d) N₀ = 10⁻¹² W/Hz için sembol ve bit olasılıklarını hesaplayın.

Sınavla birlikte verilen formül sayfasında: P_b = p₁Q((A − λ)/σ) + (1 − p₁)Q((A + λ)/σ); Q(3,09023) = 10⁻³, Q(√20) = 3,87×10⁻⁶; B_T = (R_s/2)(1 + α); SNR₀ = 3×2^(2R)/α; ikili ilişkili sinyalleşmede P_b = Q(√(E_s(1 − ρ)/N₀)); M-PSK için P_s = 2Q(√(2E_s/N₀) sin(π/M)); (1/(M/2)) Σ(2i − 1)² = (M² − 1)/3; M-PAM için P_E(M) = [2(M − 1)/M] Q(√(6E_s,av/((M² − 1)N₀))) bulunur.

## Çözüm 1: Uyumlu süzgeç

a) s(t) = Σ_{k=0}^{6} a_k g(t − kT); a₀ = a₁ = a₂ = a₄ = 1, a₃ = a₅ = a₆ = −1. Temel vurum g(t) T süreli, genliği 1 olan dikdörtgendir; enerjisi E_g = ∫₀ᵀ g²(t) dt = T. Uyumlu süzgeç çıkışında g'nin otokorelasyonu, yani 0'dan 2T'ye uzanan ve T'de tepe değeri √E_g olan üçgen elde edilir.

b) h_opt(t) = (1/√T) g(T − t). T anlarında örneklenmiş çıkış, a_k dizisiyle ağırlıklandırılmış √E_g yüksekliğinde çubuklardır: T, 2T, 3T'de +√E_g, 4T'de −√E_g, 5T'de +√E_g, 6T ve 7T'de −√E_g.

c) Çıkışın tepe değeri √E_g = √T.

## Çözüm 2: İmpulse gürültüsü

Koşullu yoğunluklar P_Y(y|0) (ortalama −A/2) ve P_Y(y|1) (ortalama +A/2) simetriktir; en iyi eşik λ_opt = 0'dır.

a) P_e = P_e0 = ∫₀^∞ p_n(y + A/2) dy = (1/√(2σ²)) ∫₀^∞ e^(−√2 (y + A/2)/σ) dy = ½ exp(−A/√(2σ²)).

b) P_e ≤ 10⁻³ için A/√(2σ²) ≥ ln(1/(2×10⁻³)) ⇒ A ≥ 8,86σ (impulse gürültüsü). Gauss gürültüsünde P_e = Q(A/2σ) ≤ 10⁻³ ⇒ A ≥ 6,2σ. Aynı P_e için impulse gürültüsü daha fazla sinyal gücü gerektirir.

*Not: ln(500) = 6,215 ve √2 × 6,215 = 8,79 olduğundan kendi hesabımız A ≥ 8,79σ verir; kâğıttaki 8,86σ yakın bir yuvarlamadır. Gauss için 3,09 × 2 = 6,18σ.*

## Çözüm 3: Nicemleme SNR'si

Adım büyüklüğü Δ = 2m_max/L = 2×2/256 = 2/128 = 1/64. Nicemleme gürültü gücü σ_q² = Δ²/12 = 1/(12 × 64²). [−2, 2] aralığında tekdüze sinyalin gücü P = ∫ x² (1/4) dx = (1/4)(x³/3) |₋₂² = (1/12)(2×2³) = 4/3. Buradan

SNR₀ = P/σ_q² = (4/3)/(Δ²/12) = 16/Δ² = 16 × 64² = 2¹⁶ = (256)² = 65536 (48,16 dB).

## Çözüm 4: 16-PAM telemetri

Ortalama güç en çok 10 dBm = 10 mW, tepe güç en çok 30 dBm = 1 W (50 Ω'a); sembol hızı R_s ≤ 12 Msembol/s, dolayısıyla T_s ≥ 1/12 µs. Seviyeler 0, a, 3a, 5a, …, 15a (a = √E₀) alınır.

a) E_av = (1/(M/2)) Σ a²(2i − 1)² = a² (M² − 1)/3 = a² × 255/3 = 85a²; E_tepe = (15a)² = 225a².
Ortalama güç sınırı: P_av = E_av/T = 85a²/T ≤ 10 mW ⇒ a ≤ √(P_av T/85) = 3,13 µV. Tepe güç sınırı: P_tepe = 225a²/T ≤ 1 W ⇒ a ≤ √(P_tepe T/225) = 1,92×10⁻⁵ = 19,25 µV. En büyük voltaj aralığı 2a = 6,16 µV'tur (kâğıtta bu değer yazılıdır).

b) En büyük voltaj aralığı ortalama güç gereksinimi tarafından sınırlanır (a'nın ortalama güç sınırı daha küçüktür).

c) M = 16 ⇒ k = 4 bit/sembol; R_b = k R_s = 4 × 12 = 48 Mbit/s. Bit hızı ortalama güce bağlıdır: P_av = E_av/T = E_av R_b/log₂M.

d) N₀ = 10⁻¹² W/Hz için E_av/N₀ = 10 mW × T/N₀ = 10⁻² × (1/12)10⁻⁶ / 10⁻¹² = 10⁴/12 = 2500/3. Sembol hatası P_E(16) = (2×15/16) Q(√(6/255 × 2500/3)) = (15/8) Q(√19,61) ≈ 8,9×10⁻⁶. Bit hata olasılığı P_b ≈ P_E/4 = 2,23×10⁻⁶.

*Not: 2a, a = 3,13 µV ile 6,26 µV'tur (kâğıttaki 6,16 µV bir yazım kaymasıdır). Ayrıca P_av T/85 hesabında T = (1/12) µs alınmıştır; sonuçlar bu varsayımla uyumludur.*
