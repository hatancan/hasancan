---
baslik: EEM332 Mikroişlemciler: Laboratuvar 6: Assembly Döngüleri ve Cümle İşleme
ozet: Cümle ve kelime işleme, sayma, dönüştürme ve assembly döngüleri; ön çalışmalar ve deney çözümleri.
---

Bu yazı, Başkent Üniversitesi **EEM332 Mikroişlemciler** ders arşivindeki ilgili notları ve uygulamaları bir araya getiriyor (2006–2015). Cümle ve kelime işleme, sayma, dönüştürme ve assembly döngüleri; ön çalışmalar ve deney çözümleri. Bir arkadaşın hazırladığı çalışmalar ve ders belgeleri birlikte aktarılmış; öğrenci adları, numaraları ve grup bilgileri çıkarılmıştır. Belgelerin PDF arşiv kopyaları ve varsa kaynak kodları yazının sonunda ZIP olarak indirilebilir.

## eem332_lab06

EEM 332 - Mikroişlemciler Deney Numarası: 6 Deney Adı: Assembly Programlama/Döngüler

Ön Çalışma Laboratuvara gelmeden önce aşağıda verilen soruları yanıtlayınız.

### 1) Çevirici dilinde, klavyeden girilen bir cümlede (en fazla 100 karakter) bulunan kelimelerin

sayısını bulan ve bu sayıyı onluk (decimal) sistemde ekrana yazdıran programı yazınız.

Deneysel Çalışma

### 1) Ön çalışmada yazdığınız programı çalıştırınız ve sonuçları gösteriniz.

### 2) Ön çalışmada yazdığınız programı, aşağıdaki işlemi yapacak şekilde değiştiriniz ve

sonuçları gösteriniz.

Yazılacak programla, return (enter) tuşuna basıldığında klavyeden girilmiş olan cümlenin en sonundaki kelimenin en başa atılması sağlanmalıdır.

### Örnek

bu kelimeyi başa atınız            <enter> atınız bu kelimeyi başa            <enter> başa atınız bu kelimeyi            <enter> kelimeyi başa atınız bu            <enter> bu kelimeyi başa atınız

Rapor

### 1) Ön ve deneysel çalışmalarda yazdığınız programlardan da faydalanarak klavyeden girilen

bir cümledeki kelimeleri ard [kişisel bilgi çıkarıldı] 3 kez gelişigüzel (random) sıralayan programı yazınız.

### Örnek

bu cümleyi random sıralayınız                     <enter> cümleyi bu sıralayınız random random bu sıralayınız cümleyi bu random cümleyi sıralayınız

## calisma-641

### 1)

```asm
.MODEL SMALL
.STACK 100h
.DATA
MAXCUMLE EQU 100
STRING DB MAXCUMLE DUP(?)
COUNT DB (?)
.CODE
START:
MOV AX,@DATA
MOV DS,AX
MOV ES,AX
MOV AH,3Fh
MOV BX,01h
MOV CX, MAXCUMLE
MOV DX,OFFSET STRING
INT 21H
AND AX,AX
JZ DONE
MOV CX,AX
MOV DI,OFFSET STRING
MOV AL,' '
MOV AH,CL
KONTROL:
CMP AL,[DI]
JZ SAY
JNZ NO
SAY:
INC BX
CMP [DI+1],AL
JZ ATLA
```

### BOSLUKGEC

```asm
INC DI
INC DX
CMP AL,[DI]
JZ ATLA
NO:
INC DI
INC DX
;CMP ah,Dl
;JZ ATLA
```

```asm
LOOP KARSILASTIR
```

```asm
MOV AX,BX
MOV DX,AX
OR DX 3030H
```

```asm
MOV AH,02H
INT 21h
DONE:
MOV AH,4CH
INT 21H
ENDP
END START
```

### 2) Gelişi güzel sayı üretmek için 3 farklı yöntem vardır. Bunlar Get Trick Count API si, Rdtsc

komutu ve nrandom komutudur.

### GetTickCount

Çağrıldığında işletim sisteminin başladığı andan itibaren geçen zamanı bize milisaniye olarak döndürür ve EAX yazmacına yazdırır. Her çağrılışda farklı bir sayı gelecektir. EAX yazmacına atılan zaman değerinin tamamını ya da 8 bitlik veya 16 bitlik kısımlarını kullanarak rassal bir sayı elde edebilirz

### RDTSC

Çağrıldığında bize işlemcinin en son resetlendiği andan itibaren her bir sayıp devrini verir. RDTSC için ayrılan yazmaçlar EAX ve EDX yazmaçlarıdır. RDTSC komutu düşük öncelikli 32 biti EAX yazmacına yüksek öncelikli 32 biti EDX yazmacına yazar.

### Masm32.lib->nrandom fonksiyonu

Masm32 ile birlikte gelen rastgele sayı üreten fonksiyondur.

### RDTSC

invoke nseed,eax invoke nrandom,sayı şeklinde çağrılır burada sayı bir değişken ya da doğrudan bir sayı olabilir. Bu da o sayıya kadar rastgele sayı üretmemizi sağlar.nseed ise nrandom komutunun program açıldığında hep aynı sayıyı değil yine rassal bir sayı üreterek açılmasını sağlar. Kullanılmazsa nrandom yine rastgele sayı üretir ancak program her açıldığında aynı sayı ile açılır.

## lab06_önçalışma

### 1)

```asm
.MODEL SMALL
.STACK 64
.DATA
SONUC    DB    100 DUP(?)
```

```asm
.CODE
MAIN          PROC    FAR                  ;this is the program entry point
MOV     AX,@DATA                  ;load the data segment address
MOV     DS,AX                    ;assign value to DS
```

```asm
SUB DX,DX        ;DX'i s?f?rla
SUB BX,BX
INC DX           ;En az bir kelime
```

```asm
DEVAM:     MOV AH,1
INT 21H
CMP AL,0DH          ;Enter'a basildi mi?
JZ BITIS            ;Basildiysa döngüden çık
MOV [SI],AL
INC SI           ;stringi arttir
CMP AL,20H         ;Bosluk mu?
JZ BOSLUK         ;Bosluk ise DX'i arttır
JMP DEVAM          ;Devam
```

```asm
BOSLUK: INC DX             ;Bosluk, DX'i arttır
JMP DEVAM
```

```asm
MOV DI,DX
```

```asm
;Lab Föyünde verilen Hex 'i Decimal'e çeviren kod
```

```asm
BITIS: MOV DI,DX
MOV AX,DI     ;HEXVAL ADRESINDEN DEGERI AX?E AL
SUB DX,DX
MOV BL,000AH      ;BX YAZMACINA 0A DEGERINI ATA
DIV BL        ;AX YAZMACINI BX YAZMACINA B?L
MOV DH,AL      ;CIKAN DEGER DECIMAL SAYININ 10LAR
MUL BL          ;DEGERI BX?LE CARP
MOV CX,DI
SUB CX,AX    ;CX VE AX YAZMACLARININ FARKINI AL
MOV DL,CL     ;CIKAN DEGER DECIMAL SAYININ 1LER
```

```asm
OR DX,3030H      ;ASCII'ye çevir
XCHG DL,DH         ;Basamakları düzenle
MOV DI,OFFSET SONUC
MOV AX,0D0AH          ;Alt satıra yazdırmak icin
MOV [DI],AX           ;Alt Satıra yazdırmak icin
ADD DI,2
MOV [DI],DL
INC DI
MOV [DI],DH
INC DI
MOV DX,OFFSET SONUC
MOV AH,'$'      ;String sonu
MOV [DI],AH
```

```asm
MOV         AH,09H      ;Yazdır
INT        21H
```

```asm
MOV    AH,4CH           ;set up to
INT   21H             ;return to DOS
```

### MAIN          ENDP

```asm
END MAIN              ;this is the program exit point
```

### 2)

```asm
.model small
.stack 100
.data
rnum dw ?
.code
main proc far
```

```asm
in al, 40h           ; read micro-clock for initial seed
mov ah, al
in al, 40h
xchg al, ah
or ax, 1
mov rnum, ax               ;rnum değeri ax değerini alır
```

```asm
mov bx,0100                ;0-100 arası için kıstılama yapacak register
div bx                    ;bölme işlemi kalan dx registerinde
add dx,1                 ;mod işlemi gereği 1 toplanması
```

```asm
mov ax,dx
MOV aH, 0H
;decimale çevirmek için gerekli işlemler
MOV BX, 10
DIV BL
```

```asm
OR aX, 3030H
```

```asm
mov dl,al
mov bl,ah
mov ah,02H
int 21H
```

```asm
mov dl,bl      ;yazdırma işlemleri
mov ah,02H
```

```asm
int 21H
mov ah,4cH       ;DOS a dönüş
int 21H
```

main endp

```asm
end main
```

## rapor 6

```asm
.MODEL LARGE
.STACK 64
.DATA
CUMLE            DB    100 DUP(?)
KELIME_YAZDIR    DB    100 DUP(?)
RANDOM_KEL       DB    100 DUP(?)
.CODE
MAIN       PROC FAR
MOV AX,@DATA
MOV DS,AX
MOV DI,OFFSET CUMLE
MOV CX,03h
PUSH CX
SUB BL,BL
VERİ_AL:   MOV AH,01H
INT   21H
MOV [DI],AL
INC DI
CMP AL,13
JNE   VERİ_AL
MOV DI,OFFSET CUMLE
MOV SI,OFFSET KELIME_YAZDIR
MOV [SI],DI
INC DI
INC SI
KEL_BAS_AL:      MOV AL,[DI]
INC DI
CMP AL,13
JE    ENTER_EKLE
CMP AL,' '
JNE   KEL_BAS_AL
INC BL
MOV BH,BL
MOV DX,DI
MOV [SI],DX
INC SI
JMP KEL_BAS_AL
ENTER_EKLE:      INC BH
MOV AL,13
MOV [SI],AL
MOV DI,OFFSET RANDOM_KEL
RAND_KEL: MOV AH,2Ch
INT   21h
MOV SI,OFFSET KELIME_YAZDIR
POP CX
SHR DL,CL
PUSH CX
AND DL,BL
SUB DH,DH
ADD SI,DX
MOV AL,[SI]
MOV [DI],AL
INC DI
SON_BUL:   SUB AX,AX
INC SI
```

```asm
MOV AL,[SI]
DEC SI
MOV [SI],AL
INC SI
CMP AL,13
JNE  SON_BUL
DEC BL
DEC BH
CMP BH,0h
JNE  RAND_KEL
MOV DH,13
MOV [DI],DH
MOV DI,OFFSET RANDOM_KEL
YAZ_DIGER_KEL: MOV SI,OFFSET CUMLE
SUB AX,AX
MOV AL,[DI]
SUB AH,AH
ADD SI,AX
MOV DH,13
CMP [DI],DH
JE   TEKRAR_YAP
INC DI
YAZ:      SUB DX,DX
MOV DL,[SI]
INC SI
CMP DL,13
JE   BOSLUK_KOY
MOV AH,02h
INT  21h
CMP AL,' '
JE   YAZ_DIGER_KEL
JMP YAZ
BASA_DON: JMP KEL_BAS_AL
BOSLUK_KOY:    MOV DL,' '
MOV AH,02h
INT  21h
JMP YAZ_DIGER_KEL
TEKRAR_YAP:    POP CX
DEC CX
PUSH CX
MOV DI,OFFSET CUMLE
MOV SI,OFFSET KELIME_YAZDIR
MOV [SI],DI
INC DI
INC SI
SUB BX,BX
CMP CX,0
JNE  BASA_DON
MOV AH,4CH
INT  21H
```

### MAIN      ENDP

```asm
END MAIN
```

## ön calışma 6

Başkent Üniversitesi Elektrik - Elektonik Mühendisliği Bölümü

EEM 332 – Mikroişlemciler Laboratuvarı

Ön Çalışma

Deney No: #6 Deney Adı: Assembly Programlama/ Döngüler Deney Tarihi:21/04/06

```asm
.MODEL SMALL
.STACK 64
.DATA
ORG 0100h
DAT           DB 100 DUP(?)
Sayi DB   ?
```

```asm
.CODE
MAIN          PROC            FAR
MOV             AX,#DAT
MOV             DS,AX
SUB             AX,AX
MOV             CX,100
MOV             SI,OFFSET DAT
sub             bx,bx
```

### verial

```asm
mov             ax,0
int             16h
mov             [si],si
inc             si
mov             dl,al
mov             ah,02
cmp             sl,32d: (bosluk karşılaştırılması burada yapılır)
jnz             devam : 32d boşlugunun seçili kodu eger boşluk
```

bırakılmışsa bs 1 arttırılabilir.

```asm
İnc             bx
```

```asm
devam:        cmp             sl,46 : nokta karşılaştırılması burada yapılır.
Jx              yazdır
İnt             21h : dl dekini yazdırır.
loop            verial
```

```asm
inc             bl : bl son bir kez arttırılır,çünkü boşluk sayısı kelime
```

sayısından 1 azdır.

```asm
sub             ax,ax
mov             al,bl
mov             cl,10
div             al, : ax 10’a bölününce al’ye bölüm, ah’a kalan atılır.
mov             bx,ax
```

```asm
mov             dl,46
int             21h
mov             ah,02
int             21h
mov             dl,09
int             21h
mov             dl,ah
or              dl,46
int             21h
mov             dl,bh
or              dl,46
int             21h
mov             ah,4ch
int             21h
```

```asm
ENDP
END MAİN
```

## rapor03

Başkent Üniversitesi Elektrik - Elektonik Mühendisliği Bölümü

EEM 332 – Mikroişlemciler Laboratuvarı

### RAPOR

Deney No: #6 Deney Adı: Assembly Programlama/ Döngüler Deney Tarihi: 21/04/2006

### Deneysel çalışma 

### 1)

C. Mov [DI],AL Register indirect addressing 10000+0100=10100

### D.MOV AL,[BP+DI]

Based indexed addressing mode 10000+1000+0100= 11100

### E. MOV CX,[DI]

İndexed addressing mode 10100

### F. MOV DX,[BP]

Based addressing mode 11000

### G. MOV [100],DL

Direct addressing mode 10100

### H. MOV [SI+100],AX

İndexed addressing mode 20000+0200+100= 20300

### İ. MOV DL,[BX+100]

Based addressing mode 10000+0300+100= 10400

### J. MOV [SI],DX

Register indirect addressing 10000+0200= 10200

### K. MOV CL,[BX]

Based addressing addressing 10300

### L. MOV CH,[BX+SI]

Based indexed addressing mode 10000+0300+0200= 10500

### M. MOV AX,[BP+200]

Based addressing mode 10000+1000+200= 11200

### N.MOV AL,[BP+SI-200]

Based indexed addressing mode 10000+1000+0200-200= 11000

### O. MOV AL,[SI-0100]

İndexed indirect mode 10000+0200-0100= 10100

### 2)

Programın komutları :( Assembly)

### (Hafıza adresleri)        Program komutları

```
13A5:0100     mov ax,1234
13A5:0103     mov bx,ax
13A5:0105     mov cl,bl
13A5:0107     DS: mov [0200],ax
13A5:010B     mov ch,[0201]
13A5:010F     ES: mov [0220],ax
13A5:0113     mov SI,0220
13A5:0116     mov ah,[SI]
13A5:0118     mov bp,0220
13A5:011B     DS: mov ax,5678
13A5:011F     mov bx,0200
13A5:0122     DS: mov [bx+2],ax
13A5:0126     mov ax,90AB
13A5:0129     mov DI,0220
13A5:012C     mov [DI]-1c,ax
13A5:012F     mov bx,100
13A5:0132     mov SI,104
13A5:0135     mov cl,[bx][SI]
13A5:0137     mov SI,0100
13A5:013A     mov ch,[bx][SI]+5
```

Komut satırları taker taker trace yapılırsa çıkan sonuçlar şu şekildedir.

```
-t
```

```
AX=1234 BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=13A5 ES=13A5 SS=13A5 CS=13A5 IP=0103 NV UP EI PL NZ NA PO NC
13A5:0103 89C3   MOV BX,AX
-t
```

```
AX=1234 BX=1234 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=13A5 ES=13A5 SS=13A5 CS=13A5 IP=0105 NV UP EI PL NZ NA PO NC
13A5:0105 88D9   MOV CL,BL
-t
```

```
AX=1234 BX=1234 CX=0034 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=13A5 ES=13A5 SS=13A5 CS=13A5 IP=0107 NV UP EI PL NZ NA PO NC
13A5:0107 3E     DS:
13A5:0108 A30002   MOV [0200],AX            DS:0200=0000
-t
```

```
AX=1234 BX=1234 CX=0034 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=13A5 ES=13A5 SS=13A5 CS=13A5 IP=010B NV UP EI PL NZ NA PO NC
13A5:010B 8A2E0102 MOV CH,[0201]             DS:0201=12
```

-

```
-t
```

```
AX=1234 BX=1234 CX=1234 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=13A5 ES=13A5 SS=13A5 CS=13A5 IP=010F NV UP EI PL NZ NA PO NC
13A5:010F 26     ES:
13A5:0110 A32002   MOV [0220],AX            ES:0220=0000
-t
```

```
AX=1234 BX=1234 CX=1234 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=13A5 ES=13A5 SS=13A5 CS=13A5 IP=0113 NV UP EI PL NZ NA PO NC
13A5:0113 BE2002  MOV SI,0220
-t
```

```
AX=1234 BX=1234 CX=1234 DX=0000 SP=FFEE BP=0000 SI=0220 DI=0000
DS=13A5 ES=13A5 SS=13A5 CS=13A5 IP=0116 NV UP EI PL NZ NA PO NC
13A5:0116 8A24   MOV AH,[SI]              DS:0220=34
-t
```

```
AX=3434 BX=1234 CX=1234 DX=0000 SP=FFEE BP=0000 SI=0220 DI=0000
DS=13A5 ES=13A5 SS=13A5 CS=13A5 IP=0118 NV UP EI PL NZ NA PO NC
13A5:0118 BD2002  MOV BP,0220
```

-

```
-t
```

```
AX=3434 BX=1234 CX=1234 DX=0000 SP=FFEE BP=0220 SI=0220 DI=0000
DS=13A5 ES=13A5 SS=13A5 CS=13A5 IP=011B NV UP EI PL NZ NA PO NC
13A5:011B 3E     DS:
13A5:011C B87856   MOV AX,5678
```

```
-t
```

```
AX=5678 BX=1234 CX=1234 DX=0000 SP=FFEE BP=0220 SI=0220 DI=0000
DS=13A5 ES=13A5 SS=13A5 CS=13A5 IP=011F NV UP EI PL NZ NA PO NC
13A5:011F BB0002  MOV BX,0200
-t
```

```
AX=5678 BX=0200 CX=1234 DX=0000 SP=FFEE BP=0220 SI=0220 DI=0000
DS=13A5 ES=13A5 SS=13A5 CS=13A5 IP=0122 NV UP EI PL NZ NA PO NC
13A5:0122 3E     DS:
13A5:0123 894702  MOV [BX+02],AX             DS:0202=0000
-t
```

```
AX=5678 BX=0200 CX=1234 DX=0000 SP=FFEE BP=0220 SI=0220 DI=0000
DS=13A5 ES=13A5 SS=13A5 CS=13A5 IP=0126 NV UP EI PL NZ NA PO NC
13A5:0126 B8AB90  MOV AX,90AB
```

-

```
-t
```

```
AX=90AB BX=0200 CX=1234 DX=0000 SP=FFEE BP=0220 SI=0220 DI=0000
DS=13A5 ES=13A5 SS=13A5 CS=13A5 IP=0129 NV UP EI PL NZ NA PO NC
13A5:0129 BF2002  MOV DI,0220
-t
```

```
AX=90AB BX=0200 CX=1234 DX=0000 SP=FFEE BP=0220 SI=0220 DI=0220
DS=13A5 ES=13A5 SS=13A5 CS=13A5 IP=012C NV UP EI PL NZ NA PO NC
13A5:012C 8945E4  MOV [DI-1C],AX            DS:0204=0000
-t
```

```
AX=90AB BX=0200 CX=1234 DX=0000 SP=FFEE BP=0220 SI=0220 DI=0220
DS=13A5 ES=13A5 SS=13A5 CS=13A5 IP=012F NV UP EI PL NZ NA PO NC
13A5:012F BB0001  MOV BX,0100
-t
```

```
AX=90AB BX=0100 CX=1234 DX=0000 SP=FFEE BP=0220 SI=0220 DI=0220
DS=13A5 ES=13A5 SS=13A5 CS=13A5 IP=0132 NV UP EI PL NZ NA PO NC
13A5:0132 BE0401  MOV SI,0104
```

-

```
-t
```

```
AX=90AB BX=0100 CX=1234 DX=0000 SP=FFEE BP=0220 SI=0104 DI=0220
DS=13A5 ES=13A5 SS=13A5 CS=13A5 IP=0135 NV UP EI PL NZ NA PO NC
13A5:0135 8A08   MOV CL,[BX+SI]             DS:0204=AB
-t
```

```
AX=90AB BX=0100 CX=12AB DX=0000 SP=FFEE BP=0220 SI=0104 DI=0220
DS=13A5 ES=13A5 SS=13A5 CS=13A5 IP=0137 NV UP EI PL NZ NA PO NC
13A5:0137 BE0001  MOV SI,0100
-t
```

```
AX=90AB BX=0100 CX=12AB DX=0000 SP=FFEE BP=0220 SI=0100 DI=0220
DS=13A5 ES=13A5 SS=13A5 CS=13A5 IP=013A NV UP EI PL NZ NA PO NC
13A5:013A 8A6805  MOV CH,[BX+SI+05]            DS:0205=90
```

```
-t
```

```
AX=90AB BX=0100 CX=90AB DX=0000 SP=FFEE BP=0220 SI=0100 DI=0220
DS=13A5 ES=13A5 SS=13A5 CS=13A5 IP=013D NV UP EI PL NZ NA PO NC
13A5:013D 0000   ADD [BX+SI],AL            DS:0200=34
```

D komutunu kullanarak girilen değerlerin hafızadaki yerleşim hallerini görebiliriz.

```
-d
13A5:0100 B8 34 12 89 C3 88 D9 3E-A3 00 02 8A 2E 01 02 26 .4.....>.......&
13A5:0110 A3 20 02 BE 20 02 8A 24-BD 20 02 3E B8 78 56 BB . .. ..$. .>.xV.
13A5:0120 00 02 3E 89 47 02 B8 AB-90 BF 20 02 89 45 E4 BB ..>.G..... ..E..
13A5:0130 00 01 BE 04 01 8A 08 BE-00 01 8A 68 05 00 00 00 ...........h....
13A5:0140 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
13A5:0150 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
13A5:0160 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
13A5:0170 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
```

-

U komutunu kullanarak fiziksel adres ve atama değerleri bulunabilir ve incelenebilir.

```
-u 100
13A5:0100 B83412             MOV AX,1234
13A5:0103 89C3               MOV BX,AX
13A5:0105 88D9                MOV CL,BL
13A5:0107 3E                 DS:
13A5:0108 A30002             MOV [0200],AX
13A5:010B 8A2E0102           MOV CH,[0201]
13A5:010F 26                 ES:
13A5:0110 A32002              MOV [0220],AX
13A5:0113 BE2002             MOV SI,0220
13A5:0116 8A24               MOV AH,[SI]
13A5:0118 BD2002             MOV BP,0220
13A5:011B 3E                 DS:
13A5:011C B87856             MOV AX,5678
13A5:011F BB0002             MOV BX,0200
13A5:0122 3E                 DS:
13A5:0123 894702             MOV [BX+02],AX
13A5:0126 B8AB90              MOV AX,90AB
13A5:0129 BF2002             MOV DI,0220
13A5:012C 8945E4             MOV [DI-1C],AX
13A5:012F BB0001             MOV BX,0100
13A5:0132 BE0401             MOV SI,0104
13A5:0135 8A08               MOV CL,[BX+SI]
13A5:0137 BE0001              MOV SI,0100
13A5:013A 8A6805              MOV CH,[BX+SI+05]
13A5:013D 0000               ADD [BX+SI],AL
```

-

## L6S1

```asm
.MODEL SMALL
.STACK 100h
.DATA 
	MAXCUMLE EQU 100
	STRING DB MAXCUMLE DUP(?)
	COUNT DB  (?)
.CODE
START: 
	MOV AX,@DATA
	MOV DS,AX
	MOV ES,AX
	MOV AH,3Fh
	MOV BX,01h
	MOV CX, MAXCUMLE
	MOV DX,OFFSET STRING
	INT 21H
	AND AX,AX
	JZ DONE
	MOV CX,AX
	MOV DI,OFFSET STRING
    MOV AL,' '
	MOV AH,CL 
KONTROL:
    CMP AL,[DI]
    JZ SAY
	JNZ NO
SAY:
    INC BX
	CMP [DI+1],AL
    JZ ATLA
	
	
ATLA: 
	INC DI
	INC DX
	CMP AL,[DI]
	JZ ATLA 
NO:
	INC DI
	INC DX
	CMP ah,Dl
	JZ ATLA
	
	LOOP KONTROL   	

	MOV AX,BX
	MOV DX,AX
	OR DX,3030H
	INT 21h
DONE:
		MOV AH,4CH
		INT 21H
ENDP
END START
```

## lab61

```asm
;EEM 332 - LAB 6 - ÖNÇALIŞMA SORU 1

		.MODEL SMALL
		.STACK 64
		.DATA
SONUC	DB	100 DUP(?)
		

		.CODE
MAIN		PROC	FAR		;this is the program entry point
		MOV	AX,@DATA	;load the data segment address
		MOV	DS,AX	;assign value to DS
		
	
		SUB DX,DX	;DX'i sıfırla
		SUB BX,BX
		INC DX		;En az bir kelime
		
	DEVAM:	MOV AH,1
		INT 21H
		CMP AL,0DH		;Enter'a basıldı mı?
		JZ  BITIS		;Basıldıysa döngüden çık
		MOV [SI],AL
		INC SI			;stringi arttır
		CMP AL,20H		;Boşluk mu?
		JZ  BOSLUK		;Boşluk ise DX'i arttır
		JMP DEVAM		;Devam

	BOSLUK: INC DX		;Boşluk, DX'i arttır
		JMP DEVAM    

		MOV DI,DX	
	
	

		;Lab Föyünde verilen Hex 'i Decimal'e çeviren kod

	BITIS:  MOV DI,DX
		MOV AX,DI 	;HEXVAL ADRESINDEN DEGERI AX’E AL
		SUB DX,DX
		MOV BL,000AH 	;BX YAZMACINA 0A DEGERINI ATA
		DIV BL 		;AX YAZMACINI BX YAZMACINA BÖL
		MOV DH,AL 	;CIKAN DEGER DECIMAL SAYININ 10LAR
		MUL BL 		;DEGERI BX’LE CARP
		MOV CX,DI
		SUB CX,AX	;CX VE AX YAZMACLARININ FARKINI AL
		MOV DL,CL 	;CIKAN DEGER DECIMAL SAYININ 1LER 


		OR  DX,3030H		;ASCII'ye çevir
		XCHG DL,DH		;Basamakları düzenle
		MOV DI,OFFSET SONUC
		MOV AX,0D0AH		;Alt Satıra yazdırmak için
		MOV [DI],AX		;Alt Satıra yazdırmak için
		ADD DI,2
		MOV [DI],DL
		INC DI
		MOV [DI],DH
		INC DI	
		MOV DX,OFFSET SONUC	
		MOV AH,'$'		;String sonu
		MOV [DI],AH



		MOV 	AH,09H	;Yazdır
		INT 	21H
		
		MOV	AH,4CH	;set up to
		INT	21H		;return to DOS
MAIN		ENDP			
		END  MAIN		;this is the program exit point
```

## lab62

```asm
.model small
.stack 100
.data
rnum dw ?
	.code
main proc far

        in al, 40h			; read micro-clock for initial seed
        mov ah, al
        in al, 40h
        xchg al, ah
        or ax, 1
        mov rnum, ax			;rnum değeri ax değerini alır

	mov bx,0100			;0-100 arası için kıstılama yapacak register
	div bx				;bölme işlemi kalan dx registerinde
	add dx,1			;mod işlemi gereği 1 toplanması
	
	mov ax,dx	
	MOV aH, 0H
					;decimale çevirmek için gerekli işlemler		
	MOV BX, 10	
	DIV BL
	OR aX, 3030H	

	mov dl,al
	mov bl,ah
	mov ah,02H
	int 21H

	mov dl,bl			;yazdırma işlemleri
	mov ah,02H
	
	int 21H
	mov ah,4cH			;DOS a dönüş
	int 21H

main endp
	end main
```

## lab6d2

```asm
;EEM 332 - LAB 6 - ÖNÇALIŞMA SORU 1

		.MODEL SMALL
		.STACK 64
		.DATA
SONUC		DB	100 DUP(?)
ISIM		DB	100 DUP(?)
		

		.CODE
MAIN		PROC	FAR		;this is the program entry point
		MOV	AX,@DATA	;load the data segment address
		MOV	DS,AX		;assign value to DS



		SUB DX,DX	;DX'i sıfırla
		SUB CX,CX
		MOV SI,OFFSET ISIM
		MOV DI,OFFSET SONUC

		
	DEVAM:	MOV AH,1
		INT 21H
		CMP AL,0DH	;Enter'a basıldı mı?
		JZ  DONDURME		;Basıldıysa döngüden çık
		MOV [SI],AL
		INC SI		;stringi arttır
		JMP DEVAM	;Devam

      DONDURME: MOV AH,'$'
		MOV [SI],AH
		MOV SI,OFFSET ISIM


	ARA:	INC CL
		MOV AH,20H
		CMP [SI],AH	;Boşluk mu?
		JZ  YAZ		;Boşluk ise ÇIK
		INC SI
		JMP ARA		;Devam


	YAZ: 	MOV AH,'$'
		INC SI
		CMP [SI],AH
		JZ  BAS		;SONU ise ÇIK
		MOV AH,[SI]
		MOV [DI],AH
		INC DI
		JMP YAZ

	BAS:	MOV SI,OFFSET ISIM
		MOV AH,' '
		MOV [DI],AH
		INC DI
		DEC CL
	YAZ2:	MOV AH,[SI]
		MOV [DI],AH
		INC DI
		INC SI
		LOOP YAZ2


		MOV AX,0D0AH
		MOV [DI],AX	;Alt Satıra yazdırmak için
		MOV DX,OFFSET SONUC
		ADD DI,2	;İki adet 8 bit
		MOV AH,'$'	;String sonu
		MOV [DI],AH

		MOV 	AH,09H
		INT 	21H

		SUB DI,2
		MOV AH,'$'	;String sonu
		MOV [DI],AH

	        MOV AH,1
		INT 21H
		CMP AL,0DH		;Enter'a basıldı mı?
		JNZ  SON		;Basıldıysa döngüden çık

		MOV AH,'$'	;String sonu

	
		MOV SI,OFFSET SONUC
	 HESAP:	CMP [SI],AH
		JZ SAYITMM
		INC CL
		INC SI
		JMP HESAP
	SAYITMM:INC CL
		MOV SI,OFFSET ISIM
		MOV DI,OFFSET SONUC
		JMP BIRDAHA

	BIRDAHA:MOV AH,[DI]
		MOV [SI],AH
		INC SI
		INC DI
		LOOP BIRDAHA

		MOV SI,OFFSET ISIM
		MOV DI,OFFSET SONUC
		JMP ARA



		MOV 	AH,09H
		INT 	21H
		
	SON:	MOV	AH,4CH		;set up to
		INT	21H		;return to DOS
MAIN		ENDP			
		END	MAIN		;this is the program exit point
```

## lab6d3

```asm
;EEM 332 - LAB 6 - ÖNÇALIŞMA SORU 1

		.MODEL SMALL
		.STACK 64
		.DATA
SONUC		DB	100 DUP(?)
ISIM		DB	100 DUP(?)
RNUM 		DW 	?
		

		.CODE
MAIN		PROC	FAR		;this is the program entry point
		MOV	AX,@DATA	;load the data segment address
		MOV	DS,AX		;assign value to DS



		SUB DX,DX	;DX'i sıfırla
		SUB CX,CX
		MOV SI,OFFSET ISIM
		MOV DI,OFFSET SONUC

		
	DEVAM:	MOV AH,1
		INT 21H
		CMP AL,0DH	;Enter'a basıldı mı?
		JZ  DONDURME		;Basıldıysa döngüden çık
		MOV [SI],AL
		INC SI		;stringi arttır
		JMP DEVAM	;Devam

      DONDURME: MOV AH,'$'
		MOV [SI],AH
		MOV SI,OFFSET ISIM
	

	ARA1:	MOV AH,20H
		MOV AL,'$'
		CMP [SI],AH	
		JZ  BOSSAY		;Boşluk ise sayacı arttır
		CMP [SI],AL
		JZ  RANDOM		;BİTTİ İSE ÇIK	
		INC SI
		JMP ARA1		;Devam

	BOSSAY:	INC CL
		INC SI
		JMP ARA1


	RANDOM: IN AL, 40H		; READ MİCRO-CLOCK FOR İNİTİAL SEED
		MOV AH, AL
		IN AL, 40H
		XCHG AL, AH
  		OR AX, 1
     		MOV RNUM, AX		;RNUM DEĞERİ AX DEĞERİNİ ALIR

		MOV BL,CL		;0-100 ARASI İÇİN	
		DIV BX			;BÖLME İŞLEMİ KALAN DX’DE
		ADD DX,1		;MOD İŞLEMİ GEREĞİ 1 TOPLANMASI
		
		
		MOV SI,OFFSET ISIM
		SUB CX,CX


	ARA:	INC CL
		MOV AH,20H
		CMP [SI],AH	;Boşluk mu?
		JZ  YAZ		;Boşluk ise ÇIK
		INC SI
		JMP ARA		;Devam


	YAZ: 	MOV AH,'$'
		INC SI
		CMP [SI],AH
		JZ  BAS		;SONU ise ÇIK
		MOV AH,[SI]
		MOV [DI],AH
		INC DI
		JMP YAZ

	BAS:	MOV SI,OFFSET ISIM
		MOV AH,' '
		MOV [DI],AH
		INC DI
		DEC CL
	YAZ2:	MOV AH,[SI]
		MOV [DI],AH
		INC DI
		INC SI
		LOOP YAZ2
	
		DEC DX
		MOV AH,'$'	;String sonu
		MOV [DI],AH
		JNZ TEKRAR


		MOV AX,0D0AH
		MOV [DI],AX	;Alt Satıra yazdırmak için
		MOV DX,OFFSET SONUC
		ADD DI,2	;İki adet 8 bit
		MOV AH,'$'	;String sonu
		MOV [DI],AH

		MOV 	AH,09H
		INT 	21H

		SUB DI,2
		MOV AH,'$'	;String sonu
		MOV [DI],AH

	        MOV AH,1
		INT 21H
		CMP AL,0DH		;Enter'a basıldı mı?
		JNZ  SON		;Basıldıysa döngüden çık

		MOV AH,'$'	;String sonu

	
	TEKRAR:	MOV SI,OFFSET SONUC
	 HESAP:	CMP [SI],AH
		JZ SAYITMM
		INC CL
		INC SI
		JMP HESAP
	SAYITMM:INC CL
		MOV SI,OFFSET ISIM
		MOV DI,OFFSET SONUC
		JMP BIRDAHA

	BIRDAHA:MOV AH,[DI]
		MOV [SI],AH
		INC SI
		INC DI
		LOOP BIRDAHA

		MOV SI,OFFSET ISIM
		MOV DI,OFFSET SONUC
		JMP ARA



		MOV 	AH,09H
		INT 	21H
		
	SON:	MOV	AH,4CH		;set up to
		INT	21H		;return to DOS
MAIN		ENDP			
		END	MAIN		;this is the program exit point
```

## 332 deney 6

```asm
                .MODEL SMALL
		.STACK 64
		.DATA
aamcevrim db '00$'
.code
mov ax,@data
mov ds,ax
mov es,ax

call aamsonuc proc

 mov ax, 20h
 mov bl, 0Ah
 div bl ;AX=0203 yapar.
or ax,3030h ;AX’teki 0203h artık 3233h oldu.
mov sonuc, ax
lea dx,sonuc
 mov ah,9
 int 21h

aamsonuc endp
 mov ah,4ch
int 21h
end
```

## brc

```asm

	.MODEL SMALL
	.STACK 64 (?)

;________DATA SEGMENT________________________________	



	.DATA
CR	EQU	0DH
LF	EQU	0AH


MSG	DB	'Kelimeleri Sayilacak Cumleyi Giriniz..:$'
MSG2	DB	CR, LF, 'Girilen Cumledeki Kelime adeti..:', '$'
MSG3	DB	' Adettir...$'

STR1	DB  100, ?, 100 DUP (0)	; buraya klavyeden gelicek string
	ORG 100



;________CODE SEGMENT_________________________________
 
    
	.CODE
MAIN	PROC	FAR                                   
	MOV AX, @DATA                          
	MOV DS, AX                                      
	
	XOR AX,AX		

	CALL CLRSCR		
	CALL CURSOR		
	
	MOV DX, OFFSET MSG
	CALL DISPLAYSTR

	MOV DX, OFFSET STR1	; DX e stringin adresi atılıyor.
	CALL INPUT

	MOV BX, OFFSET STR1
	CALL FNDSPC		

	CALL CASCII
				
				
	MOV DX, OFFSET MSG2
	CALL DISPLAYSTR
	
	MOV AH,02H
	MOV DL,CH
	INT 21H
	
	MOV DL,CL
	INT 21H
	
	MOV DX, OFFSET MSG3
	CALL DISPLAYSTR	
	
	MOV AH, 4CH		; EXIT to DOS 
	INT 21H			

MAIN	ENDP			
	


;_________________________________________________________
;_______CLRSCR Fonksiyonu__________________________________
;_________________________________________________________


CLRSCR	PROC
	MOV AX, 0600H
	MOV BH, 07H
	MOV CX, 0000H
	MOV DX, 184FH
	INT 10H
	RET
CLRSCR	ENDP	
	
;_________________________________________________________
;_______CURSOR  Fonksiyonu_________________________________
;_________________________________________________________


CURSOR	PROC
	MOV AH, 02H
	MOV BH, 00H
	MOV DL, 00H
	MOV DH, 00H	;***************************************
	INT 10H
	RET
CURSOR	ENDP	
	

;_________________________________________________________
;_______INPUT Fonksiyonu___________________________________
;_________________________________________________________


INPUT	PROC

	MOV AH,0AH		;AH=0AH String  için INT 21 değeri.
;DX= STR ADDRESS******************
	INT 21H			; String DX in gösterdiği adreste.
	RET
INPUT	ENDP


;_________________________________________________________
;_______FNDSPC Fonksiyonu__________________________________
;_________________________________________________________


FNDSPC	PROC

	
	XOR DX,DX
	
SPACE:	INC DX			
				; en son giren space en son kelimenin başladıı yer
SEARCH:	MOV AL,[BX]
	INC BX
	CMP AL, 20H		;space arıoz 
	JE SPACE			; space varsa spacein indexini kaydetmek için SPACE e git dioz  
	CMP AL,0DH		; NULL mı acaba Null sa string bitti loopdan defol
	JE LOST		
	JMP SEARCH		
	
LOST:	RET			; DX= Kaç Space olduğu. 
				; BX=  NULL ın indexi.

FNDSPC	ENDP


;_________________________________________________________
;_______DISPLAYSTR Fonksiyonu______________________________
;_________________________________________________________


DISPLAYSTR	PROC
	MOV AH, 09H
; DX= STR ADDRESS *****************************************
	INT 21H
	RET
DISPLAYSTR ENDP



;_________________________________________________________
;_______CASCII Fonksiyonu______________________________
;_________________________________________________________


CASCII	PROC
	
	MOV AX, DX
	
	MOV CL, 04H
	SHL AX, CL
	SHR AL, CL
	OR AX, 3030H

	MOV CX, AX
	
	RET
CASCII	ENDP


;_________________________________________________________
;_______RWASCII Fonksiyonu______________________________
;_________________________________________________________


	



;__________________________________________________________
	END MAIN
```

## calisma-807

```asm

	.MODEL SMALL
	.STACK 64 (?)

;________DATA SEGMENT________________________________	



	.DATA
CR	EQU	0DH
LF	EQU	0AH


STR1	DB  100, ?, 100 DUP (0)	; buraya klavyeden gelicek string
	ORG 100
STR2	DB CR, LF, 100 DUP (?), '$'	; burası deiştirilmiş string


MSG	DB	'Donusturulecek Cumleyi Giriniz..:$'
	ORG 22H
MSG2	DB	CR, LF, 'Donusturulen Cumle..:', '$'
	ORG 20H


;________CODE SEGMENT_________________________________
 
    
	.CODE
MAIN	PROC	FAR                                   
	MOV AX, @DATA                          
	MOV DS, AX                                      
	
	XOR AX,AX		

	
	
	MOV DX, OFFSET MSG
	MOV AH, 09H
	INT 21H		 
				
				

	MOV DX, OFFSET STR1	 
	MOV AH,0AH		
	INT 21H			
			

	MOV BX, OFFSET STR1	
	XOR DX,DX
	
SPACE:	MOV DX, BX		
				
SEARCH:	MOV AL,[BX]
	INC BX
	CMP AL, 20H		 
	JE SPACE			  
	CMP AL,0DH		
	JE LOST		
	JMP SEARCH		

	MOV AX, OFFSET STR1
	ADD AX, DX
	MOV SI, AX

	MOV AX, OFFSET STR2
	MOV DI, AX

	MOV AX, BX
	SUB AX, DX
	MOV CX, AX
	DEC CX
	
	
TURN:	MOV AL, [SI]
	MOV [DI], AL
	INC SI
	INC DI
	LOOP TURN
	
	MOV AL, 20H
	MOV [DI],  AL
	INC DI

	MOV AX, OFFSET STR1
	INC AX
	INC AX
	MOV SI, AX

COPY:	MOV AL, [SI]
	MOV [DI], AL
	INC DI
	INC SI
	CMP SI, DX
	JC COPY	


	MOV DX, OFFSET MSG2
	MOV AH, 09H
	INT 21H
	
	
	MOV DX, OFFSET STR2
	MOV AH, 09H
	INT 21H
			
	MOV AH, 4CH		
	INT 21H			

MAIN	ENDP			
	


	END MAIN
```

## calisma-808

```asm
		.MODEL SMALL
		.STACK 64 (?)
		.DATA

	BRC	DB  100  (?)
		ORG 100
    
		.CODE
	MAIN	PROC	FAR                                   
		MOV AX, @DATA                          
		MOV DS, AX                                      
		SUB AX,AX
		MOV AH,0AH
		LEA DX, BRC
		INT 21H
		
		SUB DX,DX
		LEA BX, BRC

BOS:		INC DL
		
DEVAM:	MOV AL,[BX]
		INC BX
		CMP AL,20H
		JE BOS
		CMP AL,0DH
		JE DIGER
		JMP DEVAM
	
DIGER:	SUB AX,AX
		MOV AL,DL
		MOV CL, 04H
		SHL AX, CL
		SHR AL, CL
		OR AX,3030H
		MOV CX, AX
		MOV AH,02H
		MOV DL,CH
		INT 21H
		MOV DL,CL
		INT 21H
		MOV AH, 4CH		
		INT 21H			

MAIN	ENDP			
	END MAIN
```

## calisma-809

```asm

	.MODEL SMALL
	.STACK 64 (?)

;________DATA SEGMENT________________________________	



	.DATA
CR	EQU	0DH
LF	EQU	0AH


STR1	DB  100, ?, 100 DUP (0)	; buraya klavyeden gelicek string
	ORG 100
STR2	DB CR, LF, 100 DUP (?), '$'	; burası deiştirilmiş string


MSG	DB	'Donusturulecek Cumleyi Giriniz..:$'
	ORG 22H
MSG2	DB	CR, LF, 'Donusturulen Cumle..:', '$'
	ORG 20H


;________CODE SEGMENT_________________________________
 
    
	.CODE
MAIN	PROC	FAR                                   
	MOV AX, @DATA                          
	MOV DS, AX                                      
	
	XOR AX,AX		

	CALL CLRSCR		
	CALL CURSOR		
	
	MOV DX, OFFSET MSG
	CALL DISPLAYSTR		 
				
				

	MOV DX, OFFSET STR1	 
	CALL INPUT		

	MOV BX, OFFSET STR1	
	CALL FNDSPC		

	MOV AX, OFFSET STR1
	ADD AX, DX
	MOV SI, AX

	MOV AX, OFFSET STR2
	MOV DI, AX

	CALL REVERT		


	MOV DX, OFFSET MSG2
	CALL DISPLAYSTR
	
	
	MOV DX, OFFSET STR2
	CALL DISPLAYSTR
			
	MOV AH, 4CH		
	INT 21H			

MAIN	ENDP			
	


;_________________________________________________________
;_______CLRSCR Fonksiyonu__________________________________
;_________________________________________________________


CLRSCR	PROC
	MOV AX, 0600H
	MOV BH, 07H
	MOV CX, 0000H
	MOV DX, 184FH
	INT 10H
	RET
CLRSCR	ENDP	
	
;_________________________________________________________
;_______CURSOR  Fonksiyonu_________________________________
;_________________________________________________________


CURSOR	PROC
	MOV AH, 02H
	MOV BH, 00H
	MOV DL, 00H
	MOV DH, 00H	
	INT 10H
	RET
CURSOR	ENDP	
	

;_________________________________________________________
;_______INPUT Fonksiyonu___________________________________
;_________________________________________________________


INPUT	PROC

	MOV AH,0AH		
	INT 21H			
	RET
INPUT	ENDP


;_________________________________________________________
;_______FNDSPC Fonksiyonu__________________________________
;_________________________________________________________


FNDSPC	PROC

	;BX= OFFSET STR*******************************
	XOR DX,DX
	
SPACE:	MOV DX, BX		
				
SEARCH:	MOV AL,[BX]
	INC BX
	CMP AL, 20H		 
	JE SPACE			  
	CMP AL,0DH		
	JE LOST		
	JMP SEARCH		
	
LOST:	RET			; DX= Son kelimenin yeri 
				; BX=  NULL ın indexi.

FNDSPC	ENDP


;_________________________________________________________
;_______REVERT Fonksiyonu__________________________________
;_________________________________________________________



REVERT	PROC
	
	MOV AX, BX
	SUB AX, DX
	MOV CX, AX
	DEC CX
	
	
TURN:	MOV AL, [SI]
	MOV [DI], AL
	INC SI
	INC DI
	LOOP TURN
	
	MOV AL, 20H
	MOV [DI],  AL
	INC DI

	MOV AX, OFFSET STR1
	INC AX
	INC AX
	MOV SI, AX

COPY:	MOV AL, [SI]
	MOV [DI], AL
	INC DI
	INC SI
	CMP SI, DX
	JC COPY
	
	RET
REVERT	ENDP


;_________________________________________________________
;_______DISPLAYSTR Fonksiyonu______________________________
;_________________________________________________________


DISPLAYSTR	PROC
	MOV AH, 09H
	INT 21H
	RET
DISPLAYSTR ENDP

;__________________________________________________________
	END MAIN
```

## lab66

```asm
		.MODEL SMALL
		.STACK 64
		.DATA
		ORG	0100H
CUMLE          	DB	100 DUP (?)
YEDEK		DB	100 DUP (?)			


		.CODE		
MAIN		PROC	FAR		
		MOV	AX,@DATA	
		MOV	DS,AX		
		MOV	AX,0
		MOV	SI,OFFSET CUMLE		
		MOV 	CX,100

KLAVYEDENOKU:
		MOV	AH,0
		INT 	16H
		MOV	[SI],AL
		INC	SI
		MOV	DL,AL
		MOV	AH,02
		INT	21H
		CMP	AL,' '		
		JNZ	BITTIMI        
		INC	BX
		LOOP	KLAVYEDENOKU
		
BITTIMI:	
		CMP	AL,'.'		
		JZ	BITTI		
		LOOP    KLAVYEDENOKU
		
BITTI:		
		MOV	AX,0
		MOV 	AL,BL
		MOV	CL,0AH
		DIV	CL		
		MOV	BX,AX
		
		MOV	AH,02
		MOV	DL,9			
		INT	21H
		
		MOV	AH,02H
		MOV	DL,BL
		OR	DL,30H	
		INT 	21H
		MOV	DL,BH
		OR	DL,30H
		INT	21H
		
ENTERBEKLE:
		MOV	AH,0
		INT	16H
		CMP	AL,'q'
		JZ	SONLANDIR
		CMP	AL,0DH
		JNZ	ENTERBEKLE

		DEC	SI
		DEC	SI

SONKELIMEBUL:
		MOV	BL,[SI]
		DEC	SI
		CMP	BL,' '
		JNZ	SONKELIMEBUL

		INC	SI	
		MOV	BX,SI


		MOV	DI,OFFSET YEDEK
BASAAT:		
		MOV	CL,[SI]
		MOV	[DI],CL
		INC	DI
		CMP	CL,'.'
		JNZ	BASAAT

		DEC	DI
		MOV	CL,' '
		MOV	[DI],CL
		MOV	SI,OFFSET CUMLE
		
KOPYALA:	
		INC	DI
		MOV	CL,[SI]
		MOV	[DI],CL
		INC	SI
		CMP	SI,BX
		JNZ	KOPYALA

		INC	DI
		MOV	CL,'.'
		MOV	[DI],CL

		MOV	SI,OFFSET CUMLE
		MOV	DI,OFFSET YEDEK

GERIKOPYALA:
		MOV	CL,[DI]
		MOV	[SI],CL
		INC	DI
		INC	SI
		CMP	CL,'.'
		JNZ	GERIKOPYALA

		MOV	CL,'$'
		MOV	[SI],CL

		MOV	AH,02H
		MOV	DL,09H
		INT	21H

		MOV	AH,09
		MOV	DX,OFFSET CUMLE
		INT	21H

		JMP	ENTERBEKLE

SONLANDIR:

		ENDP
		END MAIN
```

## lab7

```asm
CNT3		EQU 3FD6H
APORT3		EQU 3FD0H
BPORT3		EQU 3FD2H
CPORT3		EQU 3FD4H
RAME		EQU 0FFFFH

CODE 	SEGMENT
	ASSUME 	CS:CODE,   DS:CODE

	ORG  0

START:	MOV SP,RAME
	MOV AL,90H
	MOV DX,CNT3
	OUT DX,AL

J1:	MOV DX,APORT3
	IN AL,DX
	NOT AL
	MOV DX,BPORT3
	OUT DX,AL
	JMP  J1

CODE    ENDS
	END START
```

## lab72

```asm
CNT3		EQU 3FD6H
APORT3		EQU 3FD0H
BPORT3		EQU 3FD2H
CPORT3		EQU 3FD4H
RAME		EQU 0FFFFH

CODE 	SEGMENT
	ASSUME 	CS:CODE,   DS:CODE

	ORG  0

START:	MOV SP,RAME
	MOV AL,90H
	MOV DX,CNT3
	OUT DX,AL

J1:	MOV DX,APORT3
	IN AL,DX
	MOV DX,BPORT3
	OUT DX,AL
	JMP  J1

CODE    ENDS
	END START
```

## oncalisma6

```asm
.MODEL SMALL
		.STACK 64
		.DATA
		ORG   0100h
DAT		DB      100  DUP(?)
Sayi     DB      ?
		

		.CODE
MAIN		PROC			FAR          
		MOV			AX,#DAT
		MOV 			DS,AX
		SUB			AX,AX
		MOV 			CX,100
		MOV			SI,OFFSET DAT
		sub			bx,bx	

verial:
		mov			ax,0
		int			16h
		mov			[si],si
		inc 			si
		mov 			dl,al
		mov 			sh,02	
		cmp			sl,32d
		jnz			devam 
		İnc 			bx

devam:		cmp			sl,46 
		Jx			yazdır
		İnt 			21h 
		loop			verial

		inc			bl   
		sub			ax,ax
		mov 			al,bl	
		mov 			cl,10
		div			al, 
		mov			bx,ax

		mov 			dl,46
		int			21h
		mov 			ah,02
		int 			21h
		mov 			dl,09
		int 			21h
		mov			dl,ah
		or 			dl,46
		int 			21h
		mov 			dl,bh
		or 			dl,46
		int 			21h
		mov 			ah,4ch
		int 			21h


		ENDP
		END MAIN
```

## d6lab2

```asm
.MODEL SMALL
.STACK 100h
.DATA
UZUNLUK EQU 100 ; en fazla 100 karakter
BOY DW 0
CUMLE DB UZUNLUK DUP(?)
KELIME1 DB UZUNLUK DUP(?)
KELIME2 DB UZUNLUK DUP(?)
YAZI DB 'BIR CUMLE GIRIN:','$'

.CODE
BASLA:	MOV AX,@DATA
	MOV DS,AX

	MOV DX,OFFSET YAZI

	MOV AH,09H
	INT 21H		;EKRANA YAZDIRMA İŞLEMİ(DX'İN İÇERİĞİ)

	MOV AH,3FH	;READ/GET ENTRY
	MOV BX,0
	MOV CX,UZUNLUK	;CX 100 OLDU
	MOV DX,OFFSET CUMLE ; OKUMA İŞLEMİ BİTTİ

	INT 21H
	AND AX,AX	;AX'DE KAC KARAKTER GİRİLDİĞİ SAKLANACAK
	MOV CX,AX
	MOV BOY,CX

DEVAM:	MOV SI,OFFSET CUMLE;POINTER CUMLE'DEKİ İLK KARAKTERİ GÖSTERİYOR
	MOV DI,OFFSET KELIME1;POINTER KELIME1'DEKİ İLK KARAKTERİ GÖSTERİYOR

	MOV CX,BOY
	ADD SI,CX
	DEC SI

AKELIME:MOV AL,[SI]	;CUMLE'NİN İLK KARAKTERİ AL'YE ATILDI
	CMP AL,20H	;AL'DEKİ KARAKTER BOŞLUK MU?
	JE BUL		;BOŞLUK İSE BUL DÖNGÜSÜNE GİDİLİR
	MOV [DI],AL
	INC DI

BUL:	DEC SI
	CMP AL,20H	;AL'DEKİ KARAKTER BOŞLUK MU?
	LOOPNE BKELIME

	MOV AL,20H	;AL'DEKİ KARAKTER BOŞLUK MU?
	MOV [DI],AL	;BOŞLUK İSE DEVAM EDİLDİ VE BOŞLUK EKLENDİ
	INC DI
	MOV AL,24H	;'$' BİTİRME KARAKTERİ
	MOV [DI],AL	;STRING SONUNA '$' KARAKTERİ EKLENDİ

	MOV SI,OFFSET CUMLE
	MOV DI,OFFSET KELIME2

BKELIME:MOV AL,[SI]	;CUME'NİN İLK KARAKTERİ AL'YE ATILDI
	MOV [DI],AL
	INC SI
	INC DI
	LOOP BKELIME

	MOV AL,20H	;AL'DEKİ KARAKTER BOŞLUK MU?
	MOV [DI],AL	;BOŞLUK İSE DEVAM EDİLDİ VE BOŞLUK EKLENDİ
	INC DI
	MOV AL,24H	;'$' BİTİRME KARAKTERİ
	MOV [DI],AL	;CUMLE SONUNA '$' KARAKTERİ EKLENDİ

YAZ:	MOV DX,OFFSET KELIME1
	MOV AH,09H
	INT 21H		;EKRANA YAZDIRMA İŞLEMİ(DX'İN İÇERİĞİ)
	MOV DX,OFFSET KELIME2
	MOV AH,09H
	INT 21H		;EKRANA YAZDIRMA İŞLEMİ(DX'İN İÇERİĞİ)
	MOV SI,OFFSET CUMLE
	MOV DI,OFFSET KELIME1
	MOV CX,BOY

KOPYA:	MOV AL,[DI]
	MOV [SI],AL
	INC SI
	PUSH SI
	INC DI
	CMP AL,24H	;SON MU?
	LOOPNE KOPYA
	
	MOV CX,BOY
	POP BX
	MOV SI,OFFSET CUMLE
	ADD SI,BX
	MOV DI,OFFSET KELIME2

KOPYA2:	MOV AL,[DI]
	MOV [SI],AL
	INC SI
	INC DI
	CMP AL,24H	;SON MU?
	LOOPNE KOPYA2

	INC SI
	MOV AL,24H	;'$' BİTİRME KARAKTERİ
	MOV [SI],AL
	MOV AH,1
	INT 21H		;KARAKTER OKU
	CMP AL,1BH
	JE SON
	CALL DEVAM

SON:	MOV AH,4CH
	INT 21H		;PROGRAM SONU
END BASLA
```

## d6lab3

```asm
.MODEL LARGE
.STACK 64
.DATA
UZUNLUK EQU 100 ; en fazla 100 karakter
CUMLE DB UZUNLUK DUP(?)
KELIME DB UZUNLUK DUP(?)
RASTGELE DB UZUNLUK DUP(?)
.CODE
MAIN	PROC FAR	;BAŞLANGIÇ AYARLARI
	MOV AX,@DATA
	MOV DS,AX

	MOV DI,OFFSET CUMLE;POINTER CUMLENIN İLK HARFİNDE
	MOV CX,03h	;3 DEFA DÖNECEK
	PUSH CS
	MOV BX,0	;BL SIFIRLANDI

OKU:	MOV AH,01H	;
	INT 21H		;KARAKTER OKUNDU
	MOV [DI],AL
	INC DI
	CMP AL,13	;BASILAN TUŞ ENTER MI?
	JNE OKU
	MOV DI,OFFSET CUMLE;POINTER CUMLENIN İLK HARFİNDE
	MOV SI,OFFSET KELIME;POINTER KELIMENIN İLK HARFİNDE
	MOV [SI],DI
	INC SI
	INC DI

KEL_AL:	MOV AL,[DI]
	INC DI
	CMP AL,13	;BASILAN TUŞ ENTER MI?
	JE ENTIR
	CMP AL,' '	;BOŞLUK MU
	JNE KEL_AL
	INC BL
	MOV BH,BL
	MOV DX,DI
	MOV [SI],DX
	INC SI
	JMP KEL_AL

ENTIR:	INC BH
	MOV AL,13	;ENTER İŞLEMİ
	MOV [SI],AL
	MOV DI,OFFSET RASTGELE

RAST:	MOV AH,2CH	;
	INT 21H		;SISTEM ZAMANI
			;CH = SAAT
			;CL = DAKİKA
			;DH = SANİYE
			;DL = 1/100 SANİYE
	MOV SI,OFFSET KELIME
	ADD SI,DX
	MOV AL,[SI]
	MOV [DI],AL
	INC DI

SON:	MOV AX,0
	INC SI
	MOV AL,[SI]
	DEC SI
	MOV [SI],AL	;YER DEĞİŞTİRME OLDU
	INC SI
	CMP AL,13	;BASILAN TUŞ ENTER MI?
	JNE SON
	DEC BL
	DEC BH
	CMP BH,0h
	JNE RAST
	MOV DH,13
	MOV [DI],DH
	MOV DI,OFFSET KELIME

OTEKI:	MOV SI,OFFSET CUMLE
	MOV AX,0
	MOV AL,[DI]
	ADD SI,AX
	MOV DH,13
	CMP [DI],DH
	JE TEKRAR
	INC DI

YAZ:	MOV DX,0
	MOV DL,[SI]
	INC SI
	CMP DL,13	;BASILAN TUŞ ENTER MI?
	JE BOSLUK;
	MOV AH,02h	;
	INT 21h		;EKRANA YAZDIRMA İŞLEMİ(AL'NİN İÇERİĞİ)
	CMP AL,' '	;BOŞLUK MU?
	JE OTEKI
	JMP YAZ

BASA:	JMP KEL_AL

BOSLUK:	MOV DL,' '
	MOV AH,02h	;
	INT 21h		;EKRANA YAZDIRMA İŞLEMİ(AL'NİN İÇERİĞİ)
	JMP OTEKI

TEKRAR:	POP CX
	DEC CX
	PUSH CX
	MOV DI,OFFSET CUMLE
	MOV SI,OFFSET KELIME
	MOV [SI],DI
	INC SI
	INC DI
	MOV BX,0
	CMP CX,0
	JNE BASA
	
	MOV AH,4CH
	INT 21H		;PROGRAM SONU
MAIN ENDP
END MAIN
```

## d6oc1

```asm
.MODEL SMALL
.STACK 100h
.DATA
UZUNLUK EQU 100 ; en fazla 100 karakter
CUMLE DB UZUNLUK DUP(?)
YEDEK DW ?
YAZI DB 'BIR CUMLE GIRIN:','$'
SONUC DB 'KELIME SAYISI:','$'

.CODE
BASLA:	MOV AX,@DATA
	MOV DS,AX

	MOV DX,OFFSET YAZI

	MOV AH,09H
	INT 21H		;EKRANA YAZDIRMA İŞLEMİ(DX'İN İÇERİĞİ)

	MOV AH,3FH	;READ/GET ENTRY
	MOV CX,UZUNLUK	;CX 100 OLDU
	MOV DX,OFFSET CUMLE ; OKUMA İŞLEMİ BİTTİ

	INT 21H
	AND AX,AX	;AX'DE KAC KARAKTER GİRİLDİĞİ SAKLANACAK
	JZ SON		;
	MOV CX,AX	;SAYAÇ DEĞİŞTİRİLDİ
	MOV BX,0
	ADD BX,1	;İLK KELİME DAHİL
	
	MOV SI,OFFSET CUMLE;POINTER CUMLE'DEKİ İLK KARAKTERİ GÖSTERİYOR

SAYAC:	MOV AL,[SI]	;CUMLE'NİN İLK KARAKTERİ AL'YE ATILDI
	CMP AL,20H	;AL'DEKİ KARAKTER BOŞLUK MU?
	JE BOSLUK	;BOŞLUK İSE BOSLUK DÖNGÜSÜNE GİDİLİR
	INC SI		;BOŞLUK DEĞİLSE DEVAM
	LOOP SAYAC	;DÖNGÜYE DEVAM
	CALL DEVAM	;DONGU SONUNDA BOSLUK VE ARTTIR ILERLEMESIN!!!!

BOSLUK:	INC SI;
	MOV AL,[SI]	;BOŞLUKTAN SONRAKİ KARAKTER AL'YE ATILIR
	INC SI
	CMP AL,20H	;AL'DEKİ KARAKTER BOŞLUK MU?
	JNE ARTTIR	;BOŞLUK DEĞİLSE SAYAÇ ARTTIRMA DÖNGÜSÜNE
	LOOPE BOSLUK	;KARAKTER BULANA KADAR DEVAM

ARTTIR:	INC BX		;KELİME SAYACI ARTTIRILIR
	LOOP SAYAC	;CUMLE BİTENE KADAR DEVAM

DEVAM:	MOV YEDEK,BX	;KELİME SAYACINI YEDEĞE ALDIK
	
	MOV DX,OFFSET SONUC

	MOV AH,09H
	INT 21H		;EKRANA YAZDIRMA İŞLEMİ(DX'İN İÇERİĞİ)

	MOV AX,YEDEK	;KELİME SAYISI AX'E YÜKLENDİ
	MOV AH,0H	;
	MOV BX,10	;
	DIV BL		;AX DECIMAL YAPILDI
	OR AX,3030H	;DECIMAL AX ASCII YAPILDI
	MOV YEDEK,AX	;ASCII DEGER YEDEKLENDI

	CMP AL,30H	;AL'DEKI DEGER SIFIR MI?
	JE BASAMAK	;0 DEĞİLSE SAYI ÇİFT HANELİ

	MOV DL,AL
	MOV AH,02H
	INT 21H		;EKRANA YADIRMA İŞLEMİ(AL'NİN İÇERİĞİ)

BASAMAK:MOV AX,YEDEK
	MOV DL,AH
	MOV AH,02H	;
	INT 21H		;EKRANA YADIRMA İŞLEMİ(AL'NİN İÇERİĞİ)


SON:	MOV AH,4CH
	INT 21H		;PROGRAM SONU
END BASLA
```

## d6oc2

```asm
.MODEL SMALL
.STACK 100h

.CODE
BASLA:	MOV AH,2CH
	INT 21H		;GET SYSTEM TIME
			;CH = HOUR
			;CL = MINUTE
			;DH = SECOND
			;DL = 1/100 SECONDS

	MOV AL,DL
	
	MOV AH,0	;
	MOV BX,10	;
	DIV BL		;AX DECIMAL'E ÇEVRİLDİ
	OR AX,3030H	;DECIMAL AX ASCII'YE ÇEVRİLDİ

	MOV CX,0
	MOV CL,AH
	MOV DL,AL

	MOV AH,02H	;
	INT 21H		;EKRANA YAZDIRMA İŞLEMİ(AL'NİN İÇERİĞİ)

	MOV DL,CL	;
	INT 21H		;EKRANA YAZDIRMA İŞLEMİ(AH'NİN İÇERİĞİ)

	MOV AH,4CH	;
	INT 21		;PROGRAM SONLANDIRILDI

END BASLA
```

## RAND3

```asm
		.MODEL LARGE
		.STACK 64
		.DATA
CUMLE		DB	100 DUP(?)
KELIME_BAS	DB	100 DUP(?)
RANDOM_KEL	DB	100 DUP(?)
		.CODE
MAIN		PROC	FAR		
		MOV	AX,@DATA	
		MOV	DS,AX		
		MOV	DI,OFFSET CUMLE
		MOV	CX,03h
		PUSH	CX
		SUB	BL,BL
CUMLE_AL:	MOV	AH,01H
		INT	21H
		MOV	[DI],AL
		INC	DI
		CMP	AL,13
		JNE	CUMLE_AL
		MOV	DI,OFFSET CUMLE
		MOV	SI,OFFSET KELIME_BAS
		MOV	[SI],DI
		INC	DI
		INC	SI
KEL_BAS_AL:	MOV	AL,[DI]
		INC	DI
		CMP	AL,13
		JE	ENTER_EKLE
		CMP	AL,' '
		JNE	KEL_BAS_AL
		INC	BL
		MOV	BH,BL
		MOV	DX,DI
		MOV	[SI],DX
		INC	SI
		JMP	KEL_BAS_AL
ENTER_EKLE:	INC	BH
		MOV	AL,13
		MOV	[SI],AL
		MOV	DI,OFFSET RANDOM_KEL
RAND_KEL:	MOV	AH,2Ch
		INT	21h
		MOV	SI,OFFSET KELIME_BAS
		POP	CX
		SHR	DL,CL
		PUSH	CX
		AND	DL,BL
		SUB	DH,DH
		ADD	SI,DX
		MOV	AL,[SI]
		MOV	[DI],AL
		INC	DI
SON_BUL:	SUB	AX,AX
		INC	SI
		MOV	AL,[SI]
		DEC	SI
		MOV	[SI],AL
		INC	SI
		CMP	AL,13
		JNE	SON_BUL
		DEC	BL
		DEC	BH
		CMP	BH,0h
		JNE	RAND_KEL
		MOV	DH,13
		MOV	[DI],DH
		MOV	DI,OFFSET RANDOM_KEL
YAZ_DIGER_KEL:	MOV	SI,OFFSET CUMLE
		SUB	AX,AX
		MOV	AL,[DI]
		SUB	AH,AH
		ADD	SI,AX
		MOV	DH,13
		CMP	[DI],DH
		JE	TEKRAR_YAP
		INC	DI
YAZ:		SUB	DX,DX
		MOV	DL,[SI]
		INC	SI
		CMP	DL,13
		JE	BOSLUK_KOY
		MOV	AH,02h
		INT	21h
		CMP	AL,' '
		JE	YAZ_DIGER_KEL
		JMP	YAZ
BASA_DON:	JMP	KEL_BAS_AL
BOSLUK_KOY:	MOV	DL,' '
		MOV	AH,02h
		INT	21h
		JMP	YAZ_DIGER_KEL
TEKRAR_YAP:	POP	CX
		DEC	CX
		PUSH 	CX
		MOV	DI,OFFSET CUMLE
		MOV	SI,OFFSET KELIME_BAS
		MOV	[SI],DI
		INC	DI
		INC	SI
		SUB	BX,BX
		CMP	CX,0
		JNE	BASA_DON
		MOV	AH,4CH		
		INT	21H		
MAIN		ENDP			
		END	MAIN
```
