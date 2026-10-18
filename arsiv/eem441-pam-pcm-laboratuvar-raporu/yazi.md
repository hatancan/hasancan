---
baslik: EEM441 Haberleşme I: PAM ve PCM Laboratuvar Raporu (EEM442 Belgesi)
ozet: Örnekleme, kuantalama, kodlama ve zaman bölmeli çoğullama üzerine anonimleştirilmiş laboratuvar raporu.
---

EEM441 klasöründe bulunan bu arkadaş çalışmasının kapağında EEM442 yazıyor. PAM ve PCM deneyini anlatan rapor, kişisel bilgileri çıkarılarak arşivlendi. Tarihsiz belgenin kaynak dosya tarihi kullanıldı; rapor ve anonimleştirilmiş kapak yazının sonunda indirilebilir.

## PCM: örnekleme, kuantalama ve kodlama

Darbe kod modülasyonu üç aşamayla açıklanıyor: analog işaretin örneklenmesi, örneklerin sonlu sayıdaki seviyeye kuantalanması ve seviyelerin ikili kod sözcüklerine çevrilmesi. Q = 8 seviye, n = 3 bit ve a = 1 için bir örnek çizilmiş.

Deneyde kelime uzunluğu ve bit hızı ayarlanıyor. Osiloskobun birinci kanalı demodülatör çıkışına, ikinci kanalı tetikleme işaretine bağlanıyor. Çıkışta basamaklı dalga gözleniyor; giriş genliği değiştirilince basamak yüksekliğinin sabit kaldığı belirtiliyor.

Bit hızı azaltıldığında çıkış dalgasının sağa kayması, bir sözcüğün tüm bitlerinin alınmasını bekleyen demodülatörün gecikmesiyle açıklanıyor. Rapor ayrıca PCM demodülatöründeki sorun nedeniyle beklenen sonuçların tümünün alınamadığını açıkça belirtiyor.

## PAM ve zaman bölmeli çoğullama

PAM'de darbe genlikleri mesajın örnek değerlerini izler. Rapor düz tepeli örneklemeyi kullanıyor. Kısa darbeler arasındaki boşluklara farklı kanallardan örnekler yerleştirilmesi TDM, yani zaman bölmeli çoğullama olarak anlatılıyor.

Verici ve alıcıdaki dağıtıcı anahtarların eşzamanlı olması gerekir. Her verici anahtar dönüşünde ilgili işaretten bir örnek alınır; alıcı anahtar aynı anda bu örneği doğru çıkış kanalına yönlendirir.

## Örnekleme koşulu

Mesajın bant genişliği fm, örnekleme periyodu Ts ve örnekleme frekansı fs = 1/Ts olarak gösterilmiş. Bant sınırlı mesajı yeniden elde etmek için fs > 2fm koşulu kullanılıyor. Örnekler ideal alçak geçiren süzgeçten geçirilir. Pratik süzgeçler ideal olmadığından Nyquist sınırının üzerinde pay bırakılması gerektiği belirtiliyor.

*Not: Rapordaki “sayısal işaretler gürültüden etkilenmez” ifadesi mutlak anlamda doğru değildir; karar eşiklerinin aşılması bit hatası üretir. PAM'ın tüm biçimleri düz tepeli örnekleme değildir. PCM'nin yalnız 1970'lerde ortaya çıktığı yönündeki tarih ifadesi de kaynağın iddiasıdır, doğrulanmış bir tarih olarak alınmamalıdır.*

## Raporda belirtilen kaynaklar

MEGEP Analog ve Sayısal Haberleşme ders notları, KTÜ telekomünikasyon föyleri, Hasan Balık'ın haberleşme laboratuvarı sayfası ve GYTE deney föyü listeleniyor.
