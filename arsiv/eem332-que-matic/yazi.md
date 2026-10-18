---
baslik: EEM332 Mikroişlemciler: PIC16F877 ile Que-Matic Projesi
ozet: Üç işlem türü ve gişeler için sıra numarası sistemi; portlar, göstergeler, akış şeması ve malzeme tablosu.
---

Bu yazı, Başkent Üniversitesi **EEM332 Mikroişlemciler** ders arşivindeki ilgili notları ve uygulamaları bir araya getiriyor (2006; sonraki arşiv kopyalarıyla birlikte). Üç işlem türü ve gişeler için sıra numarası sistemi; portlar, göstergeler, akış şeması ve malzeme tablosu. Bir arkadaşın hazırladığı çalışmalar ve ders belgeleri birlikte aktarılmış; öğrenci adları, numaraları ve grup bilgileri çıkarılmıştır. Belgelerin PDF arşiv kopyaları ve varsa kaynak kodları yazının sonunda ZIP olarak indirilebilir.

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

## Yeni Microsoft Excel Çalışma Sayfası

### KULLANILAN MALZEME            ADET   BİRİM FİYATI (YTL)   FİYATI (YTL)

16F877 (pic)              1           15.00             15.00

```asm
Seven Segment Ekran           6            2.00             12.00
```

74CH595 seri paralel register    6            1.50              9.00 470 ohm’luk direnç          6            0.50              3.00 0 ohm’luk sigorta atlama teli    11           0.40              4.40 10K ‘lık direnç         6            0.50              3.00 470 uF kapasitans           1            0.60              0.60 100 nF kapasitans           1            0.25              0.25 22 pF kapasitans           2            0.15              0.30 4 MHZ frekanslı kristal       1            0.30              0.30

```asm
Push Buton               10           0.50              5.00
```

Baskı devre giderleri        1            8.00              8.00 Regüle                2            0.40              0.80 9 voltluk pil            1            2.00              2.00

### TOPLAM              63.65

## Yeni Microsoft Word Belgesi (3)

### AKIŞ ŞEMASI

### BAŞL

### A

### YAPILACAK İŞLEM İÇİN PORT BELİRLE

### İŞLEM TÜRÜ SEÇ

### A                                B                             C

### Y=                                 Z=

### X

=

Gişe                           Gişe                             Gişe numarası                       numarası                         numarası belirle                        belirle                          belirle

Seçilen                          Seçilen                         Seçilen

### 1X                                2Y                              3Z

olarak                           olarak                          olarak belirle                          belirle                         belirle

Tekrar A işlemi                     Tekrar B işlemi                            Tekrar C y= x=

y+              seçildi mi ?                               işlemi x+

1                           z= seçildi mi?                                             z   +1              seçildi mi ?

Gişeye (Bankoya)                     Gişeye (Bankoya)                      Gişeye (Bankoya)

### 1X                                   2Y                                    3Z

yaz                                  yaz                                   yaz

### BİTİR

![Yeni Microsoft Word Belgesi (3): sayfa 1, devre, tablo ve şekiller](sekil-759-01.jpg "Yeni Microsoft Word Belgesi (3), sayfa 1.")

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

## rapor

Başkent Üniversitesi Elektrik - Elektonik Mühendisliği Bölümü

EEM 332 – Mikroişlemciler

Proje Raporu

Proje No: 20 Proje Adı: QUE-MATİC

### A) PROJENİN TANIMI

Projemizin konusu bankalarda kullanılan, verilen sıra numarasına göre bankolarda bulunan que-matic’in (sıralandırma makinesi) prototipidir. Bu que-matic’te bulunan üç banko sırasıyla 3 farklı işlem için verilen sıra numarasına göre yapılacak işlem türünü belirleme ve sıra arttırma yetkisine sahiptir.

Amaç olarak ise her banko A, B yada C işlemine göre sıra numarasını belirlemektedir. Bir bankoda yapılan iş cinsi bittiğinde kendi belirleyeceği işleme göre (A,B,C işlemi) en son kalan sıradan itibaren devam edecektir.

### B) SİSTEM YAPISI

Ekte sunulan çıktılarda sistemin donanımsal yapısı gösterilmiştir. Sistemde yer alan donanımsal malzemeler.

- 1 adet 16F877 (pic)

- 6 adet seven segment ekran

- 6 adet 74CH595 seri paralel register

- 6 adet 470 ohm’luk direnç

- 11 adet 0 ohm’luk sigorta atlama teli

- 6 adet 10K ‘lık direnç

- 470 uf lık , 100 nf lık ,2 tane 22 pf lık kondansatör

- 1 adet 4 MHZ frekanslı kristal

- 10 adet push putton

- 2 adet regüle

- 1 adet 9 voltluk pil

### C) SİSTEMİN TANIMLANMASI

Programlamayı yapabilmek için 16F877 pıc’i kullanılmıştır. Bu pıc’ i kullanmamızın nedeni ise 10 adet push buton olduğu için ve 16F877 de de bunu ve diğer bağlantıları sağlayacak yeterli miktarda port bulunduğu için bu pıc tercih edilmiştir. Bu pıc’e clock pulse verebilmek için 4 MHZ frekansında kristal kullanılmıştır. Pıc den alınan outputları port kullanım sayısını optimize ederek seven segmentle pıc arasındaki veri iletimini sağlamak için 74CH595 shift register entegresi kullanılmıştır. Bu entegre sayesinde veriyi yedi bit yerine tek bit olarak gönderiyoruz. Böylece porttan tasarruf sağlarız. Sıra artırım işlemini sağlamak için 9 adet push buton kullanılmıştır. Sistemi resetlemek içinse 1 adet push buton kullanılmıştır. 11 adet sigorta atlama teli kullanılmıştır. Bu teller sayesinde eğer kısa devre olursa bunlar sayesinde diğer devre elemanı bu kısa devreden dolayı kaynaklanan zarardan etkilenmeyecektir. Çıktıları görebilmek için 3 gişe için çift haneli numaralar olmasından dolayı 6 adet seven segment kullanılmıştır. Seven segmentlerin kullanılması için 6 adet 470 ohm’luk dirençler kullanılmıştır. Pıc için gerekli gerilimi depolayabilmek için 2 adet kapasitans kullanılmıştır. 2 adet 22 pF’lık kapasitans ise clock pulse sağlanmak için kristale ordanda pıc’e bğlanmıştır.

### D) SONUÇ VE YORUMLAR

Bu çalışma sonucunda gerçek hayatta bankalarda kullanılan Que-matic sisteminin çalışan bir prototipini yapmış olduk. Çalışma durumu olarak gerçekten hiçbir farkı bulunmayan bir sistem geliştirdik, sadece gerçek hayattaki sistemlerde bulunan müşteriye verilen kağıt sistemi eksiktir, bunun haricinde sistem orijinal sistem gibi çalışmaktadır. Bu proje sürecinde günlük hayatta kullanılan bir sistem tasarlanmış oldu. Ayrıca

projede 16F84 yerine 16F877 kullanılmıştır. Bu sayede yeni bir pıc’ın yapısı hakkında bilgi sahibi olduk ve pıc’lerin kullanım amacı daha iyi anlaşılmış oldu. Pıc programlama istenilen düzeyde anlaşılması için faydalı bir çalışma olmuştur. Baskı devre yapımını tekrardan uygulama imkanı bulduk. Böylece Pıc’lerin gerçek hayatta ne tür uygulama alanları olduğunu görmüş olduk.

### E) MALİYET ANALİZİ

### KULLANILAN MALZEME            ADET   BİRİM FİYATI (YTL)   FİYATI (YTL)

16F877 (pic)             1           15,00             15,00

```asm
Seven Segment Ekran           6            2,00             12,00
```

74CH595 seri paralel register    6            1,50              9,00 470 ohm’luk direnç          6            0,50              3,00 0 ohm’luk sigorta atlama teli    11           0,40              4,40 10K ‘lık direnç         6            0,50              3,00 470 uF kapasitans           1            0,60              0,60 100 nF kapasitans           1            0,25              0,25 22 pF kapasitans           2            0,15              0,30 4 MHZ frekanslı kristal       1            0,30              0,30

```asm
Push Buton               10           0,50              5,00
```

Baskı devre giderleri        1            8,00              8,00 Regüle                2            0,40              0,80 9 voltluk pil            1            2,00              2,00

### TOPLAM              63,65

### F) KAYNAKLAR

- Mikrodenetleyiciler ve PIC Programlama, Orhan

### ALTINBAŞAK

- Beta Yayınları; Bilgisayar : Programlama PIC

Mikrodenetleyiciler

- Alfa Yayınları, Elektronik Hobi: Güçlü TUĞAY

- www.antrak.com.tr

*Not: Excel maliyet tablosunun 1999 oluşturma kaydı şablondan kalmış göründüğünden yazı tarihi için proje raporunun 8 Haziran 2006 tarihli kaydı esas alınmıştır.*
