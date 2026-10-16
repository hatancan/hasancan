---
baslik: BİL106 Laboratuvar Çalışması #10: C++ ile Sınıf Tanımlama
ozet: BİL106 Programlamaya Giriş dersinin 10. laboratuvar föyü (2015): Tarih sınıfı, iki boyutlu düzlemde doğru parçasını modelleyen Dogru sınıfı (eğim, kaydırma) ve üçgen kuralına uyan Ucgen sınıfı. Arayüz ve kod uygulaması ayrımıyla C++ sınıfları.
---

Bu yazı, Başkent Üniversitesi **BİL106 Programlamaya Giriş** dersinin 10. laboratuvar çalışmasıdır (Nisan 2015). Föyü hazırlayan Muhammet Yorulmaz; amaç **sınıf tanımlama**. Sorularda C++ sınıflarının arayüz (interface) ve kod uygulaması (implementation) olarak ayrı yazılması isteniyor; hangi üye fonksiyonların gerektiğine verilen örnek programa bakarak öğrenci karar veriyor. Föyün orijinal PDF'i yazının sonunda indirilebilir.

## Soru 1: Tarih sınıfı (20 puan)

Derste çözdüğünüz `Tarih` sınıfı örneğinin kodunu yazarak çalıştırınız.

## Soru 2: Dogru sınıfı (40 puan)

İki boyutlu düzlem üzerinde bir doğru parçasını modelleyen, adı `Dogru` olan sınıf arayüzünü (interface) ve kod uygulamasını (implementation) yazınız. Bu sınıf tanımlamasının üye verileri (member data), doğrunun iki ucunun koordinat değerleridir (x1, y1 ve x2, y2). Sınıfın hangi üye fonksiyonlara sahip olacağını aşağıdaki programdaki kullanıma göre siz belirleyiniz.

Not: İki noktası bilinen bir doğrunun eğimi şu formülle bulunur: **eğim = (y1 − y2) / (x1 − x2)**

Örnek program:

```cpp
...........................//Arayüzü koda dahil ediniz
int main()
{
  Dogru a;
  a.yaz();
  cout << "Doğrunun eğimi=" << a.egim() << endl;
  a.kaydir('x',3); // x ya da y ekseninde
                   // istenilen değer kadar kaydırır
  a.yaz();
  return 0;
}
```

Çıktı:

```
X1= 1, Y1= 2, X2= 3, Y2= 4
Doğrunun eğimi = 1
X1= 4, Y1= 2, X2= 6, Y2= 4
```

## Soru 3: Ucgen sınıfı (40 puan)

Üçgen geometrik şeklini modelleyen, adı `Ucgen` olan sınıf arayüzünü (interface) ve kod uygulamasını (implementation) yazınız. Bu sınıf tanımlamasının üye verileri (member data), üçgenin kenar uzunluk değerleridir. Sınıfın hangi üye fonksiyonlara sahip olacağını aşağıdaki programdaki kullanıma göre siz belirleyiniz.

Üçgen olma kuralı: Bir kenarın uzunluğu, diğer iki kenarın farkından büyük, toplamından küçüktür.

Örnek program:

```cpp
...........................//Arayüzü koda dahil ediniz
int main()
{
   Ucgen a( 3, 4);
   //istenirse 3 kenar uzunluğu da verilebilir
   //Ancak iki kenar verildiğinde 3. kenar üçgen kuralına
   //uygun olarak rastgele verilir.
   a.yaz();
   cout << "Üçgenin çevresi=" << a.cevre();
   return 0;
}
```

Çıktı:

```
a= 3, b= 4, c= 5
Üçgenin çevresi= 12
```

*Not: Üçüncü kenar rastgele seçildiği için çıktı her çalıştırmada farklı olabilir; 3-4-5 yalnızca bir örnektir. 3 ve 4 kenarlı bir üçgende üçüncü kenar 1 ile 7 arasında (uçlar hariç) olmalıdır.*
