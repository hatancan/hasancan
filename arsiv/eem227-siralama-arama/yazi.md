---
baslik: EEM227 Veri Yapıları: Sıralama ve Arama Algoritmaları (Hafta 4)
ozet: EEM227 Veri Yapıları dersinin 4. hafta ders notu ve programları (Öğr. Gör. Oğul Göçmen, Ekim 2007): bubble sort, selection sort, quick sort, shell sort, sıralı arama, ikili arama ve merge algoritmaları; C ve vector şablonlu C++ kodlarıyla.
---

Bu yazı, Başkent Üniversitesi **EEM227 Veri Yapıları** dersinin 2007 güz dönemi **4. hafta ders notudur**: sıralama (sort) ve arama (search) algoritmaları. Hazırlayan **Öğr. Gör. Oğul Göçmen**, tarih 21 Ekim 2007. Notun metni ve örnek programları aşağıda; sonda aynı haftanın klasöründeki STL (vector) ile yazılmış ek programlar da var. Ders notunun PDF'i ve bütün kaynak dosyalar yazının sonunda ZIP olarak indirilebilir.

## Sıralama (sort) ve arama (search) algoritmaları

Düzensiz olarak verilmiş dizi elemanlarını küçükten büyüğe veya büyükten küçüğe doğru sıralamak, bir düzene koymak için çeşitli sıralama algoritmaları geliştirilmiştir. Sıralanan bilgilerde arama işlemleri de kolaylaşmaktadır. En çok kullanılan sıralama algoritmaları aşağıdaki algoritmalardır:

1. Bubble sort (kabarcık sıralama)
1. Shell sort (ikili bölerek sıralama)
1. Selection sort (seçerek sıralama)
1. Quick sort (hızlı sıralama)

## Bubble sort algoritması

Dizide yer alan her eleman, sırayla kendisinden sonra gelen elemanla karşılaştırılır ve gerekiyorsa yer değiştirilir. Sıralama işlemi yer değiştirme olduğu sürece devam eder. Herhangi bir sıralama yönteminin etkinliğini analiz ederken kaç kez karşılaştırma ve yer değiştirme (takas) yapıldığına bakılır. Kabarcık sıralamada karşılaştırma sayısı daima aynıdır. Verilen dizi sıralı olsa bile kullanılan iki for döngüsü belirtilen sayıda tekrar yapar. Bu da yöntemin (n² – n)/2 karşılaştırma yapacağı anlamına gelir. Buradaki n sıralanacak eleman sayısıdır. Bu formüle dıştaki döngünün n-1 kez, içteki döngünün de ortalama n/2 kez çalıştığı düşünülerek varılmıştır.

Kabarcık sıralamanın bir n² algoritması olduğu söylenmektedir, çünkü çalışma süresi sıraladığı eleman sayısının karesiyle orantılıdır. Dolayısıyla dizi elemanlarının sayısının fazla olması durumunda işlem zamanı fazlalaşan bir algoritmadır. Sırası tamamen bozuk bir veri yapısı için, yani en kötü durum için bu algoritmanın Büyük-O notasyonu (Big-O notation) O(n²)'dir.

(n-1) + (n-2) + … + 2 + 1 = n·(n-1)/2 = O(n²)

*Not: Ders notunda bu toplam n·(n-2)/2 olarak yazılmış; doğrusu n·(n-1)/2'dir (yukarıdaki (n² – n)/2 ile aynı).*

Özel bir durum olarak, eğer verinin belli kısmı sıralı ise, n adet verinin c tanesi sıralı değil ise algoritmanın karmaşıklığı O(cn) olmaktadır.

### Örnek 1.1: rastgele elemanlı diziyi bubble sort ile sıralama

```cpp
#include <iostream>

using namespace std;

//--------------------------- bubbleSort -----------------------------
//
// Amaç     : Verilen değerlerin, küçükten büyüğe sıraya koymak
//
// Giriş parametresi : Değerlerin yazılı olduğu vektör
//
// Dönüş değeri : void
//
// Fonksiyonda sıralama işlemi, Bubble Sort algoritması ile
// gerçeklenmiştir.
//
//-----------------------------------------------------------------------

void bubbleSort ( int dizi[],int size)
{
      int temp;
// for her dönüşünde, sıraya sokulmamış elemanların ilkinden başlayarak
// her elemanı sağdaki komşusu ile karşılaştırıyor. Eğer komşusundan
// daha büyük bir değere sahipse, onunla yer değiştiriliyor.
      for (int i = size; i > 2; i --)
      {
// Buradaki i, sıraya sokulmamış eleman sayısını gösteriyor, yani
// (i-1). terime kadar olan elemanlar henüz sıralı değiller.
// Sıraya girmemiş elemanların herbiri, sağındaki komşusu ile
// karşılaştırılıyor. Eğer değeri komşusundan büyükse, onunla yer
// değiştiriliyor. Sıraya sokulmamış elemanların değerce en büyük
// olanı, (i-1). terime kadar tüm elemanlar ile yer değiştireceği
// için, sıralı elemanların başına kadar ulaşır. Daha önceden
// sıraya girmiş elemanların her biri zaten bu elemandan daha
// büyük bir değere sahip olduğu için, bu eleman da artık sıralıdır.
            for (int j = 0; j < i - 1; j ++)
            {
            // Komşusu ile yer değiştiriyor. (swap)
                  if (dizi[j] > dizi[j + 1])
                  {
                        temp = dizi[j + 1];
                        dizi[j + 1] = dizi[j];
                        dizi[j] = temp;
                  }
            }
      }
}

//------------------------------ main -----------------------------------

int main ()
{
     int d[20];

// 20 elemanlı, rasgele bir katar oluşturuluyor.
     for (int i = 0; i < 20; i ++)
     d[i]=(rand () % 1000);
     bubbleSort (d,20);

     for (int i = 0; i < 20; i ++)
     cout<<d[i]<<" ";
     cout<<endl;
     system("pause");
     return 0;
}
```

*Not: Dış döngünün koşulu `i > 2` olduğu için son geçiş (yalnızca `dizi[0]` ile `dizi[1]`'i karşılaştıran i = 2 adımı) hiç yapılmıyor; ilk iki eleman ters sırada kalabilir. Örneğin {3, 2, 1} dizisi {2, 1, 3} olarak kalır. Koşul `i > 1` olmalı. Aynı hata Örnek 1.2'de ve klasördeki BubbleSortSTL.cpp'de de var.*

### Örnek 1.2: bubble sort (vector şablonu ile)

```cpp
#include <iostream>
#include <vector>
using namespace std;

template <class T>
void bubbleSort (vector<T>& dizi)
{     for (int i = dizi.size (); i > 2; i --)
      { for (int j = 0; j < i - 1; j ++)
            { if (dizi[j] > dizi[j + 1])
                  {     T temp = dizi[j + 1];
                        dizi[j + 1] = dizi[j];
                        dizi[j] = temp;
                  }
            }
      }
}

//------------------------------ main -----------------------------------

int main ()
{
      vector<int> D;

// 20 elemanlı, rasgele bir katar oluşturuluyor.
      for (int i = 0; i < 20; i ++) D.push_back (rand () % 10);
      bubbleSort (D);
      return 0;
}
```

## Selection sort algoritması

Seçerek sıralamada, eğer dizi küçükten büyüğe sıralanacaksa, ilk eleman alınır ve geri kalanlar arasında en küçük değerli eleman aranır; eğer bulunursa ilk elemanla yer değiştirilir. Daha sonra kalan n-1 elemandan en küçük olan bulunur ve ikinci elemanla yer değiştirilir. İşlem bu şekilde devam eder. Bu yöntem de (n² – n)/2 sayıda karşılaştırma gerektirir. Kabarcık sıralamaya göre karşılaştırma sayısı aynı olsa bile ortalama yer değiştirme sayısı daha azdır.

T(n) = 2·(n-1) + 2·(n-2) + 2·(n-3) + … + 2·(n-(n-2)) + 2·(n-(n-1))
= 2·((n-1) + (n-2) + (n-3) + … + 2 + 1) (ilk n-1 tamsayının toplamının 2 katı)
= 2·((n-1)·n/2) = n² – n

Dolayısıyla bu algoritmanın karmaşıklığı O(n²)'dir.

### Örnek 2.1: selection sort ile küçükten büyüğe sıralama (C)

```c
#include<stdio.h>
/* selection sort ile diziyi kucukten buyuye dogru siralar */
int main(void)
{
int d[10];
int i,j,n,min,yer;
printf(" dizinin eleman sayisini < 10 giriniz \n");
scanf("%d",&n);
printf(" dizi elemanlarini giriniz \n");
for (i=0;i<n;i++)
   scanf("%d",&d[i]);
for(i=0;i<n-1;i++)
{
   yer=i;
   min=d[i];
     for(j=i+1;j<n;j++)
         if(d[j]<min)
         {
              yer=j;
              min=d[j];
          }
       d[yer]=d[i];
       d[i]=min;
     }
  printf(" sirali dizi \n\n");

for(i=0;i<n;i++)
printf("%4d",d[i]);

return 0;
 }
```

### Örnek 2.2: selection sort (vector şablonu ile)

```cpp
#include <iostream>
#include <vector>
using namespace std;

//--------------------------- selectionSort -----------------------------
//
// Amaç     : Verilen değerlerin, küçükten büyüğe sıraya koymak
//
// Giriş parametresi : Değerlerin yazılı olduğu vektör
//
// Dönüş değeri : void
//
// Fonksiyonda sıralama işlemi, Selection Sort algoritması ile
// gerçeklenmiştir.
//
//-----------------------------------------------------------------------
template <class T>
void selectionSort (vector<T>& dizi)
{
      int minIndex;

       // for her dönüşünde, sıraya sokulmamış elemanlar içerisinden en
       // küçük olanını buluyor ve bu değerin vektör üzerindeki yerini
       // minIndex isimli değişkende saklıyor.
       for (int i = 0; i < dizi.size () - 1; i ++)
       {
             minIndex = i;

              // vektörün sıraya sokulmamış kısmında (i+1'den itibaren),
              // en küçük değerli eleman bulunuyor. Ilk olarak, sıralanmamış
              // kısımdaki ilk elemanın en küçük olduğu varsayılıyor. Bu
              // elemandan itibaren diğer elemanlara bakılıyor. Eğer daha
              // küçük bir değer ile karşılaşılırsa, artık bu elemanın yeri
              // minIndex isimli değişkene atanıyor. Böylece, sıralanmamış
              // kısımdaki en küçük eleman bulunmuş olunuyor.
              for (int j = i + 1; j < dizi.size (); j ++)
                    if (dizi [minIndex] > dizi [j]) minIndex = j;

              // swap işlemi
              // bulunan bu yeni eleman ile sıraya sokulmamış ilk eleman
              // yer değiştiriliyor. Zaten ikisi de aynı eleman ise, bu
              // değişime gerek yoktur.
              if (minIndex != i)
              {
                    T temp = dizi[i];
                    dizi[i] = dizi[minIndex];
                    dizi[minIndex] = temp;
              }
       }
}

//------------------------------ main -----------------------------------

int main ()
{
      vector<int> D;

       // 20 elemanlı, rasgele bir katar oluşturuluyor.
       for (int i = 0; i < 20; i ++) D.push_back (rand () % 10);

       selectionSort (D);

       return 0;
}
```

## Quick sort algoritması

Geliştirilmiş sıralama algoritmalarının en iyisi olarak bilinen bir algoritmadır. Genel işleyişinde karşılaştırma değeri (comparand) adı verilen bir değer seçilir ve sonra dizi ikiye ayrılır. Karşılaştırma değerinden büyük ya da eşit olanlar bir tarafa, küçük olanlar diğer tarafa yerleştirilir. Bu işlem geriye kalan her bölme üzerinde tekrarlanır. Karşılaştırma değeri ya rastgele seçilir ya da dizideki az sayıda elemanın değerinin ortalaması alınır.

Quick sort algoritması için ortalama karşılaştırma sayısı n log n ve ortalama yer değiştirme sayısı n/6 log n olarak verilebilir. Yöntemde dikkat edilmesi gereken husus karşılaştırma değerinin iyi seçilmesidir. Her bölüm için karşılaştırılan değer en büyük değer ise yöntem yavaşlayacaktır. Verilerin yapısına göre uygun bir sıralama algoritmasının seçilmesi isabetli olacaktır. Quick sort algoritması en etkin algoritma olmasına rağmen az sayıda elemana sahip dizilerde tekrarlanan çağrılarından ötürü randımanlı olmayabilir. Bu tip dizilerde (eleman sayısı 100 veya daha az) bubble sort veya selection sort daha iyi sonuç verecektir.

### Örnek 3.1: quick sort ile katar (string) sıralama

```c
#include<iomanip>
/*karakter dizisini quick sort ile siralar */
#include<stdio.h>
#include<string.h>
void quick_str(char dizi[][10],int say);
void qs_string(char dizi[][10],int sol,int sag);
char str[][10]={"tulay","pelin","aysu","can","beril","ogul"};
int main(void)
{

int i;
quick_str(str,sizeof(str));
printf("siralanmis dizi\n");
for (i=0;i<sizeof(str);i++)
printf("%s\n",str[i]);
system("pause");
return 0;

}

void quick_str(char dizi[][10],int say)
{
qs_string(dizi,0,say-1);
}

void qs_string(char dizi[][10],int sol,int sag)
{
int i,j;
char *x;
char yedek[10];
i=sol;j=sag;
x=dizi[(sol+sag)/2];
do {
  while((strcmp(dizi[i],x)< 0) && (i< sag))i++;
  while((strcmp(dizi[j],x)> 0) && (j > sol))j--;
      if(i <= j)
        {
       strcpy( yedek,dizi[i]);
       strcpy( dizi[i],dizi[j]);
       strcpy( dizi[j],yedek);
          i++; j--;
        }
     }while(i <= j);
     if(sol < j) qs_string(dizi,sol,j);
     if(i < sag) qs_string(dizi,i,sag);
}
```

Beklenen sıralı çıktı: aysu, beril, can, ogul, pelin, tulay.

*Not: `sizeof(str)` dizinin eleman sayısını değil bayt cinsinden boyutunu verir (6 × 10 = 60). Hem `quick_str` çağrısında hem de yazdırma döngüsünde eleman sayısı olarak `sizeof(str)/sizeof(str[0])` (yani 6) kullanılmalı; aksi hâlde dizinin dışına taşılır. Ayrıca pivot `x` bir kopya değil, dizideki bir satırı gösteren işaretçi; takaslar sırasında o satırın içeriği değişebildiği için pivotun önce `yedek` gibi ayrı bir diziye kopyalanması daha güvenlidir.*

### Örnek 3.2: quick sort (vector şablonu ile)

```cpp
#include <iostream>
#include <vector>
using namespace std;

//---------------------------- quickSort --------------------------------
//
// Amaç     : Verilen değerleri, küçükten büyüğe doğru sıraya koymak
//
// Giriş parametresi : Değerlerin yazılı olduğu vektör
//
//-----------------------------------------------------------------------

template <class T>
void quickSort (vector<T>& dizi)
{
      quickSort (dizi, 0, dizi.size () - 1);
}

//---------------------------- quickSort --------------------------------
//
// Giriş parametreleri : Değerlerin yazılı olduğu vektör. Bu vektörün
//                       hangi aralığı ile ilgilendiğimizi gösteren
//                       sol ve sag isimli iki değişken. Bu aralık
//                       içerisinden bir pivot seçilip, bu aralık da
//                       iki parçaya bölünecek.
//
//-----------------------------------------------------------------------

template <class T>
void quickSort (vector<T>& dizi, int sol, int sag)
{
      int x = sol;
      int y = sag;
      T pivot = dizi[x]; // Verilen aralığın ilk elemanı pivot olarak seçiliyor

       // Pivottan büyük elemanların sağ tarafa, pivottan küçük
       // elemanların ise sol tarafa alınması sağlanıyor. En sonda
       // ise pivot, oluşan yeni iki gurubun ortasına yerleşecek.
       while (x < y)
       {
             // Sağda pivottan küçük ilk elemanı bul
             while ((dizi[y] >= pivot) && (x < y)) y --;

              // Bu elemanı sola al
              if (x != y)
              {
                    dizi[x] = dizi[y];
                    x ++;
              }

              // Solda pivottan büyük ilk elemanı bul
              while ((dizi[x] <= pivot) && (x < y)) x ++;

              // bu elemanı sağa al
              if (x != y)
              {
                    dizi[y] = dizi[x];
                    y --;
              }
       }

       dizi[x] = pivot; // pivot buraya taşındı

       int pivotIndis = x; // pivotun yeni yeri

       // Pivottan küçük elemanlar [sol,pivotIndis-1] aralığına yerleşti.
       // Pivottan büyük elemanlar [pivotIndis+1,sag] aralığına yerleşti.
       // Her iki aralık değeri için, eğer aralığın boyu birden büyükse,
       // quickSort fonksiyonu özyinelemeli olarak yeniden çağırılıyor

       if (sol + 1 < pivotIndis)
             quickSort (dizi, sol, pivotIndis - 1); // pivotun sol tarafı

       if (sag - 1 > pivotIndis)
             quickSort (dizi, pivotIndis+1, sag); // pivotun sağ tarafı
}

//------------------------------ main -----------------------------------

int main()
{
      vector<int> D;

       // 100 elemanlı, rasgele bir katar oluşturuluyor.
       for (unsigned int i = 0; i < 100 ; i ++) D.push_back (rand ()%10);

       quickSort (D);

       return 0;
}
```

## Shell sort algoritması

Bu sıralama, algoritmayı geliştiren D. L. Shell'in adını almasına karşın, bu isimle anılması işleyiş şeklinin üst üste yığılmış deniz kabuklarına (shell) benzemesindendir. n adet elemanı sıralamak için yöntemin çalışma süresinin n^1.2 ile orantılı olduğu söylenebilir. Bu durumda shell sort algoritmasının n-kare algoritmalarına göre iyileştirilmiş bir algoritma olduğu görülmektedir.

Ders notunda shell sort için kod yok; klasördeki `ShellSort.cpp` diziyi büyükten küçüğe sıralıyor. Aralık (`orta`) önce (n-1)/2 alınıyor ve her turda yarıya indiriliyor; her aralık için o kadar uzaktaki elemanlar karşılaştırılıp gerekirse yer değiştiriliyor.

```c
#include <stdio.h>
/* shell sort algoritmasi ile buyukten kucuge siralama yapar */
int main (void)
{
int a[10],i,j,n,orta,k,yedek;
printf(" dizinin eleman sayisini < 10 giriniz \n");
scanf("%d",&n);
printf("Diziyi  giriniz\n");
for(i=0;i<n;i++)
scanf("%d",&a[i]);
orta=(n-1)/2;
     while(orta >0){
	  for(i=orta+1;i<n;i++){
              j=i-orta;
	      while(j>0){
                k=(j-1)+orta;
	        if(a[j-1]>=a[k]) j=0;
	        else {
		yedek=a[j-1];
		a[j-1]=a[k];
                a[k]=yedek;
                j=j-orta;
	       }
	    }
	 }
    orta=orta/2;
    }
printf("Siralanmis Dizi\n");
for(i=0;i<n;i++)
printf("%3d",a[i]);
scanf("%d",&n);
return 0;
}
```

*Not: Başlangıç aralığı `(n-1)/2` olduğundan n = 2 için aralık 0 olur ve döngü hiç çalışmaz; iki elemanlı dizi sıralanmaz. Başlangıç aralığı `n/2` alınmalı.*

## Arama algoritmaları

Sıralanmamış bir dizide bilgi aramak iki şekilde mümkündür: ya ilk elemandan başlayarak eşiti bulunduğunda sona eren ya da dizinin sonuna gelindiğinde aramayı bitiren bir sıralı arama (sequential search) yapılır. Sıralı bir dizi kullanılıyorsa ikili arama (binary search) algoritması ile daha kısa zamanda sonuç alınabilmektedir.

### Sıralı arama

Eleman sayısı bilinen bir dizide istenilen bilgi bulununcaya kadar arama yapan basit bir algoritmadır.

```c
# include <stdio.h>
# include <stdlib.h>
/* sirali arama yapar */
int sirali_ara (int a[],int n)
{
int sonuc,x,j;
printf("aranacak sayiyi Giriniz:\n");
scanf("%d",&x);
for(j=0;j<n;j++){
if(a[j]==x){
sonuc=j;
break;
}
else sonuc=-1;
}
return(sonuc);
}
int main (void)
{
int n,i,dizi[10],x,bul;
printf("dizinin eleman sayisini giriniz < 10:\n");
scanf("%d",&n);
printf("dizi elemanlarini Giriniz:\n");
for (i=0;i<n;i++)
scanf("%d",&dizi[i]);
bul=sirali_ara(dizi,n);
if(bul==-1)printf(" aranan sayi dizide yer almiyor\n");
else
printf(" aranan sayi dizinin %d . elemanidir",bul);
return 0;
}
```

*Not: Ders notunda iki karşılaştırma `= =` (arada boşlukla) yazılmış; C'de bu derlenmez, `==` olmalı (yukarıda düzeltilmiş hâli var).*

### İkili arama

Bu yöntemde önce sıralı dizide tam ortadaki eleman alınır, aranan sayı ile karşılaştırılır. Aranan sayı ortadaki elemandan büyükse, tekrar ikinci yarının orta elemanı bulunarak karşılaştırma yapılır. İşlem aranan sayı bulununcaya kadar devam eder. İkili aramada en kötü durumda karşılaştırma sayısı log₂n'dir.

```c
#include <stdio.h>
/* binary search algoritmasi ile sirali dizide arama yapar */
int main (void)
{
int a[10],i,bas,son,x,orta,bul,n;
printf(" dizinin eleman sayisini < 10 giriniz \n");
scanf("%d",&n);
printf("Diziyi sirali olarak giriniz\n");
for(i=0;i<n;i++)
scanf("%d",&a[i]);
printf("\n aranacak sayıyı giriniz\n");
scanf("%d",&x);
     bas=0;son=n;
     bul=0;
     while(bas <= son && bul==0){
        orta=(bas+son)/2;
        if(x==a[orta]) bul=1 ;
        else
        if(x>a[orta]) bas=orta+1;
        else
          son=orta-1;
        }
     if(x==a[orta]) printf("aranan sayı%3d dizideki indisi:%3d",x,orta);
     else printf("bulunamadı");
scanf("%d",&x); // ekranı durdurma
return 0;
}
```

*Not: Son indis `son=n` değil `son=n-1` olmalı; aranan sayı dizideki en büyük elemandan büyükse program dizinin dışındaki `a[n]` elemanını okur.*

## Merge (birleştirme) algoritması

Girilen iki sıralı diziyi birleştiren bir algoritmadır.

```c
# include <stdio.h>
/* merge algoritmasi ile iki sirali diziyi birlestirir */
// Not Her iki girilen dizide kendi içinde sıralı olmalıdır...

int main (void)
{
int a[10],b[10],d[20];
int n,m,i,j,l;
printf("ilk dizinin boyutu < 10 ?\n");
scanf("%d",&n);
printf("ikinci dizinin boyutu <10 ?\n");
scanf("%d",&m);
printf(" birinci dizinin elemanlari\n ");
for(i=0;i<n;i++)
scanf("%d",&a[i]);
printf(" ikinci dizinin elemanlari\n ");
for(i=0;i<m;i++)
scanf("%d",&b[i]);
a[n]=b[m-1];
b[m]=a[n-1];
i=0;
j=0;
for(l=0;l<n+m;l++)
   if(a[i]<=b[j]){
      d[l]=a[i];
      i++;
      }
      else
      { d[l]=b[j];
         j++;
      }
printf(" birlestirilmis dizi \n\n" );
for(i=0;i<n+m;i++)
printf("%5d",d[i]);
scanf("%d",&n); // ekranı durdurmak için
return 0; }
```

Program her dizinin sonuna, öbür dizinin son (en büyük) elemanını bir "bekçi" (sentinel) değer olarak koyuyor; böylece dizilerden biri bittiğinde ayrıca sınır kontrolü yapmadan diğerinden okumaya devam ediliyor.

*Not: Bekçi değer, ilk dizi bittiğinde ikinci dizide bekçiye eşit değerler kaldıysa yine seçilip `i` dizinin dışına ilerleyebiliyor; ayrıca boyut olarak 10 girilirse `a[10]`/`b[10]` taşar. Güvenli sürümde döngü `i<n` ve `j<m` koşullarıyla yazılır.*

## Klasördeki ek programlar (STL vector ile)

Aynı haftanın klasöründe ders notundaki programların .cpp dosyalarının yanında, STL vector kullanan birkaç ek program var.

### STL ve vector

`STL.cpp` dosyasının başındaki açıklama:

> STL (Standart Template Library) Standart Şablon Kütüphanesi, verileri işlemek için kullanılan genel bir rutinler kümesidir. Vektör, deque, list konteyner sınıflarıdır.

> Vektörler akıllı diziler olarak düşünülebilir. Vektörler verileri ekler veya çıkartırken vektör boyutunu genişletip daraltarak bellekte yer ayırma işlemini sizin adınıza gerçekleştirirler. Vektör elemanlarına [] operatörü ile erişerek vektörleri dizilere çok benzer şekilde kullanabilirsiniz. Bu tür rastgele erişimler vektörlerle çok hızlıdır. Vektörlerin sonuna (arkasına) yeni elemanlar eklemek de ayrıca hızlıdır. Bu tür bir durum karşısında, yeni veri öğesini tutmak için vektör boyutu otomatik olarak arttırılır.

> D vektörünü tanımlamak için vektörün varsayılan kurucu fonksiyonu (argümansız) kullanılır. Tüm STL konteynerlarda olduğu gibi, konteynerin tutacağı değişken tipini (bu örnekte int tipi) belirtmek için şablon (template) biçimi kullanılır. Konteynerin büyüklüğü açıkça belirtilmez; bu nedenle konteyner 0'dan başlar.

> push_back() üye fonksiyonu aldığı parametreyi vektörün sonuna ekler. Vektörün arkası (sonu) en yüksek indeks numarasına sahip olan elemanın bulunduğu yerdir. Vektörün önü 0 indeks numarasına sahip olduğu yerdir ve yeni eleman eklemek için kullanılmaz.

> Vektör veri içermeye başlar başlamaz, bu veriler tıpkı bir dizi içerisindeymiş gibi, aşırı yüklenmiş [] operatörü yardımıyla okuma ve yazmak için erişilebilir hâle gelir. size() üye fonksiyonu hâlihazırda konteynerde bulunan elemanların sayısını döndürür.

```cpp
#include <iostream>
#include <vector>

using namespace std;

template <typename T>
void foo(vector<T>& dizi)
{
  for(int i=0;i<dizi.size();i++)
    cout<<dizi[i]<<" ";
}

int main()
{
    vector<int> v;
    v.push_back(10);
    v.push_back(112);
    v.push_back(15);
    v.push_back(56);
    v.push_back(17);
    v.push_back(19);
    v.push_back(33);

    foo(v);

    system("pause");
    return 0;
}
```

```
10 112 15 56 17 19 33
```

### Sıralı arama (vector şablonu ile)

`seqSearch`, [ilk, son) aralığında aranan değeri bulursa indisini, bulamazsa `son` değerini döndürüyor.

```cpp
// Sequential Search...
//-----------------------
#include <iostream>
#include <iomanip> // setw fonksiyonu için
#include <vector>

using namespace std;

template <class T>
int seqSearch (vector<T>& dizi,int ilk, int son, int aranan)
{
	int i=ilk;
	while(i != son && dizi[i] != aranan)
	i++;

	return i;
}

//------------------------------ main -----------------------------------

int main ()
{
    vector<int> D;
    int x;

    // 20 elemanlı, rasgele bir katar oluşturuluyor.
	for (int i = 0; i < 10; i ++)
     D.push_back (rand () % 150);

	for(int i=0;i<D.size();i++)
	cout<<setw(4)<<'['<<i<<']'<<setw(5)<<D[i]<<"\n";
	cout<<"Aranacak Deger ? ";
	cin>>x;
	cout<<"Indis No : "<< seqSearch(D,0,D.size(),x)<<endl;
    system("pause");
	return 0;
}
```

Dosyadaki örnek çalışma (rastgele 10 değer; bulamazsa "Indis No : 10" der):

```
   [0]   41
   [1]   17
   [2]   34
   [3]  100
   [4]  119
   [5]  124
   [6]   78
   [7]  108
   [8]  112
   [9]   14
Aranacak Deger ? 119
Indis No : 4
Press any key to continue . . .
```

### İkili arama (vector şablonu ile)

```cpp
// Binary  Search...
// Sıralı dizi içerisinde aranan değeri bulma kodu
#include <iostream>
#include <iomanip> // setw fonksiyonu için
#include <vector>

using namespace std;

template <class T>
int binSearch (vector<T>& dizi,int ilk, int son, int aranan)
{
	int orta; // orta noktanın indeksi
	T ortadeger; // dizi[orta] ye atanacak değer
	int origSon=son; // orjinal son değeri sakla

	while(ilk < son)
	{
    orta=(ilk+son)/2;
	ortadeger=dizi[orta];

	if(aranan==ortadeger)
	   return orta;
    else if ( aranan < ortadeger)
       {
       son=orta; // alt alt listede arama yap
       binSearch (dizi,ilk,son,aranan);
       }
    if ( aranan > ortadeger)
       {
       ilk=orta+1; // üst alt listede arama yap
       binSearch (dizi,ilk,son,aranan);
       }
    }
    return origSon; // aranan bulunamadı...
}

//------------------------------ main -----------------------------------

int main ()
{
    vector<int> D;
    int x;

    // 20 elemanlı, sıralı bir dizi oluşturuluyor.
	for (int i = 0; i < 20; i ++)
     D.push_back (i*10-3);

	for(int i=0;i<D.size();i++)
	cout<<setw(4)<<'['<<i<<']'<<setw(6)<<D[i]<<"\n";
	cout<<"Aranacak Deger ? ";
	cin>>x;
	cout<<"Indis No : "<< binSearch(D,0,D.size(),x)<<endl;
    system("pause");
	return 0;
}
```

Dosyadaki örnek çalışma (bulamazsa "Indis No : 20" der):

```
   [0]    -3
   [1]     7
   [2]    17
   [3]    27
   [4]    37
   [5]    47
   [6]    57
   [7]    67
   [8]    77
   [9]    87
   [10]    97
   [11]   107
   [12]   117
   [13]   127
   [14]   137
   [15]   147
   [16]   157
   [17]   167
   [18]   177
   [19]   187
Aranacak Deger ? 127
Indis No : 13
Press any key to continue . . .
```

*Not: Fonksiyonun içindeki özyinelemeli `binSearch(...)` çağrılarının dönüş değeri kullanılmıyor; sonucu asıl bulan, `ilk` ve `son` güncellendiği için `while` döngüsünün kendisi. Bu çağrılar gereksiz yere aynı aramayı tekrarlıyor.*

### Diğer dosyalar

- `BubbleSortSTL.cpp`: bubble sort'un vector sürümü; sıralamadan önce ve sonra ilk 10 elemanı yazdırıyor.
- `STLSelectionSort.cpp`: selection sort'un vector sürümü; 10'dan 1'e azalan diziyi sıralarken her turun sonunda diziyi yazdırıyor.
- `QuickSortTemplate.cpp`: Örnek 3.2'deki quick sort'un şablonsuz, int dizisiyle yazılmış hâli; rastgele 20 sayıyı sıralayıp yazdırıyor.

*Not: `BubbleSortSTL.cpp`'de vektörü dolduran `for(int i=10;i>0;i++)` döngüsü hiç bitmez (`i--` olmalı). Bu dosyada ve `STLSelectionSort.cpp`'de fonksiyonlar `T` döndüreceğini bildirdiği hâlde `return` yok (`void` olmalı). `QuickSortTemplate.cpp`'de `quickSort(d,0,20)` çağrısı son indis olarak 20 veriyor; 20 elemanlı dizide son indis 19'dur.*
