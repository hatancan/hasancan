---
baslik: EEM332 Mikroişlemciler: 8086 Ödevleri ve Çalışma Soruları
ozet: 2004 ve 2005 ödev grupları, komut kodlama, adresleme, donanım ve program izleme soruları.
---

Bu yazı, Başkent Üniversitesi **EEM332 Mikroişlemciler** ders arşivindeki ilgili notları ve uygulamaları bir araya getiriyor (2004–2006). 2004 ve 2005 ödev grupları, komut kodlama, adresleme, donanım ve program izleme soruları. Belgelerin PDF arşiv kopyaları ve varsa kaynak kodları yazının sonunda ZIP olarak indirilebilir.

## EEM%20332%20odev11

Başkent Üniversitesi Elektrik-Elektronik Mühendisliği Bölümü EEM 332 Mikroişlemciler Ödev 1/Grup 1

ÖNEMLİ BİLGİ:        -Ödevleri 29 Mart 2004 Salı günü saat 17.00’ye kadar C302-B no’lu ofise teslim edebilirsiniz. -Ödevlerinizi, grubunuzu da belirterek, beyaz A4 kağıda hazırlayınız ve gerekiyorsa bir köşesinden zımbalayarak teslim ediniz (poşet dosya kabul edilmeyecektir). -Sadece adınızın bulunduğu gruba ait soruları cevaplayınız. Grup listesini web sayfasında bulabilirsiniz. -Kendi grubunuza ait olmayan soruları cevaplamanız durumunda ödev notunuz sıfır olarak değerlendirilecektir.

### 1) Aşağıda verilen komutlardan hangilerinin 8086/88 Assembly komutlarıyla kodlanıp

kodlanamadığını belirtin. Kodlanamayan var ise nedenini açıklayın.

a.MOV AX,27              g.MOV DS,9BF2 b.MOV AL,97F             h.MOV CX,397 c.MOV CS,3490            i.MOV AX,23FB9 d.MOV BX,CS              j.MOV AX,DL e.MOV CS,BH              k.MOV CH,AX f.MOV DS,BX              l.MOV SI,9516

### 2) Aşağıda verilen registerlar offset olarak kullanılmaktadır. Mantıksal adrese (logical

```asm
address) ulaşmak için default segmentlerin kullanıldığı varsayılırsa, her offset
```

registerinin ilgili olduğu segment registerını belirtiniz.

(a) BP     (b) DI    (c) IP   (d) SI     (e) SP       (f) BX

### 3) Aşağıda verilen işlemler için CF, PF, AF, ZF ve SF durumlarını bulunuz.

a. MOV BL,9FH        b. MOV AL,23H             c. MOV DX,10FFH

```asm
ADD BL,61H           ADD AL,97H                ADD DX,1
```

### 4) CS=1000, DS=2000, SS=3000, SI=4000, DI=5000, BX=6080, BP=7000,

```
AX=25FF, CX=8791 ve DX=1299 olarak verilmiştir. Aşağıdaki işlemler için kullanılan
```

hafıza yerlerinin (memory location) fiziksel adreslerini ve bu adreslerde saklanan değerleri belirtiniz.

(a) MOV [SI],AL (b) MOV[SI+BX+8],AH (c) MOV [BX],AX (d) MOV [DI+6],BX (e) MOV [DI][BX]+28,CX (f) MOV[BP][SI]+10,DX (g) MOV [3600],AX (h) MOV[BX]+30,DX (i) MOV [BP]+200,AX

Başkent Üniversitesi Elektrik-Elektronik Mühendisliği Bölümü EEM 332 Mikroişlemciler Ödev 1/Grup 1 (j) MOV [BP+SI+100],BX (k) MOV [SI]+50,AH (l) MOV [DI+BP+100],AX

### 5) Aşağıda verilenler için adresleme modlarının ne olduğunu belirtiniz.

(a) MOV AX,DS (b) MOV BX,5678H (c) MOV CX,[3000] (d) MOV AL,CH (e) MOV [DI],BX (f) MOV AL,[BX] (g) MOV DX,[BP+DI+4] (h) MOV CX,DS (i) MOV [BP+6],AL (j) MOV AH,[BX+SI+50] (k) MOV BL,[SI]+10 (l) MOV [BP][SI]+12,AX

### 6) Aşağıda verilen komutlar işletildikten sonra komutlarda adı geçen registerların ve

CF, ZF, PF içeriklerini gösteriniz.

a.     MOV AX,6AB3

```asm
MOV BX,98F1
ADD AL,BL
```

ADC AH,BH           ;add with carry

b.   DATA1 DB 4CH

```asm
DATA2 DB 6EH
DATA3 DB ?            ;data3 is empty and located in memory
MOV DH,DATA1          ;data1=4ch
SUB DH,DATA2          ;data2=6eh
JNC NEXT              ;JUMP if not carry
NOT DH                ;1’s complement
INC DH                ;increase one
NEXT:MOV DATA3,DH
```

### 7) Aşağıdaki sorularda istenilen işlemlerin gerçekleşmesi için gereken assembly

kodlarını yazınız. (AL=0FH ‘dir)

a.     AND komutunu kullanarak AL’nin içeriğini F0 yapınız. Bu durumda CF değeri ne olmalıdır? b.     SHL komutunu kullanarak AL’nin içeriğini F0 yapınız. Bu durumda CF değeri ne olmalıdır? c.     ROR komutunu kullanarak AL’nin içeriğini F0 yapınız. Bu durumda CF değeri ne olmalıdır? d.     STC ve SHR komutlarını kullanarak AL’nin içeriğini F0 yapınız. Bu durumda CF değeri ne olmalıdır?

Başkent Üniversitesi Elektrik-Elektronik Mühendisliği Bölümü EEM 332 Mikroişlemciler Ödev 1/Grup 1

### 8) Aşağıda verilen komutlardan ilk üçü çalıştırıldıktan sonra Stack Segment ve ikinci

üçü çalıştırıldıktan sonra registerların değeri ne olur? (SP=1245, AX=1122, BX=3344, CX=5566, DX=7788)

### SS:1238

```asm
PUSH AX                SS:1239
PUSH CX                SS:1240
PUSH BX                                              AX
```

### SS:1241

### SS:1243                       BX

```asm
POP DX                 SS:1243                       CX
POP AX                 SS:1244                       DX
POP BX                                               SP
```

### SS:1245

### SP=?

## EEM%20332%20odev12

Başkent Üniversitesi Elektrik-Elektronik Mühendisliği Bölümü EEM 332 Mikroişlemciler Ödev 1/Grup 2

ÖNEMLİ BİLGİ:       -Ödevleri 29 Mart 2004 Salı günü saat 17.00’ye kadar C302-B no’lu ofise teslim edebilirsiniz. -Ödevlerinizi, grubunuzu da belirterek, beyaz A4 kağıda hazırlayınız ve gerekiyorsa bir köşesinden zımbalayarak teslim ediniz (poşet dosya kabul edilmeyecektir). -Sadece adınızın bulunduğu gruba ait soruları cevaplayınız. Grup listesini web sayfasında bulabilirsiniz. -Kendi grubunuza ait olmayan soruları cevaplamanız durumunda ödev notunuz sıfır olarak değerlendirilecektir.

### 1) Aşağıda verilen komutlardan hangilerinin 8086/88 Assembly komutlarıyla kodlanıp

kodlanamadığını belirtin. Kodlanamayan var ise nedenini açıklayın.

a.MOV SI,9516              g.MOV DS,9BF2 b.MOV CX,397               h.MOV AL,97F c.MOV DS,BX                i.MOV CS,3490 d.MOV CH,AX                j.MOV CS,BH e.MOV AX,DL                k.MOV BX,CS f.MOV AX,23FB9             l.MOV AX,27

### 2) Aşağıda verilen registerlar offset olarak kullanılmaktadır. Mantıksal adrese (logical

```asm
address) ulaşmak için default segmentlerin kullanıldığı varsayılırsa, her offset
```

registerinin ilgili olduğu segment registerını belirtiniz.

(a) BX   (b) SI     (c) IP    (d) DI     (e) SP      (f) BP

### 3) Aşağıda verilenler için adresleme modlarının ne olduğunu belirtiniz.

(a) MOV AX,DS (b) MOV [DI],BX (c) MOV CX,[3000] (d) MOV [BP][SI]+12,AX (e) MOV BX,5678H (f) MOV AL,[BX] (g) MOV [BP+6],AL (h) MOV CX,DS (i) MOV DX,[BP+DI+4] (j) MOV AH,[BX+SI+50] (k) MOV BL,[SI]+10 (l) MOV AL,CH

### 4) CS=2000, DS=3000, SS=4000, SI=1000, DI=5000, BX=8060, BP=7000,

```
AX=FF25, CX=9187 ve DX=9912 olarak verilmiştir. Aşağıdaki işlemler için kullanılan
```

hafıza yerlerinin (memory location) fiziksel adreslerini ve bu adreslerde saklanan değerleri belirtiniz.

Başkent Üniversitesi Elektrik-Elektronik Mühendisliği Bölümü EEM 332 Mikroişlemciler Ödev 1/Grup 2 (a) MOV [SI],AL (b) MOV[SI+BX+8],AH (c) MOV [BX],AX (d) MOV [DI+6],BX (e) MOV [DI][BX]+28,CX (f) MOV[BP][SI]+10,DX (g) MOV [3600],AX (h) MOV[BX]+30,DX (i) MOV [BP]+200,AX (j) MOV [BP+SI+100],BX (k) MOV [SI]+50,AH (l) MOV [DI+BP+100],AX

### 5) Aşağıda verilen işlemler için CF, PF, AF, ZF ve SF durumlarını bulunuz.

a. MOV BL,9FH          b. MOV DX,10FFH           c. MOV AL,23H

```asm
ADD BL,61H             ADD DX,1                  ADD AL,97H
```

### 6) Aşağıda verilen komutlar işletildikten sonra komutlarda adı geçen registerların ve

CF, ZF, PF içeriklerini gösteriniz.

a.     MOV AX,6AB3

```asm
MOV BX,F198
ADD AL,BL
```

ADC AH,BH           ;add with carry

b.   DATA1 DB 4CH

```asm
DATA2 DB 6EH
DATA3 DB ?            ;data3 is empty and located in memory
MOV DH,DATA1          ;data1=4ch
SUB DH,DATA2          ;data2=6eh
JNC NEXT              ;JUMP if not carry
NOT DH                ;1’s complement
INC DH                ;increase one
NEXT:MOV DATA3,DH
```

### 7) Aşağıdaki sorularda istenilen işlemlerin gerçekleşmesi için gereken assembly

kodlarını yazınız. (AL=0FH ‘dir) a.     ROR komutunu kullanarak AL’nin içeriğini F0 yapınız. Bu durumda CF değeri ne olmalıdır? b.     STC ve SHR komutlarını kullanarak AL’nin içeriğini F0 yapınız. Bu durumda CF değeri ne olmalıdır? c.     AND komutunu kullanarak AL’nin içeriğini F0 yapınız. Bu durumda CF değeri ne olmalıdır? d.     SHL komutunu kullanarak AL’nin içeriğini F0 yapınız. Bu durumda CF değeri ne olmalıdır?

Başkent Üniversitesi Elektrik-Elektronik Mühendisliği Bölümü EEM 332 Mikroişlemciler Ödev 1/Grup 2

### 8) Aşağıda verilen komutlardan ilk üçü çalıştırıldıktan sonra Stack Segment ve ikinci

üçü çalıştırıldıktan sonra registerların değeri ne olur? (SP=1245, AX=8877, BX=6655 CX=4433, DX=2211)

### SS:1238

```asm
PUSH AX                SS:1239
PUSH CX                SS:1240
PUSH BX                                              AX
```

### SS:1241

### SS:1243                       BX

```asm
POP DX                 SS:1243                       CX
POP AX                 SS:1244                       DX
POP BX                                               SP
```

### SS:1245

### SP=?

## EEM332%20odev21

Başkent Üniversitesi Elektrik-Elektronik Mühendisliği Bölümü EEM 332 Mikroişlemciler Ödev 2/Grup 1

ÖNEMLİ BİLGİ:       -Ödevleri 13 Mayıs 2005 Cuma günü saat 17.00’ye kadar C302- B no’lu ofise teslim edebilirsiniz. -Ödevlerinizi, grubunuzu da belirterek, beyaz A4 kağıda hazırlayınız ve gerekiyorsa bir köşesinden zımbalayarak teslim ediniz (poşet dosya kabul edilmeyecektir). -Sadece adınızın bulunduğu gruba ait soruları cevaplayınız. Grup listesini web sayfasında bulabilirsiniz. -Kendi grubunuza ait olmayan soruları cevaplamanız durumunda ödev notunuz sıfır olarak değerlendirilecektir.

### 1) 16F877 PIC entegresinin ADC bölümünü kısaca özetleyiniz.

Çözünürlük=resolution?, Step size?, convertion time=?

### 2) I/O işlemlerinde interrupt (kesme) ve polling arasında avantaj ve dezavantajları

açısından karşılaştırma yapınız.

### 3) 8086 işlemci tabanlı sistemde 8255 ve 8253 entegreleri kullanılmıştır. 300 Hz’lik

kare dalga elde etmek için 8255 veya 8253 kullanarak iki ayrı program yazınız.

### 4) Verilen port devresinde; OUT ......., AL komutu için boşluğa gereken adresi

yazınız.

### 5) CPU10 slide 2’de verilen sıcaklığın durumuna göre LED kontrol programını PIC

16F877 ile çalışacak şekilde yeniden yazınız. Sıcaklık sayısal olarak Port C’den alınacaktır. Çıkış Led’leri Port B’ye bağlanacaktır.

Başkent Üniversitesi Elektrik-Elektronik Mühendisliği Bölümü EEM 332 Mikroişlemciler Ödev 2/Grup 1

### 6) Verilen port devresinde portların adresini yazınız ve hangi portun giriş ve

hangisinin çıkış olduğunu belirtiniz.

### 16) Port A’nın adresinin 68H olmasını için , 8255 için kullanılan I/O devresinde

NAND kullanarak 8 bitlik adres için decoding devresini oluşturunuz.

### 17) Verilen devrede her portun adresini bulunuz.

## EEM332%20odev22

Başkent Üniversitesi Elektrik-Elektronik Mühendisliği Bölümü EEM 332 Mikroişlemciler Ödev 2/Grup 2

ÖNEMLİ BİLGİ:       -Ödevleri 13 Mayıs 2005 Cuma günü saat 17.00’ye kadar C302- B no’lu ofise teslim edebilirsiniz. -Ödevlerinizi, grubunuzu da belirterek, beyaz A4 kağıda hazırlayınız ve gerekiyorsa bir köşesinden zımbalayarak teslim ediniz (poşet dosya kabul edilmeyecektir). -Sadece adınızın bulunduğu gruba ait soruları cevaplayınız. Grup listesini web sayfasında bulabilirsiniz. -Kendi grubunuza ait olmayan soruları cevaplamanız durumunda ödev notunuz sıfır olarak değerlendirilecektir.

### 1) 8086 işlemci tabanlı sistemde 8255 ve 8253 entegreleri kullanılmıştır. 250 Hz’lık

kare dalga elde etmek için 8255 veya 8253 kullanarak iki ayrı program yazınız.

### 2) Verilen port devresine bakarak boşluklara gereken adresi ve komutu yazınız.

### ……… AL, ……….

### 3) CPU10 slide 2’de verilen sıcaklığın durumuna göre LED kontrol programını PIC

16F84 ile çalışacak şekilde yeniden yazınız. Sıcaklık sayısal olarak Port B’den alınacaktır. Çıkış Led’leri Port A’ya bağlanacaktır.

### 4) Port A’nın adresinin 68H olmasını için , 8255 için kullanılan I/O devresinde NAND

kullanarak 8 bitlik adres için decoding devresini oluşturunuz.

Başkent Üniversitesi Elektrik-Elektronik Mühendisliği Bölümü EEM 332 Mikroişlemciler Ödev 2/Grup 2

### 5) Verilen port devresinde portların adresini yazınız ve hangi portun giriş ve

hangisinin çıkış olduğunu belirtiniz.

### 6) Verilen devrede her portun adresini bulunuz. Şekilde port A’dan alınan verinin

kendisi port B’ye ve tersi port C’ye gönderilecektir.

### 7) 16F877 PIC entegresinin ADC bölümünü kısaca özetleyiniz.

Çözünürlük=resolution?, Step size?, Convertion time=?

### 8) I/O işlemlerinde interrupt (kesme) ve polling arasında avantaj ve dezavantajları

açısından karşılaştırma yapınız.

## q

Başkent Üniversitesi Elektrik-Elektronik Mühendisliği Bölümü EEM 332 – Mikroişlemciler

1.1) Aşağıdaki soruları yanıtlayınız.

a. Bir mikroişlemcinin hızını neler belirler?

b. ADD AX,BX ile ADD AX, [BX] arasındaki farkı yazınız.

c. DS=5010 ve PA(fiziksel adres)=51950 ise offset değeri nedir?

1.2) Belirlenen segment registerler hangi registerleri offset register olarak kullanır?

Segmet register              CS              DS                  ES              SS ..........      .............       ............   .............

1.3) Aşağıdaki registerlerden High ve Low olarak kullanılabilenleri işaretleyiniz.

a) CS           b) AX           c) DS           d) SS              e) BX f) DX           g) CX           h) SI              i) DI

1.4) Verilen işlemlerin karşısına doğru (D) veya yanlış (Y) olarak işaretleyiniz.

```asm
MOV BL,AX
MOV DS,3456H
MOV [3456],[5634]
MOV AX,CS
ADD AX,[BX]+[2345]
MOV CL,5643H
```

Başkent Üniversitesi Elektrik-Elektronik Mühendisliği Bölümü EEM 332 – Mikroişlemciler

2.1) Aşağıda verilen komutlar işletildikten sonra komutlarda adı geçen registerların ve CF, ZF, PF içeriklerini gösteriniz.

a.     MOV AX,6AB3

```asm
MOV BX,98F1
ADD AL,BL
```

ADC AH,BH           ;add with carry

b.   DATA1 DB 4CH

```asm
DATA2 DB 6EH
DATA3 DB ?            ;data3 is empty and located in memory
MOV DH,DATA1          ;data1=4ch
SUB DH,DATA2          ;data2=6eh
JNC NEXT              ;JUMP if not carry
NOT DH                ;1’s complement
INC DH                ;increase one
NEXT:MOV DATA3,DH
```

2.2) -2 ve -7 sayılarını toplayan ve sonucu CL registerina yazan kodu tamamlayınız. Kodun çalışması sonunda CL registerinin ve CF, ZF, PF, AF, SF durumunu gösteriniz.

```asm
MOV AL,___
MOV CL,___
ADD ___,___
```

2.3) CPU tabanlı sistemin belleğinden bir bölüm verilmiştir. Buna göre her işlemin sonucunda olan değişiklikler nelerdir? (DS=0040, SI= 0090h, BP = 0002h) adres data a) MOV AX,[SI] 00490h 35 b) MOV AX,[SI+1] 00491h 78 00492h B2            c) MOV AX,[SI][BP] 00493h 9C            d) MOV [SI-BP][3],AX 00494h 0A            e) MOV [94],AX

2.4) Aşağıdaki sorularda istenilen işlemlerin gerçekleşmesi için gereken assembly kodlarını yazınız. (AL=0FH ‘dir) a.     AND komutunu kullanarak AL’nin içeriğini F0 yapınız. Bu durumda CF değeri ne olmalıdır? b.     SHL komutunu kullanarak AL’nin içeriğini F0 yapınız. Bu durumda CF değeri ne olmalıdır? c.     ROR komutunu kullanarak AL’nin içeriğini F0 yapınız. Bu durumda CF değeri ne olmalıdır? d.     STC ve SHR komutlarını kullanarak AL’nin içeriğini F0 yapınız. Bu durumda CF değeri ne olmalıdır?

Başkent Üniversitesi Elektrik-Elektronik Mühendisliği Bölümü EEM 332 – Mikroişlemciler

2.5) Aşağıda verilen komutlardan ilk üçü çalıştırıldıktan sonra Stack Segment ve ikinci üçü çalıştırıldıktan sonra registerların değeri ne olur? (SP=1245, AX=1122, BX=3344, CX=5566, DX=7788)

### SS:123E

```asm
PUSH AX                SS:123F                         AX
PUSH CX                SS:1240                         BX
PUSH BX                SS:1241                         CX
```

### SS:1242                         DX

```asm
POP DX                 SS:1243                         SP
POP AX                 SS:1244
POP BX                 SS:1245
```

### SP=?

## ödev1

Başkent Üniversitesi Elektrik – Elektronik Mühendisliği Bölümü EEm332 Mikroişlemciler Ödev 1 / Grup 2

### 1)

a. KODLANIR. b. KODLANIR. c. KODLANIR. d. 16bit, 8 bit’e aktarılamaz. e. 8 bit, 16 bit’e partition yapılamaz. f. Overflow. 20 bit, 16bit’e aktarılamaz. g. Doğrudan deger atanamaz. h. Overflow. 12 bit, 8 bit’e aktarılamaz. i. Doğrudan değer atanamaz. j. 8 bit, 16 bit’e partition yapılamaz. k. KODLANIR. l. KODLANIR.

### 2)

a. BX->DS b. SI->DS,ES c. IP->CS d. DI->DS e. SP->SS f. BP->DS

### 3)

a. direct addressing b. c. d. base indexed direct addressing e. implied addressing f. g. base indexed direct addressing h. direct addressing i. base indexed direct addressing j. base indexed direct addressing k. l. direct addressing

*Not: 2004 ödev föyünde “29 Mart 2004 Salı” yazmaktadır; 29 Mart 2004 Pazartesi günüdür. Tarih ifadesi kaynakta olduğu gibi bırakılmıştır.*
