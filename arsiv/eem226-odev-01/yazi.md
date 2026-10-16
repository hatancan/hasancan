---
baslik: EEM226 Elektromanyetik Dalga Teorisi I: Ödev 1, Ortogonal Koordinat Sistemleri (El Yazısı)
ozet: Elektromanyetik dersi 1. ödevinin el yazısı çözümü: kartezyen, silindirik ve küresel koordinat sistemleri, birim vektörler, skaler ve vektörel çarpım, diferansiyel uzunluk ve hacim, koordinat dönüşümleri.
---

Bu yazı, Elektromanyetik dersinin 1. ödevinin el yazısıyla hazırlanmış üç sayfalık çözümüdür; sayfalar 3 Ekim 2010'da fotoğraflanmış. İlk sayfanın başlığında "Elektromanyetik 2 – Ödev 1" yazıyor; konu, vektör analizinin temeli olan **ortogonal koordinat sistemleri**: kartezyen, silindirik ve küresel koordinatlar. Aşağıda her sayfanın başlıkları, formülleri ve sonuçları metin olarak verildi; fotoğrafların kendisi arşivde saklanıyor, yayınlanmıyor.

## Sayfa 1: Kartezyen koordinatlar

**Ortogonal koordinat sistemleri — a) Kartezyen koordinatlar**

- x = x₁, y = y₁ ve z = z₁ düzlemleri ancak bir noktada kesişir. Bu noktayı P noktası olarak tanımlarsak P(x₁, y₁, z₁) olarak gösterebiliriz.
- Bu üç koordinat yönünde, birbirine dik **a**ₓ, **a**ᵧ ve **a**_z birim vektörlerine baz vektörler denir. Bu sistemde sağ el kuralı geçerlidir:

```
ax × ay = az
ay × az = ax
az × ax = ay
```

- **a**ₓ · **a**ᵧ = **a**ᵧ · **a**_z = **a**ₓ · **a**_z = 0, çünkü eksenler birbirine diktir (**A** · **B** = |A| |B| cos θ, θ = 90° için 0).
- **a**ₓ · **a**ₓ = **a**ᵧ · **a**ᵧ = **a**_z · **a**_z = 1

P(x₁, y₁, z₁) noktasının konum vektörü, O orijininden P noktasına çizilen vektördür. **a**ₓ, **a**ᵧ ve **a**_z yönlerindeki bileşenleri sırasıyla x₁, y₁ ve z₁'dir. Böylece:

- **OP** = **a**ₓ x₁ + **a**ᵧ y₁ + **a**_z z₁
- Kartezyen koordinatlarda bir vektör: **A** = **a**ₓ Aₓ + **a**ᵧ Aᵧ + **a**_z A_z
- Bir diferansiyel uzunluk: d**l** = **a**ₓ dx + **a**ᵧ dy + **a**_z dz
- Bir diferansiyel hacim: dv = dx dy dz

## Sayfa 2: Skaler ve vektörel çarpım, silindirik koordinatlar

Kartezyen koordinat sisteminde **A** = **a**ₓ Aₓ + **a**ᵧ Aᵧ + **a**_z A_z ve **B** = **a**ₓ Bₓ + **a**ᵧ Bᵧ + **a**_z B_z şeklinde tanımlansın.

**Skaler çarpım:**

**A** · **B** = (**a**ₓ Aₓ + **a**ᵧ Aᵧ + **a**_z A_z) · (**a**ₓ Bₓ + **a**ᵧ Bᵧ + **a**_z B_z) = Aₓ Bₓ + Aᵧ Bᵧ + A_z B_z

**Vektörel çarpım:**

```
        | ax  ay  az |
A × B = | Ax  Ay  Az |
        | Bx  By  Bz |
```

**A** × **B** = **a**ₓ (Aᵧ B_z − A_z Bᵧ) + **a**ᵧ (A_z Bₓ − Aₓ B_z) + **a**_z (Aₓ Bᵧ − Aᵧ Bₓ)

*Not: El yazısında **a**ᵧ bileşeni (Aₓ B_z − A_z Bₓ) olarak yazılmış; determinant açılımında bu terimin işareti ters, doğrusu (A_z Bₓ − Aₓ B_z). Ayrıca sayfada B'nin bileşenleri "bₓ Bₓ + …" diye yazılmış; birim vektörler **a**ₓ, **a**ᵧ, **a**_z olmalı. Yukarıda düzeltilmiş hâlleri verildi.*

**b) Silindirik koordinatlar**

Bu sistemde P noktasını r₁, φ₁ ve z bileşenleriyle hayali bir silindirin yüzeyinde düşünüyoruz: P(r₁, φ₁, z).

- r: radyal uzaklık
- φ: pozitif x ekseniyle yapılan açı

Sağ el kuralı geçerlidir:

```
ar × aφ = az
aφ × az = ar
az × ar = aφ
```

- Silindirik koordinatlarda vektör diferansiyel uzunluk: d**l** = **a**_r dr + **a**_φ r dφ + **a**_z dz
- Diferansiyel hacim: dv = r dr dφ dz

## Sayfa 3: Küresel koordinatlar ve dönüşümler

**Küresel koordinatlar (Soru 3)**

Küresel koordinatlarda bir P noktası üç yüzeyin kesişimi olarak tanımlanır: P(R₁, θ₁, φ₁).

- R = R₁: merkezi orijin olan, yarıçapı R₁ olan kürenin yüzeyi
- θ = θ₁: köşesi orijinde olan, z ekseni ile çakışan, θ₁ açılı dik koni
- φ = φ₁: xz düzlemi ile yapılan açı (yarı düzlem)

Sağ el kuralı geçerlidir:

```
aR × aθ = aφ
aθ × aφ = aR
aφ × aR = aθ
```

- Küresel koordinatlarda diferansiyel hacim: dv = R² sin θ dR dθ dφ
- Küresel koordinatlarda diferansiyel uzaklık: d**l** = **a**_R dR + **a**_θ R dθ + **a**_φ R sin θ dφ

Küresel koordinatlarda bir noktanın konumunun kartezyen koordinatlara dönüştürülmesi:

- x = R sin θ cos φ
- y = R sin θ sin φ
- z = R cos θ

**Soru 2: (x, y, z), (r, φ, z) ve (R, θ, φ) eşitlikleri**

Çizimde P noktası, orijinden uzaklığı R, z ekseniyle yaptığı açı θ olacak şekilde gösterilmiş; xy düzlemine izdüşümü r uzunluğunda ve x ekseniyle φ açısı yapıyor:

- r = R sin θ
- x = r cos φ
- y = r sin φ
- z = R cos θ
