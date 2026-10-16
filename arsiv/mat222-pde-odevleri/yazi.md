---
baslik: MAT222 Diferansiyel Denklemler: Kısmi Diferansiyel Denklem Ödevleri (Kurum belirtilmemiş)
ozet: İngilizce 25 PDE sorusu: karakteristikler, Cauchy ve Dirichlet problemleri, Hamilton–Jacobi, zayıf çözümler, temel çözümler ve dalga denklemi.
---

Bu yazı, **“Homework Problems for PDEs: I”** başlıklı dört sayfalık İngilizce ödev föyünü içeriyor. PDF oluşturulma tarihi **17 Mart 2003**; belgede yazar ve üniversite adı yok. `ege_notlari` klasöründe bulunması Ege Üniversitesi aidiyetini doğrulamıyor. Sorular İngilizce olarak metne aktarıldı; orijinal PDF yazının sonunda indirilebilir. uₓ, uᵧ gibi gösterimler kısmi türevdir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Characteristics and Cauchy problems: 1–9

1. Solve uuₓ + uᵧ = 1 with u = 0 when y = x. What happens if the initial condition is replaced by u = 1?
2. Show that (y − x)uₓ − (y + x)uᵧ = 0, u(x,0) = f(x), x > 0, has no solution if f is an arbitrary function.
3. For yuₓ + xuᵧ = cu, u(x,x) = f(x), x > 0, determine a condition on f for a characteristic initial value problem. Assuming it holds, obtain a nonunique solution.
4. Study the three systems listed below: existence of an unbounded solution on the whole plane; boundedness along characteristics; intersection of each characteristic with y = x + u²; existence of a first integral whose y derivative at the origin equals 1, and the derivative of that derivative along the characteristic vector.
5. For x(x² + y²)uₓ + y³uᵧ = 0, u(x,0) = 1, discuss existence and uniqueness near (x₀,0).
6. Find all solutions of yuₓ − sin(x)uᵧ = u² near (0,0).
7. Study existence and uniqueness of yuₓ = xuᵧ, u(1,y) = cos y, near (1,y₀).
8. Does yuₓ + sin(x)uᵧ = y, u(0,y) = y⁴ have a solution in the plane? Is it unique?
9. Does |∇u|² = 1 with u = 1 on y = x² have a unique smooth solution in y ≤ x²? In y ≥ x²?

The three equations in problem 4 are:

- xuₓ − (1 + x⁴ + y²)uᵧ = 2u, u(0,y) = 0.
- (2 + x² + y²)uₓ + yuᵧ = u, u(x,0) = 0.
- xuₓ + (1 + 2u⁴ + y²)uᵧ = 3u, u(0,y) = 0.

*Not: İkinci sorunun “keyfi f için çözüm yok” önermesi, karakteristik denklemlerle yerel olarak uyuşmuyor. Başlangıç eğrisi (x,0), x > 0 için karakteristik alan (−x,−x) eğriye teğet değildir; düzgün başlangıç verisi yerel çözüm verir. Sorunun ifadesi korunmuştur.*

## Boundary conditions and systems: 10–12

**10.** Solve the Dirichlet problem Δu = 0 in x² + y² < 1, with u = 1 on the upper semicircle and u = −1 on the lower semicircle.

**11.** Show that uᵧ + Auₓ = 0 is hyperbolic for A = [[1,1,0], [1,1,0], [0,0,2]]. Reduce to canonical form, find the general solution, and solve for u(x,0) = (sin x, 1, eˣ)ᵀ.

**12.** Consider u = uₓ² + uᵧ² with u(x,0) = ax². For what positive a does a solution exist? Is it unique? Find all solutions.

## Hamilton–Jacobi and power series: 13–17

**13.** For uₜ + H(∇ₓu) = 0, where H depends only on ∇ₓu, verify that u(x₁,…,xₙ;a,b) = a₁x₁ + … + aₙxₙ − tH(a) + b is a complete integral. Use envelopes to construct a solution of uₜ + |∇u|² = 0 that is not linear in x and t.

**14.** For u_zz = u²uₓ + (u_xy)², u(x,y,0) = x − y and u_z(x,y,0) = sin x, find u_xz, u_yz and u_zz at z = 0.

**15.** Is the heat equation uₜ = kuₓₓ in normal form for Cauchy data on the x axis? On the t axis? What form would the data take?

**16.** Solve uᵧᵧ = uₓₓ + u, u(x,0) = eˣ, uᵧ(x,0) = 0 as a power series Σ aₙ(x)yⁿ.

**17.** For uₜ = uₓₓ, u(x,0) = g(x), where g is a polynomial, find a Taylor series solution about (0,0) and determine where it converges.

## Well-posedness and weak solutions: 18–23

**18.** Show that uₓₓ + uᵧᵧ = 0, u(x,0) = 0, uᵧ(x,0) = k⁻¹ sin(kx), k > 0, is not well-posed in Hadamard's sense.

**19.** Show that K(x,y) = [2πi(x + iy)]⁻¹ is a fundamental solution for L = ∂ₓ + i∂ᵧ on R².

*Not: Standart dağılım normalizasyonunda (∂ₓ + i∂ᵧ)[1/(2π(x + iy))] = δ'dır. Kaynaktaki ek i çarpanı bu operatör için doğru normalizasyonu vermez.*

**20.** Let Lu = u_ξη have a jump along ξ = 0. Derive the transmission condition ∫_(−∞)^∞ [u₋(0,η) − u₊(0,η)]v_η(0,η)dη = 0, integrating first in ξ and then in η. Why must the jump u₊ − u₋ be constant along the discontinuity?

**21.** For uₜ + cuₓ = 0, show that u(x,t) = f(x − ct) is a weak solution when f is continuous. Find discontinuous weak solutions. Is there a transmission condition along x = ct?

**22.** Show that each function below is a fundamental solution of L = ∂²/(∂ξ∂η), using δ(ξ,η):

- F₁ = H(ξ)H(η).
- F₂ = −H(ξ)H(−η).
- F₃ = −H(−ξ)H(η).
- F₄ = H(−ξ)H(−η).

Use ξ = x + ct, η = x − ct to obtain four fundamental solutions of the one dimensional wave operator, supported in the wedges determined by x = ±ct.

**23.** Let L be a constant coefficient spatial differential operator. Suppose Kₜ − LK = 0 for t > 0 and K(x,0) = δ(x) in distributions. Show that extension by zero to t < 0 gives (∂ₜ − L)K = δ(x)δ(t).

## Wave equation: 24–25

**24.** Solve uₜₜ = uₓₓ + uᵧᵧ + u_zz, u(x,y,z,0) = x² + y², uₜ(x,y,z,0) = 0 using both Kirchhoff's formula and Hadamard's method.

**25.** Use Duhamel's principle to solve uₜₜ − c²Δu = f(x,t) in three space dimensions, with zero initial displacement and velocity. What regularity of f is required for a C² solution?

## Kontrol notları

Föyde çözüm anahtarı yok. Aktarım sırasında kısa sonuçlar kontrol edildi: 14. soruda u_xz = cos x, u_yz = 0 ve u_zz = (x − y)²; 24. soruda u = x² + y² + 2t² başlangıç koşullarını ve dalga denklemini sağlar. Bunlar arşiv aktarımı sırasında yapılan kontrollerdir.
