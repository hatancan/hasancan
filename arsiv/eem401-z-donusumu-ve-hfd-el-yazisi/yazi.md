---
baslik: EEM401 Sayısal Sinyal İşleme: z Dönüşümü, Yakınsama Bölgesi, Ters z Dönüşümü ve Zamanda Seyreltmeli HFD (Ders Defteri Notları)
ozet: EEM401 ders defterimden 27 Kasım 2014 notları: z dönüşümünün tanımı ve yakınsama bölgesi (ROC), kararlılık ve nedensellik, ters z dönüşümü örnekleri, zamanda seyreltmeli (DIT) hızlı Fourier dönüşümü algoritması ve 8 noktalı örnek.
---

Bu yazı, 2014–2015 güz yarıyılında **EEM401 Sayısal Sinyal İşleme** (Yrd. Doç. Dr. Selda Güney) dersinde defterime aldığım ve 27 Kasım 2014'te fotoğrafladığım 16 sayfalık el yazısı notun metne aktarılmış hâlidir. Fotoğraflar yayımlanmamış, içerik yeniden yazılmıştır. Dersin sunumları için bkz. "Ayrık Zamanlı İşaretler ve Sistemler" ve "Sayısal Süzgeçler" yazıları.

## 1. Hızlı Fourier dönüşümü (zamanda seyreltmeli, DIT)

**Tanım.** X(k) = Σ_{n=0}^{N−1} x[n]·W_N^{kn}, W_N = e^{−j2π/N}; W_N^k periyodiktir: W_N^{k+N} = W_N^k.

**Çift ve tek indisli ayırma (N çift).**
X(k) = Σ_{m=0}^{N/2−1} x[2m]·W_N^{2mk} + Σ_{m=0}^{N/2−1} x[2m+1]·W_N^{(2m+1)k}. W_N² = e^{−j(2π/N)·2} = e^{−j4π/N} = W_{N/2} olduğundan:

X(k) = F(k) + W_N^k·G(k), k = 0, 1, …, N/2 − 1
X(k + N/2) = F(k) − W_N^k·G(k), k = 0, 1, …, N/2 − 1

Burada F(k) çift indisli, G(k) tek indisli örneklerin N/2 noktalı AFD'sidir; W_N^{k+N/2} = W_N^k·W_N^{N/2} = −W_N^k (çünkü W_N^{N/2} = e^{−jπ} = −1). F(k) ve G(k), N/2 periyotla tekrarlanır (F(0) = F(4), F(1) = F(5), … N = 8 için).

**N = 4 örneği ve N = 8 için akış.** Aynı yöntem 4 noktalı AFD içinde de uygulanır: x[0], x[2], x[4], x[6] dizisi F bloğuna; x[1], x[3], x[5], x[7] dizisi G bloğuna girer. 4 noktalı bloklar kendi içinde 2 noktalı AFD'lere bölünür: F_a[0] = x[0] + W₈⁰·x[4] = x[0] + x[4], F_a[1] = x[0] − x[4], F_t[0] = x[2] + x[6], F_t[1] = x[2] − x[6]; G_a[0] = x[1] + x[5], G_a[1] = x[1] − x[5], G_t[0] = x[3] + x[7], G_t[1] = x[3] − x[7]. Sonra W₈² çarpanıyla:
- F(0) = F_a(0) + F_t(0), F(1) = F_a(1) + W₈²·F_t(1), F(2) = F_a(0) − F_t(0), F(3) = F_a(1) − W₈²·F_t(1);
- G(0), G(1), G(2), G(3) aynı biçimde; son adımda X(k) = F(k) + W₈^k·G(k) (k = 0 … 3) ile X(0) … X(3), X(k + 4) = F(k) − W₈^k·G(k) ile X(4) … X(7) bulunur. Kelebek (butterfly) çizimlerinde ağırlıklar W₈⁰, W₈¹, W₈², W₈³ ve karşıt dallarda −1'dir.

**Sayısal örnek.** x[n] = {1, 1, −1, −1, −1, 1, 1, −1}, N = 8: zamanda seyreltmeli HFD ile X(k) bulunuz. 4 noktalı DFT matrisinin satırları (1, 1, 1, 1), (1, −j, −1, j), (1, −1, 1, −1), (1, j, −1, −j) olarak alınmıştır (W₄⁰ = 1, W₄² = −1). Çift indisliler f[n] = {1, −1, −1, 1}, tek indisliler g[n] = {1, −1, 1, −1}. 4×4 DFT matrisiyle F(k) = {0, 2 + j2, 0, 2 − j2}, G(k) = {0, 0, 4, 0}. Sonuç:
X(0) = 0, X(1) = 2 + j2, X(2) = W₈²·4 = −j4, X(3) = 2 − j2, X(4) = 0, X(5) = 2 + j2, X(6) = +j4, X(7) = 2 − j2.

Birim çember üzerinde n = 0, 4 → 1; n = 1, 5 → −j; n = 2, 6 → −1; n = 3, 7 → j noktaları ve W₈ matrisinin sütunlarının 90° (W₄) ve 180° döndürmeleri (W₄ matrisinin satırları) çizilmiştir. Kısa bir güç spektrumu çizimi de vardır (P_k: 0,25; 0,5; 0,25; 0,5).

## 2. z dönüşümü

z dönüşümü, Fourier dönüşümünün genellemesidir. Bir işaretin toplamı sonsuza giderse (örneğin x[n] = (0,5)ⁿu[−n] ya da büyüyen bir işaret) Fourier dönüşümünü alamayız; bu yüzden z dönüşümü yaparız. **z dönüşümünde yakınsama bölgesi (YB, ROC) vardır.**

**Yakınsama bölgesi.**
- Z = r·e^{jω} yazılınca X_r(e^{jω}) = Σ x[n]·r^{−n}·e^{−jωn}; r seçimiyle toplam sonlu yapılabilir. Örnek: x[n] = 2ⁿu[n] için Σ|x[n]| = ∞, yani DTFT yoktur; fakat r = 3 (r > 2) ile Σ 2ⁿ·3^{−n}·e^{−jωn} = Σ (2/3)ⁿ e^{−jωn} yakınsar.
- Geometrik seri: Σ_{n=0}^{∞} αⁿ = 1/(1 − α), |α| < 1.
- Birim çember YB içindeyse ayrık zamanlı Fourier dönüşümü yapılabilir; içermiyorsa yapılamaz.
- İşaret **sağ taraflıysa** YB bir çemberin dışıdır; **sol taraflıysa** bir çemberin içidir. Sağ taraflı ise nedensel, sol taraflı ise nedensel değildir.
- **Özellikler:** YB kutup içermez; kararlı olması için YB birim çemberi içermelidir; hem nedensel hem kararlı olması için kutuplar birim çemberin içinde (0'dan küçük genlikli) olmalıdır; YB'nin kutup içermemesi için en küçük kutbun içi, en büyük kutbun dışı ya da kutupların arası olmalıdır. Örnek: kutuplar 0,5; 2; 3; 5'teyse YB: |z| < 0,5, 0,5 < |z| < 2, 2 < |z| < 3, 3 < |z| < 5 ya da |z| > 5 (2 ile 5'in arası "olmaz", 2 ile 3 olur, 3 ile 5 olur).
- Pay derecesi paydadan büyükse sistem nedensel değildir (örnek: H(z) = (z³ − 2z² + z)/(z² + z/4 + 1/8) nedensel değil).

**Örnek 1 (sol taraflı).** x[n] = −(7/8)ⁿ·u[−n−1]. X(z) = Σ_{n=−∞}^{−1} −(7/8)ⁿ z^{−n} = … = 1/(1 − (7/8)z⁻¹), YB: |z| < 7/8 (toplamın yakınsaması için |(7/8)^{−1}·z| < 1). Defterde "eğer denklem x[n] = (7/8)ⁿu[n] olsaydı X(z) aynı olur, fakat YB |z| > 7/8 olurdu" notu da vardır.

**Örnek 2.** x[n] = 7(1/3)ⁿu[n] − 6(1/2)ⁿu[n]: X(z) = 7/(1 − (1/3)z⁻¹) − 6/(1 − (1/2)z⁻¹) = (1 − (3/2)z⁻¹) / [(1 − (1/3)z⁻¹)(1 − (1/2)z⁻¹)], |z| > 1/2.

**Örnek 3 (sinüslü).** x[n] = (1/3)ⁿ·sin(πn/4)·u[n] → X(z) = ((1/3)·(√2/2)·z) / [(z − (1/3)e^{jπ/4})(z − (1/3)e^{−jπ/4})] (|z| > 1/3; kutuplar 1/3 yarıçaplı çember üzerinde ±45°).

Kutuplar 1/3 ve 1/2 olan bir örnekte üç bölge çizilmiştir: |z| > 1/2 sağ taraflı (nedensel ve kararlı, birim çemberi içerir); 1/3 < |z| < 1/2 iki taraflı; |z| < 1/3 sol taraflı (x[n] = 7(1/3)ⁿu[−n−1] + 6(1/2)ⁿu[−n−1] biçiminde).

## 3. Ters z dönüşümü

Bazı ters z dönüşüm çiftleri:

| X(z) | |z| > |α| | |z| < |α| |
|---|---|---|
| 1 / (1 − αz⁻¹) | αⁿ·u[n] | −αⁿ·u[−n−1] |
| 1 / (1 − αz⁻¹)² | (n+1)·αⁿ·u[n] | −(n+1)·αⁿ·u[−n−1] |
| 1 / (1 − αz⁻¹)^m | [(n+1)(n+2)…(n+m−1)/(m−1)!]·αⁿ·u[n] | −[(n+1)…(n+m−1)/(m−1)!]·αⁿ·u[−n−1] |

Notlar: αz⁻¹/(1 − αz⁻¹)² = αz/(z − α)²; pay ve payda dereceleri eşitse sabit katsayıyı çıkarmak için birbirine bölünür; z = 0 ve z = −1 gibi kutup/sıfır noktaları ve katlı kutuplar için bir değer daha verilir ("2'ye çarpıp 2'ye böldük" ile pay düzenlenir). Kısmi kesirli bir örnek: X(z) = z⁻¹ / [(1 − az⁻¹)(1 − bz⁻¹)²] = A/(1 − az⁻¹) + B1/(1 − bz⁻¹) + B2/(1 − bz⁻¹)².

**Sayısal örnek (üç bölge).** X(z) kısmi kesirli açılımı sonucunda üç farklı YB için üç farklı dizi bulunur:
- |z| < 1/2: x[n] = 2δ[n] + 9(1/2)ⁿu[−n−1] − 8u[−n−1],
- 1/2 < |z| < 1: x[n] = 2δ[n] − 9(1/2)ⁿu[n] − 8u[−n−1],
- |z| > 1: x[n] = 2δ[n] − 9(1/2)ⁿu[n] + 8u[n].

Bu üç durumdan yalnızca |z| > 1 olan sağ taraflı ve nedenseldir; birim çemberi içeren 1/2 < |z| < 1 iki taraflıdır ve Fourier dönüşümü vardır.

*Not: Defterdeki bazı kısımlar (özellikle kısmi kesir katsayıları ve çizimler) acele yazıldığı için el yazısından okunurken küçük farklılıklar olabilir.*
