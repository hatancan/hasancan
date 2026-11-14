---
baslik: EEM312 Sayısal Elektronik: CMOS Eşik Gerilimi, Gürültü ve Tersleyici Zinciri, El Yazısı Notlar
ozet: İdeal tersleyici, fan-out, CMOS anahtarlama eşiğinin türetilmesi, eklem sığası hesabı ve tersleyici zincirinde en uygun kademe sayısı. El yazısı notların formül ve sonuçları.
---

Bu yazı, **EEM312 Sayısal Elektronik** klasöründeki bir arkadaşın CMOS tersleyiciler üzerine hazırladığı çalışma sayfalarını içeriyor. Fotoğraflanmış sayfalardan metne aktarıldı; kişisel bilgiler çıkarıldı. Sayfalarda tarih yok, dosyalar Nisan 2014 arşiv tarihini taşıyor. Kaynak fotoğraflar özel arşivde tutuluyor; yazının indirme dosyası bulunmuyor.

## İdeal tersleyici ve gürültü ölçüleri

İdeal tersleyicinin gerilim geçiş eğrisi, V_in = V_DD/2 noktasında V_DD'den sıfıra iner:

- V_OL = 0; V_OH = V_DD; V_SW = V_DD.
- V_IL = V_IH = V_DD/2.
- V_NMH = V_OH − V_IH = V_DD/2.
- V_NML = V_IL − V_OL = V_DD/2.

Gerçek tersleyicide geçiş sonlu genişliktedir. Sayfadaki adlandırmayla belirsiz bölge V_IL ile V_IH arasındadır; V_M, giriş ile çıkışın eşitlendiği noktadır.

Gürültü duyarlılıkları:

**V_NSH = V_OH − V_M**, **V_NSL = V_M − V_OL**.

Normalize gürültü bağışıklıkları:

**V_NIH = V_NSH/V_SW**, **V_NIL = V_NSL/V_SW**.

İdeal simetrik durumda her iki duyarlılık V_DD/2 ve her iki normalize bağışıklık 1/2 olur.

## Fan-in ve fan-out

Not, fan-in'i bir kapının giriş sayısı olarak tanımlar. Çıkışın sürmesi gereken girişler için **I_out = N I′_in** yazılır. İdeal durumda R_in → ∞ ile giriş yüklenmesi azalır; R_out → 0 ile yükün şarj süresi küçülür.

Yüksek ve düşük mantık seviyelerindeki ayrı sınırlar:

N_high = I_out(high)/I′_in(high),

N_low = I_out(low)/I′_in(low).

En büyük fan-out, bu iki değerin küçüğünü aşmayan tamsayıdır.

*Not: Kaynak fan-out'u bir yerde “çıkış sayısı” diye kısaltıyor. Hesaplanan büyüklük fiziksel çıkış ucu sayısı değil, tek çıkışın sürebildiği kapı girişlerinin sayısıdır.*

## CMOS anahtarlama eşiği

V_in = V_out = V_M noktasında iki transistörün doyum akımları eşitlenir. Kaynağın işaretli PMOS gerilimleriyle yazdığı başlangıç eşitliği:

k_n V_DSATn[V_M − V_Tn − V_DSATn/2]

+ k_p V_DSATp[V_M − V_DD − V_Tp − V_DSATp/2] = 0.

V_M içeren terimler toplandığında:

V_M(k_nV_DSATn + k_pV_DSATp)

= k_nV_DSATn(V_Tn + V_DSATn/2)

+ k_pV_DSATp(V_DD + V_Tp + V_DSATp/2).

**r = k_pV_DSATp/(k_nV_DSATn)** tanımıyla:

**V_M = [(V_Tn + V_DSATn/2) + r(V_DD + V_Tp + V_DSATp/2)]/(1 + r)**.

Notta k = μC_ox(W/L) kullanılarak:

r = [μ_p C_ox,p(W_p/L_p)V_DSATp] / [μ_n C_ox,n(W_n/L_n)V_DSATn].

### Büyük overdrive yaklaşımı

V_DSAT = E_cL V_GT/(E_cL + V_GT) ifadesi büyük V_GT için E_cL'ye yaklaşır. Bu sayfada E_cL = Lv_sat/μ yazılmış. Eşit oksit kalınlıklarında C_ox,n = C_ox,p alınırsa notun ulaştığı oran:

r ≈ v_sat,p W_p/(v_sat,n W_n).

V_DD, eşik ve doyum gerilimlerinden büyük kabul edildiğinde:

V_M ≈ rV_DD/(1 + r).

r = 1 seçimi V_M ≈ V_DD/2 verir. Buna karşılık gelen boyutlandırma:

(W_p/L_p) = (W_n/L_n)[V_DSATn k′_n/(V_DSATp k′_p)].

*Not: MOS hız doyumu türetmesinin diğer sayfasında E_c = 2v_sat/μ kullanılıyor; bu sayfadaki yaklaşımın kritik alan tanımıyla aynı değil. İşaretli PMOS büyüklükleri de mutlak değerli formüllerle karıştırılmamalıdır.*

### Genel W/L oranı

Hedeflenen V_M için ayrı sayfada bulunan sonuç:

**(W/L)_p/(W/L)_n = k′_n V_DSATn(V_M − V_Tn − V_DSATn/2) / [k′_p V_DSATp(V_DD − V_M + V_Tp + V_DSATp/2)]**.

Bu, başlangıç akım eşitliğinin transistör boyutları için yeniden düzenlenmiş hâlidir.

## Eklem sığasının ortalama değeri

V_DD = 2,5 V örneğinde çıkışın ilk yarı geçişi ele alınıyor. Ters kutuplama gerilimi 2,5 V'tan 1,25 V'a değişirken taban eklemi için m = 0,5 ve Φ₀ = 0,9 V kullanılıyor. Sayfadaki eşdeğer katsayı:

K_eq = −Φ₀^m [(Φ₀ + 2,5)^(1−m) − (Φ₀ + 1,25)^(1−m)] / [(-2,5 + 1,25)(1−m)] ≈ **0,57**.

0 V'tan 1,25 V ters kutuplamaya karşılık gelen yarı geçiş için:

K_eq = −Φ₀^m [(Φ₀ + 1,25)^(1−m) − Φ₀^(1−m)] / [(-1,25)(1−m)] ≈ **0,79**.

0,25 µm süreç için 2λ = 0,25 µm, λ = 0,125 µm ve 19λ² ≈ 0,3 µm² yazılıyor. Kapı-drain örtüşme katkıları:

- NMOS: 2 × 0,31 × 0,375 ≈ 0,23 fF.
- PMOS: 2 × 0,27 × 1,125 ≈ 0,61 fF.

Arka sayfada K_eq,n = 0,57, K_eq,sw,n = 0,61, A_D = 0,3 µm², P_D = 1,875 µm alınmış:

C_db1 = K_eq,n A_D C_j + K_eq,sw,n P_D C_jsw

= 0,57 × 0,3 × 2 + 0,61 × 1,875 × 0,28 ≈ **0,66 fF**.

Çevre hesabındaki küçük çizimde 5λ + 4λ + 4λ + λ + λ = 15λ; 15 × 0,125 = 1,875 µm. Notun devamı, tersleyici geçici durum örneğinde bu yük sığasının ve W/L ile ölçeklenen R_eq'nin kullanılacağını söylüyor; sayfada nihai gecikme hesabı yok.

## Tersleyici zincirinde eşit kademe oranı

Üç kademeli çizimde giriş sığaları a, b, c ve son yük d olarak gösterilmiş:

d/c = c/b = b/a = f.

Böylece b = af, c = af², d = af³; **f = (d/a)^(1/3)**. Ara sığalar için b = √(ac), c = √(bd) yazılıyor.

Genel N kademede F = C_L/C_in ve f = F^(1/N). Notun toplam gecikme modeli:

**t_p = Nt_p0[1 + F^(1/N)/γ]**.

N'ye göre türev alıp sıfıra eşitleyince:

γ + F^(1/N) − F^(1/N)ln(F)/N = 0.

F = f^N konulursa γ + f − f ln f = 0 ve dolayısıyla:

**f = e^(1 + γ/f)**.

Notta γ = 0 sınırında N = ln F ve f = e sonucu ayrıca kutulanmış.

*Not: γ = 0 sonucu, türev koşulunun ideal sınırına aittir; 1/γ içeren gecikme ifadesine doğrudan sıfır koymak tanımsızdır.*

### F = 64, γ = 1 örneği

| Kademe sayısı N | Kademe oranı F^(1/N) | Kaynaktaki t_p/t_p0 |
|---|---|---|
| 1 | 64 | 65 |
| 2 | 8 | 18 |
| 3 | 4 | 15 |
| 4 | Yaklaşık 2,8 | 15,3 |

Bu seçenekler arasında üç kademe en küçük toplam gecikmeyi verir. Dört kademe için tam hesap 4(1 + 64^(1/4)) ≈ 15,314'tür; kaynaktaki 15,3 sonucu ile uyumludur.
