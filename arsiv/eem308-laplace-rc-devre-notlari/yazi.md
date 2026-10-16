---
baslik: EEM308 Sinyaller ve Sistemler II: Laplace Dönüşümüyle RC Devresi Çözümleri ve s-Domeni Devre Modelleri (El Yazısı Notlar)
ozet: EEM308 dersinin Haziran 2014 tarihli el yazısı çalışma notları: RC devresinde transfer fonksiyonu ve dürtü yanıtı, tek taraflı Laplace dönüşümüyle başlangıç koşullu RC devresi, direnç, kondansatör ve endüktansın tek taraflı s-domeni modelleri.
---

Bu yazı, Başkent Üniversitesi **EEM 308 Sinyaller ve Sistemler II** dersinin final dönemine (15 Haziran 2014) ait üç sayfalık **el yazısı çalışma notunu** aktarıyor: bir RC devresinin iki farklı çıkış için transfer fonksiyonu ve dürtü yanıtı, başlangıç koşulu olan RC devresinin tek taraflı Laplace dönüşümüyle çözümü ve devre elemanlarının s-domeni modelleri. Sayfalarda ad veya numara yok. Notlar fotoğraflanmış sayfalardan metne aktarıldı; fotoğrafların kendisi arşivde saklanıyor, yayınlanmıyor.

## Örnek 1: Seri RC devresinde transfer fonksiyonu ve dürtü yanıtı

Bir v_s(t) gerilim kaynağı, R direnci ve C kondansatörü seri bağlı. İki durum isteniyor:

- **a)** x(t) = v_s(t), y(t) = v_c(t) (kondansatör gerilimi) için h(t) = ?
- **b)** x(t) = v_s(t), y(t) = i(t) (devre akımı) için h(t) = ?

### a) Çıkış kondansatör gerilimi

Devrenin diferansiyel denklemi:

dy(t)/dt + (1/RC) y(t) = (1/RC) x(t)

Laplace dönüşümü alınırsa sY(s) + (1/RC) Y(s) = (1/RC) X(s), dolayısıyla

H(s) = Y(s)/X(s) = (1/RC) / (s + 1/RC)

**h(t) = ℒ⁻¹{H(s)} = (1/RC) e^(−t/RC) u(t)**

### b) Çıkış devre akımı

i(t) = C dv_c(t)/dt ve Kirchhoff gerilim yasasından

−v_s(t) + R i(t) + (1/C) ∫₋∞ᵗ i(τ) dτ = 0

Burada x(t) = v_s(t), y(t) = i(t):

y(t) + (1/RC) ∫₋∞ᵗ y(τ) dτ = (1/R) x(t)

Türev alınırsa dy(t)/dt + (1/RC) y(t) = (1/R) dx(t)/dt, Laplace dönüşümüyle sY(s) + (1/RC) Y(s) = (1/R) s X(s):

H(s) = (s/R) / (s + 1/RC) = (1/R) · s / (s + 1/RC) = 1/R − (1/(R²C)) · 1/(s + 1/RC)

**h(t) = (1/R) δ(t) − (1/(R²C)) e^(−t/RC) u(t)**

## Örnek 2: Tek taraflı Laplace dönüşümü, başlangıç koşullu RC devresi

Anahtarın t = 0'da kapandığı seri RC devresinde v_c(0) = V₀ ve v_s(t) = V·u(t). İstenenler: **a)** i(t) = ? **b)** v_c(t) = ?

### a) Akım

R i(t) + (1/C) ∫₋∞ᵗ i(τ) dτ = v_s(t)

Tek taraflı Laplace dönüşümünde integralin 0⁻ öncesi kısmı başlangıç koşulunu verir: ∫₋∞⁰ i(τ) dτ = C v_c(0) = C V₀. Böylece

R I(s) + (1/C) [ (1/s) I(s) + (1/s) C V₀ ] = V/s
R I(s) + (1/(sC)) I(s) + V₀/s = V/s
(R + 1/(sC)) I(s) = (V − V₀)/s

I(s) = ((V − V₀)/s) · 1/(R + 1/(sC)) = ((V − V₀)/R) · 1/(s + 1/RC)

**i(t) = ((V − V₀)/R) e^(−t/RC) u(t)**

### b) Kondansatör gerilimi

C dv_c(t)/dt + v_c(t)/R = v_s(t)/R, yani dv_c(t)/dt + (1/RC) v_c(t) = (1/RC) v_s(t). Tek taraflı Laplace dönüşümüyle

s V_c(s) − v_c(0) + (1/RC) V_c(s) = (1/RC)(V/s)
V_c(s) (s + 1/RC) = (1/RC)(V/s) + V₀

*Not: Not sayfası bu satırda bitiyor. Çözümün devamı: V_c(s) = V/(s(RCs + 1)) + V₀/(s + 1/RC) = V/s − V/(s + 1/RC) + V₀/(s + 1/RC), dolayısıyla v_c(t) = [V + (V₀ − V) e^(−t/RC)] u(t). Kontrol: v_c(0) = V₀, v_c(∞) = V ve C dv_c/dt = ((V − V₀)/R) e^(−t/RC), a şıkkındaki akımla aynı.*

## Devre elemanlarının tek taraflı s-domeni modelleri

| Eleman | t bölgesi | s bölgesi |
| --- | --- | --- |
| Gerilim kaynağı | v(t) | V(s) |
| Akım kaynağı | i(t) | I(s) |
| Direnç | v(t) = R i(t) | V(s) = R I(s) |
| Kondansatör | i(t) = C dv(t)/dt | I(s) = sC V(s) − C v(0) |
| | | V(s) = (1/sC) I(s) + (1/s) v(0) |
| Endüktans | v(t) = L di(t)/dt | V(s) = sL I(s) − L i(0) |
| | | I(s) = (1/sL) V(s) + (1/s) i(0) |

Bu bağıntılar iki eşdeğer devreye karşılık gelir:

- **Kondansatör:** 1/sC empedansına **paralel** C·v(0) akım kaynağı (Norton biçimi) ya da 1/sC empedansıyla **seri** v(0)/s gerilim kaynağı (Thevenin biçimi).
- **Endüktans:** sL empedansıyla **seri** L·i(0) gerilim kaynağı ya da sL empedansına **paralel** i(0)/s akım kaynağı.

Notun son satırında bir sonraki konunun başlığı var: *Frekans tepkisinin kutup-sıfır diyagramından elde edilmesi.*

*Not: Notta endüktansın paralel modelindeki akım kaynağı v(0)/s gibi okunuyor; doğrusu, ikinci satırdaki I(s) = (1/sL)V(s) + (1/s)i(0) bağıntısının gösterdiği gibi i(0)/s'dir.*
