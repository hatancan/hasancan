---
baslik: EEM332 Mikroişlemciler: 2009 Vize ve Final Soruları
ozet: 2009 sınav fotoğraflarından 8086 komutları, bayraklar, adres çözümleme, 8255, ADC ve PIC soruları.
---

Başkent Üniversitesi EEM332 Mikroişlemciler ders arşivindeki bu içerik, fotoğraflanmış sayfalardan metne aktarıldı. 2009 sınav fotoğraflarından 8086 komutları, bayraklar, adres çözümleme, 8255, ADC ve PIC soruları. Öğrenci adları ve numaraları çıkarıldı. Fotoğraflar özel arşivde tutulur; bu yazının indirme dosyası yoktur.

## Vize: AX’i sıfırlama

Dört ayrı yöntem istenmiştir:

```asm
MOV AX,00H
AND AX,00H
SUB AX,AX
XOR AX,AX
```

## ADD DL,CH ve bayraklar

| Başlangıç DL | CH | Son DL | OF | SF | CF |
| --- | --- | --- | --- | --- | --- |
| 80H | FEH | 7EH | 1 | 0 | 1 |
| FEH | FBH | F9H | 0 | 1 | 1 |

*Not: İkinci satırdaki basılı CF=0 cevabı, fotoğrafta kırmızı kalemle 1 olarak düzeltilmiştir. FEH+FBH=1F9H olduğundan elde vardır.*

## Mantıksal işlemler

```asm
MOV BH,0A8H
AND BH,3DH
OR BH,0C0H
XOR BH,05H
```

Ara değerler 28H, E8H ve EDH; son BH=EDH’dir.

## C döngüsünün assembly karşılığı

Sorudaki değişkenler a=16, b=2, c=0; koşul c<300’dür. Her turda a=a*b ve c=c+1 uygulanır. Kaynağın cevabı:

```asm
MOV AX,16
MOV BL,2
MOV CX,0
DONGU: MUL BL
       INC CX
       CMP CX,300
       JL DONGU
```

*Not: MUL BL yalnız AL ile BL’yi çarpar ve AX’e yazar. Bu kod, sınırsız duyarlıkta 16×2³⁰⁰ hesabını temsil etmez; yazmaç genişliği ve taşma dikkate alınmalıdır.*

## AL=k için polinom sorusu

```asm
MOV DL,AL
MUL DL
MOV CX,5
MUL CX
XCHG DX,AX
MOV AL,3
MUL DL
SUB DX,AX
XCHG DX,AX
SUB AX,CX
```

Cevap anahtarında 5k²−3k−5 yazmaktadır.

*Not: Kaynak kodda MUL CX, DX:AX çiftini değiştirir; ardından XCHG de DX ve AX’i değiştirir. Bu nedenle DL’nin ilk k değerini koruduğu varsayımı geçerli değildir. Anahtardaki polinom, listelenen komutların genel sonucu olarak doğrulanamaz.*

## DEC ve bayrak tablosu

AL=02H’den başlayıp üç kez DEC AL uygulanır:

| Adım | AL | ZF | PF | SF |
| --- | --- | --- | --- | --- |
| İlk | 01H | 0 | 0 | 0 |
| İkinci | 00H | 1 | 1 | 0 |
| Üçüncü | FFH | 0 | 1 | 1 |

## Bellek dizisinden beş çıkarma

Soru DS:2000–DS:2008 aralığındaki baytların her birinden 5 çıkarılmasını ister. Kaynağın cevabı:

```asm
MOV CX,8
MOV DI,2000H
TOP: SUB [DI],5
     INC DI
     LOOP TOP
```

*Not: İki uç dahil 2000H–2008H aralığı dokuz bayttır; CX=8 yalnız ilk sekiz baytı işler. Bellek işleneninin genişliği de assembler için BYTE PTR ile belirtilmelidir.*

## Adres çözümleme

74LS138 kod çözücüye A14, A15 ve A16 adres bitleri bağlanmıştır. ROM’un A0–A13 uçları 2¹⁴=16384 bayt, yani 16 KiB kapasiteyi seçer. Fotoğraftaki çözümde Y4 için F0000H–F3FFFH, Y6 için F8000H–FBFFFH aralıkları verilmiştir. Üst adres bitleri etkinleştirme girişlerini belirler.

## Dizinin kümülatif toplamı

```asm
DELTA DB 1,2,4,2,6
MOV AX,0
MOV SI,OFFSET DELTA
MOV CX,5
DONGU: ADD AX,[SI]
       MOV [SI],AX
       INC SI
       LOOP DONGU
MOV BX,AX
MOV CX,5
DIV CL
INT 03
```

El yazısı anahtar diziyi 1,3,7,9,15; AX’i 3, BX’i 15 ve DX’i 0 olarak vermektedir.

*Not: DELTA bayt dizisidir, fakat ADD AX,[SI] ve MOV [SI],AX word genişliğinde çalışır. Birer bayt ilerlemek üst üste binen word erişimleri oluşturur. DIV CL’nin bölüneni AX, sonuçları AL ve AH’dir; DX’i sıfırlamaz. Anahtar amaçlanan bayt toplamını anlatır, listelenen kodun gerçek yürütümünü değil.*

## CMP sonuçları

Başlangıçta AX=8001H, SI=0200H, DI=0300H; DS:0100=F0H, DS:0200=F0H, DS:0201=01H, DS:0300=34H ve DS:0301=12H verilmiştir.

| Komut | ZF | SF | CF | AF | OF | PF |
| --- | --- | --- | --- | --- | --- | --- |
| CMP [0100],AL | 0 | 1 | 0 | 1 | 0 | 0 |
| CMP AX,[SI] | 0 | 0 | 0 | 1 | 1 | 1 |
| CMP WORD PTR [DI],1234H | 1 | 0 | 0 | 0 | 0 | 1 |

## Final: ADC ve aktarım hızı

Fotoğraftaki örnekte 10 V tam ölçek ve 16 bit dönüşüm kullanılır. 10/2¹⁶≈0,0001526 V, yani yaklaşık 152,6 µV/adım bulunur. 4 V için ideal oransal kod yaklaşık 26214’tür. Ayrı aktarım sorusunda 1 kHz hızla her seferinde bir bayt gönderildiğinde bir saatte 3.600.000 bayt aktarılır.

*Not: ADC sorusunun devamındaki süre ifadesi fotoğrafta kesin okunamadığından aktarılmadı. Uç nokta tanımına göre çözünürlük hesabında 2ⁿ veya 2ⁿ−1 kullanımı değişebilir; burada kâğıttaki 2¹⁶ kabulü korunmuştur.*

## CALL, INT, RET ve IRET

CALL dönüş adresini yığında saklar. Yakın çağrıda IP, uzak çağrıda CS ve IP saklanır. INT, FLAGS ile CS ve IP’yi saklayarak kesme yordamına geçer. RET yordam dönüşü, IRET ise IP, CS ve FLAGS’in geri yüklenmesi için kullanılır.

## Bit sayma ve sıfırlama

DL=E0H için üç adet 1 biti vardır; kaynakta bu sayı başlangıç değerine eklenerek E3H sonucu bulunmuştur. Başka bir döngü DS:2000’den başlayarak CX=8 ile sekiz baytı sıfırlar; AL’ye okunan değer XOR AL,AL ile sıfırlanıp geri yazılır.

## 8255 ile port aktarımı

A portu giriş, B portu çıkış, C’nin üst yarısı giriş, alt yarısı çıkış seçilmiştir. Port adresleri A=7CH, B=7DH, C=7EH ve kontrol=7FH; mod 0 kontrol sözcüğü 98H’dir. A’dan okunan veri B’ye, C’nin üst dört biti sağa dört konum döndürülerek alt dört çıkışa aktarılır.

```asm
MOV AL,98H
OUT 7FH,AL
TEKRAR: IN AL,7CH
        OUT 7DH,AL
        IN AL,7EH
        MOV CL,4
        AND AL,0F0H
        ROR AL,CL
        OUT 7EH,AL
        JMP TEKRAR
```

*Not: Kaynaktaki son LOOP komutu kırmızı kalemle JMP olarak değiştirilmiştir; burada düzeltilmiş okuma gösterildi.*

## Dizi içinde 1,2 örüntüsü

Veri dizisi 5,7,9,1,2,6,5,0,1,2,1,1,1,2’dir. Ardışık 1,2 çifti üç yerde bulunur. Çözüm yan yana iki elemanı karşılaştırıp sayacı artırır.

*Not: Fotoğraftaki taslakta DX bellek adresleyicisi olarak kullanılmıştır. 8086’nın 16 bit adresleme biçiminde [DX] geçerli değildir; kaynak taslağın bu sınırlaması korunarak belirtilmiştir.*

## Porttan beş bayt okuma

```asm
MOV SI,0
MOV CX,0005H
KAL: IN AL,80H
     MOV [SI+2000H],AL
     INC SI
     LOOP KAL
```

## PIC LED uygulaması

PORTB çıkış, PORTA giriş olarak ayarlanır. PORTB’ye 01H yazılır ve taşıma temizlenir. Gecikme alt programından sonra RLF ile yanan LED sola ilerletilir. Taşıma oluşunca PORTA’nın 1. bitindeki buton beklenir; RRF ile hareket ters yönde tekrarlanır. LIST hedef işlemciyi, INCLUDE yazmaç tanımlarını; TRIS yazmaçları port yönlerini belirler.

*Not: GOTO ile aynı etikete dönmek programı sonlandırmaz; sonsuz döngü oluşturur. Kaynaktaki “program sonu” açıklaması bu anlamda okunmalıdır.*
