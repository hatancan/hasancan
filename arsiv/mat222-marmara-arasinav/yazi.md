---
baslik: MAT222 Diferansiyel Denklemler: 2005 Ara Sınavı ve Çözümleri (Marmara derlemesi, Faruk Uçar)
ozet: 28 Nisan 2005 tarihli A ve B grubu soruları: Cauchy–Euler denklemleri, Taylor serisi, yakınsaklık yarıçapı ve tekil noktaların sınıflandırılması.
---

Bu yazı, **28 Nisan 2005 Diferansiyel Denklemler II** ara sınavının A ve B gruplarını ve çözümlerini içeriyor. PDF üst verisinde **Faruk Uçar** yazıyor. Aynı yazara ait Marmara Üniversitesi MAT232 belgeleriyle birlikte saklanmış; bu iki sınavın kendi sayfalarında kurum adı bulunmadığından Marmara bağlantısı derleme bağlamına dayanıyor. Orijinal iki PDF yazının sonunda ZIP olarak indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Sınav düzeni

Her iki grupta süre 100 dakika; birinci soru 30, ikinci soru 40, üçüncü soru 30 puan. Kaynaktaki bağımsız değişken t'dir.

## A grubu: Cauchy–Euler denklemi

**Soru:** t²y″ + 5ty′ + 4y = 0, t > 0 denklemini t = eˣ dönüşümüyle çözünüz.

Y(x) = y(eˣ) seçilince y′ = Y′/t ve y″ = (Y″ − Y′)/t² olur. Böylece Y″ + 4Y′ + 4Y = 0 elde edilir. Karakteristik polinom (λ + 2)² olduğundan:

y(t) = C₁t⁻² + C₂t⁻² ln t.

## A grubu: Taylor serisi

**Soru:** (t² − 1)y″ + ty′ − y = 0 denklemini t = 0 çevresinde Taylor serisiyle çözünüz; yakınsaklık yarıçapını bulunuz.

y = Σ_(n=0)^∞ cₙtⁿ yazılır. Katsayıların eşitlenmesiyle c₂ = −c₀/2, c₃ = 0 ve cₙ₊₂ = (n − 1)cₙ/(n + 2) elde edilir.

y(t) = c₀(1 − t²/2 − t⁴/8 − t⁶/16 − …) + c₁t.

Kaynakta sonuç R = 1 olarak veriliyor.

*Not: Kaynak aynı paragrafta seriyi “her t için yakınsak” diye tanımlıyor; bu ifade R = 1 ile çelişir. Polinom olmayan çözümün Taylor serisi |t| < 1 içinde yakınsaktır. n = 5 satırındaki c₅ = (4/7)c₅ yazımında soldaki indis c₇ olmalıdır.*

## A grubu: tekil noktalar

| Denklem | Düzgün tekil nokta | Düzgün olmayan tekil nokta |
|---|---|---|
| t²(t − 5)²y″ + 4ty′ + (t² − 25)y = 0 | t = 0 | t = 5 |
| t²(t + 1)²y″ + (t² − 1)y′ + 2y = 0 | t = −1 | t = 0 |

Kontrol için denklem y″ + p(t)y′ + q(t)y = 0 biçimine getirilir. t₀ çevresinde (t − t₀)p(t) ve (t − t₀)²q(t) incelenir. İlk denklemin t = 0 noktasında limitler 4/25 ve −1; ikinci denklemin t = −1 noktasında −2 ve 2'dir.

## B grubu: Cauchy–Euler denklemi

**Soru:** t²y″ − 3ty′ + 4y = 0, t > 0 denklemini t = eˣ dönüşümüyle çözünüz.

Dönüşüm Y″ − 4Y′ + 4Y = 0 verir. Karakteristik polinom (λ − 2)² ve çözüm:

y(t) = C₁t² + C₂t² ln t.

## B grubu: Taylor serisi

**Soru:** (t² + 1)y″ + ty′ − y = 0 denklemini t = 0 çevresinde Taylor serisiyle çözünüz ve yakınsaklık yarıçapını bulunuz.

c₂ = c₀/2, c₃ = 0, cₙ₊₂ = −(n − 1)cₙ/(n + 2).

Kaynak katsayı dizisi c₄ = −c₀/8, c₆ = c₀/16 ile başlıyor. R = 1 veriliyor.

*Not: B grubunda genel c₂ₖ formülüne yazılan (−1)ᵏ işareti, hemen üstteki c₄ ve c₆ değerleriyle çelişiyor; doğru işaret (−1)ᵏ⁻¹'dir. Buna göre seri c₀(1 + t²/2 − t⁴/8 + t⁶/16 − …) + c₁t olur. “Her t için yakınsak” ifadesi burada da yanlıştır; kompleks tekil noktalar ±i olduğundan Taylor yarıçapı 1'dir. n = 5 satırında soldaki c₅, c₇ olmalıdır.*

## B grubu: tekil noktalar

| Denklem | Düzgün tekil nokta | Düzgün olmayan tekil nokta |
|---|---|---|
| t²(t − 2)²y″ + 5ty′ + (t² − 4)y = 0 | t = 0 | t = 2 |
| (t² − 9)²y″ + (t + 3)y′ + 2y = 0 | t = −3 | t = 3 |

İlk denklemde t = 0 için limitler 5/4 ve −1; ikinci denklemde t = −3 için 1/36 ve 1/18'dir. Euler çözümleri yerine koyma, seri katsayıları ise yineleme bağıntısı üzerinden kontrol edildi.
