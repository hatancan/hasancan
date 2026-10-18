---
baslik: EEM474 Güç Elektroniği: Flyback Dönüştürücü
ozet: Flyback dönüştürücünün çalışma aralıkları, sürekli ve süreksiz iletim, mıknatıslanma akımı ve DCM çıkış gerilimi.
---

Başkent Üniversitesi EEM474 Güç Elektroniği dersi için arkadaşların hazırladığı Flyback Converter sunumudur. Tarih belirtilmemiştir. Kişisel bilgiler çıkarıldı; temizlenmiş PDF yazının sonunda indirilebilir.

## Flyback dönüştürücü

Sunum, flyback'i AC/DC veya DC/DC dönüşüm yapabilen buck–boost tipi bir dönüştürücü olarak tanımlar. Sargılar arasında galvanik yalıtım bulunur. Kurulumu kolay ve maliyeti düşüktür; sunumda 5–150 W aralığındaki cep telefonu şarj cihazları, TV ve monitörlerin yüksek gerilim kaynakları, far, lazer ve fotokopi makineleri örnek verilir.

## Anahtarlama durumları

Anahtar kapalıyken primer kaynak gerilimine bağlıdır. Primer akımı artar; sekonder diyodu ters polarmadadır. Kaynak metinde bu durum “Bobin üzerinden geçen akım depolanır” ve “kapasitans dolmaya başlar” diye anlatılmıştır.

*Not: Bobinde depolanan büyüklük enerjidir. Sekonder diyodu kesimdeyken çıkış kondansatörü yükü besler; bu aralıkta sekonderden şarj olmaz.*

Anahtar açıldığında sekonder diyodu iletime geçer ve yük beslenir.

## Sürekli ve süreksiz iletim

Süreksiz iletimde (DCM) sekonder akımı bir sonraki anahtarlama öncesinde sıfıra iner. Sunum yüksek RMS ve tepe akımlarını, elektromanyetik girişimi ve gürültüyü dezavantajlar arasında sayar. Sürekli iletimde akım bu aralıkta sıfırlanmaz; kontrolün daha karmaşık olduğu belirtilir.

## Temel eşitlikler

Primer mıknatıslanma endüktansı L_m, anahtarlama periyodu T ve görev oranı D için:

- Anahtar kapalı: di_L/dt = V_s/L_m; Δi_L = V_s DT/L_m.
- Anahtar açık: v_L = −V_o N₁/N₂; Δi_L = −V_o(N₁/N₂)(1−D)T/L_m.
- Süreksiz iletimde tepe akımı: I_L,max = V_s DT/L_m.
- Giriş ortalama akımı: I_s = V_s D²T/(2L_m).
- İdeal güç dengesi: V_s I_s = V_o²/R.
- DCM çıkışı: V_o = V_s D √[TR/(2L_m)] = V_s D √[R/(2L_m f)].

Bu son bağıntı, slayttaki ideal süreksiz iletim varsayımlarına aittir.
