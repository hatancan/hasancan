---
baslik: EEM227 Data Structures: STL list, stack and queue Examples (Weeks 7–8)
ozet: C++ STL programs from weeks 7 and 8 of the EEM227 Data Structures course (November 2007): traversing a list and a vector with an iterator, insert and erase, descriptions of the stack and queue functions, printing a number in reverse using a queue, and writing your own queue class using a vector.
---

This post collects the C++ programs from the week 7 and week 8 folders of the **EEM227 Data Structures** course at Başkent University, fall semester 2007. The topics are the STL **list** container and iterators, and the **stack** and **queue** container adaptors. In most of the programs, the explanations and the screen output were written as comments; here the explanations have been moved into the text and the outputs into console windows. The source files can be downloaded as a ZIP at the end of the post.

## Printing a list and a vector with an iterator

Since lists have no index operator, their elements are accessed with an iterator. This program prints an int list from beginning to end (using a while loop and a for loop), a double list from end to beginning, and a vector with an iterator, without using indices.

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

## Modifying list elements with a template function and an iterator

An example of changing the values of list elements with the help of an iterator, using a template function: `degistir` increments each element by one.

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

## insert and erase operations

After creating a list, this program inserts an element at a desired position and deletes the element at a desired position. Since there is no index operator, iterators are used when moving through the list elements. The list's `insert()` and `erase()` functions must take as a parameter an iterator defined on the list being operated on.

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

*Note: An iterator that points to an element removed with `erase` becomes invalid; reading it with `*iter2`, as the program does, is undefined behavior. The 40 appearing in the output is due to the memory not yet having been overwritten with that compiler. The correct usage is `iter2 = L.erase(iter2);`, which obtains the position after the removed element.*

## stack

### stack functions

The explanations at the top of the file:

- `void pop();` Removes the topmost element from the stack. Precondition: the stack must not be empty. Postcondition: the stack may be empty (if there was only one element), the topmost element of the stack changes, and the number of elements in the stack decreases by 1.
- `void push( const T & item);` Adds the value given as a parameter to the top of the stack. Postcondition: there is a new element at the top of the stack.
- `T& top();` Returns a value that is a reference to the topmost element. Precondition: the stack must not be empty.
- `const T& top() const;` The const version of the previous function.
- `bool empty() const;` Returns true if the stack is empty.
- `int size() const;` Returns the number of elements in the stack.

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

### A 10-element stack with a while loop

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

Because the last element in is the first one out (LIFO), the numbers are printed in the reverse of the order in which they were pushed.

*Note: The definition `stack<int> sayi[10];` in the comment creates 10 separate stacks, not 5.*

## queue

Queue functions (from the explanations in the file):

- `bool empty() const;` True if the queue is empty, false otherwise.
- `T& front();` Returns a reference to the element at the front of the queue. Precondition: the queue must not be empty.
- `const T& front() const;` The constant version of the front() function.
- `void pop();` Removes the element at the front of the queue. Precondition: the queue must not be empty.
- `void push(const T & item);` Adds the argument named item to the back of the queue. Postcondition: there is a new element at the back of the queue.
- `int size() const;` Returns the number of elements in the queue.

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

Because the first element in is the first one out in a queue (FIFO), the numbers are printed in the order in which they were entered.

## Question: printing a number in reverse using a queue (Week 8)

> Write a program that can print an N-digit number entered from the keyboard in reverse, using the queue data structure.

The digits of the number are separated from last to first by taking the number modulo 10 and are added to the queue; since the queue is FIFO, the digits are printed in the order in which they were separated, that is, as the reverse of the number.

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

For example, if 12345 is entered, 5, 4, 3, 2, 1 are added to the queue in that order, and "Tersten Sayi : 54321" is printed on the screen.

*Note: Since `int` can hold at most 2147483647, some 10-digit numbers (those greater than 2147483647) overflow; `long long` is needed for the "Max. 10 digits" limit.*

## Question: building your own queue structure with a vector (Week 8)

> Using the vector data structure, build your own Queue structure.

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

Expected output, traced from the code:

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

Because insertion is done at the end of the vector (`push_back`) and removal from the front (the first element with `erase`), the structure behaves like a queue.

*Note: In the `Print` function, the iterator is defined as `vector<int>::iterator` instead of `vector<T>::iterator`; as it stands, the class compiles only for `MyQueue<int>`.*
