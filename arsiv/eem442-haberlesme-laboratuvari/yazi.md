---
baslik: EEM442 Haberleşme II Laboratuvarı: Deney 1 Kuantalama-PCM, Deney 2 µ-Law Sıkıştırma-Genleştirme, Deney 3 Delta Modülasyonu (MATLAB)
ozet: EEM442/444 Haberleşme II laboratuvarı Mayıs 2017: eş biçimli kuantalama ve PCM, SQNR'nin kuramsal ve ölçülen değerleri, µ-law companding ile ses işareti, doğrusal ve uyarlanır delta modülasyonu; deney raporları ve MATLAB kodları.
---

Başkent Üniversitesi'nde **EEM 442/444 Haberleşme II – Laboratuvarı** (Mayıs 2017) için hazırlanan üç deney raporu ve MATLAB fonksiyonları. Deney 1 ve 2'yi ben hazırladım; Deney 3 bir arkadaşımın raporudur (ad ve numara çıkarıldı). Öğrenci numaraları maskelenmiş raporlar ve kodlar yazının sonunda ZIP olarak indirilebilir. Klasördeki bir arkadaşın aynı Deney 1 raporunun ikinci kopyası ve `.wav` ses dosyaları yayımlanmadı.

## Deney 1: Kuantalama – PCM

**Amaç:** temel bant sayısal haberleşme modülasyonlarından PCM'in ve kuantalama işleminin gerçekleştirilmesi; kuantalama gürültüsü ve SNR değerlerinin ölçülmesi.

**Kuram.** Analogdan sayısala dönüşümün iki adımı vardır: zaman bölgesinde ayrıklaştırma (örnekleme) ve genlik bölgesinde ayrıklaştırma (**kuantalama**). Deneyde eş biçimli (uniform) kuantalayıcı MATLAB'da incelenir. Mesaj m(t) = A·cos(2πf_m·t) tek tonlu ve kuantalama hatası düzgün olasılık yoğunluklu varsayılırsa mesaj gücü ⟨x²⟩ = A²/2, hata gücü ⟨e²⟩ = a²/12 (a = 2A/2ⁿ adım aralığı) ve

SQNR_dB = 10·log10((3/2)·2^{2n}) = 1,76 + 6,02·n

(n: örnek başına bit sayısı).

**Yapılışı.** `u_pcm.m` fonksiyonu tek ton mesajla kullanılır: a) farklı kuantalama seviyeleri için kuantalanmış işaret çizilir; kuantalama seviyesi arttıkça hassasiyet ve orijinale yakınlık artar (8 seviyeli kuantalamada iki farklı zamanda aynı bit değeri çıkarken 16 seviyede farklı değerler çıkar); b) farklı seviyeler için PCM kodu oluşturulur:

```matlab
t = [0:0.01:10];
a = sin(t);
[sqnr8,  aquan8,  code8 ] = u_pcm(a, 8);
[sqnr16, aquan16, code16] = u_pcm(a, 16);
[sqnr32, aquan32, code32] = u_pcm(a, 32);
[sqnr64, aquan64, code64] = u_pcm(a, 64);
subplot(5,1,1), plot(t,a), title('örneklenen sinyal');
subplot(5,1,2), plot(t,aquan8),  title('8 seviyeli kuantalanmış sinyal');
subplot(5,1,3), plot(t,aquan16), title('16 seviyeli kuantalanmış sinyal');
subplot(5,1,4), plot(t,aquan32), title('32 seviyeli kuantalanmış sinyal');
subplot(5,1,5), plot(t,aquan64), title('64 seviyeli kuantalanmış sinyal');
```

c) SQNR değerleri hesaplanan değerlerle karşılaştırılır:

| Kuantalama seviyesi (Q) | SQNR (hesaplanan) | SQNR (ölçülen) |
|---|---|---|
| 8 | 19,280 | 18,9023 |
| 16 | 25,84 | 25,1272 |
| 32 | 31,86 | 31,3002 |
| 64 | 37,88 | 37,4202 |

*Not: Q = 8 (n = 3) için 1,76 + 6,02·3 = 19,82 dB'dir; tabloda 19,280 yazılmıştır, bu bir yazım hatasıdır. Ölçülen değerler kuramsal değerlerin biraz altındadır.*

**Sonuç.** Örneklenen orijinal işarete en yakın sonuç 64 seviyeli kuantalamadan çıkmıştır.

## Deney 2: µ-Law sıkıştırma-genleştirme (companding)

**Amaç:** PCM ve kuantalamanın µ-law sıkıştırma-genleştirme tekniğiyle gerçekleştirilmesi; kuantalama gürültüsü ve SNR ölçümü.

**Kuram.** Düzgün olmayan PCM, sıkıştırma ve genleştirme yapıları sayesinde eş biçimli kuantalamayla gerçeklenebilir: sıkıştırıcı → düzgün kuantalayıcı → genleştirici. |x| ≤ 1 normalize giriş için µ-law sıkıştırma fonksiyonu

y = [ln(1 + µ|x|) / ln(1 + µ)]·sgn(x),

tersi (genleştirme)

x = [((1 + µ)^{|y|} − 1) / µ]·sgn(y).

**Yapılışı.** `mulaw_pcm.m` fonksiyonu bir ses işareti için kullanılır (µ = 255; Q = 8, 16, 32, 64):

```matlab
x = audioread('history.wav');
x = x(1:50000);
[sqnrmu8,  aquanmu8,  codemu8 ] = mulaw_pcm(x, 8,  255);
[sqnrmu16, aquanmu16, codemu16] = mulaw_pcm(x, 16, 255);
[sqnrmu32, aquanmu32, codemu32] = mulaw_pcm(x, 32, 255);
[sqnrmu64, aquanmu64, codemu64] = mulaw_pcm(x, 64, 255);
```

Ölçülen SQNR (dB): Q = 8 → 8,2776; Q = 16 → 13,4264; Q = 32 → 19,8473; Q = 64 → 25,9201.

**Sonuç.** Orijinal sese en yakın sonuç Q = 64'te alınmıştır (neredeyse orijinal ses duyulur); kuantalama seviyesi düştükçe ses bozulur. Seviye artırıldıkça hassasiyet artmış, orijinal ses sinyaline daha yakın sonuç alınmıştır.

## Deney 3: Delta modülasyonu (DM)

**Amaç:** PCM'in delta modülasyonu ve uyarlanır delta modülasyonuyla gerçeklenmesi; kuantalama gürültüsü ve SNR ölçümü.

**Kuram.** PCM'de her örnek birden çok bitle gönderilir, bu da çok güç ve enerji harcar; bunun yerine işaretteki *değişimler* gönderilebilir: iki örnek arasındaki farkın pozitif ya da negatif olduğuna göre kodlama yapılır (delta modülasyonu), böylece örnek başına bit sayısı çok azalır. **Doğrusal DM** vericisi keskin bir sınırlayıcı (karşılaştırıcı), örnekleyici ve geri besleme yolunda bir integral alıcıdan oluşur; alıcıda integral alıcı ve bir alçak geçiren filtre (AGF) vardır. Giriş ile geri beslemeyle üretilen yaklaşık işaret arasındaki farkın işaretine göre bit darbeleri üretilir; sınırlayıcı çıkışı Nyquist frekansının çok üstünde bir f_s ile örneklenir. AGF süreksizlikleri düzgünleştirir; çıkışın x(t) ile aynı olmamasının nedeni kuantalama hatalarıdır.

DM'de üç istenmeyen durum görülebilir:
1. Başlangıçta x̂(t)'nin x(t)'ye yetişmesi için birkaç basamak gerekir (**başlama süresi**, start-up period).
2. x(t) sabit kaldığında x̂(t) bir artı bir eksi basamakla izler (**boşta çalışma gürültüsü**, idling noise).
3. x(t) hızlı değişirse x̂(t) yalnızca ±Δ kadar değişebildiğinden izleyemez (**eğim sınırlaması**, slope overload).

Bu sorunlar için **uyarlanır (adaptive) DM** geliştirilmiştir: basamak boyu her örnekleme anında uyarlanır. Kuantalanmış fark dizisi, dalga biçiminin eğimi hakkında bilgi verir: art arda gelen işaretler değişiyorsa eğim küçüktür, aynı işaretliyse eğim diktir. Jayant'ın basit kuralına göre Δ(n) = Δ(n − 1)·K^{ε(n)·ε(n−1)} (K: yerel distorsiyonu en küçük yapacak sabit, K > 1).

**Yapılışı.** `delta_mod.m` ve `adpt_delta_mod.m` dosyaları ses işareti için kullanılır; doğrusal DM, Δ = 1; 0,1; 0,01 ve 0,001 için denenir. **Sonuç:** Δ giderek küçüldükçe SQNR artmıştır, fakat son değerde eğim sınırlaması (slope overload) nedeniyle SQNR yeniden düşmüştür.

## MATLAB kodları (ZIP içindeki `kod/` klasörü)

Fonksiyonlar `u_pcm.m` (düzgün PCM), `mulaw.m`, `invmulaw.m`, `mulaw_pcm.m`, `delta_mod.m`, `adpt_delta_mod.m` ve örnek betikler. Temel iki fonksiyon:

```matlab
function [ sqnr, a_quan, code ] = u_pcm( a, n )
% uniform PCM encoding of a sequence; n = number of quantization levels
amax = max(abs(a));
a_quan = a/amax;
b_quan = a_quan;
d = 2/n;
q = d.*[0:n-1];
q = q-((n-1)/2)*d;
for i=1:n
    a_quan(find((q(i)-d/2<=a_quan) & (a_quan<=q(i)+d/2)))= q(i).*ones(1,length(find((q(i)-d/2<=a_quan) & (a_quan<=q(i)+d/2))));
    b_quan(find( a_quan== q(i) )) = (i-1).*ones(1,length(find( a_quan== q(i) )));
end
a_quan = a_quan*amax;
nu = ceil(log2(n));
code = zeros(length(a),nu);
for i = 1:length(a)
    for j=nu:-1:0
        if ( fix(b_quan(i)/2^j) == 1)
            code(i,(nu-j)) = 1;
            b_quan(i) = b_quan(i) - 2^j;
        end
    end
end
sqnr = 20*log10(norm(a)/norm(a-a_quan));
end
```

```matlab
function [X_quan, sqnr]=delta_mod(X,delta)
l = size(X,2);
Y_quan = zeros(1,l);
X_quan = zeros(1,l);
if X(1) >= 0, epsi = 1; else epsi = -1; end
Y_quan(1) = epsi * delta;
X_quan(1) = Y_quan(1);
for n = 2:l
    if X(n) >= X_quan(n-1), epsi = 1; else epsi = -1; end
    Y_quan(n) = epsi * delta;
    X_quan(n) = X_quan(n-1) + Y_quan(n);
end
sqnr = 20*log10(norm(X)/norm(X-X_quan));
```
