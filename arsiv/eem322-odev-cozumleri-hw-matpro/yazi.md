---
baslik: EEM322 Denetim Sistemleri: HW+MATPRO Ödevi ve El Yazısı Çözümleri (HW 18, 35, 36) ile Ogata B-5-15
ozet: Prof. Dr. Alper Uraz'ın EEM322 HW+MATPRO ödev föyü (G(s) = K(s+a)/[sⁿ(s+b)(s²+cs+d)], 50 parametre seti) ve 2012 baharından üç el yazısı çözüm: yüzde aşım ve yerleşme süresi, doğrudan ve kaskad durum diyagramları, statik hata katsayıları, kök yer eğrisi; ek olarak Ogata B-5-15 karşılaştırmalı sistem çözümü.
---

Bu yazı, Başkent Üniversitesi **EEM322 Denetim Sistemleri** dersinin **HW+MATPRO** adlı ödevini ve bu ödeve ait el yazısı çözümleri bir araya getiriyor. Ödev föyü dersin öğretim üyesi **Prof. Dr. Alper Uraz**'ın hazırladığı Word belgesi (ilk sürümü 2005, son düzenlemesi Ocak 2012). Çözümler 30 Nisan 2012'de fotoğraflanmış defter ve kâğıt sayfalarından **metne aktarıldı**. Fotoğraflar yayınlanmadı. Sayfalarda kimin elinden çıktıklarını gösteren bir ad yok. Sonda, aynı klasörde bulunan ve taranmış sayfalardan oluşan bir **Ogata B-5-15** çözümü de var. Ödev föyü ve B-5-15 taramaları yazının sonunda ZIP olarak indirilebilir.

Dersin klasik ödev listesi (Ogata ve Uraz kitaplarından B-problemleri) [izlence yazısında](/arsiv/eem322-izlence/) yer alıyor. Bu yazıdaki HW+MATPRO ise her öğrenciye kendi parametreleriyle verilen, tek bir sistem üzerinden ilerleyen bir ödev.

## Ödev föyü: HW+MATPRO

Açık çevrim aktarım işlevi (OLTF):

- G(s) = K(s + a) / [sⁿ (s + b)(s² + cs + d)]

{n, a, b, c, d} parametreleri her HW numarası için tabloda veriliyor. Gerektiğinde K = 1 alınabiliyor. Problemler:

1. Birim basamak giriş için Ts ve PO'yu (yüzde aşım) hesaplayın, birim basamak yanıtını çizin.
1. Durum diyagramlarını çizin ve doğrudan (direct) ile kaskad (cascade) ayrıştırmayla durum uzayı tanımını (SSD) elde edin.
1. G(s) birim geri beslemeli yapıdayken Kp, Kv, Ka'yı bulun; birim basamak, birim rampa ve parabolik giriş için ess'i hesaplayın.
1. 0 ≤ K < ∞ için kök yer eğrisini çizin; ayrılma noktaları, jω ekseni kesişimleri, asimptot merkezi, asimptotlar ve kalkış/varış açıları gibi bütün önemli noktaları gösterin.
1. Bode diyagramlarını çizin; ωg, ωp, kazanç payı (gm) ve faz payını (pm) okuyun.
1. Tam Nyquist eğrisini çözümlü örneklerdeki gibi adım adım çizin ve Nyquist ölçütüyle kapalı çevrim kararlılığını belirleyin.

Teslim kuralları: 1–4. problemler 11. haftanın cuması, 5–6. problemler 14. haftanın cuması teslim ediliyor. Bütün zaman yanıtları, kök yer eğrileri, Bode ve Nyquist çizimleri **elle** yapılıyor. **MATLAB projesi** kısmında 4–6. problemlerin her adımı için MATLAB kodu ve uygun MATLAB çizimleri isteniyor (teslim: 14. haftanın cuması).

### Parametre tablosu

| HW | n | a | b | c | d | HW | n | a | b | c | d |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 1 | 2 | 0.6 | 1 | 26 | 0 | 2 | 3 | 0.6 | 1 |
| 2 | 0 | 1 | 3 | 1.2 | 4 | 27 | 0 | 2 | 4 | 1.2 | 4 |
| 3 | 0 | 1 | 4 | 1.8 | 9 | 28 | 0 | 2 | 5 | 1.8 | 9 |
| 4 | 0 | 1 | 5 | 2.4 | 16 | 29 | 0 | 2 | 6 | 2.4 | 16 |
| 5 | 0 | 1 | 6 | 0.8 | 1 | 30 | 0 | 2 | 7 | 0.8 | 1 |
| 6 | 0 | −1 | 2 | 1.6 | 4 | 31 | 1 | 0.5 | 1 | 4 | 7.0 |
| 7 | 0 | −1 | 3 | 2.4 | 9 | 32 | 1 | 1.0 | 1 | 4 | 7.5 |
| 8 | 0 | −1 | 4 | 3.2 | 16 | 33 | 1 | 1.5 | 1 | 4 | 8.0 |
| 9 | 0 | −1 | 5 | 1 | 1 | 34 | 1 | 2.0 | 1 | 4 | 8.5 |
| 10 | 0 | −1 | 6 | 2 | 4 | 35 | 1 | 2.5 | 1 | 4 | 9.0 |
| 11 | 1 | 1 | 2 | 3 | 9 | 36 | 1 | 1.0 | 1.5 | 5 | 8.0 |
| 12 | 1 | 1 | 3 | 4 | 16 | 37 | 1 | 1.5 | 1.5 | 5 | 8.5 |
| 13 | 1 | 1 | 4 | 1.2 | 1 | 38 | 1 | 2.0 | 1.5 | 5 | 9.0 |
| 14 | 1 | 1 | 5 | 2.4 | 4 | 39 | 1 | 2.5 | 1.5 | 5 | 9.5 |
| 15 | 1 | 1 | 6 | 3.6 | 9 | 40 | 1 | 3.0 | 1.5 | 5 | 10.0 |
| 16 | 1 | −1 | 2 | 4.8 | 16 | 41 | 0 | −2 | 2 | 1.6 | 4 |
| 17 | 1 | −1 | 3 | 1.4 | 1 | 42 | 0 | −2 | 3 | 2.4 | 9 |
| 18 | 1 | −1 | 4 | 2.8 | 4 | 43 | 0 | −2 | 4 | 3.2 | 16 |
| 19 | 1 | −1 | 5 | 4.2 | 9 | 44 | 0 | −2 | 5 | 1 | 1 |
| 20 | 1 | −1 | 6 | 5.6 | 16 | 45 | 0 | −2 | 6 | 2 | 4 |
| 21 | 0 | 1 | 7 | 0 | 0 | 46 | 0 | 2 | 7 | 3 | 9 |
| 22 | 0 | 1 | 8 | 0 | 0 | 47 | 0 | 2 | 8 | 4 | 16 |
| 23 | 0 | 1 | 9 | 0 | 0 | 48 | 0 | 2 | 9 | 1.2 | 1 |
| 24 | 0 | 1 | 10 | 0 | 0 | 49 | 0 | 2 | 10 | 2.4 | 4 |
| 25 | 0 | 1 | 11 | 0 | 0 | 50 | 0 | 2 | 11 | 3.6 | 9 |

## Çözüm 1: HW 35, G(s) = (s + 2.5) / [s(s + 1)(s² + 4s + 9)]

Kareli defter sayfalarına yazılmış bu çözümde HW 35'in parametreleri (n = 1, a = 2.5, b = 1, c = 4, d = 9) kullanılmış. Sayfanın üstünde başka bir alıştırmanın izleri de var: Δ(s) = s³ + 4s² + 9s + K için Routh tablosundan K = 36 bulunmuş, yardımcı denklem 4s² + 36 = 0'dan s = ±j3 elde edilmiş. Bir de K(s + 1)/(s + 2) için kök yer başlangıcı (K = 0'da s₁ = −2) yazılmış.

### Problem 2: Doğrudan ayrıştırma

Payda açılınca G(s) = (s + 2.5)/(s⁴ + 5s³ + 13s² + 9s) oluyor. Pay ve payda s⁴'e bölünüyor:

- Y(s)/U(s) = (s⁻³ + 2.5s⁻⁴)/(1 + 5s⁻¹ + 13s⁻² + 9s⁻³)
- X(s) = U(s) − 5s⁻¹X(s) − 13s⁻²X(s) − 9s⁻³X(s)
- Y(s) = s⁻³X(s) + 2.5s⁻⁴X(s)

Dört integratörlü işaret akış grafiğinde geri besleme kazançları −5, −13, −9, ileri yol kazançları 1 ve 2.5. Durum değişkenleri integratör çıkışlarına sağdan sola x₁…x₄ diye verilince:

- ẋ = [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, −9, −13, −5]] x + [0, 0, 0, 1]ᵀ u
- y = [2.5, 1, 0, 0] x

### Problem 2: Kaskad ayrıştırma

G(s), (s + 2.5)/(s + 1) · (1/s) · 1/(s² + 4s + 9) diye üç parçaya bölünmüş. Birinci dereceden blok için genel kalıp şu:

- (s + z)/(s + p) = (1 + z s⁻¹)/(1 + p s⁻¹) ⇒ X(s) = U(s) − p s⁻¹X(s), Y(s) = X(s) + z s⁻¹X(s)

İkinci dereceden blok için 1/(s² + 4s + 9) = s⁻²/(1 + 4s⁻¹ + 9s⁻²) ⇒ X(s) = U(s) − 4s⁻¹X(s) − 9s⁻²X(s), Y(s) = s⁻²X(s). Defterde elde edilen kaskad SSD:

- ẋ = [[0, 1, 0, 0], [−9, −4, 1, 0], [0, 0, 0, 2.5], [0, 0, 0, −1]] x + [0, 0, 1, 0]ᵀ u, y = [1, 0, 0, 0] x

*Not: Defterdeki kaskad matrisinde 1/s bloğu ile (s + 2.5)/(s + 1) bloğunun bağlantısı hatalı kurulmuş: bu haliyle u, x₄'ü hiç sürmüyor. (s + 2.5)/(s + 1) = 1 + 1.5/(s + 1) olduğundan doğrusu ẋ₄ = −x₄ + u, ẋ₃ = 1.5x₄ + u, ẋ₂ = −9x₁ − 4x₂ + x₃, ẋ₁ = x₂, y = x₁; yani A'nın üçüncü satırı [0, 0, 0, 1.5], B = [0, 0, 1, 1]ᵀ olmalı.*

Sayfanın altında birinci problem için şu hatırlatma da var: ζωn = α ve Ts = 4/(ζωn).

## Çözüm 2: HW 18, G(s) = (s − 1) / [s(s + 4)(s² + 2.8s + 4)]

Düz kâğıda yazılmış bu çözümün altında "Not: Sorular 18. sıraya göre çözülmüştür." yazıyor. HW 18'in parametreleri: n = 1, a = −1, b = 4, c = 2.8, d = 4.

### Problem 1: PO ve Ts

Çözümde ikinci dereceden çarpan s² + 2.8s + 4 = s² + 2ζωn s + ωn² ile karşılaştırılmış:

- 2ζωn = 2.8 ⇒ ζωn = 1.4; ωn² = 4 ⇒ ωn = 2 ⇒ ζ = 0.7
- Ts = 2/α, α = ζωn = 1.4 ⇒ Ts = 2/1.4 = 10/7
- PO = 100·e^(−ζπ/√(1−ζ²)) = 100·e^(−0.99π) = 100·e^(−3.11) ≈ 4.46

*Not: e^(−ζπ/√(1−ζ²)) için √(1 − 0.49) = 0.714 alınırsa üs −3.08 ve PO ≈ %4.6 çıkıyor. Daha önemlisi, bu hesap açık çevrimdeki karmaşık kutup çiftini kullanıyor. Kapalı çevrim paydası s⁴ + 6.8s³ + 15.2s² + 17s − 1 ve sabit terimi negatif (a = −1 olduğundan her K > 0 için −K). Kapalı çevrim s ≈ +0.056'da bir kutupla kararsız, dolayısıyla basamak yanıtı için PO ve Ts tanımlı değil. 2.8 yerine bazı satırlarda 1.2 ve 7.2 katsayıları okunuyor; açık çevrim paydasının doğru açılımı s⁴ + 6.8s³ + 15.2s² + 16s.*

### Problem 3: Hata katsayıları

- Kp = lim(s→0) G(s) = ∞
- Kv = lim(s→0) sG(s): çözümde "−1/0 = ∞" yazılmış
- Ka = lim(s→0) s²G(s): çözümde ∞
- W(s) = 1/(1 + G), ess = lim(s→0) sR(s)W(s)
- Birim basamak: ess = 0; birim rampa: ess = −16; parabolik giriş (R = 2/s³): ess = ∞

*Not: G(s)'nin orijinde tek kutbu olduğundan sistem 1. tip: Kv = lim sG(s) = −1/16 (sonlu), Ka = 0. Rampa için bulunan ess = −16 = 1/Kv sonucu bununla tutarlı, ama Kv ve Ka satırları yanlış. Yine de kapalı çevrim kararsız olduğundan bu kalıcı durum hataları gerçekte oluşmaz.*

### Problem 4: Kök yer eğrisi

- Açık çevrim kutupları: 0, −4, −1.4 ± j1.43 (n = 4); sıfır: +1 (m = 1)
- Asimptot sayısı n − m = 3, açılar 60°, 180°, 300°
- Asimptot merkezi: çözümde σa = (−4 − 1.4 − 1.4)/3 = −6.8/3 ≈ −2.2
- jω kesişimi için Routh tablosu (Kc), ayrılma noktası için dK/ds = 0 adımları başlık olarak bırakılmış; kutup-sıfır yerleşimi çizilmiş.

*Not: Merkez formülü σa = (Σ kutuplar − Σ sıfırlar)/(n − m). +1'deki sıfır çıkarılınca σa = (−6.8 − 1)/3 = −2.6 olur.*

## Çözüm 3: HW 36, G(s) = K(s + 1) / [s(s + 1.5)(s² + 5s + 8)]

Spiralli bloknota İngilizce yazılmış, başında "HW No: 36" olan çözüm (n = 1, a = 1, b = 1.5, c = 5, d = 8).

### Problem 1

Elle çizilmiş basamak yanıtı üzerinden PO = %11.3 ve Ts = 2.94 okunmuş.

*Not: K = 1 için kapalı çevrim paydası s⁴ + 6.5s³ + 15.5s² + 13s + 1, kutupları yaklaşık −2.38 ± j1.19, −1.66 ve −0.085. Yanıt aşımsız ve çok yavaş (Ts ≈ 43 s). Grafikteki %11.3 ve 2.94 s değerleri ancak K ≈ 14 civarında elde ediliyor; çizim büyük olasılıkla başka bir K ile yapılmış.*

### Problem 2: Doğrudan ve kaskad SSD

- G(s) = (s + 1)/(s⁴ + 6.5s³ + 15.5s² + 12s) = (s⁻³ + s⁻⁴)/(1 + 6.5s⁻¹ + 15.5s⁻² + 12s⁻³)
- X(s) = U(s) − (6.5s⁻¹ + 15.5s⁻² + 12s⁻³)X(s), Y(s) = (s⁻³ + s⁻⁴)X(s)
- Doğrudan ayrıştırma: ẋ = [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, −12, −15.5, −6.5]] x + [0, 0, 0, 1]ᵀ u, y = [1, 1, 0, 0] x

Kaskad ayrıştırma için G(s) = (1/s) · (s + 1)/(s + 1.5) · 1/(s + 2.5 − j1.32) · 1/(s + 2.5 + j1.32) yazılmış ve karmaşık kutuplarla birinci dereceden bloklar dizilmiş.

### Problem 3: Hata katsayıları

- Kp = G(0) = ∞, Kv = lim sG(s) = 1/12, Ka = 0 ⇒ sistem 1. tip
- Birim basamak: ess = 0; birim rampa: ess = 12 = 1/Kv; parabolik giriş: ess = ∞
- Not olarak: birim geri beslemede W(s) = 1/(1 + G(s)), ess = lim(s→0) sR(s)W(s)

### Problem 4: Kök yer eğrisi

- Açık çevrim kutupları: 0, −1.5, −2.5 ± j1.32 (n = 4); sıfır: −1 (m = 1)
- Asimptotlar: θk = (2k + 1)π/(n − m) = 60°, 180°, 300°; σa = (0 − 1.5 − 2.5 − 2.5 − (−1))/3 = −1.83
- Δ(s) = s⁴ + 6.5s³ + 15.5s² + 12s + K(s + 1) = 0 için Routh tablosu: s⁴: 1, 15.5, K; s³: 6.5, 12 + K; s²: X = (15.5·6.5 − 12 − K)/6.5, K
- Gerçek eksende ayrılma noktası olmadığı ("reel ekseni kesmiyor") belirtilmiş; dK/ds = 0 türevi kurulmuş.
- Kalkış açısı (−2.5 + j1.32 kutbundan): θd = 180° − (152.2° + 127.2° + 90°) + 138.6° ≈ −50°
- Çizilen eğride iki kol karmaşık kutuplardan −50° ile çıkıp sanal ekseni kesiyor, diğerleri gerçek eksende kalıyor.

*Not: Routh tablosunun tamamlanmasıyla s¹ satırı sıfır yapılırsa K² − 34.5K − 1065 = 0 ⇒ Kc ≈ 54.2 bulunuyor. Yardımcı denklemden jω kesişimi ±j3.19 civarında; grafikte bu nokta yaklaşık "3.1j" olarak işaretlenmiş.*

## Ek: Ogata B-5-15, üç sistemin karşılaştırılması

Taranmış üç sayfalık (11–13. sayfalar) bu çözümde Ogata'nın B-5-15 problemi ele alınıyor. Problemde üç birim geri beslemeli sistem için birim rampa hatası ve zaman yanıtı ölçütleri karşılaştırılıyor.

| | G(s) | Tip | Rampa ess | ζ | Mp | Tr | Ts |
|---|---|---|---|---|---|---|---|
| Sistem I | 5/[s(5s + 1)] | 1 | 1/5 | 0.1 | 1.72 | 1.67 | 40 |
| Sistem II | 5(1 + 0.8s)/[s(5s + 1)] | 1 | 1/5 | 0.5 | 1.16 | 2.42 | 8 |
| Sistem III | 1/[s(s + 1)] | 1 | 1 | 0.5 | 1.16 | 2.42 | 8 |

Örnek hesaplar:

- Sistem I: Δ(s) = 5s² + s + 5 ⇒ s² + 0.2s + 1 ⇒ ωn = 1, ζ = 0.1; θ = cos⁻¹(0.1) = 1.47, Tr = (π − θ)/ωd; Ts = 4/(ζωn) = 40
- Sistem II: T(s) = (1 + 0.8s)/(s² + s + 1), W(s) = 1 − T(s) = s(s + 0.2)/(s² + s + 1) ⇒ rampa için ess = 0.2
- Sistem III: T(s) = 1/(s² + s + 1), E(s) = R(s)·s(s + 1)/(s² + s + 1) ⇒ rampa için ess = 1
- Üç sistemde de birim dürtü ve birim basamak için ess = 0

Yorum (çözümden): Sistem 1'in sönüm oranı en küçük ve en hızlı tepki veren o, ama aşımı ve yerleşme süresi çok büyük; bu yüzden seçilmemeli. Sistem 2 ile 3'ün sönüm oranları aynı ve Mp, Tr, Ts değerleri eşit; Sistem 2'nin kalıcı durum hatası daha küçük. Sonuç olarak en iyi sistem 2.

*Not: Sistem II'nin kapalı çevriminde −1.25'te bir sıfır var ve bu sıfır yanıtı hızlandırıp aşımı artırıyor. Benzetimde Sistem II için Mp ≈ 1.25 ve %0–100 yükselme süresi ≈ 1.43 s çıkıyor (Ts ≈ 7.6 s). Yani Sistem II ve III'ün Mp ve Tr değerleri aslında eşit değil. Yine de "en iyi Sistem 2" sonucu değişmiyor.*
