---
baslik: EEM441 Haberleşme I: Genlik modülasyonu ders slaytları (AM-1 … AM-31)
ozet: Genlik modülasyonu, DSB-SC, SSB, VSB, süperheterodin alıcı ve frekans bölmeli çoğullamayı kapsayan 33 sayfalık taranmış ders slaytları.
---

EEM441 Haberleşme I dersinde dağıtılan, AM-1'den AM-31'e numaralı İngilizce slayt çıktılarının taramaları; 33 sayfa. Slaytların hazırlayanı sayfalarda yazmıyor. Taranmış sayfaların tamamı yazının sonundaki PDF'tedir; aşağıda içerik, sayfa sırasıyla metne dökülmüştür.

## Sürekli dalga (CW) modülasyonu ve bant geçiren sistemler (AM-1, AM-2)

Bir haberleşme sistemi, bilgi taşıyan sinyali (taban bant) kanal üzerinden iletir. Kanalın verimli kullanılması için frekans kaydırma gerekir. Modülasyon, bir dalga biçiminin (taşıyıcı, carrier) özelliklerinin başka bir dalga biçimine (mesaj, modülasyon sinyali) göre sistematik olarak değiştirilmesidir; vericide modülasyon, alıcıda demodülasyon yapılır. CW modülasyonu ikiye ayrılır:

- Genlik modülasyonu (AM): sinüzoidal taşıyıcının genliği mesajla değişir.
- Açı modülasyonu: taşıyıcının fazı veya frekansı mesajla değişir.

Uzun mesafeli haberleşme sistemleri bant geçiren spektrumda çalışır. Pratik kural olarak bant genişliği B ≈ 0,02 fc'dir. Örnek değerler: uzun dalga radyo ~100 kHz taşıyıcı, 2 kHz bant; kısa dalga radyo 5 MHz, 100 kHz; VHF 100 MHz, 2 MHz; mikrodalga 5 GHz, 100 MHz; optik 5·10¹⁴ Hz, 10¹³ Hz.

## Genlik modülasyonu (AM-3 … AM-8)

AM dalgası s(t) = Ac [1 + ka m(t)] cos(2π fc t) biçimindedir; ka modülatörün genlik duyarlılığıdır. Zarf, taban bant sinyalle aynı biçimdedir; şu koşulda: |ka m(t)| < 1 (yani 1 + ka m(t) > 0). Aksi halde aşırı modülasyon oluşur: taşıyıcıda faz ters dönmeleri ve zarf bozulması meydana gelir. Yüzde modülasyon = 100 × max|ka m(t)|. Ayrıca fc ≫ W olmalıdır (W: mesaj bant genişliği).

Tek tonlu modülasyonda m(t) = Am cos(2π fm t), μ = ka Am (modülasyon indeksi):

s(t) = Ac cos(2π fc t) + ½ μ Ac cos[2π(fc + fm)t] + ½ μ Ac cos[2π(fc − fm)t].

Güç dağılımı (1 Ω'luk dirençte): taşıyıcı gücü Ac²/2, üst yan bant gücü μ²Ac²/8, alt yan bant gücü μ²Ac²/8; toplam yan bant gücünün toplam güce oranı μ²/(2 + μ²).

**Anahtarlamalı modülatör.** Diyotlu devre ideal anahtar gibi çalışır. v1(t) = Ac cos(2π fc t) + m(t), |m(t)| ≪ Ac için v2(t) v1 ile sıfır arasında fc hızıyla değişir; v2(t) = [Ac cos(2π fc t) + m(t)] gτ(t) ve gτ(t) periyodik darbe dizisinin Fourier açılımı 1/2 + (2/π) Σ (−1)^(n−1)/(2n−1) cos[2π(2n−1)fc t] biçimindedir. fc ≥ 2W olmak üzere fc'de ortalanmış, 2W bantlı bir bant geçiren süzgeçle AM dalgası elde edilir: v2(t) ≈ Ac [1 + (4/πAc) m(t)] cos(2π fc t) + istenmeyen bileşenler.

**Doğrusal olmayan etkiler (örnek).** Girişi m(t) + Ac cos(2π fc t) olan, giriş–çıkış bağıntısı y(t) = a1 x + a2 x² olan elemanın çıkışında, fc ± W'de ortalanmış bant geçiren süzgeçle AM sinyali elde edilir. Modülasyon indeksi μ = 2a₂/a₁ · Am biçiminde bulunur ve süzgeç koşulları fc > 3W gibi eşitsizliklerle verilir.

**Zarf detektörü (demodülatör).** Diyot, R-C yükü ve alçak geçiren davranışla çalışır. Başarılı demodülasyon için: kondansatörün şarj zaman sabiti taşıyıcı periyoduna göre küçük, boşalma zaman sabiti ise taşıyıcı periyodundan büyük ve mesajın periyodundan küçük olmalıdır: (rf + Rs)C ≪ 1/fc ve 1/fc ≪ Rℓ C ≪ 1/W.

**AM'nin sınırları.** AM, taşıyıcıyı iletmekle güç harcar ve her iki yan bandı iletmekle bant genişliği harcar (BT = 2W). Bunlar sırasıyla DSB-SC (taşıyıcı bastırılır), VSB (bir yan bant tam, diğerinin bir kalıntısı) ve SSB (tek yan bant, taşıyıcı bastırılmış) modülasyonlarıyla aşılır; karşılığında alıcı karmaşıklaşır.

## Çift yan bant taşıyıcısı bastırılmış modülasyon, DSB-SC (AM-9 … AM-13)

s(t) = Ac cos(2π fc t) m(t), S(f) = ½ Ac [M(f − fc) + M(f + fc)]. Zarf mesajın mutlak değeridir; sıfır geçişlerinde faz ters dönmeleri olur. Bant genişliği AM ile aynı (2W), ancak taşıyıcı güç harcanmaz. Tepe zarf gücü karşılaştırmasında verici tepe gücü sabitken DSB-SC daha verimlidir.

**Ring modülatörü.** Dört diyotlu halka; c(t) kare dalga ile çarpılır, çıkış s(t) = m(t) c(t). Dış diyotlar iletimdeyken iç diyotlar kesimdedir ve tersi. c(t) = (4/π) Σ ((−1)^(n−1)/(2n−1)) cos[2π(2n−1) fc t]; bant geçiren süzgeç fc çevresini seçer (fc ≫ W, m(t) bant sınırlı).

**Eş fazlı (koherent) demodülasyon.** v(t) = Ac' cos(2π fc t + φ) s(t); alçak geçiren süzgeç sonrası v0(t) = ½ Ac Ac' m(t) cos φ. Faz hatası φ = 0 iken çıkış en büyük, φ = π/2 iken sıfırdır (quadrature null effect). φ rastgele değişirse bozulma olur; yerel osilatör taşıyıcıyla eş zamanlı (frekans ve faz) olmalıdır.

**Costas alıcısı.** Pratik senkron alıcıdır: yerel osilatör frekansı önceden bilinen fc'ye ayarlıdır. I (eş fazlı) ve Q (dik fazlı) kanal çıkışları bir geri besleme sistemi oluşturur. Küçük φ için I kanalı ≈ ½ Ac m(t) ve Q kanalı ≈ ½ Ac m(t) φ olur; ikisi çarpılıp VCO'ya uygulanır ve faz hatası otomatik düzeltilir. φ'nin işareti yerel faz hatasını otomatik düzeltmek için kullanılır.

**Dik taşıyıcılı çoğullama (QAM).** Aynı bant genişliğini paylaşan iki DSB-SC sinyal: s(t) = Ac m1(t) cos(2π fc t) + Ac m2(t) sin(2π fc t). Alıcıda eş fazlı ve dik fazlı demodülatör kolları iki mesajı ayırır; bant genişliğini koruyan bir şemadır ve Costas alıcısı veya pilot sinyal senkronizasyon için kullanılabilir.

## Yan bantların süzülmesi, VSB (AM-14 … AM-20)

Frekans ayırt etme yöntemiyle DSB-SC sinyalden bir yan bant (SSB) veya artık yan bant (VSB) elde edilir: ürün modülatörünün çıkışı u(t) = Ac m(t) cos(2π fc t) bir H(f) süzgecinden geçirilir: S(f) = U(f) H(f) = (Ac/2) [M(f − fc) + M(f + fc)] H(f). Koherent detektörde bozulmasız geri kazanım için H(f − fc) + H(f + fc) = sabit (−W ≤ f ≤ W) olmalıdır; VSB süzgeci bu koşulu geçiş bandında yan bant simetrisiyle sağlar.

Faz ayırt etme yöntemi (blok diyagramı): s(t) = sI(t) cos(2π fc t) − sQ(t) sin(2π fc t), sI(t) = ½ Ac m(t) ve sQ(t) = ½ Ac m'(t), m'(t) süzgeç H(f)'e bağlı ikinci bileşen. Eş fazlı bileşen süzgeç seçiminden bağımsızdır; H(f) yalnız sQ(t)'yi etkiler, sQ(t)'nin görevi bir yan bandın gücünü azaltmak veya yok etmektir.

VSB, bir yan bandı ve diğer yan bandın bir izini (vestige) iletir; amaç iletim bant genişliğini azaltmaktır. VSB'li bir sinyal için s(t) = ½ Ac m(t) cos(2π fc t) ± ½ Ac m'(t) sin(2π fc t).

**Televizyon sinyalleri.** Video sinyali geniş bant ve önemli düşük frekans içeriği taşır. Alıcıda demodülasyon devresi basit ve ucuz olmalıdır; bu yüzden zarf detektörü uygundur ve VSB'ye taşıyıcı eklenir. VSB şekillendirme süzgeci alıcıda uygulanır; vericide yan bant süzgeçlemesi yüksek güç düzeyinde pahalı olacağından alıcı tarafında yapılır. Ticari TV yayınında VSB genişliği yaklaşık 0,75 MHz'dir.

**Zarf detektörüyle bozulma (VSB + taşıyıcı).** s(t) = Ac [1 + ½ ka m(t)] cos(2π fc t) − ½ ka Ac m'(t) sin(2π fc t) için zarf a(t) = Ac {[1 + ½ ka m(t)]² + [½ ka m'(t)]²}^(1/2). Bozulma m'(t) kaynaklıdır. İki yolla azaltılır: modülasyon yüzdesini (ka'yı) küçültmek; VSB'nin yan bant genişliğini artırmak.

## Tek yan bant, SSB (AM-21 … AM-24)

SSB üretimi için mesaj spektrumunda orijin çevresinde enerji boşluğu olmalıdır; ses sinyalleri bu özelliği sağlar. Üst yan bandı içeren SSB için H(f − fc) + H(f + fc) = 1 (−W ≤ f ≤ W) ve Ha(f) = −j sgn(f) (kuadratür süzgeç, Hilbert dönüştürücü). Zaman bölgesi ifadesi:

- Üst yan bant: s(t) = ½ Ac m(t) cos(2π fc t) − ½ Ac m̂(t) sin(2π fc t)
- Alt yan bant: s(t) = ½ Ac m(t) cos(2π fc t) + ½ Ac m̂(t) sin(2π fc t)

İki aşamalı SSB modülatörde gerekli frekans ayırımı daha kolay sağlanır; süzgeçlerin geçiş bandı gereksinimi için kristal rezonatörler kullanılabilir.

**SSB demodülasyonu.** Ürün modülatörü ve alçak geçiren süzgeç. Frekans hatası Δf ve faz hatası Δφ durumlarında: mükemmel senkronizasyonda v0(t) = ¼ Ac Ac' m(t); Δf = 0, Δφ ≠ 0 için faz bozulması (ses için katlanılabilir, veri için değil); Δf ≠ 0 için spektral kayma ve bozulma, ses için kaymanın küçük olması kabul edilebilir. Spektrum ters çevirme (scrambling) gizli konuşma sistemlerinde kullanılır.

## Frekans kaydırma ve süperheterodin alıcı (AM-25 … AM-27)

Frekans çevirmesi (mixing, heterodyne), modüleli sinyalin spektrumunun yeni bir taşıyıcı frekansına kaydırılmasıdır; kuvvetlendirme veya başka işlemler içindir. Karıştırıcı ürün modülatörü ve bant geçiren süzgeçten oluşur. Yukarı çevirmede fℓo = fc + fb veya alt çevirmede fℓo = fc − fb seçilir.

**Örnek: uydu transponderi.** Yukarı bağlantı (uplink) 6 GHz, aşağı bağlantı (downlink) 4 GHz: farklı taşıyıcılar kullanılır; kazançlı bir ortamda kendinden salınımı önlemek için. Frekans çeviricisi yükseltilmiş yukarı bağlantı spektrumunu aşağı bağlantı geçiş bandına kaydırır: 6 − 2 = 4 GHz (yerel osilatör 2 GHz), 6 + 2 = 8 GHz süzülür.

**Süperheterodin AM alıcı (550–1600 kHz bandı).** RF yükselteç ve karıştırıcı, yerel osilatör (ortak ayar), ara frekans (IF) yükselteci fIF = 455 kHz, bant genişliği BIF = 10 kHz, zarf detektörü ve ses yükselteci. fℓo = fc + fIF. Karıştırıcıdan sonra kalan sinyal ve görüntü frekansı (fi = fc + 2fIF) arasında girişim olabilir; görüntü frekansları RF kesimde süzülmelidir. Görüntü bandı: 550 + 910 = 1460 ile 1600 + 910 = 2510 kHz.

**Örnek: süperheterodin radyoda görüntü reddi.** fc = 1,6–2,6 MHz, BT = 6 kHz alıcı; 14–15 MHz ve 3,0–5,6 MHz civarında güçlü istenmeyen sinyaller. (A) fℓo = fc + fIF için görüntü frekansı fi = fc + 2fIF ≥ 5,6 MHz yapılacak şekilde fIF ≥ 2 MHz; fℓo = 3,6–4,6 MHz ve yerel osilatör ayar oranı ≈ 1,3; kesirli IF bant genişliği yaklaşık 0,003. (B) fℓo = fc − fIF için fIF = 0,6 MHz ve ayar oranı ≈ 2.

## Frekans bölmeli çoğullama, FDM (AM-28 … AM-30)

Çoğullama, birçok bağımsız sinyalin ortak bir kanal üzerinden iletilecek bileşik bir sinyalde birleştirilmesidir. 300–3400 Hz'lik konuşma sinyallerinin birbirine girişim yapmaması için ayrılmaları gerekir; ayırma frekansta (FDM) veya zamanda (TDM) yapılabilir. FDM'de en sık kullanılan modülasyon, en az bant genişliğini kaplayan SSB'dir.

Telefon hiyerarşisi: temel grup 12 SSB (alt yan bant) kanal, her biri 4 kHz; süpergrup 5 grup (60 ses kanalı); ana grup; çok büyük grup. Gruplar oluşturmak ekonomik nedenlerle yapılır.

**Örnek: ayırma (demultiplexing).** s(t) = m1(t) cos(2π f1 t) + m2(t) cos(2π f2 t) bileşik sinyalinde m1 ve m2 bant genişliği W1 ve W2 ise, her kanal bant geçiren süzgeç + eş fazlı demodülatör + alçak geçiren süzgeçle ayrılır. Girişimi önlemek için f2 − W2 > f1 + W1 (veya f2 − f1 > W1 + W2) olmalıdır. Soru: çoğullama ile ayırma arasındaki fark nedir?

## AM sistemlerinin karşılaştırması (AM-31)

1. AM: iki yan bant ve taşıyıcı iletilir; zarf veya kare yasalı dedektörle demodülasyon; ticari yayıncılıkta kullanılır.
2. DSB-SC: çok daha az verici gücü gerektirir; AM'den ucuz verici, karmaşık alıcı; noktadan noktaya haberleşmeye uygundur.
3. SSB: en az verici gücü ve en az bant genişliği; ses sinyallerinin kablo üzerinden uzun mesafe iletimi için tercih edilir; kuadratür modülasyon örneğidir.
4. VSB: SSB ile DSB-SC arasında bant genişliği gerektirir; TV ve geniş bantlı veri gibi büyük bant genişlikli sinyallerde bant tasarrufu önemlidir.

*Not: Taranmış sayfaların bir kısmında küçük el yazısı işaretlemeler vardır; yazıda yalnız basılı slayt içeriği verilmiştir. Yazı, dönemin sunum notlarını özetleyerek metne döker; şekil ve diyagramlar için sayfa taramalarına bakılmalıdır.*

*Bu içerik ders kapsamında dağıtılmış slaytlara aittir; kaynağı belirtilmeden dağıtıldığından arşiv ve nostalji amacıyla paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*
