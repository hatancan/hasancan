---
baslik: MAT340 Olasılık ve İstatistik: Kısa Sınav (Quiz) Soruları ve Çözümleri, 2007–2010
ozet: Başkent Üniversitesi MAT340 Olasılık dersi quiz anahtarları (2007-2010): koşullu olasılık, kombinasyon, sürekli ve bileşik dağılımlar, binom ve normal dağılım uygulamaları, beklenen değer, varyans ve rassal değişken dönüşümleri; çözümlü.
---

Başkent Üniversitesi Elektrik-Elektronik Mühendisliği **MAT 340 Olasılık** dersinin 2007–2010 yıllarına ait quiz kâğıtları ve **anahtarları**. Dersin hocaları Öğr. Gör. Pelin Toktaş ve (2010'da) Prof. Dr. Fulya Altıparmak'tır (iki grup). Sorular ve çözümler elle yazılmış taranmış anahtarlardan metne aktarılmış, hesaplar kontrol edilmiştir. Orijinal taramalar yazının sonundaki ZIP dosyasındadır (2010 Quiz 2 ve Quiz 3 çözümleri fotoğraf/tarama dosyası olarak geldiğinden ZIP dışındadır; yalnız metne aktarıldı).

## Quiz 1 – 19 Ekim 2007: nükleer santral (koşullu olasılık)

Bir nükleer santral A, B ve C olmak üzere 3 sistemden oluşmaktadır. A ve B sistemleri veya A ve C sistemleri bozulursa santral kapatılmaktadır. A, B, C sistemleri birbirinden bağımsız olarak sırasıyla 0,01, 0,03 ve 0,02 olasılıkla bozulmaktadır. (a) Santralin çalışıyor olma olasılığı? (b) A sisteminin çalışmıyor olduğu bilindiğine göre santralin çalışıyor olma olasılığı? (c) Santralin çalışmadığı bildirildiğinde B sisteminin çalışıyor olma olasılığı?

**Çözüm.** Sekiz durumun olasılıkları (A, B, C çalışıyor ise sırasıyla 0,99; 0,97; 0,98 ile çarpılır): ✓✓✓ 0,941094; ✓✓✗ 0,019206; ✓✗✓ 0,029106; ✓✗✗ 0,000594; ✗✓✓ 0,009506; ✗✓✗ 0,000194; ✗✗✓ 0,000294; ✗✗✗ 0,000006. Santral ilk beş durumda çalışır.

- (a) P(santral çalışıyor) = 0,941094 + 0,019206 + 0,029106 + 0,000594 + 0,009506 = **0,999506**
- (b) P(çalışıyor | A bozuk) = 0,009506 / 0,01 = **0,9506**
- (c) P(B çalışıyor | santral çalışmıyor) = 0,000194 / (1 − 0,999506) = 0,000194 / 0,000494 = **0,3927**

## Quiz 2 – 30 Ekim 2008: sürekli dağılım

f(x) = x/4 (0 < x ≤ 2), 3 − x (2 < x ≤ 3), 0 (diğer). (a) P(1 < X ≤ 5/2)? (b) Birikimli dağılım fonksiyonunu bulup P(X > 2,1)'i hesaplayınız. (c) E(X)? (d) P(X = 2)?

- (a) ∫₁² x/4 dx + ∫₂^2,5 (3 − x) dx = 3/8 + 3/8 = **0,75**
- (b) F(x) = 0 (x ≤ 0); x²/8 (0 < x ≤ 2); −7/2 + 3x − x²/2 (2 < x ≤ 3); 1 (x > 3). P(X > 2,1) = 1 − F(2,1) = **0,405**
- (d) P(X = 2) = **0** (sürekli rassal değişkende noktasal olasılık sıfırdır).
- (c) Anahtardaki hesap E(X) = 3/2 bulmuş; ancak ∫₀² x·(x/4) dx = x³/12 |₀² = 2/3'tür (anahtarda "1/3" yazılmış).

*Not: Doğru değer E(X) = 2/3 + ∫₂³ (3x − x²) dx = 2/3 + 7/6 = **11/6**'dır; anahtardaki 3/2 değeri hatalıdır.*

## Quiz 1 – 12 Ekim 2010: kombinasyon ve röle zinciri

1. 10 erkek ve 5 kız öğrenciden oluşan sınıfta: (a) 6 kişilik komisyon kaç şekilde seçilir? **C(15,6) = 5005**. (b) Her komisyonda en az bir kız olursa? 5005 − C(10,6)·C(5,0) = 5005 − 210 = **4795**. (c) Belirli bir erkek ile belirli bir kız aynı komisyonda olmak istemiyorsa? 5005 − C(13,4)·C(2,2) = 5005 − 715 = **4290**.
2. Verici ikili kodla mesaj gönderiyor; her veri alıcıya ulaşmadan önce 3 röleden geçiyor, her rölede 0,20 olasılıkla hata yapılıyor (röleler bağımsız). (a) Vericiden "1" gönderilince üç röleden de "1" çıkma olasılığı: 0,8³ = **0,512**. (b) Alıcıdan "1" alınma olasılığı (ağaç diyagramı): çift sayıda hata olmalı: 0,8·0,8·0,8 + 3 · 0,2 · 0,2 · 0,8 = 0,512 + 0,096 = **0,608**.

## Quiz 3 – 9 Kasım 2010: beklenen değer ve varyans

1. E(X) = 19, E(Y) = 25, Var(X) = 25, Var(Y) = 144, ρ_XY = −1/2 ise: Cov(X,Y) = −30. (a) Var(X − Y) = 25 + 144 − 2(−30) = **229**. (b) E(XY) = −30 + 19·25 = 445, E(−2XY + 3) = **−887**. (c) Z = −X − 5Y: E(Z) = **−144**, Var(Z) = 25 + 25·144 + 10·(−30) = **3325**.
2. X: −3, 6, 9 değerlerini 1/6, 1/2, 1/3 olasılıkla alıyor; g(X) = −3X − 1. E(X) = 5,5; E(X²) = 46,5; Var(X) = 16,25. E[g(X)] = **−17,5**, Var[g(X)] = 9 · 16,25 = **146,25**.

## Quiz 2 (26 Ekim 2010 grubu) – birikimli dağılım ve bileşik dağılım

1. 2008 quizindeki aynı yoğunluk için (a) P(1 < X ≤ 5/2) = 0,75, (b) F(x) ve P(X > 2,1) = 0,405, (c) P(X = 2) = 0.
2. f(x, y) = c(x + y), 0 < x < y < 1. (a) ∫∫ = c/2 = 1 → **c = 2**. (b) Marjinal h(y) = ∫₀^y 2(x + y) dx = 3y²; f(x|y) = 2(x + y)/(3y²). P(X > 0,6 | Y = 0,8) = (1/0,96) ∫₀,₆^0,₈ (x + 0,8) dx = 0,30/0,96 ≈ **0,3125**.

## Quiz 4 – 23 Kasım 2010: binom dağılımı (tekrarlama kodu)

Bir haberleşme sisteminde 0 yerine 00000, 1 yerine 11111 gönderiliyor; gürültü yüzünden her veri bağımsız olarak 0,2 olasılıkla hatalı iletiliyor; alıcı çoğunluğa göre çözüyor (örn. 01001 → 0). (a) Önemli bir mesajın hatalı alınma olasılığı? X ~ Binom(5; 0,2), P(X ≥ 3) = 1 − P(X ≤ 2) = 1 − 0,94208 = **0,05792**. (b) Birbirinden bağımsız gönderilen 4 mesajdan 2'sinin hatalı alınması? p ≈ 0,06, Y ~ Binom(4; 0,06): C(4,2)(0,06)²(0,94)² ≈ **0,0191**.

(Kâğıtta ayrıca kesikli düzgün, Bernoulli, binom, hipergeometrik, negatif binom ve geometrik dağılımların olasılık fonksiyonu, ortalama ve varyans formülleri yer alır.)

## Quiz 5 – 14 Aralık 2010: normal dağılım

X ~ N(110, 10²) bir bilgisayarın güç kaynağından geçen voltajdır. Bilgisayar 100 V altında 0,01; 100–120 V arasında 0,001; 120 V üstünde 0,05 olasılıkla bozulmaktadır. P(V₁) = P(X < 100) = 0,1587; P(V₂) = P(100 < X < 120) = 0,6826; P(V₃) = P(X > 120) = 0,1587.

- (a) P(bozulma) = 0,1587·0,01 + 0,6826·0,001 + 0,1587·0,05 ≈ **0,0102**
- (b) P(V₃ | bozuldu) = (0,1587·0,05)/0,0102 ≈ **0,778**
- (c) Voltajın en düşük %15'lik dilimi için üst sınır: z = −1,04 → x* = 110 − 10,4 = **99,6 V**

## Quiz 6 – 2010: rassal değişken dönüşümü

1. f(x) = 2x e^(−x²), 0 < x < ∞; Y = X² ise: x = √y, |J| = 1/(2√y); g(y) = 2√y e^(−y) · 1/(2√y) = **e^(−y), 0 < y < ∞** (üstel dağılım).
2. f(x₁, x₂) = x₁x₂/36, x₁, x₂ = 1, 2, 3; Y₁ = X₁X₂, Y₂ = X₂. (a) Bileşik dağılım g(y₁, y₂) = y₁/36 (y₁ = 1, 2, 3, 4, 6, 9; y₂ = 1, 2, 3; y₁ = x₁y₂):

| g(y₁, y₂) | y₁ = 1 | 2 | 3 | 4 | 6 | 9 |
|---|---|---|---|---|---|---|
| y₂ = 1 | 1/36 | 2/36 | 3/36 | 0 | 0 | 0 |
| y₂ = 2 | 0 | 2/36 | 0 | 4/36 | 6/36 | 0 |
| y₂ = 3 | 0 | 0 | 3/36 | 0 | 6/36 | 9/36 |

(b) Y₁'in marjinal dağılımı: f(1) = 1/36, f(2) = 4/36, f(3) = 6/36, f(4) = 4/36, f(6) = 12/36, f(9) = 9/36.
