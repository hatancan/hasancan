---
baslik: EEM312 Sayısal Elektronik: MOS Çalışma Bölgeleri, Hız Doyumu ve Sığalar, El Yazısı Notlar
ozet: NMOS/PMOS kanal oluşumu, gövde etkisi, kanal boyu modülasyonu, hız doyumu geriliminin türetilmesi ve MOS sığalarının hesabı. El yazısı çalışma sayfalarından okunabilir metin dökümü.
---

**EEM312 Sayısal Elektronik** arşivindeki bu çalışma, bir arkadaşın MOS transistörler üzerine hazırladığı Türkçe ve İngilizce el yazısı notlardan oluşuyor. Fotoğraflanmış sayfalardan metne aktarıldı; kişisel bilgiler çıkarıldı. Belge üzerinde tarih bulunmuyor; kaynakların arşiv tarihi Nisan 2014. Fotoğraflar özel arşivde tutuluyor, indirilebilir belge sunulmuyor.

## Gate insulation and channel formation

The notes give the following illustrative dimensions and values:

- SiO₂ thickness: 20–100 nm = 0,02–0,1 µm.
- Insulated-gate current: approximately 10⁻¹⁵ A.
- Channel length L ≈ 1–10 µm and width W ≈ 2–500 µm.
- Short-channel example: L ≈ 0,25 µm, W ≈ 0,375 µm.
- Without gate bias, the drain-source path has resistance on the order of 10¹² Ω.

These are values written in the archived notes, associated with the technologies studied there.

An induced n-channel is an inversion layer. V_T is the threshold voltage at which inversion occurs; the notes use positive V_T for enhancement NMOS and negative V_T for enhancement PMOS. **V_GS − V_T** is the excess gate voltage or overdrive.

With V_DS applied, electrons move from source to drain. Channel potential rises from 0 at the source to V_DS at the drain. The gate-to-channel voltage falls from V_GS to V_GS − V_DS, so the channel tapers toward the drain.

## Triode and saturation regions

As V_DS increases, the channel narrows at the drain and its resistance increases. The I_D–V_DS curve bends away from its initial nearly linear part. At **V_DS = V_GS − V_T**, the drain end reaches pinch-off.

| Device | Channel induced | Continuous channel / triode | Saturation |
|---|---|---|---|
| NMOS | V_GS ≥ V_T | V_DS < V_GS − V_T | V_DS ≥ V_GS − V_T |
| PMOS, signed voltages | V_GS ≤ V_T | V_DS > V_GS − V_T | V_DS ≤ V_GS − V_T |

Using **V_GS = V_GD + V_DS**, the notes rewrite the saturation condition as V_GD ≤ V_T for NMOS and V_GD ≥ V_T for PMOS.

The algebra at the region boundary is:

(V_GS − V_T)(V_GS − V_T) − (V_GS − V_T)²/2 = (V_GS − V_T)²/2.

The ideal long-channel saturation picture has constant current beyond pinch-off. The next section adds the channel-length effect.

## Channel-length modulation

Increasing V_DS beyond pinch-off extends the depleted drain region and shortens the effective conducting channel. The notes write:

**I_D = ½k′_n(W/L)(V_GS − V_T)²(1 + λV_DS)**.

Extrapolated saturation curves intersect the V_DS axis at −V_A = −1/λ. V_A is compared to the Early voltage of a BJT. The slope is marked **1/r_o**.

For the intercept, define Z = ½k′_n(W/L)(V_GS − V_T)². Then 0 = Z(1 + λV_DS) gives V_DS = −1/λ.

## Body effect in stacked NMOS devices

The drawing contains two stacked NMOS transistors. The lower source is grounded, with V_SB1 = 0; the upper source is above ground, with V_SB2 ≠ 0. The notes indicate:

|V_SB2| > |V_SB1| ⇒ V_T2 > V_T1.

Increasing source-body reverse bias raises the threshold. A separate warning on the page says that V_SB should remain above approximately −0,6 V for the NMOS example; otherwise the source-body diode becomes forward biased.

*Not: Aynı gövde etkisi çiziminin ikinci bir görüntüsü de kaynaklarda vardı; tek kez aktarıldı.*

## Hız doyumu geriliminin türetilmesi

Notta V_GT = V_GS − V_T ve K(V) = 1/[1 + V/(E_cL)] tanımları kullanılıyor. Doyum noktasında iki akım ifadesi eşitleniyor:

v_sat C_ox W(V_GT − V_DSAT)

= K(V_DSAT) μ_n C_ox(W/L)[V_GT V_DSAT − V_DSAT²/2].

Bu sayfadaki **E_c = 2v_sat/μ_n** tanımı kullanılarak:

V_GT − V_DSAT = K(V_DSAT) V_DSAT(2V_GT − V_DSAT)/(LE_c).

K(V_DSAT) = E_cL/(E_cL + V_DSAT) yerine konulduğunda:

V_DSAT(2V_GT + E_cL) = V_GT(E_cL + V_DSAT),

V_DSAT(V_GT + E_cL) = V_GT E_cL.

Sonuç:

**V_DSAT = V_GT E_cL/(V_GT + E_cL) = V_GT K(V_GT)**.

Büyük V_GT için V_DSAT ≈ E_cL.

*Not: Aynı not takımının CMOS eşik hesabı sayfası E_c = v_sat/μ yaklaşımını kullanıyor; burada ise 2v_sat/μ tanımı var. İki sayfanın kritik alan tanımları farklı olduğundan katsayılar birbirine doğrudan taşınmamalıdır.*

## Doyum akımı ve eşdeğer direnç

Notta yer alan diğer yaklaşım:

I_DSAT = v_sat C_ox W[V_GS − (V_T + V_DSAT/2)].

V_GS = V_DD ve V_DD ≫ V_T + V_DSAT/2 kabulüyle:

I_DSAT ≈ v_sat C_ox W V_DD.

R_eq = (3/4)(V_DD/I_DSAT)[1 − (7/9)λV_DD].

Böylece V_DD, ilk çarpanda sadeleşir. Not, bu yaklaşımda direncin besleme geriliminden büyük ölçüde bağımsızlaştığını; kalan küçük değişimin kanal boyu modülasyonundan geldiğini söylüyor.

## Sıfır kutuplamada MOS sığaları örneği

Kaynakta verilenler:

| Parametre | Değer |
|---|---|
| t_ox | 6 nm |
| L | 0,24 µm |
| W | 0,36 µm |
| L_D = L_S | 0,625 µm |
| C₀ | 3 × 10⁻¹⁰ F/m |
| C_j0 | 2 × 10⁻³ F/m² |
| C_jsw0 | 2,75 × 10⁻¹⁰ F/m |

C_ox = ε_ox/t_ox ≈ 5,7 fF/µm².

C_GC = WL C_ox ≈ 0,49 fF.

Source ve drain örtüşme sığalarının her biri W C₀ olarak hesaplanmış; sayfada 0,105 fF yazıyor. Toplam gate sığası sayfada **0,49 + 0,105 + 0,105 = 0,7 fF**.

Difüzyon sığasının taban ve yan duvar bileşenleri:

- C_bottom = C_j0 L_D W = 0,45 fF.
- C_sidewall = C_jsw0(2L_D + W) ≈ 0,44 fF.
- Toplam difüzyon sığası ≈ **0,89 fF**.

*Not: Yazılı W = 0,36 µm ve C₀ = 0,3 fF/µm ile örtüşme sığası 0,108 fF çıkar; 0,105 fF kaynakta kullanılan yuvarlatılmış/farklı ara değerdir. Toplam gate sığası bu verilerle yaklaşık 0,708 fF olur.*

## Tabaka ve kontak direnci

Uniform bir iletken şerit için:

R = ρL/A, A = tw ⇒ **R = (ρ/t)(L/W) = R_□(L/W)**.

R_□ tabaka direncidir; birimi Ω/kare olarak yazılır. L ve W aynı oranda büyütülürse L/W oranı ve direnç değişmez. Source/drain seri direnci notta:

R_S,D = (L_S,D/W)R_□ + R_C.

R_C kontak direncidir. Seri direnç aynı kontrol geriliminde drain akımını azaltır. Kaynak, düşük özdirençli yüzey işlemi ve transistörün genişletilmesini direnci azaltma yolları olarak sayar; yüzey işleminden sonra 1–4 Ω/kare mertebesini verir.
