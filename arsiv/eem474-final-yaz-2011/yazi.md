---
baslik: EEM474 Güç Elektroniği: 17 Ağustos 2011 yaz finali
ozet: Yaz finalinin soru ve cevap nüshaları; harmonik güç, dönüştürücü blokları, köprü sürme, SPWM ve RMS hesabı.
---

17 Ağustos 2011 tarihli EEM474 yaz finalinin soru ve cevap nüshaları. On iki soruluk sınavın iki PDF'i yazının sonundaki ZIP'ten indirilebilir. Cevap nüshasında boş bırakılan sorular da bulunmaktadır.

## Harmoniklerden aktif güç

İlk soruda v(t) = 1,2 cosωt + 0,33 cos3ωt + 0,2 cos5ωt; i(t) = 0,6 cos(ωt + 30°) + 0,1 cos(5ωt + 45°) + 0,1 cos(7ωt + 60°) verilir. Yalnız ortak frekanslar katkı yapar:

P = (1,2 × 0,6/2) cos30° + (0,2 × 0,1/2) cos45° ≈ 0,319 W.

Kaynak sonucu 0,32 W'a yuvarlar. Üçüncü gerilim ve yedinci akım harmoniklerinin karşı bileşeni bulunmadığından ortalama güce katkıları sıfırdır.

## Dönüştürücü zincirleri

Şebekeden genliği ve frekansı ayarlanabilir AC elde etmek için cevaplar: kontrollü doğrultucu + kare dalga evirici; kontrolsüz doğrultucu + buck + kare dalga evirici; kontrolsüz doğrultucu + SPWM evirici. İlk iki yapıda genlik DC kademede, üçüncüde eviricinin ma oranıyla ayarlanır. Çıkış frekansı eviricinin referansıyla belirlenir.

## Anahtar, doğrultucu ve regülatör soruları

İkinci soru anahtar üzerindeki gerilim dalgasını ister. Dördüncü soru seri ve paralel doğrusal regülatörün veriminin hangi koşulda en büyük olduğunu sorar. Beşinci soruda üç farklı AC/DC devrenin direnç yükü gerilimleri α ve π + α tetikleme açılarına göre çizilir. Altıncı soru tristörü iletime geçerken di/dt, kesime geçerken dv/dt zorlanmasına karşı koruyan snubber devresidir.

## Köprü ve buck–boost

Yedinci soruda verilen kapı darbelerinden VA, VB ve VAB dalga biçimleri elde edilir. Onuncu soruda, endüktif yükün akım yönü de dikkate alınarak çıkış dalgasının her aralığında iletimdeki anahtarlar/diyotlar belirlenir. Sekizinci soru buck–boost için kaynakta “ΔL” olarak yazılmıştır.

*Not: Sekizinci sorunun ΔL ifadesi belirsizdir; çoğu dönüştürücü türetmesindeki ΔiL akım dalgalanmasıyla karıştırılmaması için kaynak gösterimi korundu.*

## RMS ve SPWM

Dokuzuncu sorudaki ±Vs darbelerinin her yarım periyottaki genişliği γ ise Vrms = Vs√(γ/π) elde edilir. On birinci soruda sinüzoidal referans ve üçgen taşıyıcıdan kapı darbeleri üreten op-amp düzeni istenir. ma = 0,4, fsin = 75 Hz, mf = 21 ve Vdc = 100 V için cevapta temel gerilim tepesi 40 V, frekansı 75 Hz'dir; taşıyıcı frekansı 1575 Hz olur.

Son soruda AC faz kontrolünün RMS ifadesi ve α = π/2 özel durumu istenir. İdeal direnç yükünde sonuç Vs,rms/√2'dir.

*Not: 40 V, cevapta kullanılan temel bileşenin tepe değeridir; aynı sinüsün RMS değeri 40/√2 V olur. Soru nüshasının üst kısmındaki kırpılma, cevap nüshasıyla tamamlanmıştır.*
