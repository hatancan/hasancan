---
baslik: EEM214 Elektronik I: Deney 7 – BJT'nin DC Davranışı ve i_C–v_CE Karakteristikleri (Föy ve Öğrenci Raporları)
ozet: EEM214 Elektronik I laboratuvarının BJT föyü (2006 Experiment 7, 2012'de Experiment 8 olarak yeniden kullanılmış): BC238B ile ortak emetörlü devre, kesim–aktif–doyum bölgeleri, β ölçümü, yük doğrusu, Early gerilimi; ayrıca 2006, 2008 ve 2012 öğrenci raporlarındaki I_B–I_C–V_CE ölçüm tabloları.
---

Bu yazı, Başkent Üniversitesi **EEM 214 Electronics I** laboratuvarının **Bipolar Junction Transistor** deney föyünü ve bu deney için üç farklı yılda hazırlanmış öğrenci raporlarını bir araya getiriyor. Föy 2006'da **Experiment 7** olarak hazırlanmış; 2012'de neredeyse aynı metinle **Experiment 8** başlığıyla yeniden kullanılmış (iki sürüm de ZIP'te). Raporlar arkadaşların çalışması; ad ve öğrenci numaraları kapatıldı. Föy İngilizce olduğu için metni İngilizce aktarıldı. Kuram için [Ders 5 – BJT Transistörler](/arsiv/eem214-ders-05-bjt/) yazısına bakılabilir.

## Föy: Bipolar Junction Transistor

**Aim:** The aim of this experiment is to investigate the DC behavior of a bipolar junction transistor (BJT) in a common emitter circuit configuration.

### Theory

Like the MOSFET, the BJT is a three-terminal device: base (B), collector (C) and emitter (E); it can be NPN or PNP. Unlike MOSFETs, the total current in a BJT consists of both electron and hole currents. The BJT is regarded as a current-controlled current device: the base current controls the current flowing between collector and emitter.

At the input side, I_B is determined by V_BB and R_B. When V_BB < V_BE(ON) the transistor is cut off (OFF) and I_B = 0. When V_BB > V_BE(ON), I_B = (V_BB − V_BE(ON)) / R_B and the transistor may be forward-active (ACT) or saturated (SAT), depending on I_C and V_CE. At the output side the load line V_CC = R_C·i_C + v_CE, intersected with the transistor i_C–v_CE curve for the given I_B, determines the Q-point. If the intersection is in the constant-current region the transistor is in ACT, I_C = β·I_B and V_CE > V_CE(SAT). Otherwise it is in SAT, V_CE ≈ V_CE(SAT) and I_C = (V_CC − V_CE(SAT)) / R_C, where I_C < β·I_B.

### Preliminary work

Review Section 5 up to 5.10 of the textbook. The circuit is built with a **BC238B**: V_BB (0–12 V, variable) through R_B = 100 kΩ to the base, emitter grounded, collector through R_C (1 kΩ) to V_CC = 15 V. The BC238B has 200 < β < 320, V_CE(SAT) = 0.2 V, V_BE(ON) = 0.6 V and V_A = 100 V; use V_T = 25 mV and n = 1. I_B is measured from the voltage across the 100 kΩ resistor.

1. Determine the range of I_B that can be obtained with 0 ≤ V_BB ≤ 12 V (V_BE(ON) = 0.6 V).
1. With β = 260 and V_CE(SAT) = 0.2 V, draw the piecewise-linear i_C–v_CE characteristics for I_B = 0–100 µA in 20 µA steps, and on the same graph the load lines for R_C = 1 kΩ and V_CC = 15, 10, 5 and 1 V.
1. Note that V_CC, R_C and I_B all influence the state of the transistor and V_CE. In the lab you will change I_B and measure I_C with R_C = 1 kΩ and V_CC = 15 V fixed.
1. Determine the I_B that pushes the transistor into saturation (R_C = 1 kΩ, V_CC = 15 V).
1. Repeat for R_C = 2.2 kΩ.
1. List and explain all differences between the piecewise-linear model and the actual i_B–v_BE and i_C–v_CE characteristics in all states (OFF, ACT, SAT).
1. Simulate with PSpice (after including the BC238B model; its β is about 310–330) with R_C = 1 kΩ, V_CC = 15 V: plot V_CE versus V_BB for 0–12 V (DC sweep) and indicate the OFF, ACT and SAT regions.
1. Zoom into the SAT region to see the small changes of V_CE as V_BB increases and comment.

### Experimental work

Verify that all resistors are within 2% of their marked values. Build the circuit with R_C = 1 kΩ and V_CC = 15 V. Measure I_B from the drop across 100 kΩ and I_C from the drop across R_C.

1. Set I_B = 0 µA; measure I_C and V_CE. What is the state of the transistor?
1. Set I_B = 5–40 µA in 5 µA steps; measure I_C and V_CE, make sure the transistor is not saturated, calculate β and find the average of the eight values (use it in the rest of the experiment).
1. Plot I_C versus V_CE, fit a straight line and find its axis crossings. What does this line represent?
1. Set I_B = 50–100 µA in 10 µA steps; determine the state by comparing β·I_B with I_C. How does V_CE compare with V_CE(SAT) before and after saturation?
1. Add these points to the plot of part 3; has the straight-line behavior changed?
1. Trace the i_C–v_CE characteristic at I_B = 20 µA by decreasing V_CC from 15 V in steps of at most 1 V (closer points in SAT).
1. From these data determine the Early voltage V_A (slope in ACT and its crossing of the v_CE axis).
1. Replace R_C with 2.2 kΩ, set I_B = 5–70 µA and measure I_C and V_CE. How does R_C influence the I_B value that pushes the transistor into SAT?

**Components:** BC238B NPN transistor, 100 kΩ, 1 kΩ, 2.2 kΩ.

## Öğrenci raporları

### I_B = 0

2006: I_C = 0.01 µA, V_CE = 15.13 V; 2008: I_C = 0, V_CE = 14.894 V; 2012: I_C = 0, V_CE = 15 V. Transistör kesimde.

### β ölçümü (R_C = 1 kΩ, V_CC = 15 V)

| I_B (µA) | I_C 2006 (mA) | V_CE 2006 (V) | β 2006 | I_C 2012 (mA) | V_CE 2012 (V) | β 2012 |
|---|---|---|---|---|---|---|
| 5 | 2.58 | 12.565 | 510 | 2.240 | 10.502 | 448 |
| 10 | 5.286 | 9.870 | 528 | 5.838 (11 µA) | 6.854 | 530 |
| 15 | 7.901 | 7.247 | 523 | 8.356 | 4.341 | 557 |
| 20 | 10.162 | 4.997 | 509 | 12.634 | 2.546 | 631 |
| 25 | 12.151 | 3.003 | 487 | 12.650 | 0.777 | 506 |
| 30 | 13.911 | 1.240 | 460 | 12.664 | 0.459 | 422 |
| 35 | 14.646 | 0.493 | 417 | 12.641 | 0.397 | 361 |
| 40 | 14.753 | 0.387 | 368 | 12.315 | 0.368 | 307 |

2006 raporunda ortalama β = 475 bulunmuş. Ölçülen β değerleri föydeki 200–320 aralığının oldukça üzerinde. 2008 raporunda dördüncü ölçümde transistör arızalandığı ve kalan ölçümler yeni bir transistörle yapıldığı için β değerlerinde (128–588) büyük sıçramalar var.

*Not: 2006 raporunda ortalama "3082 / 8 = 475" diye yazılmış; sekiz β değerinin toplamı 3802'dir, ortalama 3802 / 8 ≈ 475 doğru.*

### Doyuma girme (I_B = 50–100 µA)

| I_B (µA) | I_C (mA) | V_CE (V) | I_C/I_B |
|---|---|---|---|
| 50 | 14.86 | 0.278 | 297 |
| 60 | 14.919 | 0.227 | 248 |
| 70 | 14.945 | 0.202 | 213 |
| 80 | 14.961 | 0.182 | 187 |
| 90 | 14.972 | 0.175 | 166 |
| 100 | 14.980 | 0.167 | 149 |

(2006 raporu.) I_C, (15 − V_CE(SAT)) / 1 kΩ ≈ 14.8 mA civarında sabitleniyor; I_C/I_B oranı β·I_B'nin çok altına düşüyor, yani transistör doyumda. 2008 ve 2012 raporlarında da benzer biçimde I_C ≈ 14.5–14.8 mA ve 12.4 mA'de sabit kalıyor.

### Sabit I_B = 20 µA'de V_CC taraması (2006)

| V_CC (V) | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I_C (mA) | 10.23 | 9.89 | 9.75 | 9.53 | 9.31 | 9.09 | 8.72 | 7.89 | 6.89 | 5.94 | 4.92 | 3.94 | 2.93 | 1.99 | 0.99 |
| V_CE (V) | 4.963 | 4.262 | 3.484 | 2.616 | 1.805 | 1.004 | 0.379 | 0.255 | 0.199 | 0.170 | 0.149 | 0.132 | 0.115 | 0.098 | 0.074 |

*Not: Raporda Early gerilimi bölümü boş bırakılmış. Aktif bölgedeki iki uç noktadan eğim (10.23 − 9.09) mA / (4.963 − 1.004) V ≈ 0.29 mA/V bulunur; bu doğru v_CE eksenini yaklaşık −31 V'ta keser, yani bu ölçümlerden V_A ≈ 31 V çıkar.*

### R_C = 2.2 kΩ

2006 raporunda I_B = 5 ve 10 µA'de transistör aktif (β ≈ 493, 481); I_B = 15 µA'den itibaren I_C ≈ 6.7–6.8 mA'de sabitlenip V_CE 0.28 V'un altına iniyor. 2012 raporunda transistör daha 5 µA'de doyuma girmiş (I_C ≈ 5.5–5.76 mA). Daha büyük R_C ile yük doğrusunun eğimi azaldığından transistör daha küçük I_B'de doyuma giriyor.

2008 raporunda β'nın değişme nedenleri sıcaklık, doyum noktası, Early olayı ve frekans olarak sıralanmış; laboratuvarda frekans değişmediği ve sıcaklık fazla değişmediği için β'daki değişimin esas olarak doyum noktası ve az da olsa Early olayından kaynaklandığı belirtilmiş.

## İndirme

ZIP dosyasında 2006 (Experiment 7, parolası kaldırılmış) ve 2012 (Experiment 8 başlıklı) föyleri ile 2006, 2008 ve 2012 raporlarının kişisel bilgileri kapatılmış PDF kopyaları bulunuyor.
