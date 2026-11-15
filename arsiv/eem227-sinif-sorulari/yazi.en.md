---
baslik: EEM227 Data Structures: C++ Class Questions and Solutions (Questions 3–6, Lab 1)
ozet: Solved questions from the EEM227 Data Structures course on C++ classes (September 2007): const and static members, friend functions, a Book class with ISBN generation, a Bag class for Ali and Veli's ball-drawing game; also the rational number and complex number class lab programs.
---

This post collects the **solved exam-style questions** shared in the fall 2007 semester of the **EEM227 Data Structures** course at Başkent University. The Question 3–6 sheets are signed by **Lecturer Oğul Göçmen** and dated 30 September 2007; all of them cover classes, const and static members, and friend functions in C++. At the end of the post there are also two lab programs from the same week's folder: a rational number class (the Lab 1 answer) and a complex number class with operator overloading. The original PDFs of the questions and the source files can be downloaded as a ZIP at the end of the post.

## Question 3: Are the statements on class A correct?

The definitions of class A are given below. Based on these definitions, state whether the operations performed on class A through the statements in the given main function are correct. If an operation is wrong, briefly explain why.

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

Solution:

| Statement | Correct/Incorrect | Reason for the error |
|---|---|---|
| `A obj1;` | CORRECT | |
| `const A obj2(24);` | CORRECT | |
| `A obj3(12, 2.2);` | CORRECT | |
| `obj1.a = 12;` | INCORRECT | A private member cannot be accessed |
| `obj3.d = obj2.getA();` | CORRECT | |
| `obj2.setMembers(3,"aaa");` | INCORRECT | A const object cannot call a non-const function |
| `obj1.p();` | CORRECT | |
| `A::p();` | CORRECT | |
| `obj3.c = 'x';` | INCORRECT | Cannot assign to a const member |
| `A::setMembers(1,"bbb");` | INCORRECT | The function is not static |

## Question 4: A Book class for a library

To organize the books in a library, we want to implement a class named "Kitap" (Book) and its functions as a C++ program. The system in the library works as follows:

- Each book in the library has a name of at most 100 characters, an ISBN code of at most 14 characters, a publication year, and a page count.
- The 14-character ISBN codes are stored in the format ISBN-2006-2987. Each ISBN number thus consists of 3 fields separated by hyphens (-). The first field is the same in all codes and consists of the characters 'I', 'S', 'B', 'N'; the second field is the year of the book; and the last field is a number indicating which book registered in the library the book in question is. For example, the ISBN code of a book registered in the library in 2006 that is the 15th book in the library must be ISBN-2006-15.
- When a new book is added to the library, the program must automatically generate and assign the ISBN number of that book (you may assume that the year is 2006).
- For any book to be registered in the library, the book name, publication year, and page count must be entered.
- Once a book is registered in the library, its page count is fixed and must not be changed afterward.
- The program is expected to be able to display the total number of books registered in the library on the screen.

Given the constraints above, assuming that all variables you define in the class will be private, write the class definition and the necessary functions.

**NOTE:** If you need to convert an int number to a string while implementing this program, you may use the function whose prototype is given below as if it were implemented in your program: `char * IntToString (int number)`. This function takes an int number (number) as a parameter and returns that number as a string.

Solution:

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

The fact that the page count cannot be changed afterward is ensured by `const unsigned SayfaSayisi` (assigned in the constructor's initializer list), and the total number of books is kept in `static unsigned KitapSayisi`, which is shared by all objects. Since the function that displays the total is also static, it can be called without an object as `Kitap::ToplamKitapSayisi()`.

*Note: In the solution's `IntToStr(KitapNo)` call, the function name does not match the `IntToString` given in the question, and no variable named `KitapNo` is defined. The book's sequence number should be `KitapSayisi + 1` (or the `KitapSayisi++` line should be executed first and then `IntToString(KitapSayisi)` used).*

## Question 5: friend function and const object

Based on the following class definition, write the reasons why the statements written in the main function that are incorrect are wrong.

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

Solution (5 points for each wrong statement):

| Statement | Reason for the error |
|---|---|
| `Nesne1.var2=29;` | An object cannot directly access a private member. Since the object is const, its value cannot be changed. |
| `Nesne1.setValue(5, "yyy", MyStr);` | MyStr is an extra argument. A const object cannot call a non-const function. |
| `MyFunc(5.8, c);` | It should be `MyFunc(c,5.8)`. |
| `Nesne3.MyChar = 'x';` | An object cannot directly access a private member. |
| `A::setValue(1, "zzz");` | The function is not static. |

The other lines (`A c(35);`, `const A Nesne1;`, `A Nesne2(18);`, `A Nesne3(29, 4.2);`, `Nesne3.var1 = Nesne1.getValue();`, `Nesne3.print();`, `A::print();`) are correct.

*Note: The class definition in the question is missing a `;` after the closing brace (it should be `};`).*

## Question 6: Ali and Veli's ball game (Torba class, 35 points)

Ali and Veli are playing a game of chance. The bag A in Ali's hand contains 10 red, 6 yellow, and 3 blue balls. The bag B in Veli's hand contains 10 red, 3 yellow, and 6 blue balls. The rules of the game are as follows: Either person starts the game, and balls are drawn in turn, one at a time. Each player draws a ball at random from their own bag. If the ball drawn is red, the ball is taken out of the bag; otherwise it is put back into the bag. Whether the ball drawn is red or not, the turn passes to the other player. Whoever has a total of 3 red balls outside the bag wins the game.

You are asked to write a C++ program that implements this game. In this program, write a class named "Torba" (Bag); define the member functions of this class as public and its data members as private. Accordingly:

- The constructor of this class takes the quantities of red, yellow, and blue balls, in that order, as parameters. If the number of balls of any color is not given as a parameter, it sets the quantity of that ball in the bag to 10.
- The member function named "Goster" (Show) prints on the screen how many balls of each color are in a bag and the total number of balls in the bag.
- The member function named "ToplamTop" (TotalBalls) returns the total number of balls in a bag.
- The member function named "ToplarinOrani" (BallRatios) calculates, for each color of ball in a bag, the percentage ratio of that color to the total number of balls, and prints it on the screen.
- The member function named "TopCek" (DrawBall) draws one ball of a random color from a bag and returns its value.
- The member function named "TopCikart" (RemoveBall) removes the ball of the value given to it as a parameter from the bag.
- The function named "TopEkle" (AddBall) adds the ball of the value given to it as a parameter to the bag.

Accordingly, write a program that, when the game ends, prints on the screen the winner, the number of balls in their bag, and the percentage ratio of the balls in their bag. **Attention:** Write the code split into parts ("main.cpp", "Torba.h", "Torba.cpp").

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
     case 0: KSM[0]--; return 0; break;      //   THE BALL DRAWN WAS RED
     case 1: KSM[1]--; return 1; break;      //   THE BALL DRAWN WAS YELLOW
     case 2: KSM[2]--; return 2; break;      //   THE BALL DRAWN WAS BLUE
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

      // OPERATIONS NEEDED FOR BAG A IN ALI'S HAND

      if(sira%2){
         renkkodu=A.TopCek();
         if( renkkodu == 0 ){ //- IF IT IS A RED BALL
            A.TopEkle(renkkodu); // Prevent the decrement made by TopCek
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
// OPERATIONS NEEDED FOR BAG B IN VELI'S HAND

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

*Note: In the solution, `TopCek` does not select the color in proportion to the ball counts in the bag; it picks one of the three colors with equal probability using `rand()%3` (in Ali's bag the probability of drawing red should be 10/19 but it is 1/3; and if no balls of that color remain, the count can even go negative). Also, since `srand(time(NULL))` is called again on every draw, draws within the same second always give the same result; `srand` should be called once at the start of the program. Since the constructor's default values (`=10`) are written only in the definition in Torba.cpp, they are not visible from main.cpp; for the "if not given, 10" rule in the question, the defaults should be in the declaration in Torba.h.*

## Lab 1 answer: rational number class

The file `EEM227_Lab1_Cevap.cpp` in the folder (dated October 2006) is a `rasyonel` (rational) class that stores the numerator and denominator, reduces the fraction, tests the equality of two rational numbers, and performs multiplication and division. The addition function is commented out.

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

  // Reducing both rational numbers to lowest terms
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
  // Reducing both rational numbers to lowest terms
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
  // Reducing both rational numbers to lowest terms
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

Multiplication is done with cross-cancellation: the numerator of the first number is reduced against the denominator of the second, and the numerator of the second against the denominator of the first, and then the results are multiplied. In the reduction, the `indirge` function finds the greatest common divisor using Euclid's algorithm.

*Note: In the `carp` function, after the `rnl1.degerata(...)` line, `rnl.indirge();` was mistakenly written instead of `rnl1.indirge();` (the result does not change since rnl1 is already reduced inside `degerata`, but the line operates on the uninitialized `rnl` object).*

## Complex number class (operator overloading)

`karmasik.cpp` (October 2007) in the same folder overloads the +, -, and * operators and the << and >> stream operators for complex numbers. The program reads three complex numbers and prints the sum a+b+c, the difference a-(b+c), and the value a·b + b·c.

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

*Note: Although the `operator>>` and `operator<<` functions declare that they return references, the `return oku;` / `return yaz;` lines are missing; this is undefined behavior. That is why the program prints the outputs separately instead of chaining like `cout<<d<<endl`.*
