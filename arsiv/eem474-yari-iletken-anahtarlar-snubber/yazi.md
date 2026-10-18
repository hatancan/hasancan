---
baslik: EEM474 Güç Elektroniği: Güç yarı iletkenleri ve snubber devreleri
ozet: Diyot, tristör, BJT, MOSFET ve IGBT anahtarlarının çalışma ilkeleri ile anahtarlama kayıpları ve koruma devreleri.
---

EEM474 ders klasöründeki İngilizce sunumların anlatımı ve formülleri metne aktarıldı. Hazırlayanın adı belgelerde açıkça belirtilmiyor. Fotoğraflar ve kitaplardan alınmış görseller aktarılmadığından bu yazıda indirme dosyası bulunmuyor.

## Güç anahtarlarının karşılaştırılması

Diyot, uçlarındaki gerilim ve devre akımına bağlı olarak iletime girer; bağımsız bir kontrol ucu yoktur. Tristörün kapı darbesi ile iletime geçirilmesi mümkündür, ancak normal SCR kapıdan kesime götürülmez. Ana akımın tutma akımının altına düşmesi gerekir. GTO, kapı üzerinden kesime geçirilebilen tristör türü olarak ele alınır.

BJT akımla, MOSFET ve IGBT ise kapı gerilimiyle sürülen elemanlar olarak karşılaştırılır. MOSFET'in yalıtılmış kapısı statik durumda küçük giriş akımı gerektirir; anahtarlama sırasında kapı kapasiteleri şarj ve deşarj edilir. IGBT, yalıtılmış kapı sürmesini bipolar iletim özellikleriyle birleştirir.

## Tristörün çalışma bölgeleri

İleri bloklama, ileri iletim ve ters bloklama bölgeleri ayrılır. İletime geçtikten sonra kapı işareti kaldırılabilir. Kilitlenme akımı ile tutma akımı aynı kavram değildir: ilkinde tetikleme sonrasındaki kalıcı iletim, ikincisinde sürmekte olan iletimin devamı söz konusudur. AC devrelerde doğal akım sıfırı komütasyona yardımcı olur; DC devrelerde ek komütasyon düzeni gerekebilir.

## İletim ve anahtarlama kayıpları

İletim kaybı anahtar üzerindeki gerilim ile akımın çarpımından hesaplanır. Direnç modeli uygun bir MOSFET için Piletim ≈ Irms² RDS(on) kullanılır. Anahtarlama sırasında gerilim ile akım aynı anda sıfırdan farklı olduğundan geçiş enerjisi oluşur:

Egeçiş = ∫ v(t)i(t) dt

Panahtarlama = fs (Eaçılma + Ekapanma)

Sunumlarda açılma ve kapanma dalga biçimleri, gecikme, yükselme, düşme ve depolama süreleri üzerinden incelenir. Diyotun ters toparlanması da diğer anahtarın akım ve kayıplarını etkiler.

## Anahtar seçimi

Bloklama gerilimi, ortalama/etkin/tepe akım, çalışma frekansı, iletim kaybı, anahtarlama süresi, güvenli çalışma alanı ve soğutma birlikte değerlendirilir. Tek başına nominal akım değeri yeterli değildir. Kapı veya baz sürücüsü anahtarın gerektirdiği gerilim, akım ve izolasyon koşullarını sağlamalıdır.

## Snubber ve endüktif yük

Endüktör akımı aniden değişemediği için anahtarın açılması aşırı gerilim oluşturabilir. Serbest dolaşım diyodu akıma alternatif yol sağlar. RC ve RCD snubber düzenleri gerilimin yükselme hızını sınırlamak veya parazitik endüktans enerjisini karşılamak amacıyla gösterilir. Endüktif seri eleman di/dt değişimini sınırlayabilir.

Kondansatör için i = C dv/dt, endüktör için v = L di/dt bağıntıları koruma elemanlarının etkisini açıklar. Snubber enerjisi dirençte harcanıyorsa bu da toplam kayba eklenir. Anahtarlama yörüngesinin güvenli çalışma alanı içinde tutulması, yalnız tepe gerilimi sınırlandırmaktan daha geniş bir tasarım konusudur.
