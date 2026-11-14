---
baslik: EEM441 Haberleşme I: 2013 yaz okulu EEM 442 Haberleşme II Quiz I (24 Temmuz 2013) ve çözümleri
ozet: EEM 442 Haberleşme II yaz okulu Quiz I: PDM ve PPM kiplemeli darbe dizileri, PAM ve ikili PCM bant genişliği ve güç karşılaştırması; el yazısı çözümlerle.
---

Bu belge EEM 442 Haberleşme II dersine aittir; EEM 441 klasöründe bulunduğu için burada yayımlanmıştır. Başkent Üniversitesi EEM 442 Haberleşme II yaz okulu Quiz I (24 Temmuz 2013, süre 1 saat) sorularının ve el yazısı çözümlerinin metne aktarımı. Sınav kâğıdı ve çözümler fotoğraflanmış sayfalardan metne aktarıldı; fotoğraflar yayınlanmamıştır. Bu nedenle indirilebilir orijinal dosya yoktur. Kişisel bilgiler (öğrenci numarası, ad) çıkarılmıştır.

## Sorular

1. Bir sayısal iletişim sisteminde t = kT_s anlarında x(t) = cos(2πt/T_m) sinyali tekdüze olarak örneklenerek bir darbe kiplemeli dalga üretilmektedir; burada T_s = T_m/3'tür. Darbe kiplemeli sinyal x_p(t) değerini vererek a) μ = 0,8, τ₀ = 0,4 T_s değerlerine sahip PDM kiplemesi için, b) t_d = 0,5 T_s ve t₀ = τ = 0,2 T_s değerlerine sahip PPM kiplemesi için çizin.
2. Bir ses sinyali 300–3300 Hz frekans aralığında 8000 örnek/s ile örneklenmiştir. Bu örnekler doğrudan M-ary PAM olarak veya önce her örnek PCM'e çevrilip ikili PCM sinyalleri olarak gönderilebilmektedir. a) PAM sinyallerinin ISI olmaksızın ve α = 1 roll-off özelliğine sahip süzgeçle algılanması için gerekli minimum sistem bant genişliğini hesaplayın. b) Aynı roll-off özelliğine sahip, sekiz seviyeli olarak nicemlenmiş ikili PCM sinyallerinin algılanması için gerekli minimum bant genişliğini bulun. c) Her iki sistemde aynı BER'e sahip olmak için ikili PCM sisteminde ±1 seviyelerine genlik karşılık gelmektedir; PAM'deki 8 seviye 1, 3, 5, 7, 9, 11, 13, 15 değerlerinde, 000…111 ile eşlenmiştir. İletim bant genişliği ve çıkış gücü açısından iki sistemi karşılaştırın.

Sınavla birlikte verilen formül sayfasında: B_T = (1/2T_s)(1 + α) = (R_s/2)(1 + α); SNR₀ = 3×2^(2R)/α, α = tepe güç/ortalama güç; M-PAM sembol hata olasılığı P_E(M) = [2(M − 1)/M] Q(√(6 E_s,av /((M² − 1)N₀))); PAM x_p(t) = Σ A₀[1 + μ x(kT_s)] p(t − kT_s); PPM t_k = kT_s + t_d + t₀ x(kT_s); PDM τ_k = τ₀[1 + μ x(kT_s)]; M-ary PCM için L = M^R, SNR_th ≈ (6B_T/W)(M² − 1); Q fonksiyonu ve erfc bağıntıları ve PDM/PPM üretim şeması (testere dişi üreteci, karşılaştırıcı, monostable) yer alır.

## Çözüm 1

x(kT_s) = cos(2πk/3): k = 0 için 1, k = 1 için −0,5, k = 2 için −0,5, k = 3 için 1.

a) PDM: τ_k = τ₀[1 + μ x(kT_s)] = 0,4 T_s [1 + 0,8 cos(2πk/3)].
k = 0: 0,4 T_s (1 + 0,8) = 0,72 T_s; k = 1: 0,4 T_s (1 − 0,4) = 0,24 T_s; k = 2: 0,24 T_s; k = 3: 0,72 T_s.
Darbeler kT_s anlarında başlar, genlikleri sabit, genişlikleri 0,72 T_s, 0,24 T_s, 0,24 T_s, 0,72 T_s'dir (zaman ekseni T_s biriminde: 0–0,72; 1–1,24; 2–2,24; 3–3,72).

b) PPM: t_k = kT_s + t_d + t₀ x(kT_s) = T_s[k + 0,5 + 0,2 cos(2πk/3)] (t_d/T_s = 0,5, t₀/T_s = 0,2).
k = 0: 0,7 T_s; k = 1: 1,4 T_s; k = 2: 2,4 T_s; k = 3: 3,7 T_s. Her darbenin genişliği 0,2 T_s'dir (0,7–0,9; 1,4–1,6; 2,4–2,6; 3,7–3,9).

## Çözüm 2

T_s = 1/f_s = 1/8000 s = 125 µs.

a) PAM: Nyquist bant genişliği W = 1/(2T_s) = R_s/2 = f_s/2 = 4 kHz. Roll-off α = 1 için B = W(1 + α) = 8 kHz.

b) Sekiz seviyeli nicemlenmiş ikili PCM: her örnek log₂8 = 3 bit; sembol hızı R_s = 3 f_s = 24 kbit/s. B = (R_s/2)(1 + α) = R_s = 24 kHz.

c) İkili PCM: seviyeler ±1; ortalama enerji E_av = 3[(±1)² T_s/3] = T_s (üç bit, her bir T_s/3 sürelidir; T_s = T_b log₂M, burada log₂M = 3).
8-ary PAM: seviyeler 1, 3, 5, 7, 9, 11, 13, 15; E_av = (T_s/8)(1² + 3² + 5² + 7² + 9² + 11² + 13² + 15²) = (T_s/8)(1 + 9 + 25 + 49 + 81 + 121 + 169 + 225) = 85 T_s.
8-ary PAM'in ikili PCM'e göre ortalama enerji artışı 85 T_s / T_s = 85 (19,3 dB); bant genişliği azalması 8 kHz / 24 kHz = 1/3.

Alternatif olarak seviyeler 0…7 alınırsa: E_av = (T_s/8)(0² + 1² + … + 7²) = (T_s/8)(140) = 17,5 T_s; güç artışı 17,5 (12,43 dB).

*Not: El yazısı çözümde a) ve b) şıklarındaki parantez etiketleri (“binary PCM”, “M-ary PAM”) birbirine karışmıştır; sorunun metnine göre 8 kHz PAM'e, 24 kHz ikili PCM'e aittir. Aynı şekilde “4000 kHz” ifadesi 4 kHz olmalıdır.*
