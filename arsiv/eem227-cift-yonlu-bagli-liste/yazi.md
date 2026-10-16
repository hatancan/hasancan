---
baslik: EEM227 Veri Yapıları: Çift Yönlü ve Dairesel Çift Yönlü Bağlı Liste (Hafta 13)
ozet: EEM227 Veri Yapıları dersinin 13. haftasına ait C++ programları (Aralık 2007): çift yönlü bağlı listeye (doubly linked list) ve dairesel çift yönlü bağlı listeye (circular doubly linked list) sıralı ekleme, iki yönde yazdırma ve eleman silme.
---

Bu yazı, Başkent Üniversitesi **EEM227 Veri Yapıları** dersinin 2007 güz dönemi 13. hafta klasöründeki iki C++ programını içeriyor: **çift yönlü bağlı liste** (doubly linked list) ve **dairesel çift yönlü bağlı liste** (circular doubly linked list). Her ikisi de 12. haftadaki sıralı ekleme sorusunun devamı: düğümlere bir de önceki düğümü gösteren `pre` işaretçisi ekleniyor. Programların başında örnek çalışmalar yorum olarak verilmiş. Kaynak dosyalar yazının sonunda ZIP olarak indirilebilir.

## Çift yönlü bağlı liste

Her düğüm hem sonraki (`next`) hem önceki (`pre`) düğümü gösteriyor; ilk düğümün `pre`'si ve son düğümün `next`'i `NULL`. Sıralı eklemede tek yönlü listedeki dört durum aynı, yalnızca her bağlantı iki yönlü kuruluyor: başa eklerken eski head'in `pre`'si yeni düğüme, araya eklerken hem `pre->next` hem `curr->pre` yeni düğüme bağlanıyor.

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
      node<T> *pre;     // previous node in the list
public:

 node(const T& item, node<T> *nextNode=NULL, node<T> *previousNode=NULL)
      {
         nodeValue=item;
		 next=nextNode;
		 pre=previousNode;
	  }

static T LLSiraliEkle(T value, node<T> * &ptr)
{

node<T> *curr=ptr,*pre=ptr,*s;

 if( ptr == NULL) // Liste boş ise ilk nodu heade yerleştir.
      {
       ptr = new node<T> (value);
       ptr->next = NULL;
       ptr->pre = NULL;
      }

 else if (ptr->nodeValue >= value) // Başa ekle (sola)
     {
       s = new node<T> (value);
       s->next = ptr;
       ptr->pre = s;
       s->pre = NULL;
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
         s->pre = curr;
       }

   else  // araya ekle
         {
          s = new node<T> (value);
          pre->next = s;
          s->pre = pre;
          s->next = curr;
          curr->pre = s;
         }

 } // ELSE
}

static T printList(node<T> *ptr)
      {
        cout<<"NULL<-";
        while (ptr->next != NULL) // Araya ok koymak için bu şekilde yaptık...
        {
         cout << ptr->nodeValue<<"<=>" ;
         ptr = ptr->next;
        }
         cout<<ptr->nodeValue<<"->NULL" ;
           cout << endl;
       }

static T node<T>::ListedenSil(node<T>* &ptr, T value)
  {

node<T> *curr=ptr,*pre=ptr,*s;

 if( ptr == NULL) // Liste boş ise
         cout<<"Liste yaratilmamis !" ;

 else if (ptr->nodeValue == value) // İlk eleman silinecek
     {
       ptr = ptr->next;
       delete curr;
       ptr->pre = NULL;
       cout<<"Silme islemi basarili"<<endl;
     }

else
 {
  while (curr->nodeValue != value && curr->next!=NULL)
    {
      pre = curr;
      curr = curr->next;
     }

   if(curr->next == NULL && curr->nodeValue == value) // sondakini sil
       {
         pre->next = NULL;
         delete curr;
       }

   else  // silinecek eleman arada ise
         {
          pre->next = curr->next;
          curr->next->pre = pre;
          delete curr;
         }
         cout<<"Silme islemi basarili"<<endl;

 } // ELSE

  }

};

int main()
{
 node<int> *head=NULL;

  int SilinecekDeger;
  int adet,deger;

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

 cout<<endl;
 cout<<"Tum Liste\n";
     node<int>::printList(head);
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

Dosyanın başındaki örnek çalışma:

```
Kac eleman listeye eklenecek ? 7
Listeye eklenecek degeri giriniz: 35
Listeye eklenecek degeri giriniz: 888
Listeye eklenecek degeri giriniz: 41
Listeye eklenecek degeri giriniz: 2
Listeye eklenecek degeri giriniz: 7
Listeye eklenecek degeri giriniz: 98
Listeye eklenecek degeri giriniz: 45
NULL<-2<=>7<=>35<=>41<=>45<=>98<=>888->NULL

 Silinecek Degeri Giriniz : 45
Silme islemi basarili
NULL<-2<=>7<=>35<=>41<=>98<=>888->NULL
Press any key to continue . . .
```

Bu örnek çalışma programın önceki bir sürümünden alınmış görünüyor: dosyadaki son sürüm her eklemeden sonra listeyi yazdırıyor ve tüm listeden önce "Tum Liste" başlığını basıyor.

*Not: Silinecek değer listede yoksa döngü son düğümde durur ve kod "arada" dalına girer: `curr->next` `NULL` olduğu için `curr->next->pre` satırı programı çökertir (bulunamadı durumu ayrıca kontrol edilmeli). Listede tek eleman varken o silinirse `ptr` `NULL` olur ve `ptr->pre = NULL;` yine çöker. `ListedenSil` ve diğer fonksiyonlar `T` döndüreceklerini bildirdiği hâlde `return` içermiyor; `main`'deki `if` bu yüzden tanımsız bir değere bakıyor.*

## Dairesel çift yönlü bağlı liste

Dairesel listede son düğümün `next`'i yeniden head'i, head'in `pre`'si de son düğümü gösteriyor; `NULL` yok. Bu yüzden döngülerin bitiş koşulu `curr->next != ptr` (head'e geri dönüldü mü?) şeklinde yazılıyor. Liste iki yönde yazdırılabiliyor: `printList` saat yönünde (`next` ile), `printListT` saat yönünün tersinde (`pre` ile).

Başa ekleme durumunda yeni düğümün `pre`'sini bağlamak için önce listenin son düğümü bulunuyor (saat yönünde dolaşılıp head'den bir önceki düğüme geliniyor), sonra hem son düğüm hem eski head yeni düğüme bağlanıyor.

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
      node<T> *pre;     // previous node in the list
public:

 node(const T& item, node<T> *nextNode=NULL, node<T> *previousNode=NULL)
      {
         nodeValue=item;
		 next=nextNode;
		 pre=previousNode;
	  }

static T LLSiraliEkle(T value, node<T> * &ptr)
{

node<T> *curr=ptr,*pre=ptr,*s;

 if( ptr == NULL) // Liste boş ise ilk nodu heade yerleştir.
      {
       ptr = new node<T> (value);
       ptr->next = ptr;
       ptr->pre = ptr;
      }

 else if (ptr->nodeValue >= value) //  (headın solu gibi düşün)
     {
     while(curr->nodeValue >= value && curr->next != ptr)
        curr = curr->next; // Saat yönünde dolanıp head den 1 önceye geldik.

       s = new node<T> (value);
       s->next = ptr;
       s->pre = curr;
       curr->next = s;
       ptr->pre = s;
       ptr = s;
     }

else
 {
  while (curr->nodeValue <= value && curr->next!=ptr)
    {
      pre = curr;
      curr = curr->next;
     }

   if(curr->next == ptr && curr->nodeValue <= value) // saat yönünde git
       {
         s = new node<T> (value);
         s->next = ptr;
         s->pre = curr;
         ptr->pre = s;
         curr->next = s;
       }

   else  // araya ekle
         {
          s = new node<T> (value);
          pre->next = s;
          s->pre = pre;
          s->next = curr;
          curr->pre = s;
         }

 } // ELSE
}

static T printList(node<T> *ptr) // Saat Yonunde listeyi yazdır
      {
        cout<<"<-";
        node<T>*curr = ptr;
        while (curr->next != ptr) // Araya ok koymak için bu şekilde yaptık...
        {
         cout << curr->nodeValue<<"<=>" ;
         curr = curr->next;
        }
         cout<<curr->nodeValue<<"->" ;
           cout << endl;
       }

static T printListT(node<T> *ptr) // Saat yonunun tersinde listeyi yazdırma
      {
        cout<<"<-";
        node<T>*curr = ptr;
        while (curr->pre != ptr) // Araya ok koymak için bu şekilde yaptık...
        {
         cout << curr->nodeValue<<"<=>" ;
         curr = curr->pre;
        }
         cout<<curr->nodeValue<<"->" ;
           cout << endl;
       }

static T node<T>::ListedenSil(T value,node<T>* &ptr)
  {

node<T> *curr=ptr,*pre=ptr,*s;

 if( ptr == NULL) // Liste boş ise
         cout<<"Liste yaratilmamis !" ;

 else if (ptr->nodeValue == value && ptr->next!=ptr) // İlk eleman silinecek
     {
       ptr = ptr->next;
       curr->pre->next = curr->next ;
       curr->next->pre = curr->pre;
       delete curr;
//       ptr->pre = ptr;
  //     ptr->next = ptr;
       cout<<"Silme islemi basarili"<<endl;
     }

else
 {
  while (curr->nodeValue != value && curr->next!=ptr)
    {
      pre = curr;
      curr = curr->next;
     }

   if(curr->next == ptr && curr->nodeValue == value) // sondakini sil
       {
         pre->next = ptr;
         ptr->pre = pre;
         delete curr;
       }

   else  // silinecek eleman arada ise
         {
          pre->next = curr->next;
          curr->next->pre = pre;
          delete curr;
         }
         cout<<"Silme islemi basarili"<<endl;

 } // ELSE

  }

};

int main()
{
 node<int> *head=NULL;

  int SilinecekDeger;
  int adet,deger;

 srand(time(NULL));
 cout<<"Kac eleman listeye eklenecek ? ";
 cin>>adet;

 for(int i=0; i<adet; i++)
 {
    cout<<"Listeye eklenecek degeri giriniz: ";
    cin>>deger;
    node<int>::LLSiraliEkle(deger,head);
 }

     cout<<"Saat Yonunde Yazdıralım\n";
     node<int>::printList(head);
     cout<<"Saat Yonu Tersi Yazdıralım\n";
     node<int>::printListT(head);

 cout<<"\n Silinecek Degeri Giriniz : ";
 cin>>SilinecekDeger;

 if( node<int>::ListedenSil(SilinecekDeger,head ) )
    {
     cout<<"Saat Yonunde Yazdıralım\n";
     node<int>::printList(head);
     cout<<"Saat Yonu Tersi Yazdıralım\n";
     node<int>::printListT(head);
     }
 else
    cout<<" Silinecek deger listede bulunamadı !\n";

  system("pause");
  return 0;
}
```

Dosyanın başındaki örnek çalışma (13, 12, 42, 34 girilip 12 siliniyor):

```
Kac eleman listeye eklenecek ? 4
Listeye eklenecek degeri giriniz: 13
Listeye eklenecek degeri giriniz: 12
Listeye eklenecek degeri giriniz: 42
Listeye eklenecek degeri giriniz: 34
Saat Yonunde Yazdıralım
<-12<=>13<=>34<=>42->
Saat Yonu Tersi Yazdıralım
<-12<=>42<=>34<=>13->

  Silinecek Degeri Giriniz : 12
Silme islemi basarili
Saat Yonunde Yazdıralım
<-13<=>34<=>42->
Saat Yonu Tersi Yazdıralım
<-13<=>42<=>34->
Press any key to continue . . .
```

Saat yönünün tersinde yazdırma head'den (en küçük eleman) başlayıp `pre` ile önce en büyük elemana geçtiği için ters çıktı "12, 42, 34, 13" sırasında. Kod izlendiğinde örnek çalışmadaki çıktılar doğrulanıyor.

*Not: Silinecek değer listede yoksa döngü son düğümde durur ve kod "arada" dalına girerek son düğümü siler, ardından "Silme islemi basarili" yazar; bulunamadı durumu ayrıca kontrol edilmeli. Tek elemanlı listede o eleman silinirse head silinen düğümü göstermeye devam eder. Çift yönlü listedeki gibi fonksiyonların `return` deyimi yok ve `main`'deki `if` tanımsız bir değere bakıyor.*
