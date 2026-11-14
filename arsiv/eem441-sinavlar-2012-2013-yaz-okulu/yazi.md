---
baslik: EEM441 Haberleşme I: 2012 ve 2013 yaz okulu sınavları (soru ve çözümler)
ozet: EEM441 Haberleşme Sistemleri I dersinin Ağustos 2012 ara sınavı, finali ve quizi ile Ağustos 2013 finali: fazör şeması, FM bant sınırlama, FDM süzgeç tasarımı, AM spektrumu ve güç.
---

Başkent Üniversitesi EEM 441 Haberleşme Sistemleri I dersinin 2012 ve 2013 yaz okulu sınavları: 7 Ağustos 2012 finali, 10 Ağustos 2012 ara sınavı, 13 Ağustos 2012 Quiz 2 ve 14 Ağustos 2013 finali. Kaynaklar sınav kâğıtlarının ve el yazısı çözümlerin telefon fotoğraflarıdır; fotoğraflanmış sayfalardan metne aktarıldı, fotoğraflar yayınlanmadı. Çözümler bir arkadaşın el yazısı notlarındandır; kişisel bilgi (ad, numara) çıkarıldı.

## Ara sınav, 10 Ağustos 2012 (süre 90 dak)

**Soru 1.** Genlik modüleli v(t) = v₁(t)cos(ω_ct) + v₂(t)cos(ω_ct + α) sinyali için fazör şemasını çizin. Fazör şeması yardımıyla v_I(t) ve v_Q(t) bileşenlerini, A(t) zarfını ve φ(t) faz açısını hesaplayın. |v₂(t)| ≪ |v₁(t)| için hesapları tekrarlayın.

*Çözüm.* v_I = v₁ + v₂cos α, v_Q = v₂sin α; A(t) = √(v₁² + 2v₁v₂cos α + v₂²) ≈ v₁ + v₂cos α; φ(t) = arctan[v₂sin α/(v₁ + v₂cos α)] ≈ v₂sin α/v₁.

**Soru 2.** Bant genişliği 4 kHz olan ses sinyaliyle modüle edilmiş, modülasyon indeksi β = 2 olan FM sinyali, merkez frekansı f_c ve bant genişliği 8500 Hz olan BPF'ye uygulanıyor. FM sinyalinin frekans spektrumunu ve fazör şemasını çizin; çıkış sinyalinin zarfını hesaplayıp çizin.

*Çözüm.* f_m = 4 kHz; J₀(2) ≈ 0,22, J₁(2) ≈ 0,58. BPF yalnız taşıyıcıyı ve birinci yan bantları (f_c ± 4 kHz) geçirir: spektrumda f_c'de 0,22A_c, f_c + 4 kHz'de +0,58A_c, f_c − 4 kHz'de −0,58A_c çizgileri bulunur (ikinci yan bantlar 8 kHz'dedir, bant dışındadır). Fazör şemasında taşıyıcı fazörüne zıt yönlerde dönen iki 0,58A_c fazörü eklenir; bileşke dikey bileşen 2 × 0,58 = 1,16A_c olur. Zarf A_min = 0,22A_c, A_max = √(0,22² + 1,16²)A_c ≈ 1,18A_c'dir; A(t) f_m'in iki katı hızda (periyot 1/2f_m) dalgalanır.

**Soru 3.** FM sinyali bir frekans çarpıcının girişine uygulanıyor; çarpıcı içindeki BPF'nin merkezi 2f_c'ye ayarlı. BPF'nin giriş ve çıkışındaki spektrumu çizin; başarılı çalışma için Δf üzerindeki koşulu f_c ve W cinsinden yazın.

*Çözüm.* β = k_fA_m/f_m = Δf/f_m; n katı çarpılmış sinyalin bant genişliği B_n ≈ 2(nβ + 1)W. Spektrumlar f_c, 2f_c, 3f_c çevresinde B₁, B₂, B₃ genişliklerindedir. Üst üste binmeme için f_c + B₁/2 < 2f_c − B₂/2 ve 2f_c + B₂/2 < 3f_c − B₃/2; buradan f_c > (B₂ + B₃)/2 = 5Δf + 2W ve **Δf < (f_c − 2W)/5**.

**Soru 4.** Genlik modüleli sinyalin zarfının genliği 5–15 V arasında değişiyor; bilgi sinyalinin frekansı 1 kHz, taşıyıcı frekansı 100 kHz. a) Zaman alanı ifadesi, b) çift taraflı frekans spektrumu, c) taşıyıcı, alt yan bant ve üst yan bandın 100 Ω'luk dirençteki güç tüketimi, d) bant genişliği, e) yan bant gücünü artırmak için ne yapılmalı?

*Çözüm.* A_c = (15 + 5)/2 = 10 V; μ = (15 − 5)/(15 + 5) = 0,5. s(t) = 10[1 + 0,5cos(2π·10³t)]cos(2π·100·10³t) = 10cos(2π·100k·t) + 2,5cos(2π·99k·t) + 2,5cos(2π·101k·t). B = 2f_m = 2 kHz. R = 100 Ω'ta P_c = (10²/2)/100 = 0,5 W, her yan bant için (2,5²/2)/100 ≈ 31 mW. Yan bant gücünü artırmak için bindirim göstergesi (μ) artırılmalıdır.

*Not: El yazısı çözümde yan bant genlikleri 1 V (spektrum 5, ½, ½ biçiminde) ve yan bant gücü 5 mW olarak verilmiş; s(t) = A_c[1 + μ cos ω_mt]cos ω_ct açılımında yan bant genliği μA_c/2 = 2,5 V olduğundan yukarıdaki değerler düzeltilmiş hâliyle verilmiştir.*

## Quiz 2, 13 Ağustos 2012 (süre 1 saat)

**Soru 1.** Bir radyo verici istasyonunda f_m = 20 kHz, β = 1,0, A_c = 100 ve f_c = 30 kHz verilmiştir. Frekans modüleli s(t) sinyali için uygun formülü türetin, frekans spektrumunu çizin ve S_T < A_c²/2 olduğunu gösterin; sistemin bant genişliğini hesaplayın.

*Çözüm özeti.* f_i(t) = f_c + βf_m cos(2πf_mt) = 30 + 20cos(40πt) kHz. Bessel katsayıları J₀(1) = 0,77, J₁(1) = 0,44, J₂(1) = 0,11, J₃(1) = 0,02: çizgiler 77, 44, 11, 2 genliklidir (f_c = 30 kHz'de 77, 50 ve 10 kHz'de ±44, 70 ve −10 kHz'de ±11, 90 ve −30 kHz'de ±2); negatif frekansa düşen çizgiler katlanır. Bant genişliği el yazısında 80 kHz (Carson ≈ 2(β + 1)f_m = 80 kHz) ve 120 kHz olarak işaretlenmiştir.

*Not: El yazısındaki toplam güç hesabı 4390 sonucunu verip A_c²/2 = 5000 ile karşılaştırır; katlanan çizgiler (−33, 75, 11, 2) toplamında sayısal bir tutarsızlık vardır, bu nedenle sayı ayrıca doğrulanmalıdır.*

## Final, 7 Ağustos 2012 (süre 110 dak)

1. Giriş sinyali ton modüleli SSB olan devrede yerel osilatör φ' faz hatasına sahiptir (zarf algılayıcı, sinyalle toplanan A_LO cos(ω_ct ± φ')). Fazör şemasıyla sinyal zarfı denklemini türetin; A_LO ≫ A_cA_m için A(t) ≈ A_LO + ½A_cA_m cos(ω_mt ± φ') olduğunu gösterin.
2. m(t) = cos(ω_mt) − (1/3)cos(3ω_mt) için SSB formülünü türetin. Kare dalga yaklaşımını kullanarak SSB sinyalinin A(t) zarfını hesaplayın; A_c = 2 için A(t)'yi ve m(t)'yi çizerek karşılaştırın.
3. 300 < |f| < 3300 Hz dışındaki bileşenleri ihmal edilen 12 ses sinyali, kanallar arasında B_gb koruma bandı bırakılarak SSB alt taşıyıcı modülasyonu ile çoklanıyor. Alıcıda her alt taşıyıcı için merkez frekansı f₀'a ayarlı BPF'lerin aktarım işlevi |H(f)| = exp{−[1,2(f − f₀)/W]²}; |H(f)| ≤ 0,1 komşu kanal yanıtını sağlayan B_gb değerini ve FDM sisteminin iletim bant genişliğini bulun.
4. A_c = 1 ve β = 1 ton modüleli FM sinyali için ω_mt = 0, π/4, π/2 anlarındaki fazör şemalarını çizin; her biri için zarf A(t) ve faz φ(t) değerlerini hesaplayın.

*Bu sınavın fotoğraflarında yalnız soru kâğıdı vardır.*

## Final, 14 Ağustos 2013 (süre 110 dak)

**Soru 1.** Bir telefon santralinda ses kanalları alıcıda aktarım işlevi |H(f)| = 1/√(1 + [2(f − f₀)/B]^(2n)) olan bant geçiren süzgeçlerle birbirinden ayrılmıştır. Taban bant ses sinyalinin 300 < |f| < 3300 Hz dışındaki bileşenleri ihmal edilerek grup spektrumundaki üç komşu kanalın spektrumunu çizin; istenen geçirgenlik bandı dışında |H(f)| ≤ 0,1 olması için B, f₀ ve n'yi bulun.

*Çözüm.* Alt taşıyıcılar 4 kHz aralıklıdır; her kanal 3 kHz genişlikte ve komşular arası 300 Hz'lik üst yan bant payıyla yerleşir. B = 3 kHz, f₀ = f_i − 0,3 kHz − B/2 = f_i − 1,8 kHz alınır; komşu kanalın en yakın bileşeni geçiş bandının kenarından B/2 + 1 kHz = 2,5 kHz uzaktadır. |H|² ≤ 0,01 için 1 + (2 × 2,5/3)^(2n) ≥ 100 ⇒ (5/3)^(2n) ≥ 99 ⇒ 2n·log(5/3) ≥ log 99 ⇒ n ≥ 4,5, yani **n = 5**.

**Soru 2.** Modülasyon indeksi β = 2 ve bilgi sinyalinin en yüksek bileşeni f_m = 200 Hz olan ton modüleli FM sinyali, merkez frekansı f_c ve bant genişliği 750 Hz olan BPF'ye uygulanıyor. FM spektrumunu ve fazör şemasını çizin; çıkış sinyalinin zarfını hesaplayın ve çizin.

*Çözüm.* 2012 ara sınavındaki 2. sorunun aynı yapısıdır: yalnız taşıyıcı (0,22A_c) ve f_c ± 200 Hz yan bantları (±0,58A_c) süzgeçten geçer; A_min = 0,22A_c, A_max ≈ 1,18A_c.

**Soru 3.** Birim genlikli görüntü sinyalleri DSB-SC modülasyonu ile iletiliyor. Ton modüleli DSB-SC sinyali için fazör şemasını çizin. Alt yan bandın genişliği yarıya düşürülürse DSB-SC modüleli sinyalin A(t) zarfını ve φ(t) faz açısını fazör şemasıyla hesaplayın.

*Çözüm.* Ton için x_c(t) = A_c cos ω_ct·cos ω_mt = (A_c/2)cos(ω_c − ω_m)t + (A_c/2)cos(ω_c + ω_m)t. Alt yan band yarıya inince (A_c/4): v_I = (A_c/2)cos ω_mt + (A_c/4)cos ω_mt = (3/4)A_c cos ω_mt, v_Q = (A_c/2)sin ω_mt − (A_c/4)sin ω_mt = (A_c/4)sin ω_mt. A(t) = (A_c/4)√(9cos²ω_mt + sin²ω_mt) = (A_c/4)√(5 + 4cos 2ω_mt); φ(t) = arctan[(tan ω_mt)/3].

**Soru 4.** a) f_m ≪ f_c, m(t) = cos(2πf_mt)u(t) ile genlik modülasyonu: DSB ve μ < 1 ile μ > 1 değerli AM için zarfları çizin; genlik değerlerini belirtin. b) Aynı soruyu T ≫ 1/f_c olmak üzere m(t) = 0,5u(t) − 1,5u(t − T) için tekrarlayın.

*Çözüm sayfasında zarf çizimleri (μ = 1 civarı AM ve DSB) vardır; metne dökülebilen sayısal ifade yoktur.*
