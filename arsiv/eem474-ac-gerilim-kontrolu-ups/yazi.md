---
baslik: EEM474 Güç Elektroniği: AC gerilim kontrolü ve kesintisiz güç kaynakları
ozet: Tam periyot ve faz açısı kontrolü, siklokonvertörler, AC–DC–AC dönüşüm ve UPS çalışma blokları.
---

EEM474 ders klasöründeki İngilizce sunumların anlatımı ve formülleri metne aktarıldı. Hazırlayanın adı belgelerde açıkça belirtilmiyor. Fotoğraflar ve kitaplardan alınmış görseller aktarılmadığından bu yazıda indirme dosyası bulunmuyor.

## AC–AC dönüştürme

AC gerilim denetleyicisi çıkışın etkin değerini değiştirir. Frekans dönüşümü doğrudan siklokonvertörle veya doğrultucu, DC ara devre ve evirici üzerinden dolaylı olarak gerçekleştirilebilir. Sunumda temel uygulamalar ısıtma, ışık ve motor denetimi olarak ele alınır.

## Tam periyot kontrolü

n periyot iletim ve m periyot kesim için k = n/(n + m) tanımlanır. Direnç yükünde Vo,rms = Vs,rms√k, Po = kVs,rms²/R ve giriş güç faktörü √k olur. Anahtarlar tam çevrim grupları boyunca iletimde tutulur.

120 V beslemede n = 25, m = 75 için k = 0,25, çıkış 60 Vrms ve güç faktörü 0,5'tir. Isıl zaman sabiti uzun yükler bu çalışma biçimine örnek gösterilir.

## Faz açısı kontrolü

Ters paralel iki tristör veya uygun bir triyak, her yarım periyotta α açısına kadar beklenerek tetiklenir. Direnç yükünde iletim yarım periyot sonunda sona erer. Çıkış etkin değeri:

Vo,rms = Vs,rms √[(π − α + sin(2α)/2)/π]

R = 10 Ω, Vs = 120 Vrms, f = 60 Hz ve α = π/2 için Vo,rms ≈ 84,85 V; güç faktörü yaklaşık 0,707'dir. Endüktif yükte akım sıfırı gerilim sıfırıyla çakışmadığından iletim ve sönme açıları ayrıca hesaplanır.

## Siklokonvertör ve dolaylı dönüşüm

Doğrudan yöntemde pozitif ve negatif doğrultucu grupları kaynak geriliminin parçalarından düşük frekanslı bir çıkış oluşturur. Dolaylı yöntemde önce DC ara gerilim üretilir, ardından evirici istenen frekansa göre sürülür. Ara devrenin filtre ve enerji depolama elemanları iki dönüşüm kademesini birbirine bağlar.

## UPS blokları

Kesintisiz güç kaynağında doğrultucu/şarj devresi, akü, evirici ve transfer veya bypass düzeni bulunur. Normal şebeke koşulu ile şebeke kesintisindeki enerji yolu ayrı gösterilir. Çevrim içi düzende yük sürekli evirici üzerinden beslenir; beklemeli düzende kesintide yedek enerji yoluna geçilir.

Sunumda aküden AC üretimi, transformatörlü çıkış ve PWM kontrolünün blok ilişkileri anlatılır. Kitaptan alınmış devre sayfaları ile ürün fotoğrafları bu metne eklenmedi.

*Not: “Güç faktörü = cosφ” ifadesi faz kontrollü, sinüzoidal olmayan akım için tek başına yeterli değildir. Buradaki PF hesapları aktif gücün görünür güce oranına dayanır.*
