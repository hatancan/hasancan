---
baslik: EEM224 Elektromanyetik I: 2004 Güz Genel Sınavı ve Çözümleri (Eski Kod EEM323)
ozet: Eski Elektromanyetik sınavından sorular, temel çözüm adımları ve sonuçların metin dökümü.
---

Bu yazı, 2004 güz dönemi Elektromanyetik sınav ve çözüm sayfalarından hazırlandı; fotoğraflanmış sayfalardan metne aktarıldı. Kaynakta eski ders kodu EEM323 olarak geçmektedir; arşivde EEM224 altında sınıflandırıldı. Kişisel bilgiler aktarılmadı. Fotoğraflar özel arşivde saklanır; bu yazıda indirme dosyası yoktur.


## Soru 1: Maxwell denklemleri ve süreklilik

Zaman uzamında dört Maxwell denklemini ve süreklilik denklemini diferansiyel biçimde yazınız; fiziksel anlamlarını birer cümleyle açıklayınız. İntegral biçimlerini çıkarınız ve fazör uzamındaki karşılıklarını veriniz.

- ∇×E = −∂B/∂t: değişen manyetik alan elektrik alanın dolaşımını oluşturur.
- ∇×H = J + ∂D/∂t: iletim ve yer değiştirme akımları manyetik alanın dolaşımını oluşturur.
- ∇·D = ρ: elektrik yükü elektrik akısının kaynağıdır.
- ∇·B = 0: kapalı yüzeyden net manyetik akı sıfırdır.
- ∇·J = −∂ρ/∂t: yükün korunumu.

İlk iki denklem Stokes teoremiyle, diğerleri diverjans teoremiyle integral biçimine dönüştürülür. Fazör alanlarda e^(jωt) kabulüyle ∂/∂t yerine jω yazılır. Doğrusal ortamda B=μH ve D=εE kullanılır.

## Soru 2: Dönen dairesel sarım

Yarıçapı 3 mm olan sarım, ω₁=4π×10⁶ rad/s ile döner. t=0'da x-y düzlemine paraleldir. Manyetik alan +z yönünde B=2 sin(4π×10⁶t) Wb/m²'dir. Gösterilen uç polaritesine göre indüklenen gerilim istenir.

Φ=BS cos(ω₁t)=9π×10⁻⁶ sin(2ω₁t).

−dΦ/dt=−72π² cos(2ω₁t). Kaynak, uç polaritesini integral yönünün tersine seçerek V_ind=72π² cos(2ω₁t) V sonucunu verir.

## Soru 3: Eğik gelen düzlem dalga

z<0 tarafındaki ε_r=2, μ_r=1 malzemeden havaya gelen dalganın elektrik alanı:

E_inc=(2â_x−3â_y−2√3â_z) cos[ωt−15π(√6x+√2z)] V/m.

Geliş açısı, dalga sabiti, açısal frekans, dalga boyu, yansıyan ve iletilen alanlar istenir. Çözümde:

θ_i=60°, k=30π√2, ω=9π×10⁹ rad/s, λ=√2/30≈0,0471 m.

Alan geliş düzlemine dik ve paralel bileşenlere ayrılır. Fazör yansıtma katsayıları ayrı hesaplanır; toplam alan bileşenlerin vektörel toplamıdır. İletilen çözümde sınıra dik yönde üstel sönüm ortaya çıkar.

*Not: Son iki alan ifadesinin uzun el yazısı satırlarında bazı işaretler yeterince kesin okunamadığından bunlar yeniden türetilerek kaynak çözümü gibi tamamlanmadı.*

## Soru 4: İletim hattı

Dört kayıpsız hat parçasında verilen karakteristik empedans, yük ve λ/2 veya λ/4 uzunlukları kullanılarak giriş empedansı bulunur. Çözümde yarım dalga hattı yükü tekrarlar; çeyrek dalga hattı Z_in=Z₀²/Z_L dönüşümünü yapar.

İlk kolun yarım dalga dönüşümü 25 Ω verir. İkinci kolun çeyrek dalga dönüşümü 35²/49=25 Ω'dur. Bunların paraleli 12,5 Ω, üçüncü kolun giriş empedansı ise 15²/12,5=18 Ω olur. Kısa devre sonlandırılmış dördüncü çeyrek dalga kolu girişte açık devre görünür; toplam Z_in=18 Ω'dur. Dördüncü kolun sonlandırması açık devreye çevrilirse girişte kısa devre görünür ve toplam Z_in=0 çıkar.
