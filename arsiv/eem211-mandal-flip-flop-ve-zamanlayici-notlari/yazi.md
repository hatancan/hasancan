---
baslik: EEM211 Sayısal Mantık Tasarımı: D Mandalı, JK Flip-Flop, Durum Tablosu ve Zamanlayıcı Çalışması
ozet: Fotoğraflanmış öğrenci notlarından D mandalı, kenar tetikleme, JK karakteristik denklemi, dört durumlu makine ve kâğıt sayısını izleyen zamanlayıcı sorusu.
---

Bir arkadaşın hazırladığı EEM211 Sayısal Mantık Tasarımı çalışma sayfaları, fotoğraflanmış sayfalardan metne aktarıldı. Üç not fotoğrafı 28 Aralık 2012 tarihlidir; ek zamanlayıcı sorusunda gün bilgisi yoktur. Öğrenci adları çıkarıldı. Fotoğrafların kendisi ve indirme dosyası yayınlanmıyor.

## D mandalı

Notta D mandalının SR mandalındaki belirsizliği önlediği yazıyor. D ve D' sinyalleri, En etkinleştirme girişiyle NAND kapılarından geçirilip çapraz bağlı NAND mandalına uygulanıyor.

| En | D | Sonraki Q |
|---|---|---|
| 0 | X | Değişmez |
| 1 | 0 | 0: reset |
| 1 | 1 | 1: set |

Ayrıca NOR ile kurulan SR, NAND ile kurulan aktif düşük SR ve D mandalı blok simgeleri karşılaştırılıyor.

## İki D mandalıyla kenar tetikleme

Seri bağlı iki D mandalından ilkinin etkinleştirmesine CLK, ikincisine terslenmiş CLK uygulanmış. Altında pozitif ve negatif kenar tetiklemeli D flip-flop simgeleri var. Notun sıraladığı işlemler: çıkışı 1 yapma, 0 yapma ve tümleme.

## JK flip-flop

İki girişli JK flip-flopun tablosu:

| Q | J | K | Q(t+1) |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 |

Karnaugh haritasından **Q(t+1) = Q'J + K'Q**. J = K = 0 iken durum korunur; 01 reset, 10 set, 11 tümleme yapar.

## Dört durumlu makine örneği

Fotoğraftaki tablo ve diyagramda giriş x, çıkış y; durum bitleri A ve B'dir. Devrenin önceki sayfası bu fotoğrafta yoktur.

| Şimdiki AB | Sonraki AB, x=0 | Sonraki AB, x=1 | y, x=0 | y, x=1 |
|---|---|---|---|---|
| 00 | 00 | 01 | 0 | 0 |
| 01 | 00 | 11 | 1 | 0 |
| 10 | 00 | 10 | 1 | 0 |
| 11 | 00 | 10 | 1 | 0 |

Durum diyagramında her ok x/y ile etiketli: 00 durumunun 0/0 öz döngüsü; 00→01 için 1/0; 01→11 için 1/0; 11→10 için 1/0 ve 10'un 1/0 öz döngüsü var. 01, 10 ve 11 durumları 0/1 ile 00'a dönüyor.

## ECG cihazı için zamanlayıcı sorusu

Kâğıttaki soru: Kendiliğinden çalışan bir ECG cihazı on dakikalık veri topluyor ve her on dakika sonunda bir çıktı veriyor. Altı kâğıt bulunduğuna göre ilk veri alımını yönetecek devreyi tasarlayınız; istenilen flip-flop türü kullanılabilir.

Çözüm çiziminde **CLK = 1/60 Hz**, dört D flip-floplu bir sayaç ve üç JK flip-floplu ikinci bir sayaç var. İlk sayaç yanında **1010**, ikinci sayaç yanında **101** ve **111** kodları not edilmiş; geri besleme ve clear bağlantıları çizilmiş. Son çıkış “ampul” olarak gösteriliyor.

*Not: 1/60 Hz saat, dakikada bir darbe üretir; on darbe on dakikaya karşılık gelir. Altı çıktı toplam 60 dakika gerektirir. Fotoğraftaki ikinci sayacın bağlantıları ve farklı son-durum işaretleri, bu davranışı kesin olarak doğrulamaya yetecek açıklıkta değildir; çizim tamamlanmış ve doğrulanmış bir tasarım olarak sunulmadı.*
