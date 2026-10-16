---
baslik: EEM322 Denetim Sistemleri: Quiz Hazırlık Defter Notları (2013 Yaz ve 2015 Bahar)
ozet: EEM322 Denetim Sistemleri için quiz hazırlık defter notları: kütle-yay-sönümleyici durum modeli, kararlılık soruları, diferansiyel denklemden ve durum uzayından transfer fonksiyonu ile zaman yanıtı, frekans yanıtı, benzerlik dönüşümü ve özdeğer quiz sorusu, PI denetleçle ikinci dereceden yanıt tasarımı.
---

Bu yazı, EEM322 Denetim Sistemleri klasörünün kökünde duran defter fotoğraflarının metne aktarılmış hâlidir. İki grup var: **2013 yaz okulu** (Temmuz–Ağustos 2013) sırasında quiz ve sınavlara hazırlanırken tutulmuş çözümlü sorular ve ders notu sayfaları; **2015 bahar dönemi** (8 Nisan 2015) defterinden benzerlik dönüşümü, bir "quiz sorusu" ve ikinci dereceden sistem notları. **Fotoğraflanmış sayfalardan metne aktarıldı**; fotoğraflar yayınlanmadı. Aynı klasördeki ders kitabı sayfalarının fotoğrafları yayınlanmadı.

## 2013: Ders notlarından tanımlar

- Sistem görsellikten matematiksel biçime çevrilirse modellenmiş olur. Dikkat edilecekler: giriş, çıkış, bozucu ve sistem değişkenleri; parametrelerin değişip değişmediği.
- **Doğrusal sistem:** homojenlik F(au) = aF(u) ve süperpozisyon F(u + ũ) = F(u) + F(ũ) sağlanır.
- **Zamanla değişen / değişmeyen:** ayrım parametrelerle yapılır; parametreler değişiyorsa sistem zamanla değişendir.
- **Dinamik / statik:** dinamik sistemde enerji depolayan elemanlar ve başlangıç değerleri vardır, çıkış zamana göre oluşur; statik sistemde başlangıç değeri yoktur, çıkış hemen oluşur.
- **Açık döngü** denetimde ölçüm yoktur; **kapalı döngü** denetimde ölçüm (sensör ve algılayıcı) vardır. Blok diyagramı: referans → karşılaştırıcı → denetleç → eyleyici (actuator) → süreç (process) → çıkış, ölçme elemanından geri besleme. Bozucu (disturbance) dış etkilerdir.
- Denetlediği fiziksel büyüklük açısından **servomekanizma** (giriş izlenir) ve **regülatör** sistemleri; analog ve sayısal denetim sistemleri.
- Zaman yanıtı ölçütleri: **tepe süresi Tp** (yanıtın tepe noktasına ulaştığı süre), **aşım %OS** (tepe değeri ile kalıcı değer arasındaki farkın kalıcı değere oranı), **yükselme süresi Tr** (yanıtın %10'dan %90'a çıkma süresi), **yerleşme süresi Ts** (yanıtın kalıcı değerin %98'ine yerleşme süresi). Oransal denetimde Gp = K/(τs + 1) için hata E(s) = R(s)/(1 + K).

## 2013: Çözümlü sorular

### Kütle-yay-sönümleyici için durum modeli

F kuvvetiyle sürülen, D sönümlü ve K yaylı m kütlesinin durum uzayı modeli (konum x₁, hız x₂): mÿ = F − Dẏ − Ky ⇒ ẋ₁ = x₂, ẋ₂ = (1/m)(−Dx₂ − Kx₁ + u).

> A = [0 1; −K/m −D/m], B = [0; 1/m], C = [1 0], D = 0

### Hangisi kararlıdır?

- (s − 1)/(s + 1): kutup −1 ⇒ kararlı.
- (s² − 1)/(s² + 2s + 2): Δ = 4 − 8 = −4 ⇒ kutuplar −1 ± j ⇒ kararlı.
- (s − 1)/(s² − 1) = 1/(s + 1): sadeleşme sonrası kutup −1 ⇒ kararlı (iç kararlılık açısından sadeleşen s = 1 kutbuna dikkat).
- 2 kazançlı blok ve −1/(s − 1) sistemi pozitif geri beslemeyle: TF = (−2/(s − 1)) / (1 + 2/(s − 1)) = −2/(s + 1) ⇒ kutup −1, kararlı.

### Blok diyagramı sadeleştirme

G₂ ile G₃'ün oluşturduğu pozitif geri besleme döngüsü G₅ = G₂/(1 − G₂G₃) olarak indirgenmiş; G₄ ile birlikte iç döngü G₈ = G₄G₅/(1 + G₄G₅) yazılmış. Defterde soru burada bırakılmış ("devamı yok").

### Diferansiyel denklemden transfer fonksiyonu

y″ + 3y′ + 2y = 3u′ − u ⇒ s²Y + 3sY + 2Y = 3sU − U ⇒ **Y(s)/U(s) = (3s − 1)/(s² + 3s + 2)**.

### Durum uzayından transfer fonksiyonu ve zaman yanıtı

ẋ = [−6 −3.5; 6 4]x + [−1; 1]u, y = [4 5]x, x(0) = (−2, 1).

1. Y(s) = C(sI − A)⁻¹x(0) (sıfır giriş yanıtı) + [C(sI − A)⁻¹B + D]U(s) (sıfır durum yanıtı).
1. det(sI − A) = (s + 6)(s − 4) + 21 = s² + 2s − 3; (sI − A)⁻¹ = [s − 4 −3.5; 6 s + 6]/(s² + 2s − 3).
1. **G(s) = C(sI − A)⁻¹B = (s + 2)/(s² + 2s − 3)**.
1. U(s) = 1/s ile Y(s) = (−3s − 12)/(s² + 2s − 3) + (s + 2)/[(s² + 2s − 3)s] = (−3s² − 11s + 2)/[(s − 1)(s + 3)s].
1. Kısmi kesirler: −3/(s − 1) + (2/3)/(s + 3) − (2/3)/s ⇒ **y(t) = −3eᵗ + (2/3)e^(−3t) − 2/3**. s = 1 kutbu yüzünden yanıt sınırsız büyür (sistem kararsız).

### Frekans yanıtı

G(s) = 0.5/(s + 0.5) ⇒ |G(jω)| = 0.5/√(ω² + 0.25), ∠G(jω) = −tan⁻¹(ω/0.5).

| ω (rad/s) | \|G(jω)\| | ∠G(jω) |
|---|---|---|
| 0.2 | 0.928 | −0.385 rad = −21.8° |
| 1.8 | 0.268 | −1.300 rad = −74.5° |

### Kazanç/faz payı ve kararlılığın sezgisel anlatımı

Faz kesim (phase crossover) frekansında süreç |G(jωx)| = K ve ∠G(jωx) = −180°. Kapalı döngüye 2 sin 5t işareti verilip döngü kesildiğinde, Q noktasındaki işaret −K × (P'deki işaret) olur:

- K = 0.5: P'de 2 sin 5t, 1 sin 5t, 0.5 sin 5t … işaret her turda yarıya iner ⇒ **kararlı**.
- K = 1: işaret hep 2 sin 5t kalır ⇒ **sınırda kararlı** (bağımlı kararlı).
- K = 3: 2, 6, 18 sin 5t … işaret büyür ⇒ **kararsız**.

Kural: faz kesim frekansında kazanç 0 dB'nin altında (gain margin > 0) ve kazanç kesim frekansında faz −180°'nin üstünde (phase margin > 0) ise, yani ikisi de sağlanırsa sistem kararlıdır.

## 2015: Benzerlik dönüşümü ve quiz sorusu

### Benzerlik (similarity) dönüşümü

x = Mz dönüşümüyle ẋ = Ax + Bu sistemi ż = Λz + Γu biçimine getirilir: Λ = M⁻¹AM, Γ = M⁻¹B, z(0) = M⁻¹x(0). M'nin sütunları A'nın özvektörleridir; Λ köşegen (özdeğerler) olur ve e^(Λt) = diag(e^(λ₁t), …, e^(λₙt)). Çözüm x(t) = M·e^(Λt)·z(0) = z₁(0)e^(λ₁t)m₁ + … + zₙ(0)e^(λₙt)mₙ biçiminde modlara ayrılır (modal ayrıştırma; paralel ayrıştırma ile aynı). Ayrık zamanda Z⁻¹{z(zI − A)⁻¹} = Aᵏ, sürekli zamanda L⁻¹{(sI − A)⁻¹} = e^(At).

Örnek: A = [0 1; −2 −3] ⇒ Λ = [−1 0; 0 −2], M = [1 1; −1 −2].

### Quiz sorusu

ẋ = [0 1; −3 −4]x + [0; 1]u, x(0) = [1 1]ᵀ. M = ? ż = Λz + Γu, z(0) = ?

1. |λI − A| = λ² + 4λ + 3 = (λ + 3)(λ + 1) = 0 ⇒ λ₁ = −1, λ₂ = −3.
1. (λ₂I − A)v₂ = 0 ⇒ [−3 −1; 3 1]v₂ = 0 ⇒ v₂ = [1; −3]. Benzer şekilde v₁ = [1; −1].
1. **M = [1 1; −1 −3]**.

*Not: Defterde çözüm M'de bitiyor. Devamı: M⁻¹ = [1.5 0.5; −0.5 −0.5], Λ = diag(−1, −3), Γ = M⁻¹B = [0.5; −0.5], z(0) = M⁻¹x(0) = [2; −1].*

### Üçüncü dereceden örnek

ẋ = [0 1 −1; −6 −11 6; −6 −11 5]x. |λI − A| = λ³ + 6λ² + 11λ + 6 ⇒ λ₁ = −1, λ₂ = −2, λ₃ = −3. Özvektörler v₁ = [1; 0; 1], v₂ = [1; 2; 4], v₃ = [1; 6; 9] (Av = λv ile denetlendi). Notta, köklerden biri karmaşıksa yazılımın farklı olacağı belirtilmiş.

## 2015: İkinci dereceden sistemler

- T(s) = ωn²/(s² + 2ζωn s + ωn²); 0 < ζ < 1 az sönümlü, ζ = 0 sönümsüz (ωn doğal frekans). Kökler −ζωn ± jωd; ωd sönümlü doğal frekans.
- Aşım PO = 100·exp(−ζπ/√(1 − ζ²)), yerleşme süresi ts(%2) = 4/(ζωn); tepe zamanı Tp, yerleşme süresi Ts grafikte gösterilmiş.
- Örnek durum modeli: A = [0 1; −3 −4], B = [0; 1], y = 10x₁ ⇒ ẋ₁ = x₂, ẋ₂ = −3x₁ − 4x₂ + u.

### PI denetleçle tasarım

Birim geri beslemeli döngüde C(s) = Kp + Ki/s ve G(s) = 10/(s + 2); istenen ess → 0, PO ≤ %20, ts(%2) ≤ 2 s.

1. T(s) = C(s)G(s)/[1 + C(s)G(s)] = 10(Kp·s + Ki)/[s² + (2 + 10Kp)s + 10Ki].
1. PO = 20 ⇒ ζ = 0.455; ts = 4/(ζωn) = 2 ⇒ ζωn = 2 ⇒ ωn = 4.396, ωn² = 19.325.
1. s² + (2 + 10Kp)s + 10Ki = s² + 4s + 19.325 ⇒ **Kp = 0.2**, **Ki ≈ 1.93**.

### Soru

G(s) = 1/[s(s + 1)], birim geri besleme: T(s) = 1/(s² + s + 1) ⇒ ωn = 1, 2ζωn = 1 ⇒ ζ = 0.5. PO = 100·e^(−π/√3) = %16.3, ts(%2) = 4/(ζωn) = 8 s, basamak girişte (tip 1) ess = 0.
