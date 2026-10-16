---
baslik: EEM214 Elektronik I: Kaynak ve Yük Direncinin Etkisi, Kaskat ve Kaskod Bağlantı (Tahta Notları, 2014)
ozet: EEM214 Elektronik I dersinin 16 Mayıs 2014 tarihli dersinde tahtaya yazılanlar: sistem yaklaşımıyla iki kapılı yükselteç modeli, R_s ve R_L'nin gerilim ve akım kazancına etkisi, sayısal örnek, emetör izleyici + ortak bazlı kaskat yükselteç örneği, iki katlı ortak emetörlü yükselteç sorusu ve kaskod bağlantının kazancı.
---

Bu yazı, EEM214 Elektronik I dersinin **16 Mayıs 2014** tarihli dersinde tahtaya yazılanları aktarıyor. Konu, yükselteçlerin **sistem yaklaşımıyla** (iki kapılı devre olarak) modellenmesi, kaynak direnci R_s ile yük direnci R_L'nin kazanca etkisi ve çok katlı (kaskat, kaskod) yükselteçler. Metin, tahtanın telefonla çekilmiş fotoğraflarından metne aktarıldı; fotoğraflarda kişiler de bulunduğu için yayınlanmadı. Devre şemaları sözle tarif edildi. Aynı dönemin quiz ve final soruları [2014 Quiz 2 ve final cevap anahtarı](/arsiv/eem214-quiz-2-final-2014/) yazısında.

## R_s (kaynak direnci) ve R_L (yük direnci) etkisi

Sistem yaklaşımına göre bir yükselteç iki kapılı bir blok olarak şöyle eşdeğerlenir: girişte R_i giriş direnci, çıkışta A_vNL·v_i bağımlı gerilim kaynağı ve ona seri R_o çıkış direnci. Kaynak v_s, R_s üzerinden girişe; yük R_L çıkışa bağlanır. Yüksüz (no load) kazanç:

v_o = A_vNL·v_i ⇒ v_o/v_i = A_vNL

**R_s'nin etkisi:** Giriş gerilimi bir gerilim bölücüyle bulunur:

v_i = v_s·R_i/(R_i + R_s) ⇒ v_i/v_s = R_i/(R_i + R_s)

A_vs (yüksüz) = v_o/v_s = (v_o/v_i)·(v_i/v_s) = **A_vNL·R_i/(R_i + R_s)**

Buradaki R_i/(R_i + R_s) çarpanı R_s'nin etkisidir. Giriş akımı R_s yoksa I_i = V_i/R_i; R_s varsa I_s = V_s/(R_s + R_i).

**R_L'nin etkisi:** R_L varsa

V_oL = (A_vNL·V_i)·R_L/(R_o + R_L) ⇒ V_oL/V_i = A_vL = A_v(yüklü) = **A_vNL·R_L/(R_o + R_L)**

Buradaki R_L/(R_o + R_L) çarpanı R_L'nin etkisidir.

**Hem R_s hem R_L varsa:**

A_vs(yüklü) = V_oL/V_s = (V_oL/V_i)·(V_i/V_s) = **A_vNL·[R_L/(R_o + R_L)]·[R_i/(R_s + R_i)]**

**Akım kazançları:**

- Yüklü akım kazancı: **A_iL = −A_vL·R_i/R_L**
- Hem yük hem R_s varsa: **A_is = −A_vs·(R_s + R_i)/R_L**

## Örnek: R_s ve R_L'nin etkisi

Yükselteç: A_vNL = −480, Z_i = 4 kΩ, Z_o = 2 kΩ; R_s = 0.2 kΩ. Sorular: R_L = 1.2 kΩ iken A_vL ve A_vs(yüklü) nedir? R_L = 5.6 kΩ iken A_vL ve A_i = I_o/I_i = I_o/I_s nedir?

- R_L = 1.2 kΩ: A_vL = A_vNL·R_L/(Z_o + R_L) = −480·1.2k/(2k + 1.2k) = **−180**
- A_vs(yüklü) = A_vL·Z_i/(Z_i + R_s) = −180·4k/(4k + 0.2k) = **−171.36**
- R_L = 5.6 kΩ: A_vL = A_vNL·5.6k/(5.6k + 2k) = **−353.76**
- A_iL = −A_vL·Z_i/R_L = −(−353.76)·4k/5.6k = **252.6…** (fotoğrafta son haneler kesik)

*Not: Tahtada A_vs(yüklü) = −171.36 yazılmış; −180·4/4.2 hesabı −171.43 verir.*

## Örnek: Kaskat bağlı iki katlı yükselteç

R_s = 1 kΩ'luk kaynak, birinci kat **emetör izleyici** (Z_i = 10 kΩ, Z_o = 12 Ω, A_vNL ≅ 1), ikinci kat **ortak bazlı** (Z_i = 26 Ω, Z_o = 5.1 kΩ, A_vNL = 240), yük R_L = 8.2 kΩ. Z_i = Z_i1, Z_o2 = Z_o. Sorular:

- a) Her katın yüklü kazancı?
- b) Devrenin toplam kazancı A_vL ve A_vsL?
- c) Devrenin toplam akım kazancı (yüklü) A_iL?
- d) 1. kat çıkarılırsa kalan devrenin toplam kazancı A_vsL?

Eşdeğer devre: v_s – 1 kΩ – 10 kΩ (1. kat girişi); A_vNL1·v_i1 kaynağı – 12 Ω – 26 Ω (2. katın girişi 1. katın yükü); A_vNL2·v_i2 kaynağı – 5.1 kΩ – R_L = 8.2 kΩ.

- a) A_v1L = A_vNL1·26 Ω/(26 Ω + 12 Ω) = **0.684**; A_v2L = A_vNL2·8.2k/(5.1k + 8.2k) = **147.97**
- b) A_vL = v_o/v_i1 = A_v1L·A_v2L = 0.684·147.97 = **101.2**; A_vsL = v_o/v_s = A_vL·10k/(1k + 10k) = **92**
- c) A_iL = −A_vL·Z_i/R_L = −101.2·… (fotoğrafta sonucun yazılmadığı anda çekilmiş)
- d) Birinci kat çıkarılınca kaynak (1 kΩ) doğrudan 26 Ω'luk girişe bağlanır: A_vL = A_vNL2·8.2k/(8.2k + 5.1k) = 147.97; A_vs = A_vL·26 Ω/(26 Ω + 1 kΩ) = 147.97·26/1026 = **3.7**

Sonuç: Düşük giriş dirençli ortak bazlı katın önüne yüksek giriş dirençli emetör izleyici konunca toplam kazanç 3.7'den 92'ye çıkıyor.

## Soru: İki katlı ortak emetörlü yükselteç

Devre: iki özdeş ortak emetörlü kat, V_CC = 20 V; her katta R1 = 15 kΩ, R2 = 4.7 kΩ gerilim bölücü, R_C = 2.2 kΩ, R_E = 1 kΩ (C_E = ∞ ile köprülü); katlar ve giriş–çıkış C = ∞ kondansatörlerle bağlı; β₁ = β₂ = 200, r_o = ∞; giriş v_i = 25 µV.

- a) Devrenin DC analizini yaparak küçük sinyal parametrelerini (r_e, r_π, g_m …) bulunuz.
- b) Devrenin toplam kazancını bulunuz. V_o'yu bulunuz.
- c) Devreye R_L = 4.7 kΩ yük bağlanırsa toplam kazancı bulunuz. V_o'yu bulunuz.
- d) Kaynağın iç direnci R_s = 1 kΩ ise A_vsL'yi bulunuz.

Tahtaya çizilen AC eşdeğer devre: girişte 15k ∥ 4.7k ∥ βr_e; birinci katın çıkışında β·I_b1 akım kaynağına paralel 2.2k ∥ 15k ∥ 4.7k ∥ βr_e2, yani **R_L1 = R_i2** (birinci katın yükü ikinci katın giriş direncidir); ikinci katta β·I_b2 akım kaynağı ve 2.2 kΩ. Sayısal çözüm fotoğraflarda yok.

## Kaskod (cascode) bağlantı

Devre: birinci transistör (npn) ortak emetörlü (R_B1, R_B2 bölücü, R_C, R_E ve C_E), kolektörü ikinci transistörün (tahtada pnp yazılı) emetörüne bağlı; ikinci transistör ortak bazlı (bazı R_B ve C_B ile AC toprakta), çıkış kolektörden R_L üzerinden alınıyor. V_o1 = V_i2.

Küçük sinyal eşdeğeri: girişte R_B1 ∥ R_B2 ve β₁r_e1; birinci katın çıkışında β₁I_b1 akım kaynağı, R_C ve ikinci katın giriş direnci r_e2 (**R_i2 = R_L1**); ikinci katta α·I_e akım kaynağı ve R_L.

- A_v1L = −β₁I_b1·(R_C ∥ r_e2) / (I_b1·β₁r_e1) = **−(R_C ∥ r_e2)/r_e1**
- A_v2L = α·I_e·R_L / (I_e·r_e2) = **α·R_L/r_e2**
- A_vTL = **−[(R_C ∥ r_e2)/r_e1]·α·R_L/r_e2**

R_C ∥ r_e2 ≈ r_e2 olduğundan birinci katın kazancı yaklaşık −1'dir; kazancın neredeyse tamamını ortak bazlı ikinci kat sağlar.
