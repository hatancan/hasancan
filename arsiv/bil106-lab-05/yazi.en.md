---
baslik: BİL106 Laboratory Work #5: Character Operations and String Applications
ozet: BİL106 Introduction to Programming, Laboratory Sheet 5 (2014): converting from a custom number system to decimal, the hangigun function, word chains and farkiSay, and the difference between two times entered as strings. Four C programming problems with sample runs.
---

This post is the 5th laboratory assignment of the **BİL106 Introduction to Programming** course at Başkent University (March 2014). The topic is **character operations and string applications**: four C programming problems, worth 25 points each. The problems are reproduced as they appear on the lab sheet; the sample runs show the output the program is expected to produce on screen. The original PDF of the lab sheet can be downloaded at the end of the post.

## Problem 1: Custom number system to decimal (25 points)

In a custom number system, the symbols **I** are used in place of **1**, **U** in place of **10**, and **Z** in place of **100**. In this system, an integer is written by placing side by side as many I, U or Z symbols as there are units, tens and hundreds in the decimal system we use. Write a program that converts a number of at most 50 digits entered in this custom number system to the decimal system and prints it on the screen.

Sample run 1:

```
Özel sayı sistemindeki sayıyı giriniz: ZZUIIII
-------------------------
Girilen sayının onluk sistemdeki karşılığı : 214
```

Sample run 2:

```
Özel sayı sistemindeki sayıyı giriniz: ZZZI
-------------------------
Girilen sayının onluk sistemdeki karşılığı : 301
```

## Problem 2: Which day of the week? (25 points)

Write a function named `hangigun` that returns which day of the week it is, based on the day name passed to it, together with a `main` function in which the name of the day to be looked up is entered from the keyboard. Reading the input and printing the result must be done in the `main` function, and no global variables may be used.

Sample run:

```
Günün adı : Pazar
--------------------------------
Pazar günü haftanın 1. günüdür
```

## Problem 3: Word chain (25 points)

Write a program that keeps asking for a new word as long as the words entered from the keyboard form a chain. For a word chain to hold, each word must have been produced from the previous word by changing only one letter (without adding any new letters). The number of differing letters, position by position, between the newly entered word and the previous word must be found by a subfunction named `farkiSay`. This function takes the words and returns the number of differing letters. All subsequently entered words have the same length as the first word entered. Words can be at most 50 characters long.

Sample run:

```
İlk kelimeyi giriniz      : DEMİR
Sonraki kelimeyi giriniz  : KEMİR
 (1 harf farklı zincir bozulmadı)
Sonraki kelimeyi giriniz  : KESİR
 (1 harf farklı zincir bozulmadı)
Sonraki kelimeyi giriniz  : MESİR
 (1 harf farklı zincir bozulmadı)
Sonraki kelimeyi giriniz  : ZEHİR
 (2 harf farklı zincir bozuldu)
Program sona erdi
```

## Problem 4: Difference between two times (25 points)

Write a C program that, given two time values entered from the keyboard, calculates the difference between them in seconds and prints it on the screen. The times must be read as separate **strings**. The time will always be given in the format `SS:DD:SS` (hours:minutes:seconds).

Sample run (the times are entered as strings):

```
Birinci zamanı giriniz: 14:02:55
İkinci zamanı giriniz: 15:03:00
-------------------------
Aradaki fark : 3 saniyedir
```

*Note: In the lab sheet's example the difference is written as 3 seconds; however, the difference between 14:02:55 and 15:03:00 is actually 3605 seconds (1 hour and 5 seconds). The example has been left as it appears in the lab sheet.*
