---
baslik: EEM227 Data Structures: Array Lab (random array, array growth, array concatenation)
ozet: Java solutions for the sample array lab (Lab 4) of the EEM227 Data Structures course: creating a random array of random length, doubling the size of an array, and concatenating two arrays. The basis of the array resizing problem.
---

This post contains the Java solutions of the sample array lab (Lab 4, October 2014) of the **EEM227 Data Structures** course at Başkent University. The code is built on the skeleton provided by the instructor: in each method, the code goes below the `// Sizin kodunuz buraya` comment. The topic is the "array resize problem" from week 3 of the syllabus. The original BlueJ project can be downloaded as a 7z archive at the end of the post.

## Helper class: RastgeleSayi

```java
import java.util.Random;

public class RastgeleSayi
{
    public static int getRandomNumber( int maksimum)
    {
        Random randomGenerator = new Random() ;
        return randomGenerator.nextInt (maksimum);
    }
}
```

`nextInt(maksimum)` returns a number between 0 and maksimum − 1.

## Question 1: Creating a random array

A random length (0–99) is chosen; an array of this length is created, each element is assigned a random value between 0 and length − 1, and the array is printed in the form `{ … }`.

```java
public class Lab4Soru1
{
    public static void main()
    {
        int uzunluk =  RastgeleSayi.getRandomNumber(100);
        int[] diziSonuc = rastgeleDiziOlustur (uzunluk);
        printDiziIcerik ( diziSonuc ) ;
    }

    public static void printDiziIcerik ( int [ ] dizi )
    {
        System.out.print("{") ;
        for ( int a : dizi )
        {
        System.out.print(" " + a + " ,") ;
        }
        System.out.println("}") ;
    }

    public static int [] rastgeleDiziOlustur ( int pUzunluk)
    {
        int[] sonucDizisi = new int[pUzunluk];
        // Sizin kodunuz buraya
        for(int i=0;i<sonucDizisi.length;i++)
        {
            sonucDizisi[i] = RastgeleSayi.getRandomNumber(pUzunluk);
        }
        return sonucDizisi ;
    }
}
```

*Note: `getRandomNumber(100)` can also return 0. If the length turns out to be 0, the array is empty, but in that case `getRandomNumber(0)` inside `rastgeleDiziOlustur` is never called, so the program does not throw an error.*

## Question 2: Doubling the size of an array

A random array of 20 elements is copied into a new array of twice the length. Since the length of an array cannot be changed afterwards in Java, "growing" actually means creating a new array and copying the old one into it. The second half of the new array remains filled with 0.

```java
public class Lab4Soru2
{
    public static void main()
    {
        int [] dizi1 = Lab4Soru1.rastgeleDiziOlustur(20);
        int [] diziSonuc = diziBuyut ( dizi1 ) ;
        printDiziIcerik ( diziSonuc ) ;
    }

    public static int [ ] diziBuyut ( int [ ] dizi )
    {
        int [ ] sonucDizisi = new int[dizi.length*2];
        // Sizin kodunuz buraya
        for(int i=0;i<dizi.length;i++)
        {
            sonucDizisi[i] = dizi[i];
        }
        return sonucDizisi ;
    }
}
```

## Question 3: Concatenating two arrays

The elements of the second array are placed into the result array, shifted by the length of the first array.

```java
public class Lab4Soru3DiziBirlestirme
{
    public static void main()
    {
        int [ ] dizi1 = {1 ,2 ,4 ,8};
        int [ ] dizi2= {2 ,7 ,8 ,11 ,17 ,25};
        int [ ] diziSonuc = diziBirlestir( dizi1 , dizi2 ) ;
        printDiziIcerik ( diziSonuc ) ;
    }

    public static int[] diziBirlestir( int[] diziBaslangic , int[] diziSon )
    {
        int [ ] sonucDizisi = new int[diziBaslangic.length + diziSon.length];
        // Sizin kodunuz buraya
        for(int i=0;i<diziBaslangic.length;i++)
        {
            sonucDizisi[i] = diziBaslangic[i];
        }
        for(int i=0;i<diziSon.length;i++)
        {
            int yeniIndex = i + diziBaslangic.length;
            sonucDizisi[yeniIndex] = diziSon[i];
        }
        return sonucDizisi ;
    }
}
```

Output:

```
{ 1 , 2 , 4 , 8 , 2 , 7 , 8 , 11 , 17 , 25 ,}
```

(The `printDiziIcerik` method is the same in all three classes; it is shown only in the first one to save space.)
