---
baslik: EEM227 Veri Yapıları: Java Dersleri, MerhabaDunya Projesi
ozet: EEM227 Veri Yapıları döneminde BlueJ ile yazılmış Java alıştırmaları (Kasım–Aralık 2014): Merhaba Dünya, dik üçgen alanı, üç sayının en büyüğü, bir sayının tersi (sayısal ve string yöntemle) ve yarım kalmış yıldız piramidi.
---

Bu yazı, Başkent Üniversitesi **EEM227 Veri Yapıları** dersi döneminde (Kasım–Aralık 2014) BlueJ ile yazılmış "Java Dersleri / MerhabaDunya" projesindeki alıştırmaları içeriyor. Sorular dersin videolarında çözülen örnek sorularla aynı, ancak buradaki kodlar dersin çözümlerinden farklı: dersi takip ederken yazılmış alıştırmalar. Orijinal kaynak dosyalar yazının sonunda ZIP olarak indirilebilir.

## Merhaba Dünya

```java
public class MerhabaDunya
{
    public static void main(){
        System.out.println("Merhaba Dünya");
    }
}
```

## Dik üçgenin alanı

```java
public class BilgiAlma
{
    public static double DikUcgenAlanBul(double DikKenarA, double DikKenarB){
        double alan = DikKenarA*DikKenarB/2;
        return alan;
    }
}
```

## Üç sayının en büyüğü

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

Dersin çözümü önce a ile b'yi karşılaştırıp sonra kazananı c ile karşılaştırıyordu; bu sürüm ise c'yi iki sayıyla birden karşılaştırıyor. İkisi de doğru sonucu verir.

## Bir sayının tersi

İki yöntem: biri yalnızca aritmetikle (mod ve bölme), diğeri sayıyı karakter dizisine çevirip tersten okuyarak.

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

İlk döngü sayının kaç basamaklı olduğunu buluyor (sayının kendisine eşit kalan elde edilene kadar 10, 100, 1000 … ile mod alarak); ikinci döngü her basamağı tek tek ayıklayıp ters basamak değeriyle çarpıyor.

## Yıldız piramidi (yarım kalmış)

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

*Not: Bu kod tamamlanmamış bir deneme. `while` döngüsünde ne `bosluk` ne `i` değiştiği için döngü sonsuza kadar sürer; ayrıca `println` her karakterden sonra alt satıra geçtiği için piramit şekli oluşmaz. Satır içinde yazdırmak için `print`, döngüden çıkmak için de sayaç artırımı gerekirdi. Projedeki `__SHELL1.java`, BlueJ'in bu metodu 6 parametresiyle çalıştırmak için kendi ürettiği yardımcı dosya.*
