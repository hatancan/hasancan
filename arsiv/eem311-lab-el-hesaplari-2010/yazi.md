---
baslik: EEM311 Elektronik II: 2010 Laboratuvarından BJT ve MOSFET El Hesapları ve Ölçümler
ozet: Fotoğraflanmış öğrenci çalışmalarından BJT küçük işaret hesabı, CD4007 ortak kaynaklı yükselteç ölçümleri ve JFET–BJT iki katlı yükseltecin DC ve AC ön çalışması.
---

Bu yazı, Başkent Üniversitesi **EEM311 Elektronik II** laboratuvarında arkadaşların hazırladığı ek ön çalışma ve rapor sayfalarını içeriyor. Kişisel bilgiler çıkarıldı; **fotoğraflanmış sayfalardan metne aktarıldı**. Fotoğraflar 14 Ekim ve 10 Kasım 2010 tarihlerinde çekilmiş. Bu yazının indirilebilir dosyası yok. Aynı dönemin diğer raporları [2010 Deney 1–4 yazısında](/arsiv/eem311-lab-raporlari-2010-deney-1-4/) bulunuyor.

## Deney 1: Ortak emetörlü BJT, el hesabı

Devre, V_CC = 15 V ile beslenen ortak emetörlü yükselteç. R_B1 = 470 kΩ, R_B2 = 1,8 kΩ ve R_C = 1 kΩ. Giriş ve çıkış kuplaj kondansatörleriyle bağlanmış; emetör toprakta.

Fotoğrafta DC çevre denklemi şöyle yazılmış:

15 V = I_B(R_B1 + R_B2) + I_C R_C

β = 320 için I_C = 320I_B alınarak:

15 V = (791,8 kΩ)I_B

I_B = **18,94 µA**, I_C = **6,061 mA**

Sayfada V_CQ = I_C R_C = 6,061 V ve V_CEQ = 6,061 V yazıyor. Aynı baz akımıyla β = 250 için I_C = 4,735 mA, β = 200 için yaklaşık 3,788 mA hesaplanmış. DC yük doğrusu ve üç farklı β için karakteristik eğriler çizilmiş.

*Not: Çizilen devrede baz direnci beslemeye bağlı; baz çevresi denkleminde V_BE bulunmalı, kolektör direnci bu çevreye girmemelidir. Ayrıca kolektör gerilimi I_C R_C değil V_CC − I_C R_C'dir. Fotoğraftaki sayılar çözüm taslağının sonuçları olarak korunmuştur; doğrulanmış çalışma noktası değildir.*

### Küçük işaret hesabı ve simülasyon çıktısı

El hesabında kullanılan bağıntılar:

r_π = nV_T/I_BQ

g_m = I_CQ/(nV_T)

r_o = (V_A + V_CE)/I_CQ

Sayfada r_π ≈ 1,32 kΩ, g_m = 242,4 µS ve r_o ≈ 17,51 kΩ yazılmış; kazanç hesabının sonunda 7,81 V / 25 mV ≈ 312,4 oranı bulunuyor. Bu satırdaki kazanç hesabı DC ve AC büyüklükleri karıştırıyor.

*Not: 6,061 mA / 25 mV = 0,2424 S = 242,4 mS eder; sayfadaki µS birimi bin kat küçüktür. Hesabın r_π değeri yaklaşık 1,32 kΩ ile uyumludur, ancak g_m'nin birimi ve DC çalışma noktası hataları kazanç hesabına taşınmıştır.*

Ayrı bir PSpice çıktı sayfasının üzerine **2 mV peak-to-peak, A_v = −92,968** notu düşülmüş. Çıktıda 0–10 ms zaman aralığında giriş ve çıkış sinüsleri ile kazanç izi var; çıkış yaklaşık 200 mV ölçeğinde, giriş ise 2 mV ölçeğinde gösterilmiş.

## Deney 3: Ortak kaynaklı MOSFET raporu

Raporda ortak kaynaklı NMOS katının DC ve AC analizi yapıldığı, CD4007'nin Proteus 7.1 modelinin bulunamaması nedeniyle PSpice kullanıldığı belirtiliyor. Ölçülen gerilimler:

| Büyüklük | Rapordaki değer |
| --- | --- |
| V_G | 3,276 V |
| V_D | 7,384 V |
| V_S | 1,46 V |

50 mV, 1 kHz giriş için dört dalga şekli elle çizilmiş: giriş, normal çıkış, C_d ve R_L olmadan çıkış, C_S olmadan çıkış. Kaydedilen kazançlar:

- Normal bağlantıda A_v = **−3,84**.
- Açık devre çıkış kazancı A_v,open = **−38,6**; çıkış 1,93 V tepeden tepeye.
- C_S kaldırıldığında A_v = **−3,654**.

Çıkış bozulmaya başlayana kadar giriş genliği artırıldığında **V_out,max = 1,09 V tepeden tepeye** kaydedilmiş.

Giriş direnci ölçümünde 50 kΩ potansiyometre ve 1 kHz kaynak kullanılmış. Metinde kaynağın 50 mV tepeden tepeye olduğu; ölçülen v_in = 940 mV ve R_in = 24,48 kΩ olduğu yazıyor. Çıkış direnci için v_out = 1,06 V tepeden tepeye ve **R_out = 16,9 kΩ** verilmiş.

*Not: Pasif giriş gerilim bölücüsünde 50 mV kaynaktan 940 mV elde edilemez. Metindeki kaynak/ölçüm genlikleri tutarsız olduğu için R_in ve R_out sonuçları bu bilgilerle doğrulanamıyor; değerler rapordaki gibi aktarıldı.*

Sonuç sayfasında başka bir simülasyon çizimi de var: CD4007 yerine **IRF9520** kullanılmış ve çalışma noktası Q(2,976 mA, 6 V) yazılmış. Bu sayfanın dirençleri R_D = 2,52 kΩ, R_S = 500 Ω; giriş 50 mV, 1 kHz, besleme 15 V. İlk ölçüm sayfasıyla aynı çalışma noktası değildir.

## Deney 4: JFET–BJT iki katlı yükselteç ön çalışması

İlk kat ortak kaynaklı JFET, ikinci kat ortak emetörlü BJT. Kuplaj kondansatörü JFET drenini BJT bazına bağlıyor; her iki katın kaynak/emetör dirençleri AC için baypaslanmış.

| Eleman / parametre | Değer |
| --- | --- |
| V_CC | 12 V |
| R_G, R_D, R_S | 1 MΩ, 1 kΩ, 330 Ω |
| BJT baz bölücüsü | 30 kΩ ve 47 kΩ |
| R_C, R_E, R_L | 1 kΩ, 2,2 kΩ, 100 kΩ |
| β, V_BE(on), V_A | 100, 0,7 V, 100 V |
| I_DSS, V_P | 50 mA, −3 V |

### JFET DC hesabı

I_D = I_DSS(1 − V_GS/V_P)²

V_G = 0, V_S = 330I_D ve V_GS = −330I_D kullanılmış:

I_D = 0,05(1 − 110I_D)²

605I_D² − 12I_D + 0,05 = 0

Seçilen kök **I_D = 5,954 mA**. Dren-kaynak çevresi:

12 = I_D(1,33 kΩ) + V_DS

**V_DS = 4,0813 V**, Q_JFET = (5,954 mA, 4,0813 V).

### BJT DC hesabı

V_BB = 12·47/77 = 7,324 V, R_B = 30 kΩ ∥ 47 kΩ = 18,31 kΩ.

Fotoğrafta V_BB = I_B[R_B + (β + 1)R_E] denklemiyle I_B ≈ 30 µA ve **I_C = 3,045 mA** bulunmuş. Son satırlarda:

12 = (1 kΩ)(3,045 mA) + V_CE + (2,2 kΩ)(3,045 mA)

**V_CE = 1,9515 V** yazılmış.

*Not: Baz çevresindeki 0,7 V V_BE terimi bu satırda atlanmış. Ayrıca gösterilen son denklemde 12 − 3,045·3,2 = 2,256 V eder; 1,9515 V sonucu aynı aritmetikle elde edilmiyor. Emetör akımı da tam hesapta I_C yerine (β + 1)I_B alınmalıdır.*

### AC hesabı

Ön çalışmada r_π = βV_T/I_C ≈ 7,41 kΩ; JFET için r_o1 = 1/(λI_D) ≈ 1,68 kΩ ve g_m1 ≈ 0,0115 S yazılmış. Birinci ve ikinci katın kazançları çarpılarak yaklaşık **A_v = 19,951** sonucuna ulaşılmış.

*Not: β = 100, V_T = 25 mV ve I_C = 3,045 mA ile r_π ≈ 821 Ω çıkar; sayfadaki 7,41 kΩ bu verilerle uyuşmuyor. Katlar birbirini yüklediğinden, birinci katın çıkış yüküne ikinci katın giriş direnci de katılmalıdır. Fotoğraf bulanık olduğu için belirsiz ara katsayılar aktarılmadı; sonuç kaynakta yazıldığı biçimiyle korunmuştur.*
