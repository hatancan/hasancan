---
baslik: BİL106 Laboratuvar Çalışması #6: Yapılar (struct) ve Dizgiler
ozet: BİL106 Programlamaya Giriş dersinin 6. laboratuvar föyü: ogrenci yapısıyla ortalamaya göre sıralı liste, zaman yapısı ve zamantopla fonksiyonu, ondalık sayıyı işaret/tam/ondalık kısımlarına ayıran floatToplam. Üç C programlama sorusu ve örnek çalışmalar.
---

Bu yazı, Başkent Üniversitesi **BİL106 Programlamaya Giriş** dersinin 6. laboratuvar çalışmasıdır. Föyü hazırlayan Muhammet Yorulmaz; föyde amaç "dizgiler (strings)" olarak yazılı, ancak soruların hepsi C'de **yapılar (struct)** üzerine kurulu. Sorular föydeki hâliyle aktarıldı; föyün orijinal PDF'i yazının sonunda indirilebilir.

## Soru 1: Öğrenci listesini ortalamaya göre sıralama

Üyeleri aşağıdaki gibi olan `ogrenci` adındaki yapıyı tanımlayınız. Bu yapı tipinde tanımlanmış 10 elemanlı bir dizi tanımlayıp elemanlarını klavyeden giren ve ekranda ortalamasına göre büyükten küçüğe olacak şekilde listeleyen programı yazınız.

| Üye adı | Tür | Uzunluk |
|---|---|---|
| ad | karakter | 20 |
| soyad | karakter | 20 |
| ort | ondalık | – |

Örnek çalışma:

```
1. adı,soyadı,ortalamasını giriniz: Mehmet Çelik 3.45
2. adı,soyadı,ortalamasını giriniz: Dursun Mert 2.45
:   :   :
9. adı,soyadı,ortalamasını giriniz: Ahmet Serdar 3.00
10. adı,soyadı,ortalamasını giriniz: Sinan Tonguç 2.99
--------LİSTE------------------
Mehmet Çelik 3.45
Ahmet Serdar 3.00
Sinan Tonguç 2.99
Dursun Mert 2.45
:   :   :
```

## Soru 2: İki zamanı toplayan zamantopla fonksiyonu

Üyeleri aşağıdaki gibi olan `zaman` adındaki yapıyı (struct) tanımlayınız. Tanımladığınız bu yapı türünde ana fonksiyon içerisinde `a1` ve `a2` adında iki adet değişken tanımlayınız. Bunların ilk değerlerini (23, 30, 20) ve (1, 0, 40) olarak belirleyiniz. Bu iki değişkeni alıp ikinciyi birincinin üzerine ekleyen `zamantopla` adındaki fonksiyonu yazınız. Fonksiyon bittikten sonra `a1` içerisindeki değerler (0, 31, 0) olmalıdır. Bunu göstermek için değişkenlerin değerlerini ana fonksiyon içerisinde, fonksiyon çağrımından sonra ekrana yazdırınız.

| Üye adı | Tür |
|---|---|
| saat | tamsayı |
| dakika | tamsayı |
| saniye | tamsayı |

## Soru 3: Ondalık sayıyı parçalarına ayıran floatToplam

Ondalık (float) türündeki sayıları ifade etmek amacıyla üyeleri aşağıdaki gibi, adı `ondalik` olan bir yapı (struct) tanımlayınız.

| Üye adı | Üye tipi |
|---|---|
| İşareti | Karakter |
| Tam kısmı | Tamsayı |
| Ondalık kısmı | Tamsayı |

Buna göre, kendisine gönderilen 2 adet ondalıklı sayının toplamını ayrıştırıp yukarıdaki yapı türünde tanımlanmış 3. parametresindeki değişkene aktaran `floatToplam` adındaki fonksiyonu yazınız. Ondalık kısmın yalnızca 3 hanesi alınacaktır. Fonksiyonunuz aşağıdaki `main` fonksiyonuna uygun olmalıdır. Global değişken kullanmayınız ve `main` fonksiyonuna boş bırakılan yerler (noktalı yerler) hariç başka bir ekleme yapmayınız. Fonksiyon prototipi ve fonksiyon çağrısı da değerlendirilecektir.

Örnek program:

```c
........................... /*Yapı tanımı*/
............................... /*Prototip*/
int main()
{
   struct ondalik sonuc;
   float sayi1=-987.6543, sayi2=12.34;

   floatToplam(sayi1, sayi2, &sonuc);
   printf("Sonucun tamkısmı=%ld\n", sonuc.tam);
   printf("Sonucun ondalıkkısmı=%ld\n", sonuc.on);
   printf("Sonucun işareti=%c", sonuc.isaret);
   return 0;
}
```

Çıktı:

```
Sonucun tamkısmı=975
Sonucun ondalıkkısmı=314
Sonucun işareti= -
```

*Not: -987,6543 + 12,34 = -975,3143; yani tam kısım 975, ondalık kısmın ilk üç hanesi 314 ve işaret eksi. Föydeki tırnak işaretleri Word'ün "akıllı tırnak"larıydı; derlenebilsin diye düz tırnakla yazıldı.*
