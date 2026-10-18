---
baslik: EEM214 Elektronik I: Zener ve Diyot Küçük Sinyal Ön Çalışma Ekleri
ozet: Zener regülasyonu, diyodun DC ve AC eşdeğeri, küçük sinyal direnci ve 0,7 gerilim aktarım oranı için direnç tasarımının el yazısı çözümleri.
---

EEM214 laboratuvarı için hazırlanmış Zener ve diyot küçük sinyal ön çalışmaları, fotoğraflanmış ve taranmış sayfalardan metne aktarıldı. Öğrenci adları ve numaraları çıkarıldı; kaynak görüntüler ve indirme dosyası paylaşılmıyor. Küçük sinyal çalışmasının arşivdeki tarihi 23 Mart 2014'tür.

## Zener ön çalışması

İki fotoğraftaki aynı hesap birlikte aktarılmıştır. Kaynak açıklama, Zener diyodun ters yönde belirli bir eşik sonrasında akım geçirmesi ile sıradan diyodun ters yönde kullanılmamasını karşılaştırır; sıradan diyodun ters iletimde yanacağını söyler.

*Not: Sıradan diyotta da ters kırılma oluşabilir. Kalıcı hasar akım ve güç sınırlarına bağlıdır; “her ters akımda yanar” ifadesi genel bir fizik kuralı değildir.*

Devrede V_s kaynağı R_s üzerinden çıkışa bağlıdır; Zener ile yük R_L çıkışa paraleldir. Kaynaktaki hesaplar:

- r_z = ΔV_z/ΔI_z = 20 Ω.
- r_z I_zk = 20 Ω × 0,2 mA = 4 mV; kaynak bunu V_z olarak adlandırır.
- 10 V − 0,5 kΩ × 5 mA = 7,5 V karşılaştırmasıyla Zenerin iletimde olduğu ve V_out = 6,8 V yazılır.
- “V_s + 1” için 8,5 V ve V_out = 6,8 V; “V_s − 1” için 6,5 V ve Zenerin iletimde olmadığı belirtilir.
- R_L = 2 kΩ, V_in = 6,5 V ve Zener kesimdeyken V_out = [R_L/(R_s + R_L)]V_in = (2/2,5) × 6,5 V.
- R_L = 0,5 kΩ için V_out = [0,5/(0,5 + 0,5)]V_in; V_in = 10 V ile 5 V bulunur.

*Not: 4 mV, verilen dinamik dirençle hesaplanan gerilim değişimidir; Zenerin nominal 6,8 V gerilimi değildir. 2 kΩ yüklü ve 6,5 V girişli durumda bölücü sonucu 5,2 V'tur. Kaynaktaki “V_s ± 1” satırları 7,5 V merkezli değerlerdir; 10 V kaynağın doğrudan ±1 V değişimiyle karıştırılmamalıdır. Yüklü regülasyon sınırında Zener akımı da kontrol edilmelidir.*

## Diyodun DC çalışma noktası

D1N4148 diyodu +5 V kaynağına 1 kΩ üzerinden, alt ucu R üzerinden toprağa bağlıdır. Giriş üst uca ve çıkış alt uçtaki 1 kΩ yüke 10 µF kondansatörlerle kuplajlanmıştır. Giriş v_i(t) = V_m cos(ωt) olarak yazılır.

Kaynak modelde eşik V_γ = 0,6 V, seri direnç r = 20 Ω ve idealite katsayısı n = 2'dir. DC'de kondansatörler açık devredir:

I_DQ = (5 − 0,6)/(1 kΩ + R + 20 Ω).

| R | Toplam DC direnç | I_DQ |
| --- | --- | --- |
| 3,9 kΩ | 4920 Ω | Yaklaşık 894 µA |
| 56 kΩ | 57020 Ω | Yaklaşık 77,1 µA |

Kaynak eğride çalışma noktası ile doğrusallaştırma gösterilir. AC için besleme toprağa alınır, kuplaj kondansatörleri kısa devre sayılır ve diyot r_d ile değiştirilir.

## Küçük sinyal direnci ve gerilim aktarımı

r_d = nV_T/I_DQ, V_T = 25 mV:

- 894 µA için r_d ≈ 56 Ω.
- 77,1 µA için r_d ≈ 650 Ω.

Çıkış yükü R_eq = R || 1 kΩ ve A_V = V_o/V_in = R_eq/(R_eq + r_d).

| R | Kaynaktaki paralel eşdeğer | r_d | Kaynaktaki A_V |
| --- | --- | --- | --- |
| 3,9 kΩ | Yaklaşık 800 Ω | 56 Ω | 0,92 |
| 56 kΩ | Yaklaşık 980 Ω | 650 Ω | 0,60 |

*Not: 800/(800 + 56) ≈ 0,935 olduğundan ilk satırdaki 0,92 sonucu aritmetik olarak uyuşmaz. İkinci oran yaklaşık 0,601'dir. Kaynak, DC'de kullandığı 20 Ω seri direnci AC'de r_d'ye ayrıca eklememiştir; sonuçlar bu kabulle aktarılmıştır.*

Kaynak küçük sinyal sınırını v_d ≪ nV_T = 50 mV olarak yazar.

*Not: Bu eşitsizlik diyot üzerindeki AC gerilim içindir; giriş kaynağı genliğiyle aynı olmak zorunda değildir.*

## 0,7 aktarım oranı için direnç tasarımı

Tasarım koşulları 0,67 < A_V < 0,73 ve I_DQ < 3 mA'dir. Çözüm, bu aşamada 20 Ω'u ihmal ederek I_DQ ≈ 4,4 V/(1 kΩ + R) kullanır. Akım koşulundan R > 466 Ω bulunur.

Dirençler kΩ ile ifade edildiğinde r_d ≈ 0,0113(1 + R), R_eq = R/(1 + R) ve hedef:

0,7 = R_eq/(R_eq + r_d).

Kaynak cebirinde 7r_d = 3R_eq, ardından yaklaşık 8R² − 284R + 8 = 0 yazılır. Kökler yaklaşık 35,4 kΩ ve 28 Ω'dur; akım sınırı nedeniyle küçük kök elenir. İlk deneme satırında 27 kΩ da yazılıdır, nihai çözümde kullanılmaz.

35,4 kΩ için kaynak denetimi:

- R_eq ≈ 0,972 kΩ.
- r_d ≈ 0,411 kΩ.
- A_V ≈ 0,972/(0,972 + 0,411) = 0,702.

Standart 33 kΩ ile R_eq ≈ 0,970 kΩ, r_d ≈ 0,384 kΩ ve A_V ≈ 0,716 yazılır; 33 kΩ'un kullanılabileceği sonucuna varılır.

*Not: Yuvarlatılmamış nV_T = 50 mV ve 4,4 V ile büyük kök yaklaşık 35,69 kΩ'dur; 35,4 kΩ ara katsayıların yuvarlatılmasından doğar. 33 kΩ için aynı model yaklaşık 0,715 verir ve istenen aralıktadır. I_DQ ≈ 0,129 mA ile 3 mA sınırı da sağlanır.*
