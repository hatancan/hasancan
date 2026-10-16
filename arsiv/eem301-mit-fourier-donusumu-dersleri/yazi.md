---
baslik: EEM301 Sinyaller ve Sistemler I: Sürekli ve Ayrık Zamanlı Fourier Dönüşümü Sunumları (MIT 6.003, Alan Willsky, 2007)
ozet: MIT Signals and Systems dersinin Bahar 2007 dönemi 8, 9 ve 10. ders sunumlarının özeti: sürekli zamanlı Fourier dönüşümünün türetilmesi, örnekler ve özellikler, konvolüsyon ve çarpma özellikleri, frekans yanıtı, Parseval bağıntısı, ayrık zamanlı Fourier dönüşümü ve özellikleri.
---

Bu yazı, EEM301 Sinyaller ve Sistemler I klasöründe kaynak olarak duran üç PowerPoint sunumunu tanıtıyor: **MIT Signals and Systems** dersinin Bahar 2007 dönemine ait **Lecture #8 (6 Mart 2007), #9 (8 Mart 2007) ve #10 (13 Mart 2007)**; sunumların yazarı Alan Willsky olarak görünüyor. Konular Oppenheim & Willsky kitabının 4. ve 5. bölümlerini izliyor. Sunumlar İngilizce; aşağıda başlıklar ve ana fikirler aktarıldı. Orijinal sunumlar yazının sonunda ZIP olarak indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Lecture 8: Sürekli zamanlı Fourier dönüşümü (CTFT)

1. Fourier dönüşümü çiftinin türetilmesi
1. Fourier dönüşümü örnekleri
1. Periyodik sinyallerin Fourier dönüşümü
1. CTFT'nin özellikleri

- **Fourier'nin türetmesi:** Periyodik olmayan x(t), periyodu T → ∞ giden bir periyodik sinyalin limiti olarak düşünülür. Harmonikler ω₀ = 2π/T aralıklıdır; T büyüdükçe ω₀ → 0 olur, ayrık frekans noktaları sıklaşır ve Fourier serisi toplamı bir integrale dönüşür (kare dalga örneği).
- **Hangi sinyaller için geçerli:** sonlu enerjili sinyaller (hata sinyalinde enerji sıfır), Dirichlet koşullarını sağlayan sinyaller; x(t) ya da X(jω)'da dürtülere izin verilerek periyodik sinyaller de kapsanır.
- **Örnekler:** dürtü ve kaydırılmış dürtü, üstel fonksiyonlar (çift ve tek simetri), zamanda kare darbe (iki genişlik arasındaki ters ilişki: belirsizlik ilkesi), Gauss fonksiyonu e^(−at²) (dönüşümü yine Gauss; Δt·Δω ~ 1, iki genişlik birden keyfî küçültülemez).
- **Periyodik sinyaller:** "çizgi spektrumu"; dürtü katarı (örnekleme fonksiyonu) için zamandaki periyot T, frekanstaki periyot 2π/T (yine ters ilişki).
- **Özellikler:** doğrusallık, zamanda kayma (genlik değişmez, fazda doğrusal değişim), eşlenik simetri (x(t) gerçel ve çiftse X gerçel ve çift, gerçel ve tekse X sanal ve tek), zaman ölçekleme.

## Lecture 9: Konvolüsyon özelliği ve DTFT'ye giriş

1. CTFT'nin konvolüsyon özelliği
1. Frekans yanıtı ve LTI sistemler
1. Çarpma özelliği ve Parseval bağıntısı
1. Ayrık zamanlı Fourier dönüşümü

- **Konvolüsyon özelliği:** y(t) = h(t) ∗ x(t) ⟷ Y(jω) = H(jω)X(jω); özfonksiyon özelliğinin bir sonucu. Sürekli zamanlı LTI sistemin frekans yanıtı, dürtü yanıtının Fourier dönüşümüdür.
- **Örnekler:** türev alıcı (H(jω) = jω, yüksek frekansları kuvvetlendirir, keskin kenarları belirginleştirir); ideal alçak geçiren süzgecin dürtü yanıtı (nedensel mi? h(0) nedir? basamak yanıtının kalıcı değeri nedir?); ardışık süzme işlemleri; Gauss ∗ Gauss = Gauss.
- **Doğrusal sabit katsayılı diferansiyel denklemlerle tanımlı LTI sistemler:** türev özelliğiyle H(jω) rasyonel bir fonksiyon olur; kısmi kesirlerle h(t) bulunur. X(jω) rasyonelse Y(jω) da rasyoneldir.
- **Parseval bağıntısı** ve **çarpma özelliği:** ikilik (dualite) sayesinde zamanda çarpma frekansta konvolüsyona karşılık gelir; genlik modülasyonu örnekleri.
- **DTFT'nin türetilmesi:** sürekli zamandakine benzer şekilde, periyodu sonsuza giden ayrık periyodik sinyalin Fourier serisinden.

## Lecture 10: Ayrık zamanlı Fourier dönüşümü (DTFT)

1. DTFT örnekleri
1. DTFT'nin özellikleri
1. Konvolüsyon özelliği ve kullanımı

- **DTFT çifti:** analiz denklemi X(e^(jω)) = Σ x[n]e^(−jωn), sentez denklemi x[n] = (1/2π)∫_{2π} X(e^(jω))e^(jωn) dω. Sentez denkleminde sonlu aralıkta integral alındığı için yakınsama sorunu yok; analiz denklemi için sonlu enerji ya da mutlak toplanabilirlik gerekir.
- **Örnekler:** sürekli zamandaki örneklerin ayrık karşılıkları, ayrık zamanlı dikdörtgen darbe (N₁ = 2 için çizilmiş), karmaşık üstellerin toplamları: e^(jω₀n)'nin DTFT'si ω₀'da alanı 2π olan bir dürtü, ama X(e^(jω)) 2π periyotlu olmak zorunda olduğundan ω₀ + 2πk noktalarının hepsinde dürtü vardır. Ayrık sinüs ve ayrık periyodik dürtü katarı (frekans domeninde de periyodik dürtü katarı).
- **Özellikler:** doğrusallık, kaydırmalar, eşlenik simetri, periyodiklik nedeniyle ayrık zamanda farklılaşan özellikler; **zamanda genişletme:** x[n/2] tanımsız, x[2n] tek indisli değerleri kaçırır; bunun yerine ardışık değerler arasına (k − 1) sıfır eklenerek x_(k)[n] elde edilir; zamanda k kat genişleme frekansta k kat sıkışma demektir. Frekansta türev ve Parseval bağıntısı (zaman ve frekans domenindeki toplam enerji eşit).
- **Konvolüsyon özelliği:** y[n] = x[n] ∗ h[n] ⟷ Y(e^(jω)) = X(e^(jω))H(e^(jω)); örnekler arasında ideal ayrık zamanlı alçak geçiren süzgeç var.
