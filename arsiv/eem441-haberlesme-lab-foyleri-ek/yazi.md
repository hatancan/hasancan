---
baslik: EEM441 Haberleşme I: Haberleşme laboratuvarı föyleri (Fırat Üniversitesi ve diğer kaynaklar)
ozet: AM/FM laboratuvar föyleri: Fırat Üniversitesi genlik ve frekans modülasyonu deneyi, MC1496 ile AM modülasyon/demodülasyon deneyi ve osiloskop tanıtımı.
---

EEM441 klasöründeki üç yardımcı laboratuvar belgesi: Fırat Üniversitesi Mühendislik Fakültesi Elektrik-Elektronik Mühendisliği Bölümü Haberleşme Laboratuvarı Deney 1 föyü (genlik ve frekans modülasyonu), kaynağı belgede yazılı olmayan "Deney 2: AM modülasyon/demodülasyon" föyü ve kaynağı belirtilmeyen bir "Osiloskop nedir?" yazısı. Orijinal PDF'ler yazının sonundaki ZIP'tedir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Fırat Üniversitesi, Deney 1: Genlik ve frekans modülasyonu

Föy modülasyonu, bildiri işaretini iletime uygun biçime sokma işlemi olarak tanımlar ve modülasyon türünün gürültü, bant genişliği ve verici gücüne göre seçildiğini söyler. Genlik modülasyonu üç türde ele alınır:

1. Tam genlik modülasyonu (FAM)
2. Çift yan bantlı bastırılmış taşıyıcı genlik modülasyonu (DSBSC AM)
3. Tek yan bantlı genlik modülasyonu (SSB AM)

Her tür için tanım, matematiksel ifade ve spektrum verilir (bölüm 2.1 – 2.3). Deneyler: 2.4 kenar frekansların varlığı (alıcının 10,7 MHz'lik IF süzgeci ve kenar bantlar), 2.5 radyo dalga yayınının çift yan bant bastırılmış taşıyıcı sinyalleri (kısa dalga alıcısı ve osiloskop kanalları); 2 kHz ve 1 kHz bildiri işareti durumları ayrı ayrı incelenir. Bölüm 3 frekans modülasyonunu tanımlar (3.1), FM için genel ilkeleri verir (3.2) ve generatör ve alıcı modülleriyle FM deneyini anlatır; deney seti ±15 V güç beslemesiyle çalışır ve osiloskopta üçgen dalga gözlemlenir.

## Deney 2: AM modülasyon ve demodülasyon

**Amaç:** genlik modülasyonu ve demodülasyonuna ilişkin teorik hesapların yapılması; modülatör ve demodülatörün gerçeklenerek temel kavramların incelenmesi.

**Malzemeler:** osiloskop, +12 V / −8 V güç kaynağı, iki işaret üreteci, bir MC1496 (LM1496) entegresi, 51 kΩ, 680 Ω, 3,9 kΩ, 1 kΩ, 6,9 kΩ, 11,5 kΩ ve 10 kΩ dirençler, 50 kΩ potansiyometre, 1 nF ve 100 nF kondansatörler, 1N4148 diyot.

**Ön bilgi.** Temel banttaki işaretin iletime uygun hale getirilmesine modülasyon denir; modülasyondan sonra bilgi yüksek banda taşınır ve anten boyutu küçülür (örnek: 3 kHz'lik ton için 1/10 dalga boylu anten yaklaşık 10 km uzunluğunda olurdu). Taşıyıcılı AM: sAM(t) = (1 + ma m(t)) Ac cos(ωc t + φ) = Ac cos(ωc t + φ) + Ac ma m(t) cos(ωc t + φ). ma modülasyon indeksi aşılırsa aşırı modülasyon oluşur ve bilgi alıcıda bozulmadan elde edilemez. Tek tonlu durumda s(t) = Ac cos(ωc t) + (Ac Am ma/2) cos((ωc + ωm)t) + (Ac Am ma/2) cos((ωc − ωm)t); örtüşme olmaması için fc ≥ 2 fm, gerekli bant genişliği B = 2 fm. Zarf detektörü, doğrusal olmayan bir doğrultucu ve alçak geçiren süzgeçten oluşur; çıkış y(t) = g c0 (1 + ma m(t)) biçiminde, bilgi işareti bir kazanç ve DC ofsetle elde edilir.

**Deneyin yapılışı.**

1. Şekil 1'deki devre kurulur; gerilim uygulamadan önce −8 V, +12 V ve toprak bağlantıları kontrol edilir.
2. Modülatör taşıyıcı girişine 500 kHz, tepeden tepeye 1 V sinüs uygulanır.
3. Bilgi işareti: 200 Hz, tepeden tepeye 0,4 V sinüs.
4. Modülasyonlu işaret entegrenin 6. ucundan gözlenir, çizilir ve modülasyon indeksi hesaplanır.
5. Potun direnci değiştirilerek çıkıştaki değişim gözlenir ve nedeni açıklanır.
6. ma < 1, ma = 1 ve ma > 1 durumlarındaki işaretler çizilir.
7. Şekil 2'deki demodülatör kurulur, modülatör çıkışı girişine verilir; bilgi işareti ile demodülatör çıkışı osiloskopta karşılaştırılır.

## Osiloskop nedir?

Elektriksel değerleri (gerilim, frekans, akım, faz farkı) ışıklı çizgiler olarak gösteren aygıt. Katot ışınlı tüp (ekran, CRT), dikey saptırma, yatay saptırma ve hızlandırma devresinden oluşur. Tüpün arkasındaki flaman ısıtılınca elektron yayar; elektronlar elektron merceği ve hızlandırıcı elektrottan geçip saptırma levhalarının arasından, iç yüzeyi fosforla kaplı ekrana ulaşır. Belge başlangıç seviyesi temel kavramları, osiloskobun yapısını ve çalıştırılmasını anlatır.

*Not: Fırat Üniversitesi föyünün ayrıntılı deney adımları ve şekilleri için ZIP içindeki PDF'e bakınız; burada ana başlıkları özetlendi.*
