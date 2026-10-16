---
baslik: EEM311 Elektronik II: 2009 Ödev Soruları ve Çözüm Taslağı, Fark Yükselteci ve MOSFET–BJT Çok Katlı Yükselteç
ozet: EEM311 Elektronik II için el yazısı ödev soruları ve çözüm taslağı (Aralık 2009): akım kaynaklı fark yükselteci ve PNP aktif yüklü çıkış katında Q noktaları, NMOS–PNP–PMOS üç katlı yükselteçte çalışma noktaları ve AC eşdeğer devre.
---

Bu yazı, **EEM311 Elektronik II** dersi için kâğıda elle yazılmış üç soruluk bir ödev ya da çalışma sorusu setini ve yarım kalmış bir çözüm taslağını içeriyor (Aralık 2009; arşivde laboratuvar notlarının arasında duruyordu). **Bir arkadaşın çalışması; kişisel bilgiler çıkarıldı.** Sayfalar **fotoğraflanmış sayfalardan metne aktarıldı**; devre şemaları sözle anlatıldı. Bu yazının indirilebilir dosyası yok.

## Soru 1: Fark yükselteci

Şekildeki fark yükselteci devresinde uyumlu (balanced) devre elemanları kullanılmıştır. Devre: Q1–Q2 npn fark çifti (kolektör dirençleri R_C1, emetörler I1 akım kaynağıyla −V_EE'ye, girişler V_A ve V_B); Q2'nin kolektörü pnp fark çifti Q3–Q4'ün bazına bağlı (Q3–Q4'ün emetörleri I2 akım kaynağıyla beslenir, kolektör dirençleri R_C2 −V_EE'ye gider); Q4'ün kolektörü pnp çıkış transistörü Q5'in bazını sürer, Q5'in emetörü I3 kaynağıyla beslenir ve çıkış V_o, R_L yüküne verilir.

- npn transistörler için: β = 100, V_A = 50 V, V_BE = 0.7 V
- pnp transistörler için: β = 50, V_A = 70 V, V_EB = 0.7 V
- V_T = 25 mV, V_CC = V_EE = 3 V
- R_C1 = 300 kΩ, R_C2 = 78 kΩ, R_L = 7 kΩ
- I1 = 10 µA, I2 = 50 µA, I3 = 250 µA, DC'de V_o = 0

a) Transistörlerin Q noktalarını bulunuz: Q(I_CQ, V_CEQ).

b) Devrenin küçük işaret AC eşdeğerini çiziniz; kazancı hesaplayınız: A_v = V_o / (V_A − V_B), R_in = ?, R_out = ?

### Çözüm taslağı

- Çıkış katı: I_C5 + I_B5 = 250 µA → 51·I_B5 = 250 µA → I_B5 = 4.9 µA, I_C5 = 2.45 × 10⁻⁴ A.
- Q3–Q4 katı: I_C4 + I_B4 = 25 µA → 51·I_B4 = 25 µA → I_B4 = 0.47 µA, I_C4 = 50·0.47 µA = **23.5 µA**; aynı şekilde I_B3 = 0.47 µA, I_C3 = 23.5 µA. R_C2 akımı I_C4 + I_B5 ≈ 23.5 µA alınmış.
- Giriş katı: I_C2 + I_B4 = 5 µA → I_C2 = 5 µA − 0.47 µA = **4.53 µA**, I_C1 = 4.53 µA.
- V_CE1 = 6 − I_C1·R_C1 = 6 − 4.53 µA·300 kΩ = 4.64 V; V_CE2 = 4.64 V.
- V_CE3 = −6 + I_C3·78 kΩ = −6 + 1.833 = −4.167 V; V_CE4 = −4.167 V; V_CE5 bulunmamış.
- Sonuç: Q1(4.53 µA, 4.64 V), Q2(4.53 µA, 4.64 V), Q3(23.5 µA, −4.167 V), Q4(23.5 µA, −4.167 V).

*Not: V_CE hesaplarında toplam besleme (V_CC + V_EE = 6 V) kullanılmış ama emetör gerilimleri hesaba katılmamış. Girişler toprakta iken Q1 ve Q2'nin emetörü ≈ −0.7 V olduğundan V_CE1 = 3 − 4.53 µA·300 kΩ + 0.7 ≈ 2.34 V olur.*

## Soru 2: Üç katlı MOSFET–BJT yükselteç

V_CC = 10 V. M1 (NMOS) ortak kaynaklı kat: kapı 20 kΩ–80 kΩ gerilim bölücüyle beslenir, drende 2 kΩ, kaynakta 5 kΩ direnç. M1'in dreni Q1 (PNP) transistörünün bazına bağlı; Q1'in emetöründe 150 Ω (V_CC'ye), kolektöründe 700 Ω (toprağa) var. Q1'in kolektörü M2 (PMOS) transistörünün kapısını sürer; M2'nin bir ucu V_CC'ye, diğer ucu 50 Ω'luk dirençle toprağa bağlı; çıkış V_o bu direncin üzerinden alınır.

- β = 100, V_EB = 0.7 V, V_TN = 2 V, V_TP = −1 V
- K_n = 8.8 mA/V², K_p = 50 mA/V², λ = 0

a) Yükseltecin çalışma noktalarını bulunuz; V_G, V_S, V_B, V_E, V_C, V_O noktalarının gerilimlerini bulunuz.

b) FET'lerin doyumda olup olmadığını kontrol ediniz.

### Çözüm taslağı

- V_G = 80 k / 100 k · 10 V = **8 V**
- I_D = (K_n/2)(V_GS − V_TN)²; −V_G + V_GS + I_D·5 kΩ = 0 yazılmış ve K_n/2 = 4.4 alınarak 4.4·V_GS² − 16.6·V_GS + 9.6 = 0 denklemi çözülmüş: V_GS = 3.059 V (diğer kök 0.713 V), I_D = 4.4 × 10⁻³·(1.059)² = **4.93 mA**; Q1(4.93 mA, 3.059 V).
- Devamında V_DS = 10 − I_D(R_S + R_D), V_B = V_DS + I_D·5 kΩ, V_S = I_D·5 kΩ ve Q1 için −10 + 150·I_E − V_CE + 700·I_C = 0 gibi denklemler kurulmuş; M2 için I_D = (K_p/2)(V_GS − V_TP)² = 25 × 10⁻³(V_GS + 1)² ve V_DS = 10 − I_D·50 yazılmış. Sayısal sonuçlar tamamlanmamış.

*Not: K_n/2 = 4.4 mA/V² olduğu için denklemde I_D·5 kΩ terimi 4.4 mA·5 kΩ = 22 V/V² katsayısı vermeli: 8 = V_GS + 22(V_GS − 2)². Bu denklemden V_GS = 2.5 V, I_D = 4.4 mA/V²·(0.5 V)² = **1.1 mA** ve V_S = 5.5 V bulunur. Taslaktaki 4.93 mA sonucu kaynak gerilimini (4.93 mA·5 kΩ ≈ 24.7 V) beslemeden büyük yaptığı için mümkün değil.*

## Soru 3: AC eşdeğer ve kazanç

a) 2. soruda verilen devrenin AC eşdeğerini çiziniz.

b) Her bir katın kazancını ayrı ayrı bulunuz; bu kazançları kullanarak toplam kazancı bulunuz: A_vT = V_o / V_G = ?

### Çözüm taslağı

AC eşdeğerde giriş direnci 20 kΩ ∥ 80 kΩ = **16 kΩ**. Birinci kat (M1, kaynakta 5 kΩ), A düğümünde 2 kΩ dren direnci; ikinci kat (Q1: rπ, β·i_b kaynağı, emetörde 150 Ω, kolektörde 700 Ω), B düğümü; üçüncü kat (M2, kaynakta 50 Ω, çıkış C düğümü) çizilmiş. Toplam kazanç katların çarpımı olarak yazılmış:

A_v = (A / v_i)·(B / A)·(v_o / B) = v_o / v_i

Sayısal kazançlar hesaplanmamış.
