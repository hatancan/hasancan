---
baslik: EEM211 Sayısal Mantık Tasarımı: Sayıcı, Gösterge ve Lojik Proje Kaynakları (Elektrotekno PCB Eki)
ozet: Trafik, CMOS lojik ve yedi parçalı gösterge çalışmaları için Proteus ve ARES kaynak dosyaları.
---

EEM211 klasöründeki arkadaşların devre çalışmalarından dört Proteus devresi ve iki ARES PCB kaynak dosyası. Kişisel dosya adları nötrleştirildi. Trafik dosyasının tarihi 26 Aralık 2007; diğer iki DSN 2015 arşiv kaydında, son PDS projesi Ocak 2016'da bulunuyor. Son projenin iç değiştirilme kaydı 11 Ocak 2016. ZIP yazının sonunda indirilebilir.

## Trafik devresi

`trafik.DSN` dosyasında 4013 D flip-flop, 4514 kod çözücü, 74XX191 sayıcı, AND/OR kapıları ve LED modelleri bulunur. Sayıcı, kod çözme ve ışık çıkışlarını birleştiren bir projedir. Buradaki bilgi dosyada okunabilen model kayıtlarından çıkarıldı; ışık süreleri veya çalışma sırası benzetilmedi.

## İki CMOS lojik proje sürümü

`lojik-proje-1.DSN` ve `lojik-proje-2.DSN` kaynakta farklı proje klasörlerinde bulunur. 4013 flip-floplar, NAND kapıları, LED'ler, dirençler ve kondansatörler içerirler. İlk sürümde ayarlı direnç modeline de başvuru vardır. Dosyalar bire bir aynı olmadığından ikisi de korunmuştur.

Bu iki kaynağın dosya adlarında kişisel bilgiler vardı; indirme dosyası ve ZIP yollarında bunlar kullanılmadı. İçlerindeki metin kayıtları ayrıca kontrol edildi.

## Sayısal mantık projesi

`sayisal-mantik.pdsprj` içinde 74XX74 D flip-flop, AND, OR, evirici, 4511 kod çözücü ve ortak katotlu yedi parçalı gösterge model başvuruları yer alır. Flip-flop çıkışlarını gösterge sürücüsüne bağlayan sayısal tasarım çalışmalarına ait bir kaynak kaydıdır.

## İnceleme sınırı

Bu yayın düzenlenebilir kaynakları korur. Devreler çalıştırılmadı; içerideki model adlarından bütün bağlantıların doğruluğu veya devrenin belirli bir sayma dizisini ürettiği sonucu çıkarılmadı. Üretici kütüphaneleri, veri sayfaları ve program kurulumları pakete eklenmedi. PDS projesinin XML müşteri kimliği alanı sıfırlandı.


## ARES baskı devre ekleri

`lojik-proje-pcb.LYT`, proje klasöründeki baskı devre tasarımıdır. Kartın üzerinde metin olarak saklanan kişisel adlar da çıkarılmıştır.

`trafik-isigi-pcb.LYT`, kaynak klasöründe elektrotekno.com şemalarıyla birlikte saklanan ARES çizimidir. Bu ekin kaynak bağlamı [trafik ışığı şemaları yazısında](/arsiv/eem211-trafik-isigi-devreleri/) açıklanır. Yerleşim dosyası bu ortamda açılmadığından hangi şema sürümüyle bire bir eşleştiği doğrulanmadı.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*
