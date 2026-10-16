---
baslik: EEM214 Elektronik I: Final Çalışma Notları (2014) – Diyot Modelleri, Doğrultucu, Kırpıcı, BJT/FET Analizi, Direnç ve Kondansatör Çeşitleri
ozet: EEM214 Elektronik I finaline hazırlık için tutulmuş el yazısı özet notlar: diyot modelleri ve DC/AC analiz adımları, yarım ve tam dalga doğrultucu, seri ve paralel kırpıcı, kenetleyici devreler, transistör sınıflandırması, BJT ve FET'lerde DC ve AC analiz; ödev için diyot, direnç ve kondansatör çeşitleri ile direnç renk kodu tablosu.
---

Bu yazı, EEM214 Elektronik I dersinin **2014 bahar** dönemi final sınavına (29 Mayıs 2014) hazırlanırken tutulmuş el yazısı özet notları ve aynı dönemin finalde sorulacağı belirtilen ödevi (diyot, direnç ve kondansatör çeşitleri) için hazırlanmış notları aktarıyor. Metin, kâğıtların telefonla çekilmiş fotoğraflarından metne aktarıldı; fotoğraflar yayınlanmadı. Şekiller sözle tarif edildi. Ödevin bilgisayarda hazırlanmış cevapları için [Ödev Cevapları (2012–2014)](/arsiv/eem214-odev-cevaplari-2012-2014/), final sınavının cevap anahtarı için [2014 Quiz 2 ve final](/arsiv/eem214-quiz-2-final-2014/) yazısına bakılabilir.

## Final notları

### Yarıiletken ve diyot

- **n türü madde:** boşta fazla elektron.
- **p türü madde:** boşta fazla bağ.
- **Diyotlar:** doğru polarma altında kendi yönünde akımı ileten elemanlardır.

*Not: p türü maddede fazlalık "bağ" değil, eksik elektron yani **delik**tir.*

### Diyot modelleri

- **1) İdeal diyot:** iletimde kısa devre gibi davranır. Ters yönde akım iletmez; çalışması için V_i > 0 olması yeterli.
- **2) Sabit gerilim düşümü modeli (Constant Voltage Drop, CVD):** iletimde V_B'lik bir gerilim kaynağı. Ters yönde akım iletmez; çalışması için V_i > V_B olmalı.
- **3) Parçalı doğrusal model (Piece-Wise Linear, PWL):** iletimde V_B gerilim kaynağı ile seri r_d direnci. Ters yönde akım iletmez; çalışması için V_i > V_B olmalı.

### Diyotlarda DC ve AC analiz

**DC analiz:**

1. Akım yönü ile diyot aynı yönde mi?
2. V_giriş > V_bariyer ise
3. modeli istenene göre çiz,
4. devre analizini yap.

**AC analiz:** Girişe hem AC hem DC verilir. Ayrı ayrı AC ve DC model çizilip istenen bulunur, iki değer toplanarak sonuç bulunur. AC modelde diyot r_ac direnciyle gösterilir.

### Doğrultucu diyot devreleri

- **Yarım dalga doğrultucu:** kaynak, seri diyot ve R yükü. Giriş sinüsünün yalnız pozitif alternansları çıkışa geçer; negatif alternanslarda çıkış sıfırdır.
- **Tam dalga doğrultucu (köprü):** transformatör sekonderine bağlı dört diyotlu köprü ve R yükü. Çıkışta her iki alternans da pozitif yönde görülür.
- **Tam dalga doğrultucu (orta uçlu):** orta uçlu transformatör ve iki diyot, R yükü; çıkış köprülü doğrultucununkiyle aynı biçimde.

### Kırpıcı diyot devreleri

**a) Seri kırpıcı:** diyot ve 3 V'luk pil kaynakla seri, çıkış R üzerinden alınıyor. Pil diyota ters yönde bağlıyken giriş 3 V'u aşmadıkça diyot iletmez; çıkışta yalnız girişin 3 V'un üstündeki kısmı görülür.

*Not (defterdeki):* 3 V ile V_g = 3 V olana kadar 3 V daha güçlü olduğu için 3 V'a kadar kırpar. Diyot yönü pozitif yönde mi, negatif yönde mi, onu ayarlar.

İkinci seri kırpıcıda pil diyotla aynı yönde bağlı; çıkış dalga biçimi girişe göre yukarı kaymış olarak çizilmiş.

*Not (defterdeki):* Diyotla batarya aynı yönde olduğu için 3 V → +3 V gider.

**b) Paralel kırpıcı:** kaynak seri R üzerinden, çıkışa paralel diyot + 3 V'luk pil. Çıkış, girişin 3 V'un üstüne çıkan kısmı kesilmiş biçimde 3 V'ta sınırlanıyor; negatif alternans aynen geçiyor.

### Kenetleyici devreler

1. Analize diyodun çalıştığı alternansla başlanır.
2. Devre çalışırken kondansatör ilk gördüğü gerilimle şarj olur.
3. Karşı alternansta kondansatörün boşalmadığı kabul edilir.
4. Tekrar çalıştığında kondansatör, gerilim kaynağına destek olur.

Örnek: seri kondansatör, çıkışa paralel diyot ve R. Giriş +10 V / −10 V kare dalga iken çıkış 0 ile −20 V arasında değişen kare dalga olur.

### Transistörlerin sınıflandırılması

- **BJT'ler:** NPN (düz), PNP (ters).
- **FET'ler → JFET'ler:** n kanal, p kanal.
- **FET'ler → MOSFET'ler → Depletion (azaltan tip) MOS:** n kanal, p kanal.
- **FET'ler → MOSFET'ler → Enhancement (çoğaltan tip) MOS:** n kanal, p kanal.
- **MESFET** de MOSFET'lerin yanında anılmış.

### BJT'ler

npn ve pnp sembolleri (B, C, E uçları) çizilmiş. Eğer bazdan akım girerse C'den E'ye akım geçer; giren akım (baz) ile C–E akımı doğru orantılı olarak değişir.

- I_E = I_B + I_C
- I_C = β·I_B
- I_E = (β + 1)·I_B
- β ≫ 1 ise I_C ≅ I_E alınabilir.

**BJT'lerde DC analiz:** devreyi çizerken kondansatörler açık devre yapılır.

**BJT'lerde AC analiz:** kondansatörler kısa devre, (DC) kaynaklar öldürülür.

- **r_e modeli:** B–E arasında β·r_e direnci, C–E arasında I_b·β bağımlı akım kaynağı.
- **r_π modeli:** B–E arasında r_π direnci, C–E arasında g_m·V_BE (ya da I_b·β) bağımlı akım kaynağı.

### FET'lerde DC analiz

- V_T > V_GS ise kesim (cutoff).
- V_G > V_T ise aktif:
- a) Triyot (doğrusal) bölge, V_DS < V_GS − V_T ise: I_D = k_n′(W/L)·[(V_GS − V_T)·V_DS − ½·V_DS²]
- b) Doyum (saturation), V_DS > V_GS − V_T ise: I_D = ½·k_n′(W/L)·(V_GS − V_T)²

*Not: Aktif olma koşulu defterde "V_G > V_T" yazılmış; doğrusu V_GS > V_T.*

### FET'lerde AC analiz

G–S arası açık devre (giriş gerilimi v_gs), D–S arasında g_m·v_gs bağımlı akım kaynağı.

**AC analiz yaparken:**

1. Kondansatörler kısa devre,
2. DC kaynaklar ölür,
3. modeli çiz,
4. A_v, A_i bul.

## Ödev notları: Diyot, direnç ve kondansatör çeşitleri

### Diyot seçenekleri

- **a) Tünel diyot:** Saf silisyum, germanyuma fazla katkı maddesi katılarak imal edilir. Belli bir gerilim değerine kadar akım seviyesi artar, belli gerilimden sonra akım azalır; düşüş olduğu bölgede çalışır. Yüksek frekanslı devrelerde, osilatörlerde kullanılır.
- **b) Varikap diyot:** Uçlarına verilen gerilim ile ayarlanabilir kondansatör gibi çalışan diyottur; ters polarma altında çalışır. Voltaj artarsa yalıtkan bölge artar (ya da tam tersi).
- **c) Schottky diyot:** Normal diyotlar yüksek frekans altında uygulanan gerilimin yön değiştirmesine hızlı cevap veremezler; hızlı cevap vermek için platinle kaplanmıştır.
- **d) Foto diyot:** Ters polarma altında ışık sensörü gibi, ışığın yoğunluğuna göre; normal polarmada düz diyot.
- **e) LED diyot:** Doğru polarmada ışık yayan diyottur; galyum arsenit; RGBY.

*Not: Schottky diyot "platinle kaplanmış" bir P-N diyot değil, metal–yarıiletken eklemli bir diyottur; hızını azınlık taşıyıcı depolanmamasına borçludur.*

### Direnç çeşitleri

- **a) Karbon direnç:** Renk kodlarıyla kodlanır. ¼, ½, 1, 2, 3 W değerlerle imal edilir; 1 Ω'dan 22 MΩ'a. Eskidikçe direnç değerleri değişir.
- **b) Telli direnç (taş direnç):** 10 Ω ile 100 kΩ arasında, 30 W'a kadar. Büyükleri, büyük güç harcayanları ısınır.
- **Entegre direnç:** birden çok direncin tek paket olarak kullanılması.
- **SMD direnç:** PCB devre kartında kolay kullanım.

**Ayarlı dirençler:**

- **1) Trimpot:** Güçleri küçük, elektronik devrelerde kullanılır. Tornavida ile ayarlanır; direnci ayarlandıktan sonra sabit bırakılan dirençlerdir.
- **2) Potansiyometre:** Genellikle gerilim bölme, çıkış gerilimini ayarlamada kullanılır; devre içinde sık sık değiştirilir; genellikle ses ayarlamada kullanılır. Çeşitleri: lineer, logaritmik ve çok turlu potansiyometre.
- **3) Reosta:** Yüksek gerilimde kullanışlı, yüksek akım geçer; elle kontrol edilir.

**Değişken dirençler:**

- **Termistör (NTC–PTC):** Isı değeri ile direnç değeri değişen dirençtir.
- **Varistör:** Uçlarına uygulanan gerilime göre ters orantılı olarak direnç değeri değişir. Genellikle frekans kaymasını engellemek için ya da fazla gerilimden korunmak adına gerilim sabitlemesi yapan devrelerde kullanılır.
- **Foto direnç (LDR):** Üzerine düşen ışığa göre az ya da çok direnç gösteren dirençlerdir: karanlıkta yüksek, ışıkta az direnç gösterir.

**Direnç okuma:** İlk iki renk direnç değerini, üçüncüsü kaç sıfır olduğunu, dördüncüsü toleransı verir. Siyah 0, kahverengi 1, kırmızı 2 … mor 7, gri 8, beyaz 9.

### Direnç renk kodu tablosu

Notlarla birlikte bir web sayfasından alınmış (kaynağı belirtilmemiş, büyük olasılıkla Türkçe Vikipedi) ekran görüntüsündeki tablo:

| Renk | 1. bant | 2. bant | 3. bant (çarpan) | 4. bant (tolerans) | Sıcaklık katsayısı |
|---|---|---|---|---|---|
| Siyah | 0 | 0 | ×10⁰ | | |
| Kahverengi | 1 | 1 | ×10¹ | ±%1 (F) | 100 ppm |
| Kırmızı | 2 | 2 | ×10² | ±%2 (G) | 50 ppm |
| Turuncu | 3 | 3 | ×10³ | | 15 ppm |
| Sarı | 4 | 4 | ×10⁴ | | 25 ppm |
| Yeşil | 5 | 5 | ×10⁵ | ±%0.5 (D) | |
| Mavi | 6 | 6 | ×10⁶ | ±%0.25 (C) | |
| Mor | 7 | 7 | ×10⁷ | ±%0.1 (B) | |
| Gri | 8 | 8 | ×10⁸ | ±%0.05 (A) | |
| Beyaz | 9 | 9 | ×10⁹ | | |
| Altın | | | ×10⁻¹ | ±%5 (J) | |
| Gümüş | | | ×10⁻² | ±%10 (K) | |
| Yok | | | | ±%20 (M) | |

*Not: Ekran görüntüsündeki tabloda son sütunun başlığı "Geçici Katsayı" yazıyor; içerik direncin sıcaklık katsayısıdır.*

### Kondansatör çeşitleri

Sınıflandırma: yalıtkan cinsine göre; kapasite değerine göre (sabit ve ayarlanabilir kondansatörler); kutup durumuna göre (kutuplu ve kutupsuz).

- **Yalıtkan cinsine göre:** vakumlu, havalı, plastik film, mikalı, kâğıtlı, camlı, seramik, alüminyum elektrolitik, tantalum, OS-CON, süper ve "gimmick" kondansatör.
- **Kapasite değerine göre:** sabit kondansatör ve ayarlanabilir kondansatör (varyabl, trimer, varaktör).
- **Varyabl:** yüksek gerilim, yüksek frekans.
- **Trimer:** küçük güç; telekomünikasyonda kullanılır.
- **Varaktör:** yüksek frekans; telekomünikasyon, frekans kontrolünde de kullanılır.
