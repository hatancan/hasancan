---
baslik: EEM311 Elektronik II: 2010 Ödev Çözüm Taslakları, Üç Katlı Yükselteç ve Transistörlü Op-amp
ozet: Üç BJT'li yükseltecin DC çalışma noktaları ve küçük işaret hesabı; iki fark katı ve çıkış katından oluşan dokuz transistörlü op-amp tasarımının el yazısı çözüm taslağı.
---

Bu yazı, Başkent Üniversitesi **EEM311 Elektronik II** dersinde arkadaşların hazırladığı iki el yazısı çözüm taslağını içeriyor. Kişisel bilgiler çıkarıldı; **fotoğraflanmış sayfalardan metne aktarıldı**. Fotoğraflar 9–10 Kasım ve 17 Aralık 2010 tarihlerinde çekilmiş. Aynı sayfaların tekrarlanan çekimleri birleştirildi. Bu yazının indirilebilir dosyası yok. Dönemin ödev soruları ayrıca [2010 ödevleri yazısında](/arsiv/eem311-odevler-2010/) bulunuyor.

## Ödev I: Üç transistörlü yükselteç

Devrede V_CC = 10 V, β = 100 ve V_BE(on) = 0,7 V verilmiş. İlk npn transistörün baz bölücüsü 730 kΩ ve 270 kΩ; emetör direnci 10 kΩ, buna paralel AC kolunda 100 µF ve 230 Ω var. İkinci transistör pnp; baz düğümünden 270 kΩ toprağa ve 100 µF baypas kondansatörü bağlanmış. İkinci katın emetör tarafındaki direnç 730 kΩ. Üçüncü transistör emetör izleyici; kolektör beslemeye, emetör 5 mA akım kaynağına bağlı. Çıkış 100 µF üzerinden 1 kΩ yüke gidiyor. İkinci katın kolektör direnci 10 kΩ.

### Birinci katın DC çözümü

Baz bölücüsünün eşdeğeri:

V_BB1 = (270/1000)·10 = 2,7 V

R_B1 = 270 kΩ ∥ 730 kΩ = 197,1 kΩ

2,7 = 0,7 + (β + 1)I_B1·10 kΩ + I_B1·197,1 kΩ

2 V = (1207,1 kΩ)I_B1

**I_B1 = 1,657 µA**, **I_C1 = 0,1657 mA**

### Çıkış katının DC çözümü

I_B3 + I_C3 = 5 mA

(β + 1)I_B3 = 5 mA

**I_B3 = 0,04950 mA**, **I_C3 = 4,9504 mA**

### İkinci katın düğüm denklemleri

B₂ düğümüne göre notta şu iki ilişki kurulmuş:

I_T + I_E2 = I_C1 + I₁

I₁ = I_B2 + I

Ara adımda I₁ ≈ 13,7 µA bulunuyor ve:

βI_B2 − I = 0,152 mA

0 = (730 kΩ)I_B2 − 0,7 + (270 kΩ)I

Birlikte çözümün yanına **I_B2 = 1,566 µA** ve **I = 0,0346 mA** yazılmış. Başka satırda I_C2 ≈ 0,1566 mA gösterilmiş.

Fotoğraftaki çalışma noktası listesi:

| Transistör | Listede yazılan Q(I_C, V_CE) |
| --- | --- |
| Q₁ | (0,1657 mA, 7,73 V) |
| Q₂ | (3,46 mA, 6,339 V) |
| Q₃ | (4,9504 mA, 2,321 V) |

*Not: Q₂ için sonuç listesindeki 3,46 mA, aynı sayfadaki I_B2 = 1,566 µA ve β = 100 ile uyuşmuyor; bu ikisi I_C2 = 0,1566 mA verir. Sonraki küçük işaret hesaplarında 3,46 mA kullanıldığı için tutarsızlık devam ediyor. Liste düzeltilmeden aktarıldı.*

### Küçük işaret parametreleri

V_A = 100 V kullanılarak r_o = (V_A + V_CE)/I_C, r_π = βV_T/I_C bağıntıları yazılmış. Taslağın kullandığı değerler:

| Parametre | Değer |
| --- | --- |
| r_o1 | yaklaşık 650 kΩ |
| r_o2 | yaklaşık 30,73 kΩ |
| r_o3 | yaklaşık 20,68 kΩ |
| r_π1 | 15,08 kΩ |
| r_π2 | 722,54 Ω |
| r_π3 | 505,0097 Ω |

Giriş direnci:

R_in = 730 kΩ ∥ 270 kΩ ∥ 15,08 kΩ = **14,0142 kΩ**

Toplam kazanç, üç katın oranları çarpılarak yazılmış:

A_v = (v_out1/v_in1)(v_out2/v_in2)(v_out3/v_in3)

Son sayısal satırda **A_v = −10,4923** sonucu var.

Çıkış direnci hesabında giriş sıfırlanmış ve çıkışa test gerilimi uygulanmış. Sayfanın sonunda **R_out = r_o3/2** yazıyor; aradaki cebir bazı yerlerde eksik.

*Not: Üçüncü katın fiziksel bağlantısı emetör izleyicidir; fotoğraftaki AC eşdeğer ise emetör topraklanmış gibi çizilmiş. Bu nedenle −10,4923 kazancı ve r_o3/2 çıkış direnci, özgün devre için doğrulanmış sonuçlar değildir. Giriş direnci paralel direnç hesabı yaklaşık 14,01 kΩ ile tutarlıdır.*

## İki fark katlı, dokuz transistörlü op-amp tasarımı

İkinci taslağın devresi üç bloğa ayrılmış: **birinci fark yükselteci**, **ikinci fark yükselteci**, **çıkış katı**. Birinci fark çifti Q₁–Q₂; akım kaynağı Q₃–Q₄. İkinci fark çifti Q₅–Q₆; akım kaynağı Q₇–Q₈. Q₉ emetör izleyici olarak çıkışı sürüyor. Girişler 1 ve 2, çıkış 3 numaralı terminaller olarak işaretlenmiş.

Besleme +5 V ve −5 V. Notta kolektör dirençleri R₁ = R₂ = 5 kΩ, R₄ = R₅ = 5 kΩ; çıkış katındaki R₆ = 10 kΩ yazıyor. Baz akımı hesabında R_B3 = 1 MΩ kullanılmış. Dirençlerin, devre ve kazanç hesabına göre seçildiği belirtiliyor.

### DC analiz

İlk akım kaynağı için 4,3 V/1 MΩ hesabıyla I_B3 = 4,3 µA bulunmuş. İkinci katın baz akımı, I_B5 = 0,36 mA/β = 3,6 µA olarak yazılmış. Bir sonraki satırda:

I_B7 = I_B4 − I_B5 = 5,26 µA − 3,6 µA = 1,66 µA

I_C7 = **0,166 mA**

I_C8 = 0,720 − 0,166 = **0,554 mA**

Sonuç listesinde şu Q noktaları yer alıyor:

| Transistörler | Kaynakta yazılan Q(I_C, V_CE) |
| --- | --- |
| Q₁, Q₂ | (0,298 mA, 4,05 V) |
| Q₃ | (0,43 mA, 0,7 V) |
| Q₄ | (0,596 mA, 5,7 V) |
| Q₅, Q₆ | (0,360 mA, 3,90 V) |
| Q₇ | (0,166 mA, 5 V) |
| Q₈ | (0,554 mA, 4,7 V) |
| Q₉ | (0,306 mA, 1,94 V) |

Q₉ için kullanılan adımlar:

I_E9 ≈ I_C9 = 0,306 mA

V_E9 = 0,306 mA·10 kΩ = 3,06 V

V_CE9 = 5 − 3,06 = **1,94 V**

### AC analiz

Küçük işaret emetör dirençleri r_e = 26 mV/I_E bağıntısıyla hesaplanmış. Sonraki katın giriş direnci, önceki katın yükü olarak hesaba katılıyor; sayfanın üzerinde **“bir sonraki katın giriş direncinin yarısı”** notu var.

Tek uçtan alınan fark katı çıkışında, yüklenmiş kolektör direnci R_C ∥ R_giriş,sonraki ile gösterilerek kullanılan kazanç biçimi:

A_v ≈ −(R_C ∥ R_giriş,sonraki)/(2r_e)

Çıkış izleyicisinde r_e9 ≈ 84,97 Ω yazılmış. Çıkış katı için R_L ∥ R₆ üzerinden kazanç hesabı, iki fark katı ve çıkış katı kazançlarının çarpımı, ayrıca **CMRR_dB = 20 log₁₀|A_d/A_cm|** hesabı bulunuyor. Toplam kazancın ve CMRR'nin sonuç rakamları fotoğraflarda yeterince net seçilemiyor; tahmin edilmedi.

*Not: Bu bölüm bir tasarım taslağıdır. Çalışma noktası listesi ve formüller okunabilen satırları korur; tüm düğüm gerilimleri ve akım yönleri net okunamadığından devrenin bütünü için bağımsız doğrulama yapılamadı.*
