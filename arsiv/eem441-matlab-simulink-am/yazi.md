---
baslik: EEM441 Haberleşme I: MATLAB ve Simulink AM Çalışması
ozet: Kare dalganın AM modülasyonu için MATLAB betiği ve mesaj–taşıyıcı çarpımını kuran Simulink modeli.
---

21 Kasım 2011 tarihli Simulink modeli ile aynı AM hazırlığı klasöründeki MATLAB betiği birlikte arşivlendi. Bilgisayar/kullanıcı meta verileri temizlenmiş kaynak dosyalar ZIP olarak indirilebilir. Kodlar çalıştırılmadı.

## MATLAB betiği

```matlab
Fs = 1e7; % Sampling rate is 8e6 samples per second.
Fc = 1000000; % Carrier frequency in Hz
t = [0:.1*Fs]'/Fs; % Sampling times for .1 second
t = [-10:0.2:10];
duty = 50;
x = square(t,duty); % Representation of the signal
plot(x)
y = ammod(x,Fc,Fs); % Modulate x to produce y.
figure;
subplot(2,1,1); plot(t,x); % Plot x on top.
subplot(2,1,2); plot(t,y)% Plot y below.
```

*Not: Kaynakta örnekleme hızı 10 milyon, yorumda 8 milyon örnek/saniye yazıyor. Sayılar yalnız bilimsel gösterime çevrildi; bu uyuşmazlık korunuyor. İlk zaman vektörü sonraki `t` atamasıyla eziliyor. `square(t,duty)` argümanı radyandır; bu vektörün adımı ile `ammod` için verilen Fs aynı örnekleme düzenini tanımlamıyor. Dolayısıyla çizim ekseni ve modülasyonun zaman tabanı uyumlu kabul edilmemelidir.*

## Simulink modeli

Model adı `eem441`, sürümü 7.0, başlangıç zamanı 0 ve bitiş zamanı 10'dur. Mesaj üreteci frekans alanı 167, taşıyıcı üreteci frekans alanı 100, sabit blok değeri 0'dır. Mesaj ile sabit toplanıp taşıyıcıyla çarpılır. Mesaj, taşıyıcı ve çıkış ayrı Scope bloklarına gider. Product bloğunun örnekleme zamanı 0,001 olarak kaydedilmiş.

Bağlantıların metin karşılığı:

```
Message ──┬── Message Scope
          └── Sum ── Product ── Scope
Constant ────┘         │
carrier ──┬────────────┘
          └── Carrier Scope
```

Sabitin sıfır olması, mesajın üzerine DC taşıyıcı bileşeni eklenmediğini gösterir. Dosyada yazılı frekans alanları burada aynen aktarılmıştır; birim ayarı görülmeden bunlar otomatik olarak Hz kabul edilmemiştir.
