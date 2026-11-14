---
baslik: SOS204 İşletme: Sayısal Problemler ve Çözümleri (Amortisman, Ağırlık Merkezi, Ekonomik Sipariş Miktarı, NBD ve İç Verim Oranı)
ozet: SOS204 İşletme dersi el yazısı sayısal problem çözümleri: amortisman yöntemleri, kuruluş yeri için ağırlık merkezi ve ağırlıklı puanlama, birim bulundurma maliyeti ve ekonomik sipariş miktarı, kapasite hesabı, geri ödeme süresi, net bugünkü değer ve iç verim oranı.
---

SOS204 İşletme dersi için hazırlanmış 8 sayfalık **el yazısı problem çözümü** notunun (sayfalar "23 Aralık" tarihli, hazırlayanı yazmıyor) metne aktarılmış hâlidir. Sayfalar fotoğraflanmış/taranmış kâğıtlardan metne aktarıldı; görseller yayınlanmıyor. Çözümlerin çoğu düşük çözünürlüklü olduğundan okunamayan sayılar belirtilmiş ya da atlanmıştır.

## 1. Amortisman yöntemleri

- Soru: bir işletmede kullanılan makinenin 2. kullanım yılı sonundaki defter değeri 450 TL, 3. yıl sonundaki defter değeri 337,5 TL'dir; 4. yıl amortismanı 100 TL'den az olacağına göre hangi yöntem kullanılmıştır? 2. ve 3. yıl arasındaki amortisman 450 − 337,5 = 112,5 TL'dir; amortisman her yıl azaldığından ve 4. yılda 100 TL'nin altına düşeceğinden yöntem **azalan tutarlı amortisman**dır.
- Maliyet değeri C = 1024 TL, hurda değeri S = 243 TL, ömür n = 5 yıl olan makine için:
  - **Eşit tutarlı:** A = (C − S)/n = (1024 − 243)/5 = **156,20 TL** her yıl.
  - **Azalan tutarlı:** oran a = 1 − ⁿ√(S/C) = 1 − ⁵√(243/1024) = **0,25**. Yıllık amortisman = kalan değer × 0,25: 1. yıl 256, 2. yıl 192, 3. yıl 144, 4. yıl 108, 5. yıl 81 TL (kalan değer 1024 → 768 → 576 → 432 → 324 → 243).
  - **Artan tutarlı:** yıl sayıları toplamı 1 + 2 + 3 + 4 + 5 = 15; amortisman = (C − S) × (kalan yıl)/15 = 781 × 5/15, 781 × 4/15, … 781 × 1/15.
- Not: ilk yılın amortismanı hesaplanırken ve son yılda hurda değer çıkarılırken yöntemin özelliklerine dikkat edilmelidir (sayfadaki notlar: ilk yıl amortismanı doğrudan maliyetten, sonraki yıllar kalan değerden bulunur).

## 2. Maliyet kavramları (toplam, ortalama ve marjinal maliyet)

Üretim miktarı q için toplam maliyet TM tablosu verilmiş; ortalama maliyet OM = TM/q, **marjinal maliyet** MM = ΔTM/Δq olarak hesaplanıyor (örnek: TM 2800'den 3300'e çıkarken Δq = 1 ise MM = 500 gibi; sayfadaki tablonun değerleri tam okunamadı).

## 3. Kuruluş yeri seçimi: ağırlık merkezi yöntemi

C_x = Σ(d_ix · V_i)/ΣV_i ve C_y = Σ(d_iy · V_i)/ΣV_i; burada C_x, C_y ağırlık merkezinin koordinatları, d_ix, d_iy i. talep noktasının koordinatları, V_i o noktaya gönderilen ürün miktarıdır. Örnek: A, B, C, D, E, F talep noktalarının talepleri 400, 300, 200, 100, 300, 100 birimdir; koordinatlar (çözümde okunanlar) A(60, 85), B(80, 75), C(30, 120), D(90, 110), E(127, 30), F(65, 40). Hesap sonucunda **merkez yaklaşık (76,3; 38,3)** bulunmuştur (sayfadaki x değerinin çıkışı okunaklı değil). Bu yöntem merkezi yer verir; yönetici gerçek yer seçerken yakın bir alanı tercih eder.

## 4. Ağırlıklı puanlama yöntemi

Faktör ağırlıkları: toplam ulaşım (%30), işgücü (%10), ulaşım kalitesi (%30), yaşam koşulları (%10), satıcılara yakınlık (%10) olmak üzere her alternatif yer (A, B, C) için faktörlere harf notu (M: mükemmel, VA: vasat altı, V: vasat, I: iyi, Z: zayıf) verilip sayısal puana çevrilir ve Σ w_i · F_i toplamı alınır; örnekte A için 0,30·5 + 0,20·3 + 0,30·3 + 0,1·2 + 0,1·4 = **3,6** bulunmuştur. Alternatifler arasından en yüksek puanlı yer seçilir.

## 5. Birim bulundurma maliyeti ve ekonomik sipariş miktarı

**Soru 1.** Bir firma 50 TL'ye satın aldığı ürünlerin her biri için 5 TL taşıma, 3 TL depolama ve 2 TL sigorta maliyetine katlanıyor. Stokları bulundurma maliyeti oranı %20 olduğuna göre ve firma ortalama 3000 stok bulundurduğuna göre bulundurma maliyetini hesaplayın: birim bulundurma maliyeti = taşıma 5 + depolama 3 + sigorta 2 = 10 TL ile satın alınan malın bulundurma (finansman) maliyeti 50 × %20 = 10 TL toplanarak **20 TL** bulunur; toplam bulundurma maliyeti = ortalama stok × birim bulundurma maliyeti = 3000 × 20 = **60.000 TL**.

**Soru 2.** Bir mağaza 1 yılda 1500 adet erkek takımı satıyor; takım başına bulundurma maliyeti 3 milyon (eski TL), parti başına sipariş maliyeti 2 milyon; mağazanın ekonomik sipariş miktarı nedir? Bulundurma maliyeti %10 ve sipariş maliyeti %5 artarsa yeni ekonomik sipariş miktarı ne olur? Formül Q* = √(2·D·S/H); eski Q = √(2·1500·2.000.000/3.000.000) ve yeni değer Q_y = √(2·1500·2.100.000/3.300.000) ≈ **44** adet bulunuyor (sayfada 44,1).

## 6. Kapasite, geri ödeme süresi

**Kapasite.** Bir konfeksiyon atölyesi yılda 250.000 adet (cep) dikecek; bir makinede işlem süresi cep başına 1,5 dakikadır; makine zamanının %10'u beklenmeyen arızalarla, %3'ü (bant atölyesinde kullanılamayan) süreyle kaybedilmektedir; yılda 250 gün çalışılıyor. Hesapta verimlilik faktörü %90, pratik kapasite = 250 × 8 saat = 2000 saat/makine/yıl, gerekli toplam süre = 250.000 × 1,5 / 0,87 / 0,90 ≈ 429.553 dakika ≈ 7159 saat; makine sayısı = 7159/2000 ≈ **3,58 → 4 makine** alınmalıdır (3 alınırsa 3 makineli kapasite yetmez, 4 alınırsa kullanım düşer).

**Geri ödeme süresi.** Yatırım tutarları A: 15.000, B: 12.000, C: 20.000, D: 10.000; yıllık net nakit girişleri tabloda verilmiştir. Hesaplanan süreler: GÖS_A = 3 + (15.000 − 13.000)/3000 = **3 2/3 yıl**; GÖS_B = 3 + (12.000 − 11.000)/2000 = **3,5 yıl**; GÖS_C = 2 + 5/6 yıl; GÖS_D = 2 + 1/3 yıl (çözümde sayılar okunduğu kadarıyla yazılmıştır). En kısa süreli proje seçilir.

## 7. Net bugünkü değer

**Soru.** %40 iskonto oranıyla A ve B projelerinin (ikisi de 300.000 TL yatırım) net bugünkü değerleri: nakit girişleri A: 100.000, 200.000, 150.000, 250.000, 400.000; B: 200.000, 150.000, 100.000, 250.000, 300.000. NBD = Σ NG_t/(1 + i)^t − yatırım. Sonuç: **NBD_A ≈ 67.585 TL** ve **NBD_B ≈ 76.668 TL**; NBD'si yüksek olan seçilir (kâğıda göre B, A'dan daha yüksek).

**Soru.** Bir araç 1., 2. ve 3. yıl sonunda 200'er TL gelir getirecek; 3. yıl sonunda 1000 TL'ye satılacak; yıllık iskonto oranı %25 iken aracı 950 TL'ye almak kabul edilir mi? NBD = 200/1,25 + 200/1,25² + 1200/1,25³ = **≈ 902,4 TL** < 950 TL; bugünkü değer satın alma bedelinden düşük olduğundan satın alınmamalıdır.

## 8. İç verim oranı ve işletme sermayesi

İç verim oranı, projenin net bugünkü değerini sıfır yapan iskonto oranıdır. İki iskonto oranı (%20 ve %22) için NBD'ler +11,57 ve −124,65 bulunmuşsa, doğrusal enterpolasyonla **İVO = r_p + NBD_p/(NBD_p + |NBD_n|) · (r_n − r_p) = 0,20 + 11,57/(11,57 + 124,65) · (0,22 − 0,20) ≈ %20,17** (sayfada 0,2017).

**İşletme sermayesi ihtiyacı.** Satılan malların maliyeti 1400 olan bir işletmede faaliyet devresi bileşenleri hammadde stoku 20 gün, imalat 5 gün, mamul stoku 20 gün, vade 20 gün (ve satış 5 gün) olarak verilmiştir; faaliyet devresi süresi 20 + 5 + 20 + … gün, faaliyet devri katsayısı = 365/süre ≈ 4,56 ve **işletme sermayesi ihtiyacı = satılan malın maliyeti / faaliyet devri katsayısı = 1400/4,56 ≈ 307**'dir (sayfada 3,06 ≈ 306,x; el yazısı net okunamıyor).
