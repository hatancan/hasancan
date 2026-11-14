---
baslik: EEM441 Haberleşme I: 2013 yaz okulu ara sınavı (2 Ağustos 2013) ve çözümleri
ozet: Başkent Üniversitesi EEM 441 Haberleşme Sistemleri I yaz okulu ara sınavı: SSB zarf alıcısı, bant geçiren sinyalin zarf ve fazı, FM spektrumu ve frekans çoklayıcı tasarımı; el yazısı çözümlerle.
---

Başkent Üniversitesi Elektrik-Elektronik Mühendisliği Bölümü, EEM 441 Haberleşme Sistemleri I dersinin 2 Ağustos 2013 tarihli yaz okulu ara sınavı (süre 2 saat). Sınav kâğıdı, sınavla birlikte verilen Bessel fonksiyonları formül sayfası ve el yazısı çözümler aşağıda metne dökülmüştür. Sınav kâğıdı ve çözümler fotoğraflanmış sayfalardan metne aktarıldı; fotoğraflar yayınlanmamıştır. Bu nedenle indirilebilir orijinal dosya yoktur. Kişisel bilgiler (öğrenci numarası, ad) çıkarılmıştır.

## Sorular

1. Bir SSB alıcı sisteminde ton modüleli SSB sinyaline A_LO cos(ω_c t) sinyali eklenerek zarf alıcı devresinin girişine uygulanmaktadır. Lokal osilatörde frekans hatası olmadığı, yalnız φ′ faz hatası olduğu kabul edilsin. A_LO ≫ A_c A_m alınarak zarf alıcı çıkışındaki sinyali hesaplayın ve fazör şemasını çizin. (Şekil: s(t) SSB → toplayıcı (+ A_LO cos(ω_c t + φ′)) → zarf alıcı → A(t).)
2. Bant geçiren bir iletişim sisteminde verici çıkışındaki sinyalin aynı fazlı bileşeni s_i(t), dikgen bileşeni s_q(t), zarfı A(t) ve fazı φ(t) olmak üzere s_bp(t) = s₁(t) cos(ω_c − 3ω₀)t + s₂(t) cos(ω_c + 3ω₀)t sinyali için fazör şemasını kullanarak bunları hesaplayın.
3. Bir radyo vericisinde FM modüleli sinyale ait parametreler f_m = 20 kHz, β = 1, A_c = 100, f_c = 40 kHz alınmıştır. s(t) formülünü türetin, frekans spektrumunu çizin, S_T > A_c²/2 olduğunu gösterin ve sistemin bant genişliğini hesaplayın.
4. f_c ≫ f_m olan bir FM radyo vericisinde parametreler f_m = 4 kHz, β = 3, f_c1 = 100 kHz, Δf₁ = 16,5 Hz ve f_c = 10 MHz olacak şekilde tasarlanmıştır. Frekans çoklayıcı sistemi yalnız üçlü çarpıcılardan oluşmaktadır; bütün bant geçiren filtreler 0,01 < B/f_c < 0,1 koşulunu sağlamaktadır. Bütün Δf ve f_LO değerlerini, filtrelerin bant genişliklerini ve merkez frekanslarını hesaplayıp sistem şemasını çizin; frekansı aşağı kaydırıcıyı hiçbir frekans 13,5 MHz'i aşmayacak şekilde yerleştirin.

## Bessel fonksiyonları formül sayfası

Sınavla birlikte verilen sayfada J_n(β) birinci tür Bessel fonksiyonu grafikleri (n = 0…4, β = 0…18) ve şu bağıntılar yer alır:

- J_n(β) = (1/2π) ∫ exp[j(β sin x − n x)] dx (−π…π)
- J_n(β) = (−1)ⁿ J₋ₙ(β)
- β → 0 için J_n(β) ≈ βⁿ / (2ⁿ n!); J₀ → 1, J₁ → β/2, J₂ → β²/8
- β → ∞ için J_n(β) ≈ √(2/(πβ)) cos(β − π/4 − nπ/2)
- Σ J_n²(β) = 1 (n = −∞…∞)
- J_n(jβ) = jⁿ I_n(β), I_n(β) = (1/2π) ∫ exp[β cos θ] cos(nθ) dθ
- s(t) = A_c Re[Σ J_n(β) exp(j2π(f_c + n f_m)t)] = A_c Σ J_n(β) cos[2π(f_c + n f_m)t]
- SSB: s(t) = (A_c/2) m(t) cos ω_c t ∓ (A_c/2) m̂(t) sin ω_c t
- FM: s(t) = A_c cos[2π f_c t + β sin(2π f_m t)]

## Çözüm 1: SSB sinyaline taşıyıcı eklenmesi

Ton modüleli SSB: s(t) = (A_c/2)(A_m cos ω_m t) cos ω_c t ∓ (A_c/2)(A_m sin ω_m t) sin ω_c t; burada x(t) = A_m cos ω_m t, x̂(t) = A_m sin ω_m t. Bu, f_c ± f_m'de tek bir çizgidir ve genliği a = ½ A_c A_m'dir. Toplayıcıya A_LO cos(ω_c t + φ′) eklenir. Fazör şemasında A_LO fazörü φ′ açısındadır; ona a genlikli ve ±ω_m t ile dönen fazör eklenir, bileşke A(t)'dir.

A²(t) = (A_LO cos φ′ + a cos ω_m t)² + (A_LO sin φ′ ± a sin ω_m t)²
= A_LO² + a² + 2 A_LO a (cos ω_m t cos φ′ ± sin ω_m t sin φ′)
= A_LO² + a² + 2 A_LO a cos(ω_m t ∓ φ′)

A(t) = A_LO [1 + (a/A_LO)² + (2a/A_LO) cos(ω_m t ∓ φ′)]^½ ≈ A_LO + ½ A_c A_m cos(ω_m t ∓ φ′).

Yani A_LO ≫ a iken zarf alıcı çıkışı, DC terim artı ½ A_c A_m cos(ω_m t ∓ φ′)'dir: bilgi sinyali kurtarılır, yalnız φ′ kadar faz kayması (bozulma değil gecikme) taşır.

## Çözüm 2: Bant geçiren sinyalin zarfı ve fazı

Kâğıttaki çözüm, iki bileşeni ω₀ kaymasıyla yazar (kaynakta ω₀ olarak çalışılmıştır):

- v_i(t) = [v₁(t) + v₂(t)] cos ω₀ t
- v_q(t) = [v₂(t) − v₁(t)] sin ω₀ t
- A(t) = √(v₁²(t) + 2 v₁(t) v₂(t) cos 2ω₀ t + v₂²(t))
- φ(t) = arctan{[v₂(t) − v₁(t)] sin ω₀ t / ([v₁(t) + v₂(t)] cos ω₀ t)}

Fazör şemasında v₁ ve v₂ zıt yönlerde ω₀ t ile dönen iki fazördür; v₁ ≫ v₂ olduğunda A(t) ≈ v₁(t) + v₂(t) cos 2ω₀ t ve φ(t) ≈ −ω₀ t olur.

*Not: Soru kâğıdında kayma 3ω₀ yazılıdır, çözüm kâğıdı ise ω₀ ile çalışır; çözümdeki ifadeler soruya göre ω₀ yerine 3ω₀ konarak okunmalıdır. Kâğıttaki yaklaşık A(t) ifadesinin ikinci teriminde çarpan okunaksızdır; burada v₂(t) olarak yazıldı.*

## Çözüm 3: FM, β = 1, f_m = 20 kHz, A_c = 100, f_c = 40 kHz

s(t) = A_c cos[2π f_c t + β sin 2π f_m t] = 100 cos[2π·40·10³ t + 1·sin(2π·20·10³ t)].

a) Ani frekans: f_i(t) = (1/2π) dθ_i/dt = f_c + β f_m cos ω_m t = 40 + 20 cos ω_m t kHz.

b) Bessel tablosu J_n(1): J₀ = 0,7652 (≈ 0,77), J₁ = 0,4401 (≈ 0,44), J₂ = 0,1149 (≈ 0,11), J₃ = 0,0196 (≈ 0,02), J₄ ≈ 0.

Çizgi genlikleri A_c J_n: n = 0 → 77 (40 kHz), n = 1 → 44 (60 kHz), n = 2 → 11 (80 kHz), n = 3 → 2 (100 kHz). Alt yan bantlar: n = −1 → −44 (20 kHz), n = −2 → +11 (0 Hz, yani DC), n = −3 → −2 (−20 kHz). Negatif frekansa düşen bileşen katlanarak 20 kHz'e gelir: −44 − 2 = −46. Katlanmış bileşenler |f_c − 3f_m| = 20 kHz ve |f_c − 2f_m| = 0'dadır.

Toplam güç (DC bileşeni 11² ve AC bileşenleri ½ genlik²): S_T = 11² + ½[(−46)² + 77² + 44² + 11² + 2²] ≈ 5170 > A_c²/2 = 100²/2 = 5000. Katlanmış (aliasing) bileşenlerin toplam güce eklenmesi nedeniyle S_T, sinyalin gerçek gücü olan A_c²/2'den büyük çıkar; kâğıtta gösterilen eşitsizlik budur. Spektrumdan bant genişliği 2·3·f_m = 120 kHz olarak okunur.

*Not: Kaynak tabloda J₃(1) “0,196 ≈ 0,2” yazılıdır; doğru değer 0,0196'dır (çizgi genliği 100×0,0196 ≈ 2 ile uyumludur). Kâğıtta bant genişliği için “120 kHz yerine 100 kHz okundu” şeklinde düzeltme notu vardır; Carson kuralıyla B ≈ 2(β + 1)f_m = 80 kHz bulunur, hesapta 3. yan banda kadar çizgiler alındığından 120 kHz yazılmıştır.*

## Çözüm 4: Frekans çoklayıcı zinciri

n = 3⁶ = 729, Δf = β f_m = 3×4 kHz = 12 kHz. Başlangıç sapması Δf₀ = Δf/n = 12 kHz / 729 = 16,461 Hz (verilen 16,5 Hz'e yakın; n = 12 kHz/16,5 Hz ≈ 727 → 729 = 3⁶).

Filtre koşulu: B_Tk ≤ B_k < (5/3)f_ck − (1/3)f_ck = (4/3) f_ck; yani 10 B_k ≤ f_ck ≤ 100 B_k. B/f_c = 0,1 için f_c = 300 kHz'te B = 30 kHz, B_k = 15 kHz alınır.

| k | Δf_k | β_k = Δf_k/f_m | B_Tk | f_ck | B_k |
|---|---|---|---|---|---|
| 0 | 16,461 Hz | ≪ 1 | 8 kHz | 100 kHz | — |
| 1 | 49,383 Hz (3×Δf₀) | 0,0123 ≪ 1 | 8 kHz | 300 kHz | 15 kHz |
| 2 | 148,15 Hz (3²×Δf₀) | 0,037 ≪ 1 | 8 kHz | 900 kHz | 45 (≈ 50) kHz |
| 3 | 444,45 Hz (3³×Δf₀) | 0,11 | ≈ 9 kHz | 2,7 MHz | 135 (≈ 140) kHz |
| 4 | 1333,4 Hz (3⁴×Δf₀) | 0,33 | ≈ 13 kHz | 8,1 MHz | 405 (≈ 400) kHz |
| 5 | 4000,2 Hz (3⁵×Δf₀) | 1,0 | 20 kHz | 3,333 MHz | 166 (≈ 150) kHz |
| 6 | 12 kHz (3⁶×Δf₀) | 3,0 | 40 kHz | 10 MHz | 500 kHz |

Dördüncü çarpıcıdan sonra f_c4 = 8,1 MHz'dir; üçlü bir çarpıcı daha 24,3 MHz verip 13,5 MHz sınırını aşacağından 4. ile 5. çarpıcı arasına frekans aşağı çevirici konur: f_LO = 8,1 MHz − 10 MHz/(3×3) = 8,1 − 1,111 = 6,988 MHz. Karıştırıcıdan sonra BPF çıkışı 1,111 MHz'dir; ardından iki üçleyici (5 ve 6) 3,333 MHz ve 10 MHz verir.

Sistem şeması: m(t) → dar bantlı FM (f_c0 = 100 kHz, β₀ = 16,461/4000 = 0,004 ≪ 1, B_T0 = 2f_m = 8 kHz) → ×3 → ×3 → ×3 → ×3 (8,1 MHz) → karıştırıcı (f_LO = 6,988 MHz) → BPF (1,111 MHz) → ×3 → ×3 → çıkış f_c = 10 MHz, Δf = 12 kHz, β = 3. Çıkış bant genişliği B_T6 = 2f_m(1 + β) = 2×4×(1 + 3) = 32 kHz ≈ 40 kHz.
