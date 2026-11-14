---
baslik: EEM441 Haberleşme I: 2013 yaz okulu EEM 442 Haberleşme II final sınavı ve çözümleri
ozet: EEM 442 yaz okulu finali: raised-cosine süzgeçli QPSK sembol dizisi, PCM için M ve R seçimi ve alıcı gücü, delta modülasyonunda eğim aşımı, TDM-PCM bit hızı ve bant genişliği.
---

Bu belge EEM 442 Haberleşme II dersine aittir; EEM 441 klasöründe bulunduğu için burada yayımlanmıştır. Başkent Üniversitesi EEM 442 Haberleşme II yaz okulu final sınavı (kâğıtta tarih “…/8/2013”, süre 110 dakika; gün okunamadı) ve el yazısı çözümleri. Sınav kâğıdı ve çözümler fotoğraflanmış sayfalardan metne aktarıldı; fotoğraflar yayınlanmamıştır. Bu nedenle indirilebilir orijinal dosya yoktur. Kişisel bilgiler (öğrenci numarası, ad) çıkarılmıştır. Sınav kâğıtları yan çevrilmiş fotoğraflar olduğundan aktarım dikkatle yapılmıştır. Bir ders kitabına ait basılı çözüm sayfası içeriği yazıda yalnız sonucuyla özetlenmiştir.

## Sorular

1. Roll-off faktörü α = 0 olan raised-cosine tipi filtreye sahip bir haberleşme sisteminde 2 Mbps bit hızında çalışılmaktadır. Modülasyon M = 4 değerine sahip faz modüleli, veri dizisi {00, 01, 11, 10} ⇒ {1+j, −1+j, −1−j, 1−j} eşleme işlemi kullanılmaktadır. Raised cosine filtrenin girişine uygulanan s(0), s(T_s), s(2T_s), s(3T_s) sembol dizisi = [1+j, −1−j, −1+j, −1+j] verilmiştir. a) Dürtü tepke (impulse response) fonksiyonunu yazın. b) Sembol başına ortalama enerjiyi hesaplayın. c) Bit süresini, sembol hızını ve sembol süresini hesaplayın. d) a) şıkkında bulunan dürtü tepke fonksiyonunu kullanarak, örnekleyicinin senkronize örnekleme yaptığını varsayarak, örnekleme anlarında (t = 0, T_s, 2T_s, 3T_s, 4T_s, …) çıkış sıklığını bulun ve grafiğini çizin.
2. W = 15 kHz bant genişliğine sahip bir sinyal gürültü gücü yoğunluğu N₀ = 0,01 µW/Hz olan bir kanal üzerinden ve iletim bant genişliği B_T = 40 kHz olan M-ary PCM sinyali olarak iletilmektedir. a) SNR₀ ≥ 40 dB için en küçük M ve R değerini hesaplayın. b) PCM sinyalinin iletim bant genişliğinin tamamını kullandığını, P_e < 10⁻⁵ ve P_tepe/P = 2 olduğunu varsayarak sinyal gürültü oranının eşik değeri üzerinden çalışabilmek için alıcı gücünün minimum değeri ne olmalıdır?
3. T_s örnekleme periyoduna ve Δ basamak büyüklüğüne sahip x(t) = a·t basamak sinyali bir delta modülatörüne (DM) uygulanmıştır. a) Slope-overload bozulmasının meydana gelme koşullarını belirleyin. b) Basamak büyüklüğünün Δ = 0,75 a T_s, Δ = a T_s ve Δ = 1,25 a T_s üç değeri için DM modülatörünün çıkış grafiğini sıfırdan başlayarak çizin.
4. Bir sayısal iletişim sistemi her biri 4 kHz bant genişliğine sahip 8 sinyali zaman bölmeli olarak çoklanmış sekiz mesaj sinyalini ikili tekdüze nicemlenmiş PCM sistemi ile göndermektedir. Örnekleme hızı Nyquist hızının en az yüzde 50 fazlası olmalıdır; örnekleme hatası, tepe genliğinin yüzde 1'inden fazla olmamalıdır. a) Örnekleme hızını hesaplayın. b) Nicemleme seviyesinin sayısını ve örnek başına bit sayısını hesaplayın. c) Çoklanmış mesaj sinyali için toplam bit hızını hesaplayın. d) Sayısal iletişim sisteminin iletim bant genişliğini hesaplayın.

Sınav kâğıdında ayrıca bir “Useful formulas” sayfası vardır: gözlem vektörü r(T) = ±A + n(T) için P_b = p₁Q((A − λ)/σ) + (1 − p₁)Q((A + λ)/σ); Q(3,09023) = 10⁻³, Q(√20) = 3,87×10⁻⁶; B_T = (R_s/2)(1 + α); SNR₀ = 3×2^(2R)/α, α = tepe güç/ortalama güç; ikili ilişkili sinyalleşmede P_b = Q(√(E_s(1 − ρ)/N₀)); M-PSK için P_s = 2Q(√(2E_s/N₀) sin(π/M)); sinc(2Wt) ⇔ (1/2W)Π(f/2W); (1/(M/2))Σ(2i − 1)² = (M² − 1)/3; M-PAM için P_E(M) = [2(M − 1)/M] Q(√(6E_s,av/((M² − 1)N₀))).

## Çözüm 1: Raised-cosine, α = 0

Sembol dizisi {00, 01, 11, 10} ⇒ {1+j, −1+j, −1−j, 1−j}; kâğıttaki çözümde s(0), s(T_s), s(2T_s), s(3T_s) = {1+j, −1+j, −1−j, 1−j} sırasıyla alınmıştır (α = 0 için W = 1/(2T_s)).

a) p(t) = sinc(2Wt) = sinc(t/T_s) (α = 0).
b) Sembol başına ortalama enerji E_s = |1 ± j|² = 2.
c) Bit hızı R_b = 2 Mbps ⇒ bit süresi T_b = 0,5 µs; sembol hızı R_s = R_b/2 = 1 Msembol/s ⇒ sembol süresi T_s = 1/R_s = 1 µs.
d) Örnekleme anı = sembol süresi: T_s = 1 µs. Çıkış, her sembol için kaydırılmış sinc darbelerinin toplamıdır; tam t = kT_s anlarında yalnız ilgili sembolün darbesi sıfırdan farklı olduğundan (ISI yok) çıkış, 00 → 1+j, 01 → −1+j, 11 → −1−j, 10 → 1−j değerlerini sırasıyla 0, T_s, 2T_s, 3T_s anlarında alır.

## Çözüm 2: PCM için M, R ve alıcı gücü

SNR₀ = 3L²/α, α = 2 ⇒ (3/2) L² > 10⁴ ⇒ L² = (2/3)10⁴ ⇒ L > 81,6.

Kâğıtta sembol hızı R_s = f_s R/log₂M = 2WR/log₂M ve B ≥ 1/(2T_s) = R_s/2 yazılır; buradan B ≈ W R elde edilir. B_T = 40 kHz ile R < B_T/W = 40 kHz/15 kHz ⇒ R = 2 (kâğıtta 2,5 olarak yazılmış). L = M^R > 81,6 ⇒ M² > 81,6 ⇒ M = 10 ve L = M² = 100.

Eşik SNR: SNR_th = (6B/W)(M² − 1) = (6×40 kHz/15 kHz)(100 − 1) = 16 × 99 ≈ 1600.
Alıcı gücü: P_r = N₀ W SNR_th = 10⁻⁸ × 15×10³ × 1,6×10³ = 0,24 W = 240 mW.

*Not: Kâğıtta “R < B/W = 2,5” yazılmıştır; 40/15 = 2,67'dir. Sonuç (R = 2) değişmez.*

## Çözüm 3: Delta modülasyonu ve eğim aşımı

a) Bir T_s periyodunda giriş sinyali aT_s kadar artar; delta modülatörün çıkışı ise en çok Δ kadar değişir. Eğim aşımı (slope-overload) bozulması, Δ < aT_s olduğunda, yani Δ/T_s < a olduğunda oluşur.

b) Δ = 0,75 aT_s: çıkış, girişten sürekli geri kalır (eğim aşımı); Δ = aT_s: çıkış girişi basamak basamak izler (sınır durum); Δ = 1,25 aT_s: çıkış girişi izler ve basamaklar arası küçük salınım gösterir, eğim aşımı olmaz (granüler gürültü).

*Not: Bu şıkka ait fotoğraf, ders kitabı çözüm kılavuzundan basılı bir sayfadır; bu nedenle yalnız sonucu özetlenmiş, basılı çizimler aktarılmamıştır. Kâğıttaki basılı ifade bir yerde “Δ ≳ aT_s” gibi okunuyor; doğru koşul eğim aşımı için Δ < aT_s'dir.*

## Çözüm 4: 8 sinyalli TDM-PCM

W = 4 kHz.

a) f_s = 1,5 × 2 × W = 1,5 × 2 × 4 kHz = 12000 örnek/s.
b) Örnekleme (nicemleme) hatası: Δ/2 = m_tepe/L ≤ 0,01 m_tepe ⇒ L ≥ 100; L = 2^R ≥ 100 ⇒ R = 7 bit/örnek, L = 128.
c) Her örnek R = 7 bitle kodlanır. Sinyal başına bit hızı R_b = R f_s = 7 × 12000 = 84000 bps; 8 sinyal çoklandığında toplam R_B = 8 × 84000 = 672000 bps = 672 kbps.
d) Gerekli en küçük iletim bant genişliği B_T = 1/(2T_b) = R_b/2 = 336 kHz.
