---
baslik: EEM227 Veri Yapıları: C++ Sınıf Soruları ve Çözümleri (Soru 3–6, Lab 1)
ozet: EEM227 Veri Yapıları dersinin C++ sınıflar konusundaki çözümlü soruları (Eylül 2007): const ve static üyeler, friend fonksiyon, Kitap sınıfı ve ISBN üretimi, Ali ile Veli'nin top çekme oyunu için Torba sınıfı; ayrıca rasyonel sayı ve karmaşık sayı sınıfı lab programları.
---

Bu yazı, Başkent Üniversitesi **EEM227 Veri Yapıları** dersinin 2007 güz döneminde paylaşılan **çözümlü sınav tipi sorularını** bir araya getiriyor. Soru 3–6 sayfaları **Öğr. Gör. Oğul Göçmen** imzalı ve 30 Eylül 2007 tarihli; hepsi C++'ta sınıflar (class), const ve static üyeler, friend fonksiyonlar üzerine. Yazının sonunda aynı haftanın klasöründeki iki lab programı da var: rasyonel sayı sınıfı (Lab 1 cevabı) ve operatör yüklemeli karmaşık sayı sınıfı. Soruların orijinal PDF'leri ve kaynak dosyalar yazının sonunda ZIP olarak indirilebilir.

## Soru 3: A sınıfı üzerindeki deyimler doğru mu?

Aşağıda A sınıfına ait tanımlamalar verilmiştir. Bu tanımlamalara göre, size verilen ana (main) fonksiyon içerisinde A sınıfı üzerinde tanımlanan deyimlerle yapılan işlemlerin doğru olup olmadıklarını yazınız. Eğer yapılan işlem yanlışsa nedenini kısaca açıklayınız.

```cpp
class A {
   private:
       int a;
       float b;
       char s[15];
       static char ch;
   public:
       double d;
       const unsigned c;
       A(int=0, float=1.2);
       int getA() const;
       void setMembers(int, char *);
       static void p();
};

// Bu kısımda sınıf(class) tanımı içinde yer alan fonksiyonlar gerçekleştiriliyor.
// ...
```

Çözüm:

| Deyim | Doğru/Yanlış | Yanlışın nedeni |
|---|---|---|
| `A obj1;` | DOĞRU | |
| `const A obj2(24);` | DOĞRU | |
| `A obj3(12, 2.2);` | DOĞRU | |
| `obj1.a = 12;` | YANLIŞ | Private üyeye erişilemez |
| `obj3.d = obj2.getA();` | DOĞRU | |
| `obj2.setMembers(3,"aaa");` | YANLIŞ | Const nesne const olmayan fonksiyonu çağıramaz |
| `obj1.p();` | DOĞRU | |
| `A::p();` | DOĞRU | |
| `obj3.c = 'x';` | YANLIŞ | Const üyeye atama yapılamaz |
| `A::setMembers(1,"bbb");` | YANLIŞ | Fonksiyon statik değil |

## Soru 4: Kütüphane için Kitap sınıfı

Bir kütüphanedeki kitapların organizasyonunu gerçekleştirmek amacıyla, ismi "Kitap" olan bir sınıf ve bu sınıfa ait fonksiyonları C++ programı olarak gerçekleştirmek istiyoruz. Buna göre kütüphanedeki sistem şu şekilde işlemektedir:

- Kütüphane içerisindeki her bir kitabın en fazla 100 karakterden oluşan bir adı, en fazla 14 karakterden oluşan ISBN kodu, basım yılı ve sayfa sayısı bilgileri bulunmaktadır.
- 14 karakterden oluşan ISBN kodları ISBN-2006-2987 biçiminde tutulmaktadır. Buna göre her ISBN numarası birbirinden tire (-) ile ayrılmış 3 alandan oluşmaktadır. Birinci alan bütün kodlarda aynı biçimde 'I', 'S', 'B', 'N' karakterlerinden, ikinci alan kitabın yılından, son alan ise ilgili kitabın kütüphaneye kaydedilen kaçıncı kitap olduğunu ifade eden bir numaradan oluşmaktadır. Örneğin 2006 yılında kütüphaneye kaydedilen ve kütüphanedeki 15. kitap olan kitabın ISBN kodu ISBN-2006-15 biçiminde olmalıdır.
- Kütüphane içerisine yeni bir kitap ekleneceği zaman ilgili kitabın ISBN numarasının program tarafından otomatik olarak üretilip atanması gerekmektedir (2006 yılında olduğumuzu varsayabilirsiniz).
- Herhangi bir kitabın kütüphaneye kaydedilebilmesi için kitap adı, basım yılı ve sayfa sayısının girilmesi zorunludur.
- Bir kitap kütüphaneye kaydedildiğinde sayfa sayısı kesin olarak belirlenmekte ve bir daha değiştirilmemesi istenmektedir.
- Kütüphanede kayıtlı toplam kitap sayısının program tarafından ekranda gösterilebilmesi beklenmektedir.

Yukarıda belirlenen kısıtlara göre, sınıf içerisinde tanımlayacağınız bütün değişkenlerin private olacağını varsayarak, ilgili sınıf tanımı ve gerekli fonksiyonları yazınız.

**NOT:** Bu programı gerçekleştirirken eğer int bir sayıyı string olarak dönüştürmeye gereksinim duyarsanız, aşağıda prototipi verilen fonksiyonu sanki programınız içinde gerçekleştirilmiş gibi kullanabilirsiniz: `char * IntToString (int number)`. Bu fonksiyon int bir sayıyı (number) parametre olarak almakta ve ilgili sayıyı string olarak geri döndürmektedir.

Çözüm:

```cpp
#include <iostream>
#include <cstring>
using namespace std;
class Kitap{
      private:
                 char KitapAd[100];
                 char ISBN[15];
                 unsigned BasimYili;
                 const unsigned SayfaSayisi;
                 static unsigned KitapSayisi;
      public:
                Kitap(char *ad, unsigned yil, unsigned ss);
                static void ToplamKitapSayisi();
};

unsigned Kitap::KitapSayisi = 0;

Kitap::Kitap(char *ad, unsigned yil, unsigned ss):SayfaSayisi(ss)
{
     strcpy(KitapAd,ad);
     strcpy(ISBN,"ISBN-2006-");
     strcat(ISBN,IntToStr(KitapNo));
     BasimYili = yil;
     KitapSayisi++;
}

void Kitap::ToplamKitapSayisi()
{
     cout<<"Toplam Kitap Sayisi:"<<KitapSayisi<<endl;
}
```

Sayfa sayısının sonradan değiştirilememesi `const unsigned SayfaSayisi` ile (kurucunun ilk değer listesinde atanarak), toplam kitap sayısı ise bütün nesnelerin paylaştığı `static unsigned KitapSayisi` ile sağlanıyor. Toplamı gösteren fonksiyon da static olduğu için nesne olmadan `Kitap::ToplamKitapSayisi()` diye çağrılabilir.

*Not: Çözümdeki `IntToStr(KitapNo)` çağrısında hem fonksiyon adı soruda verilen `IntToString` ile uyuşmuyor hem de `KitapNo` diye bir değişken tanımlı değil. Kitabın sıra numarası `KitapSayisi + 1` olmalı (ya da `KitapSayisi++` satırı önce yapılıp `IntToString(KitapSayisi)` kullanılmalı).*

## Soru 5: friend fonksiyon ve const nesne

Aşağıdaki sınıf (class) tanımlamasına göre, main fonksiyon içerisinde yazılan ifadelerden yanlış olanların nedenlerini yazınız.

```cpp
class A
{
    friend void MyFunc(A &a, double b);
    public:
      float var1;
      A(int, double=1.2);
      A();
      int getValue() const;
      void setValue(int, char *);
      static void print();
    private:
      int var2;
      double var3;
      char MyStr[15];
      static char MyChar;
}

void MyFunc(A &a, double b)//Dikkat Bu fonksiyon Sınıfın üyesi değildir.
{    a.var3 = b; }

int main()
{
    A c(35);
    const A Nesne1;
    A Nesne2(18);
    A Nesne3(29, 4.2);
    Nesne1.var2=29;
    Nesne3.var1 = Nesne1.getValue();
    Nesne1.setValue(5, "yyy", MyStr);
    Nesne3.print();
    MyFunc(5.8, c);
    A::print();
    Nesne3.MyChar = 'x';
    A::setValue(1, "zzz");
    return 0;
}
```

Çözüm (her yanlış 5 puan):

| Deyim | Yanlışın nedeni |
|---|---|
| `Nesne1.var2=29;` | Nesne private üyeye doğrudan erişemez. Nesne const olduğundan değeri değiştirilemez. |
| `Nesne1.setValue(5, "yyy", MyStr);` | MyStr fazla yazılmış. Const nesnenin const olmayan fonksiyonu çağrılamaz. |
| `MyFunc(5.8, c);` | `MyFunc(c,5.8)` olmalı. |
| `Nesne3.MyChar = 'x';` | Nesne private üyeye doğrudan erişemez. |
| `A::setValue(1, "zzz");` | Fonksiyon static değil. |

Diğer satırlar (`A c(35);`, `const A Nesne1;`, `A Nesne2(18);`, `A Nesne3(29, 4.2);`, `Nesne3.var1 = Nesne1.getValue();`, `Nesne3.print();`, `A::print();`) doğrudur.

*Not: Sorudaki sınıf tanımının kapanış parantezinden sonra `;` eksik (`};` olmalı).*

## Soru 6: Ali ile Veli'nin top oyunu (Torba sınıfı, 35 puan)

Ali ve Veli bir şans oyunu oynamaktadır. Ali'nin elindeki A torbasında 10 kırmızı, 6 sarı, 3 adet de mavi renkli top vardır. Veli'nin elindeki B torbasında 10 kırmızı, 3 sarı, 6 adet de mavi renkli top vardır. Bu oyunun kuralı şu şekildedir: Oyuna herhangi bir kişi başlar ve sırayla birer top çekilir. Kendi torbasından rastgele bir top çeker. Çektiği top kırmızı ise topu torba dışına çıkartır, değilse torbaya geri bırakır. Çektiği top kırmızı olsa da olmasa da sıra diğer oyuncuya geçer. Herhangi bir kişi torba dışında toplamda 3 kırmızı topa sahip olursa oyunu kazanır.

Bu oyunu gerçekleştirecek bir C++ programı yazmanız isteniyor. Bu program içerisinde "Torba" isimli bir sınıf yazınız; bu sınıfın üye fonksiyonlarını (member functions) public, üye verilerini (data members) private olarak tanımlayınız. Buna göre:

- Bu sınıfın kurucu fonksiyonu (constructor) sırası ile kırmızı, sarı ve mavi renkli topların miktarlarını parametre olarak alır. Eğer herhangi bir renkteki top sayısı parametre olarak verilmez ise, o topun torba içerisindeki miktarını 10 olarak belirler.
- "Goster" isimli üye fonksiyon, bir torbanın içerisinde hangi renk toptan kaç adet olduğunu ve torbadaki toplam top sayısını ekranda yazdırır.
- "ToplamTop" isimli üye fonksiyon, bir torbanın içerisinde bulunan toplam top miktarını döndürür.
- "ToplarinOrani" isimli üye fonksiyon, bir torba içerisinde her renkteki top için o rengin toplam top sayısına olan yüzdelik oranını hesaplar ve ekranda yazdırır.
- "TopCek" isimli üye fonksiyon, bir torbadan rastgele renkte bir tane top çeker ve değeri döndürür.
- "TopCikart" isimli üye fonksiyon, kendisine parametre olarak verilen değerdeki topu torbadan çıkartır.
- "TopEkle" isimli fonksiyon, kendisine parametre olarak verilen değerdeki topu torbaya ekler.

Buna göre oyun bittiğinde kazanan kişiyi, torbası içerisindeki topların sayısını ve torbasındaki topların yüzdelik oranını ekrana yazdıran bir program yazınız. **Dikkat:** Yazacağınız kodu parçalara bölünmüş şekilde yazınız ("main.cpp", "Torba.h", "Torba.cpp").

### Torba.h

```cpp
// --------- Torba.h -----------------------------------
#ifndef TORBA_H
#define TORBA_H
class Torba {
   public:
        void ToplarinOrani();
        int ToplamTop();
        Torba( int, int, int);
        int TopCek( );
        void TopCikart( int );
        void TopEkle ( int );
        void Goster();
        int KirmiziAdeti();
   private:
        int KSM[3]; // Kırmızı[0] Sarı[1] Mavi[2] top adeti
};
#endif
```

### Torba.cpp

```cpp
#include <iostream>
#include <time.h>
using namespace std;
#include "Torba.h"

void Torba::ToplarinOrani()
{
  Goster();
  if(ToplamTop()>0){
    cout<<" YUZDELIK ORANLAR "<<endl;
    cout<<" KIRMIZI : % "<<(1.0*(KSM[0])/ToplamTop())*100<<endl;
    cout<<"     SARI : % "<<(1.0*(KSM[1])/ToplamTop())*100<<endl;
    cout<<"     MAVi : % "<<(1.0*(KSM[2])/ToplamTop())*100<<endl;
  }
  else{
    cout<<" YUZDELIK ORANLAR "<<endl;
    cout<<" KIRMIZI : % 0"<<endl;
    cout<<"     SARI : % 0"<<endl;
    cout<<"     MAVi : % 0"<<endl;
  }
}

int Torba::ToplamTop()
{       return KSM[0] + KSM[1] + KSM[2];     }

int Torba::TopCek ()
{
  srand(time(NULL));
  switch(rand()%3){
     case 0: KSM[0]--; return 0; break;      //   ÇEKİLEN TOP KIRMIZI ÇIKTI
     case 1: KSM[1]--; return 1; break;      //   ÇEKİLEN TOP SARI ÇIKTI
     case 2: KSM[2]--; return 2; break;      //   ÇEKİLEN TOP MAVI ÇIKTI
  }
}

void Torba::TopCikart( int renkkodu)
{
  KSM[renkkodu]--;
}

void Torba::TopEkle( int renkkodu)
{
  KSM[renkkodu]++;
}

void Torba::Goster ()
{
   cout<<endl;
   cout<<" Kirmizi = "<<KSM[0]<<endl;
   cout<<" Sari    = "<<KSM[1]<<endl;
   cout<<" Mavi    = "<<KSM[2]<<endl;
   cout<<" Toplam = "<<ToplamTop()<<endl;
   cout<<endl;
}
Torba::Torba(int k=10, int s=10, int m=10)
{
   KSM[0] = k;
   KSM[1] = s;
   KSM[2] = m;
   Goster();
}
```

### main.cpp

```cpp
// --------- Main.cpp   -----------------------------------------
#include <iostream>
#include <time.h>
#include "Torba.h"
using namespace std;

int main()
{
  cout<<" \n\n Oyuna baslamadan once, Ali'nin torbasi icindeki toplar...";
  Torba A(10,6,3);
  cout<<" Oyuna baslamadan once, Veli'nin torbasi icindeki toplar...";
  Torba B(10,3,6);
  int sira =1,renkkodu=0,Aadet=0,Badet=0;
  cout<<" Oyun basliyor...\n";

  while(Aadet!=3 && Badet!=3){

      // ALİNİN ELİNDEKİ A TORBASI İÇİN GEREKLİ İŞLEMLER

      if(sira%2){
         renkkodu=A.TopCek();
         if( renkkodu == 0 ){ //- KIRMIZI TOP İSE
            A.TopEkle(renkkodu); // TopCekin azalttığı değeri engelle
            A.TopCikart(renkkodu);
            Aadet++;

            if(Aadet == 3){
               cout<<" OYUNU ALI KAZANDI.";
               A.ToplarinOrani();
               cout<<" Oyun bitti !\n\n";
            }
         }
         else
             A.TopEkle(renkkodu);
         }
//************************************************************************
// VELİNİN ELİNDEKİ B TORBASI İÇİN GEREKLİ İŞLEMLER

      else{
         renkkodu=B.TopCek();
         if( renkkodu == 0 ){
            B.TopEkle(renkkodu);
            B.TopCikart(renkkodu);
            Badet++;
            if(Badet == 3){
                cout<<" OYUNU VELI KAZANDI.";
                B.ToplarinOrani();
                cout<<" Oyun bitti !\n\n";
            }
         }
         else
              B.TopEkle(renkkodu);
      }
 //************************************************************************
      sira ++;
  }
  return 0; }
```

*Not: Çözümdeki `TopCek` rengi torbadaki top sayılarıyla orantılı seçmiyor; `rand()%3` ile üç renkten birini eşit olasılıkla seçiyor (Ali'nin torbasında kırmızı çekme olasılığı 10/19 olmalıyken 1/3 oluyor; o renkten top kalmamışsa sayı eksiye de düşebilir). Ayrıca `srand(time(NULL))` her çekilişte yeniden çağrıldığı için aynı saniye içindeki çekilişler hep aynı sonucu verir; `srand` programın başında bir kez çağrılmalı. Kurucunun varsayılan değerleri (`=10`) yalnızca Torba.cpp'deki tanımda yazıldığı için main.cpp'den görünmez; sorudaki "verilmezse 10" kuralı için varsayılanlar Torba.h'deki bildirimde olmalı.*

## Lab 1 cevabı: rasyonel sayı sınıfı

Klasördeki `EEM227_Lab1_Cevap.cpp` dosyası (Ekim 2006 tarihli), pay ve paydayı tutan, sadeleştiren, iki rasyonel sayının eşitliğini sınayan, çarpan ve bölen bir `rasyonel` sınıfı. Toplama fonksiyonu yorum satırına alınmış.

```cpp
#include <iostream>
using namespace std;
#define TRUE  1
#define FALSE 0

class rasyonel
{
private :
  long pay;
  long payda;
  long payilk;
  long paydailk;
  void indirge(void);

public :
//void topla(rasyonel);
  void carp(rasyonel);
  void bol(rasyonel);
   int esit(rasyonel);
  void degerata(long, long);
  void yazdir(void);
};

/*
void rasyonel::topla(rasyonel r)
{
  int k, tpay, tpayda;
  rasyonel rnl;

  // Her iki rasyonel sayının en küçük terimlerine indirgenmesi
  indirge();
  r.indirge();

  rnl.degerata(payda, r.payda);
  rnl.indirge();
  k=rnl.payda;

  tpayda = payda * k;
  tpay = pay*k + r.pay*(tpayda/r.payda);
  cout<<tpayda,tpay;
  rnl.degerata(tpay, tpayda);
  rnl.indirge();
}
*/

void rasyonel::bol(rasyonel r)
{
  rasyonel rnl;
  rnl.degerata(r.payda, r.pay);
  //cout<<"Bolme Sonucu : "<<endl;
  carp(rnl);
}

void rasyonel::carp(rasyonel r)
{
  rasyonel rnl, rnl1, rnl2;
  int py, pyd;
  // Her iki rasyonel sayının en küçük terimlerine indirgenmesi
  indirge();
  r.indirge();

  rnl1.degerata(pay, r.payda);
  rnl.indirge();
  rnl2.degerata(r.pay, payda);
  rnl2.indirge();

  py  = rnl1.pay * rnl2.pay;
  pyd = rnl1.payda * rnl2.payda;

  if(pyd==1)
     cout<<"Sonuc : "<<py;
  else
     cout<<"Sonuc : "<<py<<"/"<<pyd<<endl;
}

void rasyonel::degerata(long n, long d)
  {
    if(d==0) cout << "Hata! payda 0 olamaz";
    pay = n;
    payda = d;
    payilk=n;
    paydailk=d;
    indirge();
  };

 void rasyonel::yazdir(void) {
       cout<<"\nGirilen degerler:\n" ;
       cout<<"------------------";
       cout<<"\nPay : "<<payilk<<endl;
       cout<<"Payda : "<<paydailk<<endl;
       if(payda==1)
       cout<<"Sadelesmis Hali : "<<pay<<endl;
       else
       cout <<"Sadelesmis Hali : " <<pay << "/" << payda << endl;
       };

void rasyonel::indirge(void)
{
  int a, b, r, sign;
  if (pay==0) payda = 1;
  sign = 1;
  if(pay<0 && payda<0) { pay = -pay; payda = -payda; };
  if(pay<0) { pay = -pay; sign = -1; };
  if(payda<0) { payda = -payda; sign = -1; };
  if(pay>payda) { a=pay; b=payda; } else { a=payda; b=pay; };
  while(b!=0) { r = a%b; a=b; b=r; };
  pay = sign*pay / a;
  payda = payda / a;
}
  int payilk,paydailk; // Global tanımladık...

  int rasyonel::esit(rasyonel r)
{
  // Her iki rasyonel sayının en küçük terimlerine indirgenmesi
  indirge();
  r.indirge();
  if (pay==r.pay && payda==r.payda) return TRUE; else return FALSE;
}

int main()
{
  rasyonel r1;
  cout<<"1.Sayinin Pay Degeri : ? ";
  cin>>payilk;
  cout<<"\n1.Sayinin Payda Degeri : ?";
  cin>>paydailk;
  r1.degerata(payilk,paydailk);
  r1.yazdir();

  rasyonel r2;
  cout<<"\n2.Sayinin Pay Degeri : ? ";
  cin>>payilk;
  cout<<"\n2.Sayinin Payda Degeri : ?";
  cin>>paydailk;
  r2.degerata(payilk,paydailk);
  r2.yazdir();

  cout<<"\n Sayilar esitmi (0=H, 1=E)? : "<<r1.esit(r2);
  cout<<"\n";
  cout<<"\n Carpma Sonucu: "<<endl;
  r1.carp(r2);
  cout<<"\n Bolme Sonucu: "<<endl;
  r1.bol(r2);
/*
  cout<<"\n\n Toplama Sonucu: ";
  r1.topla(r2);
*/
  cout<<"\n \n";
  system("pause");
return 0;
}
```

Çarpma, çapraz sadeleştirme ile yapılıyor: birinci sayının payı ikinci sayının paydasıyla, ikinci sayının payı birinci sayının paydasıyla ayrı ayrı sadeleştirilip sonra çarpılıyor. Sadeleştirmede `indirge` fonksiyonu Öklid algoritmasıyla en büyük ortak böleni buluyor.

*Not: `carp` fonksiyonunda `rnl1.degerata(...)` satırından sonra `rnl1.indirge();` yerine yanlışlıkla `rnl.indirge();` yazılmış (rnl1 zaten `degerata` içinde sadeleştiği için sonuç değişmiyor, ama satır ilk değeri verilmemiş `rnl` nesnesi üzerinde çalışıyor).*

## Karmaşık sayı sınıfı (operatör yükleme)

Aynı klasördeki `karmasik.cpp` (Ekim 2007), +, - ve * operatörlerini ve << ile >> stream operatörlerini karmaşık sayılar için yüklüyor. Program üç karmaşık sayı okuyup a+b+c toplamını, a-(b+c) farkını ve a·b + b·c değerini yazdırıyor.

```cpp
#include<iostream>
#include<stdlib.h>
using std::cin;
using std::cout;
using std::endl;
using std::istream;
using std::ostream;
class Karmasik
{
      friend istream& operator>>(istream& oku,Karmasik& nesne);
      friend ostream& operator<<(ostream& yaz,Karmasik& nesne);
      private:
              int gercel,sanal;
      public:
             Karmasik(int a=0,int b=0)
             {
                   gercel=a;
                   sanal=b;
             }
             int retsanal()
             {
                 return sanal;
             }
             int retgercel()
             {
                 return gercel;
             }
             Karmasik operator+(Karmasik& nesne)
             {
                       Karmasik top;
                       top.gercel=gercel+nesne.retgercel();
                       top.sanal=sanal+nesne.retsanal();
                       return top;
             }
             Karmasik operator-(Karmasik& nesne)
             {
                       Karmasik cik;
                       cik.gercel=gercel-nesne.retgercel();
                       cik.sanal=sanal-nesne.retsanal();
                       return cik;
             }
             Karmasik operator*(Karmasik& nesne)
             {
                       Karmasik carp;
                       carp.gercel=(gercel*nesne.retgercel())-(sanal*nesne.retsanal());
                       carp.sanal=(gercel*nesne.retsanal())+(sanal*nesne.retgercel());
                       return carp;
             }
};
istream&operator>>(istream& oku,Karmasik& nesne)
      {
             oku>>nesne.gercel>>nesne.sanal;;
      }
ostream&operator<<(ostream& yaz,Karmasik& nesne)
      {
             if(nesne.sanal>=0)
             yaz<<nesne.gercel<<"+"<<nesne.sanal<<"i";
             else
             yaz<<nesne.gercel<<nesne.sanal<<"i";
      }

int main()
{
    Karmasik a,b,c,d,s,f;
    cout<<"Birinci Sayiyi Gir"<<endl;
    cin>>a;
    cout<<"Ikinci Sayiyi Gir"<<endl;
    cin>>b;
    cout<<"Ucuncu Sayiyi Gir"<<endl;
    cin>>c;
    d=a+b;
    d=d+c;
    cout<<"Toplam:"; cout<<d; cout<<endl;
    s=b+c;
    d=a-s;
    cout<<"Fark:"; cout<<d; cout<<endl;
    s=a*b;
    d=b*c;
    f=s+d;
    cout<<"Carpim:"; cout<<f; cout<<endl;
    system("PAUSE");
    return 0;
}
```

*Not: `operator>>` ve `operator<<` fonksiyonları referans döndüreceklerini bildirdikleri hâlde `return oku;` / `return yaz;` satırları eksik; bu tanımsız davranıştır. Bu yüzden programda `cout<<d<<endl` gibi zincirleme yerine çıktılar ayrı ayrı yazdırılmış.*
