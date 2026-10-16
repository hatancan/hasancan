---
baslik: EEM301 Sinyaller ve Sistemler I: Sinyaller, Fourier ve Laplace Dönüşümü Notları (Texas A&M, Parlos ve Parasuram)
ozet: Texas A&M Üniversitesi Makine Mühendisliği'nin MEEN 651 (Alexander G. Parlos, 2003) ders notları ve MEEN 364 (Parasuram, 2001–2003) örnek föyleri: sinyal ve sistem tanımları, Fourier serisi ve dönüşümü, Laplace dönüşümü ve özellikleri, kütle-yay-sönümleyici transfer fonksiyonu, örnekleme ve örtüşme.
---

Bu yazı, EEM301 Sinyaller ve Sistemler I klasöründe 2017 tarihli olarak duran dokuz PDF'i tanıtıyor. Belgeler **Texas A&M University, Department of Mechanical Engineering**'e ait: **MEEN 651 Control System Design** dersinin Dr. Alexander G. Parlos tarafından hazırlanan üç ders notu (Güz 2003) ve **MEEN 364** dersinin Parasuram imzalı örnek föyleri (2001–2003). Metinler İngilizce; aşağıda içerikleri özetlendi. Bütün PDF'ler yazının sonunda ZIP olarak indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## MEEN 651 Lecture 1A: Introduction to Signals and Systems

- Sinyaller bir ya da daha fazla bağımsız değişkenin (çoğunlukla zamanın) fonksiyonu olup bilgi taşır; sistemler giriş sinyallerine çıkış sinyalleri üreterek yanıt verir (ör. elektrik devresindeki gerilim ve akımlar sinyal, devrenin kendisi sistem).
- Sürekli zamanlı ve ayrık zamanlı sinyaller ve sistemler.
- Dönüşümlerin kullanımı:

| | Kalıcı durum davranışı | Geçici durum davranışı |
|---|---|---|
| Sürekli zaman | Sürekli Fourier dönüşümü | Laplace dönüşümü |
| Ayrık zaman | Ayrık Fourier dönüşümü | z dönüşümü |

## MEEN 651 Lecture 1B: Fourier Analysis and Fourier Transforms

- Temel sürekli zamanlı sinyaller: karmaşık üstel x(t) = Ce^(at), periyodik e^(jω₀t), sinüzoit A cos(ω₀t + φ) = A·Re{e^(j(ω₀t+φ))}, T₀ = 2π/|ω₀|.
- Birim basamak u(t) ve birim dürtü δ(t): u(t) = ∫₋∞^t δ(τ)dτ, δ(t) = du(t)/dt.
- Fourier serisi x(t) = Σ a_k e^(jkω₀t); her iki taraf e^(−jnω₀t) ile çarpılıp bir periyot boyunca integral alınarak katsayılar a_k = (1/T₀)∫ x(t)e^(−jkω₀t) dt türetiliyor; periyot sonsuza götürülerek Fourier dönüşümüne geçiliyor.
- Ayrık zamanda birim basamak ve dürtü dizileri, karmaşık üstel ve sinüzoit; sürekli ve ayrık zamanlı e^(jω₀t) ile e^(jω₀n) karşılaştırması (ayrık zamanda frekanslar 2π katlarında aynı sinyali verir, periyodiklik için ω₀/2π'nin rasyonel olması gerekir).

## MEEN 651 Lecture 2A: Laplace Transforms

- Tanım: F(s) = ∫₀^∞ f(t)e^(−st) dt, s = σ + jω; ters dönüşüm f(t) = (1/2πj)∫ F(s)e^(st) ds (pratikte kısmi kesirler kullanılır).
- Tablo: δ(t) → 1, u(t) → 1/s, t → 1/s², t² → 2/s³, e^(−at) → 1/(s + a), te^(−at) → 1/(s + a)², sin ωt → ω/(s² + ω²), cos ωt → s/(s² + ω²).
- Özellikler: doğrusallık, integral (F(s)/s), türev (sⁿF(s) − başlangıç terimleri), zamanda kayma e^(−as)F(s), karmaşık domende kayma F(s + a), ilk değer f(0⁺) = lim_{s→∞} sF(s) ve son değer lim_{t→∞} f(t) = lim_{s→0} sF(s) teoremleri.
- Örnek: kütle-yay-sönümleyici sistemi. m dv/dt = F(t) − bv(t) − kx(t), dx/dt = v(t) denklemlerinden X(s)(ms² + bs + k) = F(s) + x(0⁻)(ms + b) + mv(0⁻); sıfır başlangıç koşullarıyla transfer fonksiyonu **T(s) = X(s)/F(s) = 1/(ms² + bs + k)**.

## MEEN 364 örnek föyleri (Parasuram)

- **Handout E.1 – Examples on Signals and Systems:** sinyal örnekleri, sistem gösterimi, analog/ayrık/sayısal giriş-çıkışlı sistemler, model türleri, doğrusal ve doğrusal olmayan sistemler, zaman ve frekans domeni modelleri.
- **Handout E.2 – Examples on Fourier Transforms:** f(x) = U(x)e^(−ax)'in sürekli Fourier dönüşümü, ayrık zamanlı bir sinyalin Fourier dönüşümünün geometrik seriyle hesabı.
- **Handout E.3 – Examples on Laplace Transforms:** Laplace dönüşümü örnekleri ve kısmi kesirlerle ters dönüşüm.
- **Examples on Sampling and Aliasing Phenomena (E.4):** x₁(t) = cos 2π(10)t ve x₂(t) = cos 2π(50)t, F_s = 40 Hz ile örneklenince x₁(n) = cos(πn/2) ve x₂(n) = cos(5πn/2) = cos(2πn + πn/2) = cos(πn/2) olur; iki sinyal ayırt edilemez, 50 Hz bu örnekleme hızında 10 Hz'in bir örtüşmesidir (alias). Diğer örneklerde x(t) = 3 cos 100πt için örtüşmeyi önleyen en küçük örnekleme hızı ve Nyquist hızı hesaplanıyor.
- **Handout on Fourier Analysis of Dynamic Signals:** sayısal sinyal işleme sisteminin öğeleri, sinyallerin sınıflandırılması, sürekli ve ayrık zamanlı periyodik sinyallerin Fourier serisi ve dönüşümü, hızlı Fourier dönüşümü (FFT) ve MATLAB'da `fft`/`ifft` kullanımı.
- **Handout A.2 – Laplace Transforms:** tanım, basit fonksiyonların dönüşümlerinin türetilmesi, MATLAB ile doğrulama (dönüşümler önce analitik yöntemle yapılmalı, MATLAB yalnız sağlama için kullanılmalı), özellikler, son değer teoremiyle kalıcı durum değeri, ters dönüşüm, diferansiyel denklem çözümü ve kısmi kesir açılımı teoremleri.
