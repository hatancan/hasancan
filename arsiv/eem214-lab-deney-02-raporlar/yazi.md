---
baslik: EEM214 Elektronik I: Deney 2 Diyot Karakteristikleri, Öğrenci Ön Çalışma ve Raporları (2006–2012)
ozet: EEM214 Elektronik I laboratuvarının diyot karakteristikleri deneyine ait öğrenci çalışmaları: 1N4148 için Shockley denklemiyle hesaplanan i–v değerleri, DMM ile diyot testi, 0.35–0.90 V ileri yön ölçüm tabloları, bulk direnci ve 1 MΩ ile ters yön akım ölçümleri.
---

Bu yazı, Başkent Üniversitesi **EEM 214 Electronics I** laboratuvarının **Experiment 2: Diode Characteristics** deneyi için farklı yıllarda (2006, 2008, 2012) hazırlanmış öğrenci ön çalışma ve raporlarını bir araya getiriyor. Hepsi arkadaşların çalışması; ad ve öğrenci numaraları kapatıldı. Deneyin föyü arşivde "Laboratuvar Deney 2 – Diyot Karakteristikleri" yazısında bulunuyor. Kişisel bilgileri kapatılmış PDF kopyaları yazının sonunda ZIP olarak indirilebilir.

## Ön çalışma: Shockley denklemiyle i–v değerleri

Föyün ön çalışmasında 1N4148 için i_D = I_S·(e^(v_D/nV_T) − 1) denklemiyle değerler hesaplanıp PSpice ile karşılaştırılıyor. 2006 ön çalışmasında I_S = 10⁻¹⁵ A ve nV_T ≈ 26 mV alınarak bulunan değerler:

| v_D (V) | 0.4 | 0.5 | 0.6 | 0.65 | 0.7 | 0.75 | 0.8 | 0.85 |
|---|---|---|---|---|---|---|---|---|
| i_D | 4.80 nA | 0.224 µA | 10.5 µA | 72.0 µA | 0.492 mA | 3.37 mA | 23 mA | 157.7 mA |

2008 ön çalışmasında farklı bir I_S ile 0.7 V için 1.14 mA, 0.8 V için 79 mA hesaplanmış; devrenin yarım dalga doğrultucu gibi yalnız pozitif yarım periyodu geçirdiği belirtilmiş. 2012 ön çalışması yalnız PSpice çizimlerinden (1N4148, 1 kΩ, 5 V tepe, 100 Hz) oluşuyor.

## Deney sonuçları

### DMM ile diyot testi

Silisyum diyot iyi ise ileri yönde DMM'nin diyot kademesi 0.500–0.900 V arası bir değer, ters yönde "1" (aralık dışı, açık devre) gösterir. Ölçülen ileri yön değerleri: 0.6648 V, 0.619 V (ohmmetre 6443 Ω), 0.6775 V (2006); 0.5913 V ve 0.6089 V (2008). Hepsinde diyotun sağlam olduğu sonucuna varılmış.

### İleri yön karakteristiği (R = 220 Ω)

| v_D (V) | Rapor A (mA) | Rapor B (mA) | Rapor C (mA) | 2008 (mA) |
|---|---|---|---|---|
| 0.35 | 0.0024 | 0.0035 | 0.0026 | 0 |
| 0.45 | 0.0252 | 0.0192 | 0.0259 | 0 |
| 0.55 | 0.255 | 0.072 | 0.196 | 0 |
| 0.60 | 0.628 | 0.153 | 0.571 | 0.45 |
| 0.65 | 1.230 | 1.133 | 1.663 | 0.90 |
| 0.70 | 6.204 | 4.942 | 4.498 | 4.61 |
| 0.75 | 11.89 | 11.43 | 10.95 | 23.23 |
| 0.80 | 25.34 | 24.38 | 24.31 | 22.85 |
| 0.85 | 48.87 | 48.93 | 48.11 | 50.56 |
| 0.90 | 88.38 | 95.29 | 79.60 | 65.02 |

Raporlarda yaklaşık 0.70 V'tan sonra akımın hızla arttığı, bunun altında diyotun "kapalı" sayılabileceği ama çok küçük bir akım geçtiği belirtiliyor. 2008 raporunda bazı değerlerin ölçü aleti ve diyot teorik sonucu vermediği için sonradan değiştirildiği, bu yüzden hata olabileceği not edilmiş.

### Bulk direnci

40 mA ve 50 mA'deki ileri yön gerilimlerinden r = ΔV/ΔI: 0.8344 → 0.8504 V için **1.6 Ω**; 0.835 → 0.853 V için **1.8 Ω**; 0.869 → 0.905 V için **3.6 Ω**.

### Ters yön (R = 1 MΩ)

Kaynak 0 ile −25 V arasında değiştirilip 1 MΩ üzerindeki gerilim ölçülerek diyot akımı I = V_R / 1 MΩ hesaplandı. Bir raporda −1 V'ta −2.97 mV, −25 V'ta −5.83 mV ölçülerek ters akım −2.97 nA ile −5.83 nA arası bulundu; diğerinde 1.40–3.89 mV ölçüldü.

*Not: 1 MΩ üzerindeki 1.40–3.89 mV gerilim 1.40–3.89 nA akıma karşılık gelir; bir raporda bu değerler mA olarak yazılmış. 2008 raporunda da ters yöndeki akım diyot geriliminden "0.99 mA ... 24.9 mA" olarak hesaplanmış; 1 MΩ üzerindeki birkaç mV'luk gerilim ile bu akımlar mümkün değildir, akımlar nA mertebesindedir.*

### Doğrultma

Yarım dalga devresinde giriş negatifken çıkış sıfır, pozitifken çıkış girişten yaklaşık 0.7–0.8 V düşük (silisyum diyotun iletim gerilimi).

## İndirme

ZIP dosyası yıllara göre klasörlenmiş sekiz ön çalışma/raporun kişisel bilgileri kapatılmış PDF kopyalarını içeriyor (2006: aynı öğrencinin ön çalışması ve iki rapor sürümü ile başka bir öğrencinin raporu; 2008: ön çalışma ve iki rapor sürümü; 2012: ön çalışma).
