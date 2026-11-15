---
baslik: EEM227 Data Structures: Example Problems and Java Solutions
ozet: Six example problems solved in the EEM227 Data Structures course videos, with Java solutions: the largest of three numbers, letter grade from midterm and final, days of the week with switch (including fall-through), odd-even, reversing a number, and sum of digits.
---

This post brings together the example problems worked through in the videos of the Başkent University **EEM227 Data Structures** course (November 2013), along with the Java solutions from the course's BlueJ project named "OrneklerVideo1". Each problem is given as it appears in the original text file, followed by the solution code. The problem files and the solution project can be downloaded as a single ZIP at the end of the post.

The code uses `static` methods; in BlueJ you could right-click a method and enter parameters to run it directly, so most of them have no `main`.

## 1. The largest of three entered numbers

Print the largest of the 3 entered numbers to the screen.

```
Örnek girdi 20 10 5    → Cevap 20
Örnek girdi 20 50 5    → Cevap 50
Örnek girdi 20 50 200  → Cevap 200
```

```java
public class Girilen3SayiEnBuyuk
{
    public static int enBuyukBul(int a , int b, int c)
    {
        int enBuyuk;
        if (a > b)
        {
            enBuyuk = a;
        }
        else
        {
            enBuyuk = b;
        }
        if (enBuyuk < c)
        {
            enBuyuk = c;
        }
        return enBuyuk;
    }
}
```

## 2. Letter grade from midterm and final grades

Write code that takes the midterm grade and the final grade, computes the course grade according to the formula below, and returns the letter form of this grade.

**Final Grade = Midterm Grade × 0.4 + Final Exam Grade × 0.6**

| Final grade | Letter |
|---|---|
| 100–90 | A |
| 89–80 | B |
| 79–70 | C |
| 69–60 | D |
| 59–0 | F (Fail) |

Input: midterm grade (int), final exam grade (int). Output: final letter grade (String).

```java
public class SonHarfNot
{
    public static double sonNotBul(double vizeNotu,double finalNotu)
    {
        return vizeNotu* 0.4 + finalNotu* 0.6;
    }

    public static String sonNotHarfOlarakBul(double vizeNotu,double finalNotu)
    {
        double sonNot = sonNotBul(vizeNotu,finalNotu);

        String sonNotHarf;
        if (sonNot > 90)
        {
            sonNotHarf = "A";
        }
        else if (sonNot > 80)
        {
            sonNotHarf = "B";
        }
        else if (sonNot > 70)
        {
            sonNotHarf = "C";
        }
        else if (sonNot > 60)
        {
            sonNotHarf = "D";
        }
        else
        {
            sonNotHarf = "F";
        }
        return sonNotHarf;
    }
}
```

*Note: According to the table, 90 should be an A and 80 a B; because the code uses `>`, grades exactly on the boundary (90, 80, 70, 60) fall to the next lower letter. The correct operator would be `>=`.*

## 3. Days of the week with switch

Input: the day number. Output: the day of the week as text (1 Monday, 2 Tuesday, 3 Wednesday, 4 Thursday, 5 Friday, 6 Saturday, 7 Sunday).

The solution has two versions. The second is the correct one; the first deliberately omits `break` to demonstrate **fall-through** behavior: whichever day is entered, execution continues downward and the result is always `"HATALI GIRIS"`.

```java
public class HaftaninGunleri
{
    public static String haftaninGununuBulSwitchOrnekFallThrough(int gun)
    {
         String yaziGun = "";
         switch(gun)
         {
             case 1:
                yaziGun = "Pazartesi";
             case 2:
                yaziGun = "Salı";
             case 3:
                yaziGun = "Çarşamba";
             case 4:
                yaziGun = "Perşembe";
             case 5:
                yaziGun = "Cuma";
             case 6:
                yaziGun = "Cumartesi";
             case 7:
                yaziGun = "Pazar";
             default:
                yaziGun = "HATALI GIRIS";
                break;
         }
         return yaziGun;
    }

    public static String haftaninGununuBulSwitchOrnek(int gun)
    {
         String yaziGun = "";
         switch(gun)
         {
             case 1:
                yaziGun = "Pazartesi";
                break;
             case 2:
                yaziGun = "Salı";
                break;
             case 3:
                yaziGun = "Çarşamba";
                break;
             case 4:
                yaziGun = "Perşembe";
                break;
             case 5:
                yaziGun = "Cuma";
                break;
             case 6:
                yaziGun = "Cumartesi";
                break;
             case 7:
                yaziGun = "Pazar";
                break;
             default:
                yaziGun = "HATALI GIRIS";
                break;
         }
         return yaziGun;
    }
}
```

## 4. Odd or even?

Determine whether an entered number is odd or even.

```
Örnek girdi 2  → Çıktı: Çift
Örnek girdi 15 → Çıktı: Tek
```

```java
public class TekCift
{
    public static String tekCiftBul(int girdiSayi)
    {
        if ( girdiSayi % 2 == 0)
        {
            return "Çift";
        }
        else
        {
            return "Tek";
        }
    }
}
```

## 5. Reversing a number

Write code that prints the exact reverse of an entered number. Example input 12345, example output 54321. The problem file notes two approaches: **numeric operations** and **string operations**.

```
12345 = 10000*1 + 1000*2 + 100*3 + 10*4 + 1*5
54321 = 10000*5 + 1000*4 + 100*3 + 10*2 + 1*1
```

```java
public class SayiTersi
{
    public static int sayiTersiniBul(int girdiSayi)
    {
        int toplam=0;
        int basamakDeger = basamakDegerBul(girdiSayi);

        while(girdiSayi > 0)
        {
            int basamak = girdiSayi % 10;
            toplam = toplam + basamak * basamakDeger;
            basamakDeger = basamakDeger / 10;
            girdiSayi = girdiSayi / 10;
        }
        return toplam;
    }

    public static int basamakDegerBul(int girdiSayi)
    {
        int deger = (int)Math.log10(girdiSayi);
        return (int)Math.pow(10,deger);
    }

   public static String sayiTersiniBulStringAl(String girdiSayi)
   {
       String toplam="";
       char[] charDizisi = girdiSayi.toCharArray();

       for(int i =charDizisi.length-1; i>=0 ;i--)
       {
           char c = charDizisi[i];
           toplam = toplam + c;
       }
       return toplam;
   }
}
```

## 6. Sum of digits

Write code that adds up the digits of a given number and finds the result. Example: if the number is 5689, then 5 + 6 + 8 + 9 = 28.

```java
public class BasamakToplama
{
    public static int basamaklariTopla(int girdiSayi)
    {
        int toplam=0;
        while(girdiSayi > 0)
        {
            int basamak = girdiSayi % 10;
            toplam = toplam + basamak;
            girdiSayi = girdiSayi / 10;
        }
        return toplam;
    }

   public static int basamaklariTopla(String girdiSayi)
   {
        int toplam=0;
       for(char c: girdiSayi.toCharArray())
       {
           toplam = toplam + Integer.parseInt("" +c);
       }
       return toplam;
   }
}
```

The project also contains a `BilgiAlma` class: the `DikUcgenAlanBul` method, which finds the area of a right triangle given its legs (a × b / 2), and the `MerhabaDunyaYaz` method, which prints "Merhaba, …" ("Hello, …") with the given name.
