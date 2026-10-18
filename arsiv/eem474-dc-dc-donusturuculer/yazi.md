---
baslik: EEM474 Güç Elektroniği: Buck, boost, buck–boost ve PWM kontrolü
ozet: DC kıyıcıların çalışma bölgeleri, sürekli akımda dönüşüm oranları, dalgalanma ve gerilim/akım modu kontrolü.
---

EEM474 ders klasöründeki İngilizce sunumların anlatımı ve formülleri metne aktarıldı. Hazırlayanın adı belgelerde açıkça belirtilmiyor. Fotoğraflar ve kitaplardan alınmış görseller aktarılmadığından bu yazıda indirme dosyası bulunmuyor.

## Kıyıcı ve görev oranı

D = ton/T = ton fs, anahtarın bir periyotta iletimde kaldığı orandır. Direnç yüküne uygulanan 0–Vs darbelerinde Vort = DVs, Vrms = Vs√D olur. Sabit frekansta darbe genişliği değiştirilmesine PWM denir. Diğer yöntem, iletim veya kesim süresini sabit tutup frekansı değiştirmektir.

Sunumdaki 48 V, 24 Ω ve 250 Hz örneğinde T = 4 ms'dir. ton = 1 ms için D = 0,25, Iort = 0,5 A, Irms = 1 A ve P = 24 W bulunur. ton = 3 ms için D = 0,75, Iort = 1,5 A, Irms ≈ 1,732 A ve P = 72 W olur.

*Not: Kaynakta ikinci güç sonucu, etkin akımın 1,73 A'ya yuvarlanmasıyla yaklaşık 71,8 W gösterilir; yuvarlamadan hesaplandığında 72 W'dır.*

## Kararlı durum koşulları

Bir periyottaki endüktör akım değişimi sıfırdır. Ortalama endüktör gerilimi sıfır, ortalama kondansatör akımı sıfırdır. İdeal devrede giriş ve çıkış güçleri eşittir. Sürekli iletim, endüktör akımının periyot boyunca sıfırın üzerinde kaldığı çalışma biçimidir.

## Buck

Anahtar iletimdeyken vL = Vs − Vo; kesimdeyken serbest dolaşım diyodu üzerinden vL = −Vo olur. Volt-saniye dengesiyle Vo = DVs elde edilir. Akım eğimleri sırasıyla (Vs − Vo)/L ve −Vo/L'dir.

ΔiL = Vo(1 − D)/(Lfs)

ΔVo/Vo = (1 − D)/(8LCfs²)

Son bağıntı, ideal kondansatör ve küçük dalgalanma varsayımıyla verilen sonuçtur. Kondansatörün ESR etkisi bu basit ifadede yer almaz.

## Boost

Anahtar kapalıyken endüktör kaynak üzerinden enerji depolar; açıldığında kaynak ve endüktör yükü besler. Sürekli akım ve ideal elemanlar için Vo = Vs/(1 − D)'dir. Girişten büyük çıkış elde edilir. Anahtarın ve diyodun gerilim zorlanması çıkış gerilimiyle ilişkilidir.

## Tersleyen buck–boost ve Ćuk

Buck–boost'ta anahtar iletimdeyken enerji endüktörde birikir, kesimdeyken çıkışa aktarılır. Vo/Vs = −D/(1 − D) bağıntısındaki eksi işareti polarite değişimini gösterir. D < 0,5 için çıkış büyüklüğü girişten küçük; D > 0,5 için büyüktür. Sunumda Ćuk dönüştürücü de aynı ideal gerilim oranıyla gösterilir; enerji aktarımında kondansatör kullanır.

*Not: Kaynaktaki buck–boost karşılaştırmalarında Vo > Vs ve Vo < Vs yazılmıştır. Ters polariteli çıkış nedeniyle bu karşılaştırmalar gerilimlerin büyüklükleri için okunmalıdır. Aynı bölümde “output ... connected to load” ifadesi tutarsızdır; anlatılan, giriş ile çıkış arasında doğrudan enerji aktarım yolu bulunmamasıdır.*

## Çalışma bölgeleri ve tam köprü

Birinci bölge kıyıcı yükü besler. İkinci bölgede akım yönü tersine döner ve enerji kaynağa geri verilebilir. İki bölgeli düzenler gerilimin veya akımın bir yönde, diğerinin iki yönde olmasına izin verir. Dört bölgeli köprü iki işaretin de yönünü değiştirebilir. Bipolar sürmede ortalama sıfır çıkış D = 0,5'te oluşur.

## Kapalı çevrim

Gerilim modunda çıkıştan alınan örnek referansla karşılaştırılır; hata gerilimi testere dişi taşıyıcıyla karşılaştırılarak görev oranı üretilir. Akım modunda hata işareti anahtar akımının tepe sınırını belirler. Amaç giriş gerilimi ve yük akımı değiştiğinde çıkışı düzenlemektir.

Sunumdaki basitleştirilmiş PWM modeli: D = Vcontrol/Vst,m; Vcontrol = A(Vref − Vsam); Vsam = kDVs. Buradan D = Vref/(Vst,m/A + kVs) elde edilir. Bu statik ilişki, kapalı çevrimin kararlılık incelemesinin yerine geçmez.
