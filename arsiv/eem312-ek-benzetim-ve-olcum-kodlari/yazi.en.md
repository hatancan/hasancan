---
baslik: EEM312 Digital Electronics: Additional Simulation Codes for Diode, MOS, Power, and RC Measurements
ozet: SPICE simulations of diode transients, MOS sweeps, CMOS power, and ring oscillator experiments; MATLAB plots of RC gain and phase measurements. Additional source codes and notes on source errors.
---

This post collects various simulation and plotting codes left over from the 2011–2017 laboratory work in the **EEM312 Digital Electronics** archive. Student names and numbers have been removed from the code comments and file names. These versions, which were not included in the appendices of the earlier experiment posts, can be downloaded as a ZIP at the end of the post, with their sources cleaned up. The codes were not run; the explanations below are based on reading the sources.

## Experiment conditions

- The diode model uses BV = 50 V; a 10 kΩ load, a 0–5 V pulse, and a 2 µs transient analysis with a 0.1 ns step. The DC analysis in the file has been left commented out.
- In the power codes, `-vdd#branch*v(3)` shows the instantaneous power drawn from the supply. `1_b.cir` also requests the average via `mean`, for a 5 V supply and a 0.1 pF load.
- `1a.cir` holds the input at 5 V and sweeps the supply over 0–5 V; the widths of both transistors are 1.8 µm.
- The MOS sweeps use the Level 3 and Level 49 models. The long-channel file has W/L = 90/1 µm; in the PMOS file, of the width options 1.8, 3.6, and 7.2 µm, only the first is active.
- The ring file connects five `inv` subcircuits in a closed chain. Each subcircuit has a 100 fF load and a 3.2 V supply.

## Notes on the source codes

*Note: In `nmos2.cir`, the `VIN 1 0` line is missing its source value. Although the file's analysis sweeps VIN, this definition may be incomplete from the simulator's syntax standpoint.*

*Note: The resistor-loaded NMOS file contains `C1 2 0 1F`. In SPICE suffixes, `F` means femto; this expression is a value of 1 fF.*

*Note: The ring file requests `plot V(6)`; node 6 is not defined in the top-level connections. The source line was not changed.*

## RC measurement series

The gain code puts the measured ratios on the x axis and the frequencies on the y axis. The phase code, on the other hand, takes the frequency as the x axis and the phase difference as the y axis.

| Frequency (kHz) | Gain in code | Phase difference |
|---|---|---|
| 10 | 0.872 | 17.63 |
| 50 | 0.475 | 50.9 |
| 100 | 0.26 | 69.12 |
| 150 | 0.18 | 73.07 |
| 200 | 0.14 | 80.64 |
| 250 | 0.116 | 112.5 |
| 300 | 0.096 | 72.43 |
| 400 | 0.08 | 81.29 |
| 500 | 0.064 | 59.4 |
| 1000 | 0.04 | 79.2 |

*Note: The axis label of the gain code says `Vin/Vout`. These measurements, which are less than one and decrease with frequency, correspond to the `Vout/Vin` ratio in the related RC low-pass experiment report. The label was kept as is in the source code. The value 112.5 at 250 kHz in the phase series was also left unchanged.*

## D1N4148 transient experiment

File: `diyot/Deney-4_Kod.cir`.

```spice
*D1N4148 Diyot Akım - Voltaj Grafiği

.model D1N4148 D(IS=5.84n  N=1.94  RS=.7017  XTI=3  EG=1.11  CJO=.95p 
+ M=.55  VJ=.75  FC=.5  BV=50  IBV=100u  TT=11.07n)


VIN 1 0 PULSE(0 5 0 0NS 0NS 500nS 10uS)
*VIN 1 0 DC 5
R1 2 0 10k
D1 1 2 D1N4148
*.CONTROL
*DC VIN -300 200 0.1
*PLOT -VIN#branch vs V(1)-V(2)
*.ENDC
.TRAN 0.1nS 2uS
.PLOT TRAN V(1) V(2)
.END
```

## Instantaneous and average power, input plot

File: `guc/1_b.cir`.

```spice
* Arsiv devre kaydi
.MODEL MOSN NMOS LEVEL=2 LD=0.15U TOX=200.0E-10
+ NSUB=5.36726E+15 VTO=0.743469 KP=8.00059E-05 GAMMA=0.543
+ PHI=0.6 U0=655.881 UEXP=0.157282 UCRIT=31443.8
+ DELTA=2.39824 VMAX=55260.9 XJ=0.25U LAMBDA=0.0367072
+ NFS=1E+12 NEFF=1.001 NSS=1E+11 TPG=1.0 RSH=70.00
+ CGDO=4.3E-10 CGSO=4.3E-10 CJ=0.0003 MJ=0.6585
+ CJSW=8.0E-10 MJSW=0.2402 PB=0.58
.MODEL MOSP PMOS LEVEL=2 LD=0.15U TOX=200.0E-10
+ NSUB=4.3318E+15 VTO=-0.738861 KP=2.70E-05 GAMMA=0.58
+ PHI=0.6 U0=261.977 UEXP=0.323932 UCRIT=65719.8
+ DELTA=1.79192 VMAX=25694 XJ=0.25U LAMBDA=0.0612279
+ NFS=1E+12 NEFF=1.001 NSS=1E+11 TPG=-1.0 RSH=120.6
+ CGDO=4.3E-10 CGSO=4.3E-10 CJ=0.0005 MJ=0.5052
+ CJSW=1.349E-10 MJSW=0.2417 PB=0.64

vdd 3 0 5
cl 2 0 0.1p
Vin 1 0 pulse (0 5 0 10n 10n 100n 200n)

M1 2 1 0 0 MOSN W=1.8u L=1.2u NRS=0.333 NRD=0.333
+ AD=6.5p PD=9.0u AS=6.5p PS=9.0u
M2 2 1 3 3 MOSP W=5.4u L=1.2u NRS=0.333 NRD=0.333
+ AD=6.5p PD=9.0u AS=6.5p PS=9.0u

.control 
tran 0.1ns 800ns
print mean(-vdd#branch*v(3))
plot -vdd#branch*v(3) 
plot v(1)
.endc
.end
```

## Supply DC sweep at a constant input

File: `guc/1a.cir`.

```spice
* Arsiv devre kaydi
1a

.MODEL MOSN NMOS LEVEL=2 LD=0.15U TOX=200.0E-10
+ NSUB=5.36726E+15 VTO=0.743469 KP=8.00059E-05 GAMMA=0.543
+ PHI=0.6 U0=655.881 UEXP=0.157282 UCRIT=31443.8
+ DELTA=2.39824 VMAX=55260.9 XJ=0.25U LAMBDA=0.0367072
+ NFS=1E+12 NEFF=1.001 NSS=1E+11 TPG=1.0 RSH=70.00
+ CGDO=4.3E-10 CGSO=4.3E-10 CJ=0.0003 MJ=0.6585
+ CJSW=8.0E-10 MJSW=0.2402 PB=0.58

.MODEL MOSP PMOS LEVEL=2 LD=0.15U TOX=200.0E-10
+ NSUB=4.3318E+15 VTO=-0.738861 KP=2.70E-05 GAMMA=0.58
+ PHI=0.6 U0=261.977 UEXP=0.323932 UCRIT=65719.8
+ DELTA=1.79192 VMAX=25694 XJ=0.25U LAMBDA=0.0612279
+ NFS=1E+12 NEFF=1.001 NSS=1E+11 TPG=-1.0 RSH=120.6
+ CGDO=4.3E-10 CGSO=4.3E-10 CJ=0.0005 MJ=0.5052
+ CJSW=1.349E-10 MJSW=0.2417 PB=0.64

vdd 3 0 5
vin 1 0 5

M1 2 1 0 0 MOSN W=1.8u L=1.2u 

M2 2 1 3 3 MOSP W=1.8u L=1.2u 


.control 

DC vdd 0 5 0.01
plot  -vdd#branch*V(3) 

.endc
.end
```

## Power with a 0.2 pF load and a 100 ns period

File: `guc/Lab_10_1c1.cir`.

```spice
* Arsiv devre kaydi
1c

.MODEL MOSN NMOS LEVEL=2 LD=0.15U TOX=200.0E-10
+ NSUB=5.36726E+15 VTO=0.743469 KP=8.00059E-05 GAMMA=0.543
+ PHI=0.6 U0=655.881 UEXP=0.157282 UCRIT=31443.8
+ DELTA=2.39824 VMAX=55260.9 XJ=0.25U LAMBDA=0.0367072
+ NFS=1E+12 NEFF=1.001 NSS=1E+11 TPG=1.0 RSH=70.00
+ CGDO=4.3E-10 CGSO=4.3E-10 CJ=0.0003 MJ=0.6585
+ CJSW=8.0E-10 MJSW=0.2402 PB=0.58

.MODEL MOSP PMOS LEVEL=2 LD=0.15U TOX=200.0E-10
+ NSUB=4.3318E+15 VTO=-0.738861 KP=2.70E-05 GAMMA=0.58
+ PHI=0.6 U0=261.977 UEXP=0.323932 UCRIT=65719.8
+ DELTA=1.79192 VMAX=25694 XJ=0.25U LAMBDA=0.0612279
+ NFS=1E+12 NEFF=1.001 NSS=1E+11 TPG=-1.0 RSH=120.6
+ CGDO=4.3E-10 CGSO=4.3E-10 CJ=0.0005 MJ=0.5052
+ CJSW=1.349E-10 MJSW=0.2417 PB=0.64

vdd 3 0 5
cl 2 0 0.2p
Vin 1 0 pulse (0 5 0 1n 1n 50n 100n)

M1 2 1 0 0 MOSN W=1.8u L=1.2u NRS=0.333 NRD=0.333
+ AD=6.5p PD=9.0u AS=6.5p PS=9.0u

M2 2 1 3 3 MOSP W=5.4u L=1.2u NRS=0.333 NRD=0.333
+ AD=6.5p PD=9.0u AS=6.5p PS=9.0u

.control 
tran 0.1ns 400ns
plot -vdd#branch*v(3) 

.endc
.end
```

## Level 49 model, W=90 µm and L=1 µm

File: `mos/uzun-kanal-level49.cir`.

```spice
*Soru 2 a

.MODEL MOSN NMOS LEVEL = 49
+LINT = 4.E-08 TOX = 4.E-09 VTH0 = 0.3999 RDSW = 250
+LMIN=1.8E-7 LMAX=1.8E-7 WMIN=1.8E-7 WMAX=1.0E-4 TREF=27.0 VERSION =3.1
+XJ= 6.0000000E-08 NCH= 5.9500000E+17
+LLN= 1.0000000 LWN= 1.0000000 WLN= 0.00 WWN= 0.00 LL= 0.00
+LW= 0.00 LWL= 0.00 WINT= 0.00 WL= 0.00 WW= 0.00 WWL= 0.00
+MOBMOD= 1 BINUNIT= 2 XL= 0
+XW= 0 BINFLAG= 0 DWG= 0.00 DWB= 0.00
+K1= 0.5613000 K2= 1.0000000E-02
+K3= 0.00 DVT0= 8.0000000 DVT1= 0.7500000
+DVT2= 8.0000000E-03 DVT0W= 0.00 DVT1W= 0.00
+DVT2W= 0.00 NLX= 1.6500000E-07 W0= 0.00
+K3B= 0.00 NGATE= 5.0000000E+20
+VSAT= 1.3800000E+05 UA= -7.0000000E-10 UB= 3.5000000E-18
+UC= -5.2500000E-11 PRWB= 0.00
+PRWG= 0.00 WR= 1.0000000 U0= 3.5000000E-02
+A0= 1.1000000 KETA= 4.0000000E-02 A1= 0.00
+A2= 1.0000000 AGS= -1.0000000E-02 B0= 0.00 B1= 0.00
+CDSC= 0.00 CDSCB= 0.00 CDSCD= 0.00
+ETA0= 0.2200000 ETAB= 0.00 DSUB= 0.8000000
+PCLM= 5.0000000E-02 PDIBLC1= 1.2000000E-02 PDIBLC2= 7.5000000E-03
+PDIBLCB= -1.3500000E-02 DROUT= 1.7999999E-02 PSCBE1= 8.6600000E+08
+PSCBE2= 1.0000000E-20 PVAG= -0.2800000 DELTA= 1.0000000E-02
+ALPHA0= 0.00 BETA0= 30.0000000
+KT1= -0.3700000 KT2= -4.0000000E-02 AT= 5.5000000E+04
+UTE= -1.4800000 UA1= 9.5829000E-10 UB1= -3.3473000E-19
+UC1= 0.00 KT1L= 4.0000000E-09 PRT= 0.00
+CJ= 0.00365 MJ= 0.54 PB= 0.982
+CJSW= 7.9E-10 MJSW= 0.31 PHP= 0.841
+CTA= 0 CTP= 0 PTA= 0
+PTP= 0 JS=1.50E-08 JSW=2.50E-13
+N=1.0 XTI=3.0 CGDO=2.786E-10
+CGSO=2.786E-10 CGBO=0.0E+00 CAPMOD= 2
+NQSMOD= 0 ELM= 5 XPART= 1
+CGSL= 1.6E-10 CGDL= 1.6E-10 CKAPPA= 2.886
+CF= 1.069E-10 CLC= 0.0000001 CLE= 0.6
+DLC= 4E-08 DWC= 0 VFBCV= -1

M1 3 1 0 2 MOSN W=90u L=1u NRS=0.333 NRD=0.333
+ AD=6.5p PD=9.0u AS=6.5p PS=9.0u


VIN 1 0 0V pulse(0V 5V 0 1ns 1ns 50ns 100ns)
VDD 3 0 5V
VBS 2 0 0V

.control


dc VDD 0V 2V 0.1V VIN 0.2V 2V 0.2V 
plot -VDD#branch vs v(3)


.endc
```

## Gate and body voltage sweep

File: `mos/nmos2.cir`.

```spice
* Arsiv devre kaydi

.MODEL NMOS NMOS LEVEL = 3 
+ TOX = 200E-10 NSUB = 1E17 GAMMA = 0.5 
+ PHI = 0.7 VTO = 0.8 DELTA = 3.0 
+ UO = 650 ETA = 3.0E-6 THETA = 0.1 
+ KP = 120E-6 VMAX = 1E5 KAPPA = 0.3 
+ RSH = 0 NFS = 1E12 TPG = 1 
+ XJ = 500E-9 LD = 100E-9 
+ CGDO = 200E-12 CGSO = 200E-12 CGBO = 1E-10 
+ CJ = 400E-6 PB = 1 MJ = 0.5 
+ CJSW = 300E-12 MJSW = 0.5

.MODEL PMOS PMOS LEVEL = 3 
+ TOX = 200E-10 NSUB = 1E17 GAMMA = 0.6
+ PHI = 0.7 VTO = -0.9 DELTA = 0.1 
+ UO = 250 ETA = 0 THETA = 0.1 
+ KP = 40E-6 VMAX = 5E4 KAPPA = 1 
+ RSH = 0 NFS = 1E12 TPG = -1 
+ XJ = 500E-9 LD = 100E-9 
+ CGDO = 200E-12 CGSO = 200E-12 CGBO = 1E-10 
+ CJ = 400E-6 PB = 1 MJ = 0.5 
+ CJSW = 300E-12 MJSW = 0.5

M1 2 1 4 3 NMOS W=1.8u L=1.2u NRS=0.333 NRD=0.333 
+ AD=6.5p PD=9.0u AS=6.5p PS=9.0u 

*M2 D G S B MOSP W=1.8u L=1.2u NRS=0.333 NRD=0.333 
*+ AD=6.5p PD=9.0u AS=6.5p PS=9.0u 

VIN 1 0 
Vdd 2 0 5
Vbs 0 3 5
Vsamp 4 0 0

*Alter M1 L=1u 

.control

dc VIN 0 5 0.1 Vbs 0 5 0.5
plot vsamp#branch vs V(1)
.endc
```

## PMOS width experiment

File: `mos/pmos3.cir`.

```spice
* Arsiv devre kaydi

.MODEL NMOS NMOS LEVEL = 3 
+ TOX = 200E-10 NSUB = 1E17 GAMMA = 0.5 
+ PHI = 0.7 VTO = 0.8 DELTA = 3.0 
+ UO = 650 ETA = 3.0E-6 THETA = 0.1 
+ KP = 120E-6 VMAX = 1E5 KAPPA = 0.3 
+ RSH = 0 NFS = 1E12 TPG = 1 
+ XJ = 500E-9 LD = 100E-9 
+ CGDO = 200E-12 CGSO = 200E-12 CGBO = 1E-10 
+ CJ = 400E-6 PB = 1 MJ = 0.5 
+ CJSW = 300E-12 MJSW = 0.5

.MODEL PMOS PMOS LEVEL = 3 
+ TOX = 200E-10 NSUB = 1E17 GAMMA = 0.6
+ PHI = 0.7 VTO = -0.9 DELTA = 0.1 
+ UO = 250 ETA = 0 THETA = 0.1 
+ KP = 40E-6 VMAX = 5E4 KAPPA = 1 
+ RSH = 0 NFS = 1E12 TPG = -1 
+ XJ = 500E-9 LD = 100E-9 
+ CGDO = 200E-12 CGSO = 200E-12 CGBO = 1E-10 
+ CJ = 400E-6 PB = 1 MJ = 0.5 
+ CJSW = 300E-12 MJSW = 0.5

*M1 2 1 4 3 NMOS W=1.8u L=1.2u NRS=0.333 NRD=0.333 
*+ AD=6.5p PD=9.0u AS=6.5p PS=9.0u 

M2 4 1 2 3 PMOS W=1.8u L=1.2u NRS=0.333 NRD=0.333 
+ AD=6.5p PD=9.0u AS=6.5p PS=9.0u 

VIN 0 1 2
Vdd 0 2 5
Vbs 0 3 0
Vsamp 4 0 0

.control

Alter M2 W=1.8u
*Alter M2 W=3.6u
*Alter M2 W=7.2u
dc Vdd 0 5 0.1
plot vsamp#branch vs V(2)
.endc
```

## Gain-frequency plot

File: `rc/ggg.m`.

```matlab
x=[0.872 0.475 0.26 0.18 0.14 0.116 0.096 0.08 0.064 0.04]
y=[10000 50000 100000 150000 200000 250000 300000 400000 500000 1000000]
plot(x,y,'r',x,y,'s');
xlabel('Kazanç (Vin/Vout)')
ylabel('Frekans')
```

## Phase-frequency plot

File: `rc/gggggg.m`.

```matlab
y=[17.63 50.9 69.12 73.07 80.64 112.5 72.43 81.29 59.4 79.2]
x=[10000 50000 100000 150000 200000 250000 300000 400000 500000 1000000]
plot(x,y,'r',x,y,'s');
xlabel('Frekans')
ylabel('FAZ FARKI')
```

## NMOS with resistor load and a 3 V supply

File: `tersleyici/soru1a.cir`.

```spice
* Arsiv devre kaydi
Soru1a

.MODEL MOSN NMOS LEVEL=2 LD=0.15U TOX=200.0E-10
+ NSUB=5.36726E+15 VTO=0.743469 KP=8.00059E-05 GAMMA=0.543
+ PHI=0.6 U0=655.881 UEXP=0.157282 UCRIT=31443.8
+ DELTA=2.39824 VMAX=55260.9 XJ=0.25U LAMBDA=0.0367072
+ NFS=1E+12 NEFF=1.001 NSS=1E+11 TPG=1.0 RSH=70.00
+ CGDO=4.3E-10 CGSO=4.3E-10 CJ=0.0003 MJ=0.6585
+ CJSW=8.0E-10 MJSW=0.2402 PB=0.58



VDD 3 0 DC 3
VIN 1 0 PULSE(0 3.1 0 1ns 1ns 5ns 10ns)

M1 2 1 0 0 MOSN W=1.8u L=1.2u NRS=0.333 NRD=0.333
+ AD=6.5p PD=9.0u AS=6.5p PS=9.0u

R1 3 2 100K
C1 2 0 1F

.CONTROL
DC VIN 0 3.1 0.1
PLOT V(2) VS V(1)
.ENDC
```

## Ring of five inverters with 100 fF loads

File: `halka/y6-3d.txt`.

```spice
**
.MODEL MOSN NMOS LEVEL=2 LD=0.15U TOX=200.0E-10 
+ NSUB=5.36726E+15 VTO=0.743469 KP=8.00059E-05 GAMMA=0.543 
+ PHI=0.6 U0=655.881 UEXP=0.157282 UCRIT=31443.8 
+ DELTA=2.39824 VMAX=55260.9 XJ=0.25U LAMBDA=0.0367072 
+ NFS=1E+12 NEFF=1.001 NSS=1E+11 TPG=1.0 RSH=70.00 
+ CGDO=4.3E-10 CGSO=4.3E-10 CJ=0.0003 MJ=0.6585 
+ CJSW=8.0E-10 MJSW=0.2402 PB=0.58 

.MODEL MOSP PMOS LEVEL=2 LD=0.15U TOX=200.0E-10 
+ NSUB=4.3318E+15 VTO=-0.738861 KP=2.70E-05 GAMMA=0.58
+ PHI=0.6 U0=261.977 UEXP=0.323932 UCRIT=65719.8 
+ DELTA=1.79192 VMAX=25694 XJ=0.25U LAMBDA=0.0612279 
+ NFS=1E+12 NEFF=1.001 NSS=1E+11 TPG=-1.0 RSH=120.6 
+ CGDO=4.3E-10 CGSO=4.3E-10 CJ=0.0005 MJ=0.5052 
+ CJSW=1.349E-10 MJSW=0.2417 PB=0.64

.subckt inv 1 3 
M1 3 1 0 0 MOSN W=1.8u L=1.2u NRS=0.333 NRD=0.333 
+ AD=6.5p PD=9.0u AS=6.5p PS=9.0u 
M2 3 1 2 2 MOSP W=5.4u L=1.2u NRS=0.333 NRD=0.333 
+ AD=6.5p PD=9.0u AS=6.5p PS=9.0u 
VDD 2 0 3.2V 
CL1 3 0 100f
.ends



xinv1 1 2 inv
xinv2 2 3 inv
xinv3 3 4 inv
xinv4 4 5 inv
xinv5 5 1 inv

.control
TRAN 1NS 200nS
plot V(2) 
plot V(3) 
plot V(4) 
plot V(6) 
.endc
```
