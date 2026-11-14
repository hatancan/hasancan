---
baslik: EEM441 Haberleşme I: 2006–2007 quiz, ara sınav ve final soruları
ozet: EEM441 Haberleşme Sistemleri I dersinin 2006–2007 güz dönemi sınavları: SSB/DSB/AM/FM güç ve bant genişliği, zarf algılama, süperheterodin görüntü sıklıkları, FM verici sıklık hatası.
---

Başkent Üniversitesi Elektrik-Elektronik Mühendisliği Bölümü EEM 441 Haberleşme Sistemleri I dersinin 2006–2007 güz dönemi sınavları: 16 Kasım 2006 Quiz 2, 18 Kasım 2006 ara sınavı, 19 Aralık 2006 Quiz 3 ve 12 Ocak 2007 finali (sorular İngilizce). Kaynaklar sınav kâğıtlarının ve el yazısı çözümlerin telefon/kamera fotoğraflarıdır; fotoğraflanmış sayfalardan metne aktarıldı, fotoğraflar yayınlanmadı.

## Quiz 2, 16 Kasım 2006 (süre 45 dak)

**Soru 1.** Normalleştirilmiş m(t) sinyalinin bant genişliği 10 kHz, güç içeriği 0,5 W; taşıyıcı A cos(2πf₀t)'nin güç içeriği 200 W. m(t) taşıyıcıyı a) SSB genlik kiplemesiyle, b) DSB-SC ile, c) kip derinliği 0,6 olan AM ile, d) k_f = 50 000 olan FM ile (B_T = 2(Δf + W)) kiplerse modüleli sinyalin bant genişliği ve güç içeriği ne olur?

*Çözüm.* A_c = 20, P_c = 200 W, P_m = 0,5 W.

| Kip | Bant genişliği | Güç |
|---|---|---|
| SSB | W = 10 kHz | 2P_cP_m = 200 W |
| DSB-SC | 2W = 20 kHz | P_cP_m = 100 W |
| AM (μ = 0,6) | 2W = 20 kHz | P_c(1 + μ²P_m) = 200(1 + 0,36×0,5) = 236 W |
| FM (k_f = 50 000) | 2(50 + 10) = 120 kHz | A²/2 = P_c = 200 W |

**Soru 2.** f(t) = cos(2000πt) ile modüle edilen SSB-L vericisinin çıkışı karmaşık gösterimde s(t) = Re{A[1 + m f(t) + j m f̂(t)]e^(jω_c t)}. a) f̂(t)'yi hesaplayın. b) Zarf algılayıcı çıkışını yazın; m'nin hangi değerlerinde zarf algılama mümkündür? c) 50 Ω üzerinde kipsiz güç 500 W ve kip uygulandığında ortalama güç %50 artıyorsa A ve m. d) c) şıkkındaki durumlar için tepe zarf gücü (PEP).

*Çözüm.* f̂(t) = cos(2000πt − π/2) = sin(2000πt). Zarf r(t) = A√((1 + m cos ω_m t)² + (m sin ω_m t)²) = A√(1 + m²)·√(1 + (2m/(1 + m²))cos ω_m t) ≈ A(1 + m cos ω_m t) (m² ≪ 1). Bozulma kip derinliğiyle artar; %0,1 THD ölçütüyle m < 0,126 gerekir. c) P_c = A²/(2R) = 500 W ⇒ A = 100√5 ≈ 223,6 V; P_t = 500 + m²·500 = 750 W ⇒ m² = 1/2, m = 0,707. d) Kipsiz PEP = 500 W; kipli PEP = 500(1 + m)² ≈ 1457 W.

## Ara sınav 1, 18 Kasım 2006 (süre 100 dak)

1. Çok yollu yayılmada AM'nin zarf algılama ile eşzamanlı (senkron) algılamasının başarımını inceleyin: alıcı girişi x(t) = s(t) + αs(t − τ), α < 1; s(t) AM dalgasıdır. Zarf ve eşzamanlı algılayıcı çıkışlarını yazın; ω_cτ = π/2 ve ω_cτ = π özel durumlarını karşılaştırın.
2. β = 1, f_m = 200 Hz olan ton modüleli FM sinyali merkezi f_c olan ideal, B = 500 Hz'lik BPF'ye uygulanıyor. Çıkışın çizgi izgesini, fazör diyagramını ve zarfını çizin. (J₀(1) = 0,77; J₁(1) = 0,44.)
3. DSB-SC modüleli sinyal koherent algılayıcıyla çözülüyor. a) Algılayıcıdaki yerel taşıyıcı sıklığındaki Δf hatasının etkisi; b) sinüsel mesaj için bu hatanın hata sıklığında vuru oluşturduğunu gösterin ve çözülen sinyalin eskizini çizin.
4. Şekildeki sistemde doğrusal olmayan elemanlar yarım kare yasalı (v₁ > 0, v₂ > 0; çıkışlar aV₁² ve bV₂²). K ve v(t)'nin uygun seçimiyle çıkış süzgeçlemesi olmadan AM üretildiğini gösterin (μ < 1).

## Quiz 3, 19 Aralık 2006 (süre 90 dak)

**Soru 1.** Süperheterodin TV alıcılarında yerel osilatör ikinci harmonik üretirse, bu harmonikler istenmeyen bir kanalın resim içeriğini ara frekans bandına sokabilir. Alıcıdaki video ara frekans taşıyıcısı 45,75 MHz ise alıcı a) 5. kanala, b) 6. kanala ayarlıyken bu tür girişimi yapan kanalı bulun. (VHF TV kanal tablosu verilmiştir: kanal 2: 55,25; 3: 61,25; 4: 67,25; 5: 77,25; 6: 83,25; 7: 175,25; 8: 181,25; 9: 187,25; 10: 193,25; 11: 199,25; 12: 205,25; 13: 211,25 MHz video taşıyıcısı.)

**Soru 2.** NBFM → ×n₁ → karıştırıcı (f₂(1 ± δ₂) salıngaçlı) → ×n₂ → f_c yapısındaki FM vericisinde NBFM taşıyıcısı f₁(1 ± δ₁) sıklıklıdır; osilatörler ortak kaynaktan türetilmemiştir. a) Çıkış taşıyıcı sıklığını n₁, n₂, f₁, f₂, δ₁, δ₂ cinsinden bulun. b) f_c'deki en büyük sıklık hatası. c) n₁ = 64, n₂ = 48, f₁ = 0,2 MHz, f₂ = 10,8 MHz, δ₁ = δ₂ = 10⁻⁸ için en büyük sıklık hatası ve f_c.

*Çözüm (soru verilerinden hesaplandı; fotoğrafta yalnız ara adımlar vardır).* f_c = n₂(n₁f₁ − f₂); hata en çok n₂(n₁f₁δ₁ + f₂δ₂). Sayısal: f_c = 48(12,8 − 10,8) MHz = 96 MHz; hata ≈ 48 × (12,8 + 10,8)×10⁶ × 10⁻⁸ ≈ 11,3 Hz.

**Soru 3.** f_c = 300 MHz için tasarlanmış çift dönüşümlü alıcıda f_IF,1 = 30 MHz, f_IF,2 = 3 MHz; her yerel osilatör iki olası değerin yükseği olacak biçimde ayarlı. RF ve ilk IF katlarındaki yetersiz süzgeçleme üç görüntü sıklığından girişime yol açıyor; bunlar nelerdir? (El yazısı ara adımlar: LO₁ = 330 MHz, LO₂ = 33 MHz.)

**Soru 4.** Evre ayrıştırma yöntemiyle SSB üretiminde taşıyıcı evre kayması gerçekte −90° + δ ise (δ küçük açı hatası) çıkıştaki x_c(t) ve zarf A(t) için yaklaşık ifadeleri bulun.

## Final, 12 Ocak 2007 (süre 120 dak)

1. Dar bant FM sinyali s(t) = A_c cos(2πf_ct) − βA_c sin(2πf_ct)sin(2πf_mt). a) Zarfı ve en büyük/en küçük zarf oranını (0 ≤ β ≤ 0,3 için β'ya göre çizin); b) ortalama gücü kipsiz taşıyıcı gücünün yüzdesi olarak (0 ≤ β ≤ 0,3 için çizin); c) θ_i(t) açısını kuvvet serisine açarak β ≤ 0,3 için θ_i(t) = 2πf_ct + β sin(2πf_mt) − (β³/3)sin³(2πf_mt) olduğunu gösterin; β = 0,3 için üçüncü harmonik gücünün temel bileşene oranı nedir?
2. f_LO = f_c + f_IF olduğunda SSB süperheterodin sistemde x_c(t)cos(2πf_LO t) izgesini çizerek yan bant tersine dönme etkisini gösterin.
3. (Kâğıdın sonraki sayfaları fotoğrafta yoktur.)

*Not: Ara sınav ve final için fotoğraflarda yalnız soru sayfaları ve birkaç el yazısı ara adım bulunmaktadır; tam çözüm aktarılamadı.*
