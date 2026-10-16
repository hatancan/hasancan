---
baslik: EEM227 Veri Yapıları: Örnek Sorular ve Java Çözümleri
ozet: EEM227 Veri Yapıları dersinin videolarında çözülen altı örnek soru ve Java çözümleri: üç sayının en büyüğü, vize-final ile harf notu, switch ile haftanın günleri (fall-through dahil), tek-çift, sayının tersi ve basamak toplamı.
---

Bu yazı, Başkent Üniversitesi **EEM227 Veri Yapıları** dersinde (Kasım 2013) videolarda işlenen örnek soruları ve dersin "OrneklerVideo1" adlı BlueJ projesindeki Java çözümlerini bir araya getiriyor. Her soru, orijinal metin dosyasındaki hâliyle verildi; altında çözüm kodu var. Soru dosyaları ve çözüm projesi yazının sonunda tek bir ZIP olarak indirilebilir.

Kodlarda `static` metotlar kullanılıyor; BlueJ'de bir metoda sağ tıklayıp parametre girerek doğrudan çalıştırılabiliyordu, bu yüzden çoğunda `main` yok.

## 1. Girilen üç sayının en büyüğü

Girilen 3 sayının en büyüğünü ekrana yaz.

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

## 2. Vize ve final notundan harf notu

Vize notu ve final notunu alan, aşağıdaki son not formülüne göre not hesaplayıp bu notun harf hâlini döndüren kodu yazınız.

**Son Not = Vize Notu × 0,4 + Final Notu × 0,6**

| Son not | Harf |
|---|---|
| 100–90 | A |
| 89–80 | B |
| 79–70 | C |
| 69–60 | D |
| 59–0 | F (Fail) |

Girdi: vize notu (int), final notu (int). Çıktı: son harf notu (String).

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

*Not: Tabloya göre 90 A, 80 B olmalı; kod `>` kullandığı için tam sınırdaki notlar (90, 80, 70, 60) bir alt harfe düşüyor. Doğrusu `>=` olurdu.*

## 3. Switch ile haftanın günleri

Girdi: gün sayısı. Çıktı: yazı olarak haftanın günü (1 Pazartesi, 2 Salı, 3 Çarşamba, 4 Perşembe, 5 Cuma, 6 Cumartesi, 7 Pazar).

Çözümde iki sürüm var. İkincisi doğru sürüm; birincisi bilerek `break` unutulmuş, **fall-through** davranışını göstermek için yazılmış: hangi gün girilirse girilsin akış aşağıya doğru devam eder ve sonuç her zaman `"HATALI GIRIS"` olur.

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

## 4. Tek mi, çift mi?

Girilen bir sayının tek mi çift mi olduğunu bulunuz.

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

## 5. Bir sayının tersi

Girilen bir sayının tam tersini yazan kodu yazınız. Örnek girdi 12345, örnek çıktı 54321. Soru dosyasında iki yaklaşım not edilmiş: **sayı işlemleri** ve **string işlemleri**.

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

## 6. Basamakların toplamı

Verilen bir sayının basamaklarını toplayıp sonucunu bulan kodu yazınız. Örnek: sayı 5689 ise 5 + 6 + 8 + 9 = 28.

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

Projede ayrıca `BilgiAlma` sınıfı var: dik kenarları verilen dik üçgenin alanını bulan `DikUcgenAlanBul` (a × b / 2) ve verilen ada "Merhaba, …" yazan `MerhabaDunyaYaz` metotları.
