---
baslik: EEM332 Mikroişlemciler: 2007 Vize Soruları ve Çözüm Kontrolleri
ozet: 13 Nisan 2007 vizesinde döngüler, yığın, aritmetik bayraklar, ASCII dönüşümü ve dolaylı adresleme.
---

Başkent Üniversitesi EEM332 Mikroişlemciler ders arşivindeki bu içerik, fotoğraflanmış sayfalardan metne aktarıldı. 13 Nisan 2007 vizesinde döngüler, yığın, aritmetik bayraklar, ASCII dönüşümü ve dolaylı adresleme. Öğrenci adları ve numaraları çıkarıldı. Fotoğraflar özel arşivde tutulur. Temiz tarayıcı kopyasının iki sayfalık PDF sürümü yazının sonunda ZIP olarak indirilebilir.

## Döngü sonunda BX

```asm
MOV BX,0005H
MOV CX,30H
L1: CMP CX,0010H
    JA L2
    INC BX
L2: LOOP L1
```

CX, 10H veya daha küçük olduğunda BX artırılır. On altı artışın sonunda BX = 0015H olur.

## PUSH ve yığın düzeni

Başlangıç değerleri SP=1236H, AX=24B6H, DI=85C2H ve DX=5F93H olarak verilmiştir.

```asm
PUSH AX
PUSH DI
PUSH DX
```

| Adres | Bayt |
| --- | --- |
| SS:1230 | 93H |
| SS:1231 | 5FH |
| SS:1232 | C2H |
| SS:1233 | 85H |
| SS:1234 | B6H |
| SS:1235 | 24H |

Son SP=1230H olur; SS:1236 bu komutlar tarafından değiştirilmez. Düşük anlamlı bayt düşük adrese yazılır.

## İşaretli toplama ve genişletme

```asm
DATA1 DB +80
DATA2 DB +85
SONUC DW ?
MOV AL,DATA1
MOV BL,DATA2
ADD AL,BL
JNO HIGH
MOV AL,DATA2
CBW
MOV BX,AX
MOV AL,DATA1
CBW
ADD AX,BX
HIGH: MOV SONUC,AX
```

İlk ADD sonunda AL=A5H, OF=1, CF=0, SF=1’dir. JNO atlamaz; iki pozitif sayı ayrı ayrı genişletilir. İkinci ADD sonunda AX=00A5H, OF=0, CF=0 ve SF=0 olur.

## İki ASCII rakamı oluşturma

AL=29H için kaynak program:

```asm
MOV AH,AL
AND AX,F00FH
MOV CL,4
SHR AH,CL
OR AX,3030H
XCHG AH,AL
```

Sonuç AX=3932H olur. AL’de ASCII “2”, AH’de ASCII “9” bulunur.

## Yazmaçlarla denklem

```asm
PUSH DX
MOV AX,4
MUL BX
PUSH AX
MOV AX,CX
MOV CX,7
AND DX,00
DIV CX
POP BX
ADD AX,BX
POP BX
XOR DX,DX
DIV BX
```

Taşma olmadığı ve ilk DX sıfır olmadığı varsayımıyla, başlangıç yazmaçları B, C ve D denirse sonuç floor((floor(C/7)+4B)/D) biçimindedir. DIV işaretsiz tamsayı bölümüdür; kalanlar ayrıca DX’e yazılır.

## LOOPNZ

```asm
MOV CX,17
TOP: SUB CX,2
     CMP CX,12
     LOOPNZ TOP
```

İlk turda CX sırasıyla 15 ve 14 olur. İkinci turda SUB ile 12’ye iner; CMP sonucunda ZF=1 olur. LOOPNZ yine CX’i azaltarak 11 yapar, ardından atlamadan çıkar. Son CX=11’dir.

## Bayraklar

F5H+0BH toplamının 8 bit sonucu 00H’dir: CF=1, SF=0, PF=1, AF=1 ve ZF=1.

## Çıkarma programını tamamlama

Kaynakta MOV DH,4CH; SUB DH,6EH; JNC Next sonrasında iki boş satır, ardından Next: MOV BL,DH vardır. Fotoğraftaki çözüm bu satırlara NOT DH ve INC DH yazar; böylece negatif farkın mutlak değeri elde edilir.

```asm
MOV DH,4CH
SUB DH,6EH
JNC Next
NOT DH
INC DH
Next: MOV BL,DH
```

Son BL=22H’dir. SUB işleminde oluşan CF=1; NOT ve INC tarafından değiştirilmez.

## Yazmaç dolaylı adreslemeyle beş baytın toplamı

Kaynak, AL’ye sırasıyla [0200], [0201], [0202], [0203] ve [0204] değerlerini ekleyen komutları döngüyle yazmayı ister. Fotoğraftaki yöntemin metin karşılığı:

```asm
MOV AL,0
MOV BX,0200H
MOV CX,5
NEXT: ADD AL,[BX]
      INC BX
      LOOP NEXT
```

*Not: Sayısal sonuçlar komutlar üzerinden kontrol edilmiştir. Son iki sorudaki bellek adresleri onaltılık olarak yorumlanmıştır; kaynakta bazı sabitlerin H eki yazılmamıştır.*
