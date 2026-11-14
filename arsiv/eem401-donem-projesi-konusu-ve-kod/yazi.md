---
baslik: EEM401 Sayısal Sinyal İşleme: 2014 Dönem Projesi (Gaussian Gürültü ve Üç Butterworth Süzgeç) ve MATLAB Çözümü
ozet: EEM401 Sayısal Sinyal İşleme dersinin Kasım 2014 dönem projesi konusu: gri tonlu görüntüye Gaussian gürültü ekleme ve üç Butterworth alçak geçiren süzgeçle frekans uzayında süzme; bir arkadaşın MATLAB çözümü (kişisel bilgisi çıkarılmış).
---

**EEM401 Sayısal Sinyal İşleme** dersinin (Yrd. Doç. Dr. Selda Güney) 21 Kasım 2014 tarihli dönem projesi konusu ve bir arkadaşımın bu konuya yazdığı MATLAB kodu. Koddaki yorum satırlarından ad ve numara bilgisi çıkarıldı; görüntü dosyasının adı `girdi.jpg` olarak değiştirildi, projede kullanılan kişisel fotoğraf paylaşılmadı. Proje konusu PDF'i ve kod yazının sonunda ZIP olarak indirilebilir.

## Proje konusu

"EEM401-Sayısal Sinyal İşleme Dersi Projesi": Ders projesi MATLAB programı kullanılarak gerçekleştirilecek; kütüphanelerdeki hazır fonksiyonlardan yararlanılabilir.

**Amaç.** Öğrencinin kendi renkli bir resmi MATLAB'a yüklenip siyah-beyaza çevrilecektir. Bu resmin üstüne

- a) ortalaması 0,
- b) standart sapması 0,02·x

değerlerine sahip Gaussian gürültüsü eklenecektir; buradaki x, projeyi gerçekleştiren öğrencinin numarasının son hanesidir.

Gürültü eklenmiş resim, **derecesi ve kesim frekansı öğrenci tarafından belirlenecek birbirinden farklı üç adet Butterworth filtresi** ile süzgeçlenecek ve sonuçlar karşılaştırılacaktır. Projenin çalıştırılması sonucu altı resim çıktısı elde edilecektir: 1) orijinal resim, 2) siyah-beyaz resim, 3) gürültü eklenmiş resim, 4) birinci, 5) ikinci, 6) üçüncü süzgeç çıkışı.

**Teslim.** Proje en geç dersin final sınavı tarihine kadar, .m dosyası ekli olarak e-postayla gönderilecek (konu satırı "EEM401-Dönem Projesi"; mesajda öğrencinin adı, soyadı ve numarası). Ek rapor teslim edilmeyecek; gerekirse kaynak koda açıklama satırları yazılabilir.

## MATLAB çözümü

```matlab
clear all;
% program resmi okuyor
resimorg = imread('girdi.jpg');
% resim siyah-beyaz yapıldı
resimsiyahbeyaz = rgb2gray(resimorg);
resimgaus = imnoise(resimsiyahbeyaz,'gaussian',0,0.029);
% süzgeçler
cf = fftshift(fft2(resimgaus));
% butterworth 1
[x,y] = meshgrid(-128:127,-128:127);
bl1 = 1./(1+((x.^2+y.^2)/15).^5);
cfbl1 = cf.*bl1;
bt1 = ifft2(cfbl1);
bt1 = uint8(abs(bt1));
% butterworth 2
bl2 = 1./(1+((x.^2+y.^2)/15).^2);
bt2 = uint8(abs(ifft2(cf.*bl2)));
% butterworth 3
bl3 = 1./(1+((x.^2+y.^2)/15).^0.25);
bt3 = uint8(abs(ifft2(cf.*bl3)));
% çıktılar
figure;
subplot(2,3,1), imshow(resimorg), title('Orijinal Resim');
subplot(2,3,2), imshow(resimsiyahbeyaz), title('Siyah Beyaz Resim');
subplot(2,3,3), imshow(resimgaus), title('Gürültü Eklenmiş Resim');
subplot(2,3,4), imshow(bt1), title('Birinci Süzgeç Çıkışı Resim');
subplot(2,3,5), imshow(bt2), title('İkinci Süzgeç Çıkışı Resim');
subplot(2,3,6), imshow(bt3), title('Üçüncü Süzgeç Çıkışı Resim');
```

(Kod, orijinal dosyadan okunabilirlik için üç süzgeç bloğundaki tekrarlar kısaltılarak aktarılmıştır; ZIP içindeki dosya özgün hâlidir.)

## Nasıl çalışıyor?

1. Resim gri seviyeye çevrilir ve `imnoise` ile ortalaması 0 olan Gaussian gürültü eklenir. `imnoise`'un son parametresi *varyans*tır; proje ise standart sapmayı 0,02·x olarak tanımlar. Kodda 0,029 değeri kullanılmıştır.
2. 2 boyutlu FFT alınıp `fftshift` ile sıfır frekans merkeze taşınır.
3. Merkezden uzaklığın karesi D² = x² + y² olan 256×256'lık ızgarada Butterworth alçak geçiren süzgeç H = 1 / (1 + (D²/15)ⁿ) üç farklı n ile (5; 2; 0,25) oluşturulur. Derece büyüdükçe kesim keskinleşir; 0,25 gibi küçük bir değerde süzgeç çok yumuşaktır ve gürültüyü daha az bastırır.
4. Her süzgeç, kaydırılmış spektrumla elemanter çarpılır (frekans uzayında çarpma = uzamsal evrişim), ters FFT ile görüntüye dönülür ve `uint8(abs(·))` ile görüntülenir.

Dikkat: Meshgrid ızgarası 256×256 olarak sabittir; görüntü başka boyutta ise yeniden boyutlandırılmalıdır.

Bu projenin 2016'daki sürümü (periyodik gürültünün FFT genlik spektrumunda maskelenmesi) için bkz. "Spektral Görüntü Filtreleme Tasarım Projesi".
