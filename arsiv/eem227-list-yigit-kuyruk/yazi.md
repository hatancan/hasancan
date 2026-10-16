---
baslik: EEM227 Veri Yapıları: STL list, stack ve queue Örnekleri (Hafta 7–8)
ozet: EEM227 Veri Yapıları dersinin 7. ve 8. haftalarına ait C++ STL programları (Kasım 2007): list ve vector üzerinde iterator ile dolaşma, insert ve erase, stack ve queue fonksiyonlarının açıklamaları, sayıyı queue ile tersten yazdırma ve vector ile kendi kuyruk sınıfını yazma.
---

Bu yazı, Başkent Üniversitesi **EEM227 Veri Yapıları** dersinin 2007 güz döneminde 7. ve 8. hafta klasörlerindeki C++ programlarını bir araya getiriyor. Konu STL'in **list** kabı ve tekrarlayıcıları (iterator), **stack** (yığıt) ve **queue** (kuyruk) uyarlayıcı kapları. Programların çoğunda açıklamalar ve ekran çıktısı yorum olarak yazılmış; burada açıklamalar metne, çıktılar konsol penceresine alındı. Kaynak dosyalar yazının sonunda ZIP olarak indirilebilir.

## Iterator ile list ve vector yazdırma

Listelerde indis operatörü olmadığı için elemanlara iterator ile ulaşılır. Bu program bir int listesini baştan sona (while ve for döngüsüyle), bir double listesini sondan başa ve bir vektörü indis kullanmadan iterator ile yazdırıyor.

```cpp
// iterator kullanarak liste ve vector elemanlarını yazdırma yontemi...
#include <iostream>
#include <iomanip>
#include <list>
#include <vector>

using namespace std;

int main()
{
int a[5]={1,3,5,7,9};
double b[5]={2.2,4.4,6.6,8.8,10.10};

int sizea=sizeof(a)/sizeof(int);
int sizeb=sizeof(b)/sizeof(double);

  list<int> listA(a,a+sizea);   // int listenin değerlerini belirledik.
  list<double> listB(b,b+sizeb);// double listenin değerlerini belirledik.
vector<int> Avector(a,a+sizea); // vectorün değerlerini belirledik.

  list<int>::iterator iterA;    // int liste için iterator tanımladık
  list<double>::iterator iterB; // double liste için iterator tanımladık
vector<int>::iterator Vec_it;   // vectorler içinde iteratorler kullanılabilir !

//-----------------------------------------------------
// int Listeyi başından sonuna doğru listeyi yazdıralım
// listelerde indis ile değere ulaşamadığımız için iterator kullanmak zorunludur
   iterA = listA.begin();
   cout << "int Liste bastan sona dogru   : ";
  while(iterA!=listA.end())
   {
    cout<<*iterA<<" ";
    iterA++;
   }

cout<<"\nfor dongusu ile ayni listeyi tekrar yazdiralim \n";
   for ( iterA = listA.begin(); iterA != listA.end(); iterA ++ ) {
    cout << *iterA << "  ";
  }
//------------------------------------------------------

   cout<<endl<<endl;

//-----------------------------------------------------------------------------
// Liste sonundan başına doğru listeyi eksiksiz yazdıralım...
   iterB = listB.end();
   iterB--;
   cout << "double Liste Sondan basa dogru: ";
   // Listelerde tanımlı olan indis yöntemi olmadığı için begin ve end gibi
   // fonksiyonlarla iteratörümüzü konumlandırıyoruz.
   // end fonksiyonu listenin sonundaki elemandan bir sonraki konumu gösterir,
   // dolayısıyla yazdırmaya başlamadan önce bir kez iteratoru geri çektik...
   while(iterB!=listB.begin())
   {
    cout << * iterB << " ";
    iterB --;
   }
   cout << *iterB; // ilk elemanıda yazdırabilmek için koyduk...
//-----------------------------------------------------------------------------

cout<<endl<<endl;
//--------------------------------------------------------------------
// Bir vektörü indis operatörü olmadan iterator yardımı ile yazdıralım
  Vec_it = Avector.begin();
  cout << "int Vector bastan sona dogru  : " ;
while(Vec_it!=Avector.end())
   {
    cout << *Vec_it << " ";
    Vec_it ++;
   }
//---------------------------------------------------------------------

   cout<<endl<<endl;

system("pause");
return 0;
}
```

```
int Liste bastan sona dogru   : 1 3 5 7 9
for dongusu ile ayni listeyi tekrar yazdiralim
1  3  5  7  9

double Liste Sondan basa dogru: 10.1 8.8 6.6 4.4 2.2

int Vector bastan sona dogru  : 1 3 5 7 9

Press any key to continue . . .
```

## Şablon fonksiyon ve iterator ile liste elemanlarını değiştirme

Şablon fonksiyon kullanarak, iterator yardımı ile liste elemanlarının değerlerini değiştirmeye yönelik bir örnek: `degistir` her elemanı bir arttırıyor.

```cpp
#include <list>
#include <iostream>
#include <iomanip>
using namespace std;

template <typename T>
void yaz(T& Ref)
{
    list<int>::iterator p;
    for (p = Ref.begin ( ); p != Ref.end ( ); p++)
	cout <<setw(5)<< *p ;
	cout<<endl;
}

template <typename T>
void degistir(T& Ref)
{
    list<int>::iterator p;
    for (p = Ref.begin ( ); p != Ref.end ( ); p++)
	(*p)++;
}

int main () {

    list<int>L;
    L.push_back (9);
    L.push_back (7);
    L.push_back (5);
    L.push_back (3);

    cout<<"Orjinal Liste : ";
    yaz(L);
    degistir(L);
    cout<<"Degismis Liste: ";
    yaz(L);
    system("pause");
    return 0;
}
```

```
Orjinal Liste :     9    7    5    3
Degismis Liste:    10    8    6    4
Press any key to continue . . .
```

## insert ve erase işlemleri

Bu program bir liste oluşturduktan sonra, bu listeye istenilen konuma eleman ekleme işlemi ve istenilen konumdaki elemanı silme işlemi yapar. İndis operatörü olmadığından dolayı liste elemanları üzerinde dolanırken iteratorlerden faydalanılır. Listenin fonksiyonları olan `insert()` ve `erase()` fonksiyonları parametre olarak işlem yapılacak liste üzerinde tanımlanmış bir iteratoru almalıdır.

```cpp
#include <list>
#include <iostream>
#include <iomanip>
using namespace std;

template <typename T>
void yaz(T& Ref)
{
    list<int>::iterator p;
    for (p = Ref.begin ( ); p != Ref.end ( ); p++)
	cout <<setw(5)<< *p ;
	cout<<endl;
}

int main () {

    list<int>L;
    L.push_back (10);
    L.push_front (20);
    L.push_back (40);
    L.push_back (5);
    L.push_front (15);
    L.push_front (50);

    cout<<"Orjinal Liste: "<<endl;
    yaz(L);

list<int>::iterator iter1,iter2;
    iter1 = L.begin(); // iterator listenin ilk elemanını gösterir
    iter1 ++; // iterator bir sonraki elemanı işaret etmektedir.

    cout<<"3 eklenmeden once iteratorun gosterdigi deger : "<<*iter1<<endl;
    L.insert(iter1,3); // insert işlemi iteratorun gösterdiği yerden önceki
                       // konuma yapılır !!! Listenin boyu 1 artar
                       // ekleme noktasının sağında kalan değerler 1 sağa shift
                       // ettirilir..

   cout<<"Eklendikten sonra iteratorun gosterdigi deger : "<<*iter1<<endl<<endl;
                    // ekleme işlemi yapıldıktan sonra iteratörün gösterdiği
                       // değer değişmez !!! iteratorde 1 kez sola kaymıştır.

    cout<<"3 eklendikten sonra Listenin durumu: "<<endl;
    yaz(L);

    iter2 = L.end(); // listenin en son elemanından sonraki konuma konuşlanır.
    iter2-- ; // iteratoru listenin en son elemanı olacak şekilde 1 kez çektik.
    iter2-- ; // iteratoru sondan 1 önceki elemana çeker.
    cout<<"Silmeden once iteratorun gosterdigi deger : "<<*iter2<<endl;

    L.erase(iter2); // ve iteratorun gösterdiği eleman silinir.
    cout<<"Sildikten sonra iteratorun gosterdigi deger : "<<*iter2<<endl<<endl;
    // silme işleminden sonra itertorun gosterdiği değer listeden çıkartılır,
    // fakat o iterator silinen elemanı hala göstermektedir...

    cout<<"Silme isleminden sonra Listenin durumu: "<<endl;
    yaz(L);

    system("pause");
    return 0;
}
```

```
Orjinal Liste:
   50   15   20   10   40    5
3 eklenmeden once iteratorun gosterdigi deger : 15
Eklendikten sonra iteratorun gosterdigi deger : 15

3 eklendikten sonra Listenin durumu:
   50    3   15   20   10   40    5
Silmeden once iteratorun gosterdigi deger : 40
Sildikten sonra iteratorun gosterdigi deger : 40

Silme isleminden sonra Listenin durumu:
   50    3   15   20   10    5
Press any key to continue . . .
```

*Not: `erase` ile silinen elemanı gösteren iterator geçersiz (invalid) olur; programdaki gibi `*iter2` ile okunması tanımsız davranıştır. Çıktıda 40 görünmesi o derleyicide belleğin henüz üzerine yazılmamasından kaynaklanıyor. Doğru kullanım `iter2 = L.erase(iter2);` ile silinen elemandan sonraki konumu almaktır.*

## stack (yığıt)

### stack fonksiyonları

Dosyanın başındaki açıklamalar:

- `void pop();` Yığıtın en üstündeki elemanı yığıttan çıkartır. Ön koşul (precondition): stack boş olmamalı. Son durum (postcondition): stack boş olabilir (tek eleman varsa), stack'in en üstündeki eleman değişir, stack'teki eleman sayısı 1 azalır.
- `void push( const T & item);` Parametre olarak verilen değeri stack'in en üstüne ekler. Son durum: stack'in tepesinde yeni bir eleman olur.
- `T& top();` En üstteki elemana referans olacak değer döndürür. Ön koşul: stack boş olmamalıdır.
- `const T& top() const;` Diğerinin const versiyonudur.
- `bool empty() const;` Stack boş ise true döndürür.
- `int size() const;` Stack'te bulunan eleman sayısını döndürür.

```cpp
#include <iostream>
#include <stack>

using namespace std;

int main()
{

stack<int> s;

s.push(1);
s.push(2);
s.push(3);

cout<< s.top()<<endl;
s.pop();
cout<< s.top()<<endl;
s.pop();
cout<< s.top()<<endl;
s.pop();

   if(s.empty()==1)
     cout<<"Stack bos !!"<<endl;
   else
     cout<<"Dolu"<<endl;

system("pause");
return 0;
}
```

```
3
2
1
Stack bos !!
```

### while döngüsüyle 10 elemanlı yığıt

```cpp
// Stack için STL Classı

#include <iomanip>
#include <iostream>
#include <stack>

#define boy 10

using namespace std;

int main()
{
stack<int> yigin;

/*
stack<int> sayi[10]; //ismi sayi olan 5 adet birbirinden farkli stack oluşturur

Pointer array mantığı gibi düşün !!
*/

for(int i=0;i<boy;i++)
yigin.push(i);
cout<<"Yigin boyu: "<<yigin.size()<<endl;

while(!yigin.empty())
{
  cout<<yigin.top()<<" ";
  yigin.pop();
}

cout<<endl;
system("pause");
return 0;
}
```

```
Yigin boyu: 10
9 8 7 6 5 4 3 2 1 0
Press any key to continue . . .
```

Son giren ilk çıktığı için (LIFO) sayılar girildikleri sıranın tersinde yazdırılıyor.

*Not: Yorumdaki `stack<int> sayi[10];` tanımı 5 değil, 10 adet ayrı stack oluşturur.*

## queue (kuyruk)

Kuyruk fonksiyonları (dosyadaki açıklamalardan):

- `bool empty() const;` Kuyruk boş ise true, değilse false.
- `T& front();` Kuyruğun en önündeki elemana referans döndürür. Ön koşul: kuyruk boş olmamalı.
- `const T& front() const;` front() fonksiyonunun sabit olanıdır.
- `void pop();` Kuyruğun en önünden eleman siler. Ön koşul: kuyruk boş olmamalı.
- `void push(const T & item);` item isimli argümanı kuyruğun en sonuna ekler. Son durum: kuyruğun en sonunda yeni bir eleman oluşur.
- `int size() const;` Kuyruktaki eleman sayısını döndürür.

```cpp
// Queue için STL Classı

#include <iomanip>
#include <iostream>
#include <queue>

#define boy 10

using namespace std;

int main()
{
queue<int> kuyruk;

for(int i=0;i<boy;i++)
kuyruk.push(i); // Önce 0 eklenir sonra arkasına 1 sonra arkasına 2 ...

cout<<"kuyruk boyu: "<<kuyruk.size()<<endl;

while(!kuyruk.empty())
{
  cout<<kuyruk.front()<<" ";
  kuyruk.pop();
}

cout<<endl;
system("pause");
return 0;
}
```

```
kuyruk boyu: 10
0 1 2 3 4 5 6 7 8 9
Press any key to continue . . .
```

Kuyrukta ilk giren ilk çıktığı için (FIFO) sayılar girildikleri sırayla yazdırılıyor.

## Soru: sayıyı queue ile tersten yazdırma (Hafta 8)

> Klavyeden girilen N basamaklı bir sayıyı tersten yazdırabilen bir programı queue veri yapısı kullanarak kodlayınız.

Sayının basamakları 10'a göre mod alınarak sondan başa doğru ayrılıp kuyruğa ekleniyor; kuyruk FIFO olduğu için basamaklar ayrıldıkları sırayla, yani sayının tersi olarak yazdırılıyor.

```cpp
#include <queue>
#include <iostream>
using namespace std;

int main()
{
int sayi,bas=0;
queue<int> Bque;
cout<<"Max. 10 basamakli bir sayi giriniz : ";
cin>>sayi;
do{
          if(sayi!=0)
          {
           bas=sayi%10;
           sayi/=10;
           Bque.push(bas);
          }
          else
           break;
  }while((sayi!=0));

cout<<"Tersten Sayi : ";
while(!Bque.empty())
{
 cout<<Bque.front();
 Bque.pop();
}
cout<<endl;
system("pause");
return 0;
}
```

Örneğin 12345 girilirse kuyruğa sırasıyla 5, 4, 3, 2, 1 eklenir ve ekrana "Tersten Sayi : 54321" yazılır.

*Not: `int` en fazla 2147483647 değerini tutabildiği için 10 basamaklı sayıların bir kısmı (2147483647'den büyük olanlar) taşar; "Max. 10 basamaklı" sınırı için `long long` gerekir.*

## Soru: vector ile kendi kuyruk yapısını oluşturma (Hafta 8)

> Vector veri yapısını kullanarak, kendi Queue yapınızı oluşturun.

```cpp
#include <iostream>
#include <vector>
using namespace std;

template <typename T>
class MyQueue
{
      vector<T> data;
   public:
     void Add(T const &);
     void Remove();
     void Print();
};

template <typename T>
void MyQueue<T> ::Add(T const &d)
{
     data.push_back(d);
}

template <typename T>
void MyQueue<T>::Remove()
{
     data.erase(data.begin( ) + 0,data.begin( ) + 1); //en başdan 1.elemanı sil
}

template <typename T>
void MyQueue<T>::Print()
{
     vector <int>::iterator It1;
     It1 = data.begin();
     for ( It1 = data.begin( ) ; It1 != data.end( ) ; It1++ )
        cout << " " << *It1<<endl;
}

int main()
{
     MyQueue<int> q;
     q.Add(1);
     q.Add(24);
     q.Add(32);
     q.Add(11);
     q.Add(72);
     q.Add(3);

     cout<<"Veriler (Silmeden Once)"<<endl;
     q.Print();

     q.Remove();
     cout<<"Veriler (Sildikten Sonra)"<<endl;
     q.Print();
system("pause");
return 0;
}
```

Kodu izleyerek beklenen çıktı:

```
Veriler (Silmeden Once)
 1
 24
 32
 11
 72
 3
Veriler (Sildikten Sonra)
 24
 32
 11
 72
 3
```

Ekleme vektörün sonuna (`push_back`), silme baştan (`erase` ile ilk eleman) yapıldığı için yapı bir kuyruk gibi davranıyor.

*Not: `Print` fonksiyonunda iterator `vector<T>::iterator` yerine `vector<int>::iterator` olarak tanımlanmış; sınıf bu hâliyle yalnızca `MyQueue<int>` için derlenir.*
