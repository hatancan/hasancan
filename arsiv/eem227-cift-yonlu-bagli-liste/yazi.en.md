---
baslik: EEM227 Data Structures: Doubly Linked List and Circular Doubly Linked List (Week 13)
ozet: C++ programs from week 13 of EEM227 Data Structures (December 2007): sorted insertion into a doubly linked list and a circular doubly linked list, printing in both directions, and element deletion.
---

This post contains two C++ programs from the week 13 folder of the Fall 2007 **EEM227 Data Structures** course at Başkent University: a **doubly linked list** and a **circular doubly linked list**. Both continue the sorted insertion exercise from week 12: each node gets an additional `pre` pointer that points to the previous node. Example runs are given as comments at the beginning of the programs. The source files can be downloaded as a ZIP at the end of the post.

## Doubly linked list

Each node points to both the next node (`next`) and the previous node (`pre`); the `pre` of the first node and the `next` of the last node are `NULL`. In sorted insertion, the four cases are the same as in the singly linked list, except that every link is now established in both directions: when inserting at the head, the `pre` of the old head is connected to the new node, and when inserting in the middle, both `pre->next` and `curr->pre` are connected to the new node.

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

Example run at the beginning of the file:

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

This example run appears to have been taken from an earlier version of the program: the final version in the file prints the list after every insertion and prints a "Tum Liste" ("Entire List") heading before the full list.

*Note: If the value to be deleted is not in the list, the loop stops at the last node and the code enters the "middle" branch: since `curr->next` is `NULL`, the line `curr->next->pre` crashes the program (the not-found case should be checked separately). If the list has a single element and that element is deleted, `ptr` becomes `NULL` and `ptr->pre = NULL;` crashes as well. `ListedenSil` and the other functions are declared to return `T` but contain no `return`; the `if` in `main` therefore tests an undefined value.*

## Circular doubly linked list

In a circular list, the `next` of the last node points back to the head, and the `pre` of the head points to the last node; there is no `NULL`. For this reason, the loop termination condition is written as `curr->next != ptr` (have we come back around to the head?). The list can be printed in both directions: `printList` prints clockwise (using `next`), and `printListT` prints counterclockwise (using `pre`).

When inserting at the head, the last node of the list is first located (by traversing clockwise to the node just before the head) in order to link the `pre` of the new node; then both the last node and the old head are linked to the new node.

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

Example run at the beginning of the file (13, 12, 42, 34 are entered and 12 is deleted):

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

Because counterclockwise printing starts at the head (the smallest element) and moves via `pre` first to the largest element, the reversed output comes out in the order "12, 42, 34, 13". Tracing through the code confirms the outputs in the example run.

*Note: If the value to be deleted is not in the list, the loop stops at the last node and the code enters the "middle" branch, deleting the last node and then printing "Silme islemi basarili" ("Deletion successful"); the not-found case should be checked separately. If the list has a single element and that element is deleted, the head keeps pointing to the deleted node. As in the doubly linked list, the functions have no `return` statement and the `if` in `main` tests an undefined value.*
