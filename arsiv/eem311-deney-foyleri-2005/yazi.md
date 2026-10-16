---
baslik: EEM311 Elektronik II: 2005 Laboratuvar Föyleri ve 2010 Sürümüyle Farkları
ozet: EEM311 Elektronik II laboratuvarının 2005 güz dönemi deney föyleri ile 2010 sürümü arasındaki farklar: düzeltilen formül ve değer hataları (VT, CE, ID formülü), değişen giriş genlikleri, ölçüm direnci, eklenen notlar ve yeniden düzenlenen deney adımları.
---

Bu yazı, Başkent Üniversitesi Elektrik-Elektronik Mühendisliği **EEM311 Elektronik II** laboratuvarının **2005 güz dönemi** deney föylerini ele alıyor. Föyler sonraki yıllarda küçük düzeltmelerle kullanılmaya devam etmiş; arşivdeki ayrıntılı yazılar (Deney 1–2, 3–4, 5–6, 7–8 ve laboratuvar bilgilendirme kitapçığı) **2010** sürümüne dayanıyor. Bu yüzden 2005 föyleri burada baştan aktarılmadı; yalnızca iki sürüm arasındaki farklar toplandı. 2005 föyleri Ekim–Aralık 2005 arasında hazırlanmış; dosyalar parola korumalıydı, parolası kaldırılmış kopyaları yazının sonunda ZIP olarak indirilebilir.

## Genel farklar

- 2005 föylerinin sayfa altında dersin web adresi *www.baskent.edu.tr/~kocaturk*, 2010 föylerinde *www.baskent.edu.tr/~ozparlak* yazıyor.
- Deney konuları, devre değerleri ve sonuç formları iki sürümde büyük ölçüde aynı. 2010 sürümünde metin biraz daha düzenli (alt maddeler a/b/c olarak ayrılmış, sonuç formlarına çizgiler eklenmiş), µ işaretleri düzeltilmiş.
- Deney 2'nin (tek katlı BJT yükselteç tasarımı) iki sürümü, adres dışında birebir aynı.
- 2008'de kullanılan laboratuvar kuralları kitapçığı (*EEM311_LabKurallari.pdf*) arşivde zaten *Laboratuvar Bilgilendirme Kitapçığı* yazısında yer alıyor; Dropbox'taki kopyası onunla aynı dosya.

## Deney 1: Single Stage BJT Amplifier

- 2005 föyünde oda sıcaklığındaki ısıl gerilim yanlışlıkla **V_T ≈ 0.0025 mV** yazılmış; 2010 föyünde **25 mV** olarak düzeltilmiş.
- 2010 sürümünde "undistorted" ve "unclipped" sözcükleri tırnak içine alınmış; teori ve adımlar aynı.

## Deney 3: Single Stage MOSFET Amplifier

- Giriş ve çıkış empedansı ölçümünde (Şekil 6 ve 7) 2005 föyünde seri ölçüm direnci **R_x = 1 kΩ** sabit direnç; 2010 föyünde **50 kΩ'luk potansiyometre**. Malzeme listesine de 2010'da 50 kΩ pot ve 10 µF kapasitör eklenmiş.
- 2010 föyüne iki not eklenmiş: transistör bacaklarını bağlayan kabloların olabildiğince kısa tutulması; DC kaynağın AC sinyalden önce açılıp sonra kapatılması.
- Sinyal üreteci ayarı 2005'te "yaklaşık 50 mV", 2010'da "50 mVp-p" diye yazılmış; ölçüm adımlarında kaynak gerilimi *v_x* olarak adlandırılmış.
- Deneysel çalışmanın 2. adımı 2010'da a/b/c alt maddelerine bölünmüş, 3. adıma "Şekil 1'deki yükselteci yeniden kurun" cümlesi eklenmiş (C_S'nin söküldüğü adımdan sonra devreyi eski hâline getirmek için).

## Deney 4: Two Stage Amplifier Circuit

- 2005 föyünde 3. adım ikiye ayrılıyordu: a) bozulmasız en büyük tepeden tepeye çıkış; b) sinyal üretecini **üçgen dalgaya** alıp kırpılmanın (clipping) başladığı en büyük çıkış salınımını ölçmek. 2010 föyünde b şıkkı çıkarılmış, yalnızca bozulmanın başladığı salınım ölçülüyor. Sonuç formundaki "v_out,undistorted(unclipped) max" satırı da kaldırılmış.

## Deney 5: MOSFET Current Mirror

- 2005 föyünde I_D1 ve I_D2 ifadelerinde **½ katsayısı eksik**: I_D = µ_n·C_ox·(W/L)·(V_GS − V_t)²·(1 + λV_DS). 2010 föyünde doğru biçimi I_D = ½·µ_n·C_ox·(W/L)·(V_GS − V_t)²·(1 + λV_DS) olarak düzeltilmiş.
- Sonuç formunda 2005'te R_O için ayrı bir "Part 2/Part 3" düzeni varken 2010'da R_O satırı M1 sütununa taşınmış; "lab" sözcüğü "experiment" olmuş.

## Deney 6: CMOS Common-Source Amplifier with an Active Load

2005 föyünün PDF'i, klasördeki parolayla (diğer föylerin parolası) açılamadı; bu yüzden karşılaştırılamadı ve ZIP'e konmadı. Dosya boyutu 2010 föyüyle neredeyse aynı (167 109 ve 167 191 bayt), büyük olasılıkla içerik de aynı.

## Deney 7: BJT Differential Pair Amplifier

- Teori bölümünde DC analizde 2005 föyü "I_C1 = I_C2 = I_EE" diyor; 2010 föyünde doğrusu **I_C1 = I_C2 ≈ I_EE/2** olarak düzeltilmiş.
- Ortak mod giriş direnci ifadesi 2005'te yanlışlıkla **R_id** = v_icm/(2i_b) diye adlandırılmış; 2010'da **R_icm**.
- Ön çalışmadaki ortak mod simülasyonunda iki baza uygulanan sinüsün genliği 2005'te **2 V**, 2010'da **4 V**.
- Deneysel çalışmanın 5. adımında ortak mod girişi 2005'te **4.0 Vp-p**, 2010'da **8.0 Vp-p**.
- 3. adımda 2005 föyü 100 mVp-p girişin Şekil 7'deki gerilim bölücüyle elde edilmesini istiyor ve "v_in2'ye bağlayın, v_in1'i topraklayın" diyor. 2010 föyünde bölücü cümlesi çıkarılmış ve cümle "v_in2'ye bağlayın ve v_in2'yi topraklayın" diye hatalı kalmış (2010 yazısında bu not olarak düzeltildi); 2005 föyündeki ifade doğru olanı.
- Sonuç formunda Q_B ve Q2'ye ait bias satırları 2010'da tablonun sonuna taşınmış.

## Deney 8: Frequency Response of Common Emitter Amplifier

- Ön çalışma tablosunda emetör baypas kapasitörü 2005 föyünde **C_E = 10 µF** yazıyor; malzeme listesinde ise 100 µF var. 2010 föyünde tablo da **100 µF** olarak düzeltilmiş. (2008'deki bazı öğrenci çalışmalarında bu yüzden simülasyon C_E = 10 µF ile yapılmış.)
- r_x'in etkisinin ihmal edilebileceği koşul 2005'te "I_BQ ≫ ?" diye, 2010'da "**I_BQ ≪ ?**" diye soruluyor.
- 2005 föyünde kaynak *v_s* (R_s üzerinden), 2010 föyünde *v_in* olarak adlandırılmış; Şekil 2'de kaynak çizimi buna göre değişmiş, giriş/çıkış dalga şekilleri için iki osiloskop ızgarası eklenmiş.
- Frekans taraması listesine 2010'da **500 Hz, 1 kHz ve 10 kHz** eklenmiş; tablo başlığı "v_out (peak)" yerine "v_out" olmuş.
- 3. adım 2010'da a (kesim frekanslarını ölçmek) ve b (frekans cevabı eğrisi) olarak ikiye bölünmüş.
- 4. adım (C_E'nin sökülmesi) 2005'te tek paragraftı; 2010'da a) 1 kHz'de undistorted çıkış için giriş ayarlanıp orta bant kazancının ölçülmesi ve **PSpice sonucuyla karşılaştırılması**, b) f_H ve f_L'nin ölçülmesi, c) değişimlerin yorumlanması olarak üç alt adıma ayrılmış.

## Klasördeki diğer dosyalar

2005 föylerinin yanında dağıtılan PSpice kütüphane dosyaları (*jfet.lib*, *jfet.ind*, *cd4007.ind*), 2N4860 datasheet'i, standart direnç değerleri tablosu ve "how to add an include file" kılavuzu bu yazıya alınmadı.
