---
baslik: EEM301 Sinyaller ve Sistemler I: Sinyaller, Sistem Özellikleri ve Konvolüsyon Defteri (2014)
ozet: Fotoğraflanmış 22 defter sayfasından sinyal dönüşümleri, dürtü ve basamak, enerji-güç, sistem özellikleri ve konvolüsyon örnekleri.
---

Bir arkadaşın EEM301 için tuttuğu ders defterinin **22 fotoğraflanmış sayfası metne aktarıldı**. Sayfalardan birinde 8 Ekim 2014 tarihi bulunuyor; fotoğraf dizisi 14 Ekim 2014 adını taşıyor. Kişisel bilgiler aktarılmadı. Fotoğraflar özel arşivde tutulduğundan bu yazıda fotoğraf veya indirme dosyası yok. Sondaki kısa ek, ayrı bir bulanık çözüm fotoğrafının okunabilen kısmıdır.

## Karmaşık sayılar ve sinyal gösterimi

z=x+jy için gerçek kısım x, sanal kısım y ve büyüklük |z|=√(x²+y²)’dir. j²=−1, j³=−j, j⁴=1 olduğundan j’nin kuvvetleri dörtlü döngü oluşturur. Kutupsal gösterimde z=r(cosθ+j sinθ)=re^(jθ) yazılır.

Sürekli zamanlı x(t) her gerçek t için, ayrık zamanlı x[n] tam sayı n için tanımlanır. Bir dizinin grafiği, örnek noktalarına çizilen dikey çizgilerle gösterilir. Ayrık zaman ve genliğin sayısallaştırılması aynı işlem değildir.

## Kaydırma, ters çevirme ve ölçekleme

x(t−t₀) sağa kaydırma, x(t+t₀) sola kaydırma ve x(−t) zaman terslemesidir. Ayrık zamanda x[n−n₀], x[n+n₀] ve x[−n] aynı işlemleri örnek indisleri üzerinde yapar. Defterde parçalı grafikler üzerinde yeni kırılma noktaları işaretleniyor.

x(at) için |a|>1 zaman sıkışması, 0<|a|<1 zaman genişlemesidir. a<0 durumunda ayrıca tersleme vardır. Birden çok işlemde orijinal kırılma anları yeni argümana eşitlenerek taşınır.

Çift ve tek bileşenler:

- xₑ(t)=[x(t)+x(−t)]/2.
- xₒ(t)=[x(t)−x(−t)]/2.
- x=xₑ+xₒ; çift bileşen düşey eksene, tek bileşen orijine göre simetriktir.

## Periyodiklik

Sürekli zamanda x(t+T)=x(t), ayrık zamanda x[n+N]=x[n] koşulu aranır. Ayrık zamanlı N pozitif tam sayı olmalıdır.

- cos(ω₀t) için temel periyot 2π/|ω₀|’dır.
- e^(jω₀n) ancak ω₀/(2π) rasyonelse periyodiktir.
- cos(πn/5) için N=10 temel periyottur; 20 de bir periyottur.
- cos(2t) için temel periyot π’dir.

Defterde sayılabilir ve sayılamaz kümelerle ilgili kısa bir olasılık yorumu da bulunuyor: gerçek eksenden sayı seçilince tam sayı gelmesi “0” olarak yazılmış.

*Not: Tüm gerçek eksen üzerinde düzgün olasılık dağılımı tanımlanamaz. Sayılabilir bir kümenin olasılığının sıfır olması, örneğin bir aralık üzerinde sürekli dağılım seçildiğinde geçerlidir; yalnız kümelerin eleman sayılarını bölerek olasılık hesaplanmaz.*

## Üstel ve sinüzoidal sinyaller

Euler bağıntısı e^(jωt)=cosωt+j sinωt, üstel gösterimi sinüs ve kosinüse bağlar. e^(at) için a’nın gerçek kısmı büyüme/sönme, sanal kısmı salınım üretir. Ayrık zamanda aⁿ dizisi |a|<1 için sağa doğru söner; negatif a işaret değişimine yol açar.

## Birim basamak ve dürtü

u[n], n≥0 için 1, aksi durumda 0’dır. δ[n] yalnız n=0’da 1’dir. Dolayısıyla δ[n]=u[n]−u[n−1]. Sürekli zamanda dürtünün birim alan özelliği ve u(t)’nin türevi oluşu kullanılır.

*Not: Sayfalardan birindeki dürtü çiziminde sıfırdaki değer 1 olarak işaretlenmiş. Bu değer ayrık zamanlı δ[n] için geçerlidir; sürekli zamanlı δ(t), sonlu yükseklikli sıradan bir fonksiyon değildir.*

Dürtülerle örnek dizi açılımı:

x[n]=δ[n+1]+0,5δ[n]+2δ[n−1]+3δ[n−2].

Genel olarak x[n]=Σx[k]δ[n−k]. Bu gösterim, LTI sistem çıkışını dürtü yanıtlarından kurmanın başlangıcıdır.

## Enerji ve güç

Sürekli zamanlı enerji E=∫|x(t)|²dt, ayrık zamanlı enerji E=Σ|x[n]|²’dir. Ortalama güç, simetrik aralık büyütülürken birim zamana veya örnek sayısına düşen enerjinin limitidir.

Karmaşık üstel e^(jωt) için |x|²=1, ortalama güç 1 ve toplam enerji sonsuzdur. Sonlu ve sıfırdan farklı enerjili bir sinyalin ortalama gücü sıfırdır.

Defterde x(t)=e^(−2t)u(t) örneği enerji sinyali olarak sınıflandırılmış ve E=1/2 yazılmış.

*Not: Bu sonuçta sinyalin karesi alınmamış. Verilen x(t) için E=∫₀∞e^(−4t)dt=1/4 olur. Enerji sinyali sınıflandırması ve P=0 sonucu değişmez.*

## Sistem özellikleri

Belleksiz sistemin çıkışı yalnız aynı andaki girişe bağlıdır. Gecikmiş örnekler, ileri örnekler, türevler ve integraller bellek gerektirir. Nedensellik ise gelecekteki giriş değerlerine bağımlı olmama koşuludur; bellekli bir sistem nedensel olabilir.

Doğrusallık için toplamsallık ve ölçekleme birlikte sağlanmalıdır. y=2x+3 sisteminde sıfır giriş sıfır çıkış vermediği için doğrusallık yoktur. y[n]=x[n]+x[n+1] gelecekteki örneğe bağlı olduğu için nedensel değildir.

Zamanla değişmezlik, giriş kaydırıldığında çıkışın aynı miktarda kaymasını gerektirir. Defter, önce kaydırıp sistemi uygulama ile önce sistemi uygulayıp kaydırma yollarını karşılaştırır. BIBO kararlılıkta sınırlı girişin sınırlı çıkış üretmesi istenir.

Hareketli ortalama örneklerinde kullanılan pencerenin geleceğe uzanıp uzanmadığına bakılır; simetrik pencere genel olarak gelecekteki örnekleri de kullanır.

## Ayrık zamanlı konvolüsyon

LTI sistem için y[n]=Σx[k]h[n−k]. Grafiksel hesapta h[k] ters çevrilir, n kadar kaydırılır; çakışan örnekler çarpılıp toplanır.

x=[1,1,1] ve h=[3,2,1], her iki dizinin başlangıcı n=0 olmak üzere:

| n | Çakışan çarpımlar | y[n] |
|---|---|---|
| 0 | 1·3 | 3 |
| 1 | 1·2+1·3 | 5 |
| 2 | 1·1+1·2+1·3 | 6 |
| 3 | 1·1+1·2 | 3 |
| 4 | 1·1 | 1 |

Sonuç [3,5,6,3,1]’dir. Sonlu dizilerin konvolüsyon uzunluğu Nₓ+Nₕ−1 olur; başlangıç indisleri toplanır.

## Geometrik toplamlı konvolüsyon

x[n]=2ⁿu[−n] ve h[n]=u[n] için çarpımın destek koşulları k≤0 ve k≤n’dir. Bu nedenle toplamın üst sınırı min(n,0) olur:

- n<0: y[n]=Σₖ₌₋∞ⁿ2ᵏ=2^(n+1).
- n≥0: y[n]=Σₖ₌₋∞⁰2ᵏ=2.

Geometrik seri formülü Σₖ₌₀ᴺaᵏ=(1−a^(N+1))/(1−a), a≠1; sonsuz seri için ayrıca |a|<1 koşulu kullanılır.

## Sürekli zamanlı konvolüsyon örneği

Son sayfada verilen sinyaller:

x(t)=e^(−3t)[u(t)−u(t−2)], h(t)=e^(−t)u(t).

x(t) yalnız 0≤t<2 aralığında etkindir. Konvolüsyon y(t)=∫x(τ)h(t−τ)dτ olarak yazılmış; t<0, 0<t<2 ve t>2 bölgeleri çizilmiş. Sayfadaki integral satırlarında 0–2 ve 2–∞ sınırları kullanılmış.

*Not: Çarpımın etkin aralığı 0≤τ≤min(t,2)’dir. Dolayısıyla doğru parça sonuçları t<0 için 0; 0≤t<2 için e^(−t)(1−e^(−2t))/2; t≥2 için e^(−t)(1−e^(−4))/2 olur. Kaynaktaki 2–∞ integrali, sonlu destekli x(t) ile uyumlu değildir.*

## Bulanık çözüm fotoğrafından okunabilen ek

Ayrı fotoğrafta rasyonel ifadelerin kısmi kesirlere ayrılması çalışılıyor. (s+1)² ve s+2 türü paydalar, A/(s+1)² ve B/(s+1) biçimindeki terimler seçilebiliyor. Paydalar eşitlenerek katsayıların karşılaştırıldığı ara satırlar var.

*Not: Bu fotoğraftaki başlangıç ifadesi ve katsayıların tamamı güvenle okunamıyor. Sayısal bir çözüm tahmin edilmedi; yalnız seçilebilen yöntem ve terimler aktarıldı.*
