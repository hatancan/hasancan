---
baslik: EEM474 Güç Elektroniği: Buck Dönüştürücü Benzetim Dosyaları
ozet: Tepe akım modlu ve senkron buck PSIM şemaları ile kaydedilmiş akım-gerilim verileri.
---

EEM474 proje klasöründeki tepe akım modlu buck ve senkron buck PSIM şemaları, kaydedilmiş sayısal sonuçlarıyla birlikte arşivlendi. Şemaların içindeki kişisel bilgisayar yolları anonimleştirildi. ZIP dosyası yazının sonunda indirilebilir; benzetimler yeniden çalıştırılmadı.

## Tepe akım modu ve eğim telafisi

Şemada “Peak Current Mode Control with Slope Compensation” açıklaması bulunuyor. Bobin, kondansatör, direnç, IGBT, diyot, akım sensörü, karşılaştırıcı, SR flip-flop, kare dalga kaynağı ve sıfırlanabilir integratör blokları var. `Ipeak_ref` ve `Slope compensation` açıklamaları akım eşiğini ve eğim telafisini gösteriyor.

Sonuç dosyasının sütunları:

```
Time  I(L)  Vo  Vslope  Vm
```

4000 örnek, 0,2 µs zaman adımıyla 0,2 µs–0,8 ms aralığını kapsıyor. Kaydedilmiş sonuçlarda bobin akımı 0,01–2,66651 A, çıkış gerilimi yaklaşık 0–11,443 V aralığında. Son örnekte I(L) = 2,13 A, Vo = 11,4201 V, Vslope = 0 ve Vm = 2,1. Telafi rampasının kaydedilmiş en büyük değeri 0,5976.

Bu devrenin açıklaması [Tepe Akım Modu Proje Raporu](/arsiv/eem474-tepe-akim-modu-raporu/) yazısında bulunuyor.

## Senkron buck

İkinci şema bobin, kondansatör, direnç, MOSFET anahtarları, DC kaynak ve gating blokları içeriyor. Sonuç dosyası:

```
Time  I2  V1
```

Yine 4000 örnek ve 0,2 µs adım bulunuyor. I2 yaklaşık −19,81 µA ile 3,11913 A arasında; V1 10,8581–12 V arasında değişiyor. Son örnekte I2 ≈ −19,59 µA ve V1 = 10,8581 V.

*Not: `I2` ve `V1` isimleri kayıttaki prob adlarıdır; şema yeniden açılıp benzetilmediğinden bunlar otomatik olarak çıkış akımı/gerilimi diye yeniden adlandırılmadı. Uzun rakam dizileri bilimsel gösterimli ölçüm verileridir, öğrenci numarası değildir.*
