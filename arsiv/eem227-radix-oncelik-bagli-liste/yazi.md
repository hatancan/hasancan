---
baslik: EEM227 Veri Yapıları: Radix Sort, Öncelikli Kuyruk ve Bağlı Liste Düğümleri (Hafta 10–11)
ozet: EEM227 Veri Yapıları dersinin 10. ve 11. haftalarına ait C++ programları (Kasım–Aralık 2007): queue dizisiyle radix sort, priority_queue ile normal queue farkı ve priority_queue ile sıralama, node şablon sınıfıyla başa ve sona ekleyerek bağlı liste oluşturma soruları.
---

Bu yazı, Başkent Üniversitesi **EEM227 Veri Yapıları** dersinin 2007 güz döneminde 10. ve 11. haftalara ait klasördeki ("227_10_11") C++ programlarını içeriyor. Üç konu var: kuyruklarla çalışan **radix sort** (tabana göre sıralama), STL **priority_queue** (öncelikli kuyruk) ve `node` şablon sınıfıyla **bağlı liste** (linked list) oluşturma soruları. Programların başındaki açıklamalar ve sonundaki ekran çıktıları kaynak dosyalardan alındı. Kaynak dosyalar yazının sonunda ZIP olarak indirilebilir.

## Radix sort (tabana göre sıralama)

Dosyanın başındaki açıklama:

- d basamaklı sayılar için çalışma zamanı O(2·d·n) = O(n) kadardır.
- Lineer bir algoritmadır.
- Sayıları karşılaştırarak sıralama işlemi yapmadığı için hızlı çalışır.

Her turda sayılar, o turdaki basamaklarına (önce birler, sonra onlar...) göre 0–9 numaralı 10 kuyruğa dağıtılıyor (`distribute`), sonra kuyruklar sırayla boşaltılarak vektöre geri toplanıyor (`collect`). Kuyruklar FIFO olduğu için bir önceki turun sırası korunuyor; d tur sonunda vektör sıralanmış oluyor.

```cpp
#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <time.h>
using namespace std;

void distribute(const vector<int>& v, queue<int> digitQueue[],int power)
{
	int i;
	for (i = 0; i < v.size(); i++)
		digitQueue[(v[i] / power) % 10].push(v[i]);
}

void collect(queue<int> digitQueue[], vector<int>& v)
{
	int i = 0, digit;
	for (digit = 0; digit < 10; digit++)

		while (!digitQueue[digit].empty())
		{
			v[i] = digitQueue[digit].front();
			digitQueue[digit].pop();
			i++;
		}
}

void radixSort(vector<int>& v, int d)
{
	int i;
	int power = 1;
	queue<int> digitQueue[10]; // 10 adet  queue yaratıldı

	for (i=0;i < d;i++)
	{
		distribute(v, digitQueue, power);
		collect(digitQueue, v);
		power *= 10;
	}
}

void displayVector(const vector<int>& v)
{
	int i;

	for (i=0; i < v.size(); i++)
	{
		cout << setw(12) << v[i];
		if ((i+1) % 6 == 0)		// newline every 6 numbers
			cout << endl;
	}
	cout << endl;
}

int main()
{
	vector<int> intVector;

	srand(time(NULL));
	int bnumber=2; // sağdan kaç basamağa göre sıralama yapılacak
	int i;
	for (i = 0; i < 20; i++)
		intVector.push_back(rand()%100);
	cout<<"SIRALAMADAN ONCE VEKTORUN ICINDEKI BILGI \n";
    displayVector(intVector);

    cout<<"SIRALANDIKTAN SONRA VECTORUN ICINDEKI BILGI \n";
	radixSort(intVector, bnumber);
	displayVector(intVector);
	system("pause");
	return 0;
}
```

Dosyadaki örnek çalışma:

```
SIRALAMADAN ONCE VEKTORUN ICINDEKI BILGI
          13          68          47          48          72          48
          64          91          32          56          28          75
          23          75          31          61          60          80
          66          69
SIRALANDIKTAN SONRA VECTORUN ICINDEKI BILGI
          13          23          28          31          32          47
          48          48          56          60          61          64
          66          68          69          72          75          75
          80          91
Press any key to continue . . .
```

*Not: Dosyanın başındaki açıklamada "3 basamağa kadar olan 20 adet random sayı" yazıyor; program ise `rand()%100` ile en fazla 2 basamaklı sayılar üretip 2 tur (`bnumber=2`) sıralıyor. 3 basamaklı sayılar için `rand()%1000` ve `bnumber=3` kullanılmalı.*

## Öncelikli kuyruk (priority queue)

Dosyadaki açıklama: Yüksek öncelikli olanlar priority queue'nun en üstünde bulunur, yani işleme en önce girecek değerler bunlardır. Dolayısıyla kuyruğa push edilen değerleri push edilme sırasına göre değil, önceliğine göre kuyruktan çıkarır (`top()`). Normal kuyrukta bulunan FIFO kuralı priority queue'da geçerli değildir.

```cpp
#include <queue>
#include <iomanip>
#include <iostream>
#include <vector>
using namespace std;
int main()
{

// ÖNCELİKLİ KUYRUK
// FIFO olarak ÇALIŞMAZ !!!
priority_queue<int> pq;
pq.push(10);
pq.push(30); // ---> En yüksek prioritye sahip olan değer bu !!! En üsttedir
pq.push(5);
pq.push(3);
cout<<"PRIORITY QUEUE"<<endl;
cout<<"Size : "<<pq.size()<<endl<<"Yuksek Oncelikli Olan : "<<pq.top()<<endl;

// NORMAL KUYRUK
//---------------
// Dikkat normal queue nun top fonksiyonu yoktur !!! front() fonksiyonu vardır.
queue<int> s;
s.push(10); // ----> ilk giren bu First In, İlk çıkacak da bu !
s.push(30);
s.push(5);
s.push(3);

int x=s.front();
cout<<endl<<"NORMAL QUEUE"<<endl;
cout<<"Size : "<<s.size()<<endl<<"FIFO dan dolayi kuyruktan cikan : "<<x<<endl;

system("pause");
return 0;
}
```

```
PRIORITY QUEUE
Size : 4
Yuksek Oncelikli Olan : 30

NORMAL QUEUE
Size : 4
FIFO dan dolayi kuyruktan cikan : 10
```

### priority_queue ile sıralama

Priority queue içerisine aktarım işlemi zaten önceliğe, yani büyüklüğe göre sıralı bir şekilde otomatik olarak yapıldığı için ekstradan bir karşılaştırma işlemi yapmamıza gerek yoktur. Elemanlar kuyruğa atılıp her seferinde en büyüğü (`top()`) alınarak vektörün sonundan başına doğru yerleştiriliyor; böylece vektör küçükten büyüğe sıralanıyor. Döngü baştan sona kurulursa büyükten küçüğe sıralanır.

```cpp
#include <queue>
#include <iomanip>
#include <iostream>
#include <vector>
using namespace std;

int main()
{
priority_queue<int> pq;
//int arr[]={16,29,14,32,18,14,87,50,64,35};
int arr[]={1,1,10,9,8,7,6,5,4,3,2,1};
int arrsize=sizeof(arr)/sizeof(int);
vector<int> v(arr,arr+arrsize);

int i, n=v.size();

cout<<"Vektor ilk Hali (Sirasiz): ";
  	for(i = 0; i < n; i++)
		cout << v[i] << "  ";
 	cout << endl;

// Sıralayan kısım-----------
for(int i=0 ; i<n ; i++)

  pq.push(v[i]);

for(int i=n-1 ; i>=0 ; i--) // Küçükten büyüğe sıralar
//for(int i=0 ; i<n ; i++)  // Büyükten küçüğe sıralar
{
 v[i] = pq.top();
 pq.pop();
} // Sıralama bitti------------

cout<<"Vektor Son hali (Sirali) : ";
 	for(i = 0; i < n; i++)
		cout << v[i] << "  ";
 	cout << endl;

system("pause");
return 0;
}
```

```
Vektor ilk Hali (Sirasiz): 1  1  10  9  8  7  6  5  4  3  2  1
Vektor Son hali (Sirali) : 1  1  1  2  3  4  5  6  7  8  9  10
```

## Bağlı liste (linked list) soruları

Bu sorularda aynı `node` şablon sınıfı kullanılıyor: her düğüm bir değer (`nodeValue`) ve sonraki düğümü gösteren bir işaretçi (`next`) tutuyor. Listeyi yazdıran `printList` fonksiyonu static tanımlanmış; böylece sınıftan türemiş bir nesne olmadan `node<int>::printList(...)` şeklinde, kapsam çözünürlük operatörüyle çağrılabiliyor. Düğümler arasına ok koymak için son düğüm döngüden sonra ayrıca yazdırılıyor.

### Soru 1: bağlı liste oluşturun

Düğümler listenin başına eklenerek oluşturuluyor: her yeni düğümün `next`'i bir önceki düğümü gösteriyor.

```cpp
#include<iostream>
using namespace std;

template <typename T>
class node
{

  private:
      T nodeValue;      // data held by the node
      node<T> *next,*curr;    // next node in the list

   public:
      node(const T& item, node<T> *nextNode=NULL)
      {
         nodeValue=item;
		 next=nextNode;
	  }

/*
 fonksiyona Class dan türemiş nesne olmadan erişmek için fonksiyonu static
tanımladık */
static void printList(node<T> *ptr)
      {
        while (ptr->next != NULL) // Araya ok koymak için bu şekilde yaptık...
        {
         cout << ptr->nodeValue<<" -> " ;
         ptr = ptr->next;
        }
         cout<<ptr->nodeValue<<" -> NULL" ;
           cout << endl;
       }

};

int main()
{
// Listenin başına ekleyen yapı...

 node<int> *p = new node<int>(10);
 node<int> *q = new node<int>(20,p);
 node<int> *r = new node<int>(30,q);

// nesne kullanmadan scope resolution ile fonksiyona eriştik
 node<int>::printList(r);

 system("pause");
 return 0;
}
```

```
30 -> 20 -> 10 -> NULL
Press any key to continue . . .
```

### Soru 2: 10 rastgele float sayıdan bağlı liste (başa ekleme)

> 10 adet random float sayıdan oluşan bir link list oluşturun, ekranda listeleyin. Listeyi oluştururken elemanları başa ekle yöntemini kullanarak LL'e ekleyin.

Klasörde bu sorunun iki sürümü var. İlk sürümde (`LL_STL_2_10RandomFloat.cpp`) liste doğrudan `P` işaretçisi üzerinde kuruluyor; düzeltilmiş sürümde (`LL_STL_2_50Random.cpp`) listenin başı `NULL` ile başlatılan bir `head` işaretçisinde tutuluyor. Sınıf iki sürümde de aynı (Soru 1'deki `node` sınıfının `curr` alanı olmayan hâli, `printList` burada `static T` olarak bildirilmiş).

İlk sürümün `main` fonksiyonu:

```cpp
int main()
{

node<float> *P;

for(int i=0 ; i<10 ; i++)
 P = new node<float> (15.0/(rand()%40*1.0),P);

// nesne kullanmadan scope resolution ile static fonksiyona eriştik...
 node<float>::printList(P);

 system("pause");
 return 0;
}
```

Düzeltilmiş sürüm:

```cpp
int main()
{

node<float> *P,*head=NULL;

for(int i=0 ; i<10 ; i++)
{
  P = new node<float> (15.0/(rand()%40*1.0),head);
  head = P;
}
// nesne kullanmadan scope resolution ile static fonksiyona eriştik...
 node<float>::printList(head);

 system("pause");
 return 0;
}
```

```
0.625->7.5->0.394737->0.394737->3.75->1.66667->0.75->1.07143->0.555556->15->NULL
Press any key to continue . . .
```

Başa ekleme yapıldığı için ilk üretilen sayı (15) listenin sonunda görünüyor.

*Not: İlk sürümde `P` ilk değer verilmeden kullanıldığı için listenin ilk eklenen düğümünün `next`'i rastgele bir adresi gösterir; `printList` listenin sonunu bulamaz. Ayrıca `rand()%40` sıfır çıkarsa 15.0/0 ile sonsuz (inf) değer oluşur. Her iki dosyada `printList` `T` döndüreceğini bildirdiği hâlde `return` içermiyor (`void` olmalı).*

### Soru: 10 rastgele karakterden bağlı liste

> 10 elemanlık rastgele karakter değerlerinden oluşmuş LL oluşturun. Sona ekle yöntemi ile yapınız.

```cpp
int main()
{

node<char> *P,*head=NULL;

srand(time(NULL));
for(int i=1 ; i<10 ; i++)
{
 P = new node<char> (65+rand()%26,head);
 head = P;
}

// nesne kullanmadan scope resolution ile static fonksiyona eriştik...
 node<char>::printList(head);

 system("pause");
 return 0;
}
```

`65+rand()%26` ifadesi 'A' ile 'Z' arasında rastgele bir büyük harf üretir. Dosyadaki örnek çıktı:

```
Q->Q->J->H->T->S->U->A->U->NULL
Press any key to continue . . .
```

*Not: Döngü `i=1`'den `i<10`'a kadar döndüğü için 10 değil 9 düğüm oluşuyor (örnek çıktıda da 9 harf var). Ayrıca soruda sona ekleme isteniyor, ama kod her yeni düğümü `head`'in önüne, yani başa ekliyor.*

### Soru 4: tam sayılardan sona ekleyerek liste (fonksiyonsuz)

> Tam sayılardan oluşan 10 elemanlık bir listeyi sona ekleyerek oluşturun.

Bu sürümde `node` sınıfının üyeleri public yapılmış; böylece `main` içinde `next` alanına doğrudan erişilerek listenin sonu bulunuyor ve yeni düğüm oraya bağlanıyor.

```cpp
#include<iostream>
#include<ctime>
using namespace std;

template <typename T>
class node
{
   public:

      T nodeValue;      // data held by the node
      node<T> *next;    // next node in the list

      node(const T& item, node<T> *nextNode=NULL)
      {
         nodeValue=item;
		 next=nextNode;
	  }

/*
 fonksiyona Class dan türemiş nesne olmadan erişmek için fonksiyonu static
tanımladık */
static T printList(node<T> *ptr)
      {

        while (ptr->next != NULL) // Araya ok koymak için bu şekilde yaptık...
        {
         cout << ptr->nodeValue<<"->" ;
         ptr = ptr->next;
        }
         cout<<ptr->nodeValue<<"->NULL" ;
           cout << endl;

       }

};

int main()
{

node<int> *head=NULL,*curr;

srand(time(NULL));

for(int i=1 ; i<=10 ; i++)
{

 if(head == NULL)
   head = new node<int> (i);

 else
 {
 curr = head;

 while(curr->next!=NULL)
   curr = curr->next;

 curr->next = new node<int> (i); ;
 }
}

// nesne kullanmadan scope resolution ile static fonksiyona eriştik...
 node<int>::printList(head);

 system("pause");
 return 0;
}
```

```
1->2->3->4->5->6->7->8->9->10->NULL
Press any key to continue . . .
```
