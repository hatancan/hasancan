---
baslik: EEM474 Power Electronics: Flyback Converter
ozet: Operating intervals of the flyback converter, continuous and discontinuous conduction, magnetizing current, and the DCM output voltage.
---

This is a Flyback Converter presentation prepared by classmates for the EEM474 Power Electronics course at Başkent University. No date is given. Personal information has been removed; a cleaned-up PDF can be downloaded at the end of the post.

## Flyback converter

The presentation describes the flyback as a buck–boost-type converter capable of AC/DC or DC/DC conversion. There is galvanic isolation between the windings. It is easy to set up and low in cost; the presentation gives as examples cell phone chargers in the 5–150 W range, high-voltage supplies for TVs and monitors, and headlights, lasers, and photocopiers.

## Switching states

When the switch is closed, the primary is connected to the source voltage. The primary current increases; the secondary diode is reverse biased. The source text describes this state as "the current flowing through the inductor is stored" and "the capacitance begins to charge."

*Note: What is stored in the inductor is energy. While the secondary diode is off, the output capacitor supplies the load; during this interval there is no charging from the secondary.*

When the switch opens, the secondary diode begins to conduct and the load is supplied.

## Continuous and discontinuous conduction

In discontinuous conduction (DCM), the secondary current falls to zero before the next switching cycle. The presentation lists high RMS and peak currents, electromagnetic interference, and noise among the disadvantages. In continuous conduction, the current does not drop to zero during this interval; the control is noted to be more complex.

## Basic equations

For primary magnetizing inductance L_m, switching period T, and duty ratio D:

- Switch closed: di_L/dt = V_s/L_m; Δi_L = V_s DT/L_m.
- Switch open: v_L = −V_o N₁/N₂; Δi_L = −V_o(N₁/N₂)(1−D)T/L_m.
- Peak current in discontinuous conduction: I_L,max = V_s DT/L_m.
- Average input current: I_s = V_s D²T/(2L_m).
- Ideal power balance: V_s I_s = V_o²/R.
- DCM output: V_o = V_s D √[TR/(2L_m)] = V_s D √[R/(2L_m f)].

This last relation applies under the ideal discontinuous-conduction assumptions on the slide.
