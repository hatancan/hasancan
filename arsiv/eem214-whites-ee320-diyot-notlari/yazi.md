---
baslik: EEM214 Elektronik I: Diyot Ders Notları – İdeal Diyottan Doğrultuculara ve Kenetleyicilere (Keith W. Whites, EE 320, 2009)
ozet: Keith W. Whites'ın EE 320 Electronics I dersinin diyot konusundaki sekiz ders notu: ideal diyot, pn ekleminin fiziksel çalışması, DC analiz ve CVD/PWL modelleri, küçük sinyal modeli r_d = nV_T/I_D, Zener diyotlar, doğrultucular, tepe doğrultucu ve dalgalılık, sınırlayıcı ve kenetleyici devreler, özel diyotlar.
---

Bu yazı, EEM214 Elektronik I dersinin klasöründe bulunan, **Keith W. Whites**'ın (South Dakota School of Mines and Technology) **EE 320 Electronics I** dersi için 2009 güz döneminde hazırladığı İngilizce ders notlarından diyotlarla ilgili sekiz tanesini (Lecture 1–4 ve 6–9) tanıtıyor. Notlar Sedra & Smith'in *Microelectronic Circuits* kitabını izliyor ve şekillerin bir kısmı bu kitaptan alınmış. Aşağıda her dersin ana fikirleri ve formülleri Türkçe özetlendi; PDF'ler yazının sonunda ZIP olarak indirilebilir. Aynı yazarın BJT ve MOSFET notları ayrı bir yazıda: [Whites EE 320 BJT ve MOSFET notları](/arsiv/eem214-whites-ee320-bjt-mosfet-notlari/).

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Lecture 1: Ideal Diode

Direnç, bobin ve kondansatör doğrusal elemanlardır: y = f(x) için m·y = f(m·x) sağlanır (v = Ri, i = C·dv/dt). Diyot ise iki farklı yarıiletkenin oluşturduğu bir eklemdir ve **doğrusal değildir**. İdeal diyotun iki çalışma bölgesi vardır: v < 0 ⇒ i = 0 (kapalı) ve i > 0 ⇒ v = 0 (açık). Diyot akımı yalnız sembolündeki ok yönünde geçiren bir elektronik "vana" gibidir; örneğin pil ters takıldığında devreyi korumak için kullanılır. Uygulama olarak işaret doğrultucu (v_I > 0 iken diyot iletir, v_O = v_I) ve diyotlu mantık kapıları tanıtılıyor.

## Lecture 2: Physical Operation of Diodes

Gerçek silisyum diyotun üç bölgesi: **ileri kutuplama** (iletimde yaklaşık 0.6–0.7 V), **ters kutuplama** (i = −I_S; küçük sinyal diyotlarında I_S ≈ fA mertebesinde) ve **kırılma** (v ≈ −V_ZK). İleri yönde i = I_S·(e^(v/nV_T) − 1); n emisyon sabiti (1–2), V_T = kT/q ≈ 25 mV. Notun devamında silisyum kristali, ısıl uyarımla oluşan elektron–delik çiftleri, deliklerin iletime katkısı, akseptör (bor, p tipi) ve donör (fosfor, n tipi) katkılama ve pn ekleminin oluşumu anlatılıyor.

## Lecture 3: DC Analysis of Diode Circuits

V_DD, R ve diyottan oluşan devrede KVL V_DD = I·R + V_D ile diyot denklemi birleşince V_D için analitik çözümü olmayan (transandantal) bir denklem çıkar. Beş çözüm yolu:

1. **Grafik çözüm:** diyot eğrisi ile yük doğrusu I = V_DD/R − V_D/R'nin kesişimi (nitel anlayış için faydalı).
1. **Simülasyon** (SPICE, ADS): 2 V, 1 kΩ ve 1N4148 için V_D = 565 mV, I = 1.43 mA.
1. **Sayısal yöntemler** (Mathematica, MATLAB, Mathcad).
1. **İteratif analiz.**
1. **Yaklaşık analiz:** en yaygın yol. **Sabit gerilim düşümü (CVD)** modelinde iletimdeki diyot 0.7 V'luk bir kaynaktır; **parçalı doğrusal (PWL)** modelde buna seri bir r_D direnci eklenir ("batarya + iç direnç").

## Lecture 4: Small-Signal Diode Model and Its Application

Zamanla değişen küçük bir işaret DC bir değerin üzerine biner: v_D(t) = V_D + v_d(t). Diyot akımı i_D(t) = I_D·e^(v_d/nV_T) olur; v_d << 2nV_T ise üstel terim ilk iki terimle yaklaşılarak i_D(t) ≈ I_D + (I_D/nV_T)·v_d(t) bulunur. Böylece **küçük sinyal direnci** r_d = nV_T / I_D tanımlanır; Q noktasındaki teğetin eğiminin tersidir ve kutuplamaya bağlıdır (PWL modelindeki r_D'den farklı bir büyüklüktür). Analiz süperpozisyonla yapılır: DC çözümden sonra "tüm DC kaynaklar sıfırlanır ve diyotun yerine r_d konur".

## Lecture 6: Zener Diodes

Ters yöndeki dik kırılma bölgesinde gerilim neredeyse sabit kalır. İki fiziksel mekanizma vardır: **Zener etkisi** (boşaltılmış bölgedeki büyük alanın elektronları bağlardan koparması) ve **çığ etkisi** (hızlanan yüklerin örgü atomlarına çarpıp yeni yükler koparması). Güç sınırı aşılmadıkça diyot zarar görmez. Üretici V_Z'yi bir test akımı I_ZT'de verir (örnek katalogda 8.2 V, 31 mA, 1 W); akım değiştikçe ΔV_Z = r_z·ΔI_Z (r_z birkaç ohm ile onlarca ohm), model V_Z = V_Z0 + r_z·I_Z. Uygulamalar: aşırı gerilim koruması ve gerilim regülasyonu.

**Örnek N6.1:** 6.8 V (5 mA'de), r_z = 20 Ω, I_ZK = 0.2 mA, 10 V ± 1 V kaynak, 500 Ω seri direnç. V_Z0 = 6.8 − 20 × 5 mA = 6.7 V; yüksüz V_O = 6.83 V; kaynaktaki ±1 V değişim çıkışta ±38.5 mV değişim yapar (**hat regülasyonu**); yük bağlanınca I_Z 3.4 mA azalır ve ΔV_O = 20 × (−3.4 mA) = −68 mV (**yük regülasyonu**).

## Lecture 7: Diode Rectifier Circuits (Half Cycle, Full Cycle, Bridge)

DC güç kaynağı blokları: transformatör (V_2/V_1 = N_2/N_1; 120 V_rms şebekeden yaklaşık 15 V için 8:1), doğrultucu, filtre, regülatör. Üç doğrultma yöntemi: **yarım dalga**, **orta uçlu tam dalga** ve en yaygın olan **köprü**. PWL modeliyle yarım dalga çıkışı v_O = [v_S − V_D0]·R/(R + r_D) (v_S > V_D0 iken), aksi hâlde sıfır. Doğrultucu diyot seçerken iki parametre önemlidir: **akım taşıma kapasitesi** ve **ters tepe gerilimi (PIV)**; yarım dalga doğrultucuda PIV = V_s.

## Lecture 8: Peak Rectifiers

Yüke paralel bir kondansatör, pozitif yarı periyotlarda tepe değerine şarj olur ve diyot kapalıyken yük üzerinden yavaşça boşalır; τ = RC >> T seçilmelidir. Boşalma v_O(t) = V_p·e^(−t/τ) ile olur (ideal olmayan diyotta V_p − 0.7). τ >> T için dalgalılık yaklaşık **V_r ≈ V_p·T/(RC) = V_p/(f·R·C)** (yarım dalga; tam dalgada T yarıya iner). Diyotun yalnız kısa bir **iletim aralığı** Δt boyunca akım geçirdiği, iletim açısının ωΔt ≈ √(2V_r/V_p) olduğu ve bu kısa sürede diyottan büyük tepe akımları aktığı gösteriliyor; ardından 2 V_pp dalgalılık için C hesabı örneği var.

## Lecture 9: Limiting and Clamping Diode Circuits, Voltage Doubler, Special Diode Types

- **Sınırlayıcılar (kırpıcılar):** gerilimi önceden belirlenen sınırlar arasında tutar; koruma ve işaret şartlandırma için kullanılır. İdeal diyotlarla istenen bir transfer fonksiyonunun nasıl gerçekleştirileceği gösteriliyor.
- **Kenetlenmiş kondansatör devresi:** diyot v_O ≥ 0 tutar, kondansatör yalnız v_I < 0 iken şarj olur; kararlı durumda kondansatör girişin negatif tepe değerine (örnekte 6 V) şarj olur ve çıkışın en alt değeri sıfıra kenetlenir. Uygulamalar: darbe genişlik modülasyonu (PWM) dedektörü ve tepe doğrultucuyla birleşerek **gerilim ikileyici** (çıkış ≈ 2V_p).
- **Özel diyotlar:** Schottky diyot (metal–n yarıiletken, yaklaşık 0.2 V ileri düşüm, azınlık taşıyıcı birikimi olmadığından hızlı), varaktör (ters kutuplu, gerilimle kontrol edilen kapasite), fotodiyot (ters kutuplu eklemde ışıkla oluşan akım) ve LED (ileri kutuplu eklemde birleşen taşıyıcıların ışık yayması).

## İndirme

ZIP dosyasında sekiz ders notunun orijinal PDF'leri (320Lecture1–4 ve 320Lecture6–9) bulunuyor.
