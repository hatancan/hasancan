---
baslik: EEM308 Sinyaller ve Sistemler II: Spektral Görüntü Filtreleme Projesi (2016)
ozet: Sinyaller arşivindeki sayısal sinyal işleme projesinin önerisi ve raporu: MATLAB ile iki boyutlu FFT, logaritmik spektrum maskesi ve ters dönüşümle periyodik gürültü azaltma.
---

Bu yazı, **EEM308 Sinyaller ve Sistemler II arşivinde bulunan**, Başkent Üniversitesi **Sayısal Sinyal İşleme** dersi için hazırlanmış 2016 tarihli spektral görüntü filtreleme proje önerisini ve öğrenci raporunu aktarıyor. Belgelerde EEM308 ders kodu yazmıyor; arşivde bulundukları ders altında sunuluyorlar. Öğrenci adı, öğrenci numaralı e-posta adresi ve fotoğraf örnekleri çıkarılmış PDF kopyaları yazının sonunda ZIP olarak indirilebilir.

## Önerilen proje

Gri tonlu görüntüye belirli frekansta, düzenli tekrarlanan bir örüntü biçiminde gürültü eklenmesi isteniyor. Görüntünün FFT genlik gösteriminden kullanıcı fareyle dikdörtgen bir alan seçecek; seçilen gürültü bölgesi spektrumdan temizlenecek ve ters FFT ile görüntü geri elde edilecek.

Amaç, bu işlemleri yapan MATLAB programını hazırlamak. Başarı ölçütü, seçilen gürültü alanının temizlenmesi ve görüntünün gürültüden arındırılması olarak yazılmış. Yönetim düzeni bölümü boş bırakılmış.

### Rapor, sunum ve takvim

- Rapor en az iki sayfa ve iki sütunlu olacak.
- Sunum 15–20 slayt içerecek; 15 dakika anlatım ve 5 dakika soru-cevap için toplam 20 dakika ayrılacak.
- Grup üyelerinin tümü sunum sırasında derslikte bulunacak.
- Öneri teslimi: **11 Kasım 2016**.
- Rapor teslimi: **9 Aralık 2016**.
- Sunumlar: **13–14 Aralık** ders saatlerinde.
- Her grup bir proje önerebilir; aynı konuya başvurulursa yeterli öneri formunu önce teslim eden grup önceliklidir.

## Raporun uyguladığı yöntem

Raporda görüntü gri tona çevrilip normalize ediliyor ve **256 × 256** boyutuna getiriliyor. İki boyutlu FFT ve `fftshift` ile merkezlenmiş spektrum alınıyor. Gösterim için:

fLog = log(1 + abs(f)).

Maske iki eşikle oluşturulmuş:

filter = (fLog > 0,7 max(fLog)) veya (fLog < 0,43 max(fLog)).

Bu maskede en yüksek ve en düşük değerler korunuyor; iki eşik arasında kalan spektrum değerleri sıfırlanıyor. Kaynak, merkezi parlak bileşeni ve düşük genlikleri korumayı amaçladığını söylüyor. Maskenin siyah alanları sıfır, beyaz alanları bir değerindedir.

*Not: Öneride fareyle dikdörtgen seçim istenirken rapordaki kod otomatik genlik eşikleri kullanıyor; etkileşimli bölge seçimi bu kodda yok.*

## MATLAB kodu

Raporun kodu, yorumlardaki Türkçe karakter bozulmaları düzeltilerek aktarılmıştır:

```matlab
% Görüntüyü oku
I = imread('clown.jpg');
% Gri tona çevir ve normalize et
I = rgb2gray(I);
I = double(mat2gray(I));
I = imresize(I, [256 256]);
[rows,cols] = size(I);

% Merkezlenmiş Fourier dönüşümü
f = fftshift(fft2(I));
fLog = log(1 + abs(f));

% Genlik aralığına göre maskele
filter = (fLog > .7*max(fLog(:))) | (fLog < .43*max(fLog(:)));
B = abs(ifft2(f.*filter));

% Sonucun Fourier gösterimi
f1 = fftshift(fft2(B));
fLog1 = log(1 + abs(f1));

colormap(gray)
subplot(3,2,1), imagesc(I); title('Orijinal Görüntü')
subplot(3,2,2), imagesc(fLog); title('Fourier Görüntü')
subplot(3,2,3), imagesc(fLog); title('Fourier Görüntü')
subplot(3,2,4), imagesc(filter); title('Çıktı Maskesi')
subplot(3,2,5), imagesc(fLog1); title('Temizlenme Sonrası Fourier Görüntü')
subplot(3,2,6), imagesc(B); title('Temizlenmiş Görüntü')
annotation('textbox', [0 0.9 1 0.1], ...
    'String', 'FFT ile Görüntü Temizleme', ...
    'EdgeColor', 'none', ...
    'HorizontalAlignment', 'center', ...
    'FontSize', 15, ...
    'FontWeight', 'bold')
```

*Not: Kaynak kod `clown.jpg` adını kullanıyor, ancak rapor çıktısındaki örnek bir top görüntüsü. Ayrı giriş görüntüsü dosyası bu kaynak grubunda bulunmuyor.*

*Not: Kod, `fftshift` uygulanmış spektrumu doğrudan `ifft2`ye veriyor. Merkezlenmiş spektrumun doğru ters dönüşümü için önce `ifftshift` uygulanır. Buradaki 256 × 256 çift boyutlu dizide kaydırmadan doğan işaret örüntüsü `abs` ile gizlenebilir; bu, genel olarak doğru yeniden oluşturma işleminin yerine geçmez. Kaynak satırı değiştirilmedi.*

## Tartışma ve sonuç

Rapor, bazı gürültü bileşenlerinin temizlendiğini; seçilen maskenin bazı DC bileşenlerini koruduğunu ve yöntemin her görüntü için en iyi filtreleme yöntemi olmadığını belirtiyor. Sonuç kısmında görüntünün gürültülerden temizlendiği ifade edilmiş; hata ölçütü veya sayısal kalite karşılaştırması verilmemiş.

*Not: DC bileşeninin korunması tek başına hata değildir; görüntünün ortalama parlaklığıyla ilişkilidir. Rapordaki “hata payı” yorumu kaynak ifadesidir.*

## Rapordaki kaynakça

- Charles Van Loan, *Computational Frameworks for the Fast Fourier Transform*, SIAM, 1992.
- Heideman, Johnson ve Burrus, “Gauss and the history of the fast Fourier transform”, IEEE ASSP Magazine, 1984; aynı başlıklı 1985 tarihli Archive for History of Exact Sciences makalesi.
- Gilbert Strang, “Wavelets”, American Scientist, 1994.
- Dongarra ve Sullivan, “Guest Editors Introduction to the top 10 algorithms”, Computing in Science & Engineering, 2000.
- Frank Yates, *The Design and Analysis of Factorial Experiments*, 1937.
