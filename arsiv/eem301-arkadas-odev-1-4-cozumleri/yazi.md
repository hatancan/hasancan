---
baslik: EEM301 Sinyaller ve Sistemler I: Arkadaşların Ödev 1 ve Ödev 4 Çözümleri (Konvolüsyon Toplamı, Sistem Özellikleri, Diferansiyel Denklemler)
ozet: EEM301 Sinyaller ve Sistemler I ödevlerinin arkadaş çözümleri: x²[n − 2] sisteminin doğrusallığı ve zamanla değişmezliği, ayrık sinyal dönüşümleri, αⁿu[n] ∗ αⁿu[n], (−1/2)ⁿu[n − 4] ∗ 4ⁿu[2 − n], 2ⁿu[−n] ∗ u[n] konvolüsyonları ve ilk koşullu homojen diferansiyel denklemler.
---

Bu yazı, EEM301 Sinyaller ve Sistemler I klasöründeki "ödev" klasöründe duran, arkadaşların el yazısı ödev çözümlerini bir araya getiriyor: Oppenheim & Willsky problemlerinden oluşan bir **Ödev 1** ve 2013 yazına ait bir **Ödev 4**. Kişisel bilgiler çıkarıldı. Çözümler fotoğraflanmış sayfalardan metne aktarıldı; fotoğraflar yayınlanmadı, bu yüzden indirilebilir dosya yok.

## Ödev 1

### Doğrusallık ve zamanla değişmezlik: y[n] = x²[n − 2]

x₃[n] = a·x₁[n] + b·x₂[n] için y₃[n] = (a·x₁[n − 2] + b·x₂[n − 2])² = a²x₁²[n − 2] + 2ab·x₁[n − 2]x₂[n − 2] + b²x₂²[n − 2]; bu a·y₁[n] + b·y₂[n]'ye eşit olmadığından sistem **doğrusal değildir**. x₂[n] = x₁[n − n₀] için y₂[n] = x₁²[n − 2 − n₀] = y₁[n − n₀] olduğundan sistem **zamanla değişmezdir**.

### Ayrık sinyal dönüşümleri

Kitaptaki bir ayrık zamanlı sinyal için x[n − 4] (sağa 4 kaydırma) ve x[3 − n] = x[−(n − 3)] (önce x[−n] ile ters çevirip sonra 3 sağa kaydırma) çizilmiş.

### Konvolüsyon: x[n] = h[n] = αⁿu[n]

y[n] = Σ_{k=0}^{n} αᵏ α^(n−k) = αⁿ Σ_{k=0}^{n} 1 = **αⁿ(n + 1)u[n]**.

### Konvolüsyon: x[n] = (−1/2)ⁿu[n − 4], h[n] = 4ⁿu[2 − n]

y[n] = Σ_{k ≥ max(4, n−2)} (−1/2)ᵏ 4^(n−k) = 4ⁿ Σ (−1/8)ᵏ:

- n ≤ 6 (n − 2 ≤ 4): y[n] = **(8/9)(−1/8)⁴·4ⁿ**
- n > 6: alt sınır n − 2 olur.

*Not: Kâğıtta n > 6 için sonuç (8/9)(−1/2)ⁿ yazılmış. 4ⁿ·(8/9)(−1/8)^(n−2) = (8/9)·64·(−1/2)ⁿ olduğundan doğrusu **(512/9)(−1/2)ⁿ**'dir. Kontrol: n = 7 için doğrudan toplam 4⁷·(8/9)(−1/8)⁵ = −4/9 verir.*

Ayrıca kısa bir dikdörtgen dizinin h[n] ile konvolüsyonu, h[n]'nin kaydırılmış kopyalarının toplamı (h[n] + h[n − 1] + h[n − 2] + …) olarak bulunup çizilmiş.

### Homojen diferansiyel denklemler

**(a)** d³y/dt³ + d²y/dt² − dy/dt − y(t) = 0, y(0) = 1, y′(0) = 1, y″(0) = −2.

- (p³ + p² − p − 1) = (p + 1)(p² − 1) ⇒ kökler 1, −1, −1
- y(t) = Ae^t + Be^(−t) + Cte^(−t)
- A + B = 1, A − B + C = 1, A + B − 2C = −2 ⇒ C = 3/2, B = 3/4, A = 1/4
- **y(t) = ¼e^t + ¾e^(−t) + (3/2)te^(−t)**

**(b)** d²y/dt² + 2 dy/dt + 5y(t) = 0, y(0) = 1, y′(0) = 1.

- p² + 2p + 5 = 0 ⇒ p₁,₂ = −1 ± 2j
- y(t) = Ae^(−t) cos 2t + Be^(−t) sin 2t; y(0) = A = 1, y′(0) = −A + 2B = 1 ⇒ B = 1
- **y(t) = e^(−t)[cos 2t + sin 2t]**

## Ödev 4: x[n] = 2ⁿu[−n], h[n] = u[n]

y[n] = Σ x[k]h[n − k] = Σ_{k ≤ min(n, 0)} 2ᵏ.

- n ≥ 0: y[n] = Σ_{k=−∞}^{0} 2ᵏ = 1 + 1/2 + 1/4 + … = 1/(1 − 1/2) = **2**
- n < 0: y[n] = Σ_{k=−∞}^{n} 2ᵏ = **2^(n+1)** (örneğin y[−1] = 1, y[−2] = 1/2)

Çözümlerden biri bu sonuca geometrik seri formülüyle ulaşıyor. Aynı klasördeki ilk deneme sayfalarında x[k]'nın k > 0 için de sıfırdan farklı olduğu varsayılıp y[0] = 1, y[1] = 3, y[2] = 7, y[3] = 15 gibi değerler bulunmuş; x[n] = 2ⁿu[−n] yalnız n ≤ 0 için sıfırdan farklı olduğundan bu deneme hatalıdır, sonraki sayfalarda düzeltilmiş.
