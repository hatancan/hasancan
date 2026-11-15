---
baslik: BİL106 Lab Assignment #9: Introduction to the C++ Programming Language
ozet: The 9th lab handout of the BİL106 Introduction to Programming course: sum and average with setw and setprecision, the asalatamamla function using a reference, the symmetric function with default parameters, and a class bonus. First steps with C++.
---

This post is the 9th lab assignment of the **BİL106 Introduction to Programming** course at Başkent University. The handout was prepared by Muhammet Yorulmaz; its aim is an **introduction to the C++ programming language**. Three typical novelties in the move from C to C++ are at the center of the questions: formatted output with `cout`, parameter passing by **reference (alias)**, and **default parameters**. The original PDF of the handout can be downloaded at the end of the post.

## Question 1: Sum and average (35 points)

Write a C++ program that prints the sum and the average of the numbers entered from the keyboard until the answer H (no) is given to the question "Do you want to continue?".

To print floating-point values to the screen in a formatted way, add the following lines to the header of the program and use them in your program by following the example.

```cpp
#include <iomanip>
using std::setprecision;   // Number of digits after the decimal point
using std::setw;           // Width of the number
```

Example:

```cpp
cout<<"sayı="<<setw(10)<<setprecision(4)<<18.6666666666666<<endl;
```

Output:

```
Sayı =     18.67
```

Sample run:

```
BİLGİ GİRİŞ
---------------------------------
Sayı= 7
Devam etmek istiyor musunuz?(E/H): E
Sayı= 9
Devam etmek istiyor musunuz?(E/H): E
Sayı= 40
Devam etmek istiyor musunuz?(E/H): H
----------------------------------
Girilen 3 adet sayının:
Toplamı = 56.00
Ortalaması= 18.67
```

## Question 2: asalatamamla with a reference (35 points)

Write a function named `asalatamamla` that converts the integer it takes as a parameter into the smallest prime number greater than itself, together with a `main` function in which the integer is entered from the keyboard. Print the modified value of the integer entered from the keyboard, after it has been passed to the function, inside `main`. No global variables should be used. Write this program **using a reference (alias) instead of a pointer**.

Sample run:

```
Tam sayıyı giriniz : 6
--------------------------------
Sayının dönüştüğü asal sayı = 7
```

## Question 3: Symmetric with default parameters (30 points)

Write a function named `simetrik` that produces the symmetric of a point according to the coordinates of the point sent to it and the axis information. This function takes 3 parameters: the x and y values of the point and the axis information. When `'X'` is sent as the axis information, it takes the symmetric with respect to the X axis; when `'Y'` is sent, with respect to the Y axis; and when `'O'` is sent, with respect to the origin. Define the function so that, when no axis information is sent, the **default is the origin**.

## Bonus (10 points)

Write and run any class application shown in the lecture.

*Note: Because the character encoding in the PDF is corrupted, some "İ" letters appear as "Đ"; this was corrected in the post. The handout's internal file name is "Bil106_lab11_06" and the file is dated 2010, while its title is "Laboratory Assignment #9".*
