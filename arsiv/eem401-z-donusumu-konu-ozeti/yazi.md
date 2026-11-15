---
baslik: EEM401 Sayısal Sinyal İşleme: z Dönüşümü Dersleri Ne Anlatıyordu? (Konu Özeti)
ozet: EEM401 Sayısal Sinyal İşleme dersindeki z dönüşümü anlatımının (I–III) konu özeti: tanım ve DTFT ilişkisi, yakınsama bölgesi (ROC), özellikler, ters z dönüşümü ve sabit katsayılı fark denklemlerinin sistem fonksiyonu.
---

2014–2015 güz yarıyılında Başkent Üniversitesi'nde Yrd. Doç. Dr. Selda Güney'den aldığım **EEM401 Sayısal Sinyal İşleme** dersinde z dönüşümü üç sunumda (z Transform I, II ve III) anlatıldı. Bu sunumlar Oppenheim, Schafer ve Buck'ın *Discrete-Time Signal Processing* kitabının içeriğine ve şekillerine dayandığı için **yayımlanmıyor**; aşağıda yalnızca konuların kendi cümlelerimle özeti var. Ayrıntı için kitaba bakınız: A. V. Oppenheim, R. W. Schafer, J. R. Buck, *Discrete-Time Signal Processing*, 2. baskı, Prentice Hall. İndirme dosyası yoktur.

## 1. Tanım ve DTFT ile ilişkisi

z dönüşümü, Laplace dönüşümünün ayrık zamanlı karşılığıdır ve Fourier dönüşümünün genellemesidir. Bir x[n] dizisi için X(z) = Σ x[n] z⁻ⁿ toplamıdır. z karmaşık bir değişkendir (z = r·e^{jω}); r = 1 alındığında, yani z birim çember üzerindeyken z dönüşümü **DTFT**'ye (ayrık zamanlı Fourier dönüşümü) indirgenir. Her dizinin DTFT'si olmayabilir (örneğin |a| > 1 için aⁿu[n]); z dönüşümü, diziyi r⁻ⁿ ile çarparak toplamı yakınsatabildiği için bu durumlarda da işe yarar.

## 2. Yakınsama bölgesi (ROC)

Toplamın yakınsadığı z değerlerinin kümesine **yakınsama bölgesi** denir. Her r değeri z-düzleminde bir çembere karşılık geldiğinden ROC, orijin merkezli çemberlerden oluşan bir halka ya da disktir. Derste vurgulanan kurallar:

- DTFT, ancak ve ancak ROC birim çemberi içeriyorsa vardır.
- ROC kutup içeremez.
- Sonlu uzunluklu dizinin ROC'si (belki z = 0 ve z = ∞ dışında) tüm z-düzlemidir.
- Sağ taraflı dizinin ROC'si en dış kutbun dışına, sol taraflı dizinin ROC'si en iç kutbun içine doğru uzanır; iki taraflı dizinin ROC'si kutuplarla sınırlı bir halkadır.
- Aynı z dönüşümü, ROC verilmeden diziyi tek olarak belirlemez. Örnek: kutupları aynı olan bir H(z) için sistem kararlıysa ROC birim çemberi içermeli, nedenselse sağ taraflı olmalıdır (iki koşul birlikte aranır).

Geometrik seri örnekleri (sağ taraflı üstel dizi aⁿu[n] gibi) ve sık kullanılan dönüşüm çiftlerinin dizi–dönüşüm–ROC tablosu da işlenmişti.

## 3. Özellikler

Dönüşümün temel özellikleri örneklerle incelendi: doğrusallık, zamanda öteleme (n₀ tamsayı; ROC değişebilir), z-düzleminde üstel ile çarpma (ROC ölçeklenir, kutup ve sıfırlar ölçeklenir; çarpan birim genlikli karmaşık sayıysa düzlem döner) ve benzerleri.

## 4. Ters z dönüşümü

Resmî ters dönüşüm Cauchy integraline dayanır; çoğu zaman daha pratik yollar yeterlidir:

- **İnceleme (inspection) yöntemi:** bilinen çiftlerden tanıma.
- **Kısmi kesirlere ayırma:** X(z) oranı polinomlar cinsinden yazılır; M ≥ N ise bir polinom terimi, birinci dereceden kutuplar ve katlı kutuplar için ayrı terimler çıkar; her terim inceleme ile ters çevrilir. Katsayılar kutup değerinde hesaplanır; gerekirse uzun bölme ile polinom kısmı bulunur.
- **Kuvvet serisi açılımı:** z dönüşümü zaten bir kuvvet serisidir; özellikle sonlu uzunluklu dizilerde katsayılar doğrudan dizi değerleridir.

## 5. Sistem fonksiyonu ve tek yanlı z dönüşümü

Üçüncü sunum, **sabit katsayılı fark denklemleri** için sistem fonksiyonu H(z)'yi türetip örnek bir sistem üzerinde (a, b, c şıklarıyla) incelemeye ayrılmıştı: fark denkleminden H(z), kutup-sıfır diyagramı, kararlılık ve nedensellik. Son bölümde **tek yanlı z dönüşümü** ve zaman öteleme özelliği tanıtıldı; bu, başlangıç koşulları olan fark denklemlerini çözmek için kullanılır.

## Bağlantılı yazılar

- Defter notlarım: [z dönüşümü, ters z dönüşümü ve zamanda seyreltmeli HFD](/arsiv/eem401-z-donusumu-ve-hfd-el-yazisi/)
- Dersin önceki konuları: [Ayrık zamanlı işaretler ve sistemler](/arsiv/eem401-ayrik-zamanli-isaretler-ve-sistemler/)
- Sonraki konu: [Sayısal süzgeçler](/arsiv/eem401-sayisal-suzgecler/)
- Sınavlar: [Ara sınav cevap anahtarı 2014](/arsiv/eem401-ara-sinav-cevap-anahtari-2014/), [Final sınavı 2015](/arsiv/eem401-final-sinavi-2015/)

*Not: Bu yazı slaytların kopyası değildir; konu başlıklarının ve dersin akışının kendi sözlerimle özetidir.*
