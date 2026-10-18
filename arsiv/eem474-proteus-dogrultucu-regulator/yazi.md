---
baslik: EEM474 Güç Elektroniği: Proteus Doğrultucu ve Regülatör Projesi
ozet: Transformatör, köprü doğrultucu ve 7812 içeren Proteus projesinin bileşen ve parametre dökümü.
---

EEM474 klasöründeki 18 Mayıs 2015 tarihli Proteus projesi, transformatör, köprü doğrultucu ve 7812 regülatörü içeriyor. Projenin lisans/müşteri meta verisi temizlendi; devre dosyası ZIP olarak indirilebilir. Proje açılıp çalıştırılmadı.

## Dosyada bulunan devre öğeleri

| Öğe | Kayıtlı değer/özellik |
| --- | --- |
| AC kaynak | 220 V genlik, 1 Hz frekans |
| Transformatör | TRAN-2P2S; LP = 1 H, LS = 1 H, M = 1 |
| Sargı dirençleri | RP = RS = 1 mΩ |
| Doğrultucu | BRIDGE |
| Regülatör | 7812 modeli |
| Kondansatörler | 1000 µF, 10 µF ve 100 nF elemanları |
| Ölçüm | DC voltmetre ve akım probu |

Kaynak dosyada okunabilen parametre örneği:

```
{MODFILE=SINE}
{AMP=220V}
{FREQ=1Hz}
{LP=1H}
{LS=1H}
{M=1.0}
{RP=1m}
{RS=1m}
{MODFILE=7812}
```

*Not: Kaynaktaki frekans 1 Hz olarak korunmuştur; şebeke frekansı olduğu varsayılarak değiştirilmedi. Bu liste dosyadaki parametrelerin dökümüdür; doğrulanmış bir güç kaynağı tasarımı veya deney sonucu değildir.*
