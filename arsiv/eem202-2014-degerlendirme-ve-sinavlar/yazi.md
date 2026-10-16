---
baslik: EEM202 Devre Teorisi II: 2013-2014 Bahar Değerlendirme Ölçütleri, Kısa Sınav III ve Dönem Sonu Sınavı Çözümleri
ozet: EEM202 Devre Teorisi II 2013-2014 bahar dönemi: not dağılımı (kısa sınav, ödev, ara sınav, final), 16 Mayıs 2014 Kısa Sınav III soruları ve dönem sonu sınavına ait notlandırılmış bir cevap kâğıdının çözümleri (rms güç, Thevenin–Norton ile maksimum güç, ideal trafo, üç fazlı sistem, Laplace ile devre analizi).
---

Bu yazı, Başkent Üniversitesi Elektrik-Elektronik Mühendisliği **EEM202 Devre Teorisi II** dersinin 2013-2014 bahar dönemine ait üç belgeyi bir araya getiriyor: derste gösterilen **değerlendirme** slaytı (18 Şubat 2014), Yrd. Doç. Dr. Selda Güney'in **Kısa Sınav III** soru kâğıdı (16 Mayıs 2014) ve dönem sonunda fotoğraflanmış (13 Haziran 2014), hocanın kırmızı kalemle puanladığı **dört sayfalık bir sınav cevap kâğıdı**. Hepsi fotoğraflanmış sayfalardan metne aktarıldı; fotoğrafların kendisi yayınlanmıyor ve kâğıtlardaki ad-numara bilgileri metne geçirilmedi. Bu yazının indirilebilir dosyası yok.

## Değerlendirme

Dönemin ilk haftasında gösterilen slayttaki not dağılımı:

| Bileşen | Ağırlık |
| --- | --- |
| Katılım | %3 |
| Kısa sınavlar | %15 |
| Ödevler | %7 |
| Ara sınav | %35 |
| Final | %40 |

Devam zorunluluğu: **%70**.

## Kısa Sınav III (16.05.2014)

1. Aşağıdaki şekildeki devrede Z₀ empedansına maksimum güç aktarılması için Z₀ empedansının hangi değerde olması gerektiğini hesaplayınız. (Devre: 30∠0° V (rms) kaynak, 15 Ω direnç, j30 Ω ve j15 Ω'luk iki bobin, aralarında j18 Ω'luk karşılıklı endüktans.)
1. Aşağıdaki Y-Δ bağlı, pozitif sıralı (abc) devrede (kaynak fazları 1365∠0°, 1365∠−120° ve 1365∠120° V; her hatta j2 Ω + 1,5 Ω; üçgen yükün her kolu 85,5 Ω + j114 Ω) şunları bulunuz:

- a) Hat akımlarını (I_aA, I_bB, I_cC) ve faz akımlarını (I_AB, I_BC, I_CA) hesaplayınız.
- b) Kaynağın faz başına ürettiği kompleks gücü hesaplayınız.
- c) Kaynağın ürettiği aktif gücün yüzde kaçı yükte harcanmaktadır, hesaplayınız.

Bu sınavın cevap anahtarı arşivdeki [Kısa Sınav Soruları ve Cevap Anahtarları](/arsiv/eem202-kisa-sinav-cozumleri/) yazısında çözümleriyle birlikte yer alıyor.

## Dönem sonu sınavı: notlandırılmış cevap kâğıdı

Kâğıtta soru metinleri yok; aşağıda her sorunun ne istediği çözümden çıkarılarak yazıldı, ardından cevap kâğıdındaki hesaplar ve sonuçlar verildi. Parantez içindeki puanlar hocanın kâğıda verdiği puanlardır.

### Soru 1: Periyodik bir gerilimin rms değeri ve güç (20 puan)

T = 10 s periyotlu gerilim: 0 ≤ t ≤ 2 s'de v = −5t, 2–4 s'de −10 V, 4–5 s'de 0, 5–10 s'de 10 V. R = 2 Ω'luk dirençte harcanan ortalama güç P = V_rms²/R:

- V_rms = [ (1/10) ( ∫₀² 25t² dt + ∫₂⁴ 100 dt + ∫₅¹⁰ 100 dt ) ]^(1/2)
- = [ (1/10)(66,67 + 200 + 500) ]^(1/2) = √76,67 ≈ 8,76 V
- **P = 76,67/2 = 38,33 W**

### Soru 2: Thevenin–Norton eşdeğeri ve maksimum güç (8 + 7 + 5 puan)

100∠0° V (rms) kaynak, iki 5 Ω direnç, −j5 Ω kondansatör, j5 Ω bobin ve 0,1V_φ bağımlı akım kaynağından oluşan devre:

- Açık devre: (V_φ − 100)/5 + V_φ/(j5) − 0,1V_φ = 0 → V_φ(0,5 − j) = 100 → V_φ = 40 + j80 V
- **V_Th** = 0,1V_φ(−j5) + V_φ = V_φ(1 − j0,5) = **80 + j60 V (rms)**
- Kısa devre: V_φ = 100 V, I_N = 0,1V_φ + V_φ/(−j5) = (0,1 + j0,2)V_φ = **10 + j20 A (rms)**
- **Z_Th** = V_Th/I_N = (80 + j60)/(10 + j20) = **4 − j2 Ω**
- Maksimum güç için Z_y = Z_Th* = **4 + j2 Ω**

Devamında yükteki güç: I = (80 + j60)/8 = 10 + j7,5 A (rms), S = Z·|I|² = (4 + j2)(10 + j7,5)(10 − j7,5) = **625 + j312,5 VA**, yani **P = 625 W**, **Q = 312,5 VAr**.

### Soru 3: İdeal trafolu devre (10 + 5 + 5 puan)

300 V kaynak, primerde 60 Ω, primer ile sekonder çevresi arasında ortak 20 Ω, sekonderde 40 Ω; ideal trafo için V₂ = V₁/4 ve I₂ = −4I₁:

- 300 = 60I₁ + V₁ + 20(I₁ − I₂), 0 = 20(I₂ − I₁) + V₂ + 40I₂
- Yerine koyunca: 300 = 160I₁ + V₁ ve V₁ = 1040I₁
- **I₁ = 0,25 A, V₁ = 260 V, I₂ = −1 A, V₂ = 65 V**
- P₂₀ = (I₁ − I₂)²·20 = 1,25²·20 = **31,25 W**, P₄₀ = 1²·40 = **40 W**

### Soru 4: Üç fazlı sistem (2 + 3 + 3 + 6 + 3 + 3 puan)

Hat gerilimi V_AB = 7200 V, hat empedansı 0,5 + j4 Ω, yükte paralel iki dengeli yük (Z₁ ve Z₂ = 207,36 + j60,48 Ω):

- V_AN = 7200/(√3∠−30°) = **4156,92∠30° V** (kâğıttaki yazımla)
- Birinci yük: S₁ (üç faz) = 691,2 − j201,6 kVA → faz başına 230,4 − j67,2 kVA; θ = arctan(−201,6/691,2) = −16,26°, güç çarpanı 0,96 (ileri). P₁ = V_AN·I₁·cos θ → 230,4·10³ = 4156,92·I₁·0,96 → **I₁ = 57,73∠46,26° A**
- İkinci yük: I₂ = V_AN/Z₂ = 4156,92∠30° / 216∠16,26° = **19,2∠13,74° A**
- **I_aA** = I₁ + I₂ = 58,65 + j46,26 = **74,7∠38,26° A**; kâğıtta I_bB = 74,7∠158,26° A, I_cC = 74,7∠−81,73° A
- V_an = (0,5 + j4)(58,65 + j46,26) + V_AN = 3444,28 + j2336,24 = **4161,72∠34,14° V**
- Kâğıtta V_ab = 7208,3∠64,14° V, V_bc = 7208,3∠124,14° V, V_ca = 7208,3∠−115,86° V

*Not: Soru metni elimizde olmadığı için faz sırası bilinmiyor. Kâğıttaki V_AN = V_AB/√3∠+30° ilişkisi ve I_bB'nin I_aA'dan 120° ileride olması negatif (acb) sıraya uyar; bu durumda V_ab = √3·V_an∠−30° = 7208,3∠4,14° V olmalıdır. Kâğıttaki V_ab = 7208,3∠64,14° V ise pozitif sıradaki ∠+30° ilişkisiyle bulunmuş; V_bc ve V_ca açıları da (124,14° ve −115,86°) iki faz sırasından biriyle tutarlı değil (hat gerilimleri arasında 120° olmalı). Akım ve gerilimlerin büyüklükleri doğru.*

### Soru 5: Laplace dönüşümüyle devre analizi (5 + 5 + 5 + 5 puan)

s bölgesinde devre: 1/s'lik kondansatör (C = 1 F) ve 2 Ω, 2/s A'lik akım kaynağı, s'lik bobin (L = 1 H), 12/s V'luk gerilim kaynağı ve çıkış direnci 2 Ω. Çevre akımları I₁ ve I₂ ile:

- I₁(2 + 1/s) = V₁, V₁ + (2 + s)I₂ + 12/s = 0, akım kaynağından I₁ − I₂ = 2/s
- I₁(s² + 4s + 1) = 2s + 16 → I₁ = (2s + 16)/(s² + 4s + 1); kökler s = −0,27 ve s = −3,73
- I₂ = I₁ − 2/s = K₁/(s + 0,27) + K₂/(s + 3,73) − 2/s; K₁ = 15,46/3,46 = 4,46, K₂ = 8,54/(−3,46) = −2,46
- V_o = 2I₂ = 8,92/(s + 0,27) − 4,92/(s + 3,73) − 4/s
- **v_o(t) = [−4 + 8,92e^(−0,27t) − 4,92e^(−3,73t)] u(t) V**

Kontrol: v_o(0⁺) = −4 + 8,92 − 4,92 = 0 ve v_o(∞) = −4 V.
