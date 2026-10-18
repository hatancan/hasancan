---
baslik: EEM474 Güç Elektroniği: Adım motorları ve fırçasız DC motorlar
ozet: Tam ve yarım adım sürme, adım açısı ve darbe frekansı hesapları; Hall algılayıcılı fırçasız motor komütasyonu.
---

EEM474 ders klasöründeki İngilizce sunumların anlatımı ve formülleri metne aktarıldı. Hazırlayanın adı belgelerde açıkça belirtilmiyor. Fotoğraflar ve kitaplardan alınmış görseller aktarılmadığından bu yazıda indirme dosyası bulunmuyor.

## Adım motorunun hareketi

Adım motoru, sargıların belirli sırada enerjilenmesiyle ayrık açısal hareket üretir. Konum, darbe sayısıyla; hız, darbe frekansıyla ilişkilidir. Değişken relüktanslı, sabit mıknatıslı ve hibrit yapıların rotor ve stator düzenleri gösterilir.

Bir turdaki adım sayısı N için adım açısı β = 360°/N'dir. q darbe sonunda dönme açısı θ = qβ; darbe frekansı fp ise hız n = 60fp/N dev/dakikadır.

## Tam adım ve yarım adım

Sargıların tek tek veya ikişerli enerjilendiği tam adım dizileri karşılaştırılır. Yarım adım sürmede tek ve çift sargılı durumlar sırayla uygulanır; mekanik adım küçülür ve bir tur için gereken darbe sayısı iki katına çıkar. Sıralama ters çevrildiğinde dönme yönü değişir.

Tutma momenti, motor dururken enerjili sargıların konumu koruma yeteneğidir. Hız arttıkça sargı akımının yükselmesine ayrılan süre azalır; bu nedenle moment, sürücü ve besleme koşullarına bağlı olarak düşer. Yük ve ivmelenme gereksinimi aşılırsa adım kaçırma görülebilir.

## Sunumdaki hesaplar

| Veri | Sonuç |
| --- | --- |
| β = 1,8° | N = 200 adım/tur |
| N = 200, fp = 6000 darbe/s | 30 tur/s = 1800 dev/dakika |
| β = 1,8°, θ = 46,8° | 26 darbe |
| N = 500, n = 3600 dev/dakika | fp = 30 000 darbe/s |

Bu hesaplar adım kaçırılmadığı ve belirtilen adım modunun korunduğu varsayımına dayanır.

## Fırçasız DC motor

Mekanik fırça ve komütatörün görevini elektronik anahtarlama üstlenir. Rotor konumu Hall algılayıcıları veya optik algılama ile belirlenebilir. Kontrol devresi konuma göre uygun stator sargılarını enerjiler. Motorun dönmesi için komütasyon sırası ile rotor konumu uyumlu olmalıdır.

Sunum Hall algılayıcısının çalışma ilkesini, algılayıcı durumlarından anahtarlama üretimini ve faz akımlarının sırasını gösterir. Lazer yazıcı ve benzeri hareket sistemleri uygulama örnekleridir.

*Not: Kaynağın iki kopyası tek yazıda birleştirildi. Fotoğraflar ve ürün görüntüleri yerine çalışma ilkesi ve sayısal örnekler metne aktarıldı.*
