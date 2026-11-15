---
baslik: EEM227 Data Structures: Loop Logic in Java (while, do-while, for, break, continue)
ozet: Java examples from the loops video of the EEM227 Data Structures course: finding the sum from 1 to 10 by hand, with while, with do-while, and with for; the sum of even numbers, continue and break, numbers whose square root is an integer, and a triangle of stars with nested loops.
---

This post brings together the question list of the video in which loops were covered in the Başkent University **EEM227 Data Structures** course (November 2013) and the Java code from the BlueJ project named "Donguler" (Loops). The same problem (the sum from 1 to 10) is solved first without a loop, then with three different loops; `continue`, `break`, and nested loops follow. The original files can be downloaded as a ZIP at the end of the post.

## Question list

The topics covered in the video, in the order of the original text file:

- Loop logic: the sum of 1..10; while, do while, for
- The sum of the even numbers in 1..10
- Summing the numbers between 1..100 whose square root is an integer (4 → 2, 9 → 3, 16 → 4 …)
- continue, break
- Nested loops: a triangle made of stars

```
*
**
***
****
*****
******
```

## Without a loop: why do we need loops?

The first example writes the sum 1 + 2 + … + 10 = 55 without using any loop. Seeing the same two lines repeated ten times is the shortest way to explain why a loop is needed.

```java
public class DonguMantigi
{
    public static void main()
    {
        // toplam = 1+2+3+4+5+6+7+8+9+10 = 55
        int toplam = 0;
        int a = 1;
        toplam = toplam +a; // 1
        a = a+1; // 2
        toplam = toplam +a; // 2
        a = a+1; // 3
        toplam = toplam +a; // 3
        // ... the same two lines continue up to 10 ...
        a = a+1; // 10
        toplam = toplam +a; // 10

        System.out.println("toplam = " + toplam);
    }
}
```

## while, do-while, and for

```java
public class DonguMantigiWhileLoop
{
    public static void main()
    {
        int toplam = 0;
        int a = 1;
        while(a <=10)
        {
            // runs as long as the control expression is true.
            toplam = toplam +a;
            a = a+1;
        }
        System.out.println("toplam = " + toplam);
    }
}
```

```java
public class DonguMantigiDoWhileLoop
{
    public static void main()
    {
        int toplam = 0;
        int a = 1;
        do
        {
            toplam = toplam +a;
            a = a+1;
            // runs at least once,
            // and then as long as the
            // control expression is true.
        }while(a <=10);
        System.out.println("toplam = " + toplam);
    }
}
```

```java
public class DonguMantigiForLoop
{
    public static void main()
    {
        int toplam = 0;
        for(int a=1;a <=10;a = a+1)
        {
            toplam = toplam +a;
        }
        System.out.println("toplam = " + toplam);
    }
}
```

All three produce the same output:

```
toplam = 55
```

## Sum of even numbers: two approaches

The first approach increments the counter by two; the second looks at every number and skips the odd ones with `continue`.

```java
public class DonguCiftSayilarToplam
{
    public static void main()
    {
        int toplam = 0;
        for(int a=2;a <=10;a = a+2)
        {
            toplam = toplam +a;
        }
        System.out.println("toplam = " + toplam);
    }
}
```

```java
public class DonguCiftSayilarContinue
{
    public static void main()
    {
        int toplam = 0;
        for(int a=1;a <=10;a = a+1)
        {
            if (a %2 == 1)
            {
                continue;
            }
            toplam = toplam +a;
        }
        System.out.println("toplam = " + toplam);
    }
}
```

```
toplam = 30
```

## Numbers whose square root is an integer

```java
public class DonguKarekokTamsayiOlanlariToplama
{
    public static void main()
    {
        int toplam = 0;
        for(int sayi=1;sayi <=100;sayi = sayi+1)
        {
            int a = (int)Math.sqrt(sayi);
            if (a*a == sayi)
            {
                continue;
            }
            toplam = toplam +sayi;
        }
        System.out.println("toplam = " + toplam);
    }
}
```

*Note: The question asks for the sum of the numbers whose square root is an integer (1, 4, 9, …, 100), which is 385. The code, however, skips the perfect squares with `continue`; that is, it sums the numbers that are not perfect squares and prints 5050 − 385 = 4665. To get the result the question asks for, the opposite of the `if` condition (`a*a != sayi`) should be used.*

## Exiting a loop with break

As soon as the total exceeds 100, the loop is cut short instead of running all the way to 1000.

```java
public class BreakOrnek1
{
    public static void main()
    {
        int toplam = 0;
        for(int a=1;a <=1000;a = a+1)
        {
            if (toplam > 100)
            {
                break;
            }
            toplam = toplam +a;
        }
        System.out.println("toplam = " + toplam);
    }
}
```

```
toplam = 105
```

The sum from 1 to 13 is 91; adding 14 makes it 105, and the loop is broken at the next step.

## Nested loops: a triangle of stars

```java
public class IcIceDongu1UcgenYildiz
{
    public static void main()
    {
        for(int i=1;i<10;i++)
        {
            for(int j=1;j<=i;j++)
            {
                System.out.print("*");
            }
            System.out.println("");
        }
    }
}
```

Because the outer loop has `i < 10`, the triangle has 9 rows; row i has i stars.
