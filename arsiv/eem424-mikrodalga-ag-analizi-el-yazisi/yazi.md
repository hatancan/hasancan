---
baslik: EEM424 Mikrodalga Kuramı: Mikrodalga Ağ Analizi Ders Notları (Z, Y, S ve ABCD Matrisleri, 3 dB Zayıflatıcı Örneği)
ozet: EEM424 dersinden el yazısı notların metne aktarımı: empedans ve admitans matrisleri, kayıpsız ağlar, saçılma (S) matrisi, 8,56 ohm - 141,8 ohm - 8,56 ohm T tipi 3 dB zayıflatıcı örneği ve iletim (ABCD) matrisi.
---

Bu yazı, Mayıs 2015'te **EEM424 Mikrodalga Kuramı** dersinde (Prof. Dr. S. Gökhun Tanyer, konu: *mikrodalga ağ analizi*) tuttuğum 19 sayfalık el yazısı notun metne aktarılmış hâlidir. Notlar ağırlıkla İngilizce yazılmış; açıklamalar burada Türkçeleştirildi. Fotoğraflanmış sayfalar yayımlanmamıştır.

## 1. Empedans matrisi: V = Z·I

V = [V1, V2, …]ᵀ ve I = [I1, I2, …]ᵀ vektörleri ile V = Z·I (ve I = Y·V).

**Soru:** Kaynak olarak yalnızca I_j verilmiş, diğer kapılarda kaynak yok (I_k = 0, k ≠ j). Gözlem V_i'dir:

Z_ij = V_i / I_j |_{I_k = 0, k ≠ j}   (kaynak: I_j, gözlem: V_i)

**Örnek (T ağı).** Seri kollarda Z_A ve Z_B, ortak (paralel) kolda Z_C bulunan iki kapılı ağ için:
- Z11 = V1/I1 |_{I2=0} = Z_A + Z_C,
- Z22 = Z_B + Z_C,
- Z21 = V2/I1 |_{I2=0}: V2 = I1·Z_C ⇒ Z21 = Z_C (aynı sonuç V2 = V1·Z_C/(Z_B + Z_C) ve I1 = V1/(Z_A + Z_C) ile de bulunur),
- Z12 = V1/I2 |_{I1=0} = Z_C.

Dolayısıyla Z12 = Z21: **karşılıklı (reciprocal) ağ**; benzer biçimde Y_ij = Y_ji. Matris biçiminde:

[V1; V2] = [[Z_A + Z_C, Z_C]; [Z_C, Z_B + Z_C]] · [I1; I2]

**Kayıpsız ağ:** Re{Z_mn} = 0 (tüm m, n için); yani Z_ij'ler tamamen sanaldır.

## 2. Admitans matrisi

Y_ij = I_i / V_j |_{V_k = 0, k ≠ j} (kaynak/giriş: V_j, gözlem: I_i). Örnek: aynı T ağında Y12 = I1/V2 |_{V1=0}: I1 = V2 · (Z_A ∥ Z_C)/(Z_B + (Z_A ∥ Z_C)); buradan Y12 = (Z_A ∥ Z_C)/(Z_B + (Z_A ∥ Z_C)) (defterde bu biçimde yazılmıştır; birim açısından bu ifadenin bir admitansa karşılık gelmesi için ek bir 1/Z çarpanı gerekir). Z ve Y matrislerinin ilişkisi, [Y] = [Z]⁻¹, ödev olarak bırakılmıştır.

## 3. Saçılma (scattering) matrisi

[V⁻] = S·[V⁺]: gözlem V_i⁻ (giden dalga), giriş V_j⁺ (gelen dalga):

S_ij = V_i⁻ / V_j⁺ |_{V_k⁺ = 0, k ≠ j}

*Soru:* V_k⁺ = 0 (k ≠ j) nasıl sağlanır? *Cevap:* k ≠ j olan kapılara **uyumlu yük (matched load)** bağlayarak.

### Örnek: T tipi zayıflatıcı (R_A, R_B, R_C, 50 Ω hat)

Kapı 1 ile 2 arasında R_A (seri), R_B (seri) ve ortada R_C (paralel) vardır; kapılara bağlanan hat 50 Ω'dur.

- **S11** = V1⁻/V1⁺ |_{V2⁺=0}: 2. kapıda 50 Ω yük varken giriş empedansı Z_in^(1) = R_A + R_C ∥ (R_B + 50) = R_A + R_C(R_B + 50)/(R_C + R_B + 50). S11 = Γ^(1) = (Z_in^(1) − Z0)/(Z_in^(1) + Z0). Z_in^(1) = 50 Ω ise **S11 = 0**.
- Verilen değerler: **R_A = R_B = 8,56 Ω, R_C = 141,8 Ω**; bu değerlerde Z_in = 8,56 + 141,8 ∥ 58,56 = 8,56 + 41,44 ≈ 50 Ω olur, yani S11 = 0 (simetriden S22 = 0).
- **S12 = ?** S12 = V1⁻/V2⁺ |_{V1⁺=0}; simetri (karşılıklı ağ) nedeniyle S12 = S21.
- **S21** = V2⁻/V1⁺ |_{V2⁺=0}. S11 = S22 = 0 ve 2. kapı uyumlu yükle sonlandırılmış olduğundan V1 = V1⁺ (V1⁻ = 0) ve V2 = V2⁻ (V2⁺ = 0). Bölücü ilişkisiyle:

V2⁻ = V2 = V1 · [R_C ∥ (R_B + 50) / (R_A + R_C ∥ (R_B + 50))] · [50/(50 + R_B)]

Sayısal değerlerle = V1⁺ · [141,8 ∥ (8,56 + 50) / (8,56 + 141,8 ∥ (8,56 + 50))] · [50/(50 + 8,56)] = **0,707·V1⁺** ⇒ **S21 = S12 = 0,707**.

**Güç hesabı.** Yalnız V1⁺ girişi için P_in = ½·|V1⁺|²/Z0 ve P_out = ½·|V2⁻|²/Z0, V2⁻ = S21·V1⁺ olduğundan P_out = ½·S21²·|V1⁺|²/Z0. Buradan

P_out / P_in = S21² = 1/2 ⇒ **S21 = −3 dB**.

Yani bu ağ bir **3 dB zayıflatıcıdır (pad)**: giriş gücünün yarısı çıkışa iletilir, her iki kapıda da uyumludur.

## 4. İletim (ABCD) matrisi

İki kapılı ağ için: V1 = A·V2 + B·I2 ve I1 = C·V2 + D·I2, yani [V1; I1] = [[A, B]; [C, D]] · [V2; I2].

**Soru:** 1–2–3 şeklinde ardışık iki ağ bağlanırsa 1 ile 3 arasındaki ilişki nedir? Cevap: [V1; I1] = M1·[V2; I2] ve [V2; I2] = M2·[V3; I3] olduğundan **[V1; I1] = M1·M2·[V3; I3]**: ağların kaskat (zincir) bağlantısında ABCD matrisleri çarpılır.

**Örnekler.**
- *Seri empedans Z:* A için I2 = 0 (açık devre): V1 = V2 ⇒ A = 1. B için V2 = 0 (kısa devre): V1 = Z·I2 ⇒ B = Z. C için I2 = 0: I1 = 0 ⇒ C = 0. D için V2 = 0: I1 = I2 ⇒ D = 1. Sonuç: [[1, Z], [0, 1]].
- *Ödev:* paralel admitans Y için ABCD matrisi.
- *Ödev:* uzunluğu ℓ, karakteristik empedansı Z0 ve yayılma sabiti β olan iletim hattı parçasının ABCD matrisi.

*Not: El yazısında Y matrisi örneğinin formülleri kısaltılmış yazıldı; yukarıdaki Z ve Y bağıntıları ders kitabındaki standart tanımlara göre yeniden düzenlenmiştir.*
