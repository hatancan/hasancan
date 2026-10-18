---
baslik: EEM474 Güç Elektroniği: Proje ve Araştırma Konuları
ozet: Dönüştürücüler, motor denetimi, güç kalitesi ve benzetim için kişisel bilgilerden arındırılmış proje konuları.
---

EEM474 arşivindeki proje duyuruları ve konu listeleri, öğrenci adları ve dağıtım çizelgeleri çıkarılarak bir araya getirildi. 5 Mayıs 2015 güncellemesi ile yıl belirtilmeyen eski listeler aşağıda ayrı bölümlerde veriliyor. Bu yazı yalnız konu metinlerini içerir; kişi listeleri indirilemez.

## 2015 araştırma ve sunum konuları

Duyuruda iki tercih gönderilmesi, sunum ve benzetimin aynı konudan seçilebilmesi, çalışmaların son hafta teslim edilmesi isteniyor. Sunum 7, benzetim 5 puan üzerinden değerlendiriliyor.

1. Flyback dönüştürücü.
2. Zero current switching dönüştürücü.
3. Zero voltage switching dönüştürücü.
4. SEPIC dönüştürücü.
5. Ćuk dönüştürücü.
6. Matrix converter.
7. Ultrasonik motorlar.
8. Forward dönüştürücü.
9. Çok seviyeli dönüştürücü ve inverterler.
10. Space vector inverter.
11. Senkron buck dönüştürücü.
12. Faz kaydırmalı tam köprü DC/DC dönüştürücü.
13. Motor denetiminde V/Hz ve field oriented control karşılaştırması.
14. Interleaved/multiphase buck dönüştürücü.
15. Forward dönüştürücünün çalışma prensibi ve analizi.
16. İki anahtarlı forward dönüştürücü.
17. Push-pull dönüştürücü.
18. Anahtarlamalı kondansatör dönüştürücüleri.
19. DC/DC dönüştürücüyle güç faktörü düzeltme.
20. Seri rezonanslı DC/DC dönüştürücü.

## 2015 tasarım ve benzetim konuları

Giriş-çıkış gerilimleri ve eleman değerleri seçilerek PSIM ya da MATLAB benzetimi isteniyor.

1. Seri regülatör ve farklı yüklerde performans.
2. Paralel regülatör ve farklı yüklerde performans.
3. Ćuk dönüştürücü.
4. SEPIC dönüştürücü.
5. Tek fazlı cycloconverter.
6. Gerilim geri beslemeli boost.
7. Gerilim geri beslemeli buck-boost.
8. Sıfır geçiş devreli tam kontrollü tek faz AC/DC.
9. Sıfır geçiş devreli yarım kontrollü tek faz AC/DC.
10. ON/OFF kontrollü AC/AC.
11. Flyback dönüştürücü.
12. Forward dönüştürücü.
13. İki anahtarlı forward.
14. Push-pull.
15. Flyback tasarım ve analizi (listede ikinci kez yer alıyor).
16. Seri rezonanslı inverter.
17. Seri rezonanslı DC/DC.
18. Senkron buck.
19. Faz kaydırmalı tam köprü DC/DC.
20. Buck üzerinde average current mode control.

## Eski PSIM 6 proje listesi

İlk 12 konu için örnek devre bulunduğu; bunları seçenlerin araştırma ve benzetim raporunu birlikte hazırlaması gerektiği yazıyor. Üç tercih isteniyor.

1. Flyback modelleme ve benzetimi.
2. ZVS buck araştırma ve benzetimi.
3. ZCS buck araştırma ve benzetimi.
4. Push-pull araştırma ve benzetimi.
5. PLL'nin güç elektroniğinde kullanılması.
6. PWM doğrultucu.
7. Lineer regülatör.
8. Boost PFC.
9. Buck üzerinde average current mode control.
10. Gerilim geri beslemeli faz kontrollü doğrultucu.
11. Buck üzerinde peak current mode control.
12. Space vector inverter.
13. Dead time generator ile yarım köprü DC/AC inverter.
14. SEPIC hesaplama ve benzetimi.
15. Ćuk hesaplama ve benzetimi.
16. Buck-boost hesaplama ve benzetimi.
17. Çok seviyeli inverter.
18. Tek fazlı quasi-square inverter ve dalga üretici.
19. Üç fazlı kare dalga inverter ve dalga üretici.
20. ON/OFF kontrollü AC/AC gerilim dönüştürücü.
21. Tek fazlı faz kontrollü AC/AC.
22. Boost tasarımı.
23. Buck'a ON/OFF denetim uygulanması.
24. Boost'a ON/OFF denetim uygulanması.
25. Tek fazlı kare dalga inverter ve dalga üretici.

## Eski araştırma listesi

Elektrikli araçlar; dynamic voltage restorer (DVR); HVDC iletim; maksimum güç noktası izleme; güneş pilleri; yumuşak anahtarlama; ZVS/ZCS; MATLAB, Simulink ve PSpice gibi yazılımlar; PFC; SEPIC; balast; Ćuk; PWM doğrultucu; matrix converter; indüksiyonla ısıtma; ultrasonik motor; piezoelektrik motor; rüzgâr enerjisi; PaveGen; flyback; rezonanslı dönüştürücüler; kojenerasyon; akıllı güç modülü; senkron motor ve jeneratör; doğrusal motor; direct drive motor; güç kalitesi; çok seviyeli dönüştürücü ve inverterler; akım sensörleri; piezoelektrik transformatör ve dönüştürücüler. Listede öğrencilerin yeni konu önerebileceği de belirtiliyor.

## Eski çizelgelerden tasarım hedefleri

| Dönüştürücü | Giriş | Çıkış | Güç |
| --- | --- | --- | --- |
| Buck | 18–28 V | 12 V | 120 W |
| Boost | 12–16 V | 24 V | 120 W |
| Buck-boost | 10–30 V | 24 V | 120 W |
| Flyback | 260–370 V | 12 V | 20 W |
| Push-pull | 260–370 V | 12 V | 250 W |
| Tam köprü | 260–370 V | 48 V | 1000 W |

Ek konular: sinüzoidal olmayan işaretlerin RMS ve faz farkını ölçme; 8 bit DAC ve lookup table ile 0–440 Hz tek faz SPWM üretme; dsPIC/C30 ile bir ve üç faz inverter; quadrature encoder ile hız/konum ölçme; LM3524 ile boost, Ćuk ve buck-boost; aktif filtre; tek çevrim denetimi; ölü zamanın harmoniklere etkisi ve düzeltme; V/f motor denetimi; inverterlerde akım denetimi; interharmonikler; wavelet, Kalman filtresi, yapay sinir ağı, destek vektör makinesi ve neurofuzzy ile harmonik analizi.

## Aynı çalışma kitaplarındaki mikrodenetleyici konuları

L298 ile DC motor yön/hız denetimi; unipolar ve bipolar adım motoru; RC servo; encoder darbelerinden hız hesabı; Sharp sensör verisiyle lookup table veya fuzzy doğrusallaştırma; CCP ile darbe genişliği ve frekans ölçme; üç konumlu ve ölü bantlı denetim; PWM ile sinüs; seri ADC ve LCD; bulanık mantıklı robot; CAN/USB; C ve Proteus ile bulaşık makinesi benzetimi; EEPROM'a kayıt. Son EEPROM satırı kaynakta tamamlanmamış.

*Not: Eski çizelgelerde Mayıs güncellemeleri var, yıl yok. Bunlar 2015 listesiyle aynı döneme aitmiş gibi birleştirilmedi. Duyurular arşiv belgesidir; güncel teslim ya da tercih çağrısı değildir.*
