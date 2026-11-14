---
baslik: BIL437 Bilgisayarlı Görü: MATLAB Giriş Föyü, Renkli Görüntü ve FFT-Gürültü Laboratuvarları, Programlama Ödevi 1
ozet: BIL437 Bilgisayarlı Görü dersinin MATLAB'a giriş föyü, renkli görüntü işleme ve frekans uzayında süzgeçleme/gürültü laboratuvar kodları, görüntü küçültme ve logaritmik/üstel dönüşüm içeren programlama ödevi ile artı işareti bulma kodu.
---

2015 yaz okulundaki **BIL437 Bilgisayarlı Görü** (laboratuvar föylerinin başlığına göre "BİL421 İmge İşleme" ile ortak içerik) dersinde kullanılan uygulama malzemeleri: bir MATLAB giriş föyü, iki laboratuvar föyü, programlama ödevi ve benim yazdığım küçük bir kod. Orijinal dosyalar yazının sonunda ZIP olarak indirilebilir. Laboratuvar föyleri ve ödev dersin öğretim elemanının malzemesidir; MATLAB giriş föyünün yazarı belirtilmemiştir (Kermit Sigmon'un "MATLAB Primer" metnine dayanıyor görünüyor).

## MATLAB giriş föyü (437L1.pdf, 8 sayfa)

Föy, MATLAB'ı 18 başlıkta tanıtır:

1. MATLAB'a erişim.
2. Matris girişi: `A = [1 2 3; 4 5 6; 7 8 9]`, karmaşık sayılar (`1+5i`), `rand(n)`, `magic(n)`; `A(2,3)` ikinci satır üçüncü sütun.
3. Matris ve dizi (eleman eleman) işlemleri: `+ - * ^ ' \ /`; nokta ile `.*`, `.^` eleman eleman çalışır (`[1,2,3,4].^2` → `[1,4,9,16]`). `x = A\b`, Ax = b'nin çözümüdür.
4. İfadeler, değişkenler, oturumu kaydetme (`who`, `whos`, `clear`, `save`, `load`, `eps`).
5. Matris üreten fonksiyonlar: `eye, zeros, ones, diag, triu, tril, rand, hilb, magic, toeplitz`.
6. `for`, `while`, `if` ve ilişkisel/mantıksal işleçler (`<, >, <=, >=, ==, ~=, &, |, ~`).
7. Skaler fonksiyonlar (`sin, cos, exp, log, abs, round, floor, ceil, rem, sign, sqrt`).
8. Vektör fonksiyonları (`max, min, sort, sum, prod, mean, median, std, any, all`) sütun sütun çalışır; matrisin en büyük elemanı `max(max(A))`.
9. Matris fonksiyonları (`eig, chol, svd, inv, lu, qr, det, rank, norm, cond, expm` …).
10. Komut satırı düzenleme ve geri çağırma (ok tuşları).
11. Alt matrisler ve iki nokta gösterimi: `1:5`, `0.2:0.2:1.2`, `A(:,3)`, `A(1:4,:)`, `A(:,[2 4]) = …`.
12. M-dosyaları ve fonksiyon dosyaları; örnek:

```matlab
function a = randint(m,n,a,b)
%RANDINT Randomly generated integral matrix.
if nargin < 3, a = 0 ; b = 9 ; end
a = floor((b-a+1)*rand(m,n)) + a;
```

13. Metin dizgeleri, `disp`, `error`, `input`.
16. Çıktı biçimi: `format short`, `format long`, `format rat` …
18. Grafikler: `plot`, `plot3`, `mesh`, `surf`; başlık/eksen komutları (`title`, `xlabel`, `ylabel`, `axis`), `hold on`, çizgi tipleri, işaret tipleri ve renk kodları (`plot(x,y,'r--')`).

## Laboratuvar 1: renkli görüntü işleme (lab_color.pdf)

Altı alıştırmayı `peppers.png` görüntüsü üzerinde yapar:

1. **RGB – HSV**: `hsv2rgb`/`rgb2hsv` ile H (renk), S (renk miktarı) ve V (şiddet) bileşenlerini göster.
2. **Gri seviyeye çevirme**: `rgb2gray` ile ortalama `(R+G+B)/3` karşılaştırılır; ağırlıklı formül `0.2989*R + 0.5870*G + 0.1140*B`.
3. **RGB – CMY**: `C = 255 − R`, `M = 255 − G`, `Y = 255 − B` (cyan = beyaz − kırmızı).
4. **RGB histogram eşitleme**: her bant ayrı ayrı `histeq` ile eşitlenir.
5. **Parlaklık artırma**: her banda 128 eklenir. Föyde "Her banda (R,G,B) ayrı ayrı uygulanır!" uyarısı vardır.
6. **RGB süzgeçleme**: `fspecial('average',7)` ile `imfilter(I,H,'replicate')` ve her bantta `medfilt2(…,[7 7])`.

## Laboratuvar 2: frekans uzayında süzgeçleme ve gürültü (lab_fft_noise.pdf)

```matlab
I = imread('eight.tif');
fI = fft2(I);
fS = fftshift(fI);            % spektrumu görüntünün ortasına öteler
H  = fspecial('average',9);
fH = fft2(H, x, y);           % süzgecin FFT'si (görüntü boyutuna tamamlanmış)
NI = ifft2(fI .* fH);         % frekans uzayında çarpma = uzamsal evrişim
```

Aynı sonucun `imfilter(I,H)` ile (2 boyutlu evrişim) elde edildiği gösterilir. İkinci bölüm gürültü üretimidir: `imnoise(I,'salt & pepper',0.02)` (yoğunluk 0,02) ve `imnoise(I,'gaussian',0,0.01)` (ortalama 0, varyans 0,01).

## Programlama ödevi 1 (teslim: 22 Temmuz 2015, laboratuvarda gösterim)

**Problem 1: piksel azaltarak görüntü küçültme.** Kullanıcının verdiği tamsayı küçültme çarpanı X için görüntüyü küçülten bir MATLAB programı yazılacak; Şekil 2.20(a) kullanılacak ve sonuçlar `imwrite` ile özgün biçimde ayrı dosyalara yazılacak.

**Problem 2: yoğunluk dönüşümleriyle iyileştirme.** Şekil 3.8(a) için (a) s = c·log(1 + r) ve (b) s = c·r^γ dönüşümleri uygulanacak. (a)'da tek parametre c, (b)'de c ve γ vardır; amaç her dönüşümle elde edilen en iyi görsel iyileştirmeyi deneyerek bulmak ve ikisi arasındaki farklı sonuçların nedenini açıklamaktır (açıklama program içinde yorum satırı olarak yazılabilir).

Notlar: yalnızca .m kaynak dosyaları teslim edilir; görüntü okuma/yazma ve giriş/çıkış dışında MATLAB kütüphane fonksiyonu kullanılmaz; kodda yeterince yorum ve anlamlı değişken adları beklenir.

## Artı işareti bulma (arti-isareti-bulma.m)

İkili bir görüntüde "+" biçimli (merkez ve dört komşusu 1 olan) pikselleri bulan kısa bir kod:

```matlab
function islem1 = islem1(image)
[x,y]=size(image);
image2=zeros(x,y);
for m=1:x-2
    for n=1:y-2
        if image(m+1,n+1)==1 && image(m,n+1)==1 && image(m+1,n)==1 && image(m+1,n+2) && image(m+2,n+1)==1
            image2(m+1,n+1)=1;
        end
    end
end
islem1=image2;
end
```

*Not: `image(m+1,n+2)` karşılaştırmasında `==1` eksik; sayısal değer sıfırdan farklı olduğunda koşul doğru sayıldığı için ikili görüntüde sonuç değişmez.*
