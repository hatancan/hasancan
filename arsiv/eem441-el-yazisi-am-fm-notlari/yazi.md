---
baslik: EEM441 Haberleşme I: El yazısı ders notları – AM, DSB-SC, SSB ve FM
ozet: Eş fazlı demodülasyonda frekans ve faz hatası, frekans modülasyonu, dar bant FM yaklaşımı ve AM/DSB-SC/SSB/FM formül özeti; fotoğraflanmış el notlarından metne aktarıldı.
---

Arkadaşların tuttuğu iki ayrı el yazısı not takımı (21 fotoğraf) fotoğraflanmış sayfalardan metne aktarıldı; kişisel bilgiler çıkarıldı. Fotoğrafların kendisi yayımlanmadı. Notların bir kısmı kareli defterde (eş fazlı demodülasyon ve FM türetmeleri), bir kısmı tek sayfalık formül özetleri olarak (AM, DSB-SC, SSB, FM) yazılmıştır.

## Formül özeti: AM, DSB-SC, SSB ve FM

**AM.** s(t) = Ac (1 + ka m(t)) cos(ωc t), ωc = 2π fc. |ka m(t)| < 1 (yani 1 + ka m(t) > 0) ise zarf bozulmaz (çakışma yok); ka m(t) > 1 olursa kesişir (aşırı modülasyon). Spektrum: S(f) = (Ac/2)[δ(f − fc) + δ(f + fc)] + ka (Ac/2)[M(f − fc) + M(f + fc)]. Taşıyıcı gücü Ac²/2; μ = ka Am için üst yan bant gücü μ²Ac²/8 ve alt yan bant gücü μ²Ac²/8. Tek tonda s(t) = Ac (1 + μ cos ωm t) cos ωc t; bant genişliği BW = 2 fm. Zarftan okuma: Ac = (Amax + Amin)/2, μ = (Amax − Amin)/(Amax + Amin).

**DSB-SC.** s(t) = Ac cos ωc t · m(t); S(f) = ½ Ac [M(f − fc) + M(f + fc)]. Eş fazlı (koherent) detektörde v(t) = Ac cos(ωc t + φ) s(t): v(t) φ = 0 iken en büyük, φ = π/2 iken en küçüktür. Dik taşıyıcılı çoğullama: s(t) = Ac cos ωc t m1(t) + Ac sin ωc t m2(t); 90° faz farklı iki DSB-SC sinyalin toplamı. Artık yan bant (vestigial): s(t) = ½ Ac cos ωc t m(t) + ½ Ac m'(t) sin ωc t.

**SSB.** s(t) = (Ac/2) m(t) cos ωc t ∓ (Ac/2) m̂(t) sin ωc t; m̂(t) mesajın Hilbert dönüşümüdür (m(t) = Am cos ωm t için m̂(t) = Am sin ωm t).

**FM.** s(t) = Ac cos(ωc t + 2π kf ∫ m(t)dt); tek tonda s(t) = Ac cos(ωc t + β sin ωm t), β = Δf/fm. β ≫ 1 geniş bant, β ≪ 1 dar bant. Sapma oranı D = Δf/W, W = fm. Anlık frekans fi(t) = fc + kf Am cos ωm t ve kf Am = Δf = β fm. Spektrum: β ≪ 1 için J0(β) ve J1(β) önemlidir; β ≫ 1 için n_max, Jn(β) > 0,01 koşuluyla bulunur.

## Eş fazlı demodülasyonda frekans ve faz hatası

Sinyal c(t) = f(t) cos ω0 t, yerel osilatör cos[(ω0 + Δω)t + θ] ile çarpılır (ardından alçak geçiren süzgeç, AGS):

c1(t) = f(t) cos ω0 t · cos[(ω0 + Δω)t + θ] = ½ f(t) [cos((2ω0 + Δω)t + θ) + cos(Δω t + θ)].

AGS'den geçen çıkış e0(t) = ½ f(t) cos(Δω t + θ). Durumlar:

- Δω = 0, θ = 0 ise e0(t) = ½ f(t): hiç bozulma yok.
- Δω = 0, θ ≠ 0 ise e0(t) = ½ f(t) cos θ = k f(t): θ zamanla değişmedikçe yalnız genlik küçülür veya büyür. θ mümkün olduğunca sabit olmalı ve θ ≠ 90° olmalıdır; θ = π/2 ise e0(t) = 0. θ zamanla değişirse (θ(t)) çıkış dikkat edilmesi gereken biçimde bozulur.
- Δω ≠ 0, θ = 0 ise e0(t) = ½ f(t) cos(Δω t): ciddi bozulma vardır (çıkışın zarfı Δω t'ye göre salınır). Spektrumda E0(ω) = ¼ [F(ω − Δω) + F(ω + Δω)]; Δω küçükse iki kopya birbirine çok yakındır.

Tek yan bantlı (TYB) sinyal c(t) = f(t) cos ω0 t − f̂(t) sin ω0 t aynı biçimde demodüle edilirse AGS çıkışı e0(t) = ½ f(t) cos(Δω t + θ) + ½ f̂(t) sin(Δω t + θ) olur. Δω = 0, θ = 0 için e0 = ½ f(t) (bilgi işareti); Δω = 0, θ ≠ 0 için e0 = (f(t)/2) cos θ + (f̂(t)/2) sin θ: üst veya alt TYB'de θ, f(t) ile Hilbert dönüşümünün bir karışımını verir (faz bozulması).

## Frekans modülasyonu

Genlik A ve açı θ(t) ile c(t) = A cos θ(t); anlık açısal frekans ωa(t) = dθ(t)/dt. Taşıyıcının açısı mesajla değişir; bu notlarda anlık frekans kullanılır.

- c(t) = A cos θ(t) = A cos(ω0 t + θ0 + k f(t)): faz (açı) modülasyonu.
- c(t) = A cos[ω0 t + k ∫ f(t) dt]: frekans modülasyonu; ωa(t) = ω0 + k f(t), Δω ≈ k |f(t)|max.

Örnek: f(t) = a cos ωm t için ωa(t) = ω0 + k a cos ωm t, Δω = k a ve c(t) = A cos[ω0 t + (k a/ωm) sin ωm t] = A cos[ω0 t + (Δω/ωm) sin ωm t]. Modülasyon derecesi β = Δω/ωm. β ≪ π/2 için dar bant FM: cos(β sin ωm t) ≈ 1, sin(β sin ωm t) ≈ β sin ωm t ve

c(t) ≈ A [cos ω0 t − β sin ω0 t sin ωm t] = A [cos ω0 t − (β/2) cos(ω0 − ωm)t + (β/2) cos(ω0 + ωm)t].

Sayısal doğrulama (β ≪ 1,57 rad/s koşulu): β = 0,2 için cos β = 0,9801 ≈ 1 ve sin β = 0,19867 ≈ 0,2; β = 0,5 için cos β = 0,8776 ≈ 1,0 ve sin β = 0,4794 ≈ 0,5.

Seri açılımla daha iyi yaklaşım (cos Q = 1 − Q²/2! + Q⁴/4! − …, sin Q = Q − Q³/3! + …) β biraz artırılarak yapılır: cos(β sin ωm t) ≈ 1 − (β sin ωm t)²/2 ve sin(β sin ωm t) ≈ β sin ωm t. Sonuç

c(t) = (1 − β²/4) cos ω0 t + (β²/8) cos(ω0 − 2ωm)t + (β²/8) cos(ω0 + 2ωm)t − (β/2) cos(ω0 − ωm)t + (β/2) cos(ω0 + ωm)t,

β ≪ 1 için geçerlidir. Spektrumda ω0'da π(1 − β²/4), ω0 ± ωm'de ±πβ/2 ve ω0 ± 2ωm'de πβ²/8 genlikli çizgiler görülür; bu yaklaşımda bant genişliği 4ωm'dir (tahtadaki çizimde gösterilmiştir). Dar bant FM'de yan bantlar taşıyıcının iki tarafında, geniş bantta ise gerçek FM sinyali c(t) = cos ω0 t − kg(t) sin ω0 t biçiminde yazılır: burada g(t) = ∫ f(t)dt ve k g(t) ≪ π/2 rad/s olduğunda cos[k ∫ f dt] ≈ 1 ve sin[k ∫ f dt] ≈ k g(t). Yan bandlar g(t)'nin görünümüne benzer; AM'de yan bandlar f(t) ile orantılıdır. Dar bant FM'de bant genişliği g(t)'nin en yüksek frekansının iki katıdır ve f(t) ile g(t)'nin en yüksek frekans bileşenleri aynıdır.

*Not: Kareli defter sayfaları solukta çekildiğinden bazı denklemlerde belirsizlik vardı; belirsiz kısımlar standart FM/AM türetmeleriyle uyumlu biçimde yazıldı, fotoğraflar yayınlanmadığı için doğrulama yalnız özel arşivdedir.*
