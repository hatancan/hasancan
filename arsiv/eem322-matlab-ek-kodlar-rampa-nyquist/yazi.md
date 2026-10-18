---
baslik: EEM322 Denetim Sistemleri: Ek MATLAB Çalışmaları: Rampa, Kök Yer, Bode ve Nyquist
ozet: Öğrenci MATLAB çalışmalarının ekleri: B-5-17, B-5-31, B-8-16, kök yer örnekleri ve bağımsız kaynak dosyaları.
---

EEM322 ders klasöründe bulunan ek **MATLAB ödev çizimleri ve kaynak dosyaları**, farklı arkadaşların çalışmalarından bir araya getirildi. Özgün Word dosyalarının oluşturulma bilgileri 2004, 2007 ve 2013 yıllarına uzanıyor; derlemenin arşiv tarihi en yeni belgenin 17 Mayıs 2013 tarihine dayanıyor. Öğrenci adı taşıyan dosya adları değiştirildi; Office yazar bilgileri PDF kopyalarından çıkarıldı. PDF’ler ve MATLAB dosyaları yazının sonunda ZIP olarak indirilebilir.

## B-5-17: Üçüncü dereceden sistemin basamak yanıtı

Belgedeki model **T(s) = 10/(s³ + 6s² + 8s + 10)**. MATLAB grafiğinde tepe 1.21, aşım %21.4, tepe zamanı 2.67 s olarak işaretlenmiş.

```matlab
num=[0 0 0 10];
den=[1 6 8 10];
step(num,den)
grid
```

## B-8-16: Nyquist çizimi

Model **G(s) = (s² + 2s + 1)/(s³ + 0.2s² + s + 1)**. Belge, Nyquist eğrisinin kazanç/faz payı işaretleriyle alınmış ekran çıktısını içerir.

```matlab
num=[0 1 2 1];
den=[1 0.2 1 1];
nyquist(num,den)
grid
```

## B-5-31: Rampa yanıtında K değişimi

T(s) = K/(s² + s + K) sistemi için B = 1 sabit tutularak K = 0.5, 8 ve 50 denenir. Aynı kalıp her K değeri için çalıştırılmıştır:

```matlab
num=[0 0 0.5];
den=[1 1 0.5];
t=0:0.1:10;
r=t;
y=lsim(num,den,r,t);
plot(t,r,'-',t,y,'o')
grid
title('Ramp response for different values of K');
xlabel('t Sec')
ylabel('Output')
text(3.2,6.5,'Unit Ramp Input')
text(6.0,3.1,'Output')
```

`Rl1.m` aynı deneyi K = 150 ile tekrarlar. Grafikte çizgi giriş rampasını, daireler sistem çıkışını gösterir.

## B-6-5, B-6-9 ve B-6-12: Kök yer eğrileri

| Problem | Pay katsayıları | Payda katsayıları |
|---|---|---|
| B-6-5 | [0 0 0 0 1] | [1 4 11 14 10] |
| B-6-9 | [0 0 1 9] | [1 4 11 0] |
| B-6-12 | [0 0 0 1 1] | [1 4 11 14 10] |

Belgede `rlocus(num,den)` çağrısından sonra `axis`, `grid` ve başlık komutları uygulanır. B-6-5 ve B-6-12 paydası (s² + 2s + 2)(s² + 2s + 5) çarpanlarına ayrılır. `Rl2.m`, B-6-12 için eksenleri −10…10 aralığında ayarlayan ayrı bir dosyadır.

## Bağımsız MATLAB dosyaları

Aşağıdaki kodlar kaynaklarının içeriği korunarak aktarılmıştır. Dosyalar çalıştırılmadı; polinom tanımları ve komutların kaynakta farklı amaçlarla kullanılabildiğine dikkat edilmelidir.

### Uraz 5.4(b): polinom kökleri ve kök yer

```matlab
clc;
clear all;

p=[1 5 9 20 2];
roots(p);

num=[1 5 9 20 0];
den=[0 0 0 0 1];
rlocus(num,den);
%axis('square');
grid on;
title('Root Locus');
```

### B-6-11: polinom kökleri ve kök yer

```matlab
clc;
clear all;

p=[1 4 8 2];
roots(p);

num=[0 0 0 1];
den=    [1 4 8 0];
rlocus(num,den);
%axis('square');
grid on;
title('Root Locus');
```

### K = 150 için rampa yanıtı

```matlab
num=[0  0 150];
den=[1 1 150];
t=0:0.1:10;
r=t;
y=lsim(num,den,r,t);
plot(t,r,'-',t,y,'o')
grid 
title('Ramp response for different values of K');
xlabel('t Sec')
ylabel('Output')
text(3.2,6.5,'Unit Ramp Input')
text(6.0,3.1,'Output')
```

### B-6-12 için kök yer

```matlab
num=[0 0 0 1 1];
den=[1 4 11 14 10];
rlocus(num,den);
v=[-10 10 -10 10];
axis(v);axis('square')
grid;
title('Root-Locus Plot of G(s)=K(s+1)/[(s^2+2s+2)(s^2+2s+5)]')
```

### Uraz 6.1(d): kutupsal çizim

```matlab
num=[0 0 1 -5];
den=[1 11 10 0];
Polar(num,den)
grid
title('H(s) nin Polar çizimi')
```

### Uraz 6.1(d): Bode çizimi

```matlab
num=[0 0 1 -5];
den=[1 11 10 0];
bode(num,den)
grid
title('H(s) nin Bode çizimi')
```

### Uraz 6.2(c): Nyquist çizimi

```matlab
num=[0 0 10 10];
den=[1 -11 10 0];
nyquist(num,den)
grid
title('H(s) nin Nyquist çizimi')
```

### Ek Bode örneği

```matlab
num=[0 0 0 (0.25*3.4626)];
den=[0.25 0.25 1 0];
bode(num,den)
grid
title('G(s) nin Bode çizimi','FontWeight','bold')
```

### Ek Nyquist örneği

```matlab
num=[0 2 1];
den=[1 -1 0];
nyquist(num,den)
grid
title('G(s) nin Nyquist çizimi','FontWeight','bold')
```

### Bant geçiren sistemin Bode çizimi

```matlab
sys=tf([(4*10^8),0],[1,20001,20000])
bode(sys,'m')
```

*Not: `uraz5bs4b.m` dosyasındaki `roots(p)` polinomu sabit terimi 2 olan bir polinomdur; `rlocus` için ayrı tanımlanan payın sabit terimi 0’dır. `b6s11.m` dosyasında da `roots` polinomu ile açık döngü paydası farklıdır. Bu tanımlar birleştirilmedi veya düzeltilmedi. `Polar` çağrısının ihtiyaç duyduğu ayrı yordam arşivde bulunmuyor.*

## Ek ekran çıktısı

`Bode-Ekran-Ciktisi.pdf`, “C-D” başlığı altında bir genlik ve faz grafiğidir. Genlik önce yükselip düzleşir, sonra düşer; faz +90°’den −90°’ye geçer. Bu sayfada transfer fonksiyonu yazmadığı için tek başına grafikten bir model atanmadı.
