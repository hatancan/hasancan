---
baslik: EEM474 Güç Elektroniği: Tek fazlı ve üç fazlı doğrultucular
ozet: Diyotlu ve kontrollü doğrultucular, direnç ve endüktif yük, serbest dolaşım, dalgalanma ve ateşleme açısı.
---

EEM474 ders klasöründeki İngilizce sunumların anlatımı ve formülleri metne aktarıldı. Hazırlayanın adı belgelerde açıkça belirtilmiyor. Fotoğraflar ve kitaplardan alınmış görseller aktarılmadığından bu yazıda indirme dosyası bulunmuyor.

## Tek fazlı kontrolsüz doğrultucular

Yarım dalga doğrultucuda diyot, kaynak sinüsünün uygun yarım periyodunda iletir. Direnç yükünde akım gerilimi izler. Kaynak tepe değeri Vm ise ideal yarım dalga çıkış için Vort = Vm/π, Vrms = Vm/2'dir.

Tam dalga doğrultma, orta uçlu transformatör ve iki diyotla ya da dört diyotlu köprüyle gerçekleştirilir. Köprüde her iletim yolunda iki diyot bulunur. İdeal direnç yükünde Vort = 2Vm/π ve Vrms = Vm/√2'dir. Tam dalga çıkışın temel dalgalanma frekansı şebeke frekansının iki katıdır.

## RL yük ve serbest dolaşım

Endüktör, akım değişimini geciktirir. Kaynak gerilimi sıfırdan geçse de yük akımı hemen sıfıra düşmeyebilir. Akımın sönme açısı β, yükün R/L oranına ve ateşleme koşuluna bağlıdır. Serbest dolaşım diyodu, kaynak yükten ayrıldığında endüktif akımın dolaşabileceği bir yol oluşturur.

Yük akımı için L di/dt + Ri = v(t) denklemi her iletim aralığında ayrı kurulur. Akımın sürekliliği ile gerilimin anahtarlamayla değişebilmesi birbirinden ayrılır.

## Kontrollü doğrultma

SCR ateşleme açısı α ile çıkışın ortalama değeri ayarlanır. Direnç yüklü tek fazlı yarım dalga devrede Vort = Vm(1 + cosα)/(2π); tam dalga kontrollü devrede Vort = Vm(1 + cosα)/π olur. Tam kontrollü köprüde **sürekli akım** varsayımı altında Vort = 2Vm cosα/π elde edilir.

*Not: Sürekli akımlı köprü bağıntısı, direnç yükünün kesintili akım bağıntısı yerine kullanılmamalıdır. Sunumlarda gösterilen farklı dalga biçimlerinin ortalama gerilimleri bu nedenle farklıdır.*

Kaynak endüktansı komütasyonu anlık olmaktan çıkarır. İki iletim grubunun kısa süre birlikte akım taşıdığı komütasyon örtüşmesi, ortalama DC çıkışı etkiler.

## Üç fazlı doğrultucular

Üç fazlı yarım dalga bağlantıda en yüksek faz gerilimine bağlı diyot iletir. Köprüde pozitif bara en yüksek, negatif bara en düşük faza bağlanır. Böylece çıkış, fazlar arası gerilim parçalarından oluşur. Altı darbeli köprüde iletim çifti 60° aralıklarla değişir; her diyot ideal sürekli akım koşulunda 120° iletir.

İdeal diyot köprüsü için ortalama çıkış yaklaşık Vdc = 1,35 VLL,rms'tir. Tam kontrollü üç fazlı köprüde, sürekli akım ve örtüşmesiz komütasyon varsayımıyla Vdc = 1,35 VLL,rms cosα kullanılır. Altı darbeli çıkışın dalgalanma frekansı 6f'dir.

## Filtre ve değerlendirme

Kondansatörlü filtre tepe çevresinde şarj olur, diyot kesimdeyken yükü besler. Daha küçük çıkış dalgalanması sağlanırken giriş akımı dar ve yüksek darbeler hâline gelebilir. Bu nedenle DC çıkışın düzgünlüğü, giriş güç faktörü ve diyot tepe akımı birlikte incelenir.

Proje klasöründeki üç çizim aynı konuları tamamlar: tek fazlı diyot bağlantıları, filtreli çıkış ve üç fazlı köprü. Devreler metinde açıklanmış; görsel dosyalar ayrıca yayımlanmamıştır.
