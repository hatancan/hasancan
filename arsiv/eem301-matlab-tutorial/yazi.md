---
baslik: EEM301 Sinyaller ve Sistemler I: MATLAB'a Giriş, Tutorial 1 ve 2 (Başkent EEM417 föyü, Control Tutorials for MATLAB uyarlaması)
ozet: Başkent Üniversitesi EEM bölümünün iki MATLAB giriş föyü: vektör ve matris oluşturma, transpoz, matris çarpımı, inv, eig, poly, roots, polyval, conv, deconv; function ile m-dosyası yazma, plot, renk ve işaretçiler, hold, subplot, axis, title, xlabel, gtext.
---

Bu yazı, EEM301 Sinyaller ve Sistemler I klasöründe duran iki MATLAB giriş föyünü içeriyor. Föyler Başkent Üniversitesi Elektrik-Elektronik Mühendisliği Bölümü'nün **EEM 417 Denetim Sistemi Tasarımı** dersi için 2005'te hazırlanmış (**Tutorial_1** ve **Tutorial_2 – Introduction to MATLAB**); EEM301'in MATLAB ödevlerinde de kullanılmış. Metin İngilizce. Aşağıda ana başlıklar ve örnek komutlar aktarıldı. Orijinal Word dosyaları yazının sonunda ZIP olarak indirilebilir.

Föylerin metni büyük ölçüde Michigan Üniversitesi'nin **Control Tutorials for MATLAB** sitesindeki MATLAB temel bilgiler dersine dayanıyor.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Tutorial 1: MATLAB'a giriş

MATLAB, sayısal hesaplama ve veri görselleştirme için etkileşimli bir program; denetim mühendisleri tarafından analiz ve tasarımda yoğun kullanılır. Bu derslerde özellikle **Control System Toolbox** kullanılıyor: transfer fonksiyonu, sıfır-kutup-kazanç ve durum uzayı modelleri, sürekli ve ayrık zamanlı sistemler, zaman ve frekans yanıtları, kök yer eğrileri.

### Başlarken

- `intro`: MATLAB tanıtımı; `helpdesk`: belgeler; `demo`: örnekler
- `help`, `help plot`, `lookfor filter` (anahtar sözcük araması)
- `clc` (komut penceresini temizler), `clear` (değişkenleri siler), `close` (şekli kapatır)
- `more on`: çıktıyı ekran ekran gösterir

> When unsure about a command, use help

Bir değişkenin adını yazmak değerini gösterir; atanmamış sonuçlar `ans` değişkeninde tutulur. Bir satırda birden çok komut noktalı virgül ya da virgülle ayrılabilir.

### Sayı gösterimi

MATLAB'ın gösterebildiği sayılar yaklaşık 10⁻³⁰⁸ ile 10³⁰⁸ arasındadır. Şu gösterimlerin hepsi aynı sayıdır (üsten önce boşluk olmamalı):

```matlab
12345.6789
123456.789e-1
1234.56789E1
12.3456789e3
1234567.89E-2
```

### Diziler: vektörler ve matrisler

```matlab
a = [1 2 3 4 5]      % vektör
t = 0:2:20           % 0'dan 20'ye 2'şer artan zaman vektörü
b = a + 2            % her elemana 2 ekler: 3 4 5 6 7
c = a + b            % aynı uzunlukta vektörlerin toplamı
B = [1 2 3 4; 5 6 7 8; 9 10 11 12];   % 3x4 matris
size(B)              % 3 4
length(a)            % 5
C = B'               % transpoz (karmaşıkta eşlenik transpoz; yalın transpoz için .')
D = B * C            % matris çarpımı (sıra önemli)
```

MATLAB'da indis 1'den başlar; B(1,1) ilk satırın ilk elemanıdır.

Eleman eleman işlemler ve matris fonksiyonları:

```matlab
E = [1 2;3 4]
F = [2 3;4 5]
G = E .* F     % [2 6; 12 20]
E^3            % [37 54; 81 118]
E.^3           % [1 8; 27 64]
X = inv(E)     % [-2 1; 1.5 -0.5]
eig(E)         % -0.3723, 5.3723
p = poly(E)    % karakteristik polinom: 1 -5 -2
roots(p)       % 5.3723, -0.3723 (özdeğerlerle aynı)
```

### Polinomlar

Polinom, katsayılarının azalan derece sırasıyla yazıldığı bir vektördür. s⁴ + 3s³ − 15s² − 2s + 9 için `x = [1 3 -15 -2 9]`; eksik terimler sıfırla doldurulur, örneğin s⁴ + 1 için `y = [1 0 0 0 1]`.

```matlab
z = polyval([1 0 0 0 1],2)   % s = 2'de değer: 17
roots([1 3 -15 -2 9])        % -5.5745, 2.5836, -0.7951, 0.7860
x = [1 2];
y = [1 4 8];
z = conv(x,y)                % çarpım: 1 6 16 16
[xx, R] = deconv(z,y)        % bölme: xx = 1 2, kalan R = 0 0 0 0
```

## Tutorial 2: Fonksiyonlar ve grafik çizimi

### Fonksiyonlar

MATLAB'da `sin`, `cos`, `log`, `exp`, `sqrt` gibi standart fonksiyonlar ve `pi`, `i`, `j` sabitleri hazırdır; `sin(pi/4)` sonucu 0.7071'dir. `roots`, `plot`, `step` gibi komutlar aslında girdisi ve çıktısı olan m-dosyalarıdır. Kendi fonksiyonunuzu `.m` uzantılı bir dosyada `function` ile yazarsınız; ilk satır şu biçimdedir:

```matlab
function [output1,output2] = filename(input1,input2,input3)
```

Sonraki `%` ile başlayan satırlar `help filename` ile görünen açıklamadır. Girdi sayısını denetlemek için `error(nargchk(x,y,nargin));` satırı önerilir. Basit bir örnek, `add.m`:

```matlab
function [var3] = add(var1,var2)
%add is a function that adds two numbers
var3 = var1+var2;
```

Komut satırında `y = add(3,8)` ile kullanılır.

### Grafik çizimi

`plot(x,y)`, x vektörünü yatay, y vektörünü dikey eksende çizer; x ve y aynı uzunlukta olmalıdır. Tek vektör verilirse elemanlar indislerine karşı çizilir; karmaşık sayılarda gerçel kısım yatay, sanal kısım dikey eksene gelir.

```matlab
t=0:0.25:7;
y = sin(t);
plot(t,y)

x = 0:0.1:100;
y = 3*x;
plot(x,y,'r:')    % kırmızı, noktalı çizgi
```

Üçüncü parametre renk ve işaretçi belirler:

| Renk | İşaretçi | Çizgi |
|---|---|---|
| y sarı, m eflatun, c camgöbeği, r kırmızı | . nokta, o daire, x çarpı, + artı, * yıldız | - düz |
| g yeşil, b mavi, w beyaz, k siyah | s kare, d elmas, v ^ < > üçgenler | : noktalı, -. çizgi-nokta |
| | p beşgen yıldız, h altıgen yıldız | -- kesikli |

Aynı eksende birden çok eğri:

```matlab
x = linspace(0,2*pi,50);
y = sin(x);
z = cos(x);
plot(x,y,'r', x,z,'gx')

% ya da hold on / hold off ile:
plot(x,y,'r')
hold on
plot(x,z,'gx')
hold off
```

### subplot

`subplot(m,n,p)` şekli m satır ve n sütunluk bir ızgaraya böler ve p'inci grafiği etkin yapar; sıralama kitap okur gibi soldan sağa, yukarıdan aşağıdır.

```matlab
x = linspace(0,2*pi,50);
y = sin(x);
z = cos(x);
w = tan(x);

subplot(2,2,1)
plot(x,y)
subplot(2,2,2)
plot(x,z)
subplot(2,2,3)
plot(x,w)
```

Sonraki her `plot` komutu en son kullanılan alt grafiğin üzerine çizer; bunu önlemek için `clf` ya da `figure` kullanılır.

### Eksenler ve yazılar

`axis([xmin, xmax, ymin, ymax])` görüntülenen eksen aralığını değiştirir. Örneğin y = e^(5t) − 1 grafiği 0–5 s aralığında 8·10¹⁰ mertebesine çıktığından ilk saniyeye bakmak daha anlamlıdır:

```matlab
t=0:0.01:5;
y=exp(5*t)-1;
plot(t,y)
axis([0, 1, 0, 50])
title('exponential function')
xlabel('time (sec)')
ylabel('output')
gtext('unnecessary labeling')   % fareyle tıklanan yere yazı koyar
```

`text(xcor,ycor,'textstring')` yazıyı verilen koordinata koyar. Diğer yararlı komutlar: `clf`, `figure`, `close`, `loglog`, `semilogx`, `semilogy`, `grid`.
