---
baslik: EEM441 Haberleşme I: Açı modülasyonu ve FM ders slaytları (FM-1 … FM-29)
ozet: Faz ve frekans modülasyonu, dar ve geniş bantlı FM, Carson kuralı, Bessel fonksiyonları, FM üretimi, demodülasyonu ve PLL konularını içeren taranmış ders slaytları.
---

EEM441 Haberleşme I dersinin FM-1'den FM-29'a numaralı İngilizce slayt çıktılarının taramaları; 31 sayfa. Slaytların hazırlayanı sayfalarda yazmıyor. Taranmış sayfaların tamamı yazının sonundaki PDF'tedir; içerik aşağıda sayfa sırasıyla özetlenmiştir.

## Açı modülasyonu ve temel tanımlar (FM-1 … FM-4)

Açı modülasyonunda taşıyıcının açısı mesaja göre değiştirilir, genlik sabit kalır. Açı modülasyonlu dalga s(t) = Ac cos[θi(t)]; anlık frekans fi(t) = (1/2π) dθi/dt. Modülasyonsuz taşıyıcı için θi = 2π fc t + φc ve fi = fc.

- Faz modülasyonu (PM): θi(t) = 2π fc t + kp m(t); fi(t) = fc + (kp/2π) dm/dt.
- Frekans modülasyonu (FM): fi(t) = fc + kf m(t); θi(t) = 2π fc t + 2π kf ∫ m(τ)dτ.

PM'de faz, FM'de frekans mesajla orantılıdır. Entegratör ve türev alıcı devrelerle faz modülatörü FM üretebilir ve tersi: m(t) → entegratör → faz modülatörü → FM; m(t) → türev alıcı → frekans modülatörü → PM.

**Örnek (anlık frekans).** s(t) = 10 cos[2π·1000 t + 2π sin(10π t)] sinyalinin anlık frekansı fi(t) = 1000 + 10 cos(10π t) olarak bulunur ve tepe frekans sapması çizilir; ikinci örnekte fazı t'nin ikinci dereceden fonksiyonu olan bir sinyal için anlık frekansın doğrusal arttığı gösterilir.

AM ile açı modülasyonunun karşılaştırması: açı modülasyonunda zarf sabittir (AM'de mesaja doğrusal bağlıdır); ortalama iletim gücü Ac²/2'dir; sıfır geçişleri sabit hızda değildir ve mesaj bilgisi taşır; modüleli dalga mesaj dalga biçimine benzemez.

Tek tonlu FM: m(t) = Am cos(2π fm t), fi(t) = fc + kf Am cos(2π fm t), Δf = kf Am (maksimum frekans sapması), modülasyon indeksi β = Δf/fm; FM sinyali s(t) = Ac cos[2π fc t + β sin(2π fm t)]; dar bant FM β ≪ 1 radyan, geniş bant β ≫ 1.

## Dar bantlı FM (FM-5, FM-6)

s(t) = Ac cos(2π fc t + β sin 2π fm t) = Ac cos φ cos(ωc t) − Ac sin φ sin(ωc t), φ(t) = β sin(2π fm t). φ(t) ≪ 1 radyan (≈ 57°) iken cos φ ≈ 1 ve sin φ ≈ φ: s(t) ≈ Ac cos(ωc t) − Ac β sin(2π fm t) sin(ωc t) = Ac cos(ωc t) + (Ac β/2)[cos(ωc + ωm)t − cos(ωc − ωm)t].

Tonla modüleli AM: s(t) = Ac cos(ωc t) + (μAc/2)[cos(ωc + ωm)t + cos(ωc − ωm)t]. Tek fark alt yan bandın işaretidir; bu yüzden tonla modüleli AM ve dar bantlı FM benzer özellikte ve aynı iletim bant genişliğindedir. Fazör karşılaştırmasında AM'de yan bantlar taşıyıcıyla aynı doğrultuda genlik değiştirir, dar bantlı FM'de yan bantlar taşıyıcıya dik olup fazı değiştirir.

Dar bantlı FM üretimi: φ(t) = 2π Δf ∫ m(t)dt entegratör, sin ve cos kolları, ürün modülatörü ve toplayıcıdan oluşan blok diyagramla elde edilir.

## Geniş bantlı FM ve Bessel fonksiyonları (FM-7 … FM-13)

Tek tonlu FM'nin kompleks zarfı s̃(t) = Ac e^{jβ sin(2π fm t)} periyodiktir ve Fourier serisine açılır: katsayılar cn = Ac Jn(β), burada Jn(β) = (1/2π) ∫ exp[j(β sin x − n x)] dx birinci tür n. dereceden Bessel fonksiyonudur. Böylece

s(t) = Ac Σ Jn(β) cos[2π(fc + n fm)t], S(f) = (Ac/2) Σ Jn(β)[δ(f − fc − n fm) + δ(f + fc + n fm)].

Bessel fonksiyonlarının özellikleri: Jn(β) = (−1)ⁿ J−n(β); β → 0 için J0 → 1, J1 ≈ β/2, J2 ≈ β²/8; β → ∞'da sönümlü sinüs gibi davranır; ΣJn²(β) = 1.

Spektrumun gözlemleri: taşıyıcı ve fc ± n fm'de sonsuz sayıda çizgi içerir. Taşıyıcı genliği J0(β) modülasyon indeksine bağlıdır; AM'den farklı olarak taşıyıcı genliği sabit değildir ve mesaj bilgisinin bir parçasını taşır. Toplam güç Ac²/2'dir.

**Örnek (tonlu FM çizgi spektrumu).** Ac = 100, fm = 4 kHz, Δf = 8 kHz, β = 2. J0..J5 = 0,22; 0,58; 0,35; 0,13; 0,03; < 0,01. fc = 30 kHz için yan bantlar |fc ± n fm| = |30 ± 4n| kHz'de; BT = 2 nmax fm = 2·4·4 = 32 kHz. fc = 11 kHz için yan bantların bir kısmı negatif frekanslara katlanır (folded terms) ve BT = 26 kHz olur. fm ve Am'in spektruma etkisi (Δf sabit, fm değişken; fm sabit, Am değişken) normalize FM spektrumlarıyla gösterilir.

## FM iletim bant genişliği (FM-10, FM-11)

FM sinyali sonsuz yan bant içerir; pratikte bant genişliği belirli sayıda anlamlı yan bantla sınırlıdır. Etkili bant genişliği (Carson kuralı): BT ≈ 2Δf + 2fm = 2Δf(1 + 1/β) = 2fm(1 + β). Daha doğru tanım: taşıyıcıya göre genliği %1'den büyük olan yan bantların en uzağına kadar olan bant genişliğidir; BT = 2 nmax fm, nmax = |Jn(β)| > 0,01 koşulunu sağlayan en büyük tam sayı.

| β | 0,1 | 0,3 | 0,5 | 1 | 2 | 5 | 10 | 20 | 30 |
|---|---|---|---|---|---|---|---|---|---|
| 2 nmax | 2 | 4 | 4 | 6 | 8 | 16 | 28 | 50 | 70 |

Keyfi bir modülasyon sinyali için sapma oranı D = Δf/W (W: m(t)'nin en yüksek frekansı); β'nın tonlu durumdaki rolü D'dedir. Örnek: Δf = 75 kHz, W = 15 kHz → D = 5; Carson kuralıyla BT = 2(75 + 15) = 180 kHz; evrensel %1 eğrisi ile BT ≥ 3,2 Δf = 240 kHz.

## FM üretimi (FM-14 … FM-18)

İki temel yöntem vardır.

**Dolaylı FM (Armstrong).** Mesaj önce entegre edilir, β küçük tutularak dar bantlı bir faz modülatöründe (kristal denetimli osilatörle) dar bantlı FM üretilir; sonra frekans çarpanıyla istenen sapma elde edilir (bellekşiz doğrusal olmayan eleman + BPF). Frekans kararlılığı kristal osilatörden gelir. Doğrusal olmayan elemanın çıkışı v(t) = a1 s(t) + a2 s²(t) + … + an sⁿ(t); giriş FM sinyali için n'inci harmonik çıkışta fi'(t) = n fc + n kf m(t); BPF bant genişliği girişin n katıdır, β'nın n katına çıkması gerekir.

**Geniş bantlı FM modülatörü örneği.** Hedef: fc = 100 MHz, Δf = 75 kHz. Faz modülatöründe β1 ≈ 0,2 radyan; modülasyon frekansı 100 Hz–15 kHz için Δf1 = 20 Hz ve 3 kHz (alçak mesaj frekansları daha kritiktir). Toplam çarpım 3750; iki aşamalı çarpanlar n1 = 75 ve n2 = 50, ara karıştırıcıda 8,5 MHz kaydırma (taşıyıcı frekansı 0,1 MHz → 7,5 MHz → 2 MHz → 100 MHz; sapma 20 Hz → 1,5 kHz → 1,5 kHz → 75 kHz).

**Doğrudan FM.** Taşıyıcının anlık frekansı mesajla doğrudan değiştirilir: gerilim kontrollü osilatör (VCO). 1 GHz üzerinde klistron tüpü; düşük frekanslarda varikap (ters öngerilimli p-n eklemi kapasitesi) ile ayarlı bir LC rezonatörü (örneğin Hartley osilatörü). C(t) = C0 − ΔC m(t) ve ΔC ≪ C0 için fi(t) = f0 [1 + ΔC/(2C0) m(t)] = f0 + kf m(t), kf = f0 ΔC/(2C0).

Avantaj: iyi osilatör kararlılığı elde edilir (frekans çarpanları ve kristal ile), çıkış frekansı ile giriş gerilimi arasında sabit orantı, geniş frekans sapması elde edilebilir. Dezavantaj: frekans kararlılığı için ek devre gerekir (geri beslemeli kararlı yapı: VCO, alçak geçiren süzgeç, karıştırıcı, kristal osilatör, frekans ayırt edici).

## FM demodülasyonu (FM-19 … FM-23)

Frekans demodülasyonu, FM dalgasından mesajın geri kazanılmasıdır. Frekans ayırt edici (discriminator) çıkış gerilimi anlık frekansla doğrusal değişir. Dört yaklaşım: FM–AM dönüşümü (frekans ayırt etme), faz kaydırmalı ayırt etme, sıfır geçişli dedektör, frekans geri beslemesi.

**Frekans ayırt etme.** Sınırlayıcı (limiter) → türev alıcı (d/dt) → zarf dedektörü → DC bloğu. A noktasında s(t) = Ac cos[ωc t + 2π kf ∫m]; türevden sonra s'(t) = −2π Ac [fc + kf m(t)] sin[...]; zarf, 2π Ac[fc + kf m(t)]'ye orantılıdır; DC bileşeni çıkarılınca m(t) elde edilir. **Dengeli frekans ayırt edici:** iki ayarlı devre (fres > fc ve fres < fc), doğrusal aralığı genişletir; transfer fonksiyonu küçük bir frekans aralığında istenen doğrusal genlik cevabına yaklaşır (eğim dedeksiyonu).

**Faz kaymalı ayırt edici.** Doğrusal faz cevabı olan devre kullanır (eğim dedeksiyonundaki doğrusal genlik cevabının aksine). Grup gecikmesi ve ωc T = π/2 faz kayması: çıkış gerilimi ∝ dφ/dt ∝ kf m(t). Dengeli ayırt ediciye göre daha iyi doğrusallık sağlar.

**Sıfır geçişli dedektör.** Sert sınırlayıcı + tek kararlı (monostable) darbe üreteci + alçak geçiren süzgeç (entegratör) + DC bloğu. FM sinyalinin her yukarı veya aşağı sıfır geçişinde sabit genlikli ve süreli kısa darbe üretilir. Anlık frekans fi = nT/T, burada nT: T aralığındaki darbe sayısı. Entegratör çıkışı A·τ·fi(t)'ye eşittir; DC blok sonrası ∝ m(t). Ticari sıfır geçişli dedektörler %0,1'den iyi doğrusallıkla ve 100 MHz'e kadar çalışabilir.

**FM stereo çoğullama.** Frekans bölmeli çoğullamanın bir biçimidir; aynı taşıyıcı üzerinden iki ayrı kanal iletilir. FM radyo yayıncılığında kullanılır; mono alıcılarla uyumludur ve ayrılan FM yayın kanalı içinde çalışır.

## Faz kilitlemeli çevrim, PLL (FM-24 … FM-26)

PLL negatif geri besleme sistemidir ve frekans modülasyonuyla yakından ilişkilidir. Kullanım alanları: senkronizasyon, frekans bölme/çarpma, dolaylı frekans demodülasyonu. Bloklar: faz dedektörü (çarpıcı), alçak geçiren çevrim süzgeci h(t), VCO. VCO, çıkış frekansı dışarıdan uygulanan gerilimle belirlenen sinüzoidal sinyal üretecidir: s(t) = Ac sin[2π fc t + φ1(t)], φ1(t) = 2π kv ∫ m(t)dt; r(t) = Av cos[2π fc t + φ2(t)], φ2(t) = 2π kv ∫ v(t)dt. Amaç, VCO çıkışı r(t)'nin girişteki FM sinyaliyle aynı faza sahip olmasıdır, yani v(t) ∝ m(t).

Doğrusal olmayan model: e(t) = km Ac Av [sin(φe(t)) + yüksek frekans bileşeni]; φe = φ1 − φ2; v(t) = ∫ e(τ)h(t − τ)dτ; dφe/dt = dφ1/dt − 2π K0 ∫ sin φe(τ) h(t − τ)dτ, K0 = km kv Ac Av (çevrim kazanç parametresi, Hz). Sinüzoidal doğrusal olmama PLL davranışının çözümlemesini zorlaştırır.

Doğrusal model: faz hatası küçükken (φe ≪ 1 radyan) sin φe ≈ φe: Φe(f) = Φ1(f)/(1 + L(f)), L(f) = K0 H(f)/(jf) açık çevrim transfer fonksiyonu. |L(f)| ≫ 1 ise V(f) ≈ (jf/kv) Φ1(f)... ve v(t) ≈ (kf/kv) m(t): PLL, φ1'in türevini alan bir sistemle eşdeğerdir ve FM demodülatörü gibi çalışır.

## Doğrusal olmayan etkiler (FM-27, FM-28)

Güçlü doğrusal olmama kasıtlı olarak sokulur (frekans çarpanı); zayıf doğrusal olmama ise elemanların kusurlarından kaynaklanır (genlik doğrusal olmaması). v0 = a1 vi + a2 vi² + a3 vi³ girişte FM sinyali için ikinci ve üçüncü harmonikler ortaya çıkar. İstenen FM sinyalini ayırmak için gerekli koşul 2fc − (2Δf + W) > fc + Δf + W ve BPF ile fc'de ayırma: fc > 3Δf + 2W.

FM sinyalleri faz doğrusal olmamasına karşı çok hassas, genlik doğrusal olmamasına karşı duyarsızdır. En sık karşılaşılan faz doğrusal olmaması AM-PM dönüşümüdür; dB başına derece cinsinden sabit K ile nitelenir (girişteki zarfta 1 dB'lik değişim için çıkıştaki tepe faz değişimi). İyi bir mikrodalga tekrarlayıcıda K < 2°/dB'dir.

## Süperheterodin FM alıcı (FM-29)

Süperheterodin alıcı taşıyıcı frekans ayarı (radyo veya TV sinyali seçimi), süzme (istenmeyen modüleli sinyallerin ayrılması) ve yükseltme (iletim sırasındaki güç kaybının telafisi), ardından demodülasyon yapar. Ayarlanabilir, yüksek ve değişken Q'lu süzgeç yapma güçlüğünü sabit merkez frekanslı ve bant genişlikli IF süzgeci kullanarak aşar; bütün radyo ve TV alıcıları süperheterodin tipindedir. FM alıcısında sıra: anten → RF bölümü → karıştırıcı (yerel osilatör, ortak ayar) → IF bölümü → sınırlayıcı → frekans ayırt edici → ses yükselteci → hoparlör.

| Parametre | AM radyo | FM radyo |
|---|---|---|
| RF frekansı | 535–1605 kHz | 88–108 MHz |
| IF orta bant frekansı | 455 kHz | 10,7 MHz |
| IF bant genişliği | 10 kHz | 200 kHz |

*Not: Slayt dökümü hızlı bir okumadan yazıldı; birkaç değer (özellikle örnek hesapların ara sonuçları) taranmış sayfa üzerinden doğrulanmalıdır. Şekil ve devre diyagramları için sayfa taramalarına bakınız.*

*Bu içerik ders kapsamında dağıtılmış slaytlara aittir; kaynağı belirtilmeden dağıtıldığından arşiv ve nostalji amacıyla paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*
