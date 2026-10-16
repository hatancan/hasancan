---
baslik: EEM227 Veri Yapıları: Şablon (Template) Sınıflar ve vector Fonksiyonları
ozet: EEM227 Veri Yapıları dersinin 5. ve 6. haftalarına ait C++ programları (Ekim–Kasım 2007): farklı tipteki sayıları toplayan Sayi şablon sınıfı, << ve >> yüklenmiş Bilgi şablon sınıfı ve STL vector için şablon fonksiyonlar (yazdırma, boş mu, ekleme, resize).
---

Bu yazı, Başkent Üniversitesi **EEM227 Veri Yapıları** dersinin 2007 güz döneminde 5. ve 6. haftaların klasörlerinde bulunan üç C++ programını içeriyor. Konu **şablonlar (template)**: herhangi bir veri tipiyle çalışan sınıflar ve STL `vector` üzerinde çalışan şablon fonksiyonlar. İlk iki programın başında soru metni, sonunda ekran çıktısı yorum olarak yazılmış. Kaynak dosyalar yazının sonunda ZIP olarak indirilebilir.

## Soru 1: farklı tipteki sayıları toplayan şablon sınıf

> Farklı tipteki sayıların toplamını yapabilen ve sonucu aşırı yüklenmiş << operatörü sayesinde bastırabilen bir şablon sınıf yazınız.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

template <typename T>
class Sayi
{

 friend ostream &operator<<( ostream &, Sayi<T> & obje);

  public :

         Sayi(T a,T b) // Constructorda inline olarak bildirdik
         {
           data1 = a;
           data2 = b;
         };
  /* Şablon sınıfında aşırı yüklediğimiz << operatörünü inline olarak sınıf ADT
     si içerisinde bildirdik...
  */
 friend ostream &operator<<( ostream & yaz, Sayi<T> & obje)
     { yaz<<"Toplam Sonucu :"<< obje.data1 + obje.data2<<endl;
       return yaz;}

  private :
          T data1;
          T data2;

};

int main()
{

Sayi<int> Sayi1(3,5); // Dikkat !!! Tür yazılmalıdır...
cout<<"Tamsayi "<<Sayi1;

Sayi<float> Sayi2(1.3,5.8); // Tür yazılmalıdır...
cout<<"Float "<<Sayi2;

Sayi<double> Sayi3(45.343,62346.83); // Tür yazılmalıdır...
cout<<"Double "<<Sayi3;

system("pause");
return 0;
}
```

Ekran çıktısı:

```
Tamsayi Toplam Sonucu :8
Float Toplam Sonucu :7.1
Double Toplam Sonucu :62392.2
Press any key to continue . . .
```

Son satırda gerçek toplam 62392.173'tür; `cout` varsayılan olarak 6 anlamlı basamak gösterdiği için 62392.2 olarak yazılıyor.

## Soru 2: her tipte bilgiyi saklayıp yazdıran şablon sınıf

> Klavyeden girilen herhangi tipte bir bilgiyi depolayıp, bu bilgiyi ekranda tekrar bastırabilen bir şablon sınıfı tasarlayınız. Bu sınıf için klavyeden bilgi alma ve ekrana yazdırma işleminde kullanılmak üzere kullanılacak olan >> ve << operatörlerine aşırı yükleme uygulayınız. Klavyeden girilen farklı tipteki bilgiler için sınıfınızın çalıştığını gösteren ana programı kodlayınız (int, float, double, char, string).

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

template <typename T>
class Bilgi
{
 friend ostream &operator<<( ostream &, Bilgi<T> & obje);
 friend istream &operator>>( ostream &, Bilgi<T> & obje);

  public :

   friend ostream &operator<<( ostream & yaz, Bilgi<T> & obje)
     { yaz<<"Girilen Bilgi :"<< obje.data<<endl;
       return yaz;}

   friend istream &operator>>( istream & al, Bilgi<T> & obje)
     { al>>obje.data;
       return al;}

  private :
          T data;
};

int main()
{

cout<<"String :";
Bilgi<string> Nesne1;
cin>>Nesne1;
cout<<Nesne1;

cout<<"Char : ";
Bilgi<char> Nesne2;
cin>>Nesne2;
cout<<Nesne2;

cout<<"int :";
Bilgi<int> Nesne3;
cin>>Nesne3;
cout<<Nesne3;

cout<<"float : ";
Bilgi<float> Nesne4;
cin>>Nesne4;
cout<<Nesne4;

system("pause");
return 0;
}
```

Ekran çıktısı (Merhaba, W, 56 ve 34.67 klavyeden girilmiş):

```
String :Merhaba
Girilen Bilgi :Merhaba
Char : W
Girilen Bilgi :W
int :56
Girilen Bilgi :56
float : 34.67
Girilen Bilgi :34.67
Press any key to continue . . .
```

*Not: Sınıfın başındaki ikinci friend bildiriminde `operator>>`'ın ilk parametresi yanlışlıkla `ostream &` yazılmış; asıl tanım `istream &` ile yapıldığı için program çalışıyor, ama bu iki satırlık ön bildirim gereksiz. Soruda istenen tipler arasında double da var; ana programda double denenmemiş.*

## vector için şablon fonksiyonlar

6. hafta klasöründeki `Vectorler.cpp`, STL `vector` ile çalışan küçük şablon fonksiyonlar tanımlıyor: vektörü yazdırma, boş olup olmadığını sınama ve sona eleman ekleme. Diziden vektör oluşturma, `back()` ve `resize()` da gösteriliyor. Eleman çıkaran `Cikart` fonksiyonu yorum satırına alınmış (`pop_back()` değer döndürmediği için bu hâliyle derlenmez).

```cpp
#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

template <typename T>
void PrintVector(vector<T>& Ref)
{
      for(int i=0; i<Ref.size(); i++)
       cout<<Ref[i]<<" ";
      cout<<endl;
}

template <typename T>
bool BosmuDolumu(vector<T>& Ref)
{
  if(Ref.empty()==0)
   return true;
  else
   return false;
}

template <typename T>
void Ekle(vector<T>& Ref,T value)
{
  Ref.push_back(value);
}

/*
template <typename T>
T Cikart(vector<T>& Ref)
{
  T x;
  x=Ref.pop_back();
  return x;
}
*/

int main()
{

int a[5]={1,3,5,7,9};
double b[5]={2.2,4.4,6.6,8.8,10.10};

int sizea=sizeof(a)/sizeof(int);
int sizeb=sizeof(b)/sizeof(double);

vector<int> VecA(a,a+sizea);
vector<double> VecB(b,b+sizeb);

PrintVector(VecA);
PrintVector(VecB);

cout<<"Back of A : "<< VecA.back()<<endl;
cout<<"Back of B : "<< VecB.back()<<endl;

cout<<" Empty ? :"<< BosmuDolumu(VecA)<<endl;
cout<<" Empty ? :"<< BosmuDolumu(VecB)<<endl;

VecA.resize(10,0);
PrintVector(VecA);

VecB.resize(4,0);
PrintVector(VecB);

Ekle(VecA,5);
PrintVector(VecA);

Ekle(VecB,7.7);
PrintVector(VecB);

cout<<"\n";
system("pause");
return 0;
}
```

Ekran çıktısı:

```
1 3 5 7 9
2.2 4.4 6.6 8.8 10.1
Back of A : 9
Back of B : 10.1
 Empty ? :1
 Empty ? :1
1 3 5 7 9 0 0 0 0 0
2.2 4.4 6.6 8.8
1 3 5 7 9 0 0 0 0 0 5
2.2 4.4 6.6 8.8 7.7

Press any key to continue . . .
```

`resize(10,0)` vektörü 10 elemana büyütüp yeni yerleri 0 ile dolduruyor; `resize(4,0)` ise 5 elemanlı vektörü 4 elemana küçültüyor (son eleman 10.1 atılıyor).

*Not: `BosmuDolumu` fonksiyonu vektör **dolu** iken true döndürüyor (`empty()==0` dolu demektir). Bu yüzden iki dolu vektör için de "Empty ? :1" yazılıyor; soruya göre çıktı yanıltıcı. "Boş mu?" sorusu için doğrudan `return Ref.empty();` yazılmalı.*
