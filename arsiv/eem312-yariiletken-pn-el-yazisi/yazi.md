---
baslik: EEM312 Sayısal Elektronik: Yarıiletkenlerde Taşıyıcılar ve p-n Eklem Denklemi, El Yazısı Notlar
ozet: Difüzyon ve sürüklenme akımları, Einstein bağıntısı, katkılı yarıiletkenlerde denge yoğunlukları ve ileri/ters kutuplamadan diyot denklemine geçişin el yazısı notlardan metin dökümü.
---

Bu yazı, **EEM312 Sayısal Elektronik** arşivindeki bir arkadaşın hazırladığı İngilizce el yazısı notların yarıiletkenler ve p-n eklemi bölümüdür. Fotoğraflanmış sayfalardan metne aktarıldı; kişisel bilgiler çıkarıldı. Sayfalarda tarih yok; dosyalar Nisan 2014 arşiv tarihini taşıyor. Fotoğraflar özel arşivde saklanıyor, bu yazıda indirme dosyası bulunmuyor.

## Intrinsic semiconductor and diffusion

For an intrinsic semiconductor, **n = p = n_i**. Here n is electron concentration and p is hole concentration. A hole concentration that decreases with x creates diffusion current in the positive x direction:

J_p = −qD_p dp/dx.

The corresponding electron diffusion current density is:

J_n = qD_n dn/dx.

Current density is proportional to the concentration gradient. D_n and D_p are diffusion constants; the notes use A/cm² for current density.

## Drift current and mobility

With an electric field E in the x direction:

- Hole drift velocity: v_p = μ_p E.
- Electron drift velocity: v_n = −μ_n E.
- Hole drift current density: J_p,drift = qpμ_p E.
- Electron drift current density: J_n,drift = qnμ_n E.

Electrons carry negative charge and move opposite to E, so their conventional current points in the direction of E. The notes give μ_n ≈ 2,5μ_p for silicon. Mobility units are cm²/(V·s) or m²/(V·s).

The total drift current density and resistivity are:

**J_drift = q(pμ_p + nμ_n)E**, **ρ = 1/[q(pμ_p + nμ_n)]**.

This is a form of Ohm's law: J = E/ρ. For a cross-section A, the hole charge crossing it per second is qpμ_pEA.

Einstein relationship:

**D_n/μ_n = D_p/μ_p = V_T** (thermal voltage).

*Not: Bu bölümde V_T ısıl gerilimdir; MOS notlarındaki eşik gerilimiyle aynı simge kullanılsa da farklı bir büyüklüktür.*

## Doped semiconductor in thermal equilibrium

For n-type silicon:

n_n0 ≈ N_D,

n_n0 p_n0 = n_i²,

**p_n0 = n_i²/N_D**.

The majority concentration is approximately the donor concentration. The minority concentration depends strongly on temperature through n_i. The corresponding p-region relation used later is n_p0 = n_i²/N_A.

## Junction at zero bias and reverse bias

At zero applied bias, majority-carrier diffusion current I_D and minority-carrier drift current I_S balance: **I_D = I_S**.

In reverse bias, the external circuit removes electrons from the n side and holes from the p side. More fixed ion charge is exposed; the depletion region widens and its barrier increases. Diffusion current decreases. With the reverse-current reference direction in the drawing:

**I = I_S − I_D ≈ I_S**.

The notes distinguish this normal reverse-bias region from breakdown, where current can exceed I_S. The increase of barrier voltage above the built-in value appears at the terminals as V_R.

## Forward bias

The external circuit supplies majority carriers to both sides. These neutralize some exposed charge; the depletion region narrows and the barrier falls. More holes cross from p to n and more electrons from n to p. The diffusion current rises until, with the forward-current reference direction:

**I = I_D − I_S**.

Holes injected into the n region and electrons injected into the p region produce minority concentrations above their thermal-equilibrium values. The junction barrier is lower than its zero-bias value by the applied forward voltage V.

## From minority concentration to the diode equation

The notes use Φ_T for thermal voltage in this derivation. The law of the junction at the n-side depletion boundary x = w₂ is:

p_n(w₂) = p_n0 e^(V/Φ_T).

The excess concentration decays away from the boundary:

p_n(x) = p_n0 + [p_n(w₂) − p_n0]e^(−(x − w₂)/L_p)

= p_n0 + p_n0[e^(V/Φ_T) − 1]e^(−(x − w₂)/L_p).

Differentiating and applying J_p = −qD_p dp/dx gives:

J_p(x) = (qD_p/L_p)p_n0[e^(V/Φ_T) − 1]e^(−(x − w₂)/L_p).

At x = w₂:

J_p = (qD_p/L_p)p_n0[e^(V/Φ_T) − 1].

Similarly, on the p side:

J_n = (qD_n/L_n)n_p0[e^(V/Φ_T) − 1].

The two current contributions have the same terminal direction. Therefore:

I = A(J_p + J_n)

= Aq[(D_p/L_p)p_n0 + (D_n/L_n)n_p0][e^(V/Φ_T) − 1].

Substituting the equilibrium minority concentrations:

**I = I_S[e^(V/Φ_T) − 1]**,

**I_S = Aqn_i²[D_p/(L_pN_D) + D_n/(L_nN_A)]**.

Here A is junction area; L_p and L_n are diffusion lengths. These are the final expressions boxed or underlined in the source notes.
