---
baslik: EEM441 Haberleşme I: EEM442 Haberleşme II 2011 ara sınavı ve finali (soru ve çözümler)
ozet: EEM442 Haberleşme II dersinin 3 Ağustos 2011 ara sınavı ve 1 Haziran 2011 finali: sembol yerleşimi, uyum süzgeci, 16-PAM, ISI ve PCM soruları, çözüm özetleriyle.
---

Başkent Üniversitesi Elektrik-Elektronik Mühendisliği Bölümü EEM 442 Haberleşme II dersinin 2011 yazında yapılan iki sınavı: 3 Ağustos 2011 ara sınavı ve 1 Haziran 2011 finali. Kaynak, sınav kâğıtlarının ve el yazısı çözümlerinin telefonla çekilmiş fotoğraflarıdır (EEM441 klasöründe durduğu için bu arşivde EEM441 altında yer alır); fotoğraflanmış sayfalardan metne aktarıldı, fotoğrafların kendisi yayınlanmadı. Çözümler bir arkadaşın el yazısı notlarından okunmuştur; kişisel bilgi içermez.

## Final, 1 Haziran 2011 (süre 2 saat)

**Soru 1.** Şekilde 8 noktalı, iç ve dış olmak üzere iki çemberden oluşan sembol yerleşimi verilir (r₁/r₂ = 1/2, r₁ = √E₀; E₀ en küçük sembol enerjisi).

- a) Ortalama sembol enerjisini E₀ cinsinden bulun.
- b) İç ve dış çemberdeki sembollerin hata olasılığı üst sınırlarını E_s,ort/N₀ cinsinden yazın.
- c) Öklid uzaklıklarını göz önüne alarak yerleşimi Gray koduyla kodlayın; ortalama BER'i hesaplayın.
- d) Başarımı artıran basit bir değişiklik önerin ve etkisini hesaplayın.

*Çözüm özeti.* r₁ = √E₀, r₂ = 2√E₀; E_s,ort = (r₁² + r₂²)/2 = (5/2)E₀ = 3E_b,ort, yani E₀ = (2/5)E_s,ort = (6/5)E_b,ort. En yakın komşu uzaklıkları d₁ = √(2E₀), d₂² = r₁² + r₂² − √2 r₁r₂ = (5 − 2√2)E₀, d₃ = 2√(2E₀). İç halka için P_e,i ≈ 2Q(d₁/√(2N₀)) + 2Q(d₂/√(2N₀)); dış halka için P_e,o ≈ 2Q(d₂/√(2N₀)) + 2Q(d₃/√(2N₀)). Gray kodlamasında P_b ≲ (1/6)(P_e,i + P_e,o) = (1/3)[Q(d₁/√(2N₀)) + 2Q(d₂/√(2N₀)) + Q(d₃/√(2N₀))]. Öneri: d₁ = d₂ olacak biçimde r₂/r₁ oranını değiştirmek: 2r₁² = r₁² + r₂² − √2 r₁r₂ ⇒ x² − √2x − 1 = 0, x = r₂/r₁.

*Not: El yazısı çözümde x = 1,905, E_s,ort = 2,314E₀ ve kazanç 0,336 dB bulunmuş. x² − √2x − 1 = 0 denkleminin pozitif kökü (√2 + √6)/2 ≈ 1,932'dir; buradan E_s,ort = (1 + x²)E₀/2 ≈ 2,366E₀ ve 10 log(2,5/2,366) ≈ 0,24 dB çıkar.*

**Soru 2.** s₁(t) = A, 0 ≤ t ≤ T; s₂(t) = A (0 ≤ t ≤ 3T/4) ve −A (3T/4 ≤ t ≤ T). AWGN kanalında eşit olasılıkla ikili iletim yapılıyor.

- a) Sinyal enerjileri, b) ilinti katsayısı, c) alıcıdaki uyum süzgeci blok şeması ve örnekleme anındaki çıkışlar, karar ölçütü, d) koherent uyum süzgeciyle bit hata olasılığı.

*Çözüm özeti.* E₁ = E₂ = A²T. ρ = (1/E)∫s₁s₂dt = (A²/E)(3T/4 − T/4) = 1/2. Alıcı iki uyum süzgecinin (1/√E)s₁(T−t) ve (1/√E)s₂(T−t) çıkışlarının farkını alır ve eşik 0 ile karşılaştırır. Örneklenen çıkış r(T) = ±(1 − ρ)√E + n(T), gürültü varyansı N₀(1 − ρ). Hata olasılığı P_e = Q(√((E/N₀)(1 − ρ))) = Q(√(E/(2N₀))).

**Soru 3.** AWGN, N₀ = 10⁻⁶ W/Hz, eşit olasılıklı ikili sinyal s(t) = ±2t/T_b, 0 ≤ t ≤ T_b.

- a) Uyum süzgecinin dürtü yanıtını çizin, b) süzgeç çıkışındaki dalga biçimini hesaplayıp çizin, c) hata olasılığı 10⁻⁴'ten küçük olacak en küçük bit süresini ve bit hızını bulun.

*Çözüm özeti.* h(t) = s(T_b − t) = 2(T_b − t)/T_b; E_b = ∫s²dt = (4/3)T_b. Çıkış 0 ≤ t ≤ T_b için r(t) = 2(t/T_b)²(T_b − t/3), r(T_b) = (4/3)T_b, T_b ≤ t ≤ 2T_b aralığında azalarak 0'a iner. P_b = Q(√(2E_b/N₀)) = Q(√(8T_b/(3N₀))) < 10⁻⁴ için √(8T_b/(3N₀)) ≈ 3,7; T_b ≈ 5,13 µs, R_b ≈ 195 kbit/s.

**Soru 4.** Hat sürücü devresi M = 16 düzeyli 16-PAM kullanır: en büyük ortalama güç 10 dBm, en büyük anlık tepe güç 30 dBm, en büyük sembol hızı 12 Msembol/s.

- a) Eşit aralıklı 16 düzey için en büyük gerilim aralığı, b) bu aralığın tepe mi ortalama güçle mi sınırlandığı, c) ulaşılabilir bit hızı ve ortalama güce bağlılığı, d) N₀ = 10⁻¹² W/Hz için sembol ve bit hata olasılığı.

Soru kâğıdındaki yararlı formüller: ikili iletimde P(s₁→s₂) = Q(d₁₂/√(2N₀)); ilintili sinyalde P_b = Q(√((E_s/N₀)(1 − ρ))); koherent M-PSK için P_s = 2Q(√(2E_s/N₀) sin(π/M)); M-PAM için P_E = (2(M−1)/M) Q(√(6E_s,ort/((M²−1)N₀))); nicemleme gürültüsü varyansı σ_Q² = Δ²/12 = (2m_max/L)²/12, L = 2ᴿ.

*Çözüm özeti.* E_ort = a²(M²−1)/3 = 85a², E_tepe = (15a)² = 225a²; T = 1/12 µs. P_ort = 85a²/T ≤ 10 mW ve P_tepe = 225a²/T ≤ 1 W koşullarından a ≤ 3,13 µV (ortalama) ve a ≤ 19,2 µV (tepe) çıkar; sınırlayıcı olan ortalama güçtür, en büyük gerilim aralığı 2a ≈ 6,3 µV. Bit hızı R_b = 4 × 12 = 48 Mbit/s; sistemin bit hızı güçten bağımsızdır, ortalama güç E_ort·R_b/log₂M ile ilişkilidir. Sembol hata olasılığı kaynak çözümde P_e ≈ 8,9×10⁻⁶, P_b = P_e/4 ≈ 2,2×10⁻⁶ olarak verilmiştir.

*Not: Kaynak çözümdeki sayısal sonuç, E_ort/N₀ ≈ 833 alınarak elde edilmiştir; soru verileriyle (P_ort = 10 mW, T = 1/12 µs, N₀ = 10⁻¹² W/Hz) E_ort/N₀ çok daha büyüktür. Burada kaynaktaki sayılar olduğu gibi aktarılmıştır.*

## Ara sınav, 3 Ağustos 2011 (süre 110 dak)

**Soru 1.** İkili PAM sisteminde y_m = a_m + n_m + i_m; a_m = ±1, n_m sıfır ortalamalı ve σ_n² varyanslı Gauss, ISI terimi i_m = −0,5, 0, 0,5 değerlerini sırasıyla 0,25, 0,5, 0,25 olasılıkla alır. Ortalama hata olasılığını σ_n'nin fonksiyonu olarak bulun.

*Çözüm.* a_m = −1 gönderildiğinde: P_e = ¼P(n > 1/2) + ¼P(n > 3/2) + ½P(n > 1) = ¼Q(1/(2σ_n)) + ¼Q(3/(2σ_n)) + ½Q(1/σ_n).

**Soru 2.** Düzgün nicemleyiciden sonra 7 bitlik ikili kodlayıcılı bir PCM sisteminin bit hızı 50×10⁶ bit/s. a) Nyquist hızında örneklemede en büyük mesaj bant genişliği, b) frekansı 1 MHz olan sinüsün tepe değerinde çalışırken çıkıştaki sinyal/nicemleme gürültüsü oranı.

**Soru 3.** T_s örnekleme aralıklı, Δ basamaklı bir delta modülatöre x(t) = a·t basamak/rampa sinyali uygulanıyor. a) Eğim aşırı yüklenmesi koşulu, b) Δ = 0,75aT_s, aT_s ve 1,25aT_s için modülatör çıkışının çizimi.

**Soru 4.** s(t) sinyali T aralıklı yedi sembolden oluşur (a₀ = a₁ = a₂ = a₄ = 1, a₃ = a₅ = a₆ = −1) ve g(t) üçgen vuruşuyla taşınır (taban genişliği 2T). a) Uyum süzgecinin karakteristik fonksiyonu ve g(t)'nin enerjisi, b) uyum süzgecinin dürtü yanıtı ve t = nT'de örneklenmiş çıkış, c) çıkışın tepe değeri.

*Çözüm özeti.* s(t) = Σ a_k g(t − kT), E_g = T; h_opt(t) = g(T − t)/√T; örneklenmiş çıkış T, 2T, 3T, 5T anlarında +√E_g, 4T, 6T, 7T anlarında −√E_g; tepe değeri √E_g = √T.

*Not: Soru 2 ve 3 için fotoğraflanan sayfalarda çözüm yoktur; yalnız sorular aktarıldı.*
