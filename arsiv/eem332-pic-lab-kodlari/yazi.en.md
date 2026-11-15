---
baslik: EEM332 Microprocessors: PIC Laboratory Source Codes and Circuits
ozet: Lab experiment codes for port direction, button reading and LED output with the PIC16F84(A).
---

This post brings together the related notes and applications from the Başkent University **EEM332 Microprocessors** course archive (2015–2015). It covers lab experiment codes for port direction, button reading and LED output with the PIC16F84(A). Work prepared by a friend and course documents are presented together; student names, numbers and group information have been removed. PDF archive copies of the documents and, where available, source codes can be downloaded as a ZIP at the end of the post.

## calisma-886

```asm
		LIST P=16F84A
STATUS  EQU	H'03'
PORTB 	EQU H'06'
PORTA	EQU	H'05'
TRISB	EQU H'86'
TRISA	EQU	H'85'
		ORG 0X00
		CLRF PORTB
		BSF STATUS,5
		CLRF TRISB
		MOVLW H'FF'
		MOVWF TRISA
		BCF STATUS,5
BCF PORTA,0
TEKRAR
		BTFSS PORTA,0
		GOTO GIT
		MOVLW B'11110000'
		MOVWF PORTB
		GOTO TEKRAR
GIT
		MOVLW B'00001111'
		MOVWF PORTB
		GOTO TEKRAR
		END
```

## calisma-896

```asm
		LIST P=16F84A
STATUS  EQU	H'03'
PORTB 	EQU H'06'
PORTA	EQU	H'05'
TRISB	EQU H'86'
TRISA	EQU	H'85'
		ORG 0X00
		CLRF PORTB
		BSF STATUS,5
		CLRF TRISB
		MOVLW H'FF'
		MOVWF TRISA
		BCF STATUS,5
BCF PORTA,0
TEKRAR
		BTFSS PORTA,0
		GOTO GIT
		MOVLW B'00001111'
		MOVWF PORTB
		GOTO TEKRAR
GIT
		MOVLW B'11110000'
		MOVWF PORTB
		GOTO TEKRAR
		END
```

## calisma-909

```asm
		LIST P=16F84A
INCLUDE "P16F84A.INC"
		ORG 0X00
		CLRF PORTB
		BSF STATUS,5
		CLRF TRISB
		MOVLW H'FF'
		MOVWF TRISA
		BCF STATUS,5
TEKRAR
		BTFSS PORTA,0
		GOTO GIT
		MOVLW B'00001111'
		MOVWF PORTB
		GOTO TEKRAR
GIT
		MOVLW B'11110000'
		MOVWF PORTB
		GOTO TEKRAR
		END
```

## BG

```asm
	LIST P=16F84A
INCLUDE "P16F84A.INC"
	ORG 0X00
	CLRF PORTB
	BSF STATUS,5
	CLRF TRISB
	MOVLW H'FF'
	MOVWF TRISA
	BCF STATUS,5
	MOVLW B'00001010'
	MOVWF PORTB
	BTFSS PORTA,0
	GOTO SON
	COMF PORTB
SON 
    MOVLW H'FF'
    MOVWF PORTB
    
    END
```

## DENEY7

```asm
		LIST P=16F84A
STATUS  EQU	H'03'
PORTB 	EQU H'06'
PORTA	EQU	H'05'
TRISB	EQU H'86'
TRISA	EQU	H'85'
		ORG 0X00
		CLRF PORTB
		BSF STATUS,5
		CLRF TRISB
		MOVLW H'FF'
		MOVWF TRISA
		BCF STATUS,5
TEKRAR
		BTFSS PORTA,0
		GOTO GIT
		MOVLW B'00001111'
		MOVWF PORTB
		GOTO TEKRAR
GIT
		MOVLW B'11110000'
		MOVWF PORTB
		GOTO TEKRAR
		END
```

## calisma-738

The Proteus circuit source is included in the download package. Files and path entries containing personal names have been anonymized.

## 321654

The Proteus circuit source is included in the download package. Files and path entries containing personal names have been anonymized.

## SKY122

The Proteus circuit source is included in the download package. Files and path entries containing personal names have been anonymized.

## SKY122

The Proteus circuit source is included in the download package. Files and path entries containing personal names have been anonymized.

## Code screenshot

The screenshot of the PIC code was read together with the port direction and LED loop sources in this post. The source code given as text is taken as authoritative; the screenshot is not included in the download.
