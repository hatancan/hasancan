---
baslik: EEM214 Elektronik I: BJT Küçük Sinyal Modeli ve rₒ’nun Giriş Direncine Etkisi
ozet: Ortak baz ve ortak emetör bağlantıları, hibrit-π modeli, 12 voltluk BJT yükselteci örneği; emetör dirençli bağlantıda ve emetör izleyicide sonlu çıkış direncinin etkisi.
---

Bu yazı, EEM214 Elektronik I klasöründeki bir arkadaşın **8 Nisan 2013** tarihli ders notlarını ve iki el yazısı ek türetmeyi içeriyor. Fotoğraflanmış sayfalardan metne aktarıldı; kişisel bilgiler çıkarıldı. Kaynak görüntüler özel arşivde tutulduğundan bu yazıda görsel veya indirme dosyası bulunmuyor.

## Ortak baz bağlantısı ve hibrit-π modeli

Ortak baz bağlantısında giriş emetör ile baz, çıkış kolektör ile baz arasındadır. Küçük sinyal eşdeğerinde emetör giriş direnci r_e, kolektör akım kaynağı αi_e ile gösterilir:

Z_E = v_i/i_e = r_e.

BJT’nin hibrit-π modelinde baz-emetör arasında r_π, kolektör-emetör arasında g_m v_be bağımlı akım kaynağı ve r_o bulunur. Baz-kolektör arasındaki r_μ çok büyük kabul edilerek ihmal edilir.

- g_m = I_C/V_T, birimi siemens.
- V_T yaklaşık 25–26 mV.
- r_π = v_be/i_b = β/g_m = V_T/I_B.
- i_b = i_c/β = (g_m/β)v_be.
- r_e = V_T/I_E.
- I_C ≈ I_E kabulüyle r_e ≈ 1/g_m ve r_π ≈ βr_e.

*Not: r_π = βr_e eşitliği nottaki I_C ≈ I_E yaklaşımıyla kullanılmıştır. r_e = V_T/I_E tanımı tam uygulanırsa r_π = (β + 1)r_e olur.*

## Ortak emetörlü yükselteç örneği

Verilen devrede **V_CC = 12 V, R_B = 470 kΩ, R_C = 3 kΩ, β = 100, r_o = 50 kΩ**; emetör topraklıdır. İstenenler giriş/çıkış dirençleri ve gerilim/akım kazançlarıdır.

### DC çalışma noktası

I_B = (12 − 0.7)/470 kΩ = **24.04 µA**.

I_E = (β + 1)I_B ≈ **2.428 mA**.

r_e = 26 mV/2.428 mA ≈ **10.71 Ω**.

Not, I_C ≈ 2.4 mA kullanarak:

V_CEQ = 12 − 2.4 mA·3 kΩ = **4.8 V**

bulur. Yük doğrusunun uçları I_C,sat = 4 mA ve V_CE,cutoff = 12 V’tur. Q noktasının daha küçük salınım payı 4.8 V olduğundan ideal sınırlarla çizilen en büyük simetrik çıkış **9.6 V_pp** olarak gösterilir.

*Not: 9.6 V_pp hesabı doyumdaki V_CE’yi sıfır kabul eder; gerçek doyum gerilimi ve doğrusal çalışma sınırları kullanılabilir salınımı azaltır.*

### Giriş ve çıkış direnci

AC eşdeğerde besleme toprak, kuplaj kondansatörleri kısa devredir:

- Z_i = R_B ∥ βr_e = 470 kΩ ∥ 1071 Ω ≈ **1.07 kΩ**.
- Z_o = R_C ∥ r_o = 3 kΩ ∥ 50 kΩ ≈ **2.83 kΩ**.
- r_o ihmal edilirse Z_o ≈ R_C.

Çıkış direnci hesabında girişteki bağımsız işaret kaynağı sıfırlanır. Yük bağlanmışsa çıkış düğümündeki toplam paralel direnç R_C ∥ r_o ∥ R_L olur.

### Gerilim kazancı

Notta akım bölüşümüyle:

- i_RC = βi_b·r_o/(r_o + R_C).
- i_ro = βi_b·R_C/(r_o + R_C).
- v_o = −βi_b(R_C ∥ r_o).

Buradan:

A_v ≈ −(R_C ∥ r_o)/r_e.

r_o → ∞ için A_v ≈ −R_C/r_e = −3000/10.71 ≈ **−280.11**. Eksi işareti faz terslemesini belirtir. Yük varsa A_v ≈ −(R_C ∥ r_o ∥ R_L)/r_e.

### Akım kazancı

Giriş akımının baz direnci ile transistör girişi arasında bölünmesi:

i_b/i_i = R_B/(R_B + βr_e).

Çıkış akım yönü nottaki oklarla alındığında:

A_i = [βr_o/(r_o + R_C)]·[R_B/(R_B + βr_e)].

r_o → ∞ için A_i = βR_B/(R_B + βr_e).

## Ek 1: Emetör dirençli ortak emetörde sonlu rₒ

Devrede bazın toprağa direnci R_B, emetörün toprağa direnci R_E ve kolektörün toprağa direnci R_C’dir. Transistörün baz-emetör direnci βr_e, kolektör-emetör direnci r_o alınır.

Not, bağımlı kaynak dönüşümleriyle önce:

R′ = R_E ∥ (r_o + R_C) = R_E(r_o + R_C)/(R_E + r_o + R_C)

tanımını yapar. Baz gerilimi:

v_b = i_b(βr_e + R′) + [βi_b r_o/(r_o + R_C)]R′.

Böylece:

Z_b = v_b/i_b = βr_e + R′ + βr_oR′/(r_o + R_C)

= βr_e + R_E[(β + 1)r_o + R_C]/(R_E + r_o + R_C)

= **βr_e + R_E[(β + 1) + R_C/r_o]/[1 + (R_E + R_C)/r_o]**.

Yükseltecin giriş direnci **Z_i = R_B ∥ Z_b**’dir. Sonlu r_o, emetör direncinin baza yansıyan katkısını değiştirir.

## Ek 2: Emetör izleyicide sonlu rₒ

Kolektör AC toprakta olduğundan emetörün gördüğü direnç R_E ∥ r_o olur. Notun eşdeğerinden:

v_b = i_b[βr_e + (R_E ∥ r_o)] + βi_b(R_E ∥ r_o).

Z_b = βr_e + (β + 1)(R_E ∥ r_o)

= **βr_e + R_E(β + 1)/(1 + R_E/r_o)**.

Toplam giriş yine **Z_i = R_B ∥ Z_b**’dir. İki ek sayfadaki çizimler bu sonuçlara ulaşan kaynak dönüşümlerini adım adım gösterir; burada bağlantıların tanımı ve ara bağıntılar metinle korundu.
