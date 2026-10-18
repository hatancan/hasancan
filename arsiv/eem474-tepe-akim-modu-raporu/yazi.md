---
baslik: EEM474 Güç Elektroniği: Tepe Akım Modu Kontrollü Buck Raporu
ozet: PSIM 6 ile eğim kompanzasyonlu buck dönüştürücü: kontrol döngüsü, bobin akımı, çıkış gerilimi ve rampa işaretleri.
---

Başkent Üniversitesi EEM474 Güç Elektroniği dersi için bir arkadaşın hazırladığı **tepe akım modu kontrollü buck dönüştürücü** proje raporudur. Kişisel bilgiler çıkarıldı. Belgede tarih belirtilmemiştir; temizlenmiş PDF yazının sonunda indirilebilir.

## Projenin konusu

Ödev konusu 11: “Peak current mode control (Buck converter) araştırma ve simülasyonu (PSIM 6).” Rapor, eğim kompanzasyonlu bir tepe akım kontrol devresini ve benzetim sonuçlarını içerir.

## Kontrolün açıklaması

Tepe akım modu yüksek performanslı DC/DC dönüştürücülerde kullanılan kontrol yöntemlerinden biridir. Raporun açıklamasında hızlı iç akım döngüsünün referansı izlemesi ve dış döngünün çıkış gerilimini kontrol etmesi üzerinde durulur. Bobin dinamiğinin iç akım döngüsüne alınmasının gerilim döngüsünü kolaylaştırdığı belirtilir.

Devre şemasında buck güç katı, çıkış gerilimi geri beslemesi, karşılaştırıcı, saat, tutucu ve “slope compensation” işareti gösterilmiştir.

## Benzetim çıktıları

- **I(L)–zaman:** Bobin akımının başlangıç geçicisi ve anahtarlama dalgalanması.
- **V_o–zaman:** Çıkış geriliminin yükselerek kararlı duruma yaklaşması.
- **V_m–zaman:** Kontrol işaretinin zaman içindeki seyri.
- **V_slope–zaman:** Eğim kompanzasyonunun periyodik rampa dalgası.

*Not: Rapordaki “%50 Duty döngüsü” açıklaması dil ve anlam bakımından eksiktir; kesin bir kararlılık koşulu olarak yorumlanmamalıdır. Devrenin kaynak şeması ve sayısal çıktı dosyası ayrıca arşivdeki dönüştürücü benzetimleri yazısında ele alınır.*
