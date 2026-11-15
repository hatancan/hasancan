---
baslik: EEM227 Data Structures: Java Lessons, HelloWorld Project
ozet: Java exercises written with BlueJ during EEM227 Data Structures (November–December 2014): Hello World, right triangle area, largest of three numbers, reversing a number (numerically and with strings), and an unfinished star pyramid.
---

This post contains the exercises from the "Java Lessons / MerhabaDunya" project, written with BlueJ during the Başkent University **EEM227 Data Structures** course (November–December 2014). The problems are the same as the example problems solved in the course videos, but the code here differs from the course solutions: these are exercises written while following the course. The original source files can be downloaded as a ZIP at the end of the post.

## Hello World

```java
public class MerhabaDunya
{
    public static void main(){
        System.out.println("Merhaba Dünya");
    }
}
```

## Area of a right triangle

```java
public class BilgiAlma
{
    public static double DikUcgenAlanBul(double DikKenarA, double DikKenarB){
        double alan = DikKenarA*DikKenarB/2;
        return alan;
    }
}
```

## Largest of three numbers

```java
public class Girilen3SayiEnBuyuk
{
   public static int enBUyukBul (int a, int b, int c){
       int enBuyuk=a;
       if(b>a){
            enBuyuk=b;
       }
       if(c>a && c>b){
           enBuyuk=c;
       }
       return enBuyuk;
   }
}
```

The course solution first compared a with b and then compared the winner with c; this version compares c with both numbers at once. Both give the correct result.

## Reversing a number

Two methods: one uses only arithmetic (mod and division), the other converts the number to a character string and reads it backwards.

```java
public class BiRSayininTersiniBulma
{
    public static int tersiniBul(int sayi){
        int ters=0;
        int kontrol=1;
        int sayac=0;
        int basamak=10;
        while(kontrol!=sayi){
            kontrol=sayi%basamak;
            sayac++;
            basamak=basamak*10;
        }
        int basamak1=1;
        int basamak2=10;
        basamak=basamak/100;
        while(sayac!=0){
            ters=ters+((((sayi%basamak2)-(sayi%basamak1))/basamak1)*basamak);
            basamak2=basamak2*10;
            basamak1=basamak1*10;
            basamak=basamak/10;
            sayac--;
        }
        return ters;
    }

    public static String SayiyiStringleTersle(String sayi){
        String ters="";
        char[] charDizisi = sayi.toCharArray();
        for (int i =charDizisi.length-1; i>=0; i--){
            char c = charDizisi[i];
            ters=ters+c;
        }
        return ters;
    }
}
```

The first loop finds how many digits the number has (by taking the mod with 10, 100, 1000, … until the remainder equals the number itself); the second loop extracts each digit one by one and multiplies it by its reversed place value.

## Star pyramid (unfinished)

```java
public class yildiz
{
   public static int piramid(int piramidKenar){
       int pk = piramidKenar;
       int satir;
       int sutun;
       int bosluk = 1;
       int i=0;
       for(satir=0;satir<pk;satir++){
           for (sutun=0; sutun<pk; sutun++){
               System.out.println(" ");
           }
           i=bosluk+i;
           while(bosluk<=i){
               System.out.println("*");
           }
       }
       i=bosluk-i;
       i++;
       System.out.println(" ");
       return pk;
   }
}
```

*Note: This code is an incomplete attempt. Because neither `bosluk` nor `i` changes inside the `while` loop, the loop runs forever; also, since `println` moves to a new line after every character, the pyramid shape is not produced. A `print` call would be needed to print on the same line, and a counter increment to exit the loop. The `__SHELL1.java` file in the project is a helper file that BlueJ generated itself to run this method with its 6 parameters.*
