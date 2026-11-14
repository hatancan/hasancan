---
baslik: EEM442 Haberleşme II: Kısa Sınavlar (Darbe Modülasyonları, PCM, Hat Kodları, TDM-PCM, BPSK, π/4-QPSK) El Yazısı Çözümleri
ozet: EEM442 Haberleşme II dersi 2017 bahar kısa sınavlarının (Quiz 1-4) el yazısı çözümlerinin metne aktarımı: PAM/PDM/PPM çizim ve güç hesabı, PCM nicemleme, hat kodları, TDM-PCM bant genişliği, BPSK hata olasılığı ve π/4-QPSK.
---

2017 bahar yarıyılında **EEM442 Haberleşme II** dersinde yapılan kısa sınavların (Quiz 1–4) sınav sonrası yazdığım el yazısı çözümleri, 8 Haziran 2017'de fotoğraflandı. Aşağıda sorular ve çözüm adımları metne aktarılmıştır; fotoğraflar yayımlanmamıştır. Soru metinleri çözümlerden ve not başlıklarından çıkarıldığından kısa ve çıkarımsaldır; el yazısı okunuşunda küçük hatalar olabilir.

## Quiz 1: darbe modülasyonları (PAM, PDM, PPM)

**Soru:** x(t) = 2·cos(2πt) V mesaj işareti için
- a) Nyquist hızı (N.H.),
- b) Örnekleme hızı 10 Hz, darbe süresi τ = 20 ms, A = 1 V (0,1 s aralıklarla örnekleme) olacak şekilde PAM çiziniz,
- c) PAM gücü,
- d) PDM/PWM'yi aynı örnekleme hızı için çiziniz (τ₀ = 50 ms, t₀ = 15 ms, A = 1),
- e) PDM/PWM gücü,
- f) PPM'yi 0–0,1 s aralığında çiziniz,
- g) PPM gücü.

**Çözüm.**
- a) f_m = 1 Hz ⇒ **N.H. = 2·f_m = 2 Hz**.
- b) S.N.H. (seçilen örnekleme hızı) = 10 Hz, T_s = 0,1 s; örnek değerleri t = 0; 0,1; 0,2; 0,3; 0,4; 0,5 … için 2; 1,62; 0,61; −0,61; −1,62; −2; … (0,02 s genişlikli darbeler 0, 0,1, 0,2, … anlarında başlar).
- c) PAM gücü P = (A²·τ/T_s)·⟨x²(t)⟩, ⟨x²⟩ = 2²/2 = 2 ⇒ P = (1·0,02/0,1)·2 = **0,4 W**.
- d) τ = τ₀ + t₀·x(t) = 50 + 15·x(t) ms: x = 2 → τ = 80 ms; x = 1,62 → τ = 74,3 ms; x = 0,61 → τ = 59,15 ms. Çizimde darbelerin başlangıç/bitiş zamanları bu genişliklere göre 0,08; 0,1; 0,174; 0,2; 0,259 s gibi işaretlenmiştir (el yazısı tam okunmadı).
- e) ⟨τ⟩ = τ₀ + t₀·⟨x(t)⟩ = 50 ms (⟨x⟩ = 0); **P = A²·⟨τ⟩/T_s = 1·50 ms/100 ms = 0,5 W**.
- f) PPM: darbe konumu (gecikme) mesaja göre değişir: d₁, d₂ gecikmeleri; sabit τ = 20 ms genişliğinde darbeler.
- g) d = τ(t); **P = A²·τ/T_s = 1²·20/100 = 0,2 W**.

## Quiz 2: PCM

**Soru:** x(t) = 3·cos(πt) + 5·cos(5πt) V işareti için Nyquist hızında örnekleme ve 4 bitlik (Q = 16) nicemleme; PCM kodunu bulun.

**Çözüm.** En yüksek frekans 2,5 Hz ⇒ N.H. = 5 Hz; çizimde 2·N.H. = 10 Hz ve T_s = 0,1 s kullanılmıştır. Q = 16, n = 4 bit, A_max = 3 + 5 = 8 V, A_min = −8 V ⇒ adım a = (A_max − A_min)/Q = 16/16 = 1 V. Her örnek n bit olduğundan PCM bit hızı r_b = n·f_s; bit süresi T_b = T_s/n.

Örnek değerleri: t = 0,1 → 2,85 (+0); 0,2 → 2,42 − 5 = −2,58; 0,3 → 1,76; 0,4 → 5,43 (el yazısıyla); 0,5 → 0; 0,6 → −5,93. Her örnek aşağı yuvarlanarak seviyelendirilmiş ve 0000 … 1111 kod ızgarasında (−8 V = 0000, 0 V = 1000, +8 V = 1111) kodlanmıştır; yazılan PCM akışı: **1010 0101 1001 1101 0111 0010**.

*Not: t = 0,4 s'de 3cos(0,4π) + 5cos(2π) = 0,93 + 5 = 5,93 V olmalıdır; kâğıtta 5,43 yazılmıştır (kod 1101'de seviye 5 olduğundan nicemleme sonucu aynı kalır).*

## Hat kodları ve TDM

**Hat kodu çizimleri.** Bir bit dizisi (1 0 1 0 0 1 0 1 1 0 0 1 1 1 0 1 0 1 1 0 0 1 0 …) üzerinde **bipolar RZ** çizilmiş (1 → bit süresinin yarısında dönüşümlü +/− darbe, 0 → darbe yok; "yarım bit pozitif/negatif dönüşümlü"). Ardından 1, 0, 1, 1 dizisi için tek tek şunlar çizilmiştir:
- **Unipolar RZ:** yalnızca pozitif, yarım bitlik darbe;
- **Polar NRZ:** tam bit süresi; 1 → pozitif, 0 → negatif;
- **Polar RZ:** yarım bit; 1 pozitif, 0 negatif;
- **Bipolar NRZ:** tam bit süresi; 1'ler dönüşümlü pozitif ve negatif, 0 → sıfır düzey;
- **Bipolar RZ (AMI):** yarım bit; 1'ler dönüşümlü pozitif/negatif;
- **Manchester:** bit süresi ikiye bölünür; 1 → ilk yarı yüksek, ikinci yarı alçak; 0 → ilk yarı alçak, ikinci yarı yüksek.

**TDM sorusu.** Dört mesaj işareti (10, 15, 20 ve 30 kHz bant genişliklerinde) bir komütatörle çoklanır, ardından PCM kodlayıcı (Q = 32), kanal, PCM kod çözücü, dekomütatör ve her kolda AGF ile m₁(t) … m₄(t) elde edilir. Çözüm: f_m (en büyük sinyal) = 30 kHz ⇒ f_s ≥ 2·f_m ⇒ **f_s = 60 kHz** (her kanal için); 4 kanal × 60 kHz = **240 kHz** örnek/s; Q = 32 = 2ⁿ ⇒ n = 5 bit ⇒ bit hızı 240k × 5 = **1,2 Mbps**.

## Quiz 3: TDM-PCM sistemi ve kanal bant genişliği

**Soru:** Şekildeki dört kanal (45 kHz, 15 kHz, 15 kHz ve 15 kHz bant genişlikli) TDM-PCM haberleşme sistemiyle iletilmektedir (kuantalayıcı ve kodlayıcı Q = 2ⁿ, n = 6). Kanal bant genişliği 648 kHz olduğuna göre, yükseltilmiş kosinüs filtresi için yuvarlanma (roll-off) faktörü α'yı bulunuz.

**Çözüm.** 45 kHz'lik kanal 3 adet 15 kHz'lik kanal sayılır ⇒ toplam 6 kanal. Her biri için N.H. = 2·15 kHz = 30 kHz. Örnek hızı r_s = (kanal sayısı) × N.H. = 6 × 30 kHz = 180 kÖrnek/s; bit hızı r_b = n·r_s = 6 × 180 = **1080 kbps**. B.G. = (1 + α)/(2T_b) = (1 + α)·r_b/2 = 648 kHz ⇒ **α = 0,2**.

## Quiz 4: BPSK ve π/4-QPSK

**Soru 1 (BPSK).** Güç spektral yoğunluğu N₀ = 10⁻¹¹ olan beyaz Gauss gürültüsü etkisindeki BPSK işareti (s₁(t) = A·cos(ω₀t), s₂(t) = −A·cos(ω₀t), A = 10 mV) kuramsal olarak uyumlu algılanıyor. Hata olasılığının 8·10⁻⁴'ten küçük olması için **bit hızı en fazla kaç olabilir?**

**Çözüm.** P_e = Q(√(2E_b/N₀)), E_b = A²·T_b/2 ⇒ P_e = Q(√(A²T_b/N₀)) ≤ 8·10⁻⁴. A = 10⁻² V, N₀ = 10⁻¹¹ ⇒ √(10⁻⁴·T_b/10⁻¹¹) = √(10⁷·T_b); Q(3,16) ≈ 8·10⁻⁴ olduğundan 10⁷·T_b ≥ 10 (kâğıtta "T·10⁷ ≤ 3,16" yazılıp, nihai cevap olarak **r_b ≈ 1 Mbps** bulunmuştur).

*Not: Q(x) ≤ 8·10⁻⁴ için x ≥ 3,16 olmalıdır; bu √(10⁷·T_b) ≥ 3,16 ⇒ T_b ≥ 1 µs ⇒ r_b ≤ 1 Mbps verir. Yani kâğıttaki "T ≤ 3,16·10⁻⁷" ara satırındaki eşitsizlik yönü/ölçeği tutarsızdır, fakat sonuç (1 Mbps) doğrudur.*

**Soru 2 (π/4-QPSK, koherent).**
- a) Modülasyon işaretini veren blok şemayı çiziniz,
- b) ortonormal temel fonksiyonları ve genlik çarpanlarını bulunuz,
- c) konstelasyon grafiğini çiziniz,
- d) 10 11 00 10 10 00 10 01 temel bant verisi için sembol faz değişimlerini ve gönderilen sembolleri belirtiniz.

**Çözüm.** b) φ₁(t) = √(2/T) cos(ω_c t), φ₂(t) = √(2/T) sin(ω_c t) (el yazısında √(2/T_b)); genlik çarpanları (a, b) ∈ {(√E_b, 0), (0, √E_b), (−√E_b, 0), (0, −√E_b)} ve π/4 döndürülmüş kümesi {(±√(E_b/2), ±√(E_b/2))} (sekiz noktalı konstelasyon, iki QPSK kümesi arasında dönüşümlü). a) Blok şema: temel bant → iki seri-paralel (S/P) dönüştürücü (çift ve tek bit kolları) → I ve Q kolları için ±√E_b seviyeleri → çarpıcılar (cos ve sin taşıyıcılar) → toplayıcı → x(t); iki sembol kümesi arasında seçim bir anahtarla (2T_b) yapılır. c) Konstelasyon: eksen üzerinde dört nokta (kümelerden biri) ve köşegenlerde dört nokta (π/4 kaymış küme); √E_b yarıçaplı. d) Bit çiftleri sırayla I ve Q seviyelerine, tek ve çift semboller için farklı kümelere haritalanır; önceki sembole göre faz değişimleri **135°, 135°, 135°, −45°, −45°, 45°, −135°** olarak yazılmıştır (aralarındaki yönün saat yönünün tersi olduğu belirtilmiştir).
