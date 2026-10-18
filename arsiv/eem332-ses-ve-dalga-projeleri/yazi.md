---
baslik: EEM332 Mikroişlemciler: Arama Tonu, Buzzer ve Dalga Üretimi
ozet: PIC ile arama tonu ve buzzer; assembly ve BASIC kaynakları ile dalga üretimi çalışması.
---

Bu yazı, Başkent Üniversitesi **EEM332 Mikroişlemciler** ders arşivindeki ilgili notları ve uygulamaları bir araya getiriyor (2008–2016). PIC ile arama tonu ve buzzer; assembly ve BASIC kaynakları ile dalga üretimi çalışması. Bir arkadaşın hazırladığı çalışmalar ve ders belgeleri birlikte aktarılmış; öğrenci adları, numaraları ve grup bilgileri çıkarılmıştır. Belgelerin PDF arşiv kopyaları ve varsa kaynak kodları yazının sonunda ZIP olarak indirilebilir.

## proje rapor

Başkent Üniversitesi Elektrik - Elektronik Mühendisliği Bölümü

EEM 332 – Mikroişlemciler

Proje Raporu

Proje No: 22 Proje Adı: Arama Tonu (Dial Tone)

### PROJE

Bu projede 3 adet butonum bulunmaktadır. 1 nolu butona basıldığında default olarak belirlediğimiz 4 saniye değeri azalmaya başlamakta ve sayaç ise 1 nolu butona basılma sayısını tutmaktadır. 4 saniye değerimiz bittiği zaman basılma sayısı seven segment de görülmektedir. 4 saniye default süreyi kendi isteğimizle değistirebilmekteyiz. 3 nolu butona bastığımızda seven segment de ayar çizgisi çıkmakta ve devremiz süre ayarına hazır hale gelmektedir. 1 ve 2 nolu butonlardan ise süre ayarını azaltıp, arttırabilmekteyiz. Bu işlemlerden sonra tekrar 3 nolu butona bastığımızda devre tekrar en başa dönmektedir.

### KOD

```asm
LIST    p=16F84;
INCLUDE"P16F84.INC"
SAYAC1         EQU        H'0C'   ;Değişkenleri tanımladık
SAYAC2         EQU        H'0D'
HAFIZA         EQU        H'0E'
SANIYE         EQU        H'0F'   ;EQU deyimi bir hex adresi belirlenen
SURE           EQU        H'10'   ;etikete atar(s1,s2,s3…)
```

```asm
ORG H'00'
GOTO ILKDEGER                     ;Program ILKDEGER den başlıyor
ORG H'04'
GOTO INTP                         ;Interrupt geldiğinde INTP ye gider
```

### ILKDEGER

```asm
CLRF    PORTB
BSF     STATUS,5                    ;PORTB output PORTA input yapıldı
CLRF    TRISB                       ;TRISB 0 oldu ve output oldu
MOVLW   H'FF'
MOVWF   TRISA                       ;TRISA 1 oldu ve giriş oldu
BCF     STATUS,5
CLRF    HAFIZA                      ;HAFIZA yı sıfırladık
```

```asm
MOVLW   H'04'                       ;SANİYE 4 olarak atandı
MOVWF   SANIYE                      ;Default saniye değeri
MOVLW   H'3D'
MOVWF   SURE                        ;SURE değeri 3D(61) olarak atandı
```

### BASLA

```asm
BTFSC   PORTA,1                     ;PORTA nın 1.butonuna basılırsa
GOTO    BASLA                       ;devam et basılmassa BASLA ya git
```

```asm
BSF     STATUS,5      ;Pigde ayar yapmak için status 5 oldu(bank 1)
MOVLW   B'10010111'   ;256 ile carpmak için 111 oldu
MOVWF   OPTION_REG    ;Timer için ayar(256 cycle da timer 1 artar)
MOVLW   B'10100000'   ;İNTERRUPT ile ilgili
MOVWF   INTCON
BCF     STATUS,5
MOVLW   H'00'         ;TMR0 sıfırlandı (Timer)
MOVWF   TMR0           ;Timer 00 dan FF e sayacak
MOVFW   SANIYE         ;belirlediğimiz saniyeyi yazdırdık(default 4)
CALL     YAZDIR
MOVLW    h'00'        ;Ekran sıfırlandı
CALL     YAZDIR
```

### KAYIT

```asm
BTFSC   PORTA,1
GOTO    KAYIT                 ;butona basıldıysa devam et
```

```asm
INCF    HAFIZA                ;basıldıkça hafıza değeri arttı
MOVFW   HAFIZA                ;değer hafızaya atıldı
CALL     YAZDIR               ;değer yazdırıldı
GOTO     KAYIT                ;tekrar başa dönüldü
```

### DONGU

```asm
BTFSC   PORTA,4               ;3. butona basılmayı kontrol ediyor
GOTO    DONGU                 ;basılırsa devam ediyor ve çizgi
;4 saniye bitiminde buraya geliyor
UYARI
MOVLW   H'40'                 ;saniye ayarına geçti uyarısıdır
MOVWF   PORTB                 ;ortada çizgi cıkıyor
CALL    GECIKME
```

### BAK1

```asm
BTFSC   PORTA,1       ;1. butona basılıp basılmadığının kontrolü
GOTO    BAK2          ;1. butona basmaz isek BAK2 ye git
INCF    SANIYE        ;1. butona basarsak saniyeyi arttır
MOVFW   SANIYE
ANDLW   H'07'         ;Saniye 7 yi gemcesin diye and yaptık
MOVWF   SANIYE
CALL    YAZDIR
BAK2
BTFSC   PORTA,2       ; 2. butona basılıp basılmadığının kontrolü
GOTO    BAK3          ; 2. butona basmaz isek BAK2 ye git
DECF    SANIYE        ; 2. butona basarsak saniyeyi azalt
MOVFW   SANIYE
ANDLW   H'07'         ; Saniye 7 yi gemcesin diye and yaptık
MOVWF   SANIYE
CALL    YAZDIR
BAK3
```

```asm
BTFSC   PORTA,3          ; 3. butona basılıp basılmadığının kontrolü
GOTO    BAK1             ; 3. butona basmaz isek BAK1 e git
```

```asm
GOTO    BASLA            ; süre ayarı için olan döngüden çıkar
; ve tekrar başa döner
```

### GECIKME

```asm
MOVLW     H'FF'            ;Gecikmeyi arttırmak için FF yaptık (256)
MOVWF     SAYAC1
```

DONGU1                           ;Buton arklarını engellemek için

```asm
MOVLW     H'FF'
MOVWF     SAYAC2
DONGU2
DECFSZ    SAYAC2,1
GOTO      DONGU2
DECFSZ    SAYAC1,1
GOTO      DONGU1
RETURN
SEVENSEGMENT
```

```asm
ADDWF    PCL,1             ;PCL<---W(H'05')       ;Seven Segment de gösterim
RETLW    h'3f'              ; 0
RETLW    h'06'              ; 1
RETLW    h'5b'              ; 2
RETLW    h'4f'              ; 3
RETLW    h'66'              ; 4
RETLW    h'6d'              ; 5
RETLW    h'7d'              ; 6
RETLW    h'07'              ; 7
RETLW    h'7f'              ; 8
RETLW    h'6f'              ; 9
```

### INTP

```asm
BCF    INTCON,T0IF
DECFSZ SURE
RETFIE                   ;İnterrupt sağlanır
CALL   SURE_INDIR        ;Timer FF den 00 a gelmiş ise buraya gelinir
RETFIE                   ;Böylece Timerin sıfırlandığı anlaşılır
```

### SURE_INDIR

```asm
MOVLW     H'3D'
MOVWF     SURE             ;Süre ‘3D’ hex değeri kadar dönüyor
DECFSZ    SANIYE,1         ;0 değilse 1 azalt
RETURN
GOTO      DONGU
```

### YAZDIR

```asm
ANDLW    B'00001111'      ; Mod 16 yaptık çünkü seven segment 15 e
CALL     SEVENSEGMENT     ; kadar gösteriyor
MOVWF   PORTB
CALL    GECIKME
RETURN                           BAŞLA
```

### 1. BUTON KONTROLU

### NO                                       YE

### S

### SAYAÇI ARTTIR

### SÜREYİ AZALT

### SÜRE = = 0

### NO

### YE

### S

### 3. BUTON KONTROLU

### YE

### NO                                                                   S

### 1.VE 2. BUTON

### KONTROLU

### YE                                                                    YE

### S                                                                     S

### 1. BUTON                              2. BUTON

### SÜREYİ

### SÜREYİ                                 AZALT

### ARTTIR

### 3. BUTON KONTROLU

### YE                                                                         NO

### S

![proje rapor: sayfa 7, devre, tablo ve şekiller](sekil-957-07.jpg "proje rapor, sayfa 7.")

## calisma-971

```basic
'****************************************************************
'*  Name    : UNTITLED.BAS                                      *
'*  Author  : [select VIEW...EDITOR OPTIONS]                    *
'*  Notice  : Copyright (c) 2008 [select VIEW...EDITOR OPTIONS] *
'*          : All Rights Reserved                               *
'*  Date    : 14.05.2008                                        *
'*  Version : 1.0                                               *
'*  Notes   :                                                   *
'*          :                                                   *
'****************************************************************
trisa=%00011000
trisb=%10000000
SYMBOL  BIR=PORTA.3
SYMBOL  IKI=PORTA.4
SYMBOL  UC=PORTB.7
T VAR word
ZAMAN var byte
BILGI var byte
sayi var byte
x var byte
t=4000
LED var byte
porta=4
portb=%00111111
;****************************************************************
BASLA:
    if uc=0 then ayar
    if bir=0 then   
    pause 75
    count bir,t,bilgi
    x=bilgi
    gosub al
    portb=sayi
    endif
    goto basla  
    
AL:    LOOKUP X,[63,6,91,79,102,109,125,7,127,111,99,57],SAYI :RETURN    
    
AYAR:
    portb=%01000000
    if bir=0 then art
    if iki=0 then azal
    goto ayar
art:
    t=t+1000
    if t=8000 then
    t=7000
    endif
    porta=porta+1
    if porta=8 then
    porta=7
    endif
    while bir=0
    wend
    pause 100
bekle:
    if uc=0 then cik
    if bir=0 then art
    if iki=0 then azal
    goto bekle
cik:pause 50
    while uc=0
    wend 
    portb=%00111111
       goto basla
azal:    
    t=t-1000
    if t=0 then
    t=1000
    endif
    porta=porta-1
    if porta=0 then
    porta=1
    endif
    while iki=0
    wend
    pause 100
bekle1:
    if uc=0 then cik1
    if iki=0 then azal
    if bir=0 then art
    goto bekle1
cik1:pause 50
    while uc=0
    wend 
    portb=%00111111
   goto basla
```

## dalga

```asm
.MODEL SMALL
.STACK 100H
.DATA

DATA1 DB 99,?, 100 DUP ('$')
laf db "hiz giriniz: 1-hizli 2-orta 3-yavas","$"
erro db  "erroro",0dH,0ah,"$"

BAYRAK1A DB "  *                                                   ",0dH,0ah," * *                                                  ",0dH,0ah,"*   **************************************************",0dH,0ah,"$"
BAYRAK1B DB "       *                                              ",0dH,0ah,"      * *                                             ",0dH,0ah,"******   *********************************************",0dH,0ah,"$"
BAYRAK2A DB "            *                                         ",0dH,0ah,"           * *                                        ",0dH,0ah,"***********   ****************************************",0dH,0ah,"$"
BAYRAK2B DB "                 *                                    ",0dH,0ah,"                * *                                   ",0dH,0ah,"****************   ***********************************",0dH,0ah,"$"
BAYRAK3A DB "                      *                               ",0dH,0ah,"                     * *                              ",0dH,0ah,"*********************   ******************************",0dH,0ah,"$"
BAYRAK3B DB "                           *                          ",0dH,0ah,"                          * *                         ",0dH,0ah,"**************************   *************************",0dH,0ah,"$"
YOKET  DB  0dH,0ah,"$"


.CODE

MAIN PROC FAR
	MOV AX,@DATA
	MOV DS,AX
	MOV ES,AX

	JMP ILK

TEKRAR:	CALL CLRSCR

	MOV AH, 09H
	MOV DX, OFFSET yoket
	INT 21H

	MOV AH, 09H
	MOV DX, OFFSET erro
	INT 21H

ILK:	MOV AH, 09H
	MOV DX, OFFSET laf
	INT 21H		

	MOV SI,OFFSET Data1

	SUB AX,AX
	INT 16H
	MOV DL,AL
	MOV AH,02
	INT 21H
	MOV [SI],DL

	MOV AL,31H
	
	CMP DL,AL
	JZ  NO1
	INC AL
	CMP DL,AL
	JZ NO2
	INC AL
	CMP DL,AL
	JZ NO3
	JMP TEKRAR

NO1:  	MOV BX,1FFFH
	JMP STEP
NO2:	MOV BX,5FFFH
	JMP STEP
NO3:	MOV BX,9FFFH
	JMP STEP


step:	 mov cx,9fffH
bigloop: push cx

	
	PUSH BX
	
	call clrscr

	pop bx

	MOV AH, 09H
	MOV DX, OFFSET BAYRAK1A
	INT 21H	

	MOV AH, 09H
	MOV DX, OFFSET BAYRAK1B
	INT 21H	

	MOV AH, 09H
	MOV DX, OFFSET yoket
	INT 21H	
	
	mov dx,bx
	
	call dela

	mov bx,dx

	push bx

	call clrscr

	pop bx

	MOV AH, 09H
	MOV DX, OFFSET BAYRAK2A
	INT 21H	

	MOV AH, 09H
	MOV DX, OFFSET BAYRAK2B
	INT 21H	

	MOV AH, 09H
	MOV DX, OFFSET yoket
	INT 21H	

	mov dx,bx

	call dela

	mov bx,dx
		
	push bx

	call clrscr

	pop bx

	MOV AH, 09H
	MOV DX, OFFSET BAYRAK3A
	INT 21H	

	MOV AH, 09H
	MOV DX, OFFSET BAYRAK3B
	INT 21H	

	MOV AH, 09H
	MOV DX, OFFSET yoket
	INT 21H	

	mov dx, bx
	
	call dela	

	mov bx,dx		

	pop cx
	loop bigloop	
	

	MOV AH,4CH
	INT 21H
MAIN ENDP
	


CLRSCR	PROC
	MOV AX, 0600H
	MOV BH, 07H
	MOV CX, 0000H
	MOV DX, 184FH
	INT 10H
	RET
CLRSCR	ENDP	
	
DELA  	PROC

	mov cx,1fffH
lol2:	push cx
	mov cx,1fffH
lol:	loop lol
	pop cx
	loop lol2
	RET
DELA 	ENDP
	END MAIN
```

## program

```asm
	LIST P=16F84
	INCLUDE "P16F84.INC"

	__config _CP_OFF & _WDT_OFF & _PWRTE_ON & _RC_OSC 

	CLRF PORTB
	BSF STATUS,5 
	CLRF TRISB 
	MOVLW 0x11 
	MOVWF TRISA 
	BCF STATUS,5 
MAIN
	CLRF PORTB 
	CLRF TMR0 
	CLRWDT  
	BSF STATUS,5 
	MOVLW B'00000111' 
	MOVWF OPTION_REG 
	BCF STATUS,5  
	CLRF PORTB 
DONGU
	MOVF TMR0,W 
	MOVWF PORTB 
	BTFSS PORTA,0 
	CLRF TMR0 
	GOTO DONGU
	END
```

## buzzerDevre

Proteus devre kaynağı indirme paketinde yer alır. Kişisel ad taşıyan dosya ve yol kayıtları anonimleştirilmiştir.

*Not: Buzzer klasöründeki assembly taslağı TMR0 değerini PORTB’ye aktarıyor; başlıktaki ses üretimi amacının tamamlanmış uygulaması olarak değerlendirilmemelidir.*
