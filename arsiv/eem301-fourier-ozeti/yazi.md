---
baslik: EEM301 Sinyaller ve Sistemler I: Fourier Özeti ve Faydalı Bağıntılar (Alper Uraz)
ozet: EEM301 Sinyaller ve Sistemler I dersinin iki sayfalık formül özeti: sürekli ve ayrık zamanlı konvolüsyon, Fourier serisi ve Fourier dönüşümü sentez/analiz denklemleri, faydalı integraller, sonlu ve sonsuz geometrik toplamlar, dikdörtgen–kutupsal dönüşüm ve j'nin kuvvetleri.
---

Bu yazı, Başkent Üniversitesi **EEM301 Sinyaller ve Sistemler I** dersinde Prof. Dr. Alper Uraz'ın dağıttığı iki sayfalık **"Fourier Summary"** (EEM301-UsefulSummary) formül kâğıdını içeriyor. Belgenin iki sürümü var: Ocak 2007 tarihli ilk sürüm ve 2010'da düzeltilip konvolüsyon özelliği eklenmiş sürüm. Aşağıdaki metin yeni sürümden aktarıldı. Her iki Word dosyası yazının sonunda ZIP olarak indirilebilir.

## Konvolüsyon

Konvolüsyon özelliği (2010 sürümünde eklenmiş):

- y(t) = h(t) ∗ x(t) ⟷ Y(ω) = H(ω) X(ω)
- y(n) = h(n) ∗ x(n) ⟷ Y(e^(jω)) = H(e^(jω)) X(e^(jω))

| | Sürekli zaman (CT) | Ayrık zaman (DT) |
|---|---|---|
| Nedensel olmayan x(·), h(·) | y(t) = ∫₋∞^∞ x(τ) h(t − τ) dτ | y(n) = Σ_{k=−∞}^{∞} x(k) h(n − k) |
| Nedensel x(·), h(·) | y(t) = ∫₀ᵗ x(τ) h(t − τ) dτ | y(n) = Σ_{k=0}^{n} x(k) h(n − k) |

## Fourier serileri

x(t) ⟷ aₖ ve x(n) ⟷ aₖ (FS):

| | CT | DT |
|---|---|---|
| Sentez denklemi | x(t) = Σ_{k=−∞}^{∞} aₖ e^(jkω₀t) | x(n) = Σ_{k=⟨N⟩} aₖ e^(jkω₀n) |
| Analiz denklemi | aₖ = (1/T) ∫_T x(t) e^(−jkω₀t) dt | aₖ = (1/N) Σ_{n=⟨N⟩} x(n) e^(−jkω₀n) |

## Fourier dönüşümleri

x(t) ⟷ X(ω), yani F[x(t)] = X(ω), x(t) = F⁻¹[X(ω)]; ayrık zamanda x(n) ⟷ X(e^(jω)).

| | CT | DT |
|---|---|---|
| Sentez denklemi | x(t) = (1/2π) ∫₋∞^∞ X(ω) e^(jωt) dω | x(n) = (1/2π) ∫_{2π} X(e^(jω)) e^(jωn) dω |
| Analiz denklemi | X(ω) = ∫₋∞^∞ x(t) e^(−jωt) dt | X(e^(jω)) = Σ_{n=−∞}^{∞} x(n) e^(−jωn) |

## Faydalı integraller

- ∫ e^(ax) sin nx dx = e^(ax)/(a² + n²) · [a sin nx − n cos nx]
- ∫ e^(ax) cos nx dx = e^(ax)/(a² + n²) · [a cos nx + n sin nx]
- ∫ x sin nx dx = sin nx / n² − x cos nx / n
- ∫ x cos nx dx = cos nx / n² + x sin nx / n
- ∫ x e^(ax) dx = e^(ax) [x/a − 1/a²]
- ∫ p·q dx = p [∫q dx] − ∫ [∫q dx] (dp/dx) dx (kısmi integrasyon)

## Faydalı bağıntılar

**Sonlu toplam formülü** (her karmaşık a için):

- Σ_{n=0}^{N−1} aⁿ = (1 − a^N)/(1 − a), a ≠ 1; a = 1 için N

**Sonsuz toplam formülü:**

- Σ_{n=0}^{∞} aⁿ = 1/(1 − a), |a| < 1

**Türevler:**

- Σ_{n=0}^{N−1} n aⁿ = a(1 − a^N)/(1 − a)² − N a^N/(1 − a)
- Σ_{n=0}^{∞} n aⁿ = a/(1 − a)², |a| < 1

**Farklı sınırlarla** (a ≠ 1, pozitif/negatif M, N ve M ≤ N):

- Σ_{n=M}^{N−1} aⁿ = (a^M − a^N)/(1 − a); a = 1 için N − M
- Σ_{n=M}^{∞} aⁿ = a^M/(1 − a), |a| < 1
- Σ_{n=1}^{N} n = N(N + 1)/2, Σ_{n=1}^{N} n² = N(N + 1)(2N + 1)/6

*Not: 2007 tarihli ilk sürümde Σ n aⁿ (n = 0…∞) toplamı a/(1 − a) olarak yazılmıştı; doğrusu a/(1 − a)²'dir ve 2010 sürümünde düzeltilmiş.*

## Dikdörtgen ↔ kutupsal

Pozitif gerçel a, b ve tam sayı n için:

- a − jb = r e^(jθ₁) ⇒ r = √(a² + b²), θ₁ = tan⁻¹(−b/a) = −tan⁻¹(b/a)
- −a + jb = r e^(jθ₂) ⇒ r = √(a² + b²), θ₂ = π − tan⁻¹(b/a) = π + θ₁
- e^(±jnπ) = cos(nπ) = (−1)ⁿ, sin(nπ) = 0, e^(±j2πn) = 1, e^(j(2n+1)π/2) = j(−1)ⁿ

**j'nin kuvvetleri:**

- (−j)² = −1, (−j)³ = +j, (−j)⁴ = 1, (−j)⁵ = (−j)⁴(−j)¹ = −j, …
- (+j)² = −1, (+j)³ = −j, (+j)⁴ = 1, (+j)⁵ = (+j)⁴(+j)¹ = +j, …
