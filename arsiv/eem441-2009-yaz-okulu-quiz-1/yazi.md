---
baslik: EEM441 Haberleşme I: 2009 yaz okulu Quiz I (10 Temmuz 2009) ve çözümü
ozet: Doğrusal olmayan elemanlı karıştırma düzeni, genlik bindirimli im için taşıyıcı genliği, yan bant ve taşıyıcı gücü; el yazısı çözümle.
---

Başkent Üniversitesi Elektrik-Elektronik Mühendisliği Bölümü, EEM 441 Haberleşme I Quiz I (10 Temmuz 2009, süre 1 saat) sorusu ve el yazısı çözümü. Sınav kâğıdı ve çözümler fotoğraflanmış sayfalardan metne aktarıldı; fotoğraflar yayınlanmamıştır. Bu nedenle indirilebilir orijinal dosya yoktur. Kişisel bilgiler (öğrenci numarası, ad) çıkarılmıştır.

## Sorular

1. Aşağıdaki öbek gösteriminde e₁ gerilimi verildiğine göre: a) e₅ gerilimini bulun. b) A = 10 değeri için e₅ geriliminin 50 Ω'luk bir direnç üzerinde oluşturacağı ortalama gücü hesaplayın.

Öbek gösterimi: e₁(t) = cos ω₁t + cos 2ω₁t; e₁ iki kola ayrılır. Üst kolda e₂ = A e₁²; alt kolda alçak geçiren süzgeç (kesim 1,5 ω₁) e₃ verir. e₄ = e₂ + e₃ bant geçiren süzgeçten (3,5 ω₁ – 5,5 ω₁) geçerek e₅ olur.

2. Genlik bindirimli imlerin üretilmesinde kullanılan çarpıcı bindiricinin (product modulator) öbek gösterimini çizin. Binen im f(t) = 12 cos(2π 3 10³ t) volt olarak veriliyor. Bindirim yüzdesi %80 olan genlik bindirimli im elde etmek için a) taşıyıcının genliği kaç volt olmalıdır? Hesaplayın. Taşıyıcı genliğinin 12 volttan küçük olması durumunda elde edilen genlik bindirimli im nasıl etkilenir? Bu duruma ne ad verilir? b) Taşıyıcı sıklığını 30 kHz alarak yukarıda verilen değerler için genlik bindirimli imin matematiksel ifadesini yazın, çift yanlı sıklık görüntüsünü değerler belirterek çizin, bant genişliğini bulun. c) Elde edilen genlik bindirimli imin 50 Ω'luk bir direnç üzerinde oluşturacağı taşıyıcı gücünü ve toplam yan bant gücünü hesaplayın.

## Çözüm 1

e₂ = A[cos ω₁t + cos 2ω₁t]² = A cos²ω₁t + 2A cos ω₁t cos 2ω₁t + A cos²2ω₁t
= A/2 (1 + cos 2ω₁t) + A[cos(2ω₁ − ω₁)t + cos(2ω₁ + ω₁)t] + A/2 (1 + cos 4ω₁t)
= A/2 + (A/2) cos 2ω₁t + A cos ω₁t + A cos 3ω₁t + A/2 + (A/2) cos 4ω₁t.

e₃ = cos ω₁t (alçak geçiren süzgeç 1,5ω₁'in üstünü keser). e₄ = e₂ + e₃ (toplam). Bant geçiren süzgeç yalnız 3,5ω₁–5,5ω₁ arasını geçirir; burada yalnız 4ω₁ vardır:

a) e₅ = (A/2) cos 4ω₁t.

b) P_ort = (A/2 / √2)² / 50 = A²/(8 × 50) = 10²/400 = 1/4 W (A = 10).

## Çözüm 2

Çarpıcı bindirici: m f(t) önce taşıyıcı f_c(t) = A_c cos 2π f_c t ile çarpılır, sonuç taşıyıcıyla toplanır: f_GB(t) = A_c[1 + m f(t)] cos ω_c t. Bindirim m = %80 = 0,8.

a) m = A_m/A_c ⇒ A_c = A_m/m = 12/0,8 = 15 V. A_c < 12 V olursa m > 1 olur; buna aşırı bindirim (overmodulation) denir ve genlik bindirimli imde evre (faz) tersliği ve zarf bozukluğu olur.

b) f_c = 30 kHz için f_c(t) = 15 cos 2π(30×10³)t. Kâğıtta yazılan açılım: f_GB(t) = 15 cos 2π30×10³t + 72 cos 2π(27×10³)t + 72 cos 2π(33×10³)t (taşıyıcı, alt yan bant, üst yan bant); çizim: ±30 kHz'de 15/2, ±27 ve ±33 kHz'de 72/2 çizgiler; bant genişliği BW = 6 kHz.

c) P_c = (15/√2)² / 50 = 2,25 W; yan bant gücü kâğıtta (72/√2)²/50 + (72/√2)²/50 = 103,68 W olarak yazılmıştır.

*Not: Kâğıttaki yan bant genliği 72 V, m·f(t) ifadesinin 0,8 × 12 = 9,6 ile çarpılıp 15 ile çarpılmasından (15 × 9,6 / 2 = 72) çıkmıştır; oysa m zaten f(t)'nin genliğini A_c'ye oranlayan bindirim indeksidir. Doğru ifade f_GB(t) = [A_c + f(t)] cos ω_c t = 15 cos ω_c t + 6 cos 2π27×10³t + 6 cos 2π33×10³t (yan bant tepe genliği mA_c/2 = 6 V) olur; bu durumda P_c = 2,25 W, her yan bant 6²/(2×50) = 0,36 W ve toplam yan bant gücü 0,72 W'dır (= m²/2 · P_c). Bant genişliği 6 kHz'dir ve değişmez.*
