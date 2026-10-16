---
baslik: EEM224 Elektromanyetik I: Alan Kavramı, Gradyant, Diverjans, Bukle ve Stokes–Diverjans Teoremleri (El Yazısı Ders Notu)
ozet: EEM224 Elektromanyetik I el yazısı ders notu: skaler ve vektörel alan, nabla operatörü ve birimi, gradyant, diverjans ve bukle (curl), solenoidal ve irrotasyonel alanlar, diverjans teoremi, Stokes teoremi, iki sıfır özdeşliği ve Helmholtz teoremi.
---

Bu yazı, Başkent Üniversitesi **EEM224 Elektromanyetik I** dersine ait el yazısı ders notlarının iki bölümünü bir araya getiriyor: **"Alan Kavramı – Gradyant – Diverjans – Bukle"** (3 sayfa) ve **"Alanların Sınıflandırılması – Stokes ve Diverjans Teoremleri"** (3 sayfa). Notlarda hazırlayanın adı ve tarih yazmıyor. Notların içeriği metne döküldü; taranmış orijinal PDF'ler yazının sonunda ZIP olarak indirilebilir.

## Alan (field) kavramı

**Alan:** uzamsal bir dağılım; bir başka deyişle "uzay koordinatlarına" bağımlı bir fonksiyon.

- g = f(x, y, z), x = x₀, y = y₀, z = z₀ noktasında skaler bir değerdir; **f skaler alandır** (*scalar field*). Örneğin bir hacimdeki sıcaklık fonksiyonu.
- Ḡ = F̄(x, y, z), aynı noktada vektörel bir değerdir; **F̄ vektörel alandır** (*vector field*). Örneğin bir hacimdeki rüzgâr fonksiyonu.

Bir alan statik olabileceği gibi zaman bağımlı da olabilir: f(x, y, z; t) zaman bağımlı skaler alan, F̄(x, y, z; t) zaman bağımlı vektörel alandır.

**Statik alan:** konuma göre değişiklik gösterebilir, ancak zamana göre değişiklik göstermez.

Vektörel bir alanın her bir bileşeninin şiddeti bir skaler alandır:

F̄(x, y, z) = â_x f_x(x, y, z) + â_y f_y(x, y, z) + â_z f_z(x, y, z)

Burada f_x, f_y, f_z sırasıyla x, y ve z yönündeki bileşenlerin şiddetleridir (skaler alanlar).

**Önemli not:** x yönündeki bileşen sadece x'e bağlı bir fonksiyon olmak zorunda değildir. Bu örnekte olduğu gibi x, y ve z'ye bağlı bir fonksiyon olabilir.

## Del, delta veya nabla operatörü

Nabla operatörü (∇ ile gösterilir), Kartezyen koordinatlarda şu şekilde ifade edilen vektörel bir operatördür:

∇ = â_x ∂/∂x + â_y ∂/∂y + â_z ∂/∂z

**Soru: ∇'nın birimi nedir?** Tanıma bakıldığında ∇ operatörünün x, y ve z'ye göre türev terimleri içerdiği görülmektedir. x, y, z uzunluk değişkenleri olduğundan birimleri "metre" olarak ifade edilebilir. Dolayısıyla x, y, z'ye göre türev almak aslında "metre"ye bölmek demektir. Bu nedenle ∇ operatörünün birimi **1/metre**'dir. (Genel olarak: bir değişkene göre türev almak, o değişkenin birimine bölmek demektir.)

## Skaler bir alanın gradyantı

Gradyant, skaler bir alanın değişimi yönündeki vektörel bir alandır.

Örneğin bir bölgedeki sıcaklık fonksiyonunu ele alalım: T(x, y, z). Sabit yükseklikte sıcaklık sabit olsun, ancak yükseklik (z) arttıkça sıcaklık artıyor olsun. Bu durumda sıcaklık fonksiyonunun gradyantı â_z yönünde bir vektörel alan olacaktır.

Matematiksel olarak (Kartezyen koordinatlarda) bir skaler alanın gradyantı:

∇f(x, y, z) = â_x ∂f/∂x + â_y ∂f/∂y + â_z ∂f/∂z

Sonuç vektöreldir. ∇ (vektör) ile f (skaler) arasına, aynen bir vektör ile bir skalerin çarpımında olduğu gibi, hiçbir işaret konulmaz.

## Vektörel bir alanın diverjansı

Vektörel bir alanın diverjansı, söz konusu vektörel alanın her bir bileşeninin kendi yönünde değişimi olup olmadığını belirten bir ölçüttür. Ā(x, y, z) = â_x A_x(x, y, z) + â_y A_y(x, y, z) + â_z A_z(x, y, z) olsun:

∇ · Ā = (â_x ∂/∂x + â_y ∂/∂y + â_z ∂/∂z) · (â_x A_x + â_y A_y + â_z A_z) = ∂A_x/∂x + ∂A_y/∂y + ∂A_z/∂z

Terimler sırasıyla x yönündeki bileşenin x yönündeki değişimi, y yönündeki bileşenin y yönündeki değişimi ve z yönündeki bileşenin z yönündeki değişimidir. ∇ (vektör) ile Ā (vektör) arasında skaler çarpım vardır; **sonuç skalerdir**.

## Vektörel bir alanın buklesi

Vektörel bir alanın buklesi, söz konusu vektörel alanın rotasyonel bir değişim içerisinde olup olmadığını belirten bir ölçüttür. Kartezyen koordinatlarda:

∇ × Ā = (â_x ∂/∂x + â_y ∂/∂y + â_z ∂/∂z) × (â_x A_x + â_y A_y + â_z A_z)

```
        | â_x    â_y    â_z  |
∇ × Ā = | ∂/∂x   ∂/∂y   ∂/∂z |
        | A_x    A_y    A_z  |
```

∇ (vektör) ile Ā (vektör) arasında vektörel çarpım vardır; **sonuç vektöreldir**.

## Vektörel alanların diverjans ve buklelerine göre sınıflandırılması

- Diverjansı 0'a eşit olan bir vektörel alan **"solenoidal"** olarak adlandırılır: ∇ · Ā(x, y, z) = 0 ise Ā(x, y, z) solenoidal bir alandır.
- Buklesi 0'a eşit olan bir vektörel alan **"irrotasyonel"** veya **"konservatif"** olarak adlandırılır: ∇ × Ā(x, y, z) = 0 ise Ā(x, y, z) irrotasyonel veya konservatif bir alandır.

Not: Bazı kaynaklarda bukle (∇×) operatörü "rotasyonel" olarak da anılmaktadır. Buklesi 0 olan alanlara bu nedenle "irrotasyonel", yani "rotasyonelsiz" adı verilmektedir.

## Diverjans teoremi

v bir hacim, S de v hacmini çevreleyen kapalı yüzey olsun. Herhangi bir Ā(x, y, z) vektörel alanı için:

∫_v (∇ · Ā) dv = ∮_S Ā · ds̄

Yani Ā(x, y, z)'nin kapalı S yüzeyi üzerinde oluşturduğu toplam akı, ∇ · Ā(x, y, z)'nin v üzerindeki hacim integrali ile bulunabilir.

Kolay hatırlamak için: sol tarafta ∇ · Ā skaler alan, dv skalerdir; hacim integralinde operandlar skaler olmalı. Sağ tarafta Ā vektörel alan, ds̄ vektördür ve aralarında skaler çarpım vardır; yüzey integralinde operandlar vektörel olmalı.

**Birimler cinsinden düşünürsek** (Ā'nın birimi "Kappa" olsun): sol tarafta ∇ · Ā'nın birimi Kappa/m, dv'nin birimi m³, toplam Kappa·m². Sağ tarafta Ā Kappa, ds̄ m², toplam yine Kappa·m². Sol taraftaki terimde ∇'dan ötürü fazladan bir türev terimi var, ancak 3 katlı integral var; sağ taraftaki terimde 2 katlı integral var.

## Stokes teoremi

S bir yüzey, C de S yüzeyini çevreleyen kapalı kontur olsun. Herhangi bir Ā(x, y, z) vektörel alanı için:

∫_S (∇ × Ā) · ds̄ = ∮_C Ā · dl̄

Yani kapalı bir C konturu üzerinde ilerleme sonucu Ā(x, y, z)'ye karşı yapılan toplam iş, ∇ × Ā(x, y, z)'nin S üzerinde oluşturduğu akıya eşittir.

Kolay hatırlamak için (Ā'nın birimi Kappa olsun): sol tarafta ∇ × Ā Kappa/m, ds̄ m², toplam Kappa·m; sağ tarafta Ā Kappa, dl̄ m, toplam Kappa·m. Sol terimde ∇'dan ötürü fazladan bir türev terimi var, ancak 2 katlı integral var; sağ terimde tek katlı integral var.

## İki "0" eşitliği

**1. Skaler bir alanın gradyantının buklesi 0'dır.** f(x, y, z) bir skaler alan olsun:

∇ × (∇f(x, y, z)) = 0

Dolayısıyla buklesi 0 olan bir vektörel alan, bir skaler alanın gradyantı olarak ifade edilebilir. Yani ∇ × Ā(x, y, z) = 0 ise Ā(x, y, z) = ∇f(x, y, z) koşulunu sağlayan bir f(x, y, z) skaler alanı vardır.

**2. Vektörel bir alanın buklesinin diverjansı 0'dır.** Ā(x, y, z) bir vektörel alan olsun:

∇ · (∇ × Ā(x, y, z)) = 0

Dolayısıyla diverjansı 0 olan bir vektörel alan, başka bir vektörel alanın buklesi olarak ifade edilebilir. Yani ∇ · B̄(x, y, z) = 0 ise B̄(x, y, z) = ∇ × Ā(x, y, z) koşulunu sağlayan bir Ā(x, y, z) vektörel alanı vardır.

## Helmholtz teoremi

(i) ∇ × Ā(x, y, z) ve (ii) ∇ · Ā(x, y, z) her yerde biliniyorsa Ā(x, y, z) de her yerde hesaplanabilir.

Bir başka deyişle, bir vektörel alanın buklesini ve diverjansını uzayın her yerinde tanımlamak, söz konusu vektörel alanın kendisini tanımlamaya eşdeğerdir.
