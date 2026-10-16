---
baslik: EEM312 Sayısal Elektronik: D3 Diyot Deneyi Raporları ve SPICE ile Diyot Benzetimi (2011–2017)
ozet: EEM312 Sayısal Elektronik diyot deneyi raporları: 1N4001 ile I-V ölçümü, geri toparlama süresi trr'nin frekansla değişimi, Cj ölçümü; SPICE'ta D1N4148 modeliyle I-V eğrisi, BV ters kırılma gerilimi, trr benzetimi ve diyotlu kırpıcı devre.
---

Bu yazı, Başkent Üniversitesi **EEM312 Sayısal Elektronik** laboratuvarının diyot deneyleri için yazılmış raporları bir araya getiriyor: donanım deneyi **D3: Diyot karakteristiği ve modelleri** için iki rapor (2011 ve 2014) ile aynı konunun SPICE yazılım deneyi için 2014 tarihli bir ön çalışma, bir rapor ve 2017 tarihli bir benzetim çalışması. Hepsi arkadaşların çalışmaları; **kişisel bilgiler çıkarıldı**. Donanım föyü ve ön bilgisi (C_j formülü, t_rr = t_s + t_t) [EEM312 donanım deney föyleri](/arsiv/eem312-donanim-deney-foyleri/) yazısında. Kişisel bilgileri kapatılmış raporlar, 2017 çalışmasının SPICE ağ listeleri ve ekran görüntüleri yazının sonundaki ZIP'te.

## Donanım deneyi (D3)

### 1. İleri gerilim

Diyot ölçüm devresine (D1N4001, R1 = 100 Ω) ±10 V, 1 kHz üçgen dalga uygulanmış:

- **Rapor A (2011):** diyotun ileri gerilimi **V_ON ≈ 0.6 V**.
- **Rapor B (2014):** çıkış gerilimi **V_out = 3.54 V** (giriş ±10 V, 1 kHz).

### 2. Akım–gerilim ölçümü

| Diyot gerilimi | A (2011) | B (2014) |
|---|---|---|
| −5 V | 0 | 0.09 mA |
| 0.5 V | 0.26 mA | 0.31 mA |
| 0.55 V | 0.605 mA | 0.44 mA |
| 0.6 V | 1.146 mA | 0.76 mA |
| 0.65 V | 4.513 mA | 0.97 mA |
| 0.7 V | 13.301 mA | 1.74 mA |
| 0.75 V | 47.02 mA | 1.83 mA |
| 0.8 V | ölçülmedi | 2.15 mA |

A raporu 0.8 V'u diyot yanmasın diye ölçmemiş; 0.6 V ile 0.65 V arasındaki yaklaşık dört katlık akım artışını V_ON ≈ 0.6 V'un doğrulaması olarak yorumluyor. A'daki eğri üstel diyot karakteristiğine uyuyor.

*Not: B raporundaki değerler 0.5–0.8 V arasında neredeyse doğrusal artıyor ve −5 V'ta 0.09 mA ters akım görünüyor; silisyum bir diyot için beklenen üstel davranışa uymuyor (ters akım nA mertebesinde olmalı). Ölçümde seri direnç ya da ampermetre kademesi etkisi olabilir; rapor yine de "grafik beklenen I-V eğrisine uyuyor" diyor.*

### 3. Geri toparlama süresi

Girişe 0–5 V kare dalga uygulanıp t_rr ölçülmüş:

| Frekans | A: t_rr | B: t_rr |
|---|---|---|
| 5 kHz | 20 µs | 14.40 µs |
| 10 kHz | 19 µs | 14.40 µs |
| 20 kHz | 17 µs | 13.90 µs |
| 40 kHz | 12.1 µs | 12.40 µs |
| 100 kHz | 5.2 µs | 4.6 µs |
| 200 kHz | 2.5 µs | 2.2 µs |
| 500 kHz | 1 µs | 1 µs |
| 1 MHz | 0.53 µs | 440 ns |

İki raporda da frekans arttıkça ölçülen t_rr azalıyor. B raporu 40 kHz'ten sonra toparlanmanın tam gözlenemediğini, çünkü eklem sığasının boşalamadan diyotun yeniden iletime geçtiğini yazıyor; R1'in görevini de bu sığada biriken yükün boşalmasını sağlamak olarak açıklıyor. A raporu sonuçların veri kitabına benzediğini ama koşullar farklı olduğu için aynı olmadığını, R1 büyütülürse sürenin uzayacağını (τ = RC) söylüyor.

*Not: Yüksek frekansta ölçülen sürenin yarım periyotla sınırlanması (1 MHz'te yarım periyot 0.5 µs) "azalma"nın büyük kısmını açıklıyor; yani bu frekanslarda ölçülen değer diyotun gerçek t_rr'si değil, dalganın kendisi. 1N4001 gibi genel amaçlı bir doğrultucu diyotta t_rr µs mertebesindedir.*

### 4. Eklem sığası C_j

Föydeki Şekil 4 devresinde (R2 = 10 kΩ) diyot akımı R2 üzerindeki gerilimden (I_D = V_R/R2) bulunmuş. A raporu C_j'yi C_j(V_R) = C_j0/(1 + V_R/V_j)^m formülüyle, veri kâğıdındaki C_j0 = 2 pF ve m = 0.33 ile hesaplamış.

| V_dc ofset | Frekans | A: V_D | A: V_R | A: I_D | A: C_j | B: V_D | B: I_D | B: C_j |
|---|---|---|---|---|---|---|---|---|
| 2 V | 10 kHz | 1.95 V | 30 mV | 3.02 mA | 2.09 pF | 2.45 V | 0.011 mA | 3.02E−14 |
| 3 V | 20 kHz | 3.16 V | 11.11 mV | 1.01 mA | 2.03 pF | 3.20 V | 0.011 mA | 1.67E−13 |
| 5 V | 40 kHz | 5.17 V | 0.07 mV | 0.007 mA | 2 pF | 4.9 V | 0.010 mA | 1.21E−13 |
| 8 V | 100 kHz | 7.99 V | 0.12 mV | 0.010 mA | 2 pF | 7.52 V | 0.012 mA | 1.22E−13 |
| 10 V | 200 kHz | 9.36 V | 0.15 mV | 0.016 mA | 2 pF | 9.12 V | 0.012 mA | 1.22E−13 |

Raporların yorumu: R2 diyot üzerindeki gerilimi doğrudan belirler; R2 büyüdükçe diyot gerilimi ve buna bağlı olarak C_j azalır.

*Not: A raporunda I_D = V_R/R2 ile 30 mV/10 kΩ = 3 µA, 11.11 mV/10 kΩ ≈ 1.1 µA eder; tablodaki "mA" birimleri µA olmalı. Ayrıca ters kutuplamada C_j, C_j0'dan büyük olamaz; ters gerilim arttıkça azalmalıdır. Örneğin V_R ≈ 1.95 V, V_j = 0.75 V için C_j ≈ 2 pF/(1 + 2.6)^0.33 ≈ 1.3 pF çıkar; tablodaki 2.09 pF ve sabit 2 pF değerleri formülle uyuşmuyor. B raporundaki C_j değerlerinin (F cinsinden) nasıl hesaplandığı raporda belirtilmemiş.*

## SPICE ile diyot benzetimi

### Ön çalışma (B, 2014)

SPICE'ta diyot tanımı `DXXXXXXX N+ N- MNAME <AREA> <OFF> <IC=VD> <TEMP=T>` biçimindedir: N+ ve N− bağlantı düğümleri, MNAME model adı, AREA alan çarpanı, OFF ise DC analiz için isteğe bağlı başlangıç koşuludur. D1N4148'in I-V eğrisi için hazırlanan ağ listesi:

```
*D1N4148 Diyot Akım - Voltaj Grafiği
.model D1N4148 D(IS=5.84n N=1.94 RS=.7017 XTI=3 EG=1.11 CJO=.95p
+ M=.55 VJ=.75 FC=.5 BV=100 IBV=100u TT=11.07n)
VIN 1 0 DC 5
R1 2 0 10K
D1 1 2 D1N4148
.CONTROL
DC VIN -300 200 0.1
PLOT -VIN#branch vs V(1)-V(2)
.ENDC
.END
```

### Rapor (C, 2014)

- **Ters kırılma:** Föydeki devrenin benzetiminde ters kırılma gerilimi yaklaşık **−100.3 V** okunmuş; bu, modeldeki **BV = 100** parametresine karşılık geliyor. BV = 50 yapılınca kırılma 50 V civarına kaymış; böylece BV'nin ters kırılma gerilimi parametresi olduğu gösterilmiş. Rapor, modeldeki parametrelerin diyotun statik ve dinamik davranışını tam tanımlamaya yetmediğini de ekliyor.
- **Geri toparlama:** 0–5 V kare dalgada ölçülen t_rr:

| Frekans | t_rr (R = 10 kΩ) | t_rr (R = 1 kΩ) |
|---|---|---|
| 1 kHz | 0.070 µs | 0.042 µs |
| 50 kHz | 0.065 µs | 0.039 µs |
| 100 kHz | 0.063 µs | 0.033 µs |

Frekansın t_rr'ye etkisi çok küçük, direnç 10 kΩ'dan 1 kΩ'a inince süre yaklaşık yarıya iniyor.

- **Diyotlu devre (soru 4):** Kare dalga uygulanan iki diyotlu devrede diyotlar doğrultucu/kırpıcı olarak çalışıyor, negatif kısım kırpılıyor, kondansatör süzgeç görevi görüyor. Rapor ayrıca **Schottky diyotları** tanıtıyor: çok yüksek frekansta çalışabilen, düşük gürültülü, iletim gerilimi 0.15–0.45 V olan (normal diyotlarda 0.7 V civarı) ve bu yüzden düşük gerilimli güç kaynaklarında verimi artıran diyotlar.

### 2017 benzetim çalışması

2017 tarihli çalışmada (Soru 3) aynı D1N4148 modeliyle 0–5 V darbe girişte R1 = 1 kΩ ve 10 kΩ için geri toparlama incelenmiş:

```
.MODEL D1N4148 D(IS=5.84n N=1.94 RS=.7017 XTI=3 EG=1.11 CJO=.95p
+ M=.55 VJ=.75 FC=.5 BV=100 IBV=100u TT=11.07n)
D1 1 2 D1N4148
R1 2 0 1K
Vin 1 0 PULSE (0 5 0NS 2NS 2NS 1ms 0.01ms)
.control
tran 1ns 0.1ms
plot V(2)
.endc
.end
```

| Frekans | t_rr (R1 = 1 kΩ) | t_rr (R1 = 10 kΩ) |
|---|---|---|
| 1 kHz | 425 ns | 210 ns |
| 50 kHz | 420 ns | 220 ns |
| 100 kHz | 450 ns | 210 ns |

Yorum: direnç arttıkça I = V_in/R1 akımı azalıyor, çıkış 5 V'a daha çok yaklaşıyor ve toparlanma süresi değişiyor; frekansın etkisi yine küçük. Soru 4'te ise iki diyot (D1 toprağa, D2 5 V'a) ve 5 nF kondansatörlü kırpıcı devreye ±10 V kare dalga uygulanmış; çıkış yaklaşık −0.7 V ile 5.7 V arasında kırpılıyor.

*Not: 2014 raporu (C) R = 10 kΩ'da t_rr'yi 1 kΩ'dakinden uzun, 2017 çalışması ise kısa buluyor. Darbe girişte ileri akım I_F ≈ 5 V/R olduğundan küçük R'de depolanan yük (Q = τ_T·I_F) ve dolayısıyla depolama süresi artar; 2017 çalışmasındaki eğilim bu açıdan beklenene uygun.*

## Ek: p-n eklemi üzerine el yazısı notlar

Klasörde 2014 tarihli, fotoğraflanmış iki defter sayfası var (fotoğraflar yayınlanmadı, metne aktarıldı). Notların özeti:

- Kıtlık bölgesinde taşıyıcılar tarafından oluşturulan akım **difüzyon akımı I_D** ve **sürüklenme (drift) akımı I_S** olarak ikiye ayrılır; V_D = 0 iken I_D = I_S, denge.
- **Ters kutuplama (reverse):** p tarafı kaynağın − ucuna, n tarafı + ucuna bağlanır. Elektronlar n'den, boşluklar p'den uzaklaşır; kıtlık bölgesi büyür, eşik gerilimi büyür, akımın akması zorlaşır. I = I_S − I_D; dışarıdan akan akım çok küçük doyma akımıdır.
- **İleri kutuplama (forward):** p tarafı + uca bağlanır; kıtlık bölgesi daralır, diyot yüksek akım taşıyabilir, I_D dış devre tarafından beslenir. I = I_D − I_S. Elektronlar ve boşluklar eklem bölgesinde birleşir.
- Akım kaynağıyla beslenen eklemde bağlanan yük ne olursa olsun akım sabit kalır; gerilim kaynağıyla beslenen eklemde ise uçlardaki gerilim sabit tutulur.
