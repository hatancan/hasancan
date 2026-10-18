---
baslik: EEM301 Sinyaller ve Sistemler I: MATLAB Proje 1 Çözümleri ve Kutup–Frekans Denemeleri
ozet: 2006, 2008 ve 2011 ödev sürümlerinden zaman kaydırma, conv ve filter uygulamaları; sinyal.m dosyasındaki kutup ve frekans yanıtı kodu.
---

Arkadaşların hazırladığı üç MATLAB Proje 1 çözümü, kaynak belge tarihlerine göre **15 Kasım 2006, 23 Kasım 2008 ve 24 Kasım 2011** sürümleriyle bir araya getirildi. Kişisel bilgiler çıkarıldı; kapaktaki kimlik alanı maskelendi. ZIP’te temizlenmiş üç PDF ve aynı arşivdeki **sinyal.m** kaynak kodu bulunuyor. Kodlar çalıştırılmadan metin ve formüller üzerinden incelendi.

## Sinyali çizmek ve zaman dönüşümleri

Başlangıç örneği:

```matlab
nx=-3:1:7;
x=[0 0 0 2 0 1 -1 3 0 0 0];
stem(nx,x)
```

Sıfırdan farklı örnekler x[0]=2, x[2]=1, x[3]=−1 ve x[4]=3’tür. 2008 çözümünde iki örnek gecikme ve bir örnek ilerleme, örnek değerlerini koruyup çizim eksenini değiştirerek gösteriliyor:

```matlab
ny1=-1:1:9;
y1=[0 0 0 2 0 1 -1 3 0 0 0];
stem(ny1,y1)
ny2=-4:1:6;
y2=[0 0 0 2 0 1 -1 3 0 0 0];
stem(ny2,y2)
ny3=-7:1:3;
y3=[0 0 0 3 -1 1 0 2 0 0 0];
stem(ny3,y3)
```

Terslemede hem indislerin işareti hem de değerlerin sırası değişir. Kaynağın sonraki satırları şöyledir:

```matlab
ny4=-6:1:4;
y3=[0 0 0 3 -1 1 0 2 0 0 0];
stem(ny4,y4)
```

*Not: Son bölümde y4 çizdirilirken atama y3’e yapılmış; temiz çalışma alanında y4 tanımsızdır. Ayrıca ny4 ekseni, terslenmiş sinyali bir örnek sağa taşır; “Flipped and Advanced by 1” başlığıyla uyumlu değildir. 2006 sürümünde ise bazı kaydırmalarda hem dizi içindeki değerler hem indis ekseni kaydırılmış; bunun sonucu istenen kaydırmanın iki kez uygulanmasıdır.*

## İki dikdörtgen dizinin konvolüsyonu

```matlab
n=0:5;
x=[1 1 1 1 1 1];
y=conv(x,x);
ny=0:10;
stem(ny,y)
```

Çıktı:

```
1  2  3  4  5  6  5  4  3  2  1
```

İki uzunluğu 6 olan diziden uzunluğu 11 olan üçgen biçimli sonuç çıkar. İlk örnekte tek çarpım, merkezde altı çarpım katkı verir.

## Dikdörtgen ile sonlu rampanın konvolüsyonu

```matlab
n=0:5;
h=n;
x=[1 1 1 1 1 1];
y=conv(x,h);
ny=0:10;
stem(ny,y)
```

Sonuç [0,1,3,6,10,15,15,14,12,9,5]’tir. h[n+5] kullanılırsa aynı değerler −5:5 ekseninde gösterilir.

2011 sürümünde kaydırılmış grafik için şu eksen yazılmış:

```matlab
n=-5:1:0;
z=length(n);
ny=0:1:((z.*2)-2-5);
```

*Not: z=6 iken bu ny altı elemanlıdır; conv sonucu on bir elemanlıdır. İlgili grafiğin ekseni −5:5 olmalıdır. 2006 sürümündeki ilk conv örneğinde de önceki x dizisi yeniden tanımlanmadan kullanılmış; gösterilen üçgen sonuç için x’in altı birden oluşması gerekir.*

## filter ile fark denklemleri

MATLAB’ın `filter(b,a,x)` çağrısı, pay katsayılarını b, payda katsayılarını a alır. Üç sistemin 2008 belgesindeki tanımları:

```matlab
a1=[1]; b1=[0.5 1 2];
a2=[1 -0.8]; b2=[2];
a3=[1 -0.8]; b3=[0 2];
x=[1 2 3 4];
y1=filter(b1,a1,x)
y2=filter(b2,a2,x)
y3=filter(b3,a3,x)
```

| Sistem | Fark denklemi | İlk dört çıktı |
|---|---|---|
| 1 | y[n]=0,5x[n]+x[n−1]+2x[n−2] | 0,5; 2; 5,5; 9 |
| 2 | y[n]−0,8y[n−1]=2x[n] | 2; 5,6; 10,48; 16,384 |
| 3 | y[n]−0,8y[n−1]=2x[n−1] | 0; 2; 5,6; 10,48 |

2006 belgesi a ve b sırasını ters çeviren bir denemeyi de gösterir: `filter(a1,b1,x)` sonucu [2,0,−2,12] olur. Bu, aynı süzgeç değildir.

*Not: 2006 belgesinde ikinci sistem için a2=[1], b2=[0.8 2] yazıldığı hâlde yukarıdaki özyinelemeli sistemin sonuçları verilmiş. Yazılı katsayılar [0.8,3.6,6.4,9.2] üretir. 2011 belgesinde de önce a2=[1], b2=[2,0.8] yazılmış, daha sonraki hesapta a2=[1 −0.8], b2=[2] kullanılmış. İndirilen belgelerde bu çelişkiler korunmuştur.*

## İki seyrek dizinin konvolüsyonu

x[n]=δ[n]+δ[n−2], h[n]=2δ[n+1]−2δ[n−1]. Ara terimler birbirini götürür:

y[n]=2δ[n+1]−2δ[n−3].

```matlab
x=[1 0 1];
nx=0:1:2;
h=[2 0 -2];
nh=-1:1:1;
ny=-1:1:3;
y=conv(x,h);
stem(ny,y)
```

Sonuç −1:3 indislerinde [2,0,0,0,−2]’dir.

*Not: 2006 sürümünde aynı örneğin çizim ekseni 1:9 seçilmiş; dizi konumları fiziksel zaman indislerinden ayrılmıştır. Konvolüsyonun başlangıç indisi iki girişin başlangıç indislerinin toplamıdır.*

## sinyal.m: kutuplar ve frekans yanıtı

Aşağıdaki bağımsız kaynak dosya, dört ikinci dereceden transfer fonksiyonunun kutuplarını çizer; son bölümde bir ayrık zamanlı frekans yanıtı hesaplar. Öğrenci numarasıyla adlandırılmış eşdeğer kopyası yerine kişisel bilgi içermeyen **sinyal.m** adı kullanıldı.

```matlab
b1=[1]

a1=[1 0 1]
H1=tf(b1,a1)
ps1=roots(a1)
plot(real(ps1),imag(ps1),'x')
grid
axis([-3 3 -3 3])

figure;
a2=[1 0.5 1]
H2=tf(b1,a2)
ps2=roots(a2)
plot(real(ps2),imag(ps2),'x')
grid
axis([-3 3 -3 3])

figure;
a3=[1 2 1]
H3=tf(b1,a3)
ps3=roots(a3)
plot(real(ps3),imag(ps3),'x')
grid
axis([-3 3 -3 3])

figure;
a4=[1 4 1]
H4=tf(b1,a4)
ps4=roots(a4)
plot(real(ps4),imag(ps4),'x')
grid
axis([-3 3 -3 3])

figure;
bx=[0.25 -0.87 1]
ax=[1 -0.87 0.25]
HX=tf(bx,ax)
HX=freqz(bx,ax,512,'whole')
plot(HX)
```

| Payda | Kutuplar |
|---|---|
| s²+1 | ±j |
| s²+0,5s+1 | −1/4 ± j√15/4 |
| s²+2s+1 | −1, çift katlı |
| s²+4s+1 | −2±√3 |

*Not: Örnekleme zamanı verilmeden tf ile oluşturulan modeller sürekli zamanlıdır. freqz ise b ve a dizilerini ayrık zaman süzgeci katsayıları olarak yorumlar. Son iki satır HX transfer fonksiyonu değişkenini frekans yanıtı vektörüyle değiştirir; plot(HX), genliği frekansa karşı çizmek yerine karmaşık düzlemde gerçek ve sanal bileşenleri çizer.*
