---
baslik: EEM227 Veri Yapıları: Bağlı Listeye Sıralı Ekleme ve Bağlı Liste ile Kuyruk (Hafta 12)
ozet: EEM227 Veri Yapıları dersinin 12. haftasına ait C++ programları (Aralık 2007): tek yönlü bağlı listeye küçükten büyüğe sıralı ekleme ve listeden silme, bağlı liste (linked list) kullanarak queue veri yapısı oluşturan linkedQueue şablon sınıfı.
---

Bu yazı, Başkent Üniversitesi **EEM227 Veri Yapıları** dersinin 2007 güz dönemi 12. hafta klasöründeki iki C++ programını içeriyor: tek yönlü bağlı listeye **sıralı ekleme** (Soru 5) ve bağlı liste kullanarak **kuyruk (queue)** yapısı oluşturma. Kaynak dosyalar yazının sonunda ZIP olarak indirilebilir.

## Soru 5: sıralı ekleme

> `int x[10]={89,17,88,45,26,30,4,25,72,1};` küçükten büyüğe doğru sıralı ekleme!

Dosyanın başında, bu on sayı sırayla girildiğinde listenin her adımda aldığı hâl verilmiş:

```
89->NULL
17->89->NULL
17->88->89->NULL
17->45->88->89->NULL
17->26->45->88->89->NULL
17->26->30->45->88->89->NULL
4->17->26->30->45->88->89->NULL
4->17->25->26->30->45->88->89->NULL
4->17->25->26->30->45->72->88->89->NULL
1->4->17->25->26->30->45->72->88->89->NULL
Press any key to continue . . .
```

`LLSiraliEkle` fonksiyonu dört durumu ayırıyor:

- Liste boşsa ilk düğüm head'e yerleştirilir.
- Yeni değer head'deki değerden küçük ya da eşitse başa (sola) eklenir.
- Liste dolaşılarak yeni değerden büyük ilk düğüm aranır; listenin sonuna gelinmiş ve son değer de küçük ya da eşitse sona eklenir.
- Aksi hâlde yeni düğüm, önceki düğüm (`pre`) ile bulunan düğüm (`curr`) arasına eklenir.

`ListedenSil` ise silinecek değeri arayıp, head'de ise head'i bir ileri kaydırarak, başka bir yerdeyse önceki düğümü sonrakine bağlayarak düğümü siliyor. Fonksiyonlar `head` işaretçisini değiştirebilmek için onu referans olarak (`node<T> * &ptr`) alıyor.

```cpp
#include<iostream>
#include<ctime>
using namespace std;

template <typename T>
class node
{
private:
      T nodeValue;      // data held by the node
      node<T> *next;    // next node in the list
public:

 node(const T& item, node<T> *nextNode=NULL)
      {
         nodeValue=item;
		 next=nextNode;
	  }

static T LLSiraliEkle(T value,node<T> * &ptr)
{

node<T> *curr=ptr,*pre=ptr,*s;

 if( ptr == NULL) // Liste boş ise ilk nodu heade yerleştir.
      {
       ptr = new node<T> (value);
       ptr->next = NULL;
      }

 else if (ptr->nodeValue >= value) // Başa ekle (sola)
     {
       s = new node<T> (value);
       s->next = ptr;
       ptr = s;
     }

else
 {
  while (curr->nodeValue <= value && curr->next!=NULL)
    {
      pre = curr;
      curr = curr->next;
     }

   if(curr->next == NULL && curr->nodeValue <= value) // sona ekle
       {
         s = new node<T> (value);
         s->next = NULL;
         curr->next = s;
       }

   else  // araya ekle
         {
          s = new node<T> (value);
          pre->next = s;
          s->next = curr;
         }

 } // ELSE
}

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

static T node<T>::ListedenSil(node<T>* &ptr, T deger)
  {
  node<T> * curr, * pre;
   pre = curr = ptr;

    while(curr->nodeValue != deger && curr->next!=NULL)
     {
        pre = curr;
       curr = curr->next;
     }

   if(curr == ptr) // Silinecek değer head de bulunduysa
   {
    ptr = ptr -> next; // head i ötele
    delete curr;
   }

   else if(curr->nodeValue == deger) // head dışında bir yerde ise
    {  pre->next = curr->next;
       delete curr;
       cout<<"Silme islemi basarili"<<endl;
    }
    else
       cout<<"Silinecek deger listede bulunamadi"<<endl;
  }

};

int main()
{
//  int x[]={89,17,88,45,26,30,4,25,72,1};
  int SilinecekDeger;
  int adet,deger;

 node<int> *head=NULL;

 srand(time(NULL));
 cout<<"Kac eleman listeye eklenecek ? ";
 cin>>adet;

 for(int i=0; i<adet; i++)
 {
    cout<<"Listeye eklenecek degeri giriniz: ";
    cin>>deger;
    node<int>::LLSiraliEkle(deger,head);
    node<int>::printList(head);
 }

 cout<<"\n Silinecek Degeri Giriniz : ";
 cin>>SilinecekDeger;

 if( node<int>::ListedenSil(head,SilinecekDeger) )
     node<int>::printList(head);
 else
    cout<<" Silinecek deger listede bulunamadı !\n";

  system("pause");
  return 0;
}
```

*Not: `ListedenSil`, `LLSiraliEkle` ve `printList` `T` döndüreceklerini bildirdikleri hâlde `return` içermiyor; `main`'de `if( node<int>::ListedenSil(...) )` ile kullanılan dönüş değeri bu yüzden tanımsız (silme sonrası liste yazdırılıp yazdırılmayacağı rastlantıya kalır). Silme başarılıysa true, değilse false döndüren bir `bool` fonksiyon olmalı. Ayrıca sınıf gövdesi içinde `static T node<T>::ListedenSil` yazımındaki `node<T>::` niteleyicisi fazladır; güncel derleyiciler bunu hata sayar. Listede tek eleman varken o eleman silinirse head `NULL` olur ve ardından çağrılan `printList` boş listede çöker.*

## Soru: bağlı liste ile kuyruk

> LL veri yapısı kullanarak, queue veri yapısı oluşturun.

Çözüm, kuyruğun önünü (`qfront`) ve arkasını (`qback`) gösteren iki işaretçi ile eleman sayısını (`qsize`) tutan bir `linkedQueue` şablon sınıfı. `push` yeni düğümü listenin sonuna bağlayıp `qback`'i güncelliyor; `pop` baştaki düğümü silip `qfront`'u bir ileri alıyor. Kopyalama kurucusu, atama operatörü ve yıkıcı, yardımcı `copy()` ve `clear()` fonksiyonlarıyla yazılmış. Sınıftaki İngilizce yorumlar, dersin kaynak kitabındaki bağlı liste kuyruk sınıfının yorumları; hata durumlarında istisna (exception) fırlatmak yerine ekrana mesaj yazdırılacak şekilde uyarlanmış.

```cpp
#include <iostream>

using namespace std;

template <typename T>
class node
{
   public:
      T nodeValue;      // data held by the node
      node<T> *next;    // next node in the list

      // default constructor with no initial value
      node() : next(NULL)
      {}

      // constructor. initialize nodeValue and next
      node(const T& item, node<T> *nextNode = NULL) :
			  nodeValue(item), next(nextNode)
      {}
};

template <typename T>
class linkedQueue
{
    public:
		linkedQueue();
			// Constructor: creates an empty queue.
			// Postcondition: qsize = 0, qfront = qback = NULL

		linkedQueue(const linkedQueue<T>& obj);
			// copy constructor. builds a copy of obj

		~linkedQueue();
			// destructor. clear the linked list

		linkedQueue<T>& operator= (const linkedQueue<T>& rhs);

		void push(const T& item);
			// insert an element at the rear of the queue
			// Postcondition: the queue has one more element

		void pop();
			// remove an element from the front of the queue.
			// Precondition: the queue is not empty. if the queue
			// is empty, throw an underflowError exception
			// Postcondition: the queue has one less element

		T& front();
			// return a reference to the front of the queue.
			// Precondition: the queue is not empty. if the queue
			// is empty, throw an underflowError exception
		const T& front() const;
			// constant version

      int size() const;
			// return the current size of the queue

		bool empty() const;
			// return true if the queue is empty; otherwise return false

    private:
		node<T> *qfront, *qback;
			// the linked list with qfront stores the elements.
			// qback points to the rear of the queue
		int qsize;
			// number of elements in the queue

		void copy(const linkedQueue<T>& q);
			// copy q so the current list is identical to q

		void clear();
			// clear the list. used by the destructor and assignment

		node<T> *getNode(const T& item);
			// allocate a node with value item and pointer value NULL
			// and return a pointer to it. if memory allocation fails,
			// throw the memoryAllocationError exception
};

template <typename T>
void linkedQueue<T>::copy(const linkedQueue<T>& q)
{
	// qback moves through the list we are building and
	// winds up at the rear of our new list. p
	// moves through the list we are copying
	node<T> *newNode, *p = q.qfront;

	// initially, the list is empty
	qfront = qback = NULL;

	// nothing to do if p is NULL
	if (p != NULL)
	{
		// create the first node in the queue and assign
		// its addres to qback
		qfront = qback = getNode(p->nodeValue);

		// move forward in the list we are copying
		p = p->next;

		// copy remaining items
		while(p != NULL)
		{
			// insert new node at the back
			newNode = getNode(p->nodeValue);
			qback->next = newNode;

			// qback is the new node
			qback = newNode;

			// move to the next node of the list we are copying
			p = p->next;
		}
	}

	// the size of the new list is the size of q
	qsize = q.qsize;
}

template <typename T>
void linkedQueue<T>::clear()
{
	node<T> *curr = qfront, *p;

	// delete nodes until we arrive at the end of the list
	while (curr != NULL)
	{
		// save curr in p and move curr forward
		// to the next list node
		p = curr;
		curr = curr->next;

		// delete node p
		delete p;
	}

	// specify an emtpy list
	qfront = qback = NULL;
	qsize = 0;
}

template <typename T> // hafızada boş alan bulup node yaratır.
node<T> *linkedQueue<T>::getNode(const T& item)
{
	// allocate a new node
	node<T> *newNode = new node<T> (item);

	// check for failure
	if (newNode == NULL)
	  cout<<"Hata !";

	return newNode;
}

// create the empty list qfront = qback = NULL and qsize = 0
template <typename T>
linkedQueue<T>::linkedQueue(): qfront(NULL), qback(NULL), qsize(0)
{}

template <typename T>
linkedQueue<T>::linkedQueue(const linkedQueue<T>& obj)
{
	// call copy() and pass the pointer to the front of
	// the linked list in obj
	copy(obj);
}

template <typename T>
linkedQueue<T>::~linkedQueue()
{
	// call clear()
	clear();
}

template <typename T>
linkedQueue<T>& linkedQueue<T>::operator= (const linkedQueue<T>& rhs)
{
	// delete the current list
	clear();

	// make the current object a copy of rhs
	copy(rhs);

	return *this;
}

// insert item into the queue by inserting it at
// the back of the list
template <typename T>
void linkedQueue<T>::push(const T& item)
{
	// allocate space for the new node
	node<T> *newNode = getNode(item);

	// if the queue is empty, insert the new element at the front of
	// the list and update both qfront and qback
	if (qfront == NULL)
	{
		qfront = newNode;
		qback = newNode;
	}
	// in a non-empty list, insert new element at back and update qback
	else
	{
		qback->next = newNode;
		qback = newNode;
	}

	// increment the queue size
	qsize++;
}

// remove the item at the front of the queue by erasing
// the first element in the linked list
template <typename T>
void linkedQueue<T>::pop()
{
	// save the location of the front of the queue
	node<T> *p = qfront;

	// if the queue is empty, throw underflowError
	if (qsize == 0)
      cout<<"Boy = 0";

	// move the front forward one node
	qfront= qfront->next;

	// if the queue is now empty, set qback to NULL
	if (qfront == NULL)
		qback = NULL;

	// delete the node
	delete p;

	// decrement the queue size
	qsize--;
}

template <typename T>
T& linkedQueue<T>::front()
{
	// if the queue is empty, throw underflowError
	if (qsize == 0)
      cout<<"Queue boyu 0";

	// return the value at the front
	return qfront->nodeValue;
}

template <typename T>
const T& linkedQueue<T>::front() const
{
	// if the queue is empty, throw underflowError
	if (qsize == 0)
             cout<<"Queue boyu 0";

	// return the value at the front
	return qfront->nodeValue;
}

template <typename T>
int linkedQueue<T>::size() const
{
	return qsize;
}

template <typename T>
bool linkedQueue<T>::empty() const
{
	return qsize == 0;
}

int main()
{
	// declare an integer array and compute its size
	int arr[] = {6, 9, 2, 5}, i;
	int arrSize = sizeof(arr)/sizeof(int);

	// declare an empty queue of integer elements
	linkedQueue<int> q;

	// insert the array elements in q and output their value
	for (i = 0; i < arrSize; i++)
		q.push(arr[i]);

	// display the resulting size of the queue
	cout << "Queue size is " << q.size() << endl;

	// clear the queue
	while (!q.empty())
	{
		// display the element at the front and then
		// erase it from the queue
		cout << q.front() << "  ";
		q.pop();
	}
	cout << endl;

system("pause");
	// handle the underflowError exception thrown by a call to pop()

	return 0;
}
```

Kodu izleyerek beklenen çıktı:

```
Queue size is 4
6  9  2  5
```

Kuyruk FIFO olduğu için elemanlar eklendikleri sırayla (6, 9, 2, 5) çıkıyor.

*Not: Dosyanın sonundaki örnek çalışmada bir de "queue pop(): empty queue" satırı var; bu satır, istisna fırlatan özgün kitap sürümünün çıktısı. Bu uyarlamada boş kuyrukta `pop()` çağrılmıyor ve hata durumunda istisna yerine yalnızca mesaj yazıldığı için bu satır basılmaz. Ayrıca mesaj yazıldıktan sonra fonksiyon devam ettiği için boş kuyrukta `pop()` ya da `front()` çağrılırsa `NULL` işaretçi kullanılır; mesajdan sonra fonksiyondan çıkılmalı.*
