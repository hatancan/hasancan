---
baslik: EEM227 Veri Yapıları: Dizi Labı (rastgele dizi, dizi büyütme, dizi birleştirme)
ozet: EEM227 Veri Yapıları dersinin örnek dizi labı (Lab 4) Java çözümleri: rastgele uzunlukta rastgele dizi oluşturma, diziyi iki katına büyütme ve iki diziyi birleştirme. Dizi boyutu değiştirme probleminin temeli.
---

Bu yazı, Başkent Üniversitesi **EEM227 Veri Yapıları** dersinin örnek dizi labının (Lab 4, Ekim 2014) Java çözümlerini içeriyor. Kodlar hocanın verdiği iskelet üzerine kurulu: her metotta `// Sizin kodunuz buraya` yorumunun altı dolduruluyor. Konu, izlencedeki 3. haftanın "dizi boyut değiştirme problemi" (array resize problem). Orijinal BlueJ projesi yazının sonunda 7z arşivi olarak indirilebilir.

## Yardımcı sınıf: RastgeleSayi

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

`nextInt(maksimum)` 0 ile maksimum − 1 arasında bir sayı döndürür.

## Soru 1: Rastgele dizi oluşturma

Rastgele bir uzunluk (0–99) seçilir; bu uzunlukta bir dizi oluşturulup her elemanına 0 ile uzunluk − 1 arasında rastgele bir değer verilir ve dizi `{ … }` biçiminde yazdırılır.

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

*Not: `getRandomNumber(100)` 0 da döndürebilir. Uzunluk 0 çıkarsa dizi boş olur, ancak bu durumda `rastgeleDiziOlustur` içindeki `getRandomNumber(0)` hiç çağrılmadığı için program hata vermez.*

## Soru 2: Diziyi iki katına büyütme

20 elemanlı rastgele bir dizi, iki kat uzunlukta yeni bir diziye kopyalanır. Java'da dizilerin boyu sonradan değiştirilemediği için "büyütme" aslında yeni bir dizi açıp eskisini kopyalamaktır. Yeni dizinin ikinci yarısı 0 ile dolu kalır.

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

## Soru 3: İki diziyi birleştirme

İkinci dizinin elemanları, birinci dizinin uzunluğu kadar kaydırılarak sonuç dizisine yerleştirilir.

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

Çıktı:

```
{ 1 , 2 , 4 , 8 , 2 , 7 , 8 , 11 , 17 , 25 ,}
```

(`printDiziIcerik` metodu her üç sınıfta da aynı; yer kazanmak için yalnız birincide gösterildi.)
