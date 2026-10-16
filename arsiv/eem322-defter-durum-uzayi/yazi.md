---
baslik: EEM322 Denetim Sistemleri: Ders Defteri (Mart 2013) – Durum Uzayı, Durum Geçiş Matrisi, Eş ve Kipsel Biçim, Denetlenebilirlik ve Gözlenebilirlik
ozet: EEM322 Denetim Sistemleri 2013 ders defterinden durum uzayı haftaları: çözücü matris (sI−A)⁻¹ ve e^(At), RLC devresinin durum denklemleri, eş (companion) biçime ve Vandermonde ile kipsel (modal) biçime dönüşüm, doğrudan, kaskad ve paralel ayrıştırma, su tankı örnekleriyle denetlenebilirlik ve gözlenebilirlik.
---

Bu yazı, Başkent Üniversitesi **EEM322 Denetim Sistemleri** dersinin 2013 bahar dönemine ait bir arkadaşın **ders defterinden** durum uzayı konusunu içeriyor (7, 14 ve 16 Mart 2013'te çekilmiş sayfalar). İçerik **fotoğraflanmış sayfalardan metne aktarıldı**; fotoğraflar yayınlanmadı. Örnekler derste İngilizce yazılmış, Türkçe kenar notları da aktarıldı. Hesaplar kontrol edildi; defterdeki küçük yazım hataları notlarla belirtildi. Bulanık çekilmiş bir sayfa okunamadığı için atlandı.

Konu anlatımı için [Ders 3](/arsiv/eem322-ders-03-durum-uzayi/) yazısına bakılabilir. Defterin önceki ve sonraki bölümleri: [modelleme ve blok diyagramları](/arsiv/eem322-defter-modelleme-blok-diyagram/), [kalıcı durum hatası, Routh ve kök yer eğrisi](/arsiv/eem322-defter-kalici-hata-routh-kok-yer/).

## Mason kuralıyla sağlama

Sayfanın başında bir blok diyagramı indirgemesinin sonucu (G₁ + G₂)/(1 + G₁H) işaret akış grafiğiyle doğrulanıyor: ileri yollar P₁ = G₁, P₂ = G₂, döngü L₁ = −G₁H, Δ = 1 + G₁H, Δ₁ = Δ₂ = 1 ⇒ (P₁Δ₁ + P₂Δ₂)/Δ = (G₁ + G₂)/(1 + G₁H).

## Örnek 1: Durum denkleminin çözümü

Durum uzayı modelinin blok diyagramı: u → B → toplama → ẋ → ∫ → x → C → (D ile toplanarak) y, A ile geri besleme.

- ẋ = [[−1, −3], [1, −5]] x + [1, 0]ᵀ u, y = [1, −1] x, D = 0
- u(t) = 1 (t ≥ 0), x(0) = [1, 0]ᵀ

**(a) Sıfır giriş (homojen) çözümü:** X(s) = (sI − A)⁻¹x(0) ya da x(t) = e^(At)x(0). Çözücü (resolvent) matris:

- sI − A = [[s + 1, 3], [−1, s + 5]], det(sI − A) = s² + 6s + 8 = (s + 2)(s + 4)
- (sI − A)⁻¹ = (1/Δ(s))·[[s + 5, −3], [1, s + 1]]
- Kısmi kesirler: [[3/2/(s+2) − 1/2/(s+4), −3/2/(s+2) + 3/2/(s+4)], [1/2/(s+2) − 1/2/(s+4), −1/2/(s+2) + 3/2/(s+4)]]

Ters Laplace ile durum geçiş matrisi:

- Φ(t) = e^(At) = [[(3/2)e^(−2t) − (1/2)e^(−4t), −(3/2)e^(−2t) + (3/2)e^(−4t)], [(1/2)e^(−2t) − (1/2)e^(−4t), −(1/2)e^(−2t) + (3/2)e^(−4t)]]
- Sıfır giriş durum yanıtı: x(t) = e^(At)[1, 0]ᵀ = [(3/2)e^(−2t) − (1/2)e^(−4t), (1/2)e^(−2t) − (1/2)e^(−4t)]ᵀ

**(b) u(t) = 1 ve x(0) = [1, 0]ᵀ için çıkış:**

- Y(s) = C(sI − A)⁻¹x(0) + C(sI − A)⁻¹B U(s)
- = (1/Δ(s))·{[1, −1][s + 5, 1]ᵀ + [1, −1][(s + 5)/s, 1/s]ᵀ} = (s² + 5s + 4)/[sΔ(s)] = (s + 1)/[s(s + 2)]
- y(t) = 1/2 + (1/2)e^(−2t)

Kaynaktaki not: Bütün sadeleştirmeler ve matris işlemleri Laplace bölgesinde yapılmalı, ters Laplace en sonda uygulanmalı.

## Örnek 2: RLC devresinin durum denklemleri

vi kaynağı, R₁ = 4 kΩ, C₁ = 0.25 mF, L = 2 mH, C₂ = 0.5 mF, R₂ = 1 kΩ ve is akım kaynağından oluşan devre. Düğüm denklemleri:

- C₁ dv₁/dt + iL − (vi − v₁)/R₁ = 0 ⇒ 0.00025 dv₁/dt + iL − (vi − v₁)/4000 = 0
- C₂ dv₂/dt − iL + v₂/R₂ − is = 0 ⇒ 0.0005 dv₂/dt − iL + v₂/1000 − is = 0
- L diL/dt + v₂ − v₁ = 0 ⇒ 0.002 diL/dt + v₂ − v₁ = 0

Durum değişkenleri x₁ = v₁, x₂ = v₂, x₃ = iL; girişler u₁ = vi, u₂ = is; çıkış y = v₂:

- ẋ₁ = −x₁ − 4000x₃ + u₁
- ẋ₂ = −2x₂ + 2000x₃ + 2000u₂
- ẋ₃ = 500x₁ − 500x₂
- A = [[−1, 0, −4000], [0, −2, 2000], [500, −500, 0]], B = [[1, 0], [0, 2000], [0, 0]], C = [0, 1, 0]

*Not: Defterde ilk denklem "dv₁/dt = v₁ − 4000iL + vi" diye yazılmış; doğrusu −v₁ (durum değişkenli yazımda doğru: −x₁).*

## Örnek 3: Eş (companion) biçime dönüşüm

Örnek 1'deki sistem için karakteristik denklem Δ(s) = |sI − A| = s² + 6s + 8 = 0.

- Denetlenebilirlik matrisi U = [B, AB] = [[1, −1], [0, 1]], |U| ≠ 0 ⇒ eş biçim mümkün
- U⁻¹ = [[1, 1], [0, 1]], q = [0, 1]U⁻¹ = [0, 1] (U⁻¹'in son satırı)
- Q = [q; qA] = [[0, 1], [1, −5]], Q⁻¹ = [[5, 1], [1, 0]]
- w = Qx dönüşümüyle ẇ = QAQ⁻¹w + QBu = [[0, 1], [−8, −6]]w + [0, 1]ᵀu
- y = CQ⁻¹w + Du = [4, 1]w

## Örnek 4: Kipsel (modal) matris

Eş biçimdeki sistem: ẇ = [[0, 1], [−8, −6]]w + [0, 1]ᵀu, y = [4, 1]w, w(0) = Qx(0) = [0, 1]ᵀ.

- Δ(s) = |sI − Ac| = s² + 6s + 8 ⇒ λ₁ = −2, λ₂ = −4
- Vandermonde yaklaşımıyla özvektörler doğrudan: m₁ = [1, λ₁]ᵀ = [1, −2]ᵀ, m₂ = [1, λ₂]ᵀ = [1, −4]ᵀ
- M = [[1, 1], [−2, −4]], M⁻¹ = [[2, 0.5], [−1, −0.5]]
- Λ = M⁻¹AcM = diag(−2, −4), Γ = M⁻¹Bc = [0.5, −0.5]ᵀ, F = CcM = [2, 0]
- ż = Λz + Γu, y = Fz

Üç gösterimin aktarım işlevi:

- G(s) = C(sI − A)⁻¹B = (s + 4)/[(s + 2)(s + 4)] = 1/(s + 2)
- Gc(s) = Cc(sI − Ac)⁻¹Bc = [4, 1]·(1/Δ)[[s + 6, 1], [−8, s]]·[0, 1]ᵀ = 1/(s + 2)
- Gm(s) = F(sI − Λ)⁻¹Γ = 1/(s + 2)

G(s) = Gc(s) = Gm(s) ve Δ(s) = |sI − A| = |sI − Ac| = |sI − Λ|, beklendiği gibi.

**4(b) Kipsel ayrışım (serbest yanıt):** ẇ = [[0, 1], [−8, −6]]w için yeni başlangıç vektörü z(0) = M⁻¹w(0) = [0.5, −0.5]ᵀ.

- w = Mz = M e^(Λt) z(0) = [m₁, m₂]·diag(e^(−2t), e^(−4t))·z(0)
- w(t) = 0.5e^(−2t)[1, −2]ᵀ − 0.5e^(−4t)[1, −4]ᵀ

*Not: Defterde Örnek 4'ün başında eş biçim matrisi işaretsiz ([[0, 1], [8, 6]]) yazılmış, doğrusu [[0, 1], [−8, −6]]. M⁻¹'in ikinci satırı da [−1, 0.5] diye yazılmış, doğrusu [−1, −0.5] (Γ bu doğru değerle hesaplanmış). Serbest yanıtta ikinci terimin katsayısı −0.5 olmalı; böylece w(0) = [0, 1]ᵀ sağlanıyor.*

## Örnek 5: Aktarım işlevi ayrıştırmaları

G(s) = (3s² + 9s + 6)/(s³ + 7s² + 12s) = 3(s + 1)(s + 2)/[s(s + 3)(s + 4)]

**(i) Doğrudan ayrıştırma:**

- Y/U = (3s⁻¹ + 9s⁻² + 6s⁻³)/(1 + 7s⁻¹ + 12s⁻²)
- X(s) = U(s) − 7s⁻¹X(s) − 12s⁻²X(s), Y(s) = 3s⁻¹X(s) + 9s⁻²X(s) + 6s⁻³X(s)
- İntegratör çıkışları durum değişkeni seçilerek zaman bölgesine geçiliyor: ẋ = [[0, 1, 0], [0, 0, 1], [0, −12, −7]]x + [0, 0, 1]ᵀu, y = [6, 9, 3]x

**(ii) Kaskad (seri) ayrıştırma:** Y/U = (3/s)·[(s + 1)/(s + 3)]·[(s + 2)/(s + 4)]

- (s + z)/(s + p) = (1 + z s⁻¹)/(1 + p s⁻¹) ⇒ X = U − p s⁻¹X, Y = X + z s⁻¹X
- a/s ⇒ X = U, Y = a s⁻¹X
- Bloklar 1/s·3 → (s + 1)/(s + 3) → (s + 2)/(s + 4) sırasıyla dizilip integratörler açılınca üçgen biçimli (triangle form) A matrisi çıkıyor: ẋ = [[−4, −2, 3], [0, −3, 3], [0, 0, 0]]x + [0, 0, 1]ᵀu, y = [2 − 4, 1 − 3, 3]x = [−2, −2, 3]x

*Not: Defterdeki matrisin (2,3) elemanı −3 gibi okunuyor; (s + 1)/(s + 3) bloğunun girişi 3x₃ olduğundan ẋ₂ = −3x₂ + 3x₃, yani eleman +3 olmalı.*

**(iii) Paralel ayrıştırma:** İlk adım kısmi kesir açılımı:

- G(s) = (1/2)/s − 2/(s + 3) + (9/2)/(s + 4)
- a/(s + p) = a s⁻¹/(1 + p s⁻¹) ⇒ X = U − p s⁻¹X, Y = a s⁻¹X
- ẋ = [[0, 0, 0], [0, −3, 0], [0, 0, −4]]x + [1, 1, 1]ᵀu, y = [1/2, −2, 9/2]x

## Denetlenebilirlik ve gözlenebilirlik: su tankları (Örnek 6, ρ = 1)

**(a)** Üstteki tank (A₁, R₁) alttaki tanka (A₂, R₂) boşalıyor, giriş u alt tanka, çıkış y = x₂/R₂:

- A₁ẋ₁ = −x₁/R₁, A₂ẋ₂ = x₁/R₁ − x₂/R₂ + u
- A₁ = A₂ = 1, R₁ = R₂ = 1 için ẋ = [[−1, 0], [1, −1]]x + [0, 1]ᵀu, y = [0, 1]x
- U = [B, AB] = [[0, 0], [1, −1]] ⇒ rank 1 (determinant 0) ⇒ denetlenemez
- V = [C; CA] = [[0, 1], [1, −1]] ⇒ rank 2 ⇒ gözlenebilir

*Not: Defterde genel matrisin ikinci satırı [1/(R₁R₂), −1/(R₁A₂)] diye yazılmış; denklemlere göre doğrusu [1/(R₁A₂), −1/(R₂A₂)], B = [0, 1/A₂]ᵀ.*

**(b)** Giriş üst tanka, çıkış üst tankın debisi (y = [1, 0]x): ẋ = [[−1, 0], [1, 0]]x + [1, 0]ᵀu ⇒ denetlenebilir, gözlenemez.

**(c)** Giriş ve çıkış birinci tankta, ikinci tank bağlantısız: ẋ = [[−1, 0], [0, 0]]x + [1, 0]ᵀu, y = [1, 0]x ⇒ denetlenemez, gözlenemez.

**(d)** Yan yana, R₁ ile bağlı iki tank; giriş birinci tanka, çıkış ikinci tankın R₂ üzerinden debisi:

- A₁ẋ₁ = (x₂ − x₁)/R₁ + u, A₂ẋ₂ = −(x₂ − x₁)/R₁ − x₂/R₂, y = x₂/R₂
- Birim değerlerle ẋ = [[−1, 1], [1, −2]]x + [1, 0]ᵀu, y = [0, 1]x ⇒ denetlenebilir ve gözlenebilir

## Örnek 7: Benzerlik dönüşümünde değişmezlik

Örnek 4'teki köşegen biçim: ż = diag(−2, −4)z + [0.5, −0.5]ᵀu, y = [2, 0]z. Λ'nın elemanları negatif olduğundan sistem kararlı; çıkış matrisindeki 0 yüzünden λ₂ = −4 kipi gözlenemiyor.

| Gösterim | U = [B, AB] | det U | V = [C; CA] | det V | Sonuç |
|---|---|---|---|---|---|
| Genel (A, B, C) | [[1, −1], [0, 1]] | 1 | [[1, −1], [−2, 2]] | 0 | Denetlenebilir, gözlenemez |
| Eş biçim (Ac, Bc, Cc) | [[0, 1], [1, −6]] | −1 | [[4, 1], [−8, −2]] | 0 | Denetlenebilir, gözlenemez |
| Köşegen (Λ, Γ, F) | [[0.5, −1], [−0.5, 2]] | 0.5 | [[2, 0], [−4, 0]] | 0 | Denetlenebilir, gözlenemez |

Denetlenebilirlik ve gözlenebilirlik özellikleri benzerlik dönüşümü altında **değişmez**. Gözlenemeyen λ₂ = −4 kipi, Örnek 4'teki aktarım işlevinde sadeleşen (s + 4) çarpanı olarak görülüyor: G(s) = Gc(s) = Gm(s) = (s + 4)/[(s + 2)(s + 4)] = 1/(s + 2).
