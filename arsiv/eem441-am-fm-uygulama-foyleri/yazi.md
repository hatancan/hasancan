---
baslik: EEM441 Haberleşme I: AM ve FM Uygulama Föyleri
ozet: ANACOM setlerinde AM ve FM deneyleri: ön çalışmalar, ölçüm noktaları, süperheterodin alıcı, demodülasyon ve gürültü deneyleri.
---

Başkent Üniversitesi **EEM441 Haberleşme I** dersinin iki uygulama föyü, genlik modülasyonu (AM) ve frekans modülasyonu (FM) deneylerini anlatıyor. Hazırlayan ve tarih belirtilmemiştir. Föylerin PDF kopyaları yazının sonunda ZIP olarak indirilebilir.

## Uygulama 1: Genlik modülasyonu

Amaç, genlik modülasyonunu uygulamalı olarak incelemek, verici ve alıcıdaki işlemleri deney seti üzerinde çalışarak teorik konuları pekiştirmektir.

### Ön çalışma

1. Şekildeki kare dalga için f_c = 1 MHz taşıyıcı ile çift yanbantlı, taşıyıcılı AM işaretini zaman ve frekans alanında çiziniz; MATLAB benzetimini yapınız.
1. Aynı mesaj için çift yanbantlı, taşıyıcısı bastırılmış DSB-SC AM işaretini zaman ve frekans alanında elde ediniz.
1. Süperheterodin alıcının özelliklerini ve diğer alıcı türlerini araştırınız.
1. Genlik modülasyonunun günümüzdeki kullanım alanlarını araştırınız.

Kare dalganın seviyeleri +1 ve −1, yatay eksenin birimi ms'dir. Pozitif aralık 0–3 ms, negatif aralık 3–6 ms olarak gösterilmiştir; sinyal periyodiktir.

### Verici ve alıcı

ANACOM 1/1 vericisi DSB ve SSB AM yapabilir. Ses osilatörü modülasyon sinyalini sağlar. Dengeli modülatör taşıyıcıyı bastırır. Çıkış yükselteciyle kuvvetlendirilen işaret alıcıya kabloyla aktarılabilir veya antenden yayınlanabilir.

ANACOM 1/2 alıcısı süperheterodindir. Taşıyıcılı DSB için diyot dedektörü, SSB için çarpım dedektörü vardır. Dedektör çıkışı ses yükseltecine ve hoparlöre bağlıdır.

### Vericide ölçümler

1. Ses osilatöründen bir ton seçerek AM DSB modülatörüne veriniz. t.p.1 ve t.p.9 işaretlerini kaydediniz.
1. t.p.1'i tetikleme işareti yaparak t.p.3'ü görüntüleyiniz. İşaretin çift yanbantlı AM olup olmadığını inceleyiniz; Balance düğmesini test ediniz.
1. Zarfın V_max ve V_min değerlerinden modülasyon yüzdesini bulunuz: m = [(V_max − V_min)/(V_max + V_min)] × 100%.
1. Tonun genliğini ve frekansını değiştirerek t.p.3'teki değişimleri kaydediniz.

### Verici ayarları

- Ses yükselteci genlik ayarı, dengeli modülatör/bant geçiren filtre denge ayarı ve çıkış yükselteci kazancı maksimumda olmalıdır.
- Mod anahtarı DSB, Tx çıkışı ANT. konumunda olmalıdır.
- Hoparlör açık, anten tamamen çıkarılmış ve dik olmalıdır.

### Alıcı ayarları

- Rx girişi ANT., RF ayar devresi INT konumunda olmalıdır.
- RF yükselteci kazancı maksimum; AGC devrede olmalıdır.
- Dedektör anahtarı Diyot konumunda olmalıdır.
- Ses yükselteci genliği minimuma yakın, hoparlör açık olmalıdır.
- Beat Frequency Oscillator kapalı; anten açık ve dik olmalıdır.

### Alıcıda ölçümler

1. Tuning dial ile gönderilen istasyonu bulunuz.
1. RF yükselteci çıkışını AC bağlı osiloskopla gözleyiniz.
1. Karıştırıcı, yerel osilatör sinüsü ile RF işaretini çarpar. Yerel osilatör frekansı RF taşıyıcısından 455 kHz fazladır. Çıkış spektrumundaki bileşenleri hesaplayınız: f_LO = f_AM + f_IF, f_IF = 455 kHz.
1. t.p.20'yi AC coupling ile inceleyiniz; frekans ayarıyla temel bileşenin değişimini gözleyiniz.
1. IF yükselteçlerinin t.p.24 ve t.p.28 çıkışlarını inceleyiniz.
1. Diyot dedektörünün t.p.31 çıkışını çiziniz.
1. Ses yükseltecinin t.p.39 çıkışını inceleyerek raporu düzenleyiniz.

## Uygulama 2: Frekans modülasyonu

Amaç, frekans modülasyonunu uygulamalı olarak incelemektir.

### Ön çalışma

1. VCO, yani gerilim denetimli osilatörün çalışmasını şekille açıklayınız.
1. FM ve AM arasındaki farkları karşılaştırınız.
1. MATLAB'da kendi kodunuzla FM gerçekleştiriniz. Mesajı ve taşıyıcıyı seçerek değerlerini grafik üzerine yazınız.
1. Deney setinin blok şemasını inceleyiniz.

Föyde deneye hesap makinesi getirilmesi hatırlatılıyor. Set; ses osilatörü, reaktans ve varaktör modülatörleri, karıştırıcı/yükselteç, genlik sınırlayıcı, ayarlı rezonans devresi, Foster–Seeley/oran dedektörü, quadrature dedektörü, PLL dedektörü ve alçak geçiren filtre/yükselteç bloklarını içerir.

### FM modülasyon

1. Ses osilatörü çıkışını modülatör girişine bağlayınız.
1. Reactance–Varactor anahtarını Reactance konumuna getiriniz.
1. Carrier Frequency ayarını orta konuma getiriniz.
1. Bir ses işareti seçerek t.p.34 Mixer/Amplifier çıkışını inceleyiniz. Ses genliğini minimum yapınız; görülen FM taşıyıcısının genlik ve frekansını ölçünüz.
1. Ses genliğini maksimum yapınız. Ekranda 10–15 periyot gözleyerek salınımların değişimini kaydediniz. Mesaj genliğinin FM'e etkisini ve bu etkinin nasıl daha iyi gözlemleneceğini tartışınız.

### FM algılama ve demodülasyon

1. Ayarlı rezonans devresi girişine 1 V_pp, yaklaşık 455 kHz sinüs bağlayınız. Girişten harici tetikleme alarak çıkışı gözleyiniz.
1. Frekansı 455 kHz çevresinde değiştirerek t.p.40 DC seviyesinin maksimumunu bulunuz. 435 ve 475 kHz için de ölçerek çıkış gerilimi–giriş frekansı grafiğini çiziniz.
1. Genlik sınırlayıcı hariç tüm bağlantıları yapınız. t.p.40'ta pozitif DC seviye, t.p.14'tekine benzer sinüs ve küçük genlikli yüksek frekans dalgalanması bulunup bulunmadığını inceleyiniz.
1. t.p.73'ü t.p.40 ile karşılaştırınız. Mesajın genliği ve frekansını değiştirerek çıkış işaretini çiziniz.

### Gürültünün etkisi

1. Gürültü girişine 100 mV_pp, 2 kHz sinüs bağlayınız. t.p.5 ile tetikleyip t.p.34'te FM üzerinde genlik modülasyonu oluşup oluşmadığını inceleyiniz.
1. t.p.73'teki işareti inceleyiniz.
1. Mesaj genliğini sıfırlayarak t.p.73'te kalan gürültü genliğini ölçünüz.
1. Genlik sınırlayıcıyı devreye alıp etkisini gözleyiniz.
1. Aynı işlemleri Quadrature Detector bloğuyla tekrarlayınız ve iki demodülatörü karşılaştırınız.
1. Raporu düzenleyip teslim ediniz.

*Not: FM föyünün 7. adımında “sinyal üretecini çıkartıp girişin frekansını” değiştirmek yazıyor; bağlantı ifadesi belirsizdir. Sonraki ölçümler giriş frekansının değiştirilmesini gerektiriyor. Ayrıca 14. adımın “7–14” göndermesi kendi adımını da kapsıyor; kaynak ifadesi bu şekildedir.*
