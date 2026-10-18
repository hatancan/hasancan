---
baslik: EEM322 Denetim Sistemleri: Ek Defter Notları: Modelleme, Laplace ve Ayrık Zaman Durum Denklemleri
ozet: Fotoğraflardan metne aktarılan modelleme ve Laplace notları; durum uzayı çözüm taslağı, ayrık zaman yanıtı ve erişilebilirlik özeti.
---

EEM322 arşivindeki defter, çözüm kâğıdı ve tahta kayıtlarından kalan ek başlıklar **fotoğraflanmış sayfalardan metne aktarıldı**. Notları hazırlayan öğrenci adları belirtilmedi; belgelerde ortak bir ders tarihi yok. Arşivdeki 9 Nisan 2015 kayıt tarihi kullanıldı. Bu yazı yalnız metindir; fotoğraflar indirmeye sunulmadı.

## Sistem ve modelleme

Bir sistem giriş–sistem–çıkış ilişkisiyle gösterilir. Sistemler bir araya geldiğinde blok diyagramı oluşur. Defterde potansiyometre için giriş ve çıkış gerilimi; türev alıcı için **y = dx/dt** örnekleri çizilmiş.

Sistemler doğrusal/doğrusal olmayan, dinamik/statik, zamanla değişen/değişmeyen ve sürekli/ayrık zamanlı olarak sınıflandırılır. Model kurarken parametrelerle değişkenler ayrılır; elektriksel sistemde Kirchhoff yasaları, mekanik sistemde fiziksel kuvvet denklemleri kullanılır.

RL devresi için V_L + V_R = E, yani **L di/dt + Ri = E** yazılmış. RLC örneğinde:

L di/dt + Ri + (1/C)∫i dt = E

Sabit E için türev alınarak **L d²i/dt² + R di/dt + i/C = 0** elde edilir. Sayfanın altındaki süspansiyon modeli yalnız kütle ve sönüm terimleriyle başlanmış, tamamlanmamıştır.

## Karmaşık değişken ve Laplace dönüşümü

Defterde s = σ + jω, j = √(−1) ve F(s) = F_x + jF_y yazılır. Laplace dönüşümünün amacı diferansiyel denklemleri cebirsel ilişkilere dönüştürmektir; zaman yanıtına dönmek için ters Laplace kullanılır.

Giriş R(s), transfer fonksiyonu G(s), çıkış C(s) ile **C(s) = R(s)G(s)**. Genel transfer fonksiyonu pay ve payda polinomlarının oranı olarak gösterilmiş.

## Bir devrenin durum uzayı çözüm taslağı

Çözüm kâğıdında durumlar x₁ ve x₂, u girişi ve r, c, ℓ parametreleri kullanılıyor. Kaynağın başlangıç devre çizimi bu sayfada bulunmuyor; aşağıdaki bilgiler yalnız çözümde yazılan denklemlerdir:

- i_c = cẋ₁
- v_ℓ = ℓẋ₂
- u = rcẋ₁ + x₁ = ℓẋ₂ + rx₂
- y = x₂ + cẋ₁

Buna karşılık:

A = [−1/(rc) 0; 0 −r/ℓ], B = [1/(rc); 1/ℓ], C = [−1/r 1]

Kaynak y = Cx + Du yazımını kullanır. “Minimal sistem = hem observable hem controllable” tanımının ardından gözlenebilirlik O = [C; CA] ve denetlenebilirlik E = [B AB] matrisleri kurulmuş.

*Not: Kâğıtta matris kerteleri “2 ≤ n” olarak yazıldıktan sonra “sistem minimal değil” sonucuna gidilmiş. İki durumlu sistemde her iki kerte 2 ise sistem minimaldir. Yazılan A, B ve C için r, c, ℓ sıfırdan farklı olmak koşuluyla ℓ ≠ r²c olduğunda iki matris de tam kertelidir; ℓ = r²c özel durumu ayrıca incelenmelidir.*

Transfer fonksiyonu adımı kaynakta **H(s) = C(sI − A)⁻¹B** ile başlatılır. Diyagonal A nedeniyle rezolventin köşegen elemanları 1/[s + 1/(rc)] ve 1/(s + r/ℓ) olur.

*Not: Aynı sayfanın y = x₂ + cẋ₁ denkleminden y = −x₁/r + x₂ + u/r çıkar. Bu nedenle doğrudan geçiş D = 1/r’dir; tek çıkış için skaler olmalıdır. Kaynağın transfer fonksiyonu hesabı bu +D terimini atlamıştır. Sayfanın altındaki sadeleştirmeler doğrulanmış bir sonuç olarak kullanılmamalıdır.*

## Ayrık zamanda durum denkleminin çözümü

x(k + 1) = Ax(k) + Bu(k), y(k) = Cx(k) + Du(k).

Ardışık yerine koyma:

- x(1) = Ax(0) + Bu(0)
- x(2) = A²x(0) + ABu(0) + Bu(1)
- x(3) = A³x(0) + A²Bu(0) + ABu(1) + Bu(2)

Genel sonuç:

**x(k) = Aᵏx(0) + Σ_(j=0)^(k−1) A^(k−1−j)Bu(j)**

Aᵏ ayrık zaman durum geçiş matrisidir. D = 0 alındığında:

**y(k) = CAᵏx(0) + Σ_(j=0)^(k−1) CA^(k−1−j)Bu(j)**

İlk terim sıfır giriş yanıtı, toplam terimi sıfır durum yanıtıdır.

## z düzleminde çözüm

Tek yanlı z dönüşümüyle:

zX(z) − zx(0) = AX(z) + BU(z)

X(z) = z(zI − A)⁻¹x(0) + (zI − A)⁻¹BU(z)

D = 0 için:

Y(z) = Cz(zI − A)⁻¹x(0) + C(zI − A)⁻¹BU(z)

**Φ(k) = Aᵏ = Z⁻¹{z(zI − A)⁻¹}**.

## Tahta özeti: erişilebilirlik ve zamanın tersine çevrilmesi

Tahtada “DT C/O” başlığı altında reachability, controllability, observability ve constructibility kavramları, aralarındaki dual ilişkilerle birlikte gösterilmiş. Bir sistemin erişilebilirliği ile dual sistemin gözlenebilirliği ilişkilendiriliyor. A⁻¹’in varlığı, durumun zaman yönünde geri kurulması için ayrı bir koşul olarak belirtiliyor.

Girişsiz x(k + 1) = Ax(k) için A tersinir olduğunda:

**x(k) = A⁻¹x(k + 1), x(−1) = A⁻¹x(0)**.

Tahtada x(0)’ın gözlem verilerinden çıkarılması için “y − Tu = O(C,A)x(0)” biçiminde bir toplu ilişki de yazılmış. Tam matris tanımları fotoğrafta verilmediğinden ek bir sayısal örnek oluşturulmadı.
