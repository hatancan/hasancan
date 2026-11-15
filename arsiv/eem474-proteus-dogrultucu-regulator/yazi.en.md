---
baslik: EEM474 Power Electronics: Proteus Rectifier and Regulator Project
ozet: A breakdown of the components and parameters of a Proteus project containing a transformer, bridge rectifier, and 7812.
---

The Proteus project dated 18 May 2015 in the EEM474 folder contains a transformer, a bridge rectifier, and a 7812 regulator. The project's license/customer metadata has been removed; the circuit file can be downloaded as a ZIP. The project was not opened or run.

## Circuit elements in the file

| Element | Recorded value/property |
| --- | --- |
| AC source | 220 V amplitude, 1 Hz frequency |
| Transformer | TRAN-2P2S; LP = 1 H, LS = 1 H, M = 1 |
| Winding resistances | RP = RS = 1 mΩ |
| Rectifier | BRIDGE |
| Regulator | 7812 model |
| Capacitors | 1000 µF, 10 µF, and 100 nF components |
| Measurement | DC voltmeter and current probe |

Example of readable parameters in the source file:

```
{MODFILE=SINE}
{AMP=220V}
{FREQ=1Hz}
{LP=1H}
{LS=1H}
{M=1.0}
{RP=1m}
{RS=1m}
{MODFILE=7812}
```

*Note: The frequency in the source is kept as 1 Hz; it was not changed on the assumption that it is the mains frequency. This list is a breakdown of the parameters in the file; it is not a verified power supply design or an experimental result.*
