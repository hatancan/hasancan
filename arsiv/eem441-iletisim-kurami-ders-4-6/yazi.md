---
baslik: EEM441 Haberleşme I: İletişim Kuramı ders sunumları 4–6 (ELK 307, Nihat Kabaoğlu): genlik modülasyonu
ozet: Genlik modülasyonu, DSB-SC, tek yan bant, artık yan bant, dik taşıyıcılı ve frekans bölmeli çoğullama konularını içeren ders sunumları.
---

ELK 307 İletişim Kuramı-I dersinin genlik modülasyonu bölümü (Kısım-4): Ders 4 ve 5 sunumları ile Ders 6'daki problem çözümleri (taranmış, yalnız PDF'te). Ders sunumları ELK 307 İletişim Kuramı-I dersine ve Nihat Kabaoğlu'na aittir (kurum belgede yazmıyor); EEM441 klasöründe bulunduğundan bu derse eklendi. Sunumların PDF kopyaları yazının sonundaki ZIP'tedir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Ders 4: Genlik modülasyonu ve çift yan bant

### İçerik

Çift Yan Bant Modülasyonu Tek Yan Bant Modülasyonu Artık Yan Bant Modülasyonu  Dik Taşıyıcılı Çoğullama  Frekans Bölmeli Çoğullama

### Genlik Modülasyonu(GM)

Modüle edilmiş sinyal, modüle eden bir sinyal ile (mesaj) modüle edilen bir sinyalden (taşıyıcı) elde Modüle edilmiş sinyal Modülatör genlik duyarlılığı W bantgenişlikli m(t) sinyalinin yeniden elde edilebilmesi için ka m (t ) < 1 ve f c  W koşulunun

### Spektrum

Çift Yanbantlı Geniş Taşıyıcılı Genlik Modülasyonu

### Örneğe Devam

Üst Yanbant Gücü = μ Ac Alt Yanbant Gücü = μ Ac

### Genlik Modüleli Sinyallerin Üretimi

 Genlik modülasyonunda fc+fm ve fc-fm gibi yeni frekans bileşenlerinin ortaya çıktığı görüldü. Yeni frekans bileşenleri üretebilmek için genlik modüleli sinyal üreten elemanın ya doğrusal olmayan ya da zamanla değişen özelliği olmalıdır.  Doğrusal ve zamanla değişmeyen elemanlar yeni frekans bileşenleri üretemez.

 Kullanılan iki yöntem vardır: Kare Alma Yöntemi (Karesel Modülatör) Anahtarlama Yöntemi (Anahtarlamalı Modülatör) Bant Geçiren Filtre Bant Geçiren Filtre tarafından süzülür . Bant Geçiren Filtreden geçer .

### Karesel Modülatör Örneği

BGF tarafından süzülür

### Örnek

mesaj sinyali ile, modülasyon yüzdesi %25 ve taşıyıcı gücü 50 W olan bir AM sinyalini üretecek karesel modülatörü

Bir önceki örnekte üretilen AM sinyalinin zaman bölgesindeki şeklini ve genlik spektrumunu sayısal değerleri ile çiziniz.

### Anahtarlamalı Modülatör

Taşıyıcı frekansı etrafındaki yanbantlar (çift yanbant terimi) Taşıyıcının üçüncü harmoniği sGM ( t ) = m ( t ) cos ( 2π f c t ) + Ac cos ( 2π f c t )

### Anahtarlamalı Modülatör Örneği

Parçalı Doğrusal Modülatör RL direnci yerine merkez frekansı fc olan, bantgenişliği ise 2fm olan bir BGF kullanılırsa, çıkış aşağıdaki gibi olur.

Bu devre basit bir anahtarlamalı modülatör devresidir. Burada anahtar olarak bir diyot köprüsü kullanılmıştır. Anahtarlamanın fc Hz frekansında olabilmesi için diyot köprüsüne fc Hz frekansında bir osilatör uygulanmıştır.

### Akortlu Devre Modülatörü

Bu yöntem yüksek güç düzeylerinde genlik modüleli sinyal elde etmek için kullanılır. Bu modülatör, anodundan modülasyon verilen C sınıfı bir yükselteç olarak çalışır. Standart genlik modüleli vericilerde bu tür modülatörler yaygın olarak kullanılır. Triyot yerine pentot tüp ya da yüksek güçlü yarı iletken eleman kullanılabilir.

### Genlik Modülasyonlu Bir Vericinin

Yüksek düzeyli modülatör içeren bir genlik modülasyonlu vericinin blok diyagramı aşağıda verilmiştir. Taşıyıcı frekansının kararlı olabilmesi için taşıyıcı dalga kristal denetimli bir osilatör tarafından üretilir.

### GM Sinyallerin Demodülasyonu

 Genlik modülasyonunda demodülasyon iki yöntem kullanılarak yapılır. v1 ( t ) = sGM ( t ) ALO cos ( 2π f c t ) cLO ( t ) = ALO cos ( 2π fct )

İkinci harmonik bozulması Bozulma Oranı = Dikkat!!! Bozulma oranı ka<1 yapılarak azaltılabilir!

### Taşıyıcısı Bastırılmış (TB)

TB Genlik Modüleli sinyal 3. Kare Yasası Modülatörü (Square Law Modulator) TB Genlik Modülasyonlu Sinyal

### Ring Modülatörü Çıkış Spektrumu

Arzu edilen sinyal

### TB-ÇYB GM

v ( t ) = ALO cos ( 2π f c t + φ ) s ( t ) = Ac ALO cos ( 2π f c t ) cos ( 2π f c t + φ ) m ( t ) Ac ALO cos ( 4π f c t + φ ) m ( t ) + Ac ALO cos (φ ) m ( t )

## Ders 5: Tek yan bant, artık yan bant ve çoğullama

### İçerik

Çift Yan Bant Modülasyonu Tek Yan Bant Modülasyonu Artık Yan Bant Modülasyonu  Dik Taşıyıcılı Çoğullama  Frekans Bölmeli Çoğullama

### Tek Yan Bant(TYB) Modülasyonu

TB-GM sinyalindeki yanbantlardan biri çıkarılırsa tek yanbant sinyali Bu sayede verici gücü ve bantgenişliği yarıya indirilir. Bantgenişliği az olması nedeniyle TYB modüleli sinyaller GM ve TB-GM sinyallerine oranla sönümleme (fading)’ den daha az etkilenir. TYB modülasyonu, önemli miktarda alçak frekans bileşenleri olan sinyaller için uygun değildir. TYB modülasyonu 2-25MHz arasında askeriye ve polis teşkilatında telsiz haberleşmesi için kullanılır. Alıcı yapısı karmaşık ve pahalı olduğundan radyo yayıncılığı için TYB sinyali iki yöntemle üretilir. Süzgeç ya da Frekans Ayırma Yöntemi Faz Kaydırma ya da Faz Ayırma Yöntemi

### TYB Modülasyonu

s (t ) cos (2π f c t ) = sc (t ) cos 2 ( 2π f c t ) − ss (t ) sin (2π f c t ) cos (2π f c t )

### TYB Modüleli Sinyallerin Üretimi

Filtre Yöntemiyle TYB Sinyalinin Üretilmesi Bu yöntem TB-GM sinyaldeki yanbantlardan birinin filtre ile süzülerek bastırılması ilkesine dayanır ve faz kaydırma yöntemine göre daha basittir. Keskin kesimli filtrelerin tasarımı alçak frekanslarda daha kolay olacağı için TYB sinyali bu frekanslarda üretildikten sonra yüksek frekanslara kaydırılır. Bu sayede, istenen frekans bileşenlerinden yeteri kadar uzakta bulunan, yüksek frekanslı, istenmeyen frekans bileşenlerini bastırmak için keskin kesimli olmayan filtreler yeterli olur. Yanbant filtresinin geçiş bandı istenilen yanbandı içine almalı ve geçiş bandı mesaj sinyalinin en küçük frekans bileşeninin en çok iki katı kadar olmalıdır.

Radyo frekansında seçiciliği yüksek süzgeçler yapmak zor olduğundan modülasyon iki aşamada yapılır.

### Tek Yan Bant(TYB) Modülasyonu

Faz Kaydırma Yöntemiyle TYB Sinyalinin Üretilmesi İki sinyal toplanırsa AYB, çıkarılırsa ÜYB sTYB (t ) = Ac m (t ) cos (2π f c t ) ∓ Ac mˆ (t ) sin (2π f c t ) Hartley modülatörü olarak da bilinir.

Faz Kaydırma Yöntemiyle TYB Sinyali Üretilmesi İstenilen bant genişliği boyunca sabit faz kaydırıcı yapmak pratikte zor olduğundan, farkı 90o olan iki ayrı kaydırıcı devre kullanır. sTYB (t ) = Ac m (t ) cos (2π f c t ) ∓ Ac mˆ (t ) sin (2π f c t ) İki sinyal toplanırsa AYB, çıkarılırsa ÜYB

### TYB Modüleli Sinyallerin

TYB modüleli sinyallerin demodülasyonu için iki yöntem uygulanabilir.

Demodülasyonda Δf kadar frekans hatası olması durumunda çıkış TYB+ ve Δf < 0 veya TYB− ve Δf > 0 TYB+ ve Δf > 0 veya TYB− ve Δf < 0

Demodülasyonda Δφ kadar faz hatası olması durumunda çıkış Donald Duck ses etkisi

Zarf çözümü için TYB modüleli sinyal ile büyük genlikli taşıyıcıya gerek vardır. Vericiden gönderilen pilot(klavuz) taşıyıcının alıcıda filtrelenip genliğinin yükseltilmesiyle elde edilir. Sonra da, TYB modüleli sinyal ile elde edilen bu büyük genlikli taşıyıcı zarf çözücüye uygulanarak TYB

s1 ( t ) = m ( t ) cos ( 2π f c t ) + mˆ ( t ) sin ( 2π f c t ) + (ξ + Ac ) cos ( 2π f c t ) = m ( t ) cos ( 2π f c t ) + mˆ ( t ) sin ( 2π f c t ) + Ac cos ( 2π f c t ) ; Taşıyıcı büyük değerli olduğundan Bu nedenle kareli terimler çok küçük değerli olacağından ihmal edilebilir. Bu durumda, büyük taşıyıcılı sinyalin zarfı aşağıdaki gibi yazılabilir. Binom açınımı yardımıyla şu ifadeye ulaşılır: O halde zarf çözücü çıkışındaki sinyal budur. Kondansatör çıkışındaki sinyal ise s3 ( t ) = m ( t ) olarak bulunur.

### Artık Yanbant (AYB) Modülasyonu

Bazı durumlarda yanbantlardan biri tamamen ayrılıp alınamaz. Dolayısıyla, TYB modülasyonu kullanılamaz. Bu tür sinyaller için AYB modülasyonu kullanılır.  Yanbantlardan biri tamamen diğeri ise kısmen alınarak  Bantgenişliği W ile 2W arasındadır.  TB-GM ve TYB modülasyonları AYB modülasyonunun özel  Televizyon yayınlarında görüntü sinyali AYB modülasyonu ile

### Artık Yanbant Modülasyonu

AYB sinyalinin spektrumunu şekillendirecek süzgeç transfer fonksiyonu H(f) ne olmalıdır? Eşzamanlı demodülasyon altında, sezinleyici (AGF) çıkışındaki mesaj sinyalinin bozulmasız olarak elde edilebilmesi için Hv(f) nin sağlaması gereken şart tespit edilir.

v ( t ) = ALO cos ( 2π fc t ) sAYB ( t ) olmaması için sabit Öyle ki, HV ( f − f c ) + HV ( f + f c ) = 2 HV ( f c ) koşulu sağlanmalıdır.

Artık Yanbant Süzgeci Yani fc noktasına göre tek simetri özelliğine

Zaman ifadesi s AYB ( t ) =

### AYB Modüleli Sinyallerin

AYB modüleli sinyallerin demodülasyonu için iki yöntem de uygulanabilir. 2. Zarf Çözümü (Büyük Taşıyıcılı) v ( t ) = ALO cos ( 2π fc t ) sAYB ( t )

Büyük taşıyıcılı AYB sinyalinin zaman alanı ifadesi: = m (t ) cos (2π f c t ) − mˆ (t ) sin (2π f c t ) + gˆ (t ) sin (2π f c t ) s AYB+BT (t ) = s AYB (t ) + Büyük Taşıyıcı = m (t ) cos (2π f c t ) − mˆ (t ) sin (2π f c t ) + gˆ (t ) sin (2π f ct ) + Ac cos (2π f ct )

Bu sinyali tek bir sinüzoidal olarak ifade edersek, zarfını şöyle yazabiliriz: olduğundan, zarf çözücü çıkışında Tıkama kondansatöründen geçtikten sonra çözücü çıkışında s0 (t ) = m (t ) elde edilir. Büyük taşıyıcı, TYB çözümünde olduğu gibi, kılavuz taşıyıcının filtrelenip yükseltilmesi ile elde edilebilir.

## Ders 6: Problem çözümleri

Ders 6 dosyası genlik modülasyonu bölümünün problem çözümlerini taranmış sayfalar olarak içerir (ilk problem, demodülatörde yalnız faz bozulması bulunması durumudur); metni çıkarılabilir değildir, ZIP içindeki PDF'ten okunabilir.

*Not: Metin, slaytlardan otomatik çıkarılıp düzenlendi; denklemler ve şekiller metne dökülemediğinden ilgili kısımlar atlanmıştır. Tam hâli için yazının sonundaki PDF dosyalarına bakınız.*
