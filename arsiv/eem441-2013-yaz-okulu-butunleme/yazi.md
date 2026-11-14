---
baslik: EEM441 Haberleşme I: 2013 yaz okulu bütünleme sınavı ve çözümleri
ozet: EEM 441 yaz okulu bütünleme sınavı: FDM kanal koruma bandı, FM frekans çarpıcı, FM sinyal için aşağı çevirici yerleşimi ve AM ton hesapları; el yazısı çözümlerle.
---

Başkent Üniversitesi EEM 441 Haberleşme Sistemleri I dersinin 2013 yaz okulu bütünleme sınavı (süre 90 dakika; kâğıtta tarih “…/8/2013” olarak okunabilmektedir, gün belirsizdir) ve el yazısı çözümleri. Sınav kâğıdı ve çözümler fotoğraflanmış sayfalardan metne aktarıldı; fotoğraflar yayınlanmamıştır. Bu nedenle indirilebilir orijinal dosya yoktur. Kişisel bilgiler (öğrenci numarası, ad) çıkarılmıştır.

## Sorular

1. Bant genişliği f_m olan 12 ses sinyali, bir grup oluşturmak için SSB alt taşıyıcı modülasyonu ve frekans bölmeli çoklama ile çoklanmıştır. Kanallar arası koruma bandı B_g'dir. Frekans yanıtı |H(f)| = exp{−[1,2(f − f₀)/f_m]²} olan BPF'lerin merkez frekansı f₀ her alt taşıyıcı için ayarlanmıştır. Komşu kanal yanıtı |H(f)| ≤ 0,1 koşulunu sağlayacak şekilde B_g'yi hesaplayın. Frekans bölmeli çoklama sisteminin iletim bant genişliğini bulun.
2. Bir FM sinyali frekans çarpıcının girişine uygulanmaktadır. Frekans çarpıcının içindeki BPF'nin merkez frekansı 2f_c'ye ayarlanmıştır. BPF'nin giriş ve çıkışındaki spektrumu çizin. Başarılı bir çalışma için Δf üzerindeki koşulu f_c ve W cinsinden yazın.
3. Bir televizyon vericisinin ses bölümü W = 10 kHz, D = 2,5 ve f_c = 4,5 MHz olan, doğrudan olmayan bir FM sistemidir. Frekans sapması φ_Δ/2πT < 20 Hz ve f_c = 200 kHz için bu sistemin blok şemasını çizin. Frekansı iki katına ve üç katına çıkartan çarpıcılardan oluşan en kısa zinciri kullanarak ve frekansın 100 MHz'i geçmemesini sağlayarak aşağı çeviricinin yerini saptayın.
4. Genlik modüleli sinyalin zarfının genliği 5–15 V arasında değişmektedir. Bilgi sinyalinin frekansı 1 kHz, taşıyıcının frekansı 100 kHz'dir. a) Genlik modüleli sinyalin zaman alanındaki ifadesini değerler belirterek hesaplayın. b) Çift taraflı frekans spektrumunu çizin. c) Taşıyıcının, alt yan bandın ve üst yan bandın 100 Ω'luk bir direnç üzerinde oluşturacağı güç tüketimini hesaplayın. d) Sistemin bant genişliğini hesaplayın. e) Yan bantların gücünü arttırmak için ne yapılması gerektiğini belirtin.

## Çözüm 1

|H(f)| ≤ 0,1 koşulu |f − f₀| ≥ W/2 + B_g için aranır (W = f_m). exp{−[1,2 x]²} ≤ 0,1 ⇒ 1,2 x ≥ √(ln 10) ⇒ x = (W/2 + B_g)/W ≥ (1/1,2)√(ln(1/0,1)) ≈ 1,26.

Buradan B_g ≥ 0,76 W. İletim bant genişliği: B_T = 12 W + 11 B_g ≥ 21 W (11 × 0,76 W ≈ 9 W). Şekilde komşu kanallar arası B_g koruma bantları gösterilmiştir.

## Çözüm 2

β = k_f A_m / f_m = Δf / f_m (k_f = Δf / A_m). n. çarpıcı çıkışında nφ(t) = 2π (nΔf) ∫x(λ)dλ ve B_n ≈ 2(nβ + 1) W'dir. Çıkış spektrumunda f_c, 2f_c, 3f_c çevresinde üç spektrum bölgesi (B₁, B₂, B₃) görülür.

Üstteki bölgelerin çakışmaması için f_c + B₁/2 < 2f_c − B₂/2 ve 2f_c + B₂/2 < 3f_c − B₃/2 koşulları yazılır. Buradan f_c > ½(B₂ + B₃) = [(2β + 1) + (3β + 1)]W = 5Δf + 2W; yani Δf < (f_c − 2W)/5.

## Çözüm 3: Dolaylı (Armstrong) FM

Δf = W × D = 10 × 2,5 = 25 kHz. Dar bantlı FM çıkışında sapma φ_Δ/2πT < 20 Hz olmalı: n = 25000 / 20 = 1250. Bir iki katlayıcı ve altı üçleyici n = 2 × 3⁶ = 1458 verir; φ_Δ/2πT = 25 kHz / 1458 = 17,1 Hz < 20 Hz.

Taşıyıcı: 200 kHz × 1458 = 291,6 MHz > 100 MHz. Bu yüzden son üçleyiciden önce aşağı çevirici kullanılır; orada frekans 291,6/3 = 97,2 MHz < 100 MHz'dir. Aşağı çevirici: f_LO = 97,2 − (4,5/3) = 95,7 MHz; BPF çıkışı 1,5 MHz; sonra ×3 ile f_c = 4,5 MHz ve Δf = 25 kHz elde edilir.

Şema: x(t) → NBFM (f_c = 200 kHz) → çarpıcı zinciri (×2 ve üçleyiciler, toplam n = 1458/3 = 486) → 97,2 MHz → karıştırıcı (f_LO = 95,7 MHz) → BPF (1,5 MHz) → ×3 → f_c = 4,5 MHz, Δf = 25 kHz.

*Not: Metindeki n = 2×3⁶ = 1458 değeri bir iki katlayıcı ve altı üçleyici gerektirir; kâğıttaki şemada ise aşağı çeviriciden önce 2×3×3×3×3 (dört üçleyici) ve sonra tek bir ×3 görünür. Şema ile metin arasında tutarsızlık vardır; hesap metindeki değerlere göre verilmiştir.*

## Çözüm 4: Genlik modülasyonu

a) A_c = (A_max + A_min)/2 = (15 + 5)/2 = 10; μ = (A_max − A_min)/(A_max + A_min) = (15 − 5)/(15 + 5) = 0,5. f_m = 1 kHz (ω_m = 2π·10³ rad/s), f_c = 100 kHz (ω_c = 2π·10⁵ rad/s).

f_AM(t) = 10 [1 + 0,5 cos(2π·10³ t)] cos(2π·100·10³ t) = 10 cos(2π·100·10³ t) + 2,5 cos(2π·99·10³ t) + 2,5 cos(2π·101·10³ t).

b) Çift taraflı spektrum: ±100 kHz'de 5 genlikli çizgiler, ±99 ve ±101 kHz'de 1,25 genlikli çizgiler (her çizgi tepe genliğin yarısıdır).

c) 100 Ω için: P_taşıyıcı = (10/√2)² / 100 = 0,5 W; her yan bant için P = (2,5/√2)² / 100 = 0,03125 W ≈ 31,25 mW.

d) B = 2 f_m = 2 × 1000 = 2000 Hz = 2 kHz.

e) Yan bantların gücünü arttırmak için bindirim (modülasyon) göstergesinin değeri artırılmalıdır (μ ≤ 1 sınırı içinde).

*Not: El yazısı çözümde yan bant genlikleri 1 ve spektrumda 1/2 olarak gösterilmiş ve güç 10 mW olarak yazılmıştır; yukarıdaki sayılar yazının kendi hesabıdır (yan bant genliği μA_c/2 = 2,5 V). Kâğıtta taşıyıcı gücü R = 2×50 = 100 Ω ile 1/2 W bulunmuştur.*
