---
baslik: EEM474 Güç Elektroniği: 2004–2006 final soruları ve çözümleri
ozet: Ocak 2004, Eylül 2004, Eylül 2005 ve Ocak 2006 sınavlarından doğrultucu, kıyıcı, komütasyon ve PWM çözümleri.
---

EEM474 klasöründeki dört final çözüm sunumu bu yazıda birleştirildi: Ocak 2004, Eylül 2004, Eylül 2005 ve Ocak 2006. El yazısıyla eklenen cevaplar kaynakta bulunduğu biçimde değerlendirilmiştir. Sunumların PDF kopyaları yazının sonundaki ZIP'tedir.

## Ocak 2004

Evirici, DC kaynaktan genliği ve frekansı belirlenmiş AC çıkış üreten devre olarak tanımlanır. 200 V giriş, 5 Ω–10 mH yük, 500 Hz ve %75 görev oranlı kıyıcıda Vort = 150 V, Iort = 30 A verilir.

Endüktif AC yükte akımın gerilimden geri kalması ve ideal endüktörde 90° faz farkı çizilir. Üç fazlı kontrollü köprü sorusunda ateşleme ve 15° komütasyon örtüşmesi dikkate alınır; kaynak çözüm yaklaşık 233,69 V sonucunu gösterir.

Kapasitif komütasyonlu iki tristörlü devrede 50 V ve 5 A için yük direnci 10 Ω'dur. 30 µs sönme süresine göre kaynakta Cmin ≈ 4,33 µF, seçilen C = 5 µF, τ = 50 µs ve fmax = 2 kHz yazılmıştır. Son frekans, periyotta iki komütasyon ve her biri için 5τ kabulüne dayanır.

## Eylül 2004

AC akkor lambanın parlaklığı için triyak; yüksek akım/gerilim ve düşük frekanslı DC kıyıcı için GTO cevabı verilmiştir. Doğrultucuda komütasyon örtüşmesinin ortalama çıkışı düşürdüğü belirtilir.

4 kV kaynaktan 250 A çeken motorun anma gücü 1000 kW olarak hesaplanır. GTO 10 kHz ve %85 görev oranıyla sürülmektedir; ideal anahtar varsayımı kullanılır.

Direnç yüklü yarım dalga kontrollü doğrultucuda α = 30° için genel ortalama ifade Vm(1 + cosα)/(2π)'dir. Üç fazlı köprüde α = 60° ve 15° örtüşme ile faz gerilimleri, tetikleme sırası ve çıkış gerilimi çizilir; el yazısı cevap yaklaşık 115 V verir.

20 V → 5 V buck için D = 0,25'tir. 50 kHz anahtarlama, anahtarlama frekansının onda biri olan 5 kHz LC rezonansı ve 2500 µF kapasiteyle L = 1/[(2πfLC)²C] ≈ 0,405 µH bulunur.

*Not: Bu son L değeri yalnız sorunun verdiği rezonans koşulundan çıkar. Sürekli akım, doyma ve yük akımı koşulları ayrıca verilmediğinden tamamlanmış pratik tasarım sayılmaz.*

## Eylül 2005

Tek bölgede çalışan DC motor için kontrollü DC besleme çizilir. Tam kontrollü ve kontrolsüz tek fazlı köprüde eleman sayısı karşılaştırılır; her ikisinde dört doğrultucu elemanı bulunur. PWM'de bipolar/unipolar çıkışın harmonikleri tartışılır.

Tek tristörlü AC denetleyicide α = 45° için RMS integrali iletim aralığı üzerinden kurulur. Üç fazlı köprü sorusunda 15° komütasyon örtüşmesi ve tetikleme sırası yeniden ele alınır.

24 V girişten büyüklüğü 50 V olan tersleyen buck–boost çıkışı için 50/24 = D/(1 − D), D ≈ 0,676 bulunur. İdeal güç eşitliğinden |Io|/Ii = 24/50 = 0,48'dir.

*Not: Çözümde bazı gerilim oranları pozitif büyüklüklerle yazılmıştır. Tersleyen buck–boost'un işaretli oranı Vo/Vi = −D/(1 − D)'dir.*

## Ocak 2006

Kapı devresindeki R ve zenerin koruma/sınırlama görevi; yüksek gerilim ve akımda SCR seçimi; 24 V'tan 0–50 V ayarlanabilir çıkış için buck–boost bağlantısı sorulur. Kapasitif komütasyonda başlangıç kondansatör gerilimi sıfır kabul edilir ve geçici dalga biçimleri incelenir.

24 V transformatör çıkışıyla beslenen tam kontrollü köprüde 45° ateşleme ve 15° komütasyon süresi kullanılır. Kaynak çözümün yaklaşık çıkış sonucu 13 V'tur. H-köprü kollarının görev oranları %70 ve %40 ise Vort = Vd(0,7 − 0,4) = 0,3Vd yazılır.

*Not: Sunumlardaki “unipolarda daha az harmonik” cevabı, verilen PWM koşulları bağlamında okunmalıdır; bütün frekanslarda ve bütün ölçütlerde değişmez bir üstünlük ifadesi değildir. Ay bilgisi bulunan sınavlara kaynakta olmayan gün eklenmedi.*
