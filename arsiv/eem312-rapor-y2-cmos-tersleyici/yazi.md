---
baslik: EEM312 Sayısal Elektronik: Y2 Raporu, Dört Tersleyici Yapısının VTC ve Gecikme Karşılaştırması (2014)
ozet: EEM312 Sayısal Elektronik yazılım laboratuvarı Y2 deneyi raporu: direnç yüklü NMOS, sözde NMOS, direnç yüklü PMOS ve CMOS tersleyicilerin SPICE'ta VTC eğrileri, VOH, VOL, VIH, VIL, VM, gürültü payları, tr, tf, tpHL, tpLH ve PMOS genişliğinin etkisi.
---

Bu yazı, Başkent Üniversitesi **EEM312 Sayısal Elektronik** yazılım laboratuvarının **Y2: CMOS tersleyici karakteristiği** deneyi için 2014'te hazırlanmış bir raporu aktarıyor. Bir arkadaşın raporu; **kişisel bilgiler çıkarıldı**. Föydeki dört devrenin şeması ve sorular [EEM312 yazılım laboratuvarı föyleri Y1–Y3](/arsiv/eem312-yazilim-deneyleri-y1-y3/) yazısında. Kişisel bilgileri kapatılmış rapor ve SPICE ağ listeleri yazının sonundaki ZIP'te.

Dört devre aynı Level 2 MOSN/MOSP modelleriyle, 3.1 V beslemeyle ve 1 fF yükle benzetilmiş:

- **(a)** 100 kΩ direnç yüklü NMOS,
- **(b)** kapısı toprağa bağlı PMOS yüklü NMOS (sözde NMOS),
- **(c)** 100 kΩ'a yük olarak bağlı PMOS (direnç yüklü PMOS),
- **(d)** CMOS tersleyici.

Örnek olarak (d) devresinin DC analizi (model parametreleri kısaltıldı):

```
*D)
.MODEL MOSN NMOS LEVEL=2 LD=0.15U TOX=200.0E-10 ...
.MODEL MOSP PMOS LEVEL=2 LD=0.15U TOX=200.0E-10 ...
VIN 3 0 PULSE(0 5 0NS 2NS 2NS 500NS 1US)
VDC 1 0 DC 3.1
C1 2 0 1ff
M1 2 3 1 1 MOSP W=1.8U L=1.2U NRS=0.333 NRD=0.333
M2 2 3 0 0 MOSN W=1.8U L=1.2U NRS=0.333 NRD=0.333
.CONTROL
DC VIN 0 5 0.1
PLOT V(2) vs V(3)
.ENDC
```

## Soru 1: VTC'den okunan değerler

| Devre | V_OH | V_OL | V_IH | V_IL | V_M | NM_H | NM_L |
|---|---|---|---|---|---|---|---|
| (a) NMOS + R | 3.10 V | 118.1 mV | 1.40 V | 700 mV | 1.23 V | 1.70 V | 581.9 mV |
| (b) sözde NMOS | 3.10 V | 296 mV | 2.0 V | 1.80 V | 1.83 V | 1.10 V | 1.504 V |
| (c) PMOS + R | 2.70 V | 0 V | 2.30 V | 1.20 V | 1.540 V | 400 mV | 1.20 V |
| (d) CMOS | 3.10 V | 0 V | 1.40 V | 1.20 V | 1.29 V | 1.70 V | 1.20 V |

Gürültü payları NM_H = V_OH − V_IH ve NM_L = V_IL − V_OL tanımlarıyla tutarlı. Yalnız CMOS tersleyicide hem V_OL = 0 hem de V_OH = V_DD; oranlı (ratioed) devrelerde (a, b) V_OL sıfıra inmiyor, (c)'de ise V_OH beslemeye çıkamıyor.

## Soru 2: Geçici durum ölçümleri

Girişe 0–3.1 V, 10 ns periyotlu darbe verilip (`PULSE(0 3.1 0 1ns 1ns 4ns 10ns)`) ölçülen süreler (ns):

| Devre | t_r | t_f | t_pHL | t_pLH | t_d |
|---|---|---|---|---|---|
| (a) | 2 | 0.4 | 0.2 | 0.8 | 0.5 |
| (b) | 0.5 | 0.3 | 0.3 | 0.2 | 0.2 |
| (c) | 1.6 | 3 | 0.4 | 0.2 | 0.4 |
| (d) | 0.4 | 0.3 | 0.2 | 0.5 | 0.3 |

Dirençli yüklerde (a'da yükselme, c'de düşme) yük 100 kΩ üzerinden dolup boşaldığı için ilgili geçiş süresi belirgin şekilde uzuyor.

*Not: t_d = (t_pHL + t_pLH)/2 ile (b) 0.25 ns, (c) 0.3 ns ve (d) 0.35 ns çıkıyor; raporda sırasıyla 0.2, 0.4 ve 0.3 ns yazılmış.*

## Soru 3–4: Yorumlar

- **En iyi tersleyici** (d) CMOS devresi: VTC'sinin geçiş bölgesi dikeye en yakın olanı, yani geçiş bölgesindeki kazancı ideal tersleyiciye en yakın.
- **Simetri:** Rapora göre devreler simetrik değil; simetri için MOSN ve MOSP tanımlarındaki sığa ve direnç değerlerinin ayarlanması gerekiyor.
- **PMOS genişliği:** Doyumdaki akım I_D = (k'/2)(W/L)(V_GS − V_T)² olduğundan PMOS'un W'si artırılınca iç direnci düşüyor, akım basma yeteneği artıyor. (d) devresinde W_p büyütülünce VTC'nin geçiş bölgesi daha dikleşmiş ve çıkış daha yüksek giriş değerlerine kadar "high" kalmış (V_M sağa kaymış).

*Not: Simetrik bir CMOS tersleyici (V_M ≈ V_DD/2, t_pHL ≈ t_pLH) için asıl ayar W/L oranlarıdır: modeldeki KP değerleri 8.0E−5 (NMOS) ve 2.7E−5 (PMOS), oranları yaklaşık 3 olduğundan W_p ≈ 3·W_n alınmalı. Föyün sonraki deneylerinde kullanılan W_p = 5.4 µm, W_n = 1.8 µm seçimi buradan gelir; bu raporda ise iki transistör de 1.8 µm olduğu için V_M (1.29 V) V_DD/2'nin (1.55 V) altında kalmış.*

ZIP'teki `y2_2017_cmos_gecici.cir`, aynı deneyin 2017 sürümüne ait CMOS tersleyici (W_p = 5.4 µm, W_n = 1.8 µm) geçici durum ağ listesidir.
