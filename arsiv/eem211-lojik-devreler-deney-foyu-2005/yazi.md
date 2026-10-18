---
baslik: EEM211 Sayısal Mantık Tasarımı: Lojik Devreler İçin On Deney (Kaynağı Belirtilmemiş Föy)
ozet: TTL ve CMOS karakteristiklerinden sayıcı ve yazıcılara uzanan 68 sayfalık laboratuvar föyü.
---

2005 tarihli “LOJIK DEVRELER.pdf”, kapı devrelerinin fiziksel gerçeklenmesini ve on laboratuvar deneyini içeren 68 sayfalık bir föy. Belgede hazırlayan kişi ve kurum belirtilmiyor; EEM211 klasöründe bulunan üçüncü taraf ders materyali olarak arşivlendi. PDF oluşturma tarihi 4 Şubat 2005. Belgenin tamamı yazının sonunda indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Giriş: lojik kapıların gerçeklenmesi

Föy boyunca pozitif lojik kullanılır: lojik 1'i temsil eden gerilim, lojik 0'ı temsil eden gerilimden büyüktür. Diyotlu VE/VEYA devreleri, anahtar olarak iki kutuplu transistör, DTL ve TTL kapıları, MOS ve CMOS yapıları ele alınır.

Diyotun ileri yönde yaklaşık 0,7 V gerilimle iletime geçtiği model kullanılır. Transistör için aktif bölgede IC=βIB bağıntısı yazılır; doyuma gelindiğinde kollektör akımını dış devre sınırlar. 5 V beslemeli örnekte IC=(5−VCEsat)/RC, VCEsat yaklaşık 0,2 V kabul edilir. Eviricide giriş düşükken çıkış yüksek, giriş transistörü doyuma sürecek kadar yüksekken çıkış düşük olur.

## 1. TTL ve CMOS kapı karakteristikleri

Kapıların statik ve dinamik davranışı incelenir. Giriş/çıkış gerilimleri, akım değerleri ve yayılma gecikmeleri üzerinde çalışılır. Tek sayıda NOR kapısıyla kurulan halka düzeni gecikme ölçümü için kullanılır. Deney öncesinde devrelerin CAD ortamında benzetimi ve kullanılacak tümdevrelerin karakteristiklerinin incelenmesi istenir.

## 2. Kombinezonsal devre analizi

Verilen kapı devresinin Boolean fonksiyonu ve doğruluk tablosu çıkarılır. Giriş birleşimleri deney setinde uygulanarak ölçülen çıkışlar beklenen sonuçlarla karşılaştırılır. Böylece şema, cebirsel ifade ve tablo arasındaki ilişki sınanır.

## 3. Kombinezonsal devre sentezi

İstenen giriş/çıkış davranışından mantık fonksiyonu kurulur, sadeleştirilir ve kapılarla gerçekleştirilir. Hazırlıkta MORP ve Espresso gibi araçlarla fonksiyonların incelenmesi ve CAD benzetimi istenir. Sadeleştirme sonucunun doğruluk tablosunu değiştirmemesi esastır.

## 4. MSI kod çözücüler, çoğullayıcılar ve kodlayıcılar

Kod çözücü, çoğullayıcı ve kodlayıcı tümdevreleri blok olarak kullanılır. Seçme ve etkinleştirme girişlerinin çıkış üzerindeki etkisi araştırılır. Mantık fonksiyonlarını yalnız temel kapılarla değil, hazır MSI işlev bloklarıyla gerçekleştirme yaklaşımı öne çıkar.

## 5. Toplama, çıkarma ve karşılaştırma

Yarım ve tam toplayıcı, paralel toplama, çıkarma ve büyüklük karşılaştırması ele alınır. Deney öncesinde hazırlanan iki bitlik paralel toplayıcı deney setinde kurulur. Toplam ve elde çıkışları değişik giriş birleşimleriyle doğrulanır; daha geniş aritmetik yapıların blok bağlantıları incelenir.

## 6. Bellek elemanlarının gerçeklenmesi ve analizi

Geri beslemeli kapı devreleriyle bilgi saklama fikri tanıtılır. Mandal ve flip-flopların girişleri, çıkışları, durum koruma ve durum değiştirme davranışları incelenir. Kombinezonsal devrelerden farklı olarak önceki durumun sonraki çıkış üzerindeki etkisi izlenir.

## 7. Senkron ardışıl devre analizi

Verilmiş bir ardışıl devrede flip-flop giriş fonksiyonları, sonraki durumlar ve çıkışlar belirlenir. Saat darbeleriyle durumların değişimi izlenerek durum tablosu ve deneysel sonuçlar karşılaştırılır.

## 8. Senkron ardışıl devre sentezi

Tanımlanan davranışa uygun durumlar ve geçişler seçilir. Bellek elemanlarının uyarma fonksiyonları elde edilip sadeleştirilir. Tasarım benzetimde ve deney setinde kontrol edilir. Hazırlık, gerçekleştirme ve ölçüm adımları föyde ayrı verilmiştir.

## 9. Asenkron ve senkron sayıcılar

Sayıcı devrelerinde durum sırası ve saat bağlantılarının etkisi karşılaştırılır. Asenkron yapıda kademeler birbirini tetiklerken senkron yapıda ortak saat kullanılır. Deneyler sayma dizisini ve çıkışların zaman içindeki değişimini gözlemlemeye yöneliktir.

## 10. Yazıcılar

Son deneyde bilgi saklama ve kaydırma işlemleri ele alınır. Föyün kullandığı “yazıcı” sözcüğü bu bağlamda register/yazmaç anlamındadır. Deney öncesi devre benzetimi, tümdevre incelemesi ve kurulan devrenin çalışma durumlarının denenmesi istenir.

## Kaynakça

Föyün sonunda Ahmet Dervişoğlu, Friedman–Menon, Barry Wilkinson, Kuntman–Toker–Özcan, Ercegovac–Lang, M. Morris Mano ve Richard Tinder'ın kitapları kaynak olarak listelenir. Bunlar föyün kaynakçasıdır; föyü hazırlayan kişi ya da kurum bilgisi yerine kullanılmadı.
