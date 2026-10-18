---
baslik: EEM474 Güç Elektroniği: DC motorlar, moment–hız ilişkisi ve sürme
ozet: Sabit mıknatıslı, şönt, seri ve bileşik DC makineler; elektromekanik dönüşüm, kayıplar ve hız denetimi.
---

EEM474 ders klasöründeki İngilizce sunumların anlatımı ve formülleri metne aktarıldı. Hazırlayanın adı belgelerde açıkça belirtilmiyor. Fotoğraflar ve kitaplardan alınmış görseller aktarılmadığından bu yazıda indirme dosyası bulunmuyor.

## Enerji dönüşümü

Motor elektrik enerjisini mekanik enerjiye, jeneratör mekanik enerjiyi elektrik enerjisine dönüştürür. Temel ilişkiler E = KΦω, T = KΦI ve Pdönüşüm = EI = Tω biçimindedir. Alan içindeki iletken için kuvvet F = BℓI sinα; hareketle endüklenen gerilim uygun diklik koşulunda e = Bℓv olarak verilir.

Sunum motor seçimini maliyet, ısıl kapasite, verim, moment–hız eğrisi, ivmelenme, güç yoğunluğu ve tepe momenti üzerinden ele alır. Otomotiv, ev aletleri, sanayi, yazıcılar ve disk sürücüleri uygulama örnekleridir.

## Sabit mıknatıslı DC motor

Stator sabit manyetik alanı, rotor akım taşıyan endüvi sargılarını sağlar. Fırça ve komütatör, dönme sırasında sargı akımının bağlantısını değiştirir. Kararlı durumda Vs = Eg + RaIa; Eg = Keω; T = KtIa'dır. Dolayısıyla:

ω = Vs/Ke − RaT/(KeKt)

Kalkışta ω = 0 olduğundan zıt EMK yoktur; akım endüvi direnci ve sürücüyle sınırlanır. İdeal boşta hız Vs/Ke, kilitli rotor momenti KtVs/Ra'dır. Gerilim değiştirilince moment–hız doğrusunun konumu değişir.

*Not: Kaynaktaki hız denkleminin bir satırında Ke ve Kt etiketleri karışmaktadır. Yukarıdaki bağıntı, aynı sayfada verilen Vs = Keω + RaIa ve T = KtIa eşitliklerinden yazılmıştır. SI birimleriyle bazı modellemelerde bu iki sabitin sayısal değeri aynı olabilir.*

## Sargılı makineler

Ayrı uyartımlı makinede alan sargısı ayrı kaynaktan beslenir. Şönt bağlantıda alan sargısı endüviye paraleldir; alan akımı yaklaşık sabit tutulduğunda hız yükle az değişir. Seri motorda alan akımı endüvi akımına eşittir; yüksek kalkış momenti sağlanır, ancak yük azalınca hız büyük ölçüde artabilir. Bileşik makinede seri ve şönt alanlar birlikte bulunur.

Jeneratör için uç gerilimi U = Ea − RaIa; motor için Ea = U − RaIa yazılır. Motor ve yükün moment–hız eğrilerinin kesişimi çalışma noktasıdır.

## Kayıplar ve verim

Endüvi bakır kaybı Ia²Ra, alan bakır kaybı If²Rf'dir. Sürtünme, havalandırma, histerezis ve fuko akımı kayıpları da hesaba katılır. Verim, yararlı çıkış gücünün giriş gücüne oranıdır. Elektromekanik dönüşüm gücü ile mildeki yararlı güç, kayıplar nedeniyle aynı değildir.

*Not: Kaynak, boşta momenti ve çıkış gücünü sıfır alan ideal açıklama kullanır. Gerçek motorda sürtünme ve diğer kayıpları karşılayan boşta akımı bulunur. Sabit mıknatıslı motorun yön değiştirmesine ilişkin “alan polaritesini değiştir” ifadesi de bu motor için endüvi besleme polaritesinin terslenmesi olarak okunmalıdır.*

## Hız ve yön kontrolü

Endüvi gerilimi, alan akısı ve devre direnci hız üzerinde etkilidir. Kıyıcıyla ortalama endüvi gerilimi ayarlanır. H-köprüsü polariteyi değiştirerek iki yönde hareket sağlar; serbest dolaşım yolları endüktif akımın sürekliliğini korur. Rejeneratif çalışmada mekanik taraftan gelen enerji elektrik kaynağına geri aktarılır.
