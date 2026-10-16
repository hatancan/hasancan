---
baslik: EEM224 Elektromanyetik I: 2014: Tahta ve yansıtılan ödev soruları
ozet: Arşivdeki soru ve çözüm sayfalarının kişisel bilgiler çıkarılarak hazırlanmış metin dökümü.
---

Fotoğraflanmış sayfalardan metne aktarılan bu arşiv kaydı, soru metinleri ile okunabilen çözüm adımlarını içeriyor. Fotoğraflar özel arşivde saklanıyor; indirilebilir dosya bulunmuyor.

Şubat ve Mart 2014 ders fotoğraflarının okunabilen eğitim içeriği metne aktarıldı. Fotoğraflarda görünen kişiler yayımlanmadı. Yansıtılan notlarda Prof. Dr. S. Gökhan Tanyer’in adı bulunuyor.

## Vektörel üçlü çarpım
24 Şubat sayfasındaki ödev: A×(B×C)=B(A·C)−C(A·B) özdeşliğini örneklerle doğrulayınız.

## Potansiyel sorusu
3 Mart sayfası: V(R)=E₀Rsinθ verilmiş. a) E=? b) E(R=1, θ=60°, φ=30°)=? Fotoğraf çözüm içermiyor.

## MATLAB görselleştirme
11 Mart yansısında `legend` komutunu öğrenme ve `fprintf` için örnek üretme ödevi var. İki boyutlu “baklava” örneği `ones`, `cos`, `sin`, transpoz, eleman bazlı kare ve karekök ile matris oluşturuyor; `subplot`, `contour` ve `mesh` ile gösteriyor. Tahtada alternatifler `contour(z)`, `mesh(z)`, `surf(z)`, `surfl(z)` olarak listelenmiş.

```matlab
Rrad = pi .* (0:360) ./ 180;
lenR = length(Rrad);
x = ones(lenR,1) * cos(Rrad);
y = ones(lenR,1) * sin(Rrad);
y = y';
Baklava = sqrt(x.^2 + y.^2);
subplot(121), contour(Baklava);
subplot(122), mesh(Baklava);
```

*Not: Yansının bulanık veya kişiler tarafından örtülen satırları tamamlanmadı. Yukarıdaki okunabilen örnek, klasördeki temel06.m kaynak dosyasında da bulunuyor.*
