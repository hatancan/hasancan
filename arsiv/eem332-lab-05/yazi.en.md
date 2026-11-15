---
baslik: EEM332 Microprocessors: Laboratory 5: Strings and Loops
ozet: Replacing letters in a string, converting lowercase letters to uppercase, loops, and finding the largest value among grades.
---

This post brings together the related notes and exercises from the Başkent University **EEM332 Microprocessors** course archive (2002–2015). Replacing letters in a string, converting lowercase letters to uppercase, loops, and finding the largest value among grades. Work prepared by a friend and course documents have been included together; student names, numbers, and group information have been removed. PDF archive copies of the documents and, where available, source codes can be downloaded as a ZIP at the end of the post.

## eem332_lab05

EEM 332 - Microprocessors Experiment Number: 5 Experiment Title: Introduction to TASM/Assembly Programming/Loops

Description

The Turbo Assembler program to be used in the laboratory has been added to the web page. To install the program, extract the contents of the .zip file provided on the web page and paste the resulting folder named "t" into the C directory. You can examine the sample programs in this folder. More detailed information about using the program will be given during the experiment.

Preliminary Work

Answer the following questions. Bring an extra copy of your work with you. The preliminary work will be collected at the beginning of the laboratory session.

### 1) Write a program in assembler language that finds the lowest of the following temperature values:

+13, -10, +19, +14, -18, -9, +12, -19, +16

### 2) A student's grades are as follows: 69, 87, 96, 45, and 75. Write a program in assembler language that finds the

highest of these grades.

Experimental Work

### 1) Follow the Turbo Assembler introduction and carry out the task given by the laboratory instructor.

### 2) Modify the program given in item 2 of the preliminary work so that the grades are entered through the I/O interface and the result is displayed on the I/O interface, and state this in your report.

## eem332_lab05

EEM 332 – Microprocessors

Experiment Number: 5 Experiment Title: Assembly Programming/Loops

Experimental Work

### 1)    Write a program that converts the lowercase letters in a sentence entered from the keyboard to uppercase letters.

### Example

### 2)    Write a program that changes the desired letters in a character string defined in advance within the program.

Example: The output of a program that converts the character 'G' to the character 'J' in the string defined in the program as Mr. Gones is given below.

## LAB 5 Preliminary Work

### 1) A program that converts a vowel in a word into another vowel.

### MODEL SMALL

```asm
.STACK 64
.DATA
DATA DB ‘[kişisel bilgi çıkarıldı]’
.CODE
```

```asm
MAIN PROC FAR
MOV AX,@DATA
MOV DS,AX
MOV ES,AX
CLD
MOV DI,OFFSET DATA                     //[kişisel bilgi çıkarıldı] DI ya atılır.
MOV CX,10                              //10 tane harf oldugu için.
MOV AL,'a'                             //Değişmesi istenilen harf.
REPNE SCASB                            //REPNE komutu iki stringi karşılaştırır.
JNE ATLA                               // Eşit değilse etikete atlar.
DEC SI
MOVBYTE PTR[DI],'a'                    ;a’ nin yerine o.
ATLA: MOV AX,09H
MOV DX,OFFSET DATA
```

```asm
INT 21H
```

### MAIN ENDP

```asm
END MAIN
```

### 2) A program that reverses the entered name.

```asm
.MODEL SMALL
.STACK 64
.DATA
DATA1 DB '[kişisel bilgi çıkarıldı]’
DATA2 DB ?
.CODE
MAIN PROC FAR
MOV AX,@DATA
MOV DS,AX
MOV ES,AX
CLD
MOV DI,OFFSET DATA1                    //DI ya gönderilir.
MOV SI,OFFSET DATA2                    //Data2 SI ys.
MOV CX,10                              //toplam harf sayısını dönderir.
TOP:
```

```asm
MOV BL,[SI]
LOOP TOP
MOV BYTE PTR[DI],BL
MOV CX,10
NEXT:
DEC SI
MOV BL,[SI]
INC DI
MOV BYTE PTR[DI],BL
LOOP NEXT
JMP RESULT
```

### RESULT

```asm
MOV AX,09H
MOV DX,OFFSET DATA2
INT 21H
```

### MAIN ENDP

```asm
END MAIN
```

## 332_lab05_önçalışma

### 1)

```asm
.MODEL SMALL
.STACK 64
.DATA
AD       DB   '[kişisel bilgi çıkarıldı]'
```

```asm
.CODE
MAIN           PROC FAR     ;this is the program entry point
MOV AX,@DATA ;load the data segment address
MOV DS,AX             ;assign value to DS
```

```asm
MOV SI,OFFSET AD
```

```asm
MOV CL,9
```

```asm
MOV BL,'e'
```

```asm
DON: MOV BH,[SI]
```

```asm
CMP BL,BH
JZ DEGIS
DON2:
INC SI
LOOP DON
```

```asm
JMP SON
```

```asm
DEGIS: MOV DL,'a'
MOV [SI],DL
JMP DON2
```

### SON

```asm
MOV          AH,09
MOV          DX,OFFSET AD
INT          21H
```

```asm
MOV AH,4CH                ;set up to
INT 21H           ;return to DOS
```

### MAIN           ENDP

```asm
END MAIN          ;this is the program exit point
```

### 2)

```asm
.MODEL SMALL
.STACK 64
.DATA
AD        DB   '[kişisel bilgi çıkarıldı]'
```

```asm
.CODE
MAIN        PROC FAR     ;this is the program entry point
MOV AX,@DATA ;load the data segment address
MOV DS,AX             ;assign value to DS
```

```asm
MOV SI,OFFSET AD
MOV DI,OFFSET AD
```

```asm
MOV CL,9
```

```asm
SUB AX,AX
```

```asm
DON: MOV AL,[SI]
PUSH AX
INC SI
LOOP DON
```

```asm
MOV CL,DL
SUB SI,CX
```

```asm
DON2:POP [SI]
INC SI
LOOP DON2
```

```asm
MOV [SI],BL
```

```asm
MOV AH,09H
MOV DX,OFFSET AD
INT 21H
```

```asm
MOV AH,4CH                ;set up to
INT 21H           ;return to DOS
```

### MAIN        ENDP

```asm
END MAIN          ;this is the program exit point
```

## calisma-703

1-) In this section, we wrote a program that finds a specified vowel in the entered name and replaces it with another vowel.

```asm
.MODEL SMALL
.STACK 64
.DATA
DATA DB '[kişisel bilgi çıkarıldı]'
.CODE
MAIN PROC FAR
MOV AX,@DATA
MOV DS,AX
MOV ES,AX
CLD
MOV DI,OFFSET DATA ( İsmi buraya attık)
MOV CX,10 ( Döngü 10 defa dönmektedir)
MOV AL,'a' ( Değismesini istediğimiz harf)
REPNE SCASB ( Stringi scan ettiğimizde aradığımız harfi bulancaya kadar tekrar et )
JNE OVER
DEC SI
MOVBYTE PTR[DI],'e' ( ‘a’ nın yerine geçen harfimiz)
OVER:      MOV AX,09H
MOV DX,OFFSET DATA
```

```asm
INT 21H
```

### MAIN ENDP

```asm
END MAIN
```

Because the program I wrote did not work, I used another program in the laboratory. The program I used works completely. Since we had to write this code in a short time, I would like to state that I worked together with Fırat Özaydın.

```asm
.MODEL SMALL
.STACK 100h
.DATA
DATA DB "kelime girin: $"
CHANGE DB 30,?, 29 DUP ('$')
.CODE
MAIN PROC FAR
MOV AX,@DATA
MOV DS,AX
MOV ES,AX
MOV AH, 09H
MOV DX, OFFSET DATA
INT 21H
MOV AH, 0AH
MOV DX, OFFSET CHANGE
INT 21H
mov dl, 10d ; dl = LF
mov ah, 2h ; display subprogram
int 21h ; display LF
```

```asm
CLD
MOV DI,OFFSET CHANGE
MOV CX,0ffH
MOV AL,'e'
```

### NEXT 

```asm
REPNE SCASB
JNE OVER
DEC DI
MOV BYTE PTR[DI],'a'
INC CX
LOOP NEXT
OVER:
MOV AH,09H
MOV DX,OFFSET CHANGE+2
INT 21H
MOV AH,4CH
INT 21H
```

### MAIN ENDP

```asm
END MAIN
```

2-) In this section, we wrote a program that prints the entered name from right to left instead of left to right.

```asm
.MODEL SMALL
.STACK 64
.DATA
DATA1 DB '[kişisel bilgi çıkarıldı]'
DATA2 DB ? (ismi tersten yazdırıp buraya atacağımız için buna ihtiyacımız var)
.CODE
MAIN PROC FAR
MOV AX,@DATA
MOV DS,AX
MOV ES,AX
CLD
MOV DI,OFFSET DATA1 (ismi DI ya attık )
MOV SI,OFFSET DATA2 (ismi SI ya attık)
MOV CX,10 (döngü 10 defa dönecek )
END:       MOV BL,[SI]
LOOP END (end döngüsünde 10 defa döner )
MOV BYTE PTR[DI],BL
MOV CX,10
NEXT:      DEC SI ( SI yı azalt)
MOV BL,[SI]
INC DI ( DI yı arttır)
MOV BYTE PTR[DI],BL
LOOP NEXT (next döngüsünde 10 defa döner)
JMP RESULT
```

```asm
RESULT:       MOV AX,09H
MOV DX,OFFSET DATA2 (İsmin son halini DX e attık)
INT 21H
```

### MAIN ENDP

```asm
END MAIN
```

Because the program I wrote did not work, I used another program in the laboratory. The program I used works. Since we had to write this code in a short time, I would like to state that I worked together with Fırat Özaydın.

```asm
.model small
.stack 100h
.DATA
DATA DB " kelimeyi girin: $"
DATA DB 50,?, 49 DUP ('$')
ters DB       50 DUP(?), 49 DUP ('$')
.code
main proc far
MOV ax, @Data
MOV ds, ax
MOV AH, 09H
MOV DX, OFFSET DATA
INT 21H
MOV AH, 0AH
MOV DX, OFFSET DATA
INT 21H
MOV dl, 10d
MOV ah, 2h
İNT 21h
MOV cx, 11
MOV dx, OFFSET DATA
PUSH cx
MOV bx, OFFSET DATA
MOV si, OFFSET ters+4
ADD si, cx
DEC si
CHANGE
MOV al, [bx]
MOV [si], al
İNC bx
DEC si
LOOP CHANGE
POP cx
MOV ah, 50h
MOV bx, 1
MOV dx, OFFSET ters+2
İNT 21h
MOV ah, 4ch
İNT 21h
```

### MAİN ENDP

```asm
END MAİN
```

## eem332-5

Başkent University Department of Electrical and Electronics Engineering

EEM 332 – Microprocessors Laboratory

### REPORT

Experiment No: #5 Experiment Title: Introduction to TASM/Assembly Programming/Loops Experiment Date: 07/04/2006

```asm
.MODEL SMALL
.STACK
.DATA
```

```asm
DATA DB ? DUP (5)
RESULT DB ?
MESSAGE DB 'OGRENCI NOTLARINI GIRINIZ:';I/O arayüzünden girilecek
```

the numbers to be entered through the I/O interface are requested.

```asm
.CODE
```

```asm
MAIN PROC FAR
MOV AX, @DATA
MOV DS, AX
MOV CX, 5
MOV BX, OFFSET DATA
MOV AL,0
MOV AL, [BX]
INC BX
INT 21H
```

```asm
AGAIN:      MOV AH, 01; girilen sayıların büyüklük ve küçüklük durumları control
ediliyor
INT 16H
JZ AGAIN
MOV AH, 0
INT 16H
MOV [BP],AL
INC BP
CMP AL, [BX]
JL NEXT
MOV AL,[BX]
```

NEXT INC BX; (the instruction set required to exit the program)

```asm
LOOP AGAIN
MOV RESULT, AL
```

```asm
MOV AH, 4CH
INT 21H
```

### MAIN ENDP

```asm
END MAIN
```

## rapor5

```asm
.MODEL SMALL
.STACK
.DATA
```

```asm
DATA DB ? DUP (5)
RESULT DB ?
MESSAGE DB 'OGRENCI NOTLARINI GIRINIZ:';I/O arayüzünden girilecek
```

the numbers to be entered through the I/O interface are requested

```asm
.CODE
```

```asm
MAIN PROC FAR
MOV AX, @DATA
MOV DS, AX
MOV CX, 5
MOV BX, OFFSET DATA
MOV AL,0
MOV AL, [BX]
INC BX
INT 21H
```

```asm
AGAIN:     MOV AH, 01; girilen sayıların büyüklük-küçüklükleri kontrol ediliyor
INT 16H
JZ AGAIN
MOV AH, 0
INT 16H
MOV [BP],AL
INC BP
CMP AL, [BX]
JL NEXT
MOV AL,[BX]
```

NEXT INC BX; the instructions required to exit the program

```asm
LOOP AGAIN
MOV RESULT, AL
```

```asm
MOV AH, 4CH
INT 21H
```

### MAIN ENDP

```asm
END MAIN
```

## önçalışma5

Başkent University Department of Electrical and Electronics Engineering

EEM 332 – Microprocessors Laboratory

Preliminary Work / Report

Experiment No: # 5 Experiment Title: Introduction to TASM / Assembly Programming/Loops Experiment Date: 31/03/2006

### PRELIMINARY WORK

```asm
.Model small
.Stack 64k
.Data
SIGN_DATA DB +13,-10,+19,+14,-18,-9,+12,-19,+16
ORG 0010
LOWEST DB
```

Main:        Prog Far

```asm
MOV CX,8
MOV SI,OFFSET SING_DATA
BACK:        MOV AL,[SI]
INC SI
CMP AL,[SI]
JLE SEARCH
MOV AL,[SI]
SEARCH:      LOOP BACK
MOV LOWEST,AL
MOV AH,4CH
INT 21
ENDP
END MAIN
```

### 2)

```asm
.Model small
.Stack 64
.Data
Sign_data           DB 69,87,96,45,75
Org                 001
Hıgh                DB
```

Maın         Prog Far

```asm
MOV CX,5
MOV BX,OFFSET DATA
SUB AL,AL
AGAIN:       CMP AL,[BX]
JA NEXT
MOV AL,[BX]
NEXT:               INC BX
LOOP AGAIN
MOV DH,AL
Int 21 H
ENDP
END MAIN
```

## EEM 332 5 OC

1-) In this section, we wrote a program that finds a specified vowel in the entered name and replaces it with another vowel.

```asm
.MODEL SMALL
.STACK 64
.DATA
DATA DB '[kişisel bilgi çıkarıldı]'
.CODE
MAIN PROC FAR
MOV AX,@DATA
MOV DS,AX
MOV ES,AX
CLD
MOV DI,OFFSET DATA ( İsmi buraya attık)
MOV CX,10 ( Döngü 10 defa dönmektedir)
MOV AL,'a' ( Değismesini istediğimiz harf)
REPNE SCASB ( Stringi scan ettiğimizde aradığımız harfi bulancaya kadar tekrar et )
JNE OVER
DEC SI
MOVBYTE PTR[DI],'e' ( ‘a’ nın yerine geçen harfimiz)
OVER:      MOV AX,09H
MOV DX,OFFSET DATA
```

```asm
INT 21H
```

### MAIN ENDP

```asm
END MAIN
```

2-) In this section, we wrote a program that prints the entered name from right to left instead of left to right.

```asm
.MODEL SMALL
.STACK 64
.DATA
DATA1 DB '[kişisel bilgi çıkarıldı]'
DATA2 DB ? (ismi tersten yazdırıp buraya atacağımız için buna ihtiyacımız var)
.CODE
MAIN PROC FAR
MOV AX,@DATA
MOV DS,AX
MOV ES,AX
CLD
MOV DI,OFFSET DATA1 (ismi DI ya attık )
MOV SI,OFFSET DATA2 (ismi SI ya attık)
MOV CX,10 (döngü 10 defa dönecek )
END:       MOV BL,[SI]
LOOP END (end döngüsünde 10 defa döner )
MOV BYTE PTR[DI],BL
MOV CX,10
```

```asm
NEXT:       DEC SI ( SI yı azalt)
MOV BL,[SI]
INC DI ( DI yı arttır)
MOV BYTE PTR[DI],BL
LOOP NEXT (next döngüsünde 10 defa döner)
JMP RESULT
```

```asm
RESULT:     MOV AX,09H
MOV DX,OFFSET DATA2 (İsmin son halini DX e attık)
INT 21H
```

### MAIN ENDP

```asm
END MAIN
```

## deney

a)

```asm
.MODEL SMALL
.STACK 100h
.DATA
kelime DB "Bir kelime giriniz: $"
degistir DB 30,?, 29 DUP ('$')
.CODE
```

```asm
MAIN      PROC FAR
MOV AX,@DATA ; @ ile başlangıç adresi otomatik atanıyor.
MOV DS,AX
MOV ES,AX ; segment atamaları yapıldı.
```

```asm
MOV AH, 09H
MOV DX, OFFSET kelime            ; veri okunuyor.
INT 21H
```

```asm
MOV AH, 0AH
MOV DX, OFFSET degistir             ; veri ekrana yazılıyor.
INT 21H
```

```asm
MOV DL, 10D       ; display için yazılmış sabit kod
MOV AH, 2H
INT 21H
```

```asm
CLD   ; DF (direction flag (program artarak veya azalarak gidiyor)) içeriği 0'lanıyor.
MOV DI,OFFSET degistir ; degistir'i DI’ya attık.
MOV CX,0FFH
MOV AL,'e'   ; aranacak harf: 'e'
```

DONGU :   REPNE SCASB ; 'e' harfi bulunana kadar tarama yapılacak.

```asm
JNE OVER    ; Eşit değilse OVER' a gidiliyor.
DEC DI   ; DI'nın değeri 1 azaltılıyor.
MOV BYTE PTR[DI],'a' ; ‘e’ yerine ‘a’ yazılacak
INC CX    ; CX 1 arttırılıyor.
LOOP DONGU ;DONGU' ye geri dönülüyor.
```

```asm
OVER:     MOV AH,09H  ; yukarıda belirtildiği gibi 09H' dan devam ediyor.
MOV DX,OFFSET degistir+2
INT 21H
```

```asm
MOV AH,4CH
INT 21H
```

### MAIN ENDP

```asm
END MAIN
```

b)

```asm
.MODEL SMALL
.STACK 100H
.DATA
giris DB "Ters cevrilecek kelimeyi giriniz: $"
kelime DB 30,?, 29 DUP ('$')
ters DB 30 DUP(?), 29 DUP ('$')       ; stringler için hafızada yer ayrıldı.
.CODE
```

```asm
MAIN     PROC FAR
MOV AX, @DATA
MOV DS, AX
```

```asm
MOV AH, 09H    ;Ekrana yazdırma işlemi gerçekleştiriliyor.
MOV DX, OFFSET giris
INT 21H
```

```asm
MOV AH, 0AH     ;Klavyeden kelime okunuyor.
MOV DX, OFFSET kelime
INT 21H
```

```asm
MOV DL,10D        ;Display işlemi gerçekleştiriliyor.
MOV AH,2H
INT 21H
```

```asm
MOV CX,11
MOV DX, OFFSET kelime ;Ters çevrilecek kelime okunup DX içine atanıyor.
PUSH CX
MOV BX, OFFSET kelime
MOV SI, OFFSET ters+4 ; data girilince data+2’ye kaydediliyor. O yüzden +4 kullanılıyor.
ADD SI,CX
```

### CEVIR

```asm
MOV AL, [BX]
MOV [SI], AL
INC BX                 ;Harfler ters çeviriliyor.
DEC SI
LOOP CEVIR
POP CX
MOV AH, 40H
MOV BX, 1              ;Kelime ekrana yazılıyor.
MOV DX, OFFSET ters+2 ; data girilince data+2 den başladığı için.
INT 21H
MOV AH, 4CH     ; program sonlandırılıyor.
INT 21H
```

### MAIN ENDP

```asm
END MAIN
```

## önçalışma 5

### 1) The program code that finds a specified vowel in the given name and replaces it with another vowel is as follows;

EXAMPLE:       [kişisel bilgi çıkarıldı] → [kişisel bilgi çıkarıldı] (e → a)

```asm
.MODEL SMALL
.STACK 64
.DATA
DATA DB '[kişisel bilgi çıkarıldı]'      ; değiştirilecek string : “[kişisel bilgi çıkarıldı]”
.CODE
```

```asm
MAIN           PROC FAR
MOV AX, @DATA ; @ ile başlangıç adresi otomatik veriliyor
MOV DS, AX
MOV ES, AX
CLD
MOV DI, OFFSET DATA ; İsim DI’ya gönderildi
MOV CX, 09       ; Döngünün tekrar sayısı
MOV AL, 'a'      ; Yeni basılacak harf
REPNE SCASB ; Harf bulunana kadar tarama yapılacak
JNE OVER     ; Eşit değilse OVER döngüsüne atlıyor
DEC SI      ; SI’ nın değeri azaltılıyor
MOVBYTE PTR[DI], 'e' ; “e” yerine “a” yazılacak
```

```asm
OVER:          MOV AX, 09H
MOV DX, OFFSET DATA
```

```asm
INT 21H
```

### MAIN ENDP

```asm
END MAIN
```

### 2) The program code that writes the name entered in assembler language from right to left instead of left to right

### is as follows

EXAMPLE: [kişisel bilgi çıkarıldı] → neves ila

```asm
.MODEL SMALL
.STACK 64
.DATA
DATA1 DB '[kişisel bilgi çıkarıldı]’
DATA2 DB ?      ; “neves ila” DATA2’ye yüklenecek
.CODE
```

```asm
MAIN          PROC FAR
MOV AX, @DATA
MOV DS, AX
MOV ES, AX
CLD
MOV DI, OFFSET DATA1 ; DI’ya başlangıç adresi verildi
MOV SI, OFFSET DATA2 ; SI’ya başlangıç adresi verildi
MOV CX, 09           ; Döngünün tekrar sayısı
```

```asm
END:          MOV BL, [SI] ; SI göstericisinin olduğu yerdeki harf BL’ye atıldı
LOOP END     ; 9 tur
MOV BYTE PTR[DI], BL ; DI’ nın gösterdiği yere BL yüklenir
MOV CX, 09
```

```asm
NEXT:         DEC SI   ; SI azaltılıyor
MOV BL, [SI]
INC DI ; DI arttırılıyor
MOV BYTE PTR[DI], BL
LOOP NEXT ; 9 tur
JMP RESULT ; Result döngüsüne atlar
```

```asm
RESULT:       MOV AX, 09H
MOV DX, OFFSET DATA2 ; Çevrilmiş isim DX’ e yüklendi
```

```asm
INT 21H
```

### MAIN ENDP

```asm
END MAIN
```

## Lab5s1

```asm
MODEL SMALL
.STACK 64
.DATA
DATA DB "ala"
.CODE

MAIN PROC FAR
MOV AX,@DATA
MOV DS,AX	
MOV ES,AX
CLD 
MOV DI,OFFSET DATA 			
MOV CX,10				
MOV AL,'a' 				
REPNE SCASB 				
JNE ATLA				
DEC SI
MOV BYTE PTR[DI],'a' 			
ATLA:	MOV AX,09H
MOV DX,OFFSET DATA

INT 21H
MAIN ENDP			
END MAIN
```

## lab5s2

```asm
.MODEL SMALL
.STACK 64
.DATA
DATA1 DB '[kişisel bilgi çıkarıldı]’
DATA2 DB ?				
.CODE
MAIN PROC FAR
MOV AX,@DATA
MOV DS,AX
MOV ES,AX
CLD
MOV DI,OFFSET DATA1 		
MOV SI,OFFSET DATA2 			
MOV CX,10				
TOP:		
MOV BL,[SI]
LOOP TOP 
MOV BYTE PTR[DI],BL
MOV CX,10
NEXT:		
DEC SI 
MOV BL,[SI]
INC DI 
MOV BYTE PTR[DI],BL
LOOP NEXT 
JMP RESULT

RESULT:	
MOV AX,09H
MOV DX,OFFSET DATA2 
INT 21H
MAIN ENDP			
END MAIN
```

## 22222 332 deney 5

```asm
.model small
.stack 100h
.data

;
;Ekrana yazdırılacaklar ve stringler için hafızada yer ayrılıyor
;

giris DB "Ters cevrilecek kelimeyi giriniz: $"
kelime DB 30,?, 29 DUP ('$')
ters DB	30 DUP(?), 29 DUP ('$')


	.code
main proc far
	mov	ax, @Data
	mov	ds, ax	
	

;
;Ekrana yazdırma mesajı görüntüleniyor
;
MOV AH, 09H
MOV DX, OFFSET giris
INT 21H	




;
;Ters çevrilecek kelime klavyeden okunuyor
;
MOV AH, 0AH
MOV DX, OFFSET kelime
INT 21H

;
;İmleç bir aşağıya alınıyor
;
mov dl, 10d 
mov ah, 2h 
int 21h 


	
	mov	cx, 11				
	mov	dx, OFFSET kelime		;Ters çevrilecek kelime okunup DX içine atanıyor



			
	push	cx	
	mov	bx, OFFSET kelime
	mov	si, OFFSET ters+4
	add	si, cx	
	dec	si			
	
cevir:
		mov	al, [bx]		; 
		mov	[si], al		; 
		inc	bx			;Harfler çevrilmiş şekilde tekrar yerleştiriliyor
		dec	si			; 
		loop	cevir			; 
		pop	cx			;
		mov	ah, 40h			;
		mov	bx, 1			;Ters çevrilmiş kelime ekrana yazdırılıyor 
		mov	dx, OFFSET ters+2	;
		int	21h			; 

;
;Program sonlandırılıyor
;

		mov	ah, 4ch			
		int	21h			
		main endp
			end main
```

## lab5m

```asm
;THE FORM OF AN ASSEMBLY LANGUAGE PROGRAM
;NOTE: USING SIMPLIFIED SEGMENT DEFINITION
		.MODEL SMALL
		.STACK 64
		.DATA
SIGN_DATA 	DB	69,87,96,45,75
ORG 001
HIGHEST	DB	?
		.CODE
MAIN		PROC	FAR
		MOV 	AX,@DATA
		MOV 	DS,AX
		MOV 	CX,5
		MOV 	SI,OFFSET SIGN_DATA
		MOV 	AL,[SI]
BACK:		INC 	SI
		CMP 	AL,[SI]
		JGE 	SEARCH
		MOV 	AL,[SI]
SEARCH:		LOOP 	BACK
		MOV 	HIGHEST,AL
		MOV 	AH,4CH
		INT 	21H
MAIN		ENDP
		END	MAIN
```

## lab5m1

```asm
;THE FORM OF AN ASSEMBLY LANGUAGE PROGRAM
;NOTE: USING SIMPLIFIED SEGMENT DEFINITION
		.MODEL SMALL
		.STACK 64
		.DATA
SIGN_DATA 	DB	69,87,96,45,75
ORG 001
HIGHEST	DB	?
		.CODE
MAIN		PROC	FAR
		MOV 	AX,@DATA
		MOV 	DS,AX
		MOV 	CX,5,
		MOV 	SI,OFFSET SIGN_DATA
		MOV 	AL,[SI]
BACK:		INC 	SI
		CMP 	AL,[SI]
		JGE 	SEARCH
		MOV 	AL,[SI]
SEARCH:		LOOP 	BACK
		MOV 	HIGHEST,AL
		MOV 	AH,4CH
		INT 	21H
MAIN		ENDP
		END	MAIN
```

## calisma-787

```asm
;==========================================
;===== 8BIT Input/Output TEST PROGRAM =====
;=====         FOR SKC - 86           =====
;==========================================

CNT3  		EQU  	3FD6H
APORT3		EQU  	3FD0H
BPORT3		EQU  	3FD2H
CPORT3		EQU	3FD4H
RAME			EQU	0FFFFH 
				 
CODE		SEGMENT
		ASSUME	CS:CODE, DS:CODE				 

		ORG	0				 
				 
START:	MOV	SP,RAME
		MOV	AL,90H
		MOV	DX,CNT3	
		OUT	DX,AL 

J1:		MOV	DX,APORT3
		IN	AL,DX
		NOT	AL
		MOV	DX,BPORT3
		OUT	DX,AL
		JMP	J1

CODE		ENDS
		END	START
```

## calisma-788

```asm
;==========================================
;===== 8BIT Input/Output TEST PROGRAM =====
;=====         FOR SKC - 86           =====
;==========================================

CNT3  		EQU  	3FD6H
APORT3		EQU  	3FD0H
BPORT3		EQU  	3FD2H
CPORT3		EQU	3FD4H
RAME			EQU	0FFFFH 
				 
CODE		SEGMENT
		ASSUME	CS:CODE, DS:CODE				 

		ORG	0				 
				 
START:	MOV	SP,RAME
		MOV	AL,90H
		MOV	DX,CNT3	
		OUT	DX,AL 

J1:		MOV	DX,APORT3
		IN	AL,DX
	
		MOV	DX,BPORT3
		OUT	DX,AL
		JMP	J1

CODE		ENDS
		END	START
```

## calisma-789

```asm
TITLE PROGRAM LAB 5: KEYBOARD HIT USING INT 16	

	.MODEL SMALL
	.STACK
	.DATA

	SAYILAR DB 5 dup (?)
	RESULT DB ?
	MESSAGE DB 'NOTLARI GIRINIZ?'
	.CODE

MAIN	PROC	FAR                                   
	MOV AX, @DATA                          
	MOV DS, AX                                      
	MOV CX, 5 
	MOV BP, 0
	MOV AH,09		       
	MOV DX, OFFSET MESSAGE
    	INT 21H
	MOV BX, OFFSET SAYILAR
	MOV AL,0                   
	MOV AL, [BX] 
	INC BX
	
AGAIN:	MOV AH, 01
	INT 16H
	JZ AGAIN
	MOV AH, 0
	INT 16H
	MOV [BP],AL
	INC BP
	MOV AH, 02
	INT 21H
	CMP AL, [BX]		
	JL NEXT			
	MOV AL,[BX]		

NEXT:	INC BX
	LOOP AGAIN                              
	MOV RESULT, AL		

	MOV AH, 4CH		
	INT 21H			

MAIN	ENDP			
	END MAIN
```

## lab5

```asm
TITLE PROGRAM LAB 5: KEYBOARD HIT USING INT 16	

	.MODEL SMALL
	.STACK
	.DATA

	SAYILAR DB ? DUP (5)
	RESULT DB ?
	MESSAGE DB 'NOTLARI GIRINIZ?'
	.CODE

MAIN	PROC	FAR                                   
	MOV AX, @DATA                          
	MOV DS, AX                                      
	MOV CX, 5 		       
	MOV BX, OFFSET SAYILAR      
	MOV AL,0                   
	MOV AL, [BX] 
	INC BX
	INT 21H

AGAIN:	MOV AH, 01
	INT 16H
	JZ AGAIN
	MOV AH, 0
	INT 16H
	MOV [BP],AL
	INC BP
	CMP AL, [BX]		
	JL NEXT			
	MOV AL,[BX]		

NEXT	INC BX
	LOOP AGAIN                              
	MOV RESULT, AL		

	MOV AH, 4CH		
	INT 21H			

MAIN	ENDP			
	END MAIN
```

## 1111,1 332 deney 5

```asm
	.MODEL SMALL
	.STACK 100h
	.DATA 
kelime DB "Bir kelime giriniz: $"

degistir DB 30,?, 29 DUP ('$')
	.CODE
MAIN PROC FAR

	MOV AX,@DATA
	MOV DS,AX
	MOV ES,AX

MOV AH, 09H
MOV DX, OFFSET kelime
INT 21H	

MOV AH, 0AH
MOV DX, OFFSET degistir
INT 21H

mov dl, 10d ; dl = LF 
mov ah, 2h ; display subprogram
int 21h ; display LF

	CLD
	MOV DI,OFFSET degistir
	MOV CX,0ffH
	MOV AL,'e'
DONGU :	REPNE SCASB
	JNE OVER
	DEC  DI
	MOV BYTE PTR[DI],'a'
	INC CX
	LOOP DONGU

OVER:	MOV AH,09H
	MOV DX,OFFSET degistir+2
	INT 21H

	MOV AH,4CH
	INT 21H

MAIN ENDP
	END MAIN
```

## calisma-882

```asm
.MODEL small
.STACK 64
.DATA
.CODE
MAIN PROC FAR
MOV AX,@DATA
MOV DS,AX
MOV ES,AX
DİZİ1:MOV AH,01
İNT 21H
CMP AL,13
JZ YAZ
INC SI
CMP AL,61H
SUB AL,20H
SUB AL,0H
MOV [SNC+SI],AL
JMP DİZİ1
MOV AH,09H
MOV AH,4CH
INT 21H
MAIN ENDP
ENDP MAIN
```

## calisma-883

```asm
.MODEL small
.STACK 64
.DATA
DATA1 DB "Mr.Gones"
DATA2 DB ?
.CODE
MAIN PROC FAR
MOV	AX,@DATA
MOV DS,AX
MOV BX,AX
MOV DI,OFFSET DATA1
MOV CX,9
MOV AL,'G'
JE OVER
DEC DI
MOV DI,'J'
MOV AH,9
MOV DX,OFFSET DATA1
INT 21H
MAIN ENDP
END MAIN
```

## calisma-1226

```asm
.MODEL SMALL
.STACK 100h
.DATA
isim DB "Isim: $"
cevir DB 30,?, 29 DUP ('$')
.CODE

MAIN 	PROC FAR
	MOV AX, @DATA   ; @ ile başlangıç adresi otomatik veriliyor
	MOV DS, AX	
	MOV ES, AX

	MOV AH,09h
	MOV DX, OFFSET isim     ; İsim okunup DX’e gönderildi
	INT 21h

	MOV AH,Ah         ; Döngünün tekrar sayısı
	MOV DX, OFFSET cevir     ; Değiştirilip ekrana yazılıyor
	INT 21h

	MOV DL,10D      ;SABİT KOD
	MOV AH,2h
	INT 21h

	CLD   ;	Destination flag sıfırlaması
	MOV DI,OFFSET cevir
	MOV CX,0FFh
	MOV AL,'e';     ;Değiştirilecek harf

DONGU:	REPNE SCASB   ; Harf bulunana kadar tarama yapılacak
	JNE OVER      ; Eşit değilse OVER döngüsüne atlıyor
	DEC DI	; DI’ nın değeri azaltılıyor
	MOV BYTE PTR[DI],'a'     ; “e” yerine “a” yazılacak
	INC CX         ; CX++
	LOOP DONGU

OVER:	MOV AX, 09H
	MOV DX, OFFSET cevir
	INT 21h

	MOV AH,4CH	;SABİT KOD
	INT 21H
	MAIN ENDP			
	END MAIN
```

## calisma-1227

```asm
.MODEL SMALL
.STACK 100h
.DATA
isim DB "Isim: $"
cevir DB 30,?, 29 DUP ('$')
.CODE

MAIN 	PROC FAR
	MOV AX, @DATA   ; @ ile başlangıç adresi otomatik veriliyor
	MOV DS, AX	

	MOV AH,09h
	MOV DX, OFFSET isim     ; İsim okunup DX’e gönderildi
	INT 21h

	MOV DL,10D      ;SABİT KOD
	MOV AH,2h
	INT 21h

	MOV CX,11
	MOV DX,OFFSET isim
	PUSH CX
	MOV BX,OFFSET isim
	MOV SI,OFFSET cevir+4
	ADD SI,CX

DONDUR:	MOV AL,[BX]
	MOV [SI],AL
	INC BX
	DEC SI
	LOOP DONDUR

	POP CX
	MOV AH,40H
	MOV BX,1
	MOV DX,OFFSET cevir+2
	INT 21h

	MOV AH,4CH	;SABİT KOD
	INT 21H
	MAIN ENDP			
	END MAIN
```

## TOPLA1

```asm
;THE FORM OF AN ASSEMBLY LANGUAGE PROGRAM
;NOTE: USING SIMPLIFIED SEGMENT DEFINITION
		.MODEL SMALL
		.STACK 64
		.DATA
DATA1		DB	52H
DATA2		DB	29H
SUM		DB	?
		.CODE
MAIN		PROC	FAR		;this is the program entry point
		MOV	AX,@DATA	;load the data segment address
		MOV	DS,AX		;assign value to DS
		MOV	AL,DATA1	;get the first operand
		MOV	BL,DATA2	;get the second operand
		ADD	AL,BL		;add the operands
		MOV	SUM,AL	;store the result in location SUM
		MOV	AH,4CH	;set up to
		INT	21H		;return to DOS
MAIN		ENDP			
		END	MAIN		;this is the program exit point
```

## README

The file saved with the .asm extension is named topla1.asm; this file has been saved inside the folder containing the Td, Tlink, and Tasm files. To assemble this file as .asm, go to the t folder under C.

Perform the operations specified below.

The menu seen on the screen when TD is run is as follows. The program is run step by step using F7.

## readme

The file saved with the .asm extension is named topla1.asm; this file has been saved inside the file that contains the Td, Tlink, and Tasm files. To assemble this file as asm, go to the file under C and perform the operations below.

```
C:\t>tasm topla1.asm
```

Turbo Assembler Version 2.0 Copyright (c) 1988, 1990 Borland Internationa

Assembling file: topla1.asm Error messages: None Warning messages: None Passes:       1 Remaining memory: 424k

The obj file is run with Tlink

```
C:\t >tlink topla1.obj
```

Turbo Link Version 3.0 Copyright (c) 1987, 1990 Borland International Unable to open file topla.obj

The EXE file is run

```
C:\t>td topla1.exe
```

The menu seen on the screen in TD. The program is run step by step using F7.

```
59C9:0000 B8CB59        mov ax,59CB       - ax 12A2 ¦c=
59C9:0003 8ED8       mov ds,ax       _ bx 4647 ¦z=
59C9:0005 A00000       mov al,[0000] _ cx 12A2 ¦s=
59C9:0008 8A1E0100       mov bl,[0001] _ dx 0000 ¦o=
59C9:000C 02C3       add al,bl      _ si F68E ¦p=
59C9:000E A20200       mov [0002],al _ di 9BC1 ¦a=
59C9:0011 B44C       mov ah,4C        _ bp 0100 ¦i=
59C9:0013 CD21        int 21       _ sp 0106 ¦d=
```

___________________________________________¦             ¦

```
59B9:0000 CD 20 00 A0 00 9A F0 FE - á Ü_ ¦         ¦
59B9:0008 1D F0 E6 01 BF 26 B0 01 µ +&_ +---------------
59B9:0010 BF 26 83 02 23 21 A2 12 +&â#!ó ¦59CC:0042 FFFF
59B9:0018 FF FF FF FF FF FF FF FF         ¦59CC:0040 FF00
```
