---
baslik: EEM211 Sayısal Mantık Tasarımı: 2006–2007 Laboratuvar Raporları ve Verilog Kodları (Deney 4–9, Yedi Parçalı Gösterge Sürücüsü)
ozet: EEM211 laboratuvarı için arkadaşların hazırladığı Deney 4–9 raporları ve Verilog kodları: davranışsal ve yapısal 4 bitlik toplayıcı, kapı gecikmeli tam toplayıcı ve carry-lookahead, hatalı kablonun bulunması, MUX ve kod çözücüyle tasarım, D flip-flop ve JK sayıcılar, dört haneli yedi parçalı gösterge sürücüsü (SSdriver) ile 0–9 ve 0–99 sayıcılar.
---

Bu yazı, EEM211 Sayısal Mantık Tasarımı dersinin klasöründe "ferhat_notlari" adıyla toplanmış, **2006 ve 2007 güz dönemlerinde** laboratuvar deneyleri için arkadaşların hazırladığı raporları ve Verilog kaynak kodlarını bir araya getiriyor. Raporlardaki öğrenci adları ve numaraları kapatıldı, dosya adlarındaki numaralar çıkarıldı (raporlar A, B, C, D harfleriyle dört farklı kişiye ait olarak işaretlendi). Klasördeki Xilinx ara dosyaları (derleme çıktıları, benzetim veritabanları) alınmadı. Maskelenmiş raporlar ve Verilog dosyaları yazının sonunda ZIP olarak indirilebilir.

## Deney 4: 4 bitlik toplayıcı (Verilog)

Rapor A'da iki çözüm var. İkinci soruda tam toplayıcı davranışsal olarak, minterimlerle yazılmış:

```verilog
module fadder(s,co,c,a,b);
output s,co;
input c,a,b;
assign co = (~c & a & b) | (c & ~a & b) | (c & a & ~b) | (a & b & c);
assign s = (~c & ~a & b) | (~c & a & ~b) | (c & ~a & ~b) | (c & a & b);
endmodule
```

Üçüncü soruda AND, OR ve tümleyici kapıları ayrı modüller (`andgate`, `orgate`, `invgate`) olarak tanımlanıp tam toplayıcı (`fadderStr`) bu kapılarla yapısal olarak yeniden kurulmuş; iki çözümde de dört tam toplayıcı zincirlenerek `fourbitadder1` ve `fourbitadder2` oluşturulmuş.

## Deney 6: Kapı gecikmeli toplayıcılar

Rapor B'de tam toplayıcı kapı gecikmeleriyle (XOR 17, AND 14, OR 15 birim) tanımlanıyor:

```verilog
module tamtoplayici(s,cout,a,b,cin);
input a,b,cin;
output s,cout;
wire w1,w2,w3;
xor #(17)
  x1(w1,a,b),
  x2(s,cin,w1);
and #(14)
  a1(w2,a,b),
  a2(w3,w1,cin);
or #(15) (cout,w3,w2);
endmodule
```

Bununla 4 bitlik dalgacık eldeli toplayıcı ve `PGgen`, `carrygen` modülleriyle 4 bitlik **carry-lookahead** toplayıcı (`fourbitscarrylookahead`) kurulmuş.

## Deney 7: Hatalı devre, MUX ve kod çözücü

İki rapor (B ve C) aynı soruları cevaplıyor:

1. Verilen devredeki yanlış F fonksiyonu Karnaugh haritasında sadeleştirildiğinde, doğru F'deki **c'd** teriminin eksik olduğu görülüyor; yani d'yi c'd terimini üreten AND kapısına götüren kablo hatalı (temas etmiyor).
1. F fonksiyonu kanonik biçimde yazılıp dört girişli, tek çıkışlı devre en fazla üç adet 2 girişli MUX ile tasarlanmış.
1. 2x4 kod çözücü ve 4x1 MUX ile, iki bitlik ab ve cd sayıları eşitse 1 veren devre: F = a'b'c'd' + a'bc'd + ab'cd' + abcd. Kanonik formda yazılıp Karnaugh haritasına yerleştirilerek eşitlik kontrolü yapılıyor.

## Deney 8: D flip-flop ve JK sayıcılar

Üç açıklama belgesinde aynı sorular cevaplanıyor:

1. FD bloğu yükselen kenarda tetiklenen bir D flip-flop; çıkışın önündeki tümleyici yüzünden çıkış girişin tersi olur ve her saat darbesinde değişir (frekans yarıya iner).
1. Dört JK flip-floplu devre, her flip-flopun çıkışı bir sonrakinin saat girişine bağlı asenkron bir **geri sayıcıdır**: 1111'den 0000'a azalır.
1. Bütün saat girişlerine tümleyici konunca flip-floplar düşen kenarda tetiklenir ve devre 0000'dan **ileri sayar**.
1. Şekil 3'teki sayıcının ilk flip-flopu girişin tersini çıkışa ilettiği için, Şekil 1'deki işlem bu devreyle de yapılabilir (en düşük anlamlı bit alınarak).

*Not: Açıklamalardan birinde geri sayıcının ikinci durumu "0111, onluk karşılığı 14" diye yazılmış; bitler Q0'dan Q3'e doğru (ters sırada) okunmuş. Q3Q2Q1Q0 sırasıyla bu durum 1110 = 14'tür.*

## Deney 9: Mandallar, flip-floplar ve yedi parçalı gösterge sürücüsü

Bu deneyde dört haneli yedi parçalı gösterge sürücüsü (`SSdriver`) kullanılıyor. Rapor D'ye (19 Aralık 2006) göre modülün görevi, girişteki dört adet 4 bitlik bilgiyi (S1–S4) dört göstergeye sırayla aktarmak: önce S1'in karşılığı SS çıkışına verilip birinci göstergenin ortak anodu (AN) sürülür, sonra S2, S3 ve S4 için aynısı yapılır. Bu tarama saniyede yüzlerce kez tekrarlandığı için göz yanıp sönmeyi fark etmez ve göstergelerde sabit rakamlar görülür.

```verilog
module clkdiv(clk,mclk);
output clk;
input mclk;
reg [15:0] cnt;
assign clk=cnt[15];
initial cnt=0; // Don't forget!! Otherwise simulator does generate X only
always @(posedge mclk)
begin
cnt = cnt+1;
end
endmodule

module SSdriver(SS,AN,mclk,S1,S2,S3,S4);
input mclk;
input [3:0] S1,S2,S3,S4;
output reg [7:0] SS;
output reg [3:0] AN;
wire [7:0] w1,w2,w3,w4;
wire clk;
wire [3:0] w5;
reg [1:0] cnt;
clkdiv cdiv(clk,mclk);
decoder d1(w1,S1);
decoder d2(w2,S2);
decoder d3(w3,S3);
decoder d4(w4,S4);
anode_decoder d5(w5,cnt);
initial cnt=0;
always @(posedge clk)
begin
cnt=cnt+1;
end
always @(cnt)
begin
AN<=w5;
case (cnt)
2'b00 : SS<=w1;
2'b01 : SS<=w2;
2'b10 : SS<=w3;
2'b11 : SS<=w4;
endcase
end
endmodule
```

`decoder` modülü 0–9 rakamlarını 8 bitlik segment koduna (ör. 0 → 10000001, 1 → 10011111; etkin düşük) çeviriyor, `anode_decoder` ise 2 bitlik sayaca göre dört anottan birini 0 yapıyor (1110, 1101, 1011, 0111). `clkdiv`, kartın saatini 2¹⁶'ya bölerek tarama saatini üretiyor.

Raporlarda bu sürücüyle kurulan sayıcılar anlatılıyor:

- **0–9 sayıcı:** 8 bitlik ikili sayıcının çıkışına bağlanan AND kapısı, çıkış 1010 (10) olduğunda clr girişini 1 yapıp sayıcıyı sıfırlıyor; böylece sayıcı yalnızca 9'a kadar sayıyor ve çıkış göstergeye aktarılıyor.
- clr girişi sürekli 1'e bağlanırsa çıkışlar sıfırlanır ve göstergede hep 0 görülür.
- **0–99 sayıcı:** her basamak ayrı bir sayıcıyla saydırılıyor; birinci sayıcıyı 10'da sıfırlayan AND kapısının çıkışı ikinci sayıcının saat girişine bağlanıyor. Böylece birler basamağı her 9'dan 0'a döndüğünde onlar basamağı bir artıyor ve devre 99'a kadar sayıyor.
