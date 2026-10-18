---
baslik: EEM201 Devre Teorisi I: 2005–2006 Güz Ara Sınavı ve Yanıtları
ozet: Thevenin eşdeğeri, maksimum güç aktarımı ve iki kademeli ideal işlemsel yükselteç devrelerinin 2005 güz sınavı çözümleri.
---

Bu yazı, Başkent Üniversitesi **EEM201 Devre Teorisi I** dersinin **2005–2006 güz ara sınavına** ait iki soru ve dört yanıt sayfasını içeriyor. Soru kâğıdında Prof. Dr. Turhan Çiftçibaşı ve Öğr. Gör. Mustafa Doğan adları yer alıyor. EEM202 klasöründe saklanan fotoğraflanmış sayfalardan metne aktarıldı. Sınavın gün ve ayı yazmıyor; arşiv tarihi kaynak dosyaların 30 Kasım 2005 tarihidir. Fotoğraflar ve indirme dosyası yayınlanmıyor.

## Soru 1: Bağımlı kaynaklı devrenin Thevenin eşdeğeri

V₁ = 0,3 V verilmiştir. a–b uçlarından görülen Thevenin eşdeğerini bulunuz; a–b arasına 1 Ω bağlandığında i₀ akımını hesaplayınız. Devrede iki adet 1 Ω direnç, 4V₁ değerli bağımlı gerilim kaynağı ve i₁ değerli akım kontrollü gerilim kaynağı vardır.

Açık devre hesabında:

- Vₐ = V_oc + 4V₁ = V_oc + 1,2.
- Vₐ = −i₁·1 + 0,3 = −i₁ + i₁ = 0.
- **V_oc = −1,2 V.**

Kısa devre hesabında Vₐ = 1,2 V ve i₁ = −0,9 A bulunur. KCL ile **I_sc = −1,2 A**; dolayısıyla **R_Th = V_oc/I_sc = 1 Ω**.

1 Ω yük bağlanınca i₀ = V_oc/(R_Th + 1) = **−0,6 A**.

## Soru 2: Maksimum güç aktarımı

2 A ve 4 V bağımsız kaynakları ile 2Vₓ bağımlı akım kaynağı bulunan devrenin a–b eşdeğeri ve maksimum güç için R yükü isteniyor. Dirençler 1 Ω, 2 Ω, 0,5 Ω ve 1 Ω; d–c arasında 1 V kaynak var. Vₓ, yük uç gerilimidir.

Açık devrede d ve c düğümleri bir süperdüğüm oluşturur. Sayfadaki denklemler:

- 2 + V_d − (Vₐ − V_d)/2 + 2V_oc − (Vₐ − V_c)/0,5 = 0
- (Vₐ − V_c)/0,5 + (Vₐ − V_d)/2 + Vₐ − 4 = 0
- V_d − V_c = 1 ve Vₐ = V_oc.

Çözüm sayfasındaki ilk işlem satırları kırmızıyla düzeltilmiş; sonuç **V_oc = 7/11 V**. Kısa devrede Vₐ = 0, V_c = −1 V ve V_d = 0; **I_sc = 2 A** bulunuyor.

**R_Th = 7/22 Ω.** Maksimum güç için R = R_Th seçilir. Yük akımı 1 A ve **P_max = 7/22 W** olur.

*Not: Kontrol hesabı P_max = V_oc²/(4R_Th) = 7/22 W sonucunu doğrular. Düzeltilmiş sonuçlar esas alındı; üzeri düzeltilen ara işlemler yeniden çoğaltılmadı.*

## Soru 3: İki kademeli op-amp

Tüm op-amp'lar idealdir ve beslemeleri ±5 V'tur. Her kademede giriş dirençleri 1 kΩ, geri besleme direnci 3 kΩ'dur. İlk kademenin pozitif girişine V₂/2, ikinci kademeninkine V₃/2 uygulanır.

Düğüm denklemleri:

- (V₁ − V₂/2)/1k + (V_o1 − V₂/2)/3k = 0
- **V_o1 = 2V₂ − 3V₁**
- (V_o1 − V₃/2)/1k + (V_o − V₃/2)/3k = 0
- **V_o = 2V₃ − 3V_o1 = 2V₃ − 6V₂ + 9V₁**

| Girişler | İlk kademe | İkinci kademe |
|---|---|---|
| V₁ = 1 V, V₂ = 2 V, V₃ = 3 V | V_o1 = 1 V | V_o = 3 V |
| V₁ = −2 V, V₂ = 3 V, V₃ = 4 V | Hesap 12 V; besleme nedeniyle 5 V | Hesap −7 V; besleme nedeniyle −5 V |

*Not: Lineer op-amp bağıntıları yalnız doyum oluşmadığında geçerlidir. İkinci satırdaki doyum sınırları çözüm sayfasındaki gibi uygulandı.*

## Soru 4: Çıkış gerilimi ve çıkış akımı

1,1 V kaynak 3 kΩ üzerinden ilk op-amp'ın eviren girişine bağlanır; ilk geri besleme 18 kΩ, ikinci çıkıştan aynı düğüme geri besleme 24 kΩ'dur. İkinci op-amp'ın negatif girişinde 3 kΩ/27 kΩ geri besleme bölücüsü ve çıkışında 1,6 kΩ yük bulunur.

- (−1,1)/3k − V_o1/18k − V_o/24k = 0 ⇒ −4V_o1 − 3V_o = 26,4
- V_o1/27k + (V_o1 − V_o)/3k = 0 ⇒ V_o1 = 0,9V_o
- **V_o = −4 V**, V_o1 = −3,6 V.

Çıkış düğümündeki akımlar: i_24k = −1/6 mA; i_1,6k = −2,5 mA; geri besleme kolunda i_30k = −2/15 mA. KCL'den **i₀ = 2,8 mA**.
