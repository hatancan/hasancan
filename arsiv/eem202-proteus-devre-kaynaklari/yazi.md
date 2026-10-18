---
baslik: EEM202 Devre Teorisi II: Deney, Üç Faz, Transformatör ve Soğutucu Devre Kaynakları
ozet: EEM202 deneyleri, HW3–HW4 ve dizüstü bilgisayar soğutucu projesinin Proteus kaynak dosyaları.
---

EEM202 klasöründeki deney, ödev ve proje çalışmalarının Proteus kaynak dosyaları. Daha önce arşivlenen raporları tamamlayan sekiz devre dosyası burada birlikte sunuluyor. 2014 deney ve ödev dosyaları ile 2015 soğutucu projesi aynı pakette; son projenin iç kaydındaki 17 Nisan 2015 tarihi kullanıldı. ZIP yazının sonunda indirilebilir.

## Deney 1–3 kaynakları

`deney1.pdsprj`, `deney2.pdsprj` ve `deney3.pdsprj`, laboratuvar klasörlerinin düzenlenebilir devre kaynaklarıdır. Direnç, kapasitör, bobin, sinyal kaynağı ve ölçü aleti modelleri içerirler. İlgili ön çalışmalar ve kaydedilmiş ölçümler [laboratuvar çalışmaları yazısında](/arsiv/eem202-deney-calismalari/) bulunuyor.

*Not: Kaynak projeler birden fazla çalışma sürümünü temsil edebilir. Dosya içindeki başlangıç değerleriyle rapor ekranlarının aynı koşulu temsil ettiği varsayılmadı; projeler burada çalıştırılmadı.*

## HW3: üç fazlı ve tek fazlı devreler

`HW3.pdsprj` ile `TEK FAZLI DEVRE.pdsprj` aynı ödev klasöründen gelir. Dosyalarda sinüzoidal kaynaklar, direnç/bobin yükleri ve AC ölçü aletleri bulunur. HW3 kaydı ayrıca transformatör modeli başvuruları içerir. Ödevin soruları ve sonuçları [PSpice ödevleri](/arsiv/eem202-pspice-odevleri/) ve [HW3–HW4 raporları](/arsiv/eem202-pspice-odev-3-4-raporlari/) ile birlikte okunabilir.

Üç fazlı çalışmada faz gerilimleri arasındaki ilişki, hat/faz büyüklükleri ve yük bağlantısı belirleyicidir. Tek fazlı dosya karşılaştırma çalışması için ayrı saklanmıştır; dosya adı ve kaynak klasörü bu ayrımı gösterir.

## HW4: transformatör çalışması

`HW4.DSN` ve `HW4.pdsprj` aynı çalışma için iki kaynak biçimidir. İkisinde de sinüzoidal kaynak, transformatör ve AC ölçü aletleriyle ilgili model kayıtları bulunur. DSN şematik dosyası ile PDS proje kapsayıcısı ayrı tutuldu; dosya türü farklı olduğu için biri diğerinin gereksiz kopyası sayılmadı.

## Dizüstü bilgisayar soğutucu projesi

`devre2proje.pdsprj`, [soğutucu proje raporunun](/arsiv/eem202-proje-dizustu-bilgisayar-sogutucu/) devre kaynağıdır. İç model başvurularında NTC, op-amp, doğrultucu köprü, 7812 regülatör, transformatör, ayarlı direnç ve DC fan bulunur. Projenin sıcaklık algılama, karşılaştırma ve fan sürme bölümleri bu elemanlarla ilişkilidir.

## Dosya biçimi

PDS proje dosyalarının içinde PROJECT.XML, şematik/veri kayıtları ve yardımcı proje bileşenleri bulunur. Yalnız kaynak projeler eklendi; yedekler ve geçici çalışma dosyaları alınmadı. Proje XML'indeki müşteri kimliği alanı sıfırlandı. İndirme eski Proteus sürümlerine ait modeller gerektirebilir; herhangi bir benzetim sonucu bu turda üretilmedi.
