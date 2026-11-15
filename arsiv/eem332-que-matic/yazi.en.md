---
baslik: EEM332 Microprocessors: Que-Matic Project with the PIC16F877
ozet: A queue number system for three transaction types and service counters; ports, displays, flowchart, and bill of materials.
---

This post brings together the related notes and assignments from the Başkent University **EEM332 Microprocessors** course archive (2006; together with later archive copies). A queue number system for three transaction types and service counters; ports, displays, flowchart, and bill of materials. Works prepared by a friend and course documents are presented together; student names, numbers, and group information have been removed. PDF archive copies of the documents and, where available, the source code can be downloaded as a ZIP at the end of the post.

## 16F877

```asm
;PİC İSMİ;16F877(A)
;PİC FREKANSI;4 MHZ
;DAHİLİ KOMUT CYCLE;1 MHZ
;SİGORTA DURUMU;ON
;WATCHDOG TİMER;OFF
;PROGRAM CALISMASI;
;ACIKLAMA;
;
;*********************************************************************** º
;*********************************************************************** º


	LIST	P=16F877
	INCLUDE	"P16F877.INC"

;*********************************
;*****DEFINE TANIMLAMA BLOGU******
;*********************************


;*********************************
;******MACRO TANIMLAMA BLOGU******
;*********************************

;*********************************
;******ADRES TANIMLAMA BLOGU******
;*********************************
CBLOCK	0x20
SAYAC_A
SAYAC_B
SAYAC_C
iNDEX
NEXTA1
NEXTA2
SAYAC1
SERiAL_DATA
SERiAL_DATA_COUNTER
ENDC
;*********************************
;*******GIRIS CIKIS BLOGU*********
;*********************************
	ORG	0x000
	CLRF	PORTA
	CLRF	PORTB
	CLRF	PORTC
	CLRF	PORTD
	CLRF	PORTE
	BANK1
	MOVLW	0x07
	MOVWF	ADCON1
	MOVLW	0xF8
	MOVWF	TRISA
	CLRF	TRISB
	CLRF	TRISC
	CLRF	TRISD
	CLRF	TRISE
	BANK0
	CLRF	PORTA
	CLRF	PORTB
	CLRF	PORTC
	CLRF	PORTD
	CLRF	PORTE
;*********************************
;*******ANA PROGRAM KISMI*********
;*********************************
	
START
	MOVLW	0xFF
	MOVWF	SAYAC_A
	MOVLW	0xFF
	MOVWF	SAYAC_B
	MOVLW	0xFF
	MOVWF	SAYAC_C
START1	
	CALL	TUS_TARA
	CALL	TIMER_KEYPAD
	GOTO	START1

;*********************************
;******* ALT PROG. KISMI**********
;*********************************

TUS_TARA
	
SATIR0
	MOVLW	0X01
	MOVWF	PORTA
A_BiR				;0.SATIR AKTİF
	BTFSS	PORTA,3
	GOTO	A_iKi
	CALL	TIMER_KEYPAD
A_1
	BTFSC	PORTA,3
	GOTO	A_1
	CALL	TIMER_KEYPAD
	iNCF 	SAYAC_A,F
	MOVLW	0x0A
	XORWF	SAYAC_A,W
	BTFSC	STATUS,2
	CALL	SIFIRLA_A
	MOVF	SAYAC_A,W
	CALL	SERiAL_DATA_GONDER_1
	MOVLW	0x06
	MOVWF	SERiAL_DATA
	CALL	SERiAL_DATA_GONDER_0
	RETURN
A_iKi
	BTFSS	PORTA,4
	GOTO	A_UC
	CALL	TIMER_KEYPAD
A_2
	BTFSC	PORTA,4
	GOTO	A_2
	CALL	TIMER_KEYPAD	
	iNCF 	SAYAC_A,F
	MOVLW	0x0A
	XORWF	SAYAC_A,W
	BTFSC	STATUS,2
	CALL	SIFIRLA_A
	MOVF	SAYAC_A,W
	ANDLW	0x0F
	CALL	DEC_TABLE
	MOVWF	SERiAL_DATA
	CALL	SERiAL_DATA_GONDER_3
	MOVLW	0x06
	MOVWF	SERiAL_DATA
	CALL	SERiAL_DATA_GONDER_2
	RETURN
A_UC
	BTFSS	PORTA,5
	GOTO	SATIR1
	CALL	TIMER_KEYPAD
A_3
	BTFSC	PORTA,5
	GOTO	A_3
	CALL	TIMER_KEYPAD
	iNCF 	SAYAC_A,F
	MOVLW	0x0A
	XORWF	SAYAC_A,W
	BTFSC	STATUS,2
	CALL	SIFIRLA_A
	MOVF	SAYAC_A,W
	ANDLW	0x0F
	CALL	DEC_TABLE
	MOVWF	SERiAL_DATA
	CALL	SERiAL_DATA_GONDER_5
	MOVLW	0x06
	MOVWF	SERiAL_DATA
	CALL	SERiAL_DATA_GONDER_4
	RETURN
SATIR1
	MOVLW	0X02
	MOVWF	PORTA
B_BiR				;1.SATIR AKTİF
	BTFSS	PORTA,3
	GOTO	B_iKi
	CALL	TIMER_KEYPAD
B_1
	BTFSC	PORTA,3
	GOTO	B_1
	CALL	TIMER_KEYPAD
	MOVLW	0x0A
	XORWF	SAYAC_B,W
	BTFSC	STATUS,2
	CALL	SIFIRLA_B
	MOVF	SAYAC_B,W
	ANDLW	0x0F
	CALL	DEC_TABLE
	MOVWF	SERiAL_DATA
	CALL	SERiAL_DATA_GONDER_1
	MOVLW	0x5B
	MOVWF	SERiAL_DATA
	CALL	SERiAL_DATA_GONDER_0
	RETURN
B_iKi
	BTFSS	PORTA,4
	GOTO	B_UC
	CALL	TIMER_KEYPAD
B_2
	BTFSC	PORTA,4
	GOTO	B_2
	CALL	TIMER_KEYPAD
	iNCF 	SAYAC_B,F
	MOVLW	0x0A
	XORWF	SAYAC_B,W
	BTFSC	STATUS,2
	CALL	SIFIRLA_B
	MOVF	SAYAC_B,W
	ANDLW	0x0F
	CALL	DEC_TABLE
	MOVWF	SERiAL_DATA
	CALL	SERiAL_DATA_GONDER_3
	MOVLW	0x5B
	MOVWF	SERiAL_DATA
	CALL	SERiAL_DATA_GONDER_2
	RETURN
B_UC
	BTFSS	PORTA,5
	GOTO	SATIR2
	CALL	TIMER_KEYPAD
B_3
	BTFSC	PORTA,5
	GOTO	B_3
	CALL	TIMER_KEYPAD
	iNCF 	SAYAC_B,F
	MOVLW	0x0A
	XORWF	SAYAC_B,W
	BTFSC	STATUS,2
	CALL	SIFIRLA_B
	MOVF	SAYAC_B,W
	ANDLW	0x0F
	CALL	DEC_TABLE
	MOVWF	SERiAL_DATA
	CALL	SERiAL_DATA_GONDER_5
	MOVLW	0x5B
	MOVWF	SERiAL_DATA
	CALL	SERiAL_DATA_GONDER_4
	RETURN
SATIR2
	MOVLW	0X04
	MOVWF	PORTA
C_BiR				;2.SATIR AKTİF
	BTFSS	PORTA,3
	GOTO	C_iKi
	CALL	TIMER_KEYPAD
C_1
	GOTO	C_1
	CALL	TIMER_KEYPAD
	iNCF 	SAYAC_C,F
	MOVLW	0x0A
	XORWF	SAYAC_C,W
	BTFSC	STATUS,2
	CALL	SIFIRLA_C
	MOVF	SAYAC_C,W
	ANDLW	0x0F
	CALL	DEC_TABLE
	MOVWF	SERiAL_DATA
	CALL	SERiAL_DATA_GONDER_1
	MOVLW	0x4F
	MOVWF	SERiAL_DATA
	CALL	SERiAL_DATA_GONDER_0
	RETURN
C_iKi
	BTFSS	PORTA,4
	GOTO	C_UC
	CALL	TIMER_KEYPAD
C_2
	BTFSC	PORTA,4
	GOTO	C_2
	CALL	TIMER_KEYPAD
	iNCF 	SAYAC_C,F
	MOVLW	0x0A
	XORWF	SAYAC_C,W
	BTFSC	STATUS,2
	CALL	SIFIRLA_C
	MOVF	SAYAC_C,W
	ANDLW	0x0F
	CALL	DEC_TABLE
	MOVWF	SERiAL_DATA
	CALL	SERiAL_DATA_GONDER_3
	MOVLW	0x4F
	MOVWF	SERiAL_DATA
	CALL	SERiAL_DATA_GONDER_2
	RETURN
C_UC
	BTFSS	PORTA,5
	GOTO	TUS_TARA
	CALL	TIMER_KEYPAD
C_3
	BTFSC	PORTA,5
	GOTO	C_3
	CALL	TIMER_KEYPAD
	iNCF 	SAYAC_C,F
	MOVLW	0x0A
	XORWF	SAYAC_C,W
	BTFSC	STATUS,2
	CALL	SIFIRLA_C
	MOVF	SAYAC_C,W
	ANDLW	0x0F
	CALL	DEC_TABLE
	MOVWF	SERiAL_DATA
	CALL	SERiAL_DATA_GONDER_5
	MOVLW	0x4F
	MOVWF	SERiAL_DATA
	CALL	SERiAL_DATA_GONDER_4
	RETURN
DEC_TABLE
	ADDWF	PCL,F
	RETLW	0x3F
	RETLW	0x06
	RETLW	0x5B
	RETLW	0x4F
	RETLW	0x66
	RETLW	0x6D
	RETLW	0x7D
	RETLW	0x07
	RETLW	0x7F
	RETLW	0x6F

SERiAL_DATA_GONDER_0
	MOVLW	0x08
	MOVWF	SERiAL_DATA_COUNTER
SERiAL_DATA_0
	RLF	SERiAL_DATA,F
	BTFSS	STATUS,C
	GOTO	D0_0
	DATA_1			;DATA
	GOTO	D0_1
D0_0
	DATA_0			;DATA
D0_1
	CLOCK_1			;CLOCK
	CALL	TIMER_SERiAL
	CLOCK_0			;CLOCK
	DECFSZ	SERiAL_DATA_COUNTER,F
	GOTO	SERiAL_DATA_0
	LATC0_1
	CALL	TIMER_SERiAL
	LATC0_0
	RETURN

SERiAL_DATA_GONDER_1
	MOVLW	0x08
	MOVWF	SERiAL_DATA_COUNTER
SERiAL_DATA_1
	RLF	SERiAL_DATA,F
	BTFSS	STATUS,C
	GOTO	D1_0
	DATA_1			;DATA
	GOTO	D1_1
D1_0
	DATA_0			;DATA
D1_1
	CLOCK_1			;CLOCK
	CALL	TIMER_SERiAL
	CLOCK_0			;CLOCK
	DECFSZ	SERiAL_DATA_COUNTER,F
	GOTO	SERiAL_DATA_1
	LATC1_1
	CALL	TIMER_SERiAL
	LATC1_0
	RETURN
SERiAL_DATA_GONDER_2
	MOVLW	0x08
	MOVWF	SERiAL_DATA_COUNTER
SERiAL_DATA_2
	RLF	SERiAL_DATA,F
	BTFSS	STATUS,C
	GOTO	D2_0
	DATA_1			;DATA
	GOTO	D2_1
D2_0
	DATA_0			;DATA
D2_1
	CLOCK_1			;CLOCK
	CALL	TIMER_SERiAL
	CLOCK_0			;CLOCK
	DECFSZ	SERiAL_DATA_COUNTER,F
	GOTO	SERiAL_DATA_2
	LATC2_1
	CALL	TIMER_SERiAL
	LATC2_0
	RETURN

SERiAL_DATA_GONDER_3
	MOVLW	0x08
	MOVWF	SERiAL_DATA_COUNTER
SERiAL_DATA_3
	RLF	SERiAL_DATA,F
	BTFSS	STATUS,C
	GOTO	D3_0
	DATA_1			;DATA
	GOTO	D3_1
D3_1
	DATA_0			;DATA
D3_0
	CLOCK_1			;CLOCK
	CALL	TIMER_SERiAL
	CLOCK_0			;CLOCK
	DECFSZ	SERiAL_DATA_COUNTER,F
	GOTO	SERiAL_DATA_3
	LATC3_1
	CALL	TIMER_SERiAL
	LATC3_0
	RETURN
SERiAL_DATA_GONDER_4
	MOVLW	0x08
	MOVWF	SERiAL_DATA_COUNTER
SERiAL_DATA_4
	RLF	SERiAL_DATA,F
	BTFSS	STATUS,C
	GOTO	D4_0
	DATA_1			;DATA
	GOTO	D4_1
D4_1
	DATA_0			;DATA
D4_0
	CLOCK_1			;CLOCK
	CALL	TIMER_SERiAL
	CLOCK_0			;CLOCK
	DECFSZ	SERiAL_DATA_COUNTER,F
	GOTO	SERiAL_DATA_4
	LATC4_1
	CALL	TIMER_SERiAL
	LATC4_0
	RETURN

SERiAL_DATA_GONDER_5
	MOVLW	0x08
	MOVWF	SERiAL_DATA_COUNTER
SERiAL_DATA_5
	RLF	SERiAL_DATA,F
	BTFSS	STATUS,C
	GOTO	D5_0
	DATA_1			;DATA
	GOTO	D5_1
D5_1
	DATA_0			;DATA
D5_0
	CLOCK_1			;CLOCK
	CALL	TIMER_SERiAL
	CLOCK_0			;CLOCK
	DECFSZ	SERiAL_DATA_COUNTER,F
	GOTO	SERiAL_DATA_5
	LATC5_1
	CALL	TIMER_SERiAL
	LATC5_0
	RETURN
SIFIRLA_A
	MOVLW	0xFF
	MOVWF	SAYAC_A
	iNCF	SAYAC_A,F
	RETURN
SIFIRLA_B
	MOVLW	0xFF
	MOVWF	SAYAC_B
	iNCF	SAYAC_B,F
	RETURN
SIFIRLA_C
	MOVLW	0xFF
	MOVWF	SAYAC_C
	iNCF	SAYAC_C,F
	RETURN

TIMER_SERiAL
	MOVLW	0x05
	MOVWF	SAYAC1
NEXT_LOW_11
	DECFSZ	SAYAC1,F
	GOTO	NEXT_LOW
	RETURN

TiMER_KEYPAD
	MOVLW	0xFF
	MOVWF	NEXTA1
NEXT1_KEYPAD
	MOVLW	0xFF
	MOVWF	NEXTA2
NEXT2_KEYPAD
	DECFSZ	NEXTA2,F
	GOTO	NEXT2_KEYPAD
	DECFSZ	NEXTA1,F
	GOTO	NEXT1_KEYPAD
	RETURN

;*********************************
;*******PROGRAM BITIS KISMI*******
;*********************************
	END
```

## New Microsoft Excel Worksheet

### MATERIAL USED            QTY   UNIT PRICE (YTL)   PRICE (YTL)

16F877 (PIC)              1           15.00             15.00

```asm
Seven Segment Ekran           6            2.00             12.00
```

74CH595 serial-to-parallel register    6            1.50              9.00 470 ohm resistor          6            0.50              3.00 0 ohm fuse jumper wire    11           0.40              4.40 10K resistor         6            0.50              3.00 470 uF capacitor           1            0.60              0.60 100 nF capacitor           1            0.25              0.25 22 pF capacitor           2            0.15              0.30 4 MHZ crystal       1            0.30              0.30

```asm
Push Buton               10           0.50              5.00
```

Printed circuit board costs        1            8.00              8.00 Regulator                2            0.40              0.80 9 V battery            1            2.00              2.00

### TOTAL              63.65

## New Microsoft Word Document (3)

### FLOWCHART

### START

### A

### SELECT PORT FOR THE TRANSACTION TO BE PERFORMED

### SELECT TRANSACTION TYPE

### A                                B                             C

### Y=                                 Z=

### X

=

Counter                           Counter                             Counter number                       number                         number determine                        determine                          determine

Selected                          Selected                         Selected

### 1X                                2Y                              3Z

as                           as                         as determine                          determine                         determine

Was transaction A                     Was transaction B                            Was transaction C y= x=

y+              selected again?                               selected again? x+

1                           z= z   +1              selected again?

Write to counter (desk)                     Write to counter (desk)                      Write to counter (desk)

### 1X                                   2Y                                    3Z

write                                  write                                 write

### END

![New Microsoft Word Document (3): page 1, circuit, table and figures](sekil-759-01.jpg "New Microsoft Word Document (3), page 1.")

## proje20

```asm
;PİC İSMİ;16F877(A)
;PİC FREKANSI;4 MHZ
;DAHİLİ KOMUT CYCLE;1 MHZ
;SİGORTA DURUMU;ON
;WATCHDOG TİMER;OFF
;PROGRAM CALISMASI;
;ACIKLAMA; EEM-332 PROJE QUE-MATİC
;
;*********************************************************************** º
;*********************************************************************** º
```

```asm
LIST P=16F877
INCLUDE    "P16F877.INC"
```

```asm
;*********************************
;*****DEFINE TANIMLAMA BLOGU******
;*********************************
```

```asm
;*********************************
;******MACRO TANIMLAMA BLOGU******
;*********************************
```

```asm
;*********************************
;******ADRES TANIMLAMA BLOGU******
;*********************************
```

CBLOCK      0x20

### SAYAC_A

### SAYAC_B

### SAYAC_C

iNDEX

### NEXTA1

### NEXTA2

### SAYAC1

SERiAL_DATA SERiAL_DATA_COUNTER

```asm
ENDC
;*********************************
;*******GIRIS CIKIS BLOGU*********
;*********************************
ORG 0x000
CLRF PORTA
CLRF PORTB
CLRF PORTC
CLRF PORTD
CLRF PORTE
BANK1
MOVLW       0x07
MOVWF       ADCON1
```

```asm
MOVLW       0xF8
MOVWF       TRISA
CLRF TRISB
CLRF TRISC
CLRF TRISD
CLRF TRISE
BANK0
CLRF PORTA
CLRF PORTB
CLRF PORTC
CLRF PORTD
CLRF PORTE
;*********************************
;*******ANA PROGRAM KISMI*********
;*********************************
```

### START

```asm
MOVLW     0xFF
MOVWF     SAYAC_A
MOVLW     0xFF
MOVWF     SAYAC_B
MOVLW     0xFF
MOVWF     SAYAC_C
START1
CALL TUS_TARA
CALL TIMER_KEYPAD
GOTO START1
```

```asm
;*********************************
;******* ALT PROG. KISMI**********
;*********************************
```

### TUS_TARA

### SATIR0

```asm
MOVLW      0X01
MOVWF      PORTA
```

A_BiR                 ;0.SATIR AKTİF

```asm
BTFSSPORTA,3
GOTO A_iKi
CALL TIMER_KEYPAD
A_1
BTFSC      PORTA,3
GOTO A_1
CALL TIMER_KEYPAD
iNCF SAYAC_A,F
MOVLW      0x0A
```

### XORWF      SAYAC_A,W

```asm
BTFSC      STATUS,2
CALL SIFIRLA_A
```

```asm
MOVFSAYAC_A,W
CALL SERiAL_DATA_GONDER_1
MOVLW     0x06
MOVWF     SERiAL_DATA
CALL SERiAL_DATA_GONDER_0
RETURN
A_iKi
BTFSSPORTA,4
GOTO A_UC
CALL TIMER_KEYPAD
A_2
BTFSC      PORTA,4
GOTO A_2
CALL TIMER_KEYPAD
iNCF SAYAC_A,F
MOVLW      0x0A
```

### XORWF      SAYAC_A,W

```asm
BTFSC      STATUS,2
CALL SIFIRLA_A
MOVFSAYAC_A,W
ANDLW      0x0F
CALL DEC_TABLE
MOVWF      SERiAL_DATA
CALL SERiAL_DATA_GONDER_3
MOVLW      0x06
MOVWF      SERiAL_DATA
CALL SERiAL_DATA_GONDER_2
RETURN
A_UC
BTFSSPORTA,5
GOTO SATIR1
CALL TIMER_KEYPAD
A_3
BTFSC      PORTA,5
GOTO A_3
CALL TIMER_KEYPAD
iNCF SAYAC_A,F
MOVLW      0x0A
```

### XORWF      SAYAC_A,W

```asm
BTFSC      STATUS,2
CALL SIFIRLA_A
MOVFSAYAC_A,W
ANDLW      0x0F
CALL DEC_TABLE
MOVWF      SERiAL_DATA
CALL SERiAL_DATA_GONDER_5
MOVLW      0x06
MOVWF      SERiAL_DATA
CALL SERiAL_DATA_GONDER_4
RETURN
```

### SATIR1

```asm
MOVLW      0X02
MOVWF      PORTA
```

B_BiR                 ;1.SATIR AKTİF

```asm
BTFSSPORTA,3
GOTO B_iKi
CALL TIMER_KEYPAD
B_1
BTFSC      PORTA,3
GOTO B_1
CALL TIMER_KEYPAD
MOVLW      0x0A
```

### XORWF      SAYAC_B,W

```asm
BTFSC      STATUS,2
CALL SIFIRLA_B
MOVFSAYAC_B,W
ANDLW      0x0F
CALL DEC_TABLE
MOVWF      SERiAL_DATA
CALL SERiAL_DATA_GONDER_1
MOVLW      0x5B
MOVWF      SERiAL_DATA
CALL SERiAL_DATA_GONDER_0
RETURN
B_iKi
BTFSSPORTA,4
GOTO B_UC
CALL TIMER_KEYPAD
B_2
BTFSC      PORTA,4
GOTO B_2
CALL TIMER_KEYPAD
iNCF SAYAC_B,F
MOVLW      0x0A
```

### XORWF      SAYAC_B,W

```asm
BTFSC      STATUS,2
CALL SIFIRLA_B
MOVFSAYAC_B,W
ANDLW      0x0F
CALL DEC_TABLE
MOVWF      SERiAL_DATA
CALL SERiAL_DATA_GONDER_3
MOVLW      0x5B
MOVWF      SERiAL_DATA
CALL SERiAL_DATA_GONDER_2
RETURN
B_UC
BTFSSPORTA,5
GOTO SATIR2
CALL TIMER_KEYPAD
```

### B_3

```asm
BTFSC      PORTA,5
GOTO B_3
CALL TIMER_KEYPAD
iNCF SAYAC_B,F
MOVLW      0x0A
```

### XORWF      SAYAC_B,W

```asm
BTFSC      STATUS,2
CALL SIFIRLA_B
MOVFSAYAC_B,W
ANDLW      0x0F
CALL DEC_TABLE
MOVWF      SERiAL_DATA
CALL SERiAL_DATA_GONDER_5
MOVLW      0x5B
MOVWF      SERiAL_DATA
CALL SERiAL_DATA_GONDER_4
RETURN
SATIR2
MOVLW      0X04
MOVWF      PORTA
```

C_BiR                 ;2.SATIR AKTİF

```asm
BTFSSPORTA,3
GOTO C_iKi
CALL TIMER_KEYPAD
C_1
GOTO C_1
CALL TIMER_KEYPAD
iNCF SAYAC_C,F
MOVLW      0x0A
```

### XORWF      SAYAC_C,W

```asm
BTFSC      STATUS,2
CALL SIFIRLA_C
MOVFSAYAC_C,W
ANDLW      0x0F
CALL DEC_TABLE
MOVWF      SERiAL_DATA
CALL SERiAL_DATA_GONDER_1
MOVLW      0x4F
MOVWF      SERiAL_DATA
CALL SERiAL_DATA_GONDER_0
RETURN
C_iKi
BTFSSPORTA,4
GOTO C_UC
CALL TIMER_KEYPAD
C_2
BTFSC      PORTA,4
GOTO C_2
CALL TIMER_KEYPAD
```

```asm
iNCF SAYAC_C,F
MOVLW      0x0A
```

### XORWF      SAYAC_C,W

```asm
BTFSC      STATUS,2
CALL SIFIRLA_C
MOVFSAYAC_C,W
ANDLW      0x0F
CALL DEC_TABLE
MOVWF      SERiAL_DATA
CALL SERiAL_DATA_GONDER_3
MOVLW      0x4F
MOVWF      SERiAL_DATA
CALL SERiAL_DATA_GONDER_2
RETURN
C_UC
BTFSSPORTA,5
GOTO TUS_TARA
CALL TIMER_KEYPAD
C_3
BTFSC      PORTA,5
GOTO C_3
CALL TIMER_KEYPAD
iNCF SAYAC_C,F
MOVLW      0x0A
```

### XORWF      SAYAC_C,W

```asm
BTFSC      STATUS,2
CALL SIFIRLA_C
MOVFSAYAC_C,W
ANDLW      0x0F
CALL DEC_TABLE
MOVWF      SERiAL_DATA
CALL SERiAL_DATA_GONDER_5
MOVLW      0x4F
MOVWF      SERiAL_DATA
CALL SERiAL_DATA_GONDER_4
RETURN
DEC_TABLE
ADDWF      PCL,F
RETLW      0x3F
RETLW      0x06
RETLW      0x5B
RETLW      0x4F
RETLW      0x66
RETLW      0x6D
RETLW      0x7D
RETLW      0x07
RETLW      0x7F
RETLW      0x6F
```

SERiAL_DATA_GONDER_0

```asm
MOVLW     0x08
MOVWF     SERiAL_DATA_COUNTER
SERiAL_DATA_0
RLF SERiAL_DATA,F
BTFSSSTATUS,C
GOTO D0_0
```

### DATA_1              ;DATA

```asm
GOTO D0_1
D0_0
```

### DATA_0              ;DATA

### D0_1

```asm
CLOCK_1             ;CLOCK
CALL TIMER_SERiAL
CLOCK_0             ;CLOCK
DECFSZ    SERiAL_DATA_COUNTER,F
GOTO SERiAL_DATA_0
LATC0_1
CALL TIMER_SERiAL
LATC0_0
RETURN
```

SERiAL_DATA_GONDER_1

```asm
MOVLW     0x08
MOVWF     SERiAL_DATA_COUNTER
SERiAL_DATA_1
RLF SERiAL_DATA,F
BTFSSSTATUS,C
GOTO D1_0
```

### DATA_1              ;DATA

```asm
GOTO D1_1
D1_0
```

### DATA_0              ;DATA

### D1_1

```asm
CLOCK_1             ;CLOCK
CALL TIMER_SERiAL
CLOCK_0             ;CLOCK
DECFSZ    SERiAL_DATA_COUNTER,F
GOTO SERiAL_DATA_1
LATC1_1
CALL TIMER_SERiAL
LATC1_0
RETURN
SERiAL_DATA_GONDER_2
MOVLW     0x08
MOVWF     SERiAL_DATA_COUNTER
SERiAL_DATA_2
RLF SERiAL_DATA,F
BTFSSSTATUS,C
GOTO D2_0
```

### DATA_1              ;DATA

```asm
GOTO D2_1
D2_0
```

### DATA_0             ;DATA

### D2_1

```asm
CLOCK_1             ;CLOCK
CALL TIMER_SERiAL
CLOCK_0             ;CLOCK
DECFSZ    SERiAL_DATA_COUNTER,F
GOTO SERiAL_DATA_2
LATC2_1
CALL TIMER_SERiAL
LATC2_0
RETURN
```

SERiAL_DATA_GONDER_3

```asm
MOVLW     0x08
MOVWF     SERiAL_DATA_COUNTER
SERiAL_DATA_3
RLF SERiAL_DATA,F
BTFSSSTATUS,C
GOTO D3_0
```

### DATA_1              ;DATA

```asm
GOTO D3_1
D3_1
```

### DATA_0              ;DATA

### D3_0

```asm
CLOCK_1             ;CLOCK
CALL TIMER_SERiAL
CLOCK_0             ;CLOCK
DECFSZ    SERiAL_DATA_COUNTER,F
GOTO SERiAL_DATA_3
LATC3_1
CALL TIMER_SERiAL
LATC3_0
RETURN
SERiAL_DATA_GONDER_4
MOVLW     0x08
MOVWF     SERiAL_DATA_COUNTER
SERiAL_DATA_4
RLF SERiAL_DATA,F
BTFSSSTATUS,C
GOTO D4_0
```

### DATA_1              ;DATA

```asm
GOTO D4_1
D4_1
```

### DATA_0              ;DATA

### D4_0

```asm
CLOCK_1             ;CLOCK
CALL TIMER_SERiAL
CLOCK_0             ;CLOCK
```

```asm
DECFSZ    SERiAL_DATA_COUNTER,F
GOTO SERiAL_DATA_4
LATC4_1
CALL TIMER_SERiAL
LATC4_0
RETURN
```

SERiAL_DATA_GONDER_5

```asm
MOVLW     0x08
MOVWF     SERiAL_DATA_COUNTER
SERiAL_DATA_5
RLF SERiAL_DATA,F
BTFSSSTATUS,C
GOTO D5_0
```

### DATA_1              ;DATA

```asm
GOTO D5_1
D5_1
```

### DATA_0              ;DATA

### D5_0

```asm
CLOCK_1             ;CLOCK
CALL TIMER_SERiAL
CLOCK_0             ;CLOCK
DECFSZ    SERiAL_DATA_COUNTER,F
GOTO SERiAL_DATA_5
LATC5_1
CALL TIMER_SERiAL
LATC5_0
RETURN
SIFIRLA_A
MOVLW     0xFF
MOVWF     SAYAC_A
iNCF SAYAC_A,F
RETURN
SIFIRLA_B
MOVLW     0xFF
MOVWF     SAYAC_B
iNCF SAYAC_B,F
RETURN
SIFIRLA_C
MOVLW     0xFF
MOVWF     SAYAC_C
iNCF SAYAC_C,F
RETURN
```

TIMER_SERiAL

```asm
MOVLW     0x05
MOVWF     SAYAC1
NEXT_LOW_11
DECFSZ    SAYAC1,F
GOTO NEXT_LOW
```

```asm
RETURN
```

TiMER_KEYPAD

```asm
MOVLW     0xFF
MOVWF     NEXTA1
NEXT1_KEYPAD
MOVLW     0xFF
MOVWF     NEXTA2
NEXT2_KEYPAD
DECFSZ    NEXTA2,F
GOTO NEXT2_KEYPAD
DECFSZ    NEXTA1,F
GOTO NEXT1_KEYPAD
RETURN
```

```asm
;*********************************
;*******PROGRAM BITIS KISMI*******
;*********************************
END
```

## report

Başkent University, Department of Electrical and Electronics Engineering

EEM 332 – Microprocessors

Project Report

Project No: 20 Project Name: QUE-MATIC

### A) PROJECT DESCRIPTION

The subject of our project is a prototype of the que-matic (queuing machine) used in banks, which is located at the counters according to the issued queue number. The three counters in this que-matic are, in turn, authorized to determine the type of transaction to be performed and to increment the queue number according to the queue number issued for 3 different transactions.

The aim is that each counter determines the queue number according to transaction A, B, or C. When the type of job at a counter is finished, it will continue from the last remaining number according to the transaction it selects itself (transaction A, B, C).

### B) SYSTEM STRUCTURE

The hardware structure of the system is shown in the attached printouts. The hardware components in the system are:

- 1 16F877 (PIC)

- 6 seven-segment displays

- 6 74CH595 serial-to-parallel registers

- 6 470 ohm resistors

- 11 0 ohm fuse jumper wires

- 6 10K resistors

- 1 470 uF capacitor, 1 100 nF capacitor, and 2 22 pF capacitors

- 1 4 MHZ crystal

- 10 push buttons

- 2 regulators

- 1 9 V battery

### C) DESCRIPTION OF THE SYSTEM

A 16F877 PIC was used for programming. The reason for using this PIC is that there are 10 push buttons and the 16F877 has a sufficient number of ports to accommodate them and the other connections. A 4 MHZ crystal was used to supply the clock pulse to this PIC. The 74CH595 shift register IC was used to carry the data transmission between the PIC and the seven-segment displays by optimizing the number of ports used for the outputs taken from the PIC. Thanks to this IC, we send the data as a single bit instead of seven bits. In this way, we save ports. 9 push buttons were used to increment the queue number. 1 push button was used to reset the system. 11 fuse jumper wires were used. Thanks to these wires, if a short circuit occurs, the other circuit components will not be affected by the damage caused by the short circuit. Since the numbers for the 3 counters are two-digit, 6 seven-segment displays were used to see the outputs. 6 470 ohm resistors were used for the seven-segment displays. 2 capacitors were used to store the voltage required for the PIC. The 2 22 pF capacitors were connected to the crystal and from there to the PIC in order to provide the clock pulse.

### D) CONCLUSIONS AND COMMENTS

As a result of this work, we built a working prototype of the Que-matic system used in banks in real life. In terms of operation, we developed a system with practically no difference from the real thing; only the paper ticket system given to the customer in real-life systems is missing, and apart from that the system works like the original. During this project, a system used in daily life was designed. In addition,

the 16F877 was used in the project instead of the 16F84. In this way, we learned about the structure of a new PIC and understood the purpose of using PICs better. It was a useful exercise for understanding PIC programming at the desired level. We also had the opportunity to practice making printed circuit boards again. Thus, we saw what kinds of real-life applications PICs have.

### E) COST ANALYSIS

### MATERIAL USED            QTY   UNIT PRICE (YTL)   PRICE (YTL)

16F877 (PIC)             1           15.00             15.00

```asm
Seven Segment Ekran           6            2.00             12.00
```

74CH595 serial-to-parallel register    6            1.50              9.00 470 ohm resistor          6            0.50              3.00 0 ohm fuse jumper wire    11           0.40              4.40 10K resistor         6            0.50              3.00 470 uF capacitor           1            0.60              0.60 100 nF capacitor           1            0.25              0.25 22 pF capacitor           2            0.15              0.30 4 MHZ crystal       1            0.30              0.30

```asm
Push Buton               10           0.50              5.00
```

Printed circuit board costs        1            8.00              8.00 Regulator                2            0.40              0.80 9 V battery            1            2.00              2.00

### TOTAL              63.65

### F) REFERENCES

- Mikrodenetleyiciler ve PIC Programlama (Microcontrollers and PIC Programming), Orhan

### ALTINBAŞAK

- Beta Yayınları; Bilgisayar : Programlama PIC

Mikrodenetleyiciler (Microcontrollers)

- Alfa Yayınları, Elektronik Hobi: Güçlü TUĞAY

- www.antrak.com.tr

*Note: Since the 1999 creation record of the Excel cost table appears to be left over from a template, the 8 June 2006 record of the project report was used as the date of the post.*
