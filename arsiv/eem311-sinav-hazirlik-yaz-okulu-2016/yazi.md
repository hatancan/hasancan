---
baslik: EEM311 Elektronik II: 2016 Yaz Okulu Sınav Hazırlık Notları, Aktif Filtreler, Osilatörler ve Geri Besleme
ozet: EEM311 Elektronik II 2016 yaz okulunda tutulmuş el yazısı notlar: Butterworth yüksek geçiren ve bant geçiren filtre tasarımı, kalite faktörü ve dar bantlı BGF, Hartley, Colpitts, Clapp ve kristal osilatörler, geri besleme türleri ve empedans değişimleri, akım ve transkondüktans geri beslemeli yükselteç örnekleri.
---

Bu yazı, Başkent Üniversitesi **EEM 311 Elektronik II** dersinin **2016 yaz okulunda** (27 Temmuz – 9 Ağustos 2016) bir arkadaşın tuttuğu el yazısı ders notlarını ve derste tahtaya yazılan örnek soruları aktarıyor. Notlar, final sınavına hazırlık için geçmiş sınav sorularıyla birlikte derlenmiş. Kişisel bilgiler çıkarıldı. İçerik fotoğraflanmış sayfalardan metne aktarıldı; fotoğrafların kendisi yayınlanmıyor. El yazısının okunamadığı yerler belirtildi.

## Butterworth yüksek geçiren filtreler (27.07.2016)

### İkinci derece yüksek geçiren filtre (YGF)

Devre: girişte iki seri kapasite (C₁ = C₂ = C), aralarındaki düğümden op-amp çıkışına R₁ = R, op-amp'ın evirmeyen girişinden toprağa R₂ = 2R; op-amp gerilim izleyici gibi bağlı.

f_c = 1 / (2π √(R₁ R₂ C₁ C₂)) = 1 / (2π R C √2)

Kazanç eğrisi: f_c'de kazanç 0,707 (−3 dB), f_c/10'da 0,01 (−40 dB); geçiş bölgesindeki eğim **−40 dB/dekad** (frekans azaldıkça).

**Örnek:** 1 kHz'de çıkışı 1/100 oranında azaltan, 10 kHz ve üzerini geçiren devreyi tasarlayınız. C = 1 nF olsun.

R = 1 / (2π · 10⁻⁹ · 10 · 10³ · √2) = …

*Not: Notta sonuç yazılmamış; hesaplanırsa R ≅ 11,25 kΩ (R₂ = 2R ≅ 22,5 kΩ) bulunur.*

### Üçüncü derece YGF

İkinci derece YGF katının arkasına birinci derece bir YGF katı (C₃ = C, R₃ = R, gerilim izleyici) eklenir. f_c/10'da kazanç 0,001 (−60 dB); eğim **−60 dB/dekad**.

**Örnekler:**

- 2 kHz altındaki sinyalleri −60 dB/dekad eğimle bastıran devreyi tasarlayınız (C = 0,1 µF): R = 1 / (2π · f_c · C) biçiminde (notta değer yazılmamış).
- 5 kHz üzerini geçiren 3 kutuplu filtre devresini tasarlayınız.

## Bant geçiren filtreler

Bant geçiren filtre (BGF), bir alçak geçiren filtre (AGF) ile bir YGF'nin kaskat bağlanmasıyla elde edilir. Alt kesim frekansı f_L, YGF'nin kesim frekansı; üst kesim frekansı f_H, AGF'nin kesim frekansıdır. Bant genişliği BW = f_H − f_L.

### Birinci derece BGF

Birinci derece AGF (seri R, toprağa C, gerilim izleyici) ardından birinci derece YGF (seri C, toprağa R, gerilim izleyici). Her iki uçta eğim −20 dB/dekad.

**Örnek:** 1 kHz – 10 kHz arasını geçiren birinci derece BGF tasarlayınız (C = 0,1 µF). 1 kHz YGF, 10 kHz AGF içindir:

- AGF için: f_c = 1 / (2π · 10 · 10³ · 0,1 · 10⁻⁶ · R)
- YGF için: f_c = 1 / (2π · 10³ · 0,1 · 10⁻⁶ · R)

*Not: Buradan AGF için R ≅ 159 Ω, YGF için R ≅ 1,59 kΩ çıkar (notta sayısal değer yok).*

### İkinci derece BGF

İkinci derece YGF (C₁ = C₂ = C, R₁ = R, R₂ = 2R) ardından ikinci derece AGF (R₃ = R₄ = R*, C₃ = 2C*, C₄ = C*).

**Örnek:** 300 Hz – 3 kHz arasını geçiren filtreyi tasarlayınız.

- YGF için f_c = 300 Hz = 1 / (2π R C √2), C = 0,01 µF
- AGF için f_c = 3 kHz = 1 / (2π R C √2), C* = 0,1 µF

### Kalite faktörü

- Merkez frekansı: f_m = f_L + BW/2 = f_H − BW/2
- Rezonans frekansı: f_r = √(f_L f_H)
- Kalite faktörü: Q = f_r / BW. Notta Q ≥ 10 için dar bantlı, Q < 10 için geniş bantlı yazılmış; yanına ayrıca Q ≥ 0,5 dar bant, Q < 0,5 geniş bant ölçütü eklenmiş.

**Örnek:** f_r = √(300 · 3000) = 948,68 Hz, BW = 3000 − 300 = 2700 Hz, Q = 948,68 / 2700 ≅ 0,35 (notta 0,3) ⇒ geniş bantlı.

### Dar bantlı BGF (çoklu geri beslemeli)

Notta "ezberleme" diye işaretlenmiş devre: giriş R₁ üzerinden bir düğüme; bu düğümden toprağa R₃, op-amp çıkışına C₁, op-amp'ın eviren girişine C₂; eviren giriş ile çıkış arasında R₂.

- f_r = 1 / (2π C √((R₁ ‖ R₃) R₂))
- R₁ = Q / (2π f_r C A_f)
- R₂ = Q / (π f_r C)
- R₃ = Q / (2π f_r C (2Q² − A_f))
- Q = f_r / BW = 2π f_r A_f C R₁ = π f_r C R₂

*Not: Kazanç ifadesi notta "A_f = R₂/R₁" gibi okunuyor; yukarıdaki R₁ ve R₂ formülleri birbirine bölündüğünde R₂/R₁ = 2A_f, yani A_f = R₂/(2R₁) çıkar.*

**Örnek:** 10 kanallı bir ekolayzerin rezonans frekansları 1 kHz, 2 kHz, …, 10 kHz şeklindedir. Ekolayzerin 6. bant filtresini Q = 10 için tasarlayınız. f_r = 6 kHz, BW = f_r / Q = 6 kHz / 10 = 600 Hz.

## Osilatörler (1.8.2016)

LC osilatörlerde yükseltecin geri besleme ağındaki üç empedansın türüne göre:

| Osilatör | Z₁ | Z₂ | Z₃ |
|---|---|---|---|
| Hartley | L | L | C |
| Colpitts | C | C | L |
| Clapp | C | C | L ve C (seri) |
| Kristal | C | C | X_TAL (kristal) |

- **Hartley osilatör (op-amp'lı):** A bloğu R₁ ve R₂ ile kurulmuş eviren yükselteç; β bloğu orta ucu topraklı iki bobin (Z₂, Z₁) ve bunların uçları arasındaki kapasite (Z₃).
- **Transistörlü Hartley osilatör:** ortak emetörlü BJT'nin kolektöründe paralel Z₃ kapasitesi ve orta uçlu Z₁–Z₂ bobini; çıkış bobine sarılı ikinci sargıdan alınıyor (transformatör kuplajlı).
- **JFET'li Hartley osilatör:** aynı geri besleme ağı JFET'li bir yükseltecin girişine bağlanmış.
- **Kristal osilatör (op-amp'lı):** β bloğunda orta noktası topraklı iki kapasite ve bunlara paralel kristal (X_TAL).

## Geri beslemeli yükselteçler (2.8.2016)

Geri beslemenin avantajları:

- Giriş empedansı ne kadar büyükse o kadar iyi: R_i ↑, R_o ↓
- Yükseltecin frekans cevabını iyileştirir (BW ↑)
- Daha lineer bir çalışma yapar

Tek transistörlü ortak emetörlü devrede köprülenmemiş R_E de devrenin geri beslemesidir.

### Geri besleme türleri

| Örnekleme / karışım | Yükselteç türü | A | β |
|---|---|---|---|
| Gerilim-gerilim (seri karışım, şönt örnekleme) | Gerilim yükselteci | V_o / V_i | V_f / V_o |
| Akım-gerilim (şönt karışım, şönt örnekleme) | Transrezistans yükselteci | V_o / I_i | I_f / V_o |
| Gerilim-akım (seri karışım, seri örnekleme) | Transkondüktans yükselteci | I_o / V_i | V_f / I_o |
| Akım-akım (şönt karışım, seri örnekleme) | Akım yükselteci | I_o / I_i | I_f / I_o |

Notta kısaca: geri besleme girişe seri, çıkışa paralel bağlıysa gerilim yükselteci.

*Not: Notta gerilim-akım ve akım-akım türleri için çıkış tarafı "paralel sampled" diye yazılmış; bu iki türde çıkış akımı seri örneklenir, tabloda bu şekilde verildi.*

### Giriş-çıkış empedans değişimleri

| | Gerilim-seri (seri-şönt) | Akım-seri (seri-seri) | Gerilim-şönt (şönt-şönt) | Akım-şönt (şönt-seri) |
|---|---|---|---|---|
| Z_if | Z_i (1 + βA) | Z_i (1 + βA) | Z_i / (1 + βA) | Z_i / (1 + βA) |
| Z_of | Z_o / (1 + βA) | Z_o (1 + βA) | Z_o / (1 + βA) | Z_o (1 + βA) |

Kural: giriş seri ise (1 + βA) ile çarp, giriş şönt ise (1 + βA) ile böl; çıkışta gerilim örneklemede böl, akım örneklemede çarp.

**Örnek (seri-şönt):** Evirmeyen op-amp yükselteçte A = 100 000, R₁ = 1,8 kΩ, R₂ = 200 Ω ise devrenin geri beslemeli kazancını bulunuz.

β = V_f / V_o = R₂ / (R₁ + R₂) = 0,1

A ≫ 1 olduğundan 1 + Aβ ≅ Aβ ⇒ A_v = A / (Aβ) = 1/β = **10**

## Örnekleme-karışım ve sınav sorusu (5.8.2016)

Notta tekrar özetlenmiş:

- Seri karışım – seri örnekleme → transkondüktans yükselteci
- Seri karışım – şönt örnekleme → gerilim yükselteci
- Şönt karışım – şönt örnekleme → transrezistans yükselteci
- Şönt karışım – seri örnekleme → akım yükselteci
- Geri besleme devresinin yükleme etkisi bulunurken: seri tarafta açık devre, şönt tarafta kısa devre yapılır.

### Sınav sorusu (25 puan): geri beslemeli akım kazancı

Tahtaya yazılan soru: β = 100, r_o = ∞, r_π1 = 13,1 kΩ (= (β+1) r_e), r_π2 = 1,9 kΩ, g_m1 = 7,62 mS, g_m2 = 52,7 mS. Devrenin geri beslemeli akım kazancını bulunuz: A_if = I_o / I_s = ?

*Devre:* V⁺ = +10 V. Giriş akım kaynağı I_s, R_S = 10 kΩ ile paralel, Q₁'in bazına bağlı. Q₁'in kolektörü R_C1 = 40 kΩ ile V⁺'ya, emetörü toprağa bağlı. Q₂'nin bazı Q₁'in kolektörüne bağlı; R_C2 = 2 kΩ, çıkış C → ∞ üzerinden R_L = 0,5 kΩ'a (I_o yük akımı); Q₂'nin emetöründe R_E = 1 kΩ. Geri besleme direnci R_F = 10 kΩ (seri C → ∞ ile) Q₂'nin emetöründen (V_e düğümü) Q₁'in bazına bağlı (şönt-seri, akım yükselteci).

**Çözüm (düğüm denklemleri, tahtada ve notta):**

1. I_s = V_π1 (1/10 + 1/13,1 + 1/10) − V_e (1/10) ⇒ I_s = V_π1 (0,2763) − V_e (0,1)
1. (7,62) V_π1 + V_π2 (1/40 + 1/1,9) + V_e (1/40) = 0 ⇒ (7,62) V_π1 + V_π2 (0,5513) + V_e (0,025) = 0
1. V_π2 (1/1,9 + 52,7) = V_e (1/1 + 1/10) − V_π1 (1/10) ⇒ V_π2 (53,23) = V_e (1,1) − V_π1 (0,1)

(3)'ten: V_e = V_π2 (48,39) + V_π1 (0,0909). (1)'de yerine konursa:

I_s = V_π1 (0,2763) − (0,1)[V_π2 (48,39) + V_π1 (0,0909)] ⇒ I_s = V_π1 (0,2672) − V_π2 (4,839)

(2)'de yerine konursa: (7,622) V_π1 + V_π2 (1,761) = 0 ⇒ V_π1 = −V_π2 (0,2310)

Buradan I_s = (0,2672)(−V_π2)(0,2310) − V_π2 (4,839) ⇒ I_s = −V_π2 (4,901)

I_o = −g_m2 V_π2 [R_C2 / (R_C2 + R_L)] = (−52,7)(2 / 2,5) V_π2 = −42,16 V_π2

I_o = −(42,16)(−I_s / 4,901) ⇒ **A_if = I_o / I_s ≅ 8,60**

## Transkondüktans geri beslemeli yükselteç (9.8.2016)

Notta başlığı tam okunamayan ("… Sorusu") üç transistörlü devre: r_o = ∞, β = 120, V_T = 26 mV, I_C1 = 0,5 mA, I_C2 = 1 mA, I_C3 = 2 mA. Devrenin transkondüktans transfer fonksiyonunu bulunuz: A_gf = I_o / V_s = ?

- Geri besleme devresi: Q₁ ve Q₃'ün emetörleri arasındaki direnç (R_E) ile iki emetör direnci (R_E1, R_E2).
- Girişe yansıyan direnç R₁₁ = R_E1 (notta), çıkışa yansıyan direnç R₂₂ = R_E + R_E1.
- ac eşdeğer devrede her transistör β r_e direnci ve β I_b akım kaynağıyla modellenmiş; I_o = β I_b3.
- Q₁'in emetör düğümü için ilk denklem: I_b1 + β I_b1 = V_e1 / R_E1 + (V_e1 − V_e2) / R_E

Notta çözüm bu noktada bırakılmış. (Bu soru 2016 Ocak finalinin 2. sorusudur; cevap anahtarındaki sonuç A_gf ≅ 98 mA/V.)

Bir başka sayfada, üç katlı bir yükseltecin ac eşdeğerinde geri besleme ağının yükleme dirençleri hesaplanmış: R₁₁ = 9 kΩ ‖ 1 kΩ = 0,9 kΩ, R₂₂ = 9 kΩ + 1 kΩ = 10 kΩ, R_i3 = β r_e3 + β[(9 k + 1 k) ‖ R_L].

## Yüksek frekans cevabı

Yüksek frekans cevabını transistörün dahili (gizli) kapasiteleri belirler: C_be, C_bc ve C_ce. Harici kapasiteler (C_i, C_o kuplaj kapasiteleri) yüksek frekansta hesaba katılmaz.

- C_bc, Miller teoremiyle iki tarafa yansıtılır: C_Miller,giriş = C_bc (1 + |A_v|), C_Miller,çıkış = C_bc (1 + 1/|A_v|)
- Paralel kapasiteler toplanır.

**Frekans cevabı soruları (örnek):** alçak frekans tarafında üç kırılma frekansı 500 Hz, 700 Hz ve 1 kHz olarak verilmiş; en yüksek kırılmadan sonraki kazanç 100 kabul edilip kırılma noktalarındaki kazanç sırayla hesaplanıyor: A_V(700 Hz) = 100 / √(1 + (1 kHz / 700 Hz)²). Grafikte kazanç değerleri 100, 70,7 ve 65 olarak işaretlenmiş. Genel kural notta "A_V = bir önceki kazanç / √(1 + (oran)²)" şeklinde, alçak ve yüksek frekans tarafı için ayrı ayrı yazılmış; oranın payı ve paydası el yazısında tam seçilemiyor.
