---
baslik: EEM312 Sayısal Elektronik: Statik ve Dinamik Güç Deney Raporları, CMOS Tersleyicide Güç ve Güç-Gecikme Çarpanı (2005–2017)
ozet: EEM312 Sayısal Elektronik yazılım laboratuvarının statik ve dinamik güç deneyi için 2005–2017 arası dokuz öğrenci raporunun karşılaştırması: CMOS tersleyicide kısa devre akımı, Pdyn = C·VDD²·f, periyot, VDD ve yük sığasının etkisi, VDD'ye karşı güç-gecikme çarpanı ve en uygun besleme gerilimi.
---

Bu yazı, Başkent Üniversitesi **EEM312 Sayısal Elektronik** yazılım laboratuvarının **statik ve dinamik güç** deneyi için yazılmış dokuz raporu karşılaştırıyor. Deney yıllara göre farklı numaralarla yapılmış: 2005–2006'da **Y7**, 2011 föylerinde **Y5**, 2014'te "Deney 9", 2017'de yine "Deney 9". Raporlar: 19 Mayıs 2005 tarihli bir rapor (A), 2006 baharından beş rapor (B–F), 2011'den (G), 2014'ten (H) ve 2017'den (I) birer rapor. Hepsi arkadaşların çalışmaları; **kişisel bilgiler çıkarıldı**. Föy [EEM312 yazılım laboratuvarı föyleri Y4–Y8](/arsiv/eem312-yazilim-deneyleri-y4-y8/) yazısında (Y5 bölümü). Kişisel bilgileri kapatılmış raporlar ve SPICE ağ listeleri yazının sonundaki ZIP'te.

Devre, föydeki Level 2 modelli CMOS tersleyici: PMOS L/W = 1.2 µm/5.4 µm, NMOS L/W = 1.2 µm/1.8 µm. Anlık güç, besleme kaynağının akımı ile geriliminin çarpımından alınıyor; 2017 raporunun ağ listesinde ortalama da doğrudan hesaplatılıyor:

```
M1 3 1 0 0 MOSN W=1.8u L=1.2u NRS=0.333 NRD=0.333
M2 3 1 2 2 MOSP W=5.4u L=1.2u NRS=0.333 NRD=0.333
Vdd 2 0 5V
Cl 3 0 0.1p
Vin 1 0 pulse (0V 5V 0 10ns 10ns 100ns 200ns)
.control
tran 0.1ns 800ns
print mean (-Vdd#branch*V(2))
plot -Vdd#branch*V(2)
.endc
```

## 1a. DC analiz: kısa devre gücü

V_in 0–5 V taranırken (V_DD da 0–5 V arasında adımlanarak) beslemeden çekilen güç, giriş V_DD/2 civarındayken en büyük değerini alıyor: raporlar tepe noktasını V_in ≈ 2.65–2.7 V olarak okuyor. Bu bölgede NMOS ve PMOS aynı anda iletimde olduğu için V_DD'den toprağa doğrudan bir yol oluşuyor (kısa devre/doğrudan yol akımı). V_DD büyüdükçe bu tepe hızla yükseliyor; B raporu bunu P_stat = I_stat·V_DD ile açıklıyor.

## 1b–d. Dinamik güç: periyot, V_DD ve C_L'nin etkisi

Dinamik güç **P_dyn = P₀→₁·C_L·V_DD²·f** ile verilir. Tüm raporların ortak gözlemi: güç tüketimi yalnız anahtarlama anlarında oluşuyor; en büyük tepe, yük kondansatörünün PMOS üzerinden beslemeden doldurulduğu **çıkışın 0'dan 1'e geçişinde** görülüyor, boşalmada beslemeden enerji çekilmiyor.

Kuramsal değerler (C raporunun hesabı): C_L = 0.1 pF, V_DD = 5 V için 200 ns periyotta (f = 5 MHz) P_dyn = 12.5 µW, 100 ns periyotta (10 MHz) 25 µW; C_L = 0.2 pF'ta 50 µW. Benzetim sonuçları:

| Koşul (V_DD = 5 V) | A/G | B/H | E | F | I |
|---|---|---|---|---|---|
| C_L = 0.1 pF, T = 200 ns | 15.1 µW | 15.1 µW | – | 31.9 µW | 5.06 µW |
| C_L = 0.1 pF, T = 100 ns | 30.14 µW | 30.14 µW | 31.1 µW | 63.4 µW | 2.50 µW |
| C_L = 0.2 pF, T = 100 ns | – | 55.04 µW | 56.1 µW | 83.7 µW | 56.1 µW |

V_DD'nin etkisi: E raporunda C_L = 0.2 pF, T = 100 ns'de V_DD = 3 V için 19.6 µW, 5 V için 56.1 µW (oran ≈ 2.9, V_DD² oranı 25/9 ≈ 2.8); F raporunda 3 V için 21.9 µW. Rapor A, G ve C, C_L iki katına çıkınca gücün de iki katına çıktığını (25 µW → 50 µW) hesapla gösteriyor.

*Not: A, B, G ve H raporlarında ortalama güçler "15.1 W", "30.14 W", "55.04 W" gibi watt cinsinden yazılmış; benzetimin verdiği değerler mikrowatt mertebesinde (ör. 0.1 pF·25 V²·10 MHz = 25 µW). Tabloda birimler µW olarak düzeltildi.*

*Not: B ve H raporlarında C_L = 0.2 pF, T = 200 ns için 55.04 µW, T = 100 ns için 20 µW yazılmış; frekans iki katına çıkınca güç artmalıdır, iki değer yer değiştirmiş ya da yanlış ölçülmüş görünüyor (tabloya 55.04 µW, T = 100 ns satırına alındı). I raporunda da 100 ns periyot için 2.50 µW, 200 ns için 5.06 µW bulunup "her iki periyotta güç aynı" ve "geçiş süresi arttıkça güç arttı" denmiş; bu sonuçlar P_dyn ∝ f bağıntısıyla çelişiyor (frekansla güç artmalı).*

*Not: A raporunda C_L iki katına çıkınca benzetimde "güç değişmedi" yazılmış, aynı raporun kuramsal hesabı ise iki kat artış öngörüyor; E ve F raporlarındaki benzetimler artışı gösteriyor.*

## 2. V_DD'ye karşı güç-gecikme çarpanı

C_L = 0.1 pF, T = 100 ns'de V_DD 1–5 V arasında değiştirilip ortalama güç P_av, yayılım gecikmesi t_p ve **PDP = P_av·t_p** bulunmuş.

| V_DD | A/G: t_p | A/G: P_av | A/G: PDP | B/H: P_av | B/H: t_p | B/H: PDP | E: PDP | D: PDP |
|---|---|---|---|---|---|---|---|---|
| 1 V | 3550 ps | 1.19 µW | 4.23 fJ | 1.354 µW | 3540 ps | 4.79 fJ | 4.22 fJ | 4.19 fJ |
| 1.5 V | 1850 ps | 2.6 µW | 4.81 fJ | 2.91 µW | 1862 ps | 5.4 fJ | 4.83 fJ | 4.78 fJ |
| 2 V | 1350 ps | 4.7 µW | 6.34 fJ | 5.05 µW | 1339 ps | 6.76 fJ | 6.3 fJ | 6.37 fJ |
| 2.5 V | 1000 ps | 7.36 µW | 7.4 fJ | 7.78 µW | 1020 ps | 7.93 fJ | 7.43 fJ | 7.38 fJ |
| 3 V | 820 ps | 10.6 µW | 8.7 fJ | 11.1 µW | 860 ps | 9.55 fJ | 9.01 fJ | 8.72 fJ |
| 4 V | 850 ps | 19.3 µW | 16.41 fJ | 19.5 µW | 835 ps | 16.3 fJ | 16.21 fJ | 16.38 fJ |
| 5 V | 750 ps | 31.2 µW | 23.4 fJ | 30.14 µW | 764 ps | 23 fJ | 23.55 fJ | 23.44 fJ |

F raporu ayrı bir benzetimde daha büyük değerler bulmuş (ör. 1 V'ta 1.24 µW ve 5.85 ns, 2.5 V'ta 8.29 µW ve 2.38 ns, 5 V'ta 63.33 µW ve 1.78 ns). C raporu ise PDP'yi kuramsal P_dyn = C_L·V_DD²·f değerleriyle (1 V'ta 1 µW, 5 V'ta 25 µW) hesaplamış.

Hemen hepsi en iyi çalışma noktasını **V_DD = 2.5 V** olarak seçiyor: bu değerin altında gecikme hızla büyüyor, üstünde ise güç V_DD² ile artarken gecikme pek azalmıyor. Kısa kanallı MOSFET'ler için ortak yorum: kanal direnci ve t_p küçülür, ortalama güç değişmezse PDP azalır.

*Not: Tablolardaki PDP değerleri P_av·t_p çarpımıyla tutarlı (ör. 1.19 µW × 3.55 ns = 4.22 fJ). Ancak PDP V_DD ile sürekli artıyor; en küçük PDP 1 V'ta. 2.5 V seçimi PDP'nin minimumundan değil, enerji ile hızın birlikte gözetilmesinden geliyor: enerji-gecikme çarpanı PDP·t_p, A/G değerleriyle 1 V'ta ≈ 15·10⁻²⁴, 2 V'ta 8.6·10⁻²⁴, 2.5 V'ta 7.4·10⁻²⁴, 3 V'ta 7.1·10⁻²⁴ ve 5 V'ta 17.6·10⁻²⁴ J·s; yani en uygun bölge gerçekten 2.5–3 V civarı.*

*Not: D ve E raporlarında PDP'nin birimi "W", C raporunda "pW" yazılmış; PDP bir enerjidir, birimi joule (burada fJ). C raporunun "3.03 pW" değeri de 1 µW × 303 ps = 0.303 fJ olmalı. F raporunun PDP sütunu ise kendi P_av ve t_p değerlerinin çarpımıyla uyuşmuyor (ör. 1 V için 1.24 µW × 5.85 ns ≈ 7.3 fJ, raporda 5.85 fJ).*

## Raporlar arasındaki benzerlikler

Klasördeki raporların bir kısmı aynı benzetim sonuçlarını paylaşıyor: A ile G'nin PDP tablosu ve metinleri, B ile H'nin güç ve PDP değerleri birebir aynı. Bunlar karşılaştırmayı kolaylaştırsın diye tabloda birlikte gösterildi. A'nın tablosunu ve metnini aynen kullanan iki rapor ile E'nin metnini aynen kullanan bir rapor kopya olduğu için ayrıca alınmadı.
