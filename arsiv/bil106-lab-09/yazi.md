---
baslik: BİL106 Laboratuvar Çalışması #9: C++ Programlama Diline Giriş
ozet: BİL106 Programlamaya Giriş dersinin 9. laboratuvar föyü: setw ve setprecision ile toplam ve ortalama, referansla asalatamamla fonksiyonu, varsayılan parametreli simetrik fonksiyonu ve sınıf (class) bonusu. C++ ile ilk adımlar.
---

Bu yazı, Başkent Üniversitesi **BİL106 Programlamaya Giriş** dersinin 9. laboratuvar çalışmasıdır. Föyü hazırlayan Muhammet Yorulmaz; amaç **C++ programlama diline giriş**. C'den C++'a geçişin üç tipik yeniliği soruların merkezinde: `cout` ile biçimli çıktı, **referans (takma ad)** ile parametre aktarımı ve **varsayılan parametre**. Föyün orijinal PDF'i yazının sonunda indirilebilir.

## Soru 1: Toplam ve ortalama (35 puan)

Klavyeden "Devam etmek istiyor musunuz?" sorusuna H (hayır) cevabı verilene kadar girilen sayıların toplamını ve ortalamasını ekrana yazan C++ programını yazınız.

Ondalıklı değerleri ekrana biçimli yazdırmak için aşağıdaki satırları programın başlığına ekleyiniz ve programınızda örneğe bakarak kullanınız.

```cpp
#include <iomanip>
using std::setprecision;   // Noktadan sonraki basamak sayısı
using std::setw;           // Sayının genişliği
```

Örnek:

```cpp
cout<<"sayı="<<setw(10)<<setprecision(4)<<18.6666666666666<<endl;
```

Çıktı:

```
Sayı =     18.67
```

Örnek çalışma:

```
BİLGİ GİRİŞ
---------------------------------
Sayı= 7
Devam etmek istiyor musunuz?(E/H): E
Sayı= 9
Devam etmek istiyor musunuz?(E/H): E
Sayı= 40
Devam etmek istiyor musunuz?(E/H): H
----------------------------------
Girilen 3 adet sayının:
Toplamı = 56.00
Ortalaması= 18.67
```

## Soru 2: Referansla asalatamamla (35 puan)

Parametre olarak aldığı tamsayıyı kendisinden büyük en küçük asal sayıya dönüştüren `asalatamamla` adındaki fonksiyonu, tamsayının klavyeden girildiği bir `main` fonksiyonu ile beraber yazınız. Klavyeden girilen tamsayının fonksiyona gönderildikten sonraki değişmiş hâlini `main` içerisinde ekrana yazdırınız. Global değişken kullanılmamalıdır. Bu programı **gösterici (pointer) kullanmadan referans (takma ad) kullanarak** yazınız.

Örnek çalışma:

```
Tam sayıyı giriniz : 6
--------------------------------
Sayının dönüştüğü asal sayı = 7
```

## Soru 3: Varsayılan parametreli simetrik (30 puan)

Kendisine gönderilen bir noktanın koordinatları ve eksen bilgisine göre noktanın simetriğini üreten `simetrik` adındaki fonksiyonu yazınız. Bu fonksiyon 3 adet parametre alır: noktanın x ve y değeri ile eksen bilgisi. Eksen bilgisi olarak `'X'` gönderildiğinde X eksenine göre, `'Y'` gönderildiğinde Y eksenine göre, `'O'` gönderildiğinde ise orijine göre simetrik alacaktır. Fonksiyonu, eksen bilgisi gönderilmediğinde **varsayılan olarak orijin** olacak şekilde tanımlayınız.

## Bonus (10 puan)

Derste gösterilen herhangi bir sınıf (class) uygulamasını yazarak çalıştırınız.

*Not: PDF'teki karakter kodlaması bozuk olduğu için bazı "İ" harfleri "Đ" olarak görünüyor; yazıda düzeltildi. Föyün iç dosya adı "Bil106_lab11_06" ve dosya 2010 tarihli, başlığı ise "Laboratuvar Çalışması #9".*
