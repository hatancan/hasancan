---
baslik: EEM308 Sinyaller ve Sistemler II: EEM302 MATLAB Ödevi (2007) ve Öğrenci Çözümleri, Kutup-Sıfır Diyagramları
ozet: EEM302 (bugünkü EEM308) Sinyaller ve Sistemler II dersinin 2007 MATLAB ödevi: Buck'ın Computer Explorations kitabından kutup-sıfır diyagramı, ikinci dereceden sistemin frekans yanıtı, |H(s)| yüzeyi ve kutup vektörleri problemleri; arkadaşların .m çözümleri, notlarla.
---

Bu yazı, Başkent Üniversitesi **EEM 302 Sinyaller ve Sistemler II** dersinde (ders daha sonra EEM 308 koduyla verildi) **Yrd. Doç. Dr. Mustafa Doğan**'ın 2007 bahar döneminde verdiği **MATLAB ödevini** ve bu ödeve arkadaşların hazırladığı MATLAB çözümlerini bir araya getiriyor. Ödev, *Computer Explorations in Signals and Systems Using MATLAB* (Buck, Daniel, Singer; 2. baskı) kitabının Laplace ve z-dönüşümü bölümlerinden seçilmiş problemlerden oluşuyor. 2011'de aynı ödev sisteminde hazırlanmış iki kısa çözüm de eklendi.

Çözümler arkadaşların çalışmalarıdır; dosya adlarındaki ve kodlardaki ad ve öğrenci numaraları çıkarıldı, dosyalar problem numarasına göre yeniden adlandırıldı. Ödev dağıtım listesi (öğrenci adları ve numaraları içerdiği için) ve kitap sayfalarının fotoğrafları yayınlanmadı; problem dağılımı aşağıda adsız olarak verildi. Temizlenmiş `.m` dosyaları yazının sonunda ZIP olarak indirilebilir.

## Ödevin kuralları ve problem dağılımı

Ödev listesinin başlığı: *EEM 302 MATLAB HW — "Computer Explorations in Signals and Systems 2nd ed. – BUCK" — Yrd. Doç. Dr. Mustafa Doğan*. Ödevler **25 Mart (Pazar) saat 24:00'e kadar** bölümün web sunucusundaki yükleme adresine gönderilecekti. Sınıf sekiz gruba ayrılmış, her gruba kitaptan iki problem verilmişti:

| Grup | Laplace bölümünden | z-dönüşümü bölümünden |
| --- | --- | --- |
| 1 | Sayfa 163 (a) | Sayfa 178 (k) |
| 2 | Sayfa 163 (b) | Sayfa 178 (j) |
| 3 | Sayfa 166 (a) | Sayfa 178 (i) |
| 4 | Sayfa 166 (b) | Sayfa 177 (e) |
| 5 | Sayfa 166 (c) | Sayfa 177 (d) |
| 6 | Sayfa 166 (d) | Sayfa 177 (c) |
| 7 | Sayfa 169 (a) | Sayfa 177 (b) |
| 8 | Sayfa 169 (b) | Sayfa 177 (a) |

Ödevlerde dikkat edilmesi gerekenler:

1. Gönderilecek tek dosya, örnekteki gibi `öğrenciNo.m` biçiminde adlandırılmalı. Ödevde yapılması gereken her şey (tüm şıklar) bu m-dosyasının içinde olmalı ve dosya çalışır olmalı.
1. Değerlendirmede açıklamaların ve soruların cevaplarının katkısı çok daha fazla olacak. Değerlendirilmesi istenen açıklamalar `display('sözel cevaplar ve açıklamalar...');` örneğindeki gibi `display` ile Command Window'a yazdırılmalı.
1. Değerlendirilmesi istenmeyen çıktılar Command Window'da görünmemeli (`;` kullanılmadığında çıktı Command Window'da görünür).

## Sayfa 166 (a) ve 178 (i): Kutup-sıfır diyagramları

**166 (a).** H₁(s) = 4 / (s² + 2s + 17), Re(s) > −1 sistem fonksiyonunun pay ve payda katsayılarını `b1` ve `a1` vektörleri olarak tanımlayıp `roots` ile kutupları bulmak ve çizmek.

**178 (i).** H₃(z) = (0,25 − (√3/2)z⁻¹ + z⁻²) / (1 − (√3/2)z⁻¹ + 0,25z⁻²), |z| > 0,5 sisteminin kutuplarını ve sıfırlarını bulup çizmek; kutup ve sıfır konumlarının nasıl ilişkili olduğunu açıklamak.

Bu gruba ait iki çözüm var. İkisi de aynı yolu izliyor; ikincisinin bir sürümü kitaptaki `plotpz` mantığıyla eksenleri, ROC sınırını ve birim çemberi de çiziyor:

```matlab
b1=[4];
a1=[1 2 17];
zeros=roots(b1);
poles=roots(a1);

disp('Soru : 166 (a) için');
disp('Kutuplar:');
disp(poles);

figure (1);
plot(real(zeros),imag(zeros),'o');
hold on
plot(real(poles),imag(poles),'x');
grid
title('Soru : 166 (a)');
xlabel('Re');
ylabel('Im');
axis([-5 5 -5 5]);

b=[0.25 -(sqrt(3)/2) 1];
a=[1 -(sqrt(3)/2) 0.25];
zs=roots(b);
ps=roots(a);
disp('Soru : 178 (i) için');
disp('Sıfırlar:'); disp(zs);
disp('Kutuplar:'); disp(ps);
```

Sonuçlar: 166 (a)'da kutuplar **s = −1 ± j4** (pay sabit olduğundan sonlu sıfır yok). 178 (i)'de kutuplar **z = 0,5·e^(±jπ/6)** (= 0,433 ± j0,25), sıfırlar **z = 2·e^(±jπ/6)** (= 1,732 ± j1).

*Not: Çözümler yalnızca "2 kutup ve 2 sıfır bulunmuştur" diyor; sorunun asıl istediği ilişki şu: sıfırlar, kutupların birim çembere göre yansımaları (1/p*) ve pay katsayıları paydanınkilerin ters sırası. Bu yüzden sistem tüm geçiren (all-pass) bir süzgeç, |H₃(e^jω)| = 1 sabit (z = 1'de pay ve payda ikisi de 0,384). Ayrıca kodlardaki `rsmak('circle')` satırı MATLAB'ın Spline Toolbox'ına bağlı; bu araç kutusu yoksa hata verir.*

### |H₁(s)| yüzeyi

Aynı problem için hazırlanmış bir başka dosya, |H₁(s)|'i s-düzleminde bir yüzey olarak çiziyor: σ, −1'in hemen sağından 3'e kadar 32 örnek (σ = −1 + k/8, k = 1…32), ω ∈ [−10, 10] aralığı 0,5 adımla; `meshgrid` ile s = σ + jω ızgarası kuruluyor, H₁ = `polyval(b1,s)./polyval(a1,s)` hesaplanıp `mesh` ile çiziliyor ve jω ekseni boyunca yüzeyin kesiti mavi çizgiyle (`plot3`) işaretleniyor. Açıklamadaki sonuç: yüzey kutuplara yaklaştıkça hızla büyüyor; kutupların frekans yanıtını nasıl etkilediği 3 boyutlu çizimde görülüyor.

## Sayfa 163 (b): İkinci dereceden sistemde sönüm oranı

Problem, ikinci dereceden sistem H(s) = ωₙ² / (s² + 2ζωₙs + ωₙ²) için ωₙ = 1 alıp sönüm oranı ζ'nin farklı değerlerinde kutupları ve frekans yanıtını incelemeyi istiyor. İki çözüm de `ord2`, `printsys` ve `freqs` komutlarıyla ζ = 0, 1/4, 1 ve 2 için |H(jω)|'yı ω ∈ [−5, 5] aralığında çiziyor:

```matlab
wn=1
omega=[-5:0.1:5]
damping_ratio=1/4
[num0,den]=ord2(wn,damping_ratio);
num=wn^2*num0
printsys(num,den)
freqs(num,den,omega)
display('0<damping_ratio<1 olduğunda polinomun kutupları kompleks sayı olur dolayısıyla step response ve impulse responsları salınıma sahip olur...');
```

Çözümlerdeki açıklamaların özeti:

- **ζ = 0:** Kutuplar sanal eksende (s = ±jωₙ).
- **0 < ζ < 1:** Kutuplar karmaşık eşlenik; basamak ve dürtü yanıtı salınımlı. ζ küçüldükçe kutuplar jω eksenine yaklaşıyor ve |H(jω)| (çözümlere göre) ω = ωₙ√(1 − ζ²) frekansında tepe yapıyor; sistem ideal olmayan bir bant geçiren süzgeç gibi davranıyor.
- **ζ = 1:** Kutuplar reel eksende (çift kutup); ω arttıkça |H(jω)| monoton azalıyor.
- **ζ > 1:** Düşük ω değerlerinde |H(jω)| ω'daki değişime daha duyarlı hâle geliyor.
- ω = 0'da dört sistemin de |H(j0)| = 1 olduğu, çünkü fonksiyonun bu noktada sabite indirgendiği belirtiliyor.

*Not: Çözümlerde birkaç düzeltme gerekiyor. ζ = 0'da tepe "oluşmuyor" değil, tersine ω = ωₙ = 1'de |H| sonsuza gidiyor (ω ızgarası 1'i tam içerdiğinden `freqs` bu noktada Inf üretir ve çizimde görünmez). Rezonans tepesinin konumu ωₙ√(1 − ζ²) değil ωₙ√(1 − 2ζ²)'dir ve yalnız ζ < 1/√2 için oluşur; √(1 − ζ²) sönümlü salınım frekansıdır. Kutuplar ζ ≥ 1 için (yalnız ζ = 1'de değil) reeldir; ζ > 1'de iki ayrı reel kutup oluşur, biri orijine yaklaşırken öteki sola uzaklaşır.*

## Sayfa 177: Kutup vektörlerinin uzunlukları

Problem, H₁(z) = 1 / (1 − 0,9z⁻¹ + 0,81z⁻²) sistemi için birim çember üzerindeki 512 noktadan (ω = k·π/256) kutuplara çizilen vektörlerin uzunluklarını ve açılarını hesaplamayı, frekans yanıtıyla ilişkisini göstermeyi istiyor. Çözümlerin çekirdeği:

```matlab
omega=[0:511]*pi/256;
unitcirc=exp(j*omega);
num=[1 0 0];
den=[1 -0.9 0.81];
ps1=roots(den)
polevectors1=ones(2,1)*unitcirc-ps1*ones(1,512);
polelength1=abs(polevectors1);
poleangle1=atan2(imag(polevectors1),real(polevectors1));
zerovectors1=ones(2,1)*unitcirc;      % z = 0'daki iki sıfır
zerolength1=abs(zerovectors1);
plot(omega,polelength1,'r',omega,zerolength1,'g')
```

Kutuplar **z = 0,9·e^(±jπ/3)** (= 0,45 ± j0,779); H₁(z) = z²/(z² − 0,9z + 0,81) yazıldığında z = 0'da iki sıfır olduğundan sıfır vektörlerinin uzunluğu her frekansta 1'dir.

*Not: Bir çözümdeki sonuç cümlesi ("|H₁| kutup uzunluklarının maksimum ve minimum olduğu yerlerde minimum, 1 olduğu yerlerde maksimum") yanlış. Sıfır uzunlukları 1 olduğundan |H₁(e^jω)| = 1 / (|e^jω − p₁|·|e^jω − p₂|) olur: kutup vektörlerinin kısaldığı ω ≈ ±π/3 civarında |H₁| en büyük, uzadığı ω = π civarında en küçüktür.*

## Sayfa 169 (a) (2011)

2011'de aynı problem setinden hazırlanmış kısa bir çözüm, nedensel sistemi H(s) = 1/(s + 2) olarak `tf([1],[1 2])` ile tanımlıyor ve nedensel olmayan karşılığı için zaman ters çevrilmiş denklemden (−dy(−t)/dt − 2y(−t) = −x(−t)) yola çıkıp ikinci bir transfer fonksiyonu kuruyor. 2011 tarihli 177 (b) çözümü yukarıdaki kutup vektörü hesabının aynısı; dosyadaki nota göre ayrıntılı açıklamalar ve Laplace sorusu elle yazılıp ayrıca teslim edilmiş.

## Ev çalışması: Bant sınırlı 90° faz kaydırıcının dürtü yanıtı

Aynı klasörde, 27 Mart 2007 tarihli, bir arkadaşın el yazısı "Ev Çalışması" sayfasının fotoğrafı da vardı (fotoğraflanmış sayfadan metne aktarıldı; fotoğraf yayınlanmadı). Frekans yanıtı |ω| < ω_c bandında

H(jω) = e^(jπ/2), 0 < ω < ω_c; H(jω) = e^(−jπ/2), −ω_c < ω < 0

olan sistemin dürtü yanıtı ters Fourier dönüşümüyle bulunuyor:

h(t) = (1/2π) ∫₀^ω_c e^(jπ/2) e^(jωt) dω + (1/2π) ∫₋ω_c⁰ e^(−jπ/2) e^(jωt) dω
= (1/2πt) (e^(jω_c t) − 1) − (1/2πt) (1 − e^(−jω_c t))
= (cos ω_c t − 1) / (πt)

ve cos ω_c t = 1 − 2 sin²(ω_c t/2) kullanılarak

**h(t) = −2 sin²(ω_c t / 2) / (πt)**

sonucuna ulaşılıyor. (Sonucu kontrol ettik; doğru.)
