---
baslik: EEM202 Circuit Theory II: The Ideal Transformer
ozet: Presentation on the ideal transformer from the EEM202 Circuit Theory II course (Asst. Prof. Dr. Selda Güney, 2014): polarity via the dot convention, notation of the turns ratio, the phasor equivalent of the vg = 2500 cos 400t V example, and impedance matching.
---

This post is the content of the **Ideal Transformer** presentation prepared by Asst. Prof. Dr. Selda Güney for the Başkent University Electrical and Electronics Engineering course **EEM202 Circuit Theory II** (April 2014). It is a short six-slide presentation: the circuit diagrams are included as images, while the formulas and values are transcribed as text. The original PDF can be downloaded at the end of the post.

## Determining the polarity

In an ideal transformer, the signs of the voltage and current relationships depend on the positions of the dots on the windings (the dot convention) and on the reference directions. The four cases in the presentation:

| Case | Voltage relationship | Current relationship |
|---|---|---|
| (a) | V₁/N₁ = V₂/N₂ | N₁I₁ = −N₂I₂ |
| (b) | V₁/N₁ = −V₂/N₂ | N₁I₁ = N₂I₂ |
| (c) | V₁/N₁ = V₂/N₂ | N₁I₁ = N₂I₂ |
| (d) | V₁/N₁ = −V₂/N₂ | N₁I₁ = −N₂I₂ |


![Polarity of the ideal transformer: four different dot and reference direction arrangements (a)–(d) with voltage and current relationships](s-02.jpg "Determining the polarity: four cases according to the dot convention")

## Notation of the turns ratio

The turns ratio can be shown in three different ways. For example, for an ideal transformer with N₁ = 500 and N₂ = 2500 turns:

- (a) The numbers of turns are written directly: N₁ = 500, N₂ = 2500
- (b) As a ratio: **1 : 5**
- (c) As a ratio normalized to the primary side: **1/5 : 1**

![Three notations of the turns ratio: N1 = 500 and N2 = 2500, 1:5 and 1/5:1](s-03.jpg "The turns ratio can be shown in three different ways")

## Example: vg = 2500 cos 400t V

The source is vg = 2500 cos 400t V; the primary side has a 0.25 Ω resistance and a 5 mH inductance, followed by a 10 : 1 ideal transformer, and the load on the secondary side consists of a 237.5 mΩ resistance and a 125 µH inductance.

![Example circuit: source vg, 0.25 ohm and 5 mH, 10:1 ideal transformer, 237.5 milliohm and 125 microhenry load](s-04.jpg "Example circuit (time domain)")

### Phasor-domain equivalent circuit

The reactances of the inductances are found with X_L = jωL (ω = 400 rad/s):

- 5 mH → j·400·0.005 = **j2 Ω**
- 125 µH → j·400·125·10⁻⁶ = **j0.05 Ω**
- Source phasor: **2500∠0° V**

![Phasor-domain equivalent circuit: 2500∠0° V source, 0.25 ohm, j2 ohm, 10:1 ideal transformer, 0.2375 ohm and j0.05 ohm](s-05.jpg "Continuing the example: phasor-domain equivalent circuit")

## Using the ideal transformer for impedance matching

The last slide shows a circuit in which a source V_s with internal impedance Z_s supplies a load Z_L through a 1 : a ideal transformer.

![Impedance matching: source Vs, Zs, 1:a ideal transformer and load ZL](s-06.jpg "Using the ideal transformer for impedance matching")
