---
baslik: EEM308 Sinyaller ve Sistemler II: 2005 Ara Sınavı ve 2009 Kısa Sınav 3 Soruları (EEM 302)
ozet: EEM 302 Sinyaller ve Sistemler II dersinin 2004-2005 bahar ara sınavı (sinüzoidal girişe kalıcı durum yanıtı, kararlılık ve minimum faz, fark denkleminin birim basamak yanıtı, konvolüsyonla z-dönüşümü) ve 22 Mayıs 2009 kısa sınav 3 sorusu (tüm geçiren sistem).
---

Bu yazı, Başkent Üniversitesi **EEM 302 Sinyaller ve Sistemler II** dersinin (ders daha sonra EEM 308 koduyla verildi) iki eski sınavını aktarıyor: **Öğr. Gör. Mustafa Doğan**'ın hazırladığı **2004-2005 bahar dönemi ara sınavı** (Midterm) ve **22 Mayıs 2009** tarihli **kısa sınav 3**'ün tahtaya yazılmış sorusu. İkisi de fotoğraflanmış sayfalardan metne aktarıldı; fotoğrafların kendisi arşivde saklanıyor, yayınlanmıyor. Ara sınav fotoğrafında kâğıdın üst kısmının bir bölümü yapışkan notla kapalı; boş bir soru kâğıdı olduğundan ad veya numara içermiyor.

## 2004-2005 bahar ara sınavı

Başlık: *Başkent Üniversitesi Elektrik-Elektronik Mühendisliği Bölümü, EEM 302 Sinyaller ve Sistemler II, Midterm — Öğr. Gör. Mustafa Doğan*. Kurallar:

1. Sınavda kendi el yazınızla hazırlanmış bir A4 formül kâğıdına izin verilmiştir. Fotokopi olduğu anlaşılan formül kâğıtları alınacaktır.
1. Herkes kendi hesap makinesini kullanacaktır; ortak kullanıma kesinlikle izin verilmeyecektir.
1. Kopya çeken öğrenci "Başkent Üniversitesi Disiplin Yönetmeliği"ne göre cezalandırılacaktır.

Puanlar: Soru 1: 20, Soru 2: 20, Soru 3: 30, Soru 4: 30; toplam 100.

### 1. Steady-state response to sinusoidal inputs (20 puan)

The transfer function H(s) of an LTI system is given below. Find the steady-state response to the following input:

x(t) = 3 [cos(4t) − √3 sin(4t)]

x(t) → **H(s) = 1/(s² + 4s + 8)** → y_ss(t) = ?

### 2. Kararlılık ve minimum faz (20 puan)

Which of the following causal LTI systems are **stable**? Which of them are **minimum-phase**? WHY? Please, explain clearly.

- a) H(s) = (s + 10)(10s + 1) / ((0,01s + 1)(s² + s + 1))
- b) H(s) = (10s² + 5s + 10) / (0,1s + 1)
- c) H(z) = (1 + 2z⁻²) / (1 − 0,5z⁻¹)²
- d) H(z) = 1 / ((1 − 0,25z⁻¹)(1 + 0,75z⁻¹))
- e) H(z) = (1 − 2z⁻¹) / (1 + 0,5z⁻¹)
- f) H(z) = z⁻¹ (1 − 0,3z⁻¹) / (1 − 0,25z⁻²)

*Not: c, d ve f şıklarındaki z'nin üsleri fotoğrafta bulanık; yukarıdaki okuma en olası olanıdır.*

### 3. Unit-step response of discrete-time LTI systems (30 puan)

The difference equation of a causal LTI system is:

2y[n] − 2y[n−1] + y[n−2] = x[n]

- a) H(z) = ?
- b) Find the output y[n] for input x[n] = u[n].

### 4. Konvolüsyon ve z-dönüşümü (30 puan)

The transfer function H(z) of a discrete-time LTI system is given below. Find the output y[n] for input x[n] = (2/3)ⁿ for all n. **Hint:** Use convolution sum in discrete-time and then z-transform properties. Do **not** evaluate X(z)!

x[n] → **H(z) = (1 − 0,25z⁻¹) / (1 + (1/3)z⁻¹)** → y[n] = ?

### Kısa çözüm notları

*Not: Sınavın cevap anahtarı yoktu; aşağıdaki sonuçları biz hesapladık.*

- **Soru 1:** x(t) = 3[cos 4t − √3 sin 4t] = 6 cos(4t + 60°). H(j4) = 1/(8 − 16 + j16) = 1/(−8 + j16); |H(j4)| = 1/√320 ≈ 0,0559, ∠H(j4) = −(180° − 63,43°) = −116,57°. Dolayısıyla y_ss(t) = (6/√320) cos(4t + 60° − 116,57°) ≈ **0,335 cos(4t − 56,57°)**.
- **Soru 3:** H(z) = 1/(2 − 2z⁻¹ + z⁻²) = 0,5 / (1 − z⁻¹ + 0,5z⁻²); kutuplar z = 0,5 ± j0,5 = (1/√2)e^(±jπ/4), birim çemberin içinde (sistem kararlı). Birim basamak girişinde kalıcı değer H(1) = 1/(2 − 2 + 1) = 1.
- **Soru 4:** (2/3)ⁿ bir özfonksiyondur: y[n] = H(z)|_{z=2/3} · (2/3)ⁿ = ((1 − 0,375)/(1 + 0,5)) (2/3)ⁿ = **(5/12)(2/3)ⁿ**.

## 22 Mayıs 2009 kısa sınav 3

Tahtaya yazılan soru:

H(z) = (z⁻¹ − 0,2) / (1 − 0,2z⁻¹)

|H(e^{jω})| = 1 olduğunu gösterin.

*Not: Kısa çözüm: z = e^{jω} için pay e^{−jω} − 0,2 = e^{−jω}(1 − 0,2e^{jω}) olur. |e^{−jω}| = 1 ve 1 − 0,2e^{jω} ile payda 1 − 0,2e^{−jω} birbirinin karmaşık eşleniği olduğundan genlikleri eşittir; dolayısıyla |H(e^{jω})| = 1. Sistem, kutbu z = 0,2'de ve sıfırı z = 5'te (kutbun 1/p yansıması) olan birinci dereceden tüm geçiren (all-pass) bir süzgeçtir.*
