---
baslik: EEM474 Güç Elektroniği: Pratik buck tasarımı (Dr. Taufik, Cal Poly)
ozet: PECON 2008 sunumundan buck eleman boyutlandırma, kayıp hesabı, senkron doğrultma, yumuşak anahtarlama ve çok fazlı çalışma.
---

California Polytechnic State University öğretim üyesi Dr. Taufik'in “Practical Design of Buck Converter” başlıklı PECON 2008 eğitim sunumunun 97 sayfası incelenerek anlatımı metne aktarıldı. PDF tarihi 16 Kasım 2008'dir. Laboratuvar fotoğrafları ve veri sayfası alıntıları aktarılmadığından indirme dosyası yoktur.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Çalışma ve boyutlandırma

İdeal sürekli iletimli buck için Vo = DVs. Anahtar iletimdeyken endüktör akımının eğimi (Vs − Vo)/L, kesimdeyken −Vo/L'dir. ΔIL = Vo(1 − D)/(Lf); IL,ort = Io; IL,max/min = Io ± ΔIL/2 kullanılır.

Sürekli akım sınırında IL,min = 0 olur. Kritik endüktans Lkrit = (1 − D)R/(2f) biçimindedir. Sunum, tasarımda bu sınırın üzerinde pay bırakılmasını ve minimum yükte de koşulun denetlenmesini anlatır. Anahtar ile diyodun akım/gerilim zorlanmaları en kötü giriş ve yük koşullarında hesaplanır.

## Kondansatörler

İdeal çıkış kondansatöründe ΔVo = ΔIL/(8fC), üçgensel akımın RMS değeri IC,rms = ΔIL/(2√3)'tür. ESR kaynaklı gerilim dalgalanması ayrıca eklenir. Giriş kondansatörü anahtarın darbeli akımını sağlar; gerilim dayanımı kadar RMS akım değeri de önemlidir.

## 12 V → 2,5 V, 1 A örneği

50 kHz anahtarlama ve 0,1 A sürekli iletim sınırı için D ≈ 0,208 hesaplanır. Kritik endüktans yaklaşık 198 µH'tir; 200 µH seçilir. Tam yükte akım yaklaşık 0,901–1,099 A arasında değişir. Çıkışta %1 dalgalanma hedefiyle ideal kapasite yaklaşık 19,8 µF bulunur; 50 µF seçimiyle ideal dalgalanma yaklaşık %0,396 olur. Sonraki benzetimler açılış geçicisini ve kararlı durum dalga biçimlerini gösterir.

## Kayıplar

MOSFET iletim kaybı Isw,rms² RDS(on) ile değerlendirilir; RDS(on)'un kapı gerilimine ve sıcaklığa bağlılığı gösterilir. Geçişlerde gerilim–akım örtüşmesi anahtarlama kaybına yol açar. Kapı sürme kaybı Qg Vgate f; çıkış kapasitansına bağlı enerji kaybı yaklaşık ½Coss Vin² f biçiminde ele alınır.

Diyotta ileri düşüm, dinamik direnç, ters kaçak, açılma ve ters toparlanma kayıpları ayrı başlıklardır. Endüktörde bakır kaybı IL,rms²RL; çekirdek kaybı frekans, akı salınımı ve malzeme parametrelerine bağlıdır. Kondansatörde kayıp IC,rms²ESR'dir. Toplam kayıp hesaplandıktan sonra verim bulunur.

## Verimi iyileştirme

Düşük iletim direnci, uygun kapı yükü, Schottky diyot, düşük ESR, düşük sargı direnci ve dalgalanmanın azaltılması karşılaştırılır. Frekansı artırmak daha küçük filtre elemanlarına izin verirken anahtarlama ve manyetik kayıpları artırabilir.

Senkron buck'ta serbest dolaşım diyodunun yerine kontrollü MOSFET kullanılır. Ölü zamanda gövde diyodunun iletimi ve ters toparlanma etkileri önemini korur. Sıfır akımda kesim ve sıfır gerilimde açılma örnekleri, geçişteki gerilim–akım örtüşmesini azaltmak amacıyla tanıtılır.

## PWM kontrolcü ve PCB

Akım modu denetimde akım algılama direnci, RC filtre, hata yükselteci ve kompanzasyon ağı incelenir. UC184x/ML38xx ailesi tarihsel örnek olarak kullanılır. Zamanlama direnci/kondansatörü, maksimum görev oranı ve ölü zaman seçimi birbirine bağlıdır. Tip II kompanzasyon örneğinde kesişim frekansı, LC kutbu ve ESR sıfırı dikkate alınır.

Yüksek di/dt yolları kısa tutulur. Giriş dekuplajı anahtarlara, kontrolcü dekuplajı besleme ucuna yakın yerleştirilir. Anahtarlama düğümü hassas geri besleme ve akım algılama yollarından uzak tutulur; toprak düzeni ortak empedans kuplajını azaltmalıdır.

## Çok fazlı buck

Faz kaydırmalı paralel kollar akımı paylaşır, dalgalanmayı azaltır ve ısıyı dağıtır. İki fazın tek fazla karşılaştırıldığı benzetimlerde endüktör akımları, toplam çıkış ve giriş darbeleri birlikte gösterilir. Dinamik yanıt ve daha küçük eleman kullanımı, denetim ve akım paylaşımı gereksinimleriyle beraber değerlendirilir.

*Not: Hesaplar kaynaktaki ideal model ve yuvarlamaları izler. Daha sonra eklenen ESR, yarı iletken düşümleri ve anahtarlama kayıpları nedeniyle ilk ideal hesabın sonucu gerçek devreyle aynı olmaz.*
