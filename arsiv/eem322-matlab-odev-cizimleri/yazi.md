---
baslik: EEM322 Denetim Sistemleri: MATLAB Ödevleri 2005–2013 – Kök Yer, Bode ve Nyquist Çizimleri, margin ve step Komutları
ozet: EEM322 MATLAB projesi için farklı yıllardan öğrenci çalışmaları: Ogata B-6 kök yer eğrileri (rlocus), B-8-29 ve B-8-30 Bode diyagramları, Uraz 6.2(a) ve 6.4(a) Nyquist çizimleri, HW+MATPRO 12 için margin çıktısı ve step, bode, rlocus kullanımını anlatan yardım notu.
---

Bu yazı, Başkent Üniversitesi **EEM322 Denetim Sistemleri** dersinin **MATLAB projesi** için hazırlanmış Word belgelerini bir araya getiriyor. Belgeler 2005–2013 yılları arasında farklı öğrencilerin elinden çıkma. Kişisel bilgiler (ad, numara, belge yazar bilgisi) çıkarıldı: her belge sayfa görüntülerinden yeniden PDF'e çevrildi, ad ve numara içeren kapak satırı kapatıldı, dosya adları yıl ve problem numarasıyla değiştirildi. Belgelerin hepsi yazının sonundaki ZIP dosyasında.

Derste her öğrenciye Ogata'nın *Modern Control Engineering* kitabından ve Uraz'ın *Control Systems* kitabından problemler veriliyordu. MATLAB projesinde bu problemlerin çözüm adımları için MATLAB kodu ve bütün zaman yanıtı, kök yer, Bode ve Nyquist çizimleri isteniyordu (ödev dağılımı [izlence yazısında](/arsiv/eem322-izlence/)). 2012'den itibaren ödev tek bir parametreli sistem üzerinden verilmeye başlanmış ([HW+MATPRO](/arsiv/eem322-odev-cozumleri-hw-matpro/)).

## MATLAB yardım notu (2004–2005)

Öğrenciler arasında dolaşan "EEM322 ödev yardımı" belgesi, üç temel komutun kullanımını özetliyor. Basamak fonksiyonu girişin t = 0'da sıfırdan sonlu bir değere geçmesi; `step` komutu varsayılan olarak birim basamak yanıtını çiziyor.

Örnek 1, durum uzayı modelinin basamak yanıtı:

```matlab
A = [0 1 ; 0 -.05];
B = [0 ; 0.001];
C = [0 1];
D = [ 0];
sys = ss(A,B,C,D);
step(sys); % zaman ekseni belirlenmemiştir; ikinci örnekte olduğu gibi t vektörü tanımlanarak
           % ve step(sys,t) komutu ile zaman aralığı ve değişimi ayarlanabilir.
title('Birim Basamak Yaniti');
xlabel(' Time');
ylabel(' y(t) ');
grid on;
```

Örnek 2, kapalı çevrim aktarım işlevi T(s) = (s + 1)/(2s² + s + 3):

```matlab
num=[1 1];
den=[2 1 3];
t=0:0.1:50; % zaman vektörü: başlangıç 0, adım 0.1, bitiş 50
y=tf(num,den);
step(y,t);
title('Birim Basamak Yanıtı');
xlabel(' Time');
ylabel(' y(t) ');
grid on;
```

Bode ve kök yer eğrisi için kullanıcıdan pay ve payda isteyen kısa betikler:

```matlab
num=input(' Açık Döngü Transfer Fonksiyonun Payını Girin: ');
den=input(' Açık Döngü Transfer Fonksiyonun Paydasını Girin: ');
bode(num, den);
grid on;
```

```matlab
num=input(' Açık Döngü Transfer Fonksiyonun Payını Girin: ');
den=input(' Açık Döngü Transfer Fonksiyonun Paydasını Girin: ');
rlocus(num, den);
```

## Ogata B-6 kök yer eğrileri (2005)

Mayıs 2005 tarihli iki belgede Ogata 6. bölüm problemleri için kök yer eğrileri `rlocus` ile hesaplanıp `plot` ile işaretli çizilmiş. K, 0'dan 1000'e 0.2 adımla taranıyor:

```matlab
% Soru 6-8
num=[0 0 1 0.5]
den=[1 1 0 1]
K=[0:0.2:1000]
r=rlocus(num,den,K)
plot(r,'o')
v=[-5 1 -8 8]; axis(v)
grid
title('Root-Locus Plot of problem 6-8')
xlabel('Real Axis')
ylabel('Imag Axis')
```

Aynı kalıp B-6-10 için `num=[0 0 0 2 2]`, `den=[1 7 10 0 0]` (yani 2(s + 1)/[s²(s + 2)(s + 5)], eksen [−5 5 −10 10]) ve B-6-12 için `num=[0 0 0 1 1]`, `den=[1 4 11 14 10]` (eksen [−5 1 −5 5]) ile tekrarlanmış. B-6-10'un ayrı bir belgesinde yalnızca `rlocus(num,den)` kullanılmış.

## 2006: Uraz 5.6(b), 5.6(d) ve Ogata B-5 problemleri

Bir öğrencinin "EEM322 HW – MATLAB" belgesinde her problem için sırasıyla kök yer, basamak yanıtı, Nyquist ve Bode çizimleri var. Bode çizimlerinde MATLAB'ın veri imleciyle okunan noktalar:

| Problem | Okunan genlik noktası | Okunan faz noktası |
|---|---|---|
| Uraz 5.6(b) | 0.491 rad/s'de 30.7 dB | 0.493 rad/s'de −109° |
| Uraz 5.6(d) | 2.97 rad/s'de −28.2 dB | 2.96 rad/s'de −148° |
| Ogata B-5-26 (K = 1) | 4.25 rad/s'de −27.9 dB | 4.24 rad/s'de −36.2° |
| Ogata B-5-13 | 0.56 rad/s'de −6.51 dB | 0.559 rad/s'de 18.4° |
| Ogata B-5-27(a) | 2.56 rad/s'de −4.28 dB | 2.56 rad/s'de −180° |
| Ogata B-5-27(b) | 2.55 rad/s'de −8.69 dB | 2.55 rad/s'de −180° |

B-5-13 için birim dürtü, birim basamak ve birim rampa yanıtları ayrı ayrı çizilmiş. 2008 tarihli başka bir belge (5.4(d) ve 5.6(h) başlıklı) aynı çizimlerin kopyası olduğu için arşive eklenmedi.

Aynı yıldan ikinci bir "Matlab Ödevi" belgesinde Ogata B-8-29 ve Uraz 6.4(a) için kök yer, Nyquist, Bode ve basamak yanıtı var. B-8-29'un Bode çiziminde 0.645 rad/s'de −0.0144 dB (kazanç kesimi) ve 41.5 rad/s'de −179° (faz kesimi civarı), Uraz 6.4(a)'da 0.866 rad/s'de 0.0533 dB ve 0.925 rad/s'de −317° okunmuş.

## 2007: Kök yer, Bode ve Nyquist çizimleri

Uraz B.6.2 ve B.6.3 için kök yer eğrileri (belgede "Yapamadığım sorunun yerine Ogata'dan B.6.2'yi yaptım" notu var):

```matlab
>> num=[0 1 4];
>> den=[1 2 1];
>> g=tf(num,den)

Transfer function:
    s+4
-------------
s^2 + 2 s + 1

>> rlocus(g)
```

```matlab
>> numm=[0 0 0 0 1];
>> denn=[1 5 9 5 0];
>> f=tf(numm,denn)

Transfer function:
           1
-------------------------
s^4 + 5 s^3 + 9 s^2 + 5 s

>> rlocus(f)
```

Ogata B-8-29 ve B-8-30'un Bode diyagramlarında MATLAB'ın kararlılık payı imleçleri kullanılmış:

| Problem | Kazanç payı | Faz payı | Not |
|---|---|---|---|
| Ogata B-8-29 | 1.26 dB (2 rad/s) | 50.8° (1.48 rad/s), gecikme payı 0.6 s | Kapalı çevrim kararlı |
| Ogata B-8-30 | – | 84.2° (0.673 rad/s), gecikme payı 2.18 s | Kapalı çevrim kararlı |

Uraz 6.2(a)'nın Nyquist çiziminde kazanç payı −14 dB (0 rad/s'de), faz payı 22.8° (2.1 rad/s'de, gecikme payı 0.189 s) okunmuş ve kapalı çevrimin kararlı olduğu gösterilmiş.

## 2008: Üç K değeri için Bode ve Nyquist

İki sayfalık bir belgede aynı sistemin K = 0.2, 0.5 ve 2 için Bode ve Nyquist çizimleri üst üste verilmiş. Bode'da genlik eğrileri K ile yukarı kayarken faz eğrisi −180°'den −90°'ye çıkan tek bir eğri ("K değerleri tüm faz eğrileri için aynı"). Nyquist'te eğriler gerçek eksende −0.8, −2 ve −8 noktalarından başlayıp orijine yarım daire çizerek ilerliyor; yani çizilen sistemin sıfır frekans kazancı −4K.

## 2012–2013: HW+MATPRO 12

Son iki belge HW+MATPRO ödevinin 12 numaralı parametre setine ait (n = 1, a = 1, b = 3, c = 4, d = 16): G(s) = (s + 1)/[s(s + 3)(s² + 4s + 16)] = (s + 1)/(s⁴ + 7s³ + 28s² + 48s).

```matlab
sys=tf([1,1],[1,7,28,48,0])
rlocusplot(sys)
bode(sys)
stepplot(sys)
figure,nyquist(sys)
[Gm,Pm,Wg,Wp] = margin(sys)
```

```
Gm = 113.5587

Pm = 90.4973

Wg = 4.8041

Wp = 0.0208
```

`margin` çıktısında Gm mutlak değer (20 log 113.56 ≈ 41.1 dB), Wg faz kesim frekansı (faz −180° olduğu yer), Wp kazanç kesim frekansı. Faz −180°'yi 4.80 rad/s'de kesiyor ve orada |G| ≈ 1/113.6; kazanç düşük frekanslarda |G| ≈ 1/(48ω) olduğundan 0.0208 rad/s'de 1'e iniyor. Belgelerde Bode, Nyquist (dB çemberli), kök yer ve basamak yanıtı çizimleri var. Basamak yanıtı açık çevrim G(s) için çizildiği için (orijinde kutup var) rampa gibi sürekli artıyor.

*Not: Hesap kontrol edildi: ω = 4.804 rad/s'de G(jω)'nın fazı −180° ve 1/|G| = 113.57.*
