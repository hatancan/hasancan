---
baslik: EEM211 Sayısal Mantık Tasarımı: 24 Sütun Kayan Yazı Projesi (ANTRAK, Ali Yetiş)
ozet: PIC16F84A, PC/AT klavye, EEPROM ve TTL sayıcılarla LED matriste kayan yazı oluşturulması.
---

Ali Yetiş'in (TA5CCF) ANTRAK gazetesinde yayımlanan “24 Sütun Kayan Yazı Projesi”. Metin Kasım 2003, Kadirli imzalı; kaydedilmiş kaynak adresi `www.antrak.org.tr/gazete/122003/ali_yetis.htm`. Makalenin fotoğrafları yayımlanmadı. Görselsiz HTML metni yazının sonunda indirilebilir; aşağıda donanım ve yazılım akışı metne aktarıldı.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Uygulamanın yapısı

Devre bilgisayardan bağımsız çalışır; yazı bir PC/AT klavyeden girilir. PIC16F84A klavye kodlarını alır, EEPROM'a kaydeder ve karakterlerin sütun verilerini göstergeye gönderir. Ekran 24 sütun ve 7 kullanılan satırdan oluşur. Kaydedilebilen metin uzunluğu boşluklar dâhil 63 karakterdir; EEPROM'un H'00' adresi karakter sayısını saklar.

Kaynak, desteklenen karakter kümesini büyük İngilizce harfler, 0–9 rakamları, nokta ve boşluk olarak açıklar ve “35 karakter” der.

*Not: Sayılan küme 26 harf, 10 rakam ve iki işaretle 38 öğe eder. Metindeki 35 sayısı korunarak bu sayım uyuşmazlığı belirtildi; metin uzunluğu sınırı olan 63 ile karıştırılmamalı.*

## LED matrisi ve sürme

Uygulama 5×7 karakter gösterimi için hazırlanmıştır. Kullanılan 8×8 modüllerin yedi satırı değerlendirilir. Ortak katotlu yapıda satırlar lojik 1, seçilen sütun lojik 0 ile sürülür. Ortak anotlu yapıya geçişte sürme seviyelerinin değiştirilmesi gerekir.

Satır bilgisi karakterin görüntüsünü, sütun taraması ise bu bilginin o anda hangi konuma uygulanacağını belirler. Sütunlar hızlı sırayla etkinleştirildiğinde görüntü süreklilik kazanır. Makalede L karakteri için önce 1111111, ardından üç kez 0000001 satır deseni anlatılır; sütun verisi her adımda ötelenir.

## TTL sayıcı ve kod çözücü zinciri

Tarama kısmında üç 74160 BCD sayıcı, üç 7442 onlu kod çözücü ve 7402 NOR kapıları kullanılır. 7442'nin seçilen çıkışı aktiftir ve lojik 0 olur. Sayaç/kod çözücü kademeleri sırayla çalıştırılarak sütunlar seçilir.

Bir kademe sonuna ulaştığında kendi sayması durdurulur ve sonraki kademeye saat darbeleri geçirilir. Q0 ve Q9 çıkışlarının bir bölümü sıfırlama ve kademeler arası geçiş için kullanıldığından her onlu çıkış doğrudan bir ekran sütununa ayrılmaz. Son kademedeki belirli çıkış tüm taramayı başlangıca döndürür.

Kaynakta 25 sütunlu bir animasyon da bulunur; yazar bunun önce elde yapılmış göstergeye ait olduğunu açıklar. Asıl proje 24 sütunludur.

## Klavyeden seri veri alınması

PIC'in RB7 ucu klavye CLOCK hattını, RA4 ucu DATA hattını okur. PORTB değişimi kesmeyi başlatır. İlk düşen kenar başlangıç biti olarak atlanır; ikinci ile dokuzuncu düşen kenar arasında sekiz veri biti alınır. Sonraki parite ve durdurma darbeleri bu uygulamada değerlendirme dışında bırakılır.

Alınan bitler VERI adlı kaydedicide paralel hâle getirilir. Yazar, tuşa basma ve tuşu bırakma olaylarının ayrı bilgi üretmesi nedeniyle aynı karakterin iki kez yazılmaması için ilave bir okuma yaptığını anlatır.

## EEPROM ve görüntüleme akışı

Başlangıçta port yönleri ayarlanır; klavyenin açılışta gönderdiği bilgilerin bitmesi için beklenir. Karakter sayısı EEPROM'dan okunur. Kayıtlı tuş kodu çevrim tablosuyla karakter sütunlarına dönüştürülür; bu sütunlar tarama ile eşzamanlı olarak PORTB'ye aktarılır.

Programda SUTUN1–SUTUN24 çalışma alanları, EEPROM okuma/yazma sayaçları, geçici W/STATUS saklama alanları ve gecikme sayaçları bulunur. Reset vektörü H'0000', kesme vektörü H'0004' adresindedir.

```asm
ORG H'0000'
GOTO MAIN
ORG H'0004'
GOTO KLYOKU
```

## Kaynağın uygulama notları

Yazar, tuşa basıldığında taramanın durmasının LED'lere zarar verebileceğini belirtir. Programlama kablosunun uzunluğu ve ekranlanmasıyla ilgili kendi deneyimini de aktarır. Bunlar 2003 uygulamasının çalışma notlarıdır.

Kaynak sayfa `matrix_asm.zip`, `matrix_hex.zip`, karakter kodları ve Eagle kütüphanesi gibi indirmelere bağlantı veriyor. Bu arşiv klasöründe bağlantı hedefleri bulunmadığı için varmış gibi eklenmedi. Makale içinde görünen assembly metni HTML kopyasında korunuyor; çalıştırılmadı veya derlenmedi.
