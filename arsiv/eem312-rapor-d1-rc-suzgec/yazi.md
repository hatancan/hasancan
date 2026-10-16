---
baslik: EEM312 Sayısal Elektronik: D1 Deney Raporları, RC Alçak Geçiren Süzgeç ve Gecikme Ölçümleri
ozet: EEM312 Sayısal Elektronik donanım laboratuvarının ilk deneyi (D1) için üç öğrenci raporunun karşılaştırması: ölçülen R ve kesim frekansından C hesabı, kazanç ve faz farkının frekansla değişimi, kare dalga girişte tr, tf, tpHL, tpLH ve td ölçümleri.
---

Bu yazı, Başkent Üniversitesi **EEM312 Sayısal Elektronik** dersinin donanım laboratuvarındaki ilk deneyin, **D1: Temel laboratuvar donanımlarının kullanımı** (RC alçak geçiren süzgeç) için yazılmış üç raporu bir arada aktarıyor. İkisi 2011 bahar dönemine, biri 2014'e ait; üçü de arkadaşların hazırladığı raporlar, **kişisel bilgiler çıkarıldı** (A, B, C diye anılıyorlar). Deneyin föyü ve soruları [EEM312 donanım deney föyleri](/arsiv/eem312-donanim-deney-foyleri/) yazısında; burada yalnız raporlardaki ölçümler, hesaplar ve yorumlar var. Kişisel bilgileri kapatılmış raporlar PDF olarak yazının sonundaki ZIP'te.

## Bölüm I: Kesim frekansından C değeri

Her öğrenciye karışık bir direnç–kondansatör çifti verilmiş; R multimetreyle ölçülmüş, devre breadboard'a kurulup girişe 2 V_pp sinüs uygulanmış ve çıkışın 1.4 V_pp'ye (kazanç ≈ 0.7071) düştüğü frekans **kesim frekansı** olarak kaydedilmiş. Kondansatör bu frekanstan hesaplanıyor:

**ω_c = 1/(RC) → C = 1/(2π·R·f_c)**

| Rapor | Ölçülen R | Ölçülen f_c | Hesaplanan C |
|---|---|---|---|
| A (2011) | 55 kΩ | 23 kHz | 0.125 nF |
| B (2011) | 150 kΩ | 4.673 kHz | 227 pF |
| C (2014) | 27.5 kΩ | 10.40 kHz | 556 pF |

Üç C değeri de formülle tutarlı (125.8 pF, 227.1 pF ve 556.5 pF çıkıyor). Raporların ortak yorumu: 1. denklem tek bir RC için yeterli olsa da, frekansla parametreleri değişen başka elemanlar ve parazitik sığalar işin içine girdiğinde bir elemanın iç sığasını ölçmek için yetersiz kalır. B raporu kesim frekansını "çıkışın enerjisinin yarısını kaybettiği frekans" (−3 dB, yarı güç noktası) olarak da açıklıyor.

## Bölüm II: Kazanç ve faz farkının frekansla değişimi

Faz farkı, osiloskopta giriş ve çıkışın tepeleri arasındaki Δt süresinden **ϕ = 360°·f·Δt** ile hesaplanmış.

**A raporu (R = 55 kΩ, f_c = 23 kHz):**

| f | V_out | V_in | Kazanç | Faz farkı |
|---|---|---|---|---|
| 10 kHz | 1.78 V | 2.04 V | 0.872 | 17.63° |
| 50 kHz | 0.960 V | 2.02 V | 0.475 | 50.90° |
| 100 kHz | 0.520 V | 2.00 V | 0.260 | 69.12° |
| 150 kHz | 0.360 V | 2.00 V | 0.180 | 73.07° |
| 200 kHz | 0.280 V | 2.00 V | 0.140 | 80.64° |
| 250 kHz | 0.232 V | 2.00 V | 0.116 | 112.5° |
| 300 kHz | 0.192 V | 2.00 V | 0.096 | 72.43° |
| 400 kHz | 0.160 V | 2.00 V | 0.080 | 81.29° |
| 500 kHz | 0.128 V | 2.00 V | 0.064 | 59.4° |
| 1 MHz | 0.080 V | 2.00 V | 0.040 | 79.2° |

**B raporu (R = 150 kΩ, f_c = 4.673 kHz):**

| f | Kazanç | Faz farkı |
|---|---|---|
| 10 kHz | 0.490 | 59.88° |
| 50 kHz | 0.130 | 76.60° |
| 100 kHz | 0.076 | 78.41° |
| 150 kHz | 0.044 | 79.62° |
| 200 kHz | 0.032 | 87.76° |
| 250 kHz | 0.027 | 94.33° |
| 300 kHz | 0.021 | 103.68° |
| 400 kHz | 0.016 | 117.21° |

**C raporu (R = 27.5 kΩ, f_c = 10.4 kHz):**

| f | Kazanç | Δt | Raporda faz |
|---|---|---|---|
| 1 kHz | 0.980 | 0 µs | 0° |
| 5 kHz | 0.911 | 17 µs | 6.12° |
| 10 kHz | 0.733 | 13 µs | 23.4° |
| 15 kHz | 0.56 | 10 µs | 36° |
| 20 kHz | 0.4615 | 7 µs | 37.8° |
| 25 kHz | 0.39 | 7.2 µs | 51.84° |
| 30 kHz | 0.34 | 6.8 µs | 73.44° |
| 40 kHz | 0.26 | 5.2 µs | 74.88° |
| 50 kHz | 0.21 | 4.8 µs | 86.4° |
| 100 kHz | 0.11 | 2.4 µs | 86.4° |

Üç raporun yorumu aynı yönde: kondansatörün empedansı Z_C = 1/(jωC) frekansla azaldığı için çıkış gerilimi ve dolayısıyla kazanç düşer (alçak geçiren süzgeç); transfer fonksiyonu H = 1/(1 + jωRC) olduğundan faz açısı da −arctan(ωRC) ile frekans arttıkça büyür. C raporu ayrıca devreyi Proteus'ta kurup 1 kHz, 25 kHz ve 100 kHz'te giriş–çıkış dalgalarını karşılaştırmış (25 kHz'te kazanç ≈ 0.37, tepe farkı ≈ 7.8 µs) ve tablo değerleriyle tutarlı bulmuş.

*Not: Birinci dereceden bir RC süzgeçte faz farkı en çok 90°'ye yaklaşabilir. A raporundaki 250 kHz (112.5°) ve B raporundaki 250–400 kHz (94°–117°) değerleri bu sınırı aşıyor; yüksek frekansta Δt'nin osiloskopta göz kararı okunmasından ve prob/breadboard sığalarından kaynaklanan ölçüm hataları olmalı. A raporundaki "250 kHz'ten sonra bant genişliği bitiyor" yorumu da bu yüzden fiziksel değil.*

*Not: C raporunda 5–25 kHz satırlarındaki faz değerleri, ölçülen Δt bir önceki satırın frekansıyla çarpılarak hesaplanmış (ör. 5 kHz için 360·1 kHz·17 µs = 6.12°). Doğru hesapla 5, 10, 15, 20 ve 25 kHz için sırasıyla yaklaşık 30.6°, 46.8°, 54°, 50.4° ve 64.8° çıkıyor; kuramsal arctan(f/f_c) değerleri (25.7°, 43.9°, 55.3°, 62.5°, 67.4°) ile de uyumlu. 30 kHz ve sonrası doğru hesaplanmış.*

## Bölüm III: Kare dalga girişte gecikme ölçümleri

Girişe kare dalga uygulanıp %10–%90 yükselme/düşme süreleri (t_r, t_f), %50 noktaları arasındaki yayılım gecikmeleri (t_pHL, t_pLH) ve ortalamaları t_d = (t_pHL + t_pLH)/2 ölçülmüş.

| Rapor | Darbe biçimi | t_r | t_f | t_pHL | t_pLH | t_d |
|---|---|---|---|---|---|---|
| A | %50, 60 kHz | 1.1 µs | 6.7 µs | 3 µs | 2.4 µs | 2.7 µs |
| A | %30, 60 kHz | 1.0 µs | 6.4 µs | 2.4 µs | 3.4 µs | 2.9 µs |
| B | %50, 60 kHz | 5.4 µs | 6.4 µs | 3.6 µs | 3.6 µs | 4.8 µs |
| B | %30, 60 kHz | 8.0 µs | 8.2 µs | 4.8 µs | 4.8 µs | 4.8 µs |
| C | %50, 6 kHz | 31 µs | 34 µs | 16 µs | 17 µs | 16.5 µs |
| C | %30, 6 kHz | 37 µs | 36 µs | 14 µs | 14 µs | 14 µs |

C raporunda RC ≈ 27.5 kΩ × 556 pF ≈ 15.3 µs; birinci dereceden devre için beklenen t_r ≈ 2.2·RC ≈ 34 µs ve t_p ≈ 0.69·RC ≈ 10.6 µs, ölçülen değerlerle aynı mertebede.

Soru yorumları:

- **t_r ≠ t_f, t_pHL ≠ t_pLH:** İdealde eşit olmaları gerekir. Raporlar farkı kondansatörün dolma ve boşalma yollarının farklı olmasına (dolma R üzerinden, boşalma kaynağın iç direnci üzerinden) ve %10, %50, %90 noktalarının osiloskopta göz kararı okunmasına bağlıyor.
- **Darbe genişliğinin etkisi:** Darbe genişliği küçüldükçe kondansatörün dolma–boşalma süreleri ve buna bağlı olarak ölçülen süreler azalıyor (A ve B); C raporu darbe genişliğiyle doğru orantılı bir etki gözlemliyor.
- **Giriş t_r'si:** Girişteki yükselme ne kadar hızlı olursa olsun çıkıştaki t_r, RC zaman sabiti yüzünden girişten yavaş kalıyor.

*Not: B raporunun tablosunda t_d, t_pHL ve t_pLH'nin ortalaması olarak tanımlandığı hâlde %50 satırında (3.6 + 3.6)/2 = 3.6 µs yerine 4.8 µs yazılmış.*

## Bölüm IV: İkinci dereceden etkiler

A raporu, yüksek frekansta girişe darbe uygulandığında sinyal üretecinden gelen salınımlar ile kabloların ve elemanların endüktif/parazitik etkileri yüzünden ikinci dereceden etkiler (aşma, çınlama) görülebileceğini söylüyor. B raporu ise devrede tek enerji depolayan eleman (kondansatör) olduğu için ikinci dereceden etki görülmediğini, tellerdeki bobin etkisinin de ancak üretecin çıkamadığı çok yüksek frekanslarda ortaya çıkacağını yazıyor.
