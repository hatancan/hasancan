---
baslik: EEM441 Haberleşme I: 2013 AM ve FM Deney Raporları
ozet: AM modülasyon indisi, 455 kHz ara frekans ve FM deney gözlemlerinin kişisel bilgilerden arındırılmış metni.
---

26 Aralık 2013 tarihli AM ve FM uygulama raporları ile aynı ölçümleri içeren kısa raporlar, kişisel bilgiler çıkarılarak metne aktarıldı. Deney fotoğrafları özel arşivde tutuldu; bu yazının indirme dosyası yoktur.

## Genlik modülasyonu

Raporda taşıyıcı Vc = Ec cos(ωc t), tek tonlu mesaj Vm = Em cos(ωm t) olarak tanımlanıyor. Tam AM işareti:

VAM = [Ec + Em cos(ωm t)] cos(ωc t) = Ec[1 + m cos(ωm t)] cos(ωc t), m = Em/Ec.

Açılımda taşıyıcı ile fc − fm ve fc + fm yan frekansları elde edilir. Her yan frekansın genliği mEc/2'dir. Mesaj bant genişliği B ise çift yan bant AM ve DSB-SC için 2B, SSB için B gerekir. SSB'de iki yan banttan biri seçilir. DSB-SC'de taşıyıcı bastırılır; mesajın işaret değiştirmesi modüleli dalgada 180° faz değişimine yol açar.

Zarftan ölçülen indis m = (A − B)/(A + B). Rapordaki A = 152 mV ve B = 57 mV için m = 95/209 ≈ 0,455; sonuç 0,45 olarak verilmiş. Taşıyıcı ve yan bant genlik oranının dB değeri 20 log₁₀(2/m) biçiminde yazılıyor; yaklaşık 6 dB, m ≈ 1'e karşılık geliyor.

## AM deneyindeki ölçümler

1. Ses osilatöründen seçilen ton AM DSB modülatörüne veriliyor; t.p.1 ve t.p.9 gözleniyor.
2. t.p.1 tetikleme kaynağı seçilerek t.p.3'te modüleli işaret inceleniyor. Balance düğmesiyle çıkışın değiştiği kaydediliyor.
3. Tonun genliği ve frekansı değiştirilerek zarfın ve dalga sıklığının değişimi gözleniyor.
4. Alıcının tuning dial ayarıyla gönderilen yayın bulunuyor. RF yükselteç çıkışında girişe göre faz farkı gözleniyor.
5. Yerel osilatör ve RF işaretini karıştıran kat inceleniyor. Yerel osilatör frekansı, alınan frekanstan 455 kHz büyük; fark bileşeni ara frekansı oluşturuyor.
6. IF katları, diyot algılayıcı ve ses yükselteci çıkışları sırayla gözleniyor. Son bölümlerde fotoğraflar dışında ayrı bir sayısal ölçüm tablosu bulunmuyor.

Rapordaki alıcı örneğinde 455 ± 6 kHz geçiş bandı, yani 449–461 kHz aralığı veriliyor. 300 Hz–3 kHz ses için SSB bant genişliği 2,7 kHz olarak yazılmış.

*Not: Rapordaki “SSB'de gücün üçte ikisi taşıyıcıdadır” ve “DSB-SC'de yan bantlar gücün üçte ikisini taşır” ifadeleri taşıyıcısı bastırılmış işaretler için doğru değildir. Üçte iki/üçte bir paylaşımı, yüzde yüz modülasyonlu tek tonlu tam AM örneğine aittir. “Alıcıdan gönderip vericiden almak” ifadesinde alıcı ve verici yer değiştirmiştir. Karıştırıcı için yazılan toplam/fark frekansı anlatımı, iki frekansın sayısal çarpımı olarak okunmamalıdır.*

## FM ve PM'nin temel bağıntıları

FM raporu, taşıyıcının fazını θ(t), anlık açısal frekansını dθ/dt olarak tanımlıyor. Tek tonlu FM için:

VFM(t) = Ec cos[ωc t + β sin(ωm t)]

β = Δω/ωm = Δf/fm.

75 kHz sapma ve 300 Hz mesaj için β = 250; aynı sapmada 15 kHz mesaj için β = 5 bulunuyor. Küçük β için dar bant yaklaşımı, daha büyük indislerde Bessel fonksiyonlarıyla yan bant açılımı kullanılıyor. Carson yaklaşımı BT ≈ 2(Δf + fm) = 2(β + 1)fm olarak veriliyor.

Rapordaki β = 1 örneğinde J₀ ≈ 0,765; J₁ ≈ 0,440; J₂ ≈ 0,115. Taşıyıcı ve ilk iki yan bant çifti, toplam gücün yaklaşık %99,47'sini kapsar. Kaynakta güç sonucu yaklaşık 0,4997Ec² yazıyor.

*Not: Yazılı katsayılarla [0,765² + 2×0,440² + 2×0,115²]/2 = 0,4974375 elde edilir. Kaynağın 0,4997 sonucu bu yuvarlatılmış sayılarla uyuşmuyor. Raporda Carson bant genişliği bazı satırlarda β harfiyle yazılmış; bant genişliği ile boyutsuz modülasyon indisi farklı büyüklüklerdir. Sabit sapmada β, mesaj frekansıyla ters orantılıdır.*

## FM deney düzeni ve gözlemler

Ses osilatörü, reaktans/varaktör modülatörü, karıştırıcı-yükselteç, rezonans devresi, genlik sınırlayıcı ve alçak geçiren süzgeç inceleniyor. Düzenekte ses osilatörü için 16 Hz–20 kHz aralığı belirtilmiş.

1. Ses osilatörü modülatör girişine bağlanıyor; anahtar Reactance konumunda, taşıyıcı ayarı orta konumda tutuluyor.
2. Karıştırıcı-yükselteç çıkışında genlik 520 mV, frekans 93,98 Hz olarak kaydediliyor.
3. Ses genliği artırıldığında çıkıştaki dalga sıklığının değiştiği belirtiliyor.
4. Algılama deneyi için rezonans devresine 455 kHz sinüs uygulanıyor; ayrıca 475 kHz için ölçüm alınıyor.
5. Sonraki çıkışta sinüs, DC seviye ve küçük dalgalanma gözleniyor. t.p.73 çıkışının t.p.40 ile aynı olduğu yazılıyor.
6. Gürültü denemesinde sınırlayıcının genlikteki değişimleri bastırması tartışılıyor.

*Not: 520 mV ve 93,98 Hz rapordan aynen aktarılmıştır; ölçüm noktasının taşıyıcı, fark ya da ses çıkışı olduğu yeterince açıklanmıyor. Reaktans modülatörü yalnız “direncini değiştiren” devre, ayarsız rezonans devresi de yalnız güç yükselteci olarak tanımlanamaz. Kaynaktaki AM'nin anten gerektirmediği ve FM'nin her sinyal seviyesinde daha iyi olduğu iddiaları genel geçer değildir.*

## Ayrı laboratuvar fotoğrafları

Aynı klasördeki osiloskop fotoğraflarında tek kanallı sinüs, iki kanalın karşılaştırılması, modülasyon zarfı, düşük genlikli/gürültülü işaret ve düz çıkış izleri bulunuyor. ANACOM 1/1 verici ve ANACOM 1/2 alıcı kartları, taşıyıcı ayar düğmeleri ve deney bağlantıları görülüyor. Fotoğraflar bir ölçüm sıra numarasıyla eşleştirilmediği için ekranlardan yeni bir sonuç tablosu türetilmedi; raporda açıkça yazılı ölçümler yukarıda korundu.
