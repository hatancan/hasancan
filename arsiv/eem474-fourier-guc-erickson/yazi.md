---
baslik: EEM474 Güç Elektroniği: Fourier serilerinde güç ve RMS (R. W. Erickson)
ozet: ECEN 2260 ek ders notlarından harmoniklerle güç aktarımı, RMS, bozulma ve yer değiştirme güç faktörleri.
---

R. W. Erickson'ın “Power and RMS Values of Fourier Series” başlıklı ECEN 2260 ek ders notu, EEM474 arşivindeki kopyadan aktarılmıştır. Tarihsiz dokuz sayfalık belgenin PDF'i yazının sonundan indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Average power and energy

For periodic voltage and current, p(t) = v(t)i(t), Wcycle = ∫₀ᵀ p(t) dt and Pav = Wcycle/T. Instantaneous power can be negative during part of the cycle even when average power is positive.

Write the Fourier series with peak amplitudes Vn and In:

v(t) = V₀ + Σ Vn cos(nωt − φn)

i(t) = I₀ + Σ In cos(nωt − θn)

Orthogonality makes products of different harmonics integrate to zero over a complete period. Consequently Pav = V₀I₀ + ½Σ VnIn cos(φn − θn). Only matching frequency components contribute to average power. A fundamental voltage and a pure third-harmonic current therefore transfer zero net energy; matching third harmonics can transfer power.

## RMS values

Vrms² = V₀² + ½Σ Vn², with an equivalent expression for current. The RMS value can be found either by integrating the squared waveform or by adding squared harmonic RMS values. Individual harmonic amplitudes are not added directly.

For a resistor, Pav = Irms²R. This relation explains the additional heating caused by harmonic current even when that current does not contribute to useful power supplied by a sinusoidal voltage source.

## Power factor

PF = Pav/(Vrms Irms). When the voltage contains only a sinusoidal fundamental, PF = (I₁,rms/Irms) cos(φ₁ − θ₁). The first factor describes waveform distortion; the second describes displacement between the fundamental components.

A current waveform can have zero fundamental phase displacement and still have power factor below one. Conversely, a phase correction alone does not remove distortion current. The notes use waveforms and Fourier components to distinguish these cases.

## Total harmonic distortion

THD = √(Irms² − I₁,rms²)/I₁,rms for a current with no DC component. In that case I₁,rms/Irms = 1/√(1 + THD²). The document relates harmonic content, RMS loading, and power factor without assuming that every waveform is sinusoidal.

*Not: Fourier katsayıları bu yazıda tepe değerleridir; RMS katsayılarla yazılan eşitliklerde ½ çarpanı ayrıca kullanılmaz.*
