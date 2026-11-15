---
baslik: EEM227 Data Structures: Template Classes and vector Functions
ozet: C++ programs from weeks 5 and 6 of EEM227 Data Structures (October–November 2007): a Sayi template class that adds numbers of different types, a Bilgi template class with overloaded << and >>, and template functions for STL vector (printing, empty check, insertion, resize).
---

This post contains three C++ programs found in the week 5 and week 6 folders of the Başkent University **EEM227 Data Structures** course, fall 2007 semester. The topic is **templates**: classes that work with any data type, and template functions that operate on the STL `vector`. The first two programs begin with the problem statement and end with the screen output, both written as comments. The source files can be downloaded as a ZIP at the end of the post.

## Question 1: a template class that adds numbers of different types

> Write a template class that can add numbers of different types and print the result using an overloaded << operator.

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

Screen output:

```
Tamsayi Toplam Sonucu :8
Float Toplam Sonucu :7.1
Double Toplam Sonucu :62392.2
Press any key to continue . . .
```

On the last line the actual sum is 62392.173; since `cout` displays 6 significant digits by default, it is printed as 62392.2.

## Question 2: a template class that stores and prints any type of data

> Design a template class that can store a piece of data of any type entered from the keyboard and print it back to the screen. Overload the >> and << operators to be used for reading from the keyboard and writing to the screen for this class. Code a main program showing that your class works for different types of data entered from the keyboard (int, float, double, char, string).

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

Screen output (Merhaba, W, 56 and 34.67 were entered from the keyboard):

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

*Note: In the second friend declaration at the top of the class, the first parameter of `operator>>` was mistakenly written as `ostream &`; since the actual definition is made with `istream &`, the program works, but these two forward declaration lines are unnecessary. The problem statement also asks for double among the types; double was not tried in the main program.*

## Template functions for vector

`Vectorler.cpp` in the week 6 folder defines small template functions that work with the STL `vector`: printing a vector, checking whether it is empty, and appending an element. Creating a vector from an array, `back()` and `resize()` are also demonstrated. The `Cikart` function that removes an element is commented out (as it stands it would not compile, because `pop_back()` does not return a value).

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

Screen output:

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

`resize(10,0)` grows the vector to 10 elements and fills the new slots with 0; `resize(4,0)` shrinks the 5-element vector to 4 elements (the last element, 10.1, is discarded).

*Note: The `BosmuDolumu` function returns true when the vector is **non-empty** (`empty()==0` means non-empty). That is why "Empty ? :1" is printed for both non-empty vectors; relative to the question, the output is misleading. For the question "is it empty?", `return Ref.empty();` should be written directly.*
