---
baslik: EEM227 Data Structures: Radix Sort, Priority Queue, and Linked List Nodes (Weeks 10–11)
ozet: C++ programs from weeks 10 and 11 of EEM227 Data Structures (November–December 2007): radix sort with an array of queues, the difference between priority_queue and a normal queue, sorting with priority_queue, and linked list construction questions using a node template class with insertion at the front and at the end.
---

This post contains the C++ programs from the folder for weeks 10 and 11 ("227_10_11") of the Başkent University **EEM227 Data Structures** course, fall semester 2007. There are three topics: **radix sort** working with queues, the STL **priority_queue**, and **linked list** construction questions using a `node` template class. The comments at the beginning of the programs and the screen outputs at the end were taken from the source files. The source files can be downloaded as a ZIP at the end of the post.

## Radix sort

The description at the beginning of the file:

- For numbers with d digits, the running time is O(2·d·n) = O(n).
- It is a linear algorithm.
- It runs fast because it does not sort by comparing numbers.

In each pass, the numbers are distributed (`distribute`) into 10 queues numbered 0–9 according to their digit for that pass (first the ones digit, then the tens digit, ...), and then the queues are emptied in order and collected back into the vector (`collect`). Because queues are FIFO, the order from the previous pass is preserved; after d passes the vector is sorted.

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
	queue<int> digitQueue[10]; // 10 queues were created

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
	int bnumber=2; // how many digits from the right to sort by
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

Sample run from the file:

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

*Note: The description at the beginning of the file says "20 random numbers of up to 3 digits"; however, the program generates numbers of at most 2 digits with `rand()%100` and sorts in 2 passes (`bnumber=2`). For 3-digit numbers, `rand()%1000` and `bnumber=3` should be used.*

## Priority queue

The description in the file: Elements with high priority are at the top of the priority queue, i.e., they are the values that will be processed first. Therefore, it removes the values pushed into the queue (`top()`) according to their priority, not according to the order in which they were pushed. The FIFO rule of the normal queue does not apply to the priority queue.

```cpp
#include <queue>
#include <iomanip>
#include <iostream>
#include <vector>
using namespace std;
int main()
{

// PRIORITY QUEUE
// Does NOT work as FIFO !!!
priority_queue<int> pq;
pq.push(10);
pq.push(30); // ---> This is the value with the highest priority !!! It is at the top
pq.push(5);
pq.push(3);
cout<<"PRIORITY QUEUE"<<endl;
cout<<"Size : "<<pq.size()<<endl<<"Yuksek Oncelikli Olan : "<<pq.top()<<endl;

// NORMAL QUEUE
//---------------
// Note: the normal queue has no top function !!! It has the front() function.
queue<int> s;
s.push(10); // ----> This one entered first (First In), so it will leave first!
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

### Sorting with priority_queue

Since inserting into the priority queue is already done automatically in an order based on priority, i.e., size, we do not need to perform any extra comparison. The elements are pushed into the queue, and each time the largest one (`top()`) is taken and placed in the vector from the end toward the beginning; thus the vector is sorted from smallest to largest. If the loop is set up from the beginning to the end, it sorts from largest to smallest.

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

// The sorting part-----------
for(int i=0 ; i<n ; i++)

  pq.push(v[i]);

for(int i=n-1 ; i>=0 ; i--) // Sorts from smallest to largest
//for(int i=0 ; i<n ; i++)  // Sorts from largest to smallest
{
 v[i] = pq.top();
 pq.pop();
} // Sorting finished------------

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

## Linked list questions

The same `node` template class is used in these questions: each node holds a value (`nodeValue`) and a pointer to the next node (`next`). The `printList` function that prints the list is defined as static; this way it can be called with the scope resolution operator as `node<int>::printList(...)`, without an object derived from the class. To put arrows between the nodes, the last node is printed separately after the loop.

### Question 1: create a linked list

The nodes are created by adding to the front of the list: the `next` of each new node points to the previous node.

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
 We defined the function as static in order to access it
without an object derived from the class */
static void printList(node<T> *ptr)
      {
        while (ptr->next != NULL) // We did it this way to put arrows in between...
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
// Structure that adds to the front of the list...

 node<int> *p = new node<int>(10);
 node<int> *q = new node<int>(20,p);
 node<int> *r = new node<int>(30,q);

// we accessed the function with scope resolution, without using an object
 node<int>::printList(r);

 system("pause");
 return 0;
}
```

```
30 -> 20 -> 10 -> NULL
Press any key to continue . . .
```

### Question 2: linked list of 10 random floats (insertion at the front)

> Create a linked list consisting of 10 random float numbers and print it on the screen. When creating the list, add the elements to the LL using the insert-at-front method.

There are two versions of this question in the folder. In the first version (`LL_STL_2_10RandomFloat.cpp`), the list is built directly on the `P` pointer; in the corrected version (`LL_STL_2_50Random.cpp`), the head of the list is kept in a `head` pointer initialized with `NULL`. The class is the same in both versions (the `node` class from Question 1 without the `curr` field; `printList` is declared here as `static T`).

The `main` function of the first version:

```cpp
int main()
{

node<float> *P;

for(int i=0 ; i<10 ; i++)
 P = new node<float> (15.0/(rand()%40*1.0),P);

// we accessed the static function with scope resolution, without using an object...
 node<float>::printList(P);

 system("pause");
 return 0;
}
```

Corrected version:

```cpp
int main()
{

node<float> *P,*head=NULL;

for(int i=0 ; i<10 ; i++)
{
  P = new node<float> (15.0/(rand()%40*1.0),head);
  head = P;
}
// we accessed the static function with scope resolution, without using an object...
 node<float>::printList(head);

 system("pause");
 return 0;
}
```

```
0.625->7.5->0.394737->0.394737->3.75->1.66667->0.75->1.07143->0.555556->15->NULL
Press any key to continue . . .
```

Since insertion is done at the front, the first generated number (15) appears at the end of the list.

*Note: In the first version, because `P` is used without being initialized, the `next` of the first inserted node of the list points to a random address; `printList` cannot find the end of the list. Also, if `rand()%40` yields zero, 15.0/0 produces an infinite (inf) value. In both files, although `printList` is declared to return `T`, it contains no `return` (it should be `void`).*

### Question: linked list of 10 random characters

> Create an LL consisting of 10 random character values. Do it using the insert-at-end method.

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

// we accessed the static function with scope resolution, without using an object...
 node<char>::printList(head);

 system("pause");
 return 0;
}
```

The expression `65+rand()%26` generates a random uppercase letter between 'A' and 'Z'. Sample output from the file:

```
Q->Q->J->H->T->S->U->A->U->NULL
Press any key to continue . . .
```

*Note: Because the loop runs from `i=1` to `i<10`, 9 nodes are created rather than 10 (the sample output also has 9 letters). Also, the question asks for insertion at the end, but the code adds each new node in front of `head`, i.e., at the front.*

### Question 4: list of integers by insertion at the end (without a function)

> Create a list of 10 integers by inserting at the end.

In this version, the members of the `node` class are made public; this way, the `next` field can be accessed directly inside `main` to find the end of the list, and the new node is linked there.

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
 We defined the function as static in order to access it
without an object derived from the class */
static T printList(node<T> *ptr)
      {

        while (ptr->next != NULL) // We did it this way to put arrows in between...
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

// we accessed the static function with scope resolution, without using an object...
 node<int>::printList(head);

 system("pause");
 return 0;
}
```

```
1->2->3->4->5->6->7->8->9->10->NULL
Press any key to continue . . .
```
