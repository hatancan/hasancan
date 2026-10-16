---
baslik: EEM227 Veri Yapıları: Java'da Döngü Mantığı (while, do-while, for, break, continue)
ozet: EEM227 Veri Yapıları dersinin döngüler videosundaki Java örnekleri: 1'den 10'a toplamı elle, while, do-while ve for ile bulmak; çift sayıların toplamı, continue ve break, karekökü tamsayı olan sayılar ve iç içe döngüyle yıldız üçgeni.
---

Bu yazı, Başkent Üniversitesi **EEM227 Veri Yapıları** dersinde (Kasım 2013) döngüler konusunun işlendiği videonun soru listesini ve "Donguler" adlı BlueJ projesindeki Java kodlarını bir araya getiriyor. Aynı problem (1'den 10'a kadar toplam) önce döngüsüz, sonra üç farklı döngüyle çözülüyor; ardından `continue`, `break` ve iç içe döngüler geliyor. Orijinal dosyalar yazının sonunda ZIP olarak indirilebilir.

## Soru listesi

Videoda işlenen konular, orijinal metin dosyasındaki sırasıyla:

- Döngü mantığı: 1..10 toplamı; while, do while, for
- 1..10 çift sayıların toplamı
- 1..100 arasında karekökü tamsayı olan sayıları toplama (4 → 2, 9 → 3, 16 → 4 …)
- continue, break
- İç içe döngüler: yıldızlarla üçgen

```
*
**
***
****
*****
******
```

## Döngüsüz: neden döngüye ihtiyaç var?

İlk örnek, 1 + 2 + … + 10 = 55 toplamını hiç döngü kullanmadan yazıyor. Aynı iki satırın on kez tekrarlandığını görmek, döngünün neden gerektiğini anlatmanın en kısa yolu.

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
        // ... aynı iki satır 10'a kadar sürüyor ...
        a = a+1; // 10
        toplam = toplam +a; // 10

        System.out.println("toplam = " + toplam);
    }
}
```

## while, do-while ve for

```java
public class DonguMantigiWhileLoop
{
    public static void main()
    {
        int toplam = 0;
        int a = 1;
        while(a <=10)
        {
            // kontrol ifadesi doğru olduğu sürece çalışır.
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
            // en az bir kere olmak üzere
            // kontrol doğru olduğu sürece
            // çalışır.
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

Üçünün de çıktısı aynı:

```
toplam = 55
```

## Çift sayıların toplamı: iki yol

Birinci yol sayacı ikişer artırıyor; ikinci yol her sayıya bakıp tek olanları `continue` ile atlıyor.

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

## Karekökü tamsayı olan sayılar

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

*Not: Soru karekökü tamsayı olan sayıları (1, 4, 9, …, 100) toplamayı istiyor, toplamları 385. Kod ise `continue` ile tam kareleri atlıyor; yani tam kare olmayanları topluyor ve 5050 − 385 = 4665 yazıyor. Sorunun istediği sonuç için `if` koşulunun tersi (`a*a != sayi`) kullanılmalı.*

## break ile döngüden çıkmak

Toplam 100'ü geçtiği anda döngü 1000'e kadar gitmeden kesiliyor.

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

1'den 13'e kadar toplam 91; 14 eklenince 105 olur ve bir sonraki adımda döngü kırılır.

## İç içe döngüler: yıldız üçgeni

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

Dış döngü `i < 10` olduğu için üçgen 9 satır çıkar; i'nci satırda i tane yıldız vardır.
