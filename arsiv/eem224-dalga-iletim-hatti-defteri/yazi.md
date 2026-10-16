---
baslik: EEM224 Elektromanyetik I: Dalga yayılımı ve iletim hattı defteri
ozet: Arşivdeki soru ve çözüm sayfalarının kişisel bilgiler çıkarılarak hazırlanmış metin dökümü.
---

Fotoğraflanmış sayfalardan metne aktarılan bu arşiv kaydı, soru metinleri ile okunabilen çözüm adımlarını içeriyor. Fotoğraflar özel arşivde saklanıyor; indirilebilir dosya bulunmuyor.

Bir arkadaşın ders notu, defter fotoğraflarından aktarılmıştır; kişisel bilgiler çıkarıldı. Dosya adları 1 Ocak 2015’i gösteriyor. Açılmış defter klasöründeki aynı sayfalar ayrıca yayımlanmadı. Sayfaların fotoğraf sırası konu sırasından farklı olduğu için aşağıda konular bir araya getirildi.

## Dalga, faz hızı ve deri kalınlığı
Genel kayıplı dalga Ẽ(z)=E₀exp(−αz)exp(−jβz). Yayılma sabiti γ=α+jβ; faz hızı vp=ω/β. Genliğin e⁻¹ katına düştüğü uzaklık δ=1/α; buna deri kalınlığı deniyor. İyi iletken ile mükemmel iletken ayrımı not edilmiş: sonlu iletkenlikte alan malzemenin içine sönümlenerek girer.

Yakın frekanslı iki dalganın toplamı:

E=2E₀cos(Δωt−Δβz)cos(ω₀t−β₀z).

Taşıyıcının faz hızı ω₀/β₀; zarfın grup hızı Δω/Δβ, limitte dω/dβ. Dağılımlı ortamda bu iki hız farklı olabilir.

## Anlık ve ortalama güç
P(t)=E(t)×H(t), birimi W/m². Kapalı yüzeyden dışarı giden güç ∮P·dS ile bulunur. Sinüzoidal rejimde ortalama P=½Re{Ẽ×H̃*}. Notlar 1/2 katsayısını iki tepe değerin RMS değerlerine çevrilmesiyle ilişkilendiriyor. Örnek ortam olarak εr=80, μr=1, σ=4 S/m deniz suyu verilmiş; faz hızı, empedans, faz sabiti, deri kalınlığı, alanın onda bire düştüğü uzaklık ve güç soruluyor.

## Dik geliş ve duran dalga
Gelen Ẽᵢ=âxEᵢ₀exp(−jβ₁z), yansıyan Ẽᵣ=âxEᵣ₀exp(jβ₁z), iletilen Ẽₜ=âxEₜ₀exp(−jβ₂z). Manyetik alanlarda geri ilerleme nedeniyle yön değişimi var. Sınırda teğetsel E ve H eşitlenerek Γ=Eᵣ₀/Eᵢ₀=(η₂−η₁)/(η₂+η₁), τ=1+Γ elde ediliyor.

Mükemmel iletkende iç alan sıfır, Γ=−1 ve Eᵣ₀=−Eᵢ₀. Toplam Ẽ=−2jâxEᵢ₀sinβz; elektrik ve manyetik alan düğümleri λ/4 kaymış. Aynı tür iki komşu minimum arasındaki uzaklık λ/2. Kısmi yansımada maksimum ve minimum genlikler gelen genliğin 1+|Γ| ve 1−|Γ| katları; duran dalga oranı S=(1+|Γ|)/(1−|Γ|).

*Not: Defterde −j çarpanının zaman alanına geçirilmesine ilişkin bir satırın yanında “doğru değil, bunu bulmak ödev” uyarısı var. O satır doğrulanmış bir sonuç gibi aktarılmadı.*

## Eğik geliş ve Snell yasası
İlerleme vektörüyle elektrik alan birbirine dik; H=(1/η)ân×E. Gelen ve yansıyan açı eşit. Sınır boyunca fazların eşleşmesinden β₁sinθᵢ=β₂sinθₜ. Manyetik olmayan ortamlar için sinθᵢ/sinθₜ=√(ε₂/ε₁). Kritik açı sinθc=√(ε₂/ε₁), yalnız yoğun ortamdan daha az yoğun ortama geçişte uygulanıyor. Paralel kutuplanmada yansımanın sıfır olduğu açı Brewster açısı olarak anılıyor.

## Birden fazla sınır
Üç katman çizimlerinde ilk geçiş, ikinci sınırdan dönüş ve yeniden iletim ayrı ayrı yazılmış. Her katkıda ilgili τ ve Γ katsayıları ile kat edilen yolun exp(−jβl) fazı çarpılıyor; toplam alan bu katkıların toplamı. Defterde iki veya üç sınırın çoklu yansımalarını MATLAB ile inceleme ödevi not edilmiş.

## İletim hattı modeli
İki iletkenli hat, küçük Δz parçası için seri RΔz ve LΔz; paralel GΔz ve CΔz elemanlarıyla modelleniyor. Gerilim ve akım ileri ve geri dalgaların toplamı. Kayıpsız hat için V(z)=V⁺exp(−jβz)+V⁻exp(jβz). Açık uçta akım sıfır ve gerilim maksimum; kısa devrede gerilim sıfır. Kaynak ve yük sınır koşulları bu iki bilinmeyen dalga genliğini belirliyor.

Yükte ΓL=(ZL−Z₀)/(ZL+Z₀). ZL=Z₀ olduğunda yansıma yok. Kayıpsız hattın giriş empedansı:

Zin=Z₀[ZL+jZ₀tan(βl)]/[Z₀+jZLtan(βl)].

## Çeyrek dalga dönüştürücü
l=λ/4 için βl=π/2; giriş empedansı Zin=Z₀²/ZL. Açık uç ve kısa devre bu uzunlukta birbirine dönüşür. S=1 uyumlu hattı, S→∞ tam yansımayı gösteriyor. Darbe örneğinde 10 km hat boyunca giriş ve çıkış işaretlerinin gecikmesi çizilmiş; belirli bir dalga hızı verilmediğinden sayısal gecikme eklenmedi.
