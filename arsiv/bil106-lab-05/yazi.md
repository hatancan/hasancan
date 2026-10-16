---
baslik: BİL106 Laboratuvar Çalışması #5: Karakter İşlemleri ve Dizgi Uygulamaları
ozet: BİL106 Programlamaya Giriş dersinin 5. laboratuvar föyü (2014): özel sayı sisteminden onluk sisteme çevirme, hangigun fonksiyonu, kelime zinciri ve farkiSay, dizgi olarak girilen iki zaman arasındaki fark. Dört C programlama sorusu ve örnek çalışmalar.
---

Bu yazı, Başkent Üniversitesi **BİL106 Programlamaya Giriş** dersinin 5. laboratuvar çalışmasıdır (Mart 2014). Konu **karakter işlemleri ve dizgi (string) uygulamaları**: her biri 25 puanlık dört C programlama sorusu. Sorular föydeki hâliyle aktarıldı; örnek çalışmalar, programın ekranda üretmesi beklenen çıktıyı gösteriyor. Föyün orijinal PDF'i yazının sonunda indirilebilir.

## Soru 1: Özel sayı sisteminden onluk sisteme (25 puan)

Özel bir sayı sisteminde **1** yerine **I**, **10** yerine **U**, **100** yerine de **Z** simgeleri kullanılmaktadır. Bu sistemde bir tamsayı, kullandığımız onluk sistemde kaç tane birlik, onluk, yüzlük varsa I, U veya Z simgelerinden o kadarı yan yana dizilerek yazılır. Bu özel sayı sisteminde girilen en fazla 50 basamaklı sayıyı onluk sayı sistemine çevirip ekrana yazan programı yazınız.

Örnek çalışma 1:

```
Özel sayı sistemindeki sayıyı giriniz: ZZUIIII
-------------------------
Girilen sayının onluk sistemdeki karşılığı : 214
```

Örnek çalışma 2:

```
Özel sayı sistemindeki sayıyı giriniz: ZZZI
-------------------------
Girilen sayının onluk sistemdeki karşılığı : 301
```

## Soru 2: Haftanın kaçıncı günü? (25 puan)

Kendisine gönderilen gün ismine göre haftanın kaçıncı günü olduğunu geri döndüren `hangigun` adındaki fonksiyonu, sırası bulunacak gün adının klavyeden girildiği bir `main` fonksiyonu ile beraber yazınız. Klavyeden girme ve bulunan sonucun ekrana yazdırılması `main` fonksiyonunda gerçekleştirilmeli ve global değişken kullanılmamalıdır.

Örnek çalışma:

```
Günün adı : Pazar
--------------------------------
Pazar günü haftanın 1. günüdür
```

## Soru 3: Kelime zinciri (25 puan)

Klavyeden girilen kelimeler zincir oluşturduğu sürece yeni kelime girilmesini isteyen programı yazınız. Kelime zincirinin olabilmesi için her kelimenin, bir önceki kelimeden (yeni harf eklenmeden) yalnızca bir harf değiştirilerek üretilmiş olması gerekmektedir. Yeni girilen kelimenin önceki kelimeden aynı sıradaki farklı harf sayısı `farkiSay` adında bir alt fonksiyon ile bulunmalıdır. Bu fonksiyon kelimeleri alıp farklı harf sayısını geri döndürür. Sonraki girilen tüm kelimeler, ilk girilen ile aynı uzunluktadır. Kelimeler en fazla 50 karakter olabilir.

Örnek çalışma:

```
İlk kelimeyi giriniz      : DEMİR
Sonraki kelimeyi giriniz  : KEMİR
 (1 harf farklı zincir bozulmadı)
Sonraki kelimeyi giriniz  : KESİR
 (1 harf farklı zincir bozulmadı)
Sonraki kelimeyi giriniz  : MESİR
 (1 harf farklı zincir bozulmadı)
Sonraki kelimeyi giriniz  : ZEHİR
 (2 harf farklı zincir bozuldu)
Program sona erdi
```

## Soru 4: İki zaman arasındaki fark (25 puan)

Klavyeden girilen iki adet zaman değerine göre ikisinin arasındaki farkı saniye olarak hesaplayıp ekrana yazan C programını yazınız. Zamanlar ayrı birer **dizgi** olarak okunmalıdır. Zaman her zaman `SS:DD:SS` (saat:dakika:saniye) biçiminde verilecektir.

Örnek çalışma (zamanlar dizgi, yani string olarak giriliyor):

```
Birinci zamanı giriniz: 14:02:55
İkinci zamanı giriniz: 15:03:00
-------------------------
Aradaki fark : 3 saniyedir
```

*Not: Föydeki örnekte fark 3 saniye olarak yazılmış; ancak 14:02:55 ile 15:03:00 arasındaki fark aslında 3605 saniyedir (1 saat 5 saniye). Örnek, föydeki hâliyle bırakıldı.*
