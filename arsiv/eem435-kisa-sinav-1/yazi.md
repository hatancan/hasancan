---
baslik: EEM435 Bilgisayar Destekli Tasarım: Kısa Sınav I (27.10.2016), Genlik Modülasyonu İşaretinin MATLAB ile Üretilmesi
ozet: Dr. Alparslan Çağrı Yapıcı'nın EEM435 Bilgisayar Destekli Tasarım dersi Kısa Sınav I sorusu: tek tonlu mesaj ve taşıyıcıyla genlik modülasyonu işareti (modülasyon indeksi 0,8) üretimi ve çizimi.
---

Başkent Üniversitesi'nde **EEM 435 Bilgisayar Destekli Tasarım** dersinin (**Dr. Alparslan Çağrı Yapıcı**) **27 Ekim 2016** tarihli **Kısa Sınav I** kâğıdı. Klasörün adı yalnızca "Ders" idi; dersin adı sınav kâğıdından anlaşılıyor. Kâğıtta isim ve numara alanları boştur. Sınavın PDF'i yazının sonunda indirilebilir.

## Soru

Tek tonlu mesaj işareti için **genlik modülasyonu (GM)** işareti

s(t) = A_c·[1 + μ·cos(2π·f_m·t)]·cos(2π·f_c·t)

şeklinde tanımlanıyor olsun. MATLAB kullanarak:

- **a)** f_m = 1 kHz ve A_m = 1 V için mesaj işareti m(t) = A_m·cos(2π·f_m·t)'yi en az üç periyotluk zaman için oluşturunuz.
- **b)** f_c = 20 kHz ve A_c = 1 V için taşıyıcı işareti c(t) = A_c·cos(2π·f_c·t)'yi a şıkkındaki zaman aralığı için oluşturunuz.
- **c)** GM işareti s(t)'yi ilk iki şıktaki mesaj ve taşıyıcı için μ = 0,8 olacak şekilde aynı zaman aralığı için oluşturunuz.
- **d)** Oluşturulan mesaj, taşıyıcı ve GM işaretlerini aynı figür üzerinde ayrı plotlar olacak şekilde çizdiriniz. Her plotun başlığını ve eksen bilgilerini figür üzerinde gösteriniz.

*Notlar: Sorunun yanıtı kâğıtta yoktur. Mesaj periyodu 1 ms'dir, üç periyot 3 ms eder; taşıyıcı 20 kHz olduğundan örnekleme frekansı en az 40 kHz (pratikte 200 kHz gibi çok daha yüksek) seçilmelidir; GM işaretinin zarfı A_c·[1 + 0,8·cos(2π·1000·t)] olup 0,2 ile 1,8 V arasında değişir.*
