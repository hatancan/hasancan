---
baslik: EEM332 Mikroişlemciler: PIC Laboratuvar Kaynak Kodları ve Devreleri
ozet: PIC16F84(A) ile port yönlendirme, buton okuma ve LED çıkışı deney kodları.
---

Bu yazı, Başkent Üniversitesi **EEM332 Mikroişlemciler** ders arşivindeki ilgili notları ve uygulamaları bir araya getiriyor (2015–2015). PIC16F84(A) ile port yönlendirme, buton okuma ve LED çıkışı deney kodları. Bir arkadaşın hazırladığı çalışmalar ve ders belgeleri birlikte aktarılmış; öğrenci adları, numaraları ve grup bilgileri çıkarılmıştır. Belgelerin PDF arşiv kopyaları ve varsa kaynak kodları yazının sonunda ZIP olarak indirilebilir.

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

Proteus devre kaynağı indirme paketinde yer alır. Kişisel ad taşıyan dosya ve yol kayıtları anonimleştirilmiştir.

## 321654

Proteus devre kaynağı indirme paketinde yer alır. Kişisel ad taşıyan dosya ve yol kayıtları anonimleştirilmiştir.

## SKY122

Proteus devre kaynağı indirme paketinde yer alır. Kişisel ad taşıyan dosya ve yol kayıtları anonimleştirilmiştir.

## SKY122

Proteus devre kaynağı indirme paketinde yer alır. Kişisel ad taşıyan dosya ve yol kayıtları anonimleştirilmiştir.

## Kod ekran görüntüsü

PIC kodunun ekran görüntüsü, bu yazıdaki port yönlendirme ve LED döngüsü kaynaklarıyla birlikte okunmuştur. Metin olarak verilen kaynak kod esas alınmıştır; ekran görüntüsü indirmeye eklenmemiştir.
