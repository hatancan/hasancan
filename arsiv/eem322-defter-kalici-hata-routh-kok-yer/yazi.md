---
baslik: EEM322 Denetim Sistemleri: Ders Defteri (Mart–Nisan 2013) – Kalıcı Durum Hatası, Sinüzoidal Yanıt, Routh Tablosu, Eksen Kaydırma ve Kök Yer Eğrisi
ozet: EEM322 Denetim Sistemleri 2013 ders defterinden çözümlü örnekler: polinom ve sinüzoidal girişte kalıcı durum yanıtı, birim olmayan geri beslemenin eşdeğer birim geri beslemeye çevrilmesi, Routh tablosunda sıfır eleman ve sıfır satır, K'nın kararlılık aralığı, eksen kaydırma, kök yer eğrisinde sanal eksen kesişimi, ayrılma noktası, kalkış açısı, ζ = 0.7 için K ve Horner/Newton ile kök bulma.
---

Bu yazı, Başkent Üniversitesi **EEM322 Denetim Sistemleri** dersinin 2013 bahar dönemine ait bir arkadaşın **ders defterinden** kalıcı durum hatası, kararlılık ve kök yer eğrisi örneklerini içeriyor (29 Mart, 14–15 ve 19 Nisan 2013'te çekilmiş sayfalar). İçerik **fotoğraflanmış sayfalardan metne aktarıldı**; fotoğraflar yayınlanmadı. Örnekler derste İngilizce yazılmış; Türkçe kenar notları da aktarıldı. Hesaplar kontrol edildi. Derste izlenen kitabın Routh ve kök yer eğrisi sayfalarının fotoğrafları kitap sayfası olduğu için aktarılmadı.

Konu anlatımı için [Ders 6](/arsiv/eem322-ders-06-kararlilik/), [Ders 7](/arsiv/eem322-ders-07-surekli-hal-hatalari/) ve [Ders 8](/arsiv/eem322-ders-08-kok-yer-egrisi/) yazılarına bakılabilir. Defterin önceki bölümleri: [modelleme ve blok diyagramları](/arsiv/eem322-defter-modelleme-blok-diyagram/), [durum uzayı](/arsiv/eem322-defter-durum-uzayi/).

## Kalıcı durum hatası

### Örnek 2(b): Birim olmayan geri besleme (b ≠ 1)

Önceki sayfada başlayan örneğin (a) şıkkında çıkışın rampa girişi sonlu ess ile izlediği ve sistemin 1. tip olduğu bulunmuş. (b) şıkkında geri besleme b ≠ 1:

- W(s) = [s² + 3s + 10(b − 1)]/(s² + 3s + 10b)
- C₀ = W(0) = (b − 1)/b, C₁ = dW(s)/ds (s = 0) = 3/(10b²)
- R(s) = 1/s için ess = lim(s→0) sR(s)W(s) = W(0) = (b − 1)/b (basamak girişi için sonlu sonuç)
- R(s) = 1/s² için ess = lim(s→0) (1/s)W(s) = ∞
- Çıkış basamak girişi sonlu ess ile izliyor, sistem 0. tip.

### Örnek 3(a): Polinom giriş

Burada G(s) değil, doğrudan kapalı çevrim aktarım işlevi verilmiş (defterdeki uyarı: "Burada G(s) verilmemiş, ona dikkat et!"):

- T(s) = (3s + 2)/(s² + 3s + 2) = (b₁s + b₀)/(s² + a₁s + a₀)
- Hem basamak hem rampa için kalıcı durum hatası, b₀ = a₀ ve b₁ = a₁ ise sıfır; yalnız a₀ = b₀ ise basamak için hata sıfır.

(i) Basamak girişi r(t) = 4 için:

- css(t) = lim(t→∞) c(t) = T(0)·a = (b₀/a₀)·a = (2/2)·4 = 4

(ii) r(t) = 2 + t (basamak ve rampa birlikte) için:

- r₁(t) = 2 ⇒ css₁(t) = 2
- r₂(t) = t ⇒ css₂(t) = T(0)·t + T′(0)·1 = (b₀/a₀)t + [(a₀b₁ − b₀a₁)/a₀²]·1 = t
- Süperpozisyonla css(t) = 2 + t

Hata ifadeleri:

- Konum hatası: ep(t) = |(a₀ − b₀)/a₀| = |1 − T(0)| = 0
- Hız hatası: ev(t) = |(1 − T(0))t − T′(0)| = |[(a₀ − b₀)/a₀]t − (a₀b₁ − b₀a₁)/a₀²| = 0

Dolayısıyla (i) ve (ii) için asimptotik izleme sağlanıyor: css(t) = lim c(t) = r(t).

### Örnek 4(a): Sinüzoidal giriş

- T(s) = 3/(s + 0.4), r(t) = 5 sin 2t, ω = 2
- T(j2) = 3/(0.4 + j2) = 3/(2.04 e^(j1.37)) = 1.47 e^(−j1.37)
- css(t) = X·|T(jω)|·sin(ωt + φ) = 5 × 1.47 sin(2t − 1.37) = 7.35 sin(2t − 1.37), X = 5, φ = ∠T(jω) = −1.37 rad

### Örnek 5(a): Birim olmayan geri besleme

G(s) = 2/(s² + 3s), H(s) = 5s + 2. Önce eşdeğer birim geri beslemeli yapı:

- G/(1 + GH) = Ge/(1 + Ge) ⇒ Ge = G/[1 + G(H − 1)]
- Ge(s) = [2/(s² + 3s)]/{1 + [2/(s² + 3s)](5s + 2 − 1)} = 2/(s² + 13s + 2)
- Orijinde kutup yok ⇒ 0. tip
- Kp = Ge(0) = 1, Kv = lim sGe(s) = 0, Ka = lim s²Ge(s) = 0

r(t) = 1, t, t² için kalıcı durum hatası (W(s) hata ile giriş arasındaki aktarım işlevi, W = 1/(1 + Ge) = (s² + 13s + 2)/(s² + 13s + 4)):

- Birim basamak: ess = lim s·(1/s)·W(s) = 1/2 = 1/(1 + Kp)
- Birim rampa: ess = ∞
- Parabolik (R = 2/s³): ess = ∞

Beklendiği gibi, eşdeğer sistem 0. tip olduğundan yalnız r(t) = 1 için ess sonlu.

Bir sonraki sayfanın başında duyarlılık bağıntısı da not edilmiş: |ΔT(s)/T(s)| = |S_K^T(s)|·|ΔK/K|, s = jω.

## Bölüm 5: Kararlılık (Routh tablosu)

### Örnek 3a: Birinci sütunda sıfır

- Δ(s) = s⁵ + 2s⁴ + 2s³ + 4s² + 11s + 10 = 0
- Routh: s⁵: 1, 2, 11; s⁴: 2, 4, 10; s³: ε, 6, 0; s²: c₁, 10; s¹: d₁; s⁰: 10
- c₁ = (4ε − 12)/ε ≅ −12/ε (ε → 0₊ iken 4ε sıfıra gidiyor), d₁ = (6c₁ − 10ε)/c₁ ≅ 6
- Birinci sütunda iki işaret değişimi ⇒ sağ yarı düzlemde (RHP) iki kök

### Örnek 3b: Tamamen sıfır satır

- Δ(s) = s⁵ + 2s⁴ + 24s³ + 48s² − 25s − 50 = 0
- s⁵: 1, 24, −25; s⁴: 2, 48, −50; s³: 0, 0 (tamamen sıfır satır)
- Bir üst satırdan yardımcı denklem: A(s) = 2s⁴ + 48s² − 50, dA(s)/ds = 8s³ + 96s ⇒ s³ satırı 8, 96
- Devamı: s²: 24, −50; s¹: 112.7, 0; s⁰: −50
- Bir işaret değişimi ⇒ RHP'de bir kök. Çarpanlara ayrılmış hali: Δ(s) = (s + 1)(s − 1)(s + j5)(s − j5)(s + 2)

Kenar notu: Kararlı polinomlara Hurwitz polinomu denir; tamamen sıfır satır çıkınca yardımcı denklem yazılıp türeviyle tablo yeniden oluşturulur.

### Örnek 4: Kararlılık için K aralığı

Birim geri beslemeli sistem, G(s) = K/[s(s + 2)(s² + s + 1)]:

- CLTF: C(s)/R(s) = K/[s(s + 2)(s² + s + 1) + K]
- CLCE: Δ(s) = s⁴ + 3s³ + 3s² + 2s + K = 0
- Routh: s⁴: 1, 3, K; s³: 3, 2; s²: 7/3, K; s¹: 2 − 9K/7; s⁰: K
- Kapalı çevrim kararlılığı için 0 < K < 14/9; kritik kazanç Kc = 14/9
- Yardımcı denklem (7/3)s² + 14/9 = 0 ⇒ s² + 2/3 = 0 ⇒ s₁,₂ = ±j√(2/3) = ±j0.82 ⇒ ωp = 0.82 rad/s

### Örnek 5: Eksen kaydırma

- Δ(s) = s⁴ + 6s³ + 12s² + 11s + 6 = (s + 2)(s + 3)(s² + s + 1)
- Routh: s⁴: 1, 12, 6; s³: 6, 11; s²: 61/6, 6; s¹: 455/61; s⁰: 6 ⇒ bütün kökler sol yarı düzlemde (LHP)
- Kenar notu: İkinci dereceden polinomlarda katsayıların aynı işaretli olması kararlılık için gerek ve yeter koşuldur.

s = −1 doğrusunun sağında kök olup olmadığını bulmak için s yerine (p − 1) konuyor (jω ekseni −1'e kaydırılıp yeni eksene jν deniyor):

- Δ(p) = (p − 1)⁴ + 6(p − 1)³ + 12(p − 1)² + 11(p − 1) + 6 = p⁴ + 2p³ + p + 2
- Routh: p⁴: 1, 0, 2; p³: 2, 1; p²: −1/2, 2; p¹: 9; p⁰: 2
- İki işaret değişimi ⇒ s = −1 doğrusunun sağında iki kök var (−1/2 ± j√3/2). Kaydırmadan önce −3 ve −2'de olan kökler kaydırmadan sonra −2 ve −1'de.

## Kök yer eğrisi

### Örnek 6(a)

- CLCE: Δ(s) = s³ + 7s² + 16s + K + 10 = 0 ⇒ 1 + K/(s³ + 7s² + 16s + 10) = 0
- Eşdeğer OLTF: K/[(s + 1)(s² + 6s + 10)] = K/[(s + 1)(s + 3 ± j)]
- Açık çevrim kutupları: −1, −3 ± j (n = 3), sıfır yok (m = 0)
- Asimptotlar: θk = (2k + 1)π/(n − m) = 60°, 180°, 300°; σa = (−1 − 3 − 3)/3 = −2.33
- jω ekseni kesişimi, Routh: s³: 1, 16; s²: 7, K + 10; s¹: [112 − (K + 10)]/7; s⁰: K + 10 ⇒ Km = 102. Yardımcı denklem 7s² + 112 = 0 ⇒ s² + 16 = 0 ⇒ s₁,₂ = ±j4
- Ayrılma noktası: K = −s³ − 7s² − 16s − 10 ⇒ dK/ds = −(3s² + 14s + 16) = 0 ⇒ s₁,₂ = −2, −2.67
- Kalkış açısı (−3 + j kutbundan): θd = 180° − Σθpj + Σθzi = 180° − 90° − 153° = −63°

Çizimde karmaşık kutuplardan çıkan iki kol −63° ile ayrılıp −2.67'de gerçek eksene iniyor (K ≈ 1.85); biri −∞'a gidiyor, diğeri sağa ilerleyip −1'den gelen kolla −2'de buluşuyor (K = 2). Bu iki kol −2'den yeniden ayrılıp K = 102'de ±j4'ten sanal ekseni kesiyor.

### Örnek 6(b): ζ = 0.7 için K

ζ = 0.7 ⇒ ζ = cos θ, θ = 45°. Kapalı çevrim kutupları {−b, −a ± ja} biçiminde:

- Δ(s) = (s + b)(s² + 2as + 2a²) = s³ + (2a + b)s² + (2a² + 2ab)s + 2a²b = s³ + 7s² + 16s + (K + 10)
- 2a + b = 7, 2a² + 2ab = 16, 2a²b = K + 10 ⇒ b = 7 − 2a, a² − 7a + 8 = 0 ⇒ a = 1.4384 (ya da 5.5616)
- b = 4.1232, K = 7.06; kapalı çevrim kutupları −4.12 ve −1.44 ± j1.44

Kutuplar verildiğinde K genlik koşuluyla da bulunabilir: 1 + KGH(s) = 0 ⇒ |GH(s)| = 1/|K|, yani

- K = |(s + 1)(s + 3 + j)(s + 3 − j)| (s = −1.44 + j1.44) = |(−0.44 + j1.44)(1.56 + j2.44)(1.56 + j0.44)| = 1.506 × 2.896 × 1.621 = 7.07

### Örnek 7: Parametreye göre değişen kök yer eğrileri

- (i) KG(s) = K/[(s − a)(s² − 2bs + b² + c²)] = K/[(s − a)(s − b + jc)(s − b − jc)]: a = b + √3c iken üç kol tek noktada buluşuyor (örneğin b = −4, c = 1 için a = −0.54); a < b + √3c, a > b + √3c ve a = 0 durumları için eğrinin biçimi çizilmiş.
- (ii) KG(s) = K(s + 1)/[s²(s + a)] için a = 3, 7, 9 ve 11 durumlarının kök yer eğrileri karşılaştırılmış; a = 9 ve a = 11 çizimlerinde kollar −1'deki sıfırın çevresinde çember çiziyor.
- (iii) KG(s) = K(s + a)/[s(s + 1)(s² + 4s + 8)] için a = 1.296 civarında kolların birleştiği özel durum çizilmiş.

### Örnek 8: Horner dizisi ve Newton yöntemiyle kök bulma

p(s) = s³ + 7s² + 15s + 10 için ilk tahmin s₁ = −1:

- Horner (−1): 1, 6, 9, r₁ = 1; ikinci kez: 1, 5, r₂ = 4
- s₂ = s₁ − r₁/r₂ = −1 − 1/4 = −1.25
- Horner (−1.25): 1, 5.75, 7.813, r₃ = 0.234; ikinci kez: 1, 4.5, r₄ = 2.188
- s₃ = s₂ − r₃/r₄ = −1.25 − 0.234/2.188 = −1.357
- p(s)'nin gerçek kökleri: −1.382, −2, −3.618

### Örnek 9: Tamsayı köklerin bulunması

Örnek 3b'deki Δ(s) = s⁵ + 2s⁴ + 24s³ + 48s² − 25s − 50 = 0 için tamsayı gerçek kökler 50'nin bölenleri arasında olmalı. Horner dizisiyle:

- s = 1: 1, 3, 27, 75, 50, kalan 0
- s = −1: 1, 2, 25, 50, kalan 0 ⇒ geriye s³ + 2s² + 25s + 50 kalıyor
- Yardımcı denklemden (s² + 25)'in de çarpan olduğu biliniyor: (s³ + 2s² + 25s + 50)/(s² + 25) = s + 2 (ya da −2 ile Horner: 1, 0, 25, kalan 0)
- Δ(s) = (s + 1)(s − 1)(s² + 25)(s + 2) = 0

*Not: Defterde Örnek 9 "From Exa. 4" diye başlıyor; polinom Örnek 3b'ninki.*
