---
baslik: EEM442 Haberleşme II: Temel Bant Modülasyonu (PAM, PDM/PWM, PPM, PCM, Hat Kodları, Delta Modülasyonu)
ozet: EEM442 Haberleşme II dersinin 2017 bahar 02 ve 03 numaralı sunumları: örnekleme ve Nyquist, bant geçiren örnekleme, doğal ve tut-bırak örnekleme, darbe modülasyonları, PCM, nicemleme SNR'si, hat kodları, mu-law ve A-law, delta modülasyonu.
---

Başkent Üniversitesi'nde 2017 bahar yarıyılında verilen **EEM 442 Haberleşme II (Communications II)** dersinin iki sunumu: *02 – Baseband Modulation (PAM-PDM-PPM)* ve *03 – Baseband Modulation (PCM-DM)* (28 Mart 2017). Sunumlar İngilizcedir, açıklamalar burada Türkçedir; formüller sunum içeriğine sadıktır, slayttaki şekiller metne dökülmüştür. Ders adını dosya adları ve slayt başlığından doğruluyorum (klasörde "Haberleşme II", sunum başlığında "EEM 442 Communications II"). Sunumların yazarı dosyada belirtilmemiştir (ders öğretim elemanının kendi sunumu). İki sunumun orijinali yazının sonunda ZIP olarak indirilebilir.

## 02 – Temel bant modülasyonu: örnekleme ve darbe modülasyonları

### İdeal örnekleme

Mesaj m(t), dürtü dizisi p(t) = Σδ(t − kT_s) ile çarpılır: m_s(t) = m(t)·p(t) (dürtü örnekleme); örnek değerleri m_s[k] = m_s(t)|_{t = kT_s} (nokta örnekleme). Frekans bölgesinde çarpma evrişime dönüşür: M_s(f) = M(f) * P(f), P(f) = (1/T_s)·Σδ(f − n/T_s) ve

M_s(f) = (1/T_s)·Σ M(f − n/T_s),

yani mesaj tayfı f_s aralıklarla tekrarlanır.

**Örtüşme ve Nyquist ölçütü:** f_s − f_m < f_m olduğunda frekans bölgesinde örtüşme (aliasing) olur; örtüşme olmaması için **f_s ≥ 2·f_m** olmalıdır (Nyquist ölçütü).

*Örnek:* Aşağıdaki işaretler için minimum örnekleme hızını bulunuz: a) x(t) = sinc(6000t), b) x(t) = rect(3000t), c) x(t) = cos(2π·10⁴t) + sin(2π·10⁵t).

### Bant geçiren örnekleme

- Basit durum f_H = k·B: k tek ise F_s = 2B (f_H = 3B, 5B, …), k çift ise de F_s = 2B (f_H = 6B…) olarak gösterilir.
- Genel durum f_H ≠ k·B: (k − 1)F_s ≤ 2F_L ve 2F_H ≤ k·F_s, yani 2F_H/k ≤ F_s ≤ 2F_L/(k − 1); k_max ≤ F_H/B. F_s seçimi için grafik verilir.
- Pratik yaklaşım: n = ⌊(2f_c − B)/B⌋ = ⌊2f_L/B⌋ olmak üzere (2f_c − B)/n ≥ f_s ≥ (2f_c + B)/(n + 1), yani 2f_L/n ≥ f_s ≥ 2f_H/(n + 1).
- *Örnekler:* (a) −100…−75 ve 75…100 MHz bandındaki bir işaret; (b) x(t) = sinc(600t)·cos(2π·20·10³t) için minimum örnekleme hızı.

### Doğal örnekleme

s(t) = Σ c_n·e^{j2πnf_s t} = c_0 + Σ c_n·cos(2πnf_s t); c_n = (τ/T_s)·sinc(nτ/T_s). x_s(t) = x(t)·s(t) için X_s(f) = c_0·X(f) + Σ c_n·X(f − nf_s) + Σ c_n·X(f + nf_s): tayf c_n ağırlıklarıyla f_s katlarına kopyalanır.

*Örnek:* x(t) = 10000·sinc(2000t) Nyquist hızıyla örneklenirse örneklenmiş işaretin tayfı yukarıdaki biçimdedir, c_n = (τ/T_s)·sinc(nτ/T_s), τ/T_s = 0,1: (a) Nyquist hızını bulunuz, (b) Nyquist hızında örneklenmiş işaretin tayfını çiziniz, (c) 50 Hz koruma bandı kullanıldığında tayfı çiziniz.

### Tut ve bırak (flat-top) örnekleme ve darbe modülasyonları

- **PAM (darbe genlik modülasyonu):** örnekleme dürtüleri x(t) ile modüle edilir; darbe genliği örnek değerine karşılık gelir, darbe genişliği τ sabittir. Ortalama güç P_avg = (A²·τ/T_s)·⟨x²(t)⟩.
- **PDM/PWM (darbe süre/genişlik modülasyonu):** darbe süresi mesaja göre değişir, τ(t) = τ_0 + t_0·x(t) (τ_3 > τ_2 > τ_1); P_avg = (A²/T_s)·⟨τ(t)⟩.
- **PPM (darbe konum modülasyonu):** darbe sabit genlik ve genişlikte, konumu (gecikmesi d) mesaja göre değişir; P_avg = A²·τ/T_s = A²·τ·f_s.

## 03 – PCM ve delta modülasyonu

### Darbe kod modülasyonu (PCM)

**Nicemleme:** seviye sayısı Q = 2ⁿ (n: bit sayısı); adım a = (A_max − A_min)/Q. Örnek: 8 seviyeli, 3 bitli nicemleme (000 … 111); PCM çıkışı örnekleme anlarındaki seviye kodlarının art arda dizilmesidir (örnek: PCM = 111101010110).

**Nicemleme bozulması:** e(t) = x(t) − x_q(t), e düzgün dağılımlıysa ⟨e²⟩ = ∫ e²·P_e(e) de = a²/12. SNR = ⟨x²(t)⟩/⟨e²(t)⟩. x(t) = A·cos(2πft) ve a = 2A/2ⁿ için ⟨x²⟩ = A²/2 olduğundan

**SNR = (3/2)·2^{2n}**, **SNR_dB = 10·log10((3/2)·2^{2n}) = 1,76 + 6,02n.**

Dinamik aralık ve SNR: SNR = 1,76 + 6,02n; (S/N)_q = 10·log10(3Q²). *Örnek:* Bir sayısallaştırma sistemi 55 dB dinamik aralık belirtiyor; kaç bit gerekir, sistemin SNR'si ve (S/N)_q değeri nedir?

**Zaman bölmeli çoklama (TDM):** birden çok mesaj bir anahtarla (komütatör) sırayla örneklenir ve tek PCM kanalından gönderilir (örnek soru verilmiştir).

### Hat kodları

| Kod | Kuralı | Avantajları | Dezavantajları |
|---|---|---|---|
| **Tek kutuplu NRZ** | 1 → +V, 0 → 0 | basit gerçekleme, düşük bant genişliği | DC düzeyi, düşük frekans bileşenleri, hata düzeltme yok, senkronizasyon zor |
| **Tek kutuplu RZ** | 1 → +V yarım bit, sonra 0 | basit, sembol hızında spektral çizgi | DC düzeyi, düşük frekans bileşenleri, hata düzeltme yok, tek kutuplu NRZ'nin iki katı bant genişliği |
| **Kutuplu (polar) NRZ** | 1 → +V, 0 → −V | basit, DC bileşeni yok | hata düzeltme yok, senkronizasyon zor |
| **Kutuplu RZ** | 1 → +V yarım bit, 0 → −V yarım bit | basit, DC yok | hata düzeltme yok, polar NRZ'nin iki katı bant genişliği |
| **İki kutuplu (bipolar, AMI)** | 0 → darbe yok; 1 → +V ve −V art arda dönüşümlü (üç düzey: +V, 0, −V) | DC yok, tek kutuplu ve polar NRZ'ye göre daha az bant genişliği, hata algılama yeteneği | senkronizasyon zor |
| **Manchester** | bit süresi ikiye bölünür; 0 → ilk yarı +, ikinci yarı −; 1 → ilk yarı −, ikinci yarı + | DC yok, senkronizasyon kolay | çok geniş bant gerekir, hata algılama yok |

Slaytlar ayrıca hat kodlarının güç spektral yoğunluklarını ve bir karşılaştırma tablosunu gösterir.

### Düzgün olmayan nicemleme ve sıkıştırma-genleştirme (companding)

Düzgün (uniform) ve düzgün olmayan (non-uniform) nicemleme karşılaştırılır; düzgün olmayan nicemleme, sıkıştırıcı (compressor) + düzgün nicemleyici + genleştirici (expander) ile gerçeklenir. İki standart:
- **µ-law**: dinamik aralığı daha büyüktür; küçük sinyallerde bozulma daha kötüdür; Kuzey Amerika ve Japonya'da kullanılır.
- **A-law**: Avrupa'da yaygındır.

### Delta modülasyonu (DM)

İki ardışık örnek arasındaki farkın işaretini (1 bit) göndererek kodlama yapar; blok diyagramı karşılaştırıcı, örnekleyici ve geri beslemede entegratörden oluşur. Sorunlar: **eğim aşırı yüklenmesi (slope overload)**, sinyal adım büyüklüğünden hızlı değişince; **granüler (tanecikli) gürültü**, adım çok büyük olunca durağan sinyalde. Bu konuların laboratuvar uygulaması için bkz. "Haberleşme laboratuvarı: kuantalama, µ-law, delta modülasyonu".
