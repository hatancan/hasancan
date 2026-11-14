---
baslik: EEM441 Haberleşme I: EEM442 Haberleşme II 2012 ve 2013 sınavları (soru ve çözümler)
ozet: EEM442 Haberleşme II dersinin 30 Mayıs 2012 finali, 30 Mart 2013 ara sınavı ve 22 Mayıs 2013 finali: 8-PAM, ISI, M-PSK tasarımı, PCM, PDM/PPM ve uyum süzgeci soruları.
---

Başkent Üniversitesi EEM 442 Haberleşme II dersinin 30 Mayıs 2012 finali, 30 Mart 2013 ara sınavı ve 22 Mayıs 2013 finali. Kaynaklar sınav kâğıtlarının ve el yazısı çözümlerin telefon fotoğraflarıdır (EEM441 klasöründe durduğu için burada EEM441 altında yer alır); fotoğraflanmış sayfalardan metne aktarıldı, fotoğraflar yayınlanmadı. Çözümler bir arkadaşın el yazısı notlarından okundu; kişisel bilgi çıkarıldı.

## Final, 30 Mayıs 2012 (süre 110 dak)

**Soru 1.** Dikdörtgen şekilli 8 seviyeli iki kutuplu sinyal, N₀ = 2×10⁻⁶ W/Hz gürültü güç yoğunluklu AWGN ile alıcıya uygulanıyor. i) R_b = 150 kbit/s, ii) iletim seviyeleri arasındaki aralık ±1 V, ±3 V, ±5 V, ±7 V (aralık 2 V), iii) α = 0,4 yükseltilmiş kosinüs süzgecinin çıkışında ISI yok. a) Uyum süzgeci çıkışındaki sinyal noktalarının değerleri, b) örnekleme anındaki sinyal/gürültü oranı, c) sembol hata olasılığı, d) iletim bant genişliği.

*Çözüm.* R_s = R_b/3 = 50 ksembol/s, T_s = 20 µs; A = 1 V için E_g = A²T_s = 20×10⁻⁶, √E_g ≈ 4,47×10⁻³; uyum süzgeci çıkışı ±√E_g, ±3√E_g, ±5√E_g, ±7√E_g. Komşu geçiş olasılığı p = Q(√(2E_g/N₀)) = Q(√20) ≈ 3,87×10⁻⁶. Sembol hata olasılığı P_s = (2(M−1)/M)·p = (7/4)(3,87×10⁻⁶) ≈ 6,77×10⁻⁶; Gray kodlamayla BER = P_s/3 ≈ 2,26×10⁻⁶. Ortalama SNR: E_s/N₀ = (E_g + 9E_g + 25E_g + 49E_g)/(4N₀) = 21E_g/N₀ = 210 (23,22 dB). Bant genişliği B = (1/2T_s)(1 + 0,4) = 0,7R_s = 35 kHz.

**Soru 2.** Tabanbant sistemde g(t) = A Σ a_n p(t − nT), a_n = ±1 eşit olasılıklı. Dürtü yanıtı h(t) olan LTI süzgeç çıkışında v(T₀) = +7, v(T₀−T) = +2, v(T₀+T) = −1, |n| > 1 için v(T₀+nT) = 0; gürültü varyansı σ² = 4, a₀ = 1 varsayılır. a) t = T₀'da ISI'nın hata olasılığını en küçük ve en büyük yapan darbe değerleri, b) bu iki durum ve ortalama hata olasılığı, c) a₀ = −1 için tekrar.

*Çözüm.* Örnekleme anında ψ(T₀)/A = −a₋₁ + 7a₀ + 2a₁ (a₀ = +1):

| a₋₁ | a₁ | ψ(T₀)/A |
|---|---|---|
| +1 | +1 | 8 |
| +1 | −1 | 4 |
| −1 | +1 | 10 |
| −1 | −1 | 6 |

En küçük değer (4) hata olasılığını en büyük, en büyük değer (10) en küçük yapar: P_e,max = Q(4A/σ) = Q(2A), P_e,min = Q(10A/σ) = Q(5A). Ortalama: P_e,ort = ¼[Q(4A) + Q(2A) + Q(5A) + Q(3A)]. a₀ = −1 için simetriden değerler −6, −10, −4, −8 olur; −10 en büyük genlikli (hata en küçük), −4 hata olasılığını en büyük yapar.

**Soru 3.** Gerçek zamanlı (gecikmesiz) bir haberleşme sistemi AWGN kanalında BER'i 10⁻³'ü geçmeyecek, veri hızı 9600 bit/s, iletim bant genişliği (Nyquist) en çok 5000 Hz, alıcıdaki E_b/N₀ = 12 dB olacak biçimde M-PSK (koherent) ve M-FSK (eşevresiz) kullanılarak tasarlanacak. a) Bu koşullarda sembol hızı, sembol enerjisi, bant genişliği verimliliği ve uygun M, b) BER'i sağlayan M.

*Çözüm.* Koherent M-PSK için W = R_s = R_b/log₂M, η = log₂M; eşevresiz M-FSK için W = MR_b/log₂M, η = log₂M/M. M = 2, 4, 8, 16 için PSK verimleri 1, 2, 3, 4; FSK verimleri 0,5, 0,5, 0,375, 0,25 olduğundan her M için PSK daha verimlidir; önce PSK denenir. E_b/N₀ = 12 dB (15,85):

| M | W = R_s | Uygun mu (W ≤ 5000 Hz) | P_b |
|---|---|---|---|
| 2 | 9600 Hz | hayır | — |
| 4 | 4800 Hz | evet | ≈ 8×10⁻⁹ |
| 8 | 3200 Hz | evet | ≈ 6,3×10⁻⁵ |
| 16 | 2400 Hz | evet | ≈ 7×10⁻³ (10⁻³'ü aşar) |

Yalnız 4-PSK ve 8-PSK koşulları sağlar; bant verimi daha yüksek olduğundan 8-PSK seçilir.

**Soru 4.** (Kâğıdın bu kısmı fotoğrafta yoktur.) Çözüm sayfasından: ISI, sistemin süzgeçleme etkisinden doğar; eşdeğer aktarım işlevi H(f) = H_t(f)H_c(f)H_r(f) olup verici ve alıcı karekök yükseltilmiş kosinüs süzgeçleri kullanıldığında H(f) = H_RC(f)H_c(f) ile ilgilenilir. Kanalın düz kaldığı bant 250 kHz olduğunda (baz bant iletim varsayımıyla) (R_s/2)(1 + α) ≤ 250 kHz, α = 0,2 için R_s ≤ 500/1,2 = 416,67 ksembol/s ve M = 8 için R_b = 3R_s ≤ 1250 kbit/s. Daha yüksek hızlarda bant genişliği kanalın düz bölgesinden taşar ve ISI ortaya çıkar.

## Ara sınav, 30 Mart 2013 (süre 110 dak)

1. W = 3000 Hz bant sınırlı analog ses sinyali ikili PCM ve M-PAM ile iletilecek, SNR₀ > 60 dB. a) Verici blok şeması, b) örnek başına en az bit sayısı ve gerçek SNR₀, c) örnekleme sıklığı ve veri hızı, d) iki kutuplu NRZ, darbe süresi 62,5 µs: iletim bant genişliği ve sembol hızı.
2. Düzgün nicemleyiciden sonra 8 bitlik ikili kodlayıcılı PCM sisteminin bit hızı 100×10⁶ bit/s. a) Nyquist hızında örneklenen mesajın en büyük bant genişliği, b) frekansı 1 MHz olan sinüsün tepe değerinde çalışırken çıkış SNR'si.
3. ±12 V aralığında düzgün dağılımlı rastgele sinyal 256 seviyeli düzgün nicemleyiciden geçiriliyor; nicemleyici çıkışındaki sinyal gücünün nicemleme gürültüsüne oranı nedir?
4. s(t) = e^(−αt), 0 ≤ t ≤ T sinyali sıfır ortalamalı, güç izge yoğunluğu N₀/2 olan beyaz Gauss gürültüsüyle karışıyor. a) Uyum süzgecinin dürtü yanıtı ve grafiği, b) çıkıştaki en büyük SNR'yi α, T ve N₀ cinsinden bulun; süzgeç giriş ve çıkış izgelerini çizin, c) s₀(t) = s(t) ve s₁(t) = −s(t) eşit olasılıkla gönderiliyorsa hata olasılığı.

*Çözüm özeti.*

3. Δ = 2m_max/L = 24/256 = 12/128; σ_Q² = Δ²/12.
4. h(t) = s(T − t) = e^(−α(T−t)), 0 ≤ t ≤ T. Çıkış f(t) = s(t)⊗h(t): 0 ≤ t ≤ T için (1/2α)[e^(−α(T−t)) − e^(−α(T+t))]; T ≤ t ≤ 2T için (1/2α)[e^(−α(T−t)) − e^(−α(3T−t))]; t = T'de en büyük değer E_s = (1 − e^(−2αT))/(2α). Çıkış gürültü gücü (N₀/2)E_s, dolayısıyla SNR_çıkış = E_s²/((N₀/2)E_s) = 2E_s/N₀ = (1/(αN₀))(1 − e^(−2αT)). Karar eşiği λ = 0, hata olasılığı P_e = Q(√(2E_s/N₀)).

*Not: 3. soruda el yazısı çözüm sinyal gücünü yoğunluk 1/2 alarak 576 bulmuş ve SNR'yi 12×2¹⁶ (58,95 dB) vermiştir. [−12, 12] üzerinde düzgün dağılımda yoğunluk 1/24'tür; P = 12²/3 = 48 olur ve P/σ_Q² = L² = 2¹⁶ = 65 536 (yaklaşık 48,2 dB) bulunur. 1. ve 2. sorular için çözüm fotoğrafı yoktur.*

## Final, 22 Mayıs 2013 (süre 110 dak)

**Soru 1.** t = kT_s anlarında x(t) = cos(2πt/T_m) sinyali tekdüze örneklenerek (T_s = T_m/3) darbe kiplemeli x_p(t) üretiliyor. a) μ = 0,8, τ₀ = 0,4T_s için PDM (darbe genişliği kiplemesi), b) t_d = 0,57T_s ve t₀ = τ = 0,2T_s için PPM (darbe konumu kiplemesi) dalga biçimlerini çizin.

*Çözüm.* PDM: τ_k = 0,4T_s[1 + 0,8cos(2πk/3)] (k = 0, 1, 2, 3 için darbe genişlikleri 0,72, 0,24, 0,24, 0,72 T_s). PPM: t_k = T_s[k + 0,5 + 0,2cos(2πk/3)], genişlik 0,2T_s.

**Soru 2.** W = 15 kHz bant genişlikli sinyal, gürültü güç yoğunluğu N₀ = 0,01 µW/Hz ve iletim bant genişliği B_T = 40 kHz olan kanaldan M-ary PCM ile iletiliyor. a) SNR₀ ≥ 40 dB için en küçük M ve R, b) PCM'nin iletim bant genişliğinin tamamı kullanılırken, P_e < 10⁻⁵ ve P_tepe/P = 2 için eşik SNR'nin üstünde çalışmak üzere alıcı gücünün en küçük değeri.

*Çözüm.* SNR₀ = 3L²/α = (3/2)L² > 10⁴ ⇒ L ≥ 81,6. Bant genişliği koşulundan örnek başına M-ary sembol sayısı R ≤ B/W = 40/15 ≈ 2,67 ⇒ R = 2. L = M^R > 81,6 ⇒ M = 10, L = 100. Kaynak çözüm eşik SNR'yi 16(100 − 1) ≈ 1600 alır; alıcı gücü P_r = N₀W·SNR_eşik = 10⁻⁸ × 15×10³ × 1600 = 0,24 W = 240 mW.

**Soru 3.** Gönderilme olasılıkları P(S₀) = 0,5, P(S₁) = P(S₂) = 0,25 olan S₀, S₁, S₂ sinyalleri sırasıyla 0, −√E, √E genlikleriyle AWGN kanalında gönderiliyor. a) Sembolleri sinyal uzayında yerleştirin, karar bölgelerini ve eşik değerlerini hesaplayın. b) Optimum alıcının hata olasılığı ve karar bölgeleri.

*Çözüm.* Ara değerler: λ = d/2 + (N₀/2d)ln 2 (d = √E); karar bölgeleri r < −λ, |r| < λ, r > λ; P_e = Q(λ/σ) + ½Q((d − λ)/σ) + ½Q((d + λ)/σ), λ = d/2 için (3/2)Q(d/2σ) + ½Q(3d/2σ).

**Soru 4.** Saniyede 3000 sembol üreten, 128 farklı sembole sahip sayısal iletişim sistemi. a) Çıkışı ikili PAM sinyali olarak iletmek için gerekli bant genişliği, b) B = 3 kHz telefon hattından M-ary sinyal olarak iletmek için gerekli M. (Çözüm fotoğrafı yoktur.)

*Not: 2. sorudaki eşik SNR ifadesi el yazısında kısmen okunaklıdır; sonuç değerleri kaynaktaki gibi aktarılmıştır. 3. ve 4. sorular için yalnız 3. sorunun çözümü fotoğraflarda vardır.*
