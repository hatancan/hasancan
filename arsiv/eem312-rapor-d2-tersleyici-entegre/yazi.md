---
baslik: EEM312 Sayısal Elektronik: D2 Deney Raporları, Entegre Tersleyici (SN7404 ve CD4049) Ölçümleri
ozet: EEM312 Sayısal Elektronik donanım laboratuvarı D2 deneyi için iki öğrencinin raporu: TTL SN7404 ve CMOS CD4049 tersleyicilerde VOL, VOH, VIL, VIH, gürültü payları ile tr, tf, tpHL, tpLH ölçümleri ve üretici verileriyle karşılaştırma.
---

Bu yazı, Başkent Üniversitesi **EEM312 Sayısal Elektronik** donanım laboratuvarının **D2: Entegre devre tersleyici ölçümleri** deneyi için yazılmış iki raporu karşılaştırıyor: 2011 bahar dönemine ait, **TTL SN7404** ile yapılmış bir rapor (A) ve 2014'te **CMOS CD4049** ile yapılmış bir ön çalışma ve rapor (B). İkisi de arkadaşların raporları; **kişisel bilgiler çıkarıldı**. Föyün kendisi [EEM312 donanım deney föyleri](/arsiv/eem312-donanim-deney-foyleri/) yazısında. Raporların kişisel bilgileri kapatılmış PDF'leri yazının sonundaki ZIP'te.

## Ön çalışma: entegrelerin özellikleri (B)

B'nin ön çalışmasına göre ekte verilen CD4049/CD4050 entegreleri **CMOS** ailesindendir ve şu özellikleri öne çıkar:

- Tek bir besleme (V_DD) ile mantık seviyesi çevirme yapabilirler.
- Seviye çevirici olarak kullanıldıklarında giriş yüksek seviyesi (V_IH) V_DD'ye kadar çıkabilir.
- Doğrudan iki DTL/TTL yükü sürebilirler.
- Hex buffer (CMOS → DTL/TTL ya da CMOS akım sürücüsü) olarak tasarlanmışlardır.

Önerilen çalışma koşullarına göre CD4049/CD4050 3–15 V, SN5404/SN7404 ise nominal 5 V beslemeyle çalışır; ikisi de 5 V'ta kullanılabilir. 5 V'ta veri sayfasındaki geçiş süreleri CD4049/CD4050 için t_r = t_f = 20 ns, SN7404 için t_r, t_f < 7 ns. Föydeki devrede CD4049/CD4050, CMOS tabanlı bir entegrenin çıkışını TTL ya da başka bir CMOS entegreye bağlamak için arada hex buffer olarak kullanılıyor.

A raporu ise SN7404'ü tanıtıyor: 14 bacaklı, altı tersleyici içeren bir **hex inverter** (1 bacak toprak, 1 bacak V_CC), çalışma sıcaklığı 0–70 °C; önerilen koşullar V_CC = 4.75–5.25 V, V_IH ≥ 2 V, V_IL ≤ 0.8 V.

## Statik ölçümler (VTC)

Tersleyici kurulup girişe 0–5 V üçgen dalga (A: 1 kHz, çıkışta 10 pF; B: çıkışta 1 pF) uygulanmış, osiloskopta X-Y modunda V_out–V_in eğrisi izlenmiş.

| Büyüklük | A: SN7404 ölçülen | A: SN7404 veri sayfası | B: CD4049 ölçülen |
|---|---|---|---|
| V_OL | 0 V | 0.2 V (tipik) | 20 mV |
| V_OH | 5.2 V | 3.4 V (tipik) | 5.4 V |
| V_IL | 0 V | en çok 0.8 V | 2.8 V |
| V_IH | 5 V | en az 2 V | 2.9 V |
| NM_H = V_OH − V_IH | 0.2 V | 1.4 V | 2.4 V |
| NM_L = V_IL − V_OL | 0 V | 0.6 V | 2.58 V |

İki rapor da farkları ideal koşulların (gürültüsüz 5 V besleme, 25 °C oda sıcaklığı) sağlanamamasına, elemanların iç dirençlerine, bağlantı kablolarına ve deneyde kullanılan elemanların üreticinin ölçtüğü örneklerden daha kötü olmasına bağlıyor.

*Not: A raporunda öğrenci X-Y modunda bir eğri gözleyemediğini yazıyor; V_IL = 0 V ve V_IH = 5 V değerleri bu yüzden gerçek bir VTC okuması değil. Raporda NM_L "V_OL − V_IL" diye yazılmış, doğrusu V_IL − V_OL.*

*Not: B raporunda verilen değerlerle NM_H = 5.4 − 2.9 = 2.5 V ve NM_L = 2.8 − 0.02 = 2.78 V çıkıyor (raporda 2.4 V ve 2.58 V). 5 V beslemede ölçülen V_OH = 5.4 V da beslemenin 5 V'tan biraz yüksek ayarlandığını gösteriyor.*

## Dinamik ölçümler (100 kHz kare dalga)

Girişe 0–5 V, 100 kHz kare dalga verilip çıkışta geçiş ve gecikme süreleri ölçülmüş.

| Büyüklük | A: SN7404 ölçülen | A: veri sayfası (C_L = 15 pF) | B: CD4049 ölçülen | B: üretici verisi |
|---|---|---|---|---|
| t_r | 36 ns | 7 ns | 116 ns | 60 ns |
| t_f | 28 ns | 7 ns | 64 ns | 30 ns |
| t_pHL | 17 ns | en çok 15 ns | 69 ns | 65 ns |
| t_pLH | 18 ns | en çok 22 ns | 43 ns | 85 ns |
| t_d | 17.5 ns | – | 58 ns | – |

TTL tersleyici, CMOS CD4049'dan belirgin şekilde hızlı. Raporlar ölçülen sürelerin üretici değerlerinden büyük çıkmasını yine deney düzeneğinin (yük kondansatörü, prob ve kablo sığaları, iç dirençler) ideal olmamasıyla açıklıyor.

*Not: B'nin değerleriyle t_d = (69 + 43)/2 = 56 ns ediyor; raporda 58 ns yazılmış.*
