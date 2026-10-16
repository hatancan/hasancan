---
baslik: EEM214 Elektronik I: Deney 8 – BJT Kutuplama Devreleri ve β'ya Karşı Kararlılık (Föy ve Öğrenci Raporları)
ozet: EEM214 Elektronik I laboratuvarının 2006 tarihli Experiment 8 föyü: sabit kutuplama, emetör dirençli, kolektör geri beslemeli ve gerilim bölücü kutuplama; I_C = 6 mA için direnç tasarımı, 2N3903, 2N3904 ve BC238B ile β ölçümü ve I_CQ değişim yüzdesine göre devrelerin kararlılık sıralaması.
---

Bu yazı, Başkent Üniversitesi **EEM 214 Electronics I** laboratuvarının **Experiment 8: BJT Biasing** föyünü (Şubat 2006) ve bu deney için hazırlanmış öğrenci raporlarını içeriyor. Raporlar arkadaşların çalışması; ad ve öğrenci numaraları kapatıldı. Föy İngilizce olduğu için metni İngilizce aktarıldı. Föyün parolasız kopyası ve raporlar yazının sonunda ZIP olarak indirilebilir.

## Föy: Experiment 8 – BJT Biasing

**Aim:** To examine the different methods of setting the DC operating point (Q-point, quiescent operating point) of a transistor, to determine the most effective configuration for providing good stability with respect to changes in β, and to understand how a change of β in a transistor circuit changes the Q-point.

**Theory:** In order to use a transistor in an amplifying circuit it has to be biased; the purpose of biasing is to set the DC levels of the transistor currents and voltages (I_B, I_C, I_E and V_B, V_C, V_E). For linear applications the bias circuit must keep the transistor in the active state over the required range of input and output signals. An important issue is bias stability: β may vary significantly from transistor to transistor and with temperature, so the Q-point has to be stabilized against β variations.

Föydeki dört devre (hepsinde V_CC = 15 V, R_C = 1 kΩ):

- **Fig. 1 – sabit kutuplama:** baz V_CC'ye R_B üzerinden bağlı, emetör toprakta.
- **Fig. 2 – emetör dirençli kutuplama:** Fig. 1'e R_E = 100 Ω eklenmiş.
- **Fig. 3 – kolektör geri beslemeli kutuplama:** baz, kolektöre R_F üzerinden bağlı.
- **Fig. 4 – gerilim bölücü kutuplama:** R2 (üst) ve R1 = 2.2 kΩ (alt) bölücü, R_E = 100 Ω.

### Preliminary work

1. Review Section 5.12 of the textbook.
1. Explain why biasing is needed in transistor amplifier circuits.
1. For each circuit of Fig. 1–4: a) obtain the equations for I_B, I_C and V_CE; b) for β = 200 calculate the specified resistor (R_B, R_B, R_F, R2 respectively) to give I_C = 6 mA; c) with this resistor calculate I_C for β = 100 and β = 300.
1. Calculate the range of variation of I_CQ for each circuit as a percentage of the medium-β value, % range = 100·(I_CQ,high − I_CQ,low) / I_CQ,medium, and rate the circuits from most stable to least stable.
1. Read the experimental work.

### Experimental work

1. Measure the actual values of the resistors (1 kΩ, 100 Ω, 2.2 kΩ, 47 kΩ).
1. Build Fig. 1 with R_B = 470 kΩ and use it to find β of each of the three transistors (2N3903, 2N3904, BC238B) from V_CC, V_C and V_B. One should be below 100, one above 300 and one near the middle; the medium-β transistor is used to design the four circuits.
1. With the medium β, calculate the resistors for I_C = 6 mA (V_BE = 0.65 V, I_B = 6 mA/β): Fig. 1: R_B = (V_CC − V_BE)/I_B; Fig. 2: R_B = (V_CC − V_BE − I_C·R_E)/I_B; Fig. 3: R_F = (V_CE − V_BE)/I_B with V_CE = V_C = V_CC − I_C·R_C; Fig. 4: R2 = (V_CC − V_BE − I_C·R_E)/(I_R1 + I_B), where I_R1 = V_B/R1 = (V_BE + I_C·R_E)/R1.
1. For each circuit build it with the medium-β transistor, measure V_C and calculate I_CQ = (V_CC − V_C)/R_C, adjusting the bias resistor until V_C = 9 V ± 0.5 V; then replace the transistor with the low-β and high-β ones and repeat.
1. a) Calculate the % range of I_CQ for each circuit. b) Rate the circuits and discuss how the Q-point varies with β. c) Is there any difference between the theoretical and experimental order? Why?
1. What effect does adding an emitter resistor to the bias circuit have on bias stability? What should its value be to make the collector current less dependent on β?

**Components:** 500 kΩ potentiometer, 1 kΩ, 100 Ω, 2.2 kΩ, 2N3903, 2N3904, BC238B.

## Öğrenci raporları

### β ölçümü (Fig. 1, R_B = 470 kΩ)

| Transistör | V_C (A) | V_B (A) | β (A) | V_C (B) | V_B (B) | β (B) |
|---|---|---|---|---|---|---|
| 2N3903 | 13.242 V | 0.680 V | 54.77 | 12.951 V | 0.669 V | 68.33 |
| 2N3904 | 10.444 V | 0.712 V | 154.45 | 10.29 V | 0.715 V | 157 |
| BC238B | 4.132 V | 0.697 V | 365.7 | 4.2 V | 0.695 V | 360 |

Her iki raporda da orta β'lı transistör 2N3904 (β ≈ 155) çıkmış.

*Not: Rapor A'daki hesaplarda birimler karışmış (örneğin I_C = 1.88 A, I_B = 34.32 mA yazılmış); doğrusu I_C = (15 − 13.242)/972 Ω ≈ 1.81 mA ve I_B = (15 − 0.68)/471.2 kΩ ≈ 30.4 µA'dir, bu da β ≈ 59 verir. Diğer iki transistörün β değerleri (154, 366) birimler düzeltildiğinde de aynı kalır.*

### Tasarlanan dirençler (I_C = 6 mA)

| Devre | Rapor A (β = 154.45) | Rapor B (β = 157) |
|---|---|---|
| Fig. 1, R_B | 369.8 kΩ | 375.5 kΩ |
| Fig. 2, R_B | 354.8 kΩ | 359.8 kΩ |
| Fig. 3, R_F | 368.8 kΩ | 218.5 kΩ |
| Fig. 4, R2 | 27.2 kΩ | 22.7 kΩ |

*Not: Fig. 3'te V_CE = V_C = 15 − 6 mA × 1 kΩ = 9 V olduğundan R_F = (9 − 0.65)/(6 mA/β); β = 157 için ≈ 218 kΩ (Rapor B doğru). Rapor A'da V_C yanlışlıkla 14.96 V alınmış. Fig. 4'te I_R1 = (0.65 + 0.6)/2.2 kΩ ≈ 0.568 mA ile R2 = 13.75 V / (0.568 + 0.038) mA ≈ 22.7 kΩ çıkar.*

### Ölçülen I_CQ ve kararlılık

| Devre | β | V_C (A) | I_CQ (A) | V_C (B) | I_CQ (B) |
|---|---|---|---|---|---|
| Fig. 1 | düşük | 13.372 V | 2.628 mA | 12.060 V | 2.94 mA |
| Fig. 1 | orta | 8.993 V | 6 mA | 9.148 V | 5.852 mA |
| Fig. 1 | yüksek | 1.400 V | 13.6 mA | 2.146 V | 12.854 mA |
| Fig. 2 | düşük | 12.411 V | 2.589 mA | 11.922 V | 3.078 mA |
| Fig. 2 | orta | 9.245 V | 5.755 mA | 9.126 V | 5.874 mA |
| Fig. 2 | yüksek | 2.576 V | 12.424 mA | 2.806 V | 12.194 mA |
| Fig. 3 | düşük | 11.302 V | 3.698 mA | 12.312 V | 2.688 mA |
| Fig. 3 | orta | 9.003 V | 5.997 mA | 9.35 V | 5.65 mA |
| Fig. 3 | yüksek | 5.808 V | 9.192 mA | 6.140 V | 8.86 mA |
| Fig. 4 | düşük | 9.315 V | 5.685 mA | 9.96 V | 5.14 mA |
| Fig. 4 | orta | 9.297 V | 5.703 mA | 9.074 V | 5.926 mA |
| Fig. 4 | yüksek | 9.016 V | 5.991 mA | 9.09 V | 6.03 mA |

I_CQ değişim yüzdeleri: Rapor A'da Fig. 1 %182, Fig. 2 %171, Fig. 3 %92, Fig. 4 %5; Rapor B'de Fig. 1 %169, Fig. 2 %155, Fig. 3 %109, Fig. 4 %15. İki raporun sonucu aynı: **en kararlı devre gerilim bölücü kutuplama (Fig. 4)**, ardından kolektör geri beslemeli (Fig. 3), emetör dirençli (Fig. 2) ve en kararsız sabit kutuplama (Fig. 1). Teori ile deney arasındaki küçük farklar ölçüm hatalarına ve potansiyometrenin istenen değere tam ayarlanamamasına bağlanmış.

*Not: Rapor A'da Fig. 1 düşük β için I_CQ hesabında V_C = 12.372 V kullanılmış, tabloda ise 13.372 V yazıyor; 13.372 V ile I_CQ ≈ 1.63 mA olur.*

2008 tarihli üçüncü raporda (Türkçe) 2N3903, 2N3904 ve BC546 için β = 101, 75 ve 189 bulunmuş ve dört devrenin V_C değerleri ölçülmüş; I_CQ sütunu boş. Emetör direncinin I_E'yi ve dolayısıyla baz akımını düşürerek kararlılığı artırdığı yorumu yapılmış.

*Not: 2008 raporundaki β tablosunda I_C = V_C / 1 kΩ alınmış (örneğin V_C = 14 V için I_C = 14 mA); doğrusu I_C = (V_CC − V_C)/R_C'dir. Ayrıca BC546 için V_B = 9.7 V yazılmış, büyük olasılıkla 0.7 V olmalıydı.*

## İndirme

ZIP dosyasında föyün parolası kaldırılmış PDF'i (Experiment8.pdf) ile 2006 ve 2008 raporlarının kişisel bilgileri kapatılmış PDF kopyaları bulunuyor.
