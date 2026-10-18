---
baslik: EEM311 Elektronik II: 2014 Tasarım Ödevinin Ek Proteus Varyantları
ozet: Bant geçiren filtre, notch filtre, dar bant filtre, güç kaynağı ve EKG yükselteci için sekiz ek Proteus DSN dosyası; 2014–2015 ödevindeki farklı bileşen ve test ayarları.
---

Bu yazı, Başkent Üniversitesi **EEM311 Elektronik II** dersinin 2014 güz tasarım ödevi için arkadaşların hazırladığı **sekiz ek Proteus şemasını** içeriyor. Dosyalardaki tarihler 27 Aralık 2014–3 Ocak 2015 arasında. Kişisel bilgi denetimi yapılan dosyalar yazının sonunda ZIP olarak indirilebilir. Önceki [Proteus tasarım setleri](/arsiv/eem311-odev-2014-proteus-tasarimlari/) ile karşılaştırıldığında bu dosyalarda bileşen, bağlantı veya test ayarları farklı; aynı dosyaların kopyaları pakete tekrar alınmadı.

Ödevin soruları ve rapor açıklamaları [2014 filtre ve osilatör tasarım ödevi yazısında](/arsiv/eem311-odev-2014-filtre-osilator/) yer alıyor.

## Bant geçiren filtre: İki ayrı sürüm

`311/soru2.DSN`, 27 Aralık 2014 tarihli erken sürüm. Mevcut tasarım paketindeki `soru2` ile karşılaştırıldığında bazı dirençler 22,5 kΩ yerine **11 kΩ**, bazı kondansatörler 0,2 µF yerine **1 µF**; kaynak ve ölçüm düzeni de farklı.

`odev/proteus cizimleri/soru2.DSN`, 2 Ocak 2015 tarihli rapor sürümü. **1,5 kΩ, 1,8 kΩ ve 0,9 kΩ** dirençler ve **1 µF** kondansatörler yer alıyor. Rapor, alçak geçiren ve yüksek geçiren katların art arda bağlanarak **85–1050 Hz** aralığı hedeflendiğini anlatıyor. Raporun direnç ve kondansatör seçimleri bu sürümle birlikte okunmalı; dosyadaki test ayarları tek başına filtrenin ölçülmüş kesim frekansı değildir.

## Notch filtre

`odev/proteus cizimleri/soru3.DSN`, 3 Ocak 2015 tarihli şema. Önceki paketteki LM741 kullanılan çözümden farklı olarak bu dosyada `OA_3PIN` ideal op-amp modeli var. Kaydedilmiş test kaynağı **5 V, 1 kHz**.

İlgili raporda flüt sesi için **256–2304 Hz** bandının durdurulması amaçlanmış; bant geçiren katın çıkışı girişten çıkarılıyor. Rapordaki seçimler: C₁ = 0,1 µF, C₂ = 0,2 µF, R₁ = R₂ = 0,50 kΩ; diğer katta C₃ = C₄ = 0,5 µF, R₃ = 1,25 kΩ, R₄ = 0,625 kΩ.

## Dar bant filtre

İki dosya var: `e311/soru4.DSN` (28 Aralık 2014) ve `odev/proteus cizimleri/soru4.DSN` (2 Ocak 2015). Bunlar önceki paketteki `50 Hz.DSN` dosyasıyla aynı içerik değil. Sonraki sürümde ölçüm düzeni genişletilmiş ve kaynak ayarları değiştirilmiş.

Rapordaki tasarım **f_c = 104,2 Hz**, C₁ = C₂ = 0,1 µF, R₁ = R₄ = 15,27 kΩ, R₂ = 0,80 kΩ ve R₃ = 290 kΩ değerlerini kullanıyor.

*Not: Raporda hedef bir FM radyo kanalı olarak anlatılsa da verilen hesap 104,2 Hz içindir. 104,2 MHz ile arasında bir milyon kat fark vardır; dosya bir RF kanal seçici olarak doğrulanmış değildir.*

## Güç kaynağı: İki sürüm

`311ek/5 (25)+/olan.DSN`, 30 Aralık 2014 tarihli sürüm. Dosyada 50 Hz kaynağın genliği **22 V** olarak kayıtlı; önceki paketteki aynı adlı şemada **220 V** bulunuyor. Diyot ve bağlantı düzeninde de farklılıklar var.

`odev/proteus cizimleri/soru5.DSN`, 3 Ocak 2015 tarihli sürüm. Kaynak ayarı **220 V, 50 Hz**; transformatör, doğrultucu ve ölçüm elemanları içeriyor. Rapor, transformatörün gerilimi düşürmesini, köprü diyodun doğrultmasını ve çıkış kondansatörüyle süzülmesini anlatıyor; hedef olarak 5 V ve en çok 400 mA yazılmış.

*Not: Ödev sorusunda üst sınır 300 mA iken rapor 400 mA diyor. Direnç ve kondansatörlerle süzme, değişken yük altında tek başına gerilim regülasyonu sağlamaz. Dosyalarda model tanımlarının bulunması, o parçaların hepsinin son devreye bağlı olduğunu tek başına kanıtlamaz.*

## EKG yükselteci

`e311/soru6.DSN`, 28 Aralık 2014 tarihli sürüm. Önceki paketteki 2 Ocak sürümüne göre ölçüm/kayıt bileşenleri ve bağlantı kayıtları farklı. Dosyada **AD624** modeli ve **2 V, 1 kHz** sinüs test ayarı bulunuyor. Bu ayarlar dosyanın saklanmış deneme koşullarıdır; ödevde istenen EKG genlik/frekans özelliklerinin karşılandığına ilişkin ölçüm sonucu olarak alınmamalıdır.

## Paket içeriği

| Klasör | Dosyalar |
| --- | --- |
| 311 | soru2.DSN |
| 311ek/5 (25)+ | olan.DSN |
| odev/proteus cizimleri | soru2.DSN, soru3.DSN, soru4.DSN, soru5.DSN |
| e311 | soru4.DSN, soru6.DSN |

Şemalar Proteus ISIS biçimindedir. Bu arşivleme sırasında devreler çalıştırılmadı; farklar şema kayıtlarının karşılaştırılmasıyla, açıklamalar aynı ödevin raporundan belirlendi.
