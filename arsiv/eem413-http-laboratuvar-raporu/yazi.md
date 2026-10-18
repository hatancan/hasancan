---
baslik: EEM413 Bilgisayar Ağları: HTTP Laboratuvar Raporu
ozet: HTTP Laboratuvar Raporu. Ders arşivinden soru, açıklama ve belgeler.
---

Ders arşivindeki öğrenci laboratuvar raporlarıdır; öğrenci adları, numaraları ve kimlik bilgileri çıkarılmıştır. Belge üzerindeki tarih bulunmadığında kaynak dosyanın oluşturulma ya da son değiştirilme tarihi kullanılmıştır. Belgelerin arşiv için hazırlanmış PDF kopyaları yazının sonunda indirilebilir.

## HTTP raporu

Bilgisayar Ağları Lab - 1

Rapor

**1.** http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file1.html için sorulan sorular 1-) Benim browserım HTTP 1.1 kullanıyor. Bunu ilk yazılan URL de göderinin yanında “HTTP/1.1 “ yazmasından anlıyoruz.Serverda da “ request version: HTTP/ 1.1 “ yazmasından serverında HTTP1.1 kullandığını anlıyoruz.

2-) Yukarıdaki print screen de de gösterildiği gibi language kısmında ;

Accept-Language: tr-TR,tr;q=0.8,en-US;q=0.6,en;q=0.4\r\n

Yazmaktadır.Buda bize ingilizce ve türkçe kullanımın olduğunu göstermektedir.

3-) 25 5.008299000 192.168.2.3 128.119.245.12 HTTP 458 GET /wireshark-labs/HTTP- wireshark-file1.html HTTP/1.1

Burada 192.168.2.3 IP adresi benim bilgisayarıma ait iken ; 128.119.245.12 IP adresi Server a aittir.

4-) Status kod olarak “HTTP/1.1 200 OK (text/html)” gönderilmiştir.

5-) Son yenileme tarihi “ Last-Modified: Sat, 02 Nov 2013 18:36:01 GMT\r\n “ burda da belirtildiği gibi 2 Kasım 2013 Saat:18:36 dır.

6-)Content length aşağıdaki print screen de de gösterildiği gibi 128 b dır.

7-)Header lar listeden bakıldığında gözükmesede paket içeriğine girildiğinde hepsinin header ı vardır ve gözükmektedir. Örneğin ; Aşağıdaki print screen de işaretli kısım header ı göstermektedir.

**2.** http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file2.html için sorulan sorular:

8-) Hayır IF – Modified – Since satırını görmedim.

9-) Evet server kesin olarak text cevabı verdi bunu da serverın verdiği cevabın içindeki bu yapıdan anlayabiliriz. Çünkü bu sekmenin içerisinde Line-based text data: text/html kısmında

“Congratulations again! Now you've downloaded the file lab2-2.html. This file's last modification date will not change.

Thus if you download this multiple times on your browser, a complete copy will only be sent once by the server due to the inclusion of the IN-MODIFIED-SINCE field in your browser's HTTP GET request to the server.”

Bu yazı yer almaktadır.

10-) İkinci GET de İF – MODİFİED – SINCE yazısı bulunmaktadır. Aşağıdaki print screen de de gösterilmektedir.Print screen e göre en son 2 kasım 2013 saat : 19:29:01 de modified edilmiştir.

11-) HTTP status ikinci get ten sonra 304 yani => Message: HTTP/1.1 304 Not Modified\r\n Serverdaki bilgide bir değişiklik olmadığı için ilk get te yüklenen yazı cache den çağırılmıştır.

**3.** http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file3.html için olan soruların cevapları :

12-) Print screen de de görüldüğü gibi 1 tane GET mesajı var.

13-) TCP sekmesinden baktığımızda alttaki print screen de olduğu gibi 1452,1452,1452,447 byte kullanıyor.Tcp 4 data paketi taşıyor ve toplam boyut Content – lenght 4500 byte.

14-) Status Code: 200 yani OK konumunda

15-) Hayır , HTTP ve TCP de başka durum bildiren bir yapı yok .

**4.** http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file4.html için olan soruların cevapları :

16-) Aşağıdaki print screen de de görüldüğü gibi 3 tane GET komutu bulunmaktadır. Bunlardan 3 tane geri dönen IP vardır bunlar 128.119.245.12 , 165.193.140.14 ,

**128.** 119.240.90

17-) Bu yapıya bakıldığında iki resim için iki TCP bağlatısı kullanıldığını görüyoruz ve bu da seri indirildiğini gösteriyor.

**5.** http://gaia.cs.umass.edu/wireshark-labs/protected_pages/HTTP-wireshark-file5.html için olan soruların cevapları :

18-) HTTP GET in ilk status kodu aşağıda da belirttiğim gibi 401 yani “Authorization Required “

19-) İkinci GET te ise şifre girildikten sonra ;

Authorization: Basic d2lyZXNoYXJrLXN0dWRlbnRzOm5ldHdvcms=\r\n böyle bir kısmım geliyor.

Lab sorularının alt kısmında da bu şifrelemenin kriptolu gönderilmediğini ve kriptolu örnekler için “HTTP Access Authentication Framework” kısmına bakmamız gerektiği belirtiliyor.

![HTTP raporu: şekil ve hesap tabloları, sayfa 1](belge-01-sekil-01.jpg "HTTP raporu, sayfa 1")

![HTTP raporu: şekil ve hesap tabloları, sayfa 2](belge-01-sekil-02.jpg "HTTP raporu, sayfa 2")

![HTTP raporu: şekil ve hesap tabloları, sayfa 4](belge-01-sekil-04.jpg "HTTP raporu, sayfa 4")

![HTTP raporu: şekil ve hesap tabloları, sayfa 6](belge-01-sekil-06.jpg "HTTP raporu, sayfa 6")

*Not: HTTP 304 yanıtı istenen nesnenin değişmediğini bildirir. 404 ile karıştırılmamalıdır. Rapordaki paket numaraları bu yakalamaya aittir.*

