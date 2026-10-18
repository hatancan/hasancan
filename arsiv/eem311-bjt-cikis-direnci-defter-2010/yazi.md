---
baslik: EEM311 Elektronik II: BJT Yükselteç Tasarımı ve Çıkış Direnci, 2010 Defter Notları
ozet: Ortak emetörlü BJT için −10 kazanç ve 500 kΩ giriş direnci tasarımı; ortak bazlı ve emetör dirençli yükselteçlerde test kaynağıyla çıkış direncinin türetilmesi.
---

Bu yazı, Başkent Üniversitesi **EEM311 Elektronik II** dersinden bir arkadaşın defter notlarını içeriyor. Sayfalar **fotoğraflanmış sayfalardan metne aktarıldı**; kişisel bilgiler çıkarıldı. Fotoğrafların çekim tarihleri 6 Ekim ve 11 Kasım 2010. Aynı sayfanın iki çekimi birlikte okundu. Bu yazının indirilebilir dosyası yok.

## Çalışma noktası ve ısıl kararlılık

Notta transistörde harcanan güç, P = V_CE·I_C çarpımıyla ele alınıyor. Çalışma noktasının maksimum güç hiperbolünü aşmaması, β ve sıcaklık değişimlerine karşı kararlı tutulması isteniyor. Emetör direnci ve geri besleme, çalışma noktasını kararlı tutmak için kullanılan araçlar olarak işaretlenmiş.

## Ortak emetörlü yükselteç tasarımı

Örnek 14.11 için verilenler: **β = 75, A_v = −10, R_in = 500 kΩ**, kaynak direnci R_s = 100 Ω. Emetörde R_E var; küçük işaret eşdeğerinde baz-emetör arasında r_π, kolektörde β·i_b bağımlı akım kaynağı bulunuyor. Çıkıştaki yük R_L ile gösterilmiş.

Baz gerilimi ve giriş direnci:

v_b = i_b r_π + (β + 1)i_b R_E

R_in = v_b/i_b = r_π + (β + 1)R_E

Notta r_π = βr_e ve (β + 1)R_E ≫ βr_e yaklaşımı kullanılıyor:

R_in ≈ (β + 1)R_E ⇒ R_E ≈ 500 kΩ / 76 = **6,58 kΩ**

Gerilim kazancı:

A_v = −βR_L / [r_π + (β + 1)R_E] = −βR_L / R_in

−10 = −75R_L / 500 kΩ ⇒ **R_L ≈ 66,7 kΩ**

Burada kazancın giriş gerilimi, transistörün bazındaki v_i olarak tanımlanmış; kaynak direncinin önündeki v_s ile aynı düğüm değildir.

## Ortak bazlı devrede çıkış direnci

Örnek 14.34'te giriş emetöre, çıkış kolektöre bağlı; baz AC toprakta. Not, kazanç hesabında T modelinin, çıkış direnci türetiminde hibrit-π modelinin kullanıldığını belirtiyor.

Transistörün sonlu çıkış direnci:

r_o = (V_A + V_CE)/I_CQ

Çıkış direnci hesabı için giriş gerilim kaynağı kısa devre ediliyor, yük R_L kaldırılıyor ve kolektöre v_x test kaynağı bağlanıyor. Test kaynağının akımı i_x; **R_out = v_x/i_x**.

Emetörün toprağa eşdeğer direnci:

R_eq = r_π ∥ R_4 ∥ R_I

Notta R_I giriş kaynağına seri direnci, R_4 emetördeki diğer direnci gösteriyor. Bağıntılar:

v_e = −v_be = i_x R_eq

i_ro = i_x − g_m v_be = i_x(1 + g_m R_eq)

v_x = i_ro r_o − v_be

Yerine koyunca:

v_x = i_x(1 + g_m R_eq)r_o + i_x R_eq

**R_out = (1 + g_m R_eq)r_o + R_eq**

Sonuç, çıkış yükü kaldırıldıktan sonra transistör katına bakılarak bulunan dirençtir.

## Emetör dirençli ortak emetör katında çıkış direnci

14.11 örneğinin devamında giriş kaynağı sıfırlanıyor; baz R_s üzerinden toprağa, emetör R_E üzerinden toprağa bağlı. Kolektöre v_x uygulanıyor. Notta baz akımı i, kolektörden giren test akımı i_x ile gösterilmiş.

R_T = r_π + R_s + R_E

v_e = (i_x + i)R_E = −i(r_π + R_s)

−i = (R_E/R_T)i_x

Böylece:

v_e = [R_E ∥ (r_π + R_s)]i_x

i_ro = i_x − βi = i_x[1 + βR_E/R_T]

v_x = i_ro r_o + v_e

**R_out = [1 + βR_E/(r_π + R_s + R_E)]r_o + [R_E ∥ (r_π + R_s)]**

Defterde ikinci kez yazılan son satırdaki parantez içi direnç simgesi belirsiz; burada üstteki açık türetim esas alındı. Sayfada bu çıkış direnci için sayısal bir sonuç verilmemiş.
