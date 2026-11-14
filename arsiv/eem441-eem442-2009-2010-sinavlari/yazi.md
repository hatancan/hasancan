---
baslik: EEM441 Haberleşme I: EEM442 Haberleşme II 2009 ve 2010 sınavları (soru ve çözümler)
ozet: EEM442 Haberleşme II dersinin 25 Mayıs 2009 son sınavı, 3 Ağustos 2010 ara sınavı ve 14 Ağustos 2010 son sınavı: TFM, PCM, uyum süzgeci, zamanlama hatası ve üçlü sinyal soruları.
---

Başkent Üniversitesi EEM 442 Haberleşme II dersinin 25 Mayıs 2009 son sınavı, 3 Ağustos 2010 ara sınavı ve 14 Ağustos 2010 son sınavı. Kaynaklar sınav kâğıtlarının ve el yazısı çözümlerin telefon fotoğraflarıdır (EEM441 klasöründe durduğu için burada EEM441 altında yer alır); fotoğraflanmış sayfalardan metne aktarıldı, fotoğraflar yayınlanmadı. Çözümler bir arkadaşın el yazısı notlarından okundu; kişisel bilgi çıkarıldı.

## Son sınav, 25 Mayıs 2009 (süre 2 saat)

1. Bant genişliği W = 4000 Hz ile sınırlı analog ses sinyali önce ikili PCM, sonra M-PAM modülatörle iletilecek; sinyal/nicemleme gürültü gücü oranı 50 dB'den yüksek olmalı. a) Vericinin blok şeması, b) en düşük bit sayısı ve oranın gerçek değeri, c) gerekli örnekleme sıklığı ve veri hızı, d) darbe süresi 62,5 µs olan iki kutuplu NRZ kullanılırsa iletim bant genişliği ve sembol hızı (bant genişliği f = 0 ile PSD'nin ilk sıfırı arası), e) M değeri, f) izge verimliliği.
2. AWGN kanalında evre uyumlu BPSK ile 100 kbit/s hızda P_b = 10⁻³ isteniyor. Pasbant kanal bant genişliği 50 kHz, α = 1 yükseltilmiş kosinüs süzgeci ve Gray bit atamasıyla: a) M, b) P_b'yi sağlayan E_s/N₀, c) E_b/N₀.
3. Üçlü (ternary) sinyal yapılandırması: s₋₁, s₀, s₁ alıcıda −d, 0, d gerilimlerinde; p(s₀) = 0,5 ve p(s₁) = p(s₋₁) = 0,25. Optimum alıcının hata olasılığı ve karar bölgeleri (AWGN).
4. Verici süzgeci h_t(t), kanal h_c(t) ve alıcı uyum süzgeci h_r(t) bulunan bir sistem; α = 0,2 karekök yükseltilmiş kosinüs süzgeçleri kullanılıyor, kanal aktarım işlevi ayrıca verilmiş. (Sorunun devamı fotoğrafta kesik kalmıştır.)

Sınav kâğıdının formül bölümünde şunlar verilir: P_b = p₁Q((A − λ)/σ) + (1 − p₁)Q((A + λ)/σ); Q(3,09023) = 10⁻³; Q(√20) = 3,87×10⁻⁶; B_T = (R_b/2)(1 + α); SNR₀ = 3·2²ᴺ/α (α = tepe güç/ortalama güç); P(s₁→s₂) = Q(d₁₂/√(2N₀)); P_b = Q(√((E_b/N₀)(1 − ρ))); P_s = 2Q(√(2E_s/N₀)·sin(π/M)); P_E(M) = (2(M−1)/M)Q(√(6E_s,ort/((M²−1)N₀))). Bu sınavın 4. sorusu olarak 16-PAM hat sürücü sorusu (10 dBm ortalama, 30 dBm tepe güç, 12 Msembol/s) ayrı bir sayfada yer alır; aynı soru 2011 finalinde de sorulmuştur.

## Ara sınav, 3 Ağustos 2010 (süre 2 saat)

**Soru 1.** Tamed frequency modulation (TFM) vericisinde ön modülasyon süzgeci, kollarında T, 0 ve −T gecikmeli, 1/4, 1/2, 1/4 katsayılı bir gecikmeli hat ile H₀(f) = πfT/sin(πfT), 0 ≤ |f| ≤ 1/(2T) alçak geçiren süzgeçten oluşur ve bir VCO'yu besler. Ön modülasyon süzgecinin dürtü yanıtını ve toplam aktarım işlevini bulun.

*Çözüm.* h(t) = (1/4)h₀(t − T) + (1/2)h₀(t) + (1/4)h₀(t + T). H(f) = [(1/4)e^(−jωT) + 1/2 + (1/4)e^(jωT)]H₀(f) = (1/2 + (1/2)cos ωT)H₀(f) = cos²(πfT)·H₀(f) = (πfT/sin(πfT))·cos²(πfT), 0 ≤ |f| ≤ 1/(2T); başka yerde 0.

**Soru 2.** W = 4000 Hz bant sınırlı ses sinyali ikili PCM + M-PAM ile iletilecek, SNR₀ > 50 dB. a) Verici blok şeması, b) bit/örnek ve gerçek SNR, c) en düşük örnekleme hızı ve bit hızı, d) iki kutuplu NRZ, darbe süresi 62,5 µs: iletim bant genişliği ve sembol hızı, e) M, f) izge verimliliği.

*Çözüm.* SNR₀ = 3L² > 10⁵ ⇒ L ≥ 182, L = 2ᴿ ⇒ R = 8, L = 256, gerçek SNR₀ = 3·256² ≈ 1,97×10⁵ ≈ 53 dB. f_s ≥ 8 kHz, R_b = 8 × 8 = 64 kbit/s. T_s = 62,5 µs ⇒ R_s = 16 ksembol/s, B = 1/T_s = 16 kHz. k = R_b/R_s = 4 ⇒ M = 16. İzge verimliliği R_b/B = 4 bit/s/Hz. Blok şeması: örnekleyici (f_s ≥ 8 kHz) → nicemleyici (L = 256) → kodlayıcı (R = 8) → M-PAM modülatör.

**Soru 3.** İkili sistemde 1 için s(t) (enerji E), 0 için −s(t)/2 gönderiliyor, 0 ≤ t ≤ T, iki simge eşit olasılıklı, AWGN, iki yanlı güç yoğunluğu N₀/2. a) Uyum süzgeçli alıcı blok şeması; örnekleme anındaki sinyal düzeyinin αE (α = 1 veya −1/2) ve gürültü varyansının EN₀/2 olduğunu gösterin. b) Karar kuralı ve optimum eşik. c) İletim hata olasılığı. d) s(t) ve −s(t)/2 iyi bir seçim mi, hata olasılığı nasıl azaltılır?

*Çözüm.* Alıcı h(t) = s(T − t) süzgeci, T anında örnekleyici ve eşik λ karşılaştırıcısıdır. y(T) = αE + n, σ² = EN₀/2. λ_opt = (E − E/2)/2 = E/4. P_e = Q((λ + E/2)/σ) = Q((3/4)√(2E/N₀)). Ortalama enerji düşük olduğundan hata olasılığı yüksektir; s₀ = −s(t) seçilirse λ = 0 olur ve P_e = Q(√(2E/N₀)) daha küçüktür, fakat ortalama gönderim gücü artar.

**Soru 4.** Dar bantlı (ISI'sız) sistemde T süreli r(t) sembolü L + 1 örnekli (r_k, k = 0…L) alınıyor, uyum süzgecinin dürtü yanıtı da L + 1 örnek (h_k). a) h(t) = r(T − t) için uyum süzgeci çıkışının t = T anında örneklenmiş değerinin Z = Σ h_k r_(L−k) olduğunu gösterin. b) Ayrık zamanlı uyum süzgecinin enine FIR süzgeç olarak gösterimi ve blok şeması. c) Süzgeç örnekleri giriş örnekleriyle eşleştirilirse Z'yi r_k cinsinden bulun.

*Çözüm.* T = LΔ, τ = kΔ alınırsa Z = z(LΔ) = Σ r(kΔ)h(LΔ − kΔ) = Σ r_k h_(L−k) = Σ h_k r_(L−k). FIR süzgeç: z⁻¹ gecikmeli hat, h₀…h_L katsayı çarpıcıları ve toplayıcı. h_k = r*_(L−k) seçilirse Z = Σ|r_k|², yani işaretin enerjisi.

## Son sınav, 14 Ağustos 2010 (süre 2 saat)

1. Bir telemetri sisteminde her biri 2 kHz bant genişlikli sekiz mesaj sinyali ikili tekdüze nicemlenmiş PCM olarak zaman bölmeli çoklanıyor. Örnekleme genliğindeki hata tepe genliğin %1'inden büyük olmamalı; α = 0,2 yükseltilmiş kosinüs darbeleri kullanılırsa gerekli en küçük iletim bant genişliği nedir? Örnekleme hızı Nyquist hızının en az %20 üstünde olmalı.
2. Evre uyumlu BPSK demodülatörün zaman senkronizasyon hatası pT (0 ≤ p ≤ 1): sembol pT kadar geç başlayıp geç bitiyor. a) Bit hata olasılığını p'nin fonksiyonu olarak bulun. b) E_b/N₀ = 9,6 dB ve p = 0,2 için hata olasılığının kaç kat arttığı. c) Zamanlama hatası giderilemezse p = 0 değerine dönmek için E_b/N₀ kaç dB artmalı?
3. Bant genişliği W ile sınırlı x(t) = Σ x_n·sin[2πW(t − n/2W)]/[2πW(t − n/2W)]. a) x₋₁ = −1, x₀ = 2, x₁ = −1 (diğerleri 0) için X(f). b) Bu örnekler ikili sistemle iletilirse örnekleme anlarında alınan düzeyler ve olasılıkları (bitler eşit olasılıklı).
4. Üçlü sinyal konfigürasyonu: s₋₁, s₀, s₁ alıcıda −d, 0, d; p(s₀) = 0,5, p(s₁) = p(s₋₁) = 0,25. Optimum alıcının hata olasılığı ve karar bölgeleri (AWGN). Yararlı formül: yükseltilmiş kosinüs için W = (1/2T)(1 + α) (taban bant), (1/T)(1 + α) (pasbant).

*Çözüm özeti (2, 3, 4).*

2. Bir bit ve ardından gelen bit zıt işaretliyse korelatör çıkışı √E_b(1 − 2p), aynı işaretliyse √E_b olur; buradan P_b = ½Q(√(2E_b/N₀)) + ½Q(√(2E_b/N₀)·(1 − 2p)). E_b/N₀ = 9,6 dB'de p = 0 için P_b = Q(4,27) ≈ 10⁻⁵; p = 0,2 için P_b ≈ 2,6×10⁻³ (yaklaşık 260 kat). P_b = 10⁻⁵ değerini p = 0,2'de yeniden elde etmek için deneme-yanılmayla E_b/N₀ = 23,56 (13,7 dB) bulunur; yani 13,7 − 9,6 = 4,1 dB artış gerekir.
3. x(t) = 2·sinc₀(t) − sinc(t + 1/2W) − sinc(t − 1/2W) ve sinc(2Wt) ↔ (1/2W)Π(f/2W) ilişkisiyle X(f) = (1/2W)[2 − e^(−jπf/W) − e^(jπf/W)] = (1/W)[1 − cos(πf/W)] = (2/W)sin²(πf/2W), |f| ≤ W. Alınan düzeyler B_n = 2I_n − I_(n−1) − I_(n+1), I_n = ±1: B_n = 0 (olasılık 1/4), ±2 (her biri 1/4), ±4 (her biri 1/8).
4. MAP kuralı: λ = d/2 − (σ²/d)ln[p(s₁)/p(s₀)] = d/2 + (N₀/2d)ln 2. Karar bölgeleri: r < −λ ⇒ s₋₁; |r| < λ ⇒ s₀; r > λ ⇒ s₁. P_e = Q(λ/σ) + ½Q((d − λ)/σ) + ½Q((d + λ)/σ); λ = d/2 için P_e = (3/2)Q(d/2σ) + ½Q(3d/2σ).

*Not: 14 Ağustos 2010 sınavının 1. sorusu için fotoğraflarda çözüm bulunmadığından yalnız soru aktarıldı. Aynı üçlü sinyal sorusu 2009 ve 2013 sınavlarında da çıkmıştır.*
