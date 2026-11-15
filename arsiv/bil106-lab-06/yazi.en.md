---
baslik: BİL106 Laboratory Work #6: Structures (struct) and Strings
ozet: The 6th laboratory sheet of the BİL106 Introduction to Programming course: a list sorted by average using the student structure, a time structure and the zamantopla function, and floatToplam, which splits a decimal number into its sign, integer and fractional parts. Three C programming questions and sample runs.
---

This post is the 6th laboratory work of the **BİL106 Introduction to Programming** course at Başkent University. The sheet was prepared by Muhammet Yorulmaz; the stated goal of the sheet is "strings", but all of the questions are actually built on **structures (struct)** in C. The questions are reproduced as they appear on the sheet; the original PDF of the sheet can be downloaded at the end of the post.

## Question 1: Sorting the student list by average

Define a structure named `ogrenci` whose members are as follows. Define an array of 10 elements of this structure type, write a program that reads its elements from the keyboard and lists them on the screen from largest to smallest according to their average.

| Member name | Type | Length |
|---|---|---|
| ad | character | 20 |
| soyad | character | 20 |
| ort | floating-point | – |

Sample run:

```
1. adı,soyadı,ortalamasını giriniz: Mehmet Çelik 3.45
2. adı,soyadı,ortalamasını giriniz: Dursun Mert 2.45
:   :   :
9. adı,soyadı,ortalamasını giriniz: Ahmet Serdar 3.00
10. adı,soyadı,ortalamasını giriniz: Sinan Tonguç 2.99
--------LİSTE------------------
Mehmet Çelik 3.45
Ahmet Serdar 3.00
Sinan Tonguç 2.99
Dursun Mert 2.45
:   :   :
```

## Question 2: The zamantopla function that adds two times

Define a structure (struct) named `zaman` whose members are as follows. In the main function, define two variables named `a1` and `a2` of this structure type. Set their initial values to (23, 30, 20) and (1, 0, 40), respectively. Write a function named `zamantopla` that takes these two variables and adds the second to the first. After the function finishes, the values in `a1` must be (0, 31, 0). To demonstrate this, print the values of the variables to the screen in the main function, after the function call.

| Member name | Type |
|---|---|
| saat | integer |
| dakika | integer |
| saniye | integer |

## Question 3: floatToplam, which splits a decimal number into its parts

Define a structure (struct) named `ondalik` whose members are as follows, in order to represent floating-point (float) numbers.

| Member name | Member type |
|---|---|
| Sign | Character |
| Integer part | Integer |
| Fractional part | Integer |

Accordingly, write a function named `floatToplam` that takes two floating-point numbers, splits their sum into parts, and stores the result in the variable passed as its 3rd parameter, which is defined with the structure type above. Only 3 digits of the fractional part will be kept. Your function must be compatible with the `main` function below. Do not use global variables, and do not make any additions to the `main` function other than the blank (dotted) places. The function prototype and the function call will also be evaluated.

Sample program:

```c
........................... /*Structure definition*/
............................... /*Prototype*/
int main()
{
   struct ondalik sonuc;
   float sayi1=-987.6543, sayi2=12.34;

   floatToplam(sayi1, sayi2, &sonuc);
   printf("Sonucun tamkısmı=%ld\n", sonuc.tam);
   printf("Sonucun ondalıkkısmı=%ld\n", sonuc.on);
   printf("Sonucun işareti=%c", sonuc.isaret);
   return 0;
}
```

Output:

```
Sonucun tamkısmı=975
Sonucun ondalıkkısmı=314
Sonucun işareti= -
```

*Note: -987.6543 + 12.34 = -975.3143; that is, the integer part is 975, the first three digits of the fractional part are 314, and the sign is minus. The quotation marks on the sheet were Word "smart quotes"; they were written as straight quotes so that the code can be compiled.*
