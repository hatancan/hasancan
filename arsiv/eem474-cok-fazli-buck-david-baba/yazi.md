---
baslik: EEM474 Güç Elektroniği: Çok fazlı buck dönüştürücü (David Baba, Texas Instruments)
ozet: 2012 tarihli makalede faz kaydırmalı buck, giriş ve çıkış dalgalanması, 40 A uygulama örneği ve yerleşim ilkeleri.
---

David Baba'nın Texas Instruments Analog Applications Journal dergisinin 2012 ilk çeyrek sayısında yayımlanan “Benefits of a multiphase buck converter” makalesi. PDF oluşturma tarihi 22 Şubat 2012'dir; makalenin tamamı yazının sonundan indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Faz kaydırmalı çalışma

İki fazlı buck'ta aynı çıkışı besleyen iki endüktörün anahtarlama zamanları kaydırılır. 40 A yükün dengeli paylaşımında her fazın ortalama akımı 20 A olur. Akımın paylaşılması elemanlardaki ısıl yükü dağıtır; akım dalgalanmalarının kısmen birbirini götürmesi giriş ve çıkış kondansatörlerini rahatlatır.

## Dalgalanmanın görev oranına bağımlılığı

N faz ve görev oranı D için k = floor(ND) alınarak makaledeki normalize çıkış dalgalanması:

r(D) = N [D − k/N][(k + 1)/N − D] / [D(1 − D)]

İki fazda D = 0,20 için r = 0,75, yani %25 azalma bulunur. D = 0,25 benzetiminde tek endüktör dalgalanması 2,2 A iken çıkıştaki toplam dalgalanma yaklaşık 1,5 A'dır. İdeal iki fazlı sistemde D = 0,5 noktasında dalgalanmalar birbirini tamamen götürür.

*Not: Sıfır dalgalanma sonucu eşit fazlar ve ideal zamanlama varsayımına aittir; gerçek devrede toleranslar ve parazitler bulunur. Formül uç noktalar D = 0 ve D = 1'de doğrudan bölme yapılarak kullanılmaz.*

## Giriş kondansatörü ve geçici yanıt

Makale giriş kondansatörünün RMS akım gereksinimini de görev oranına göre karşılaştırır. Endüktör başına daha düşük enerji depolanması yük basamağına yanıtı iyileştirebilir. Dalgalanma iptali çıkıştaki ESR kaynaklı gerilim dalgalanmasını azaltır.

## Uygulama örneği

LM3754 değerlendirme kartında 10,8–13,2 V giriş, 1,2 V çıkış, 40 A maksimum yük ve 300 kHz anahtarlama kullanılır. Faz başına 0,5 µH endüktör ve toplam 2000 µF çıkış kapasitesi listelenir. Makaledeki ölçümlerde 10 A yük basamağına yaklaşık 20 µs yanıt ve yaklaşık 27 mV alt/üst aşım gösterilir. Verim ve güç kaybı grafikleri 0,9 V ile 1,2 V çıkışları karşılaştırır.

## Yerleşim

Yüksek akımlı yollar ve kapı sürme dönüş yolları kısa tutulur. Sinyal toprağı ile güç toprağı uygun noktada birleştirilir. Küçük sinyal elemanları kontrolcüye yakın konur; anahtarlama düğümünün bakır alanı ve hassas işaretlerle kuplajı sınırlanır. Giriş kondansatörünün MOSFET çiftine yakınlığı özellikle vurgulanır.

*Not: Ürün adları ve ölçüm değerleri 2012 tarihli makaledeki uygulamaya aittir; güncel ürün tavsiyesi veya her çok fazlı devre için garanti edilmiş performans değildir.*
