---
baslik: EEM202 Devre Teorisi II: İşlemsel Yükselteçler (Op-Amp) Ders Notları (Bülent Ecevit Üniversitesi, İsmail Şahin)
ozet: Bülent Ecevit Üniversitesi Alaplı Meslek Yüksekokulu Elektronik II ders notları (Öğr. Gör. İsmail Şahin): ideal ve gerçek op-amp özellikleri, faz çeviren ve çevirmeyen yükselteç, gerilim izleyici, toplayıcı, fark yükselteci, karşılaştırıcı, integral ve türev alıcı, aktif filtreler ve osilatörler; örnek ve test sorularıyla.
---

Bu yazı, **Bülent Ecevit Üniversitesi Alaplı Meslek Yüksekokulu**'nda **Öğr. Gör. İsmail Şahin**'in hazırladığı **"Elektronik II Ders Notları"**nı tanıtıyor (58 sayfa, PDF Aralık 2012). Notlar tamamen işlemsel yükselteçlere (op-amp) ayrılmış; EEM202 laboratuvarındaki aktif süzgeç deneyleri için kaynak olarak ders klasöründe saklanmış. Aşağıda konular, ana tanım ve formüller özetlendi; notların tamamı (orijinal PDF) yazının sonunda indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Op-amp'ın tanıtımı

Op-amp'lar doğrudan kuplajlı, yüksek kazançlı devre elemanlarıdır; devresinde fazla değişiklik yapmadan kazançları ayarlanabilir (örnek: 741 entegresi). Kullanıldıkları yerler: faz çevirici, gerilim izleyici, faz çevirmeyen yükselteç, toplayıcı, fark yükselteci, karşılaştırıcı, integral ve türev devresi, filtre, D/A çevirici, osilatör.

**İdeal op-amp'ın özellikleri:**

1. Açık çevrim gerilim kazancı sonsuzdur.
1. V1 = V2 iken V0 = 0'dır.
1. Giriş direnci sonsuz, giriş akımları sıfırdır.
1. Çıkış direnci sıfırdır.
1. Bant genişliği sonsuzdur.
1. Karakteristikleri sıcaklık ve zamanla değişmez.

## Gerçek (ideal olmayan) özellikler

- **Giriş ofset gerilimi:** Giriş katındaki transistör çiftleri tam eş olmadığından V1 = V2 = 0 iken çıkış sıfırdan farklıdır. Giriş ofset gerilimi, çıkışı sıfır yapan giriş fark gerilimidir (LM741 için yaklaşık 1 mV); 10 kΩ'luk bir potansiyometreyle ayarlanır.
- **Giriş polarma akımı (I_B):** LM741 için yaklaşık 80 nA, FET girişli tiplerde 50 pA mertebesinde.
- **Açık çevrim kazancı ve frekans karakteristiği:** K = 20 log[V0/(V2 − V1)] dB. Yüksek frekanslarda kazanç-bant genişliği çarpımı (GBW) sabittir; LM741 için **GBW = 1 MHz** (birim kazanç bant genişliği). Kapalı çevrim kazancı K_n ise bant genişliği B_n = GBW/K_n.
- **Yükselme süresi:** t_r·B_n = 0,35 (LM741 için 200 mV'luk girişte t_r = 0,3 µs).
- **Çıkış gerilimi sınırı:** çıkış besleme gerilimlerine ulaşamaz; LM741'de ±15 V beslemede yaklaşık ±13 V'ta kırpılır.
- **Büyük işaret değişim hızı (slew rate):** S = 2V_k/T_SR.
- **Ortak işaret bastırma oranı (CMRR):** fark kazancının ortak işaret kazancına oranı; LM741 için yaklaşık 90 dB.
- **Çıkış direnci (R_O).**

*Not: Belgede LM741'in giriş ofset akımı "yaklaşık 21 mA", sıcaklıkla kayması "0–5 mA/°C" ve değişim hızı "S = 0,5 V/msn" olarak yazılmış; 741'in tipik değerleri ofset akımı için yaklaşık 20 nA ve değişim hızı için **0,5 V/µs**'dir. Giriş direnci de 741 için yaklaşık 2 MΩ'dur.*

## Temel devreler

- **Faz çeviren yükselteç:** V0 = −(R_f/R_1)·V_i.
- **Faz çevirmeyen yükselteç:** V0 = (1 + R_f/R_1)·V_i. Örnek: V1 = 2 V, R_f = 500 kΩ, R_1 = 100 kΩ için V0 = 6·2 = 12 V.
- **Gerilim izleyici:** çıkış eksi girişe bağlanır; e3 = A0(e2 − e1) ve e1 = e3'ten, A0 çok büyükken e2 = e1 = e3 olur. Kazanç 1, etkin giriş empedansı Z_et = (1 + 1/A0)/(1/A0) yani yaklaşık A0 kat büyütülmüş, çıkış empedansı çok düşüktür. Bu yüzden yüksek çıkış empedanslı bir devreyi düşük giriş empedanslı bir devreye bağlamak için "tampon" olarak kullanılır.
- **Toplayıcı:** V0 = −R_f(V1/R1 + V2/R2 + … + Vn/Rn). R_f = R1 = R2 = … seçilirse girişler yükseltilmeden toplanır: örneğin V1 = 5 V, V2 = 5 V, Vn = −1 V için V0 = −9 V.
- **Fark yükselteci:** iki girişin farkını yükseltir; R1 = R2 ve R3 = R_f ise V0 = (R_f/R1)(V2 − V1). Örnek: R1 = R2 = 20 kΩ, R3 = R_f = 40 kΩ, V1 = 2 V, V2 = 8 V için V0 = 2·(8 − 2) = 12 V.
- **Karşılaştırıcı:** girişler arasındaki küçük bir fark bile açık çevrim kazancıyla (yaklaşık 200 000) çarpılır; Vi > Vref ise V0 ≈ +V, Vi < Vref ise V0 ≈ −V. TTL devre sürülecekse çıkışa diyot eklenir.

## İntegral ve türev alıcı devreler

- **İntegral alıcı:** geri besleme yolunda kondansatör, girişte direnç: V0 = −(1/RC)∫V_i dt. Kondansatörün reaktansı X_C = 1/(2πfC).
- **Türev alıcı:** integral devresindeki direnç ile kondansatörün yerleri değiştirilir: V0 = −RC·dV_i/dt. Transfer fonksiyonu ve uygulamaları (diyotlu devreler dahil) veriliyor.

## Op-amp'lı filtreler

- **Alçak geçiren filtre:** üst kesim frekansı f_OH = 1/(2πRC) (R = X_C koşulu).
- **Yüksek geçiren filtre:** alt kesim frekansı f_OL = 1/(2πRC).
- **Bant geçiren filtre:** yüksek ve alçak geçiren bölümlerin art arda bağlanmasıyla. Örnek: R1 = R3 = 10 kΩ, C1 = 0,01 µF, C2 = 0,001 µF için alt kesim frekansı 1/(2π·10 kΩ·0,01 µF) ≈ 1,59 kHz, üst kesim frekansı 1/(2π·10 kΩ·0,001 µF) ≈ 15,9 kHz.

## Osilatörler

Op-amp'lı faz kaymalı RC osilatör, Wien köprü osilatörü ve kristal kontrollü osilatör devreleri ve çalışma frekansları.

## Sorular

Her bölümün sonunda örnek sorular, üç test sorusu seti (cevap anahtarlarıyla), çözümlü 10 problem ve filtrelerin kesim frekanslarıyla ilgili sorular var.

## İndirilebilir dosya

58 sayfalık orijinal PDF aşağıdan indirilebilir.
