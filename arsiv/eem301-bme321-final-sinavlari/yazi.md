---
baslik: EEM301 Sinyaller ve Sistemler I: BME 321 Signals and Systems Final Sınavları ve Çözümleri (2005, 2006)
ozet: Başkent Üniversitesi BME 321 Signals and Systems dersinin Ocak 2005 ve Ocak 2006 final sınavlarının soruları ve el yazısı çözümleri: doğrusallık, zamanla değişmezlik ve nedensellik, konvolüsyon, seri bağlı sistemlerin dürtü yanıtı, sin³ sinyalinin Fourier serisi, dürtü katarının süzülmesi, frekans yanıtı ve süperpozisyon.
---

Bu yazı, EEM301 Sinyaller ve Sistemler I klasöründeki "BME Sinyal Sınavı" klasöründen derlendi: Başkent Üniversitesi Mühendislik Fakültesi **BME 321 – Signals and Systems** dersinin **13 Ocak 2005** (2004/2005 güz) ve **4 Ocak 2006** (2005/2006 güz) tarihli final sınavları ve el yazısı çözümleri. Sınav kâğıtları ve çözümler fotoğraflanmış sayfalardan metne aktarıldı; fotoğraflar yayınlanmadı, bu yüzden indirilebilir dosya yok. Sınavlar İngilizce; sorular kısaltılarak aktarıldı. Her iki sınav 35 puan üzerinden.

## Final – 4 Ocak 2006

### Soru 1 (9 puan)

Ayrık zamanlı sistem y[n] = 2x[n] − 5x[n − 1] + 2x[n − 2].

1. Sistem doğrusal, zamanla değişmez ve nedensel mi?
1. Frekans yanıtının ifadesini bulun.
1. Genlik yanıtını frekansın fonksiyonu olarak çizin.
1. x₂[n] = 4 + 4 cos(0.5π(n − 1)) girişi için çıkışı bulun (ipucu: doğrusallık ve zamanla değişmezlik).

**Çözüm:** Sistem doğrusal ve zamanla değişmezdir (x[n − n₀] girişi y[n − n₀] verir); yalnız x[n], x[n − 1], x[n − 2]'ye, yani şimdiki ve geçmiş değerlere bağlı olduğundan nedenseldir.

- H(e^(jω)) = Σ b_k e^(−jωk), b_k = {2, −5, 2} ⇒ H(e^(jω)) = 2 − 5e^(−jω) + 2e^(−j2ω) = (2e^(jω) − 5 + 2e^(−jω))e^(−jω) = **(4 cos ω − 5)e^(−jω)**
- |H(e^(jω))| = |4 cos ω − 5|: ω = 0'da 1, ω = ±π'de 9 olan, 2π periyotlu bir eğri
- H(e^(j0)) = −1, H(e^(jπ/2)) = −5e^(−jπ/2) = 5e^(jπ/2)
- y₂[n] = (−1)(4) + 5·4 cos(0.5π(n − 1) + π/2) = **−4 + 20 cos(0.5πn)**

### Soru 2 (8 puan)

Giriş x(t) = u(t) − 2u(t − 4) + u(t − 6) ve verilen üçgen biçimli h(t) (−1 < t < 0'da 1 + t, 0 < t < 1'de 1 − t) için (a) çıkış y(t), (b) y(0), (c) y(t) = 0 olan bölgeler ve noktalar.

**Çözüm:** Önce g(t) = h(t) ∗ u(t) = ∫_{−∞}^{t} h(τ)dτ bulunur: t < −1'de 0, −1 < t < 0'da (t + 1)²/2, 0 < t < 1'de 1/2 + [1/2 − (1 − t)²/2], t > 1'de 1. Doğrusallık ve zamanla değişmezlikten y(t) = g(t) − 2g(t − 4) + g(t − 6); y(0) = g(0) = 1/2.

### Soru 3 (6 + 6 puan)

İki LTI sistem seri bağlı.

- (a) Birinci sistem w(t) = ∫_{−∞}^{t} x(τ)dτ, ikinci sistemin dürtü yanıtı h₂(t) = u(t − 5). **Çözüm:** h₁(t) = u(t), h(t) = u(t) ∗ u(t − 5) = **(t − 5)u(t − 5)** (t < 5'te 0, t ≥ 5'te t − 5).
- (b) Birinci sistem w(t) = dx(t)/dt + 3x(t); toplam dürtü yanıtının h(t) = δ(t) olması için h₂(t) = Ae^(−α(t−t₀))u(t − t₀) biçiminde olması gerektiğini gösterin. **Çözüm:** h(t) = (dδ/dt + 3δ(t)) ∗ e^(αt)u(t) = (3 + α)e^(αt)u(t) + δ(t); h(t) = δ(t) için α = −3, yani **h₂(t) = e^(−3t)u(t)**.

### Soru 4 (7 puan)

"sin-küp" sinyali sin³(3πt)'nin bütün Fourier serisi katsayılarını Fourier integraliyle bulun.

**Çözüm:** Periyot T₀ = 2π/(3π) = 2/3. (a + b)³ açılımıyla

sin³(3πt) = (j/8)e^(j9πt) − (3j/8)e^(j3πt) + (3j/8)e^(−j3πt) − (j/8)e^(−j9πt)

Her terim ayrı ayrı integre edilir; k ≠ ±1, ±3 için integraller sıfırdır. Sonuç: **a₁ = −3j/8, a₋₁ = 3j/8, a₃ = j/8, a₋₃ = −j/8**, diğerleri 0.

### Soru 5 (5 puan)

x(t) = Σ δ(t − 50k) = Σ (1/50)e^(j(2π/50)kt) periyodik dürtü katarı.

1. Temel frekans: **ω₀ = 2π/50 rad/s**.
1. Frekans yanıtı |ω| ≤ π/20'de 1, dışında 0 olan LTI sistemin çıkışı (gerçel ifadeyle): Süzgeç yalnız ω = 0 ve ±2π/50 bileşenlerini geçirir ⇒ **y(t) = (1/50)(1 + 2 cos(2πt/50))**.

## Final – 13 Ocak 2005

### Soru 1 (4.5 puan)

Aşağıdaki sistemlerin doğrusal, zamanla değişmez ve nedensel olup olmadığı:

| Sistem | Doğrusal | Zamanla değişmez | Nedensel |
|---|---|---|---|
| y[n] = e^(x[n]) | Hayır | Evet | Evet |
| y[n] = x[n] cos(0.2πn) | Evet | Hayır | Evet |
| y[n] = −x[n + 1] + x[n] − x[n − 1] | Evet | Evet | Hayır (x[n + 1]'e bağlı) |

### Soru 2

1. w(t) = u(t + 2) − u(t − 2)'yi çizin.
1. y(t) = w(t) ∗ w(t) konvolüsyonunu tanımlayıp çizin.
1. x(t) girişi verilen y(t) çıkışını üreten LTI sistemin dürtü yanıtı h(t)?

**Çözüm:** Konvolüsyon integrali dört basamak terimine ayrılarak

y(t) = (t + 4)u(t + 4) − 2t·u(t) + (t − 4)u(t − 4)

bulunur: −4 ile 4 arasında, tepesi t = 0'da olan bir üçgen. (c)'de çıkış, x(t)'nin 2, 10 ve 18 kadar kaydırılmış ve ölçeklenmiş üç kopyasının toplamı olduğundan **h(t) = δ(t − 2) − δ(t − 10) + ½δ(t − 18)**.

*Not: Çözümdeki çizimde üçgenin tepe değeri 1 olarak işaretlenmiş; dikdörtgenin genişliği 4 olduğundan y(0) = ∫w²(τ)dτ = 4'tür.*

### Soru 3

Blok diyagramla verilen sistem: (a) diferansiyel denklem, (b) frekans yanıtı, (c) dürtü yanıtı. **Çözüm:** Blok diyagramdan denklem d²y/dt² + (5/4)dy/dt + (3/8)y(t) = x(t) biçimine getiriliyor; H(jω) = 1/((jω)² + (5/4)jω + 3/8) = **1/((jω + 1/2)(jω + 3/4))**, ardından kısmi kesirlerle dürtü yanıtına geçiliyor.

### Soru 4

H(e^(jω)) = (1 + e^(−jω))(1 − e^(jπ/3)e^(−jω))(1 − e^(−jπ/3)e^(−jω)).

1. Fark denklemi: e^(jπ/3) + e^(−jπ/3) = 2 cos(π/3) = 1 olduğundan H(e^(jω)) = (1 + e^(−jω))(1 − e^(−jω) + e^(−j2ω)) = 1 + e^(−j3ω) ⇒ **y[n] = x[n] + x[n − 3]**.
1. Dürtü yanıtı: **h[n] = δ[n] + δ[n − 3]**.
1. x[n] = Ae^(jφ)e^(jωn) girişi için y[n] = 0 olan frekanslar H'nin sıfırlarıdır: **ω = π, ω = −π/3, ω = π/3**.
1. x[n] = 3 + δ[n − 2] + cos(0.5πn + π/4) için: H(e^(j0)) = 2, H(e^(j0.5π)) = 1 + e^(−j1.5π) = 1 + j = √2e^(jπ/4). Süperpozisyonla y[n] = 3·2 + (δ[n − 2] + δ[n − 5]) + √2 cos(0.5πn + π/4 + π/4) = **6 + δ[n − 2] + δ[n − 5] + √2 cos(0.5πn + π/2)**.

### Soru 5

Şekildeki x(t) sinyali dikdörtgen parça x₁(t) ve üçgen parça x₂(t)'nin toplamı olarak yazılıp türev ve zaman kaydırma özellikleriyle spektrumu çıkarılması isteniyor (δ(t) ⟷ 1 kullanılarak). Fotoğraflarda bu sorunun çözümü yok.
