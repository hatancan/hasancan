---
baslik: BİL106 Laboratory Work #10: Defining Classes in C++
ozet: The 10th laboratory handout of the BİL106 Introduction to Programming course (2015): a Date class, a Line class that models a line segment in the two-dimensional plane (slope, translation), and a Triangle class that obeys the triangle rule. C++ classes with a separation of interface and implementation.
---

This post is the 10th laboratory assignment of the Başkent University **BİL106 Introduction to Programming** course (April 2015). The handout was prepared by Muhammet Yorulmaz; the goal is **defining classes**. In the questions, C++ classes are to be written separately as an interface and an implementation; the student decides which member functions are needed by looking at the example program. The original PDF of the handout can be downloaded at the end of the post.

## Question 1: The Date class (20 points)

Write and run the code of the `Tarih` (Date) class example that you solved in class.

## Question 2: The Line class (40 points)

Write the interface and the implementation of a class named `Dogru` (Line) that models a line segment in the two-dimensional plane. The member data of this class definition are the coordinate values of the two endpoints of the line (x1, y1 and x2, y2). Determine which member functions the class will have according to their usage in the program below.

Note: The slope of a line whose two points are known is found with the following formula: **slope = (y1 − y2) / (x1 − x2)**

Example program:

```cpp
...........................//Include the interface in the code
int main()
{
  Dogru a;
  a.yaz();
  cout << "Doğrunun eğimi=" << a.egim() << endl;
  a.kaydir('x',3); // shifts by the desired amount
                   // along the x or y axis
  a.yaz();
  return 0;
}
```

Output:

```
X1= 1, Y1= 2, X2= 3, Y2= 4
Doğrunun eğimi = 1
X1= 4, Y1= 2, X2= 6, Y2= 4
```

## Question 3: The Triangle class (40 points)

Write the interface and the implementation of a class named `Ucgen` (Triangle) that models the geometric shape of a triangle. The member data of this class definition are the side length values of the triangle. Determine which member functions the class will have according to their usage in the program below.

Triangle rule: The length of a side is greater than the difference of the other two sides and less than their sum.

Example program:

```cpp
...........................//Include the interface in the code
int main()
{
   Ucgen a( 3, 4);
   //if desired, all 3 side lengths can also be given
   //However, when two sides are given, the 3rd side is
   //assigned randomly in accordance with the triangle rule.
   a.yaz();
   cout << "Üçgenin çevresi=" << a.cevre();
   return 0;
}
```

Output:

```
a= 3, b= 4, c= 5
Üçgenin çevresi= 12
```

*Note: Since the third side is chosen randomly, the output may differ on each run; 3-4-5 is only an example. In a triangle with sides 3 and 4, the third side must be between 1 and 7 (exclusive).*
