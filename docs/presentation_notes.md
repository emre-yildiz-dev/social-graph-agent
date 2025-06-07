# LangGraph ile Sosyal Ağ Analizi - Sunum Notları

## Genel Sunum Rehberi

### Başlangıç (5 dakika)
**Açılış:** "Günümüzde sosyal ağlar hayatımızın ayrılmaz bir parçası. Ancak bu karmaşık yapıları analiz etmek oldukça zor. Bugün sizlerle, çizge teorisinin güçlü matematiksel temellerini modern AI teknolojileriyle birleştiren yenilikçi bir yaklaşımı paylaşacağım."

**Motivasyon Vurguları:**
- Veri karmaşıklığı örneği: "10 kişilik bir grupta 45 farklı ilişki türü olabilir"
- Geleneksel yöntemlerin yetersizliği
- AI'ın analiz sürecindeki dönüştürücü rolü

---

## Bölüm Bazında Detaylı Notlar

### 1. Çizge Teorisi Temelleri (10 dakika)

#### Slide: Temel Tanımlar
**Konuşma Notu:** "Çizge teorisi, matematiksel olarak ilişkileri modelleyebilmemizi sağlar. Sosyal ağlarda her kişi bir düğüm (node), aralarındaki ilişkiler ise kenar (edge) olarak temsil edilir."

**Önemli Vurgular:**
- Yoğunluk formülünü açıklarken: "Yoğunluk 0 ile 1 arasında değişir. 1'e yaklaştıkça ağ daha sıkı bağlı demektir"
- TikZ diyagramını işaret ederek: "Bu basit örnekte 4 düğüm ve 4 kenar görüyoruz"

#### Slide: Merkezi Önem Ölçümleri
**Demo Hazırlığı:** Bu kısımda gerçek proje çıktısından örnekler gösterin

**Her ölçüm için açıklama:**
1. **Derece Merkeziliği:** "En popüler kişi kimdir? Doğrudan bağlantı sayısı"
2. **Arasındalık Merkeziliği:** "Bilgi köprüsü kimdir? İki kişi arasındaki yolda bulunma sıklığı"
3. **Yakınlık Merkeziliği:** "Herkese en hızlı ulaşan kimdir? Ortalama mesafe"
4. **Özvektor Merkeziliği:** "Etkili kişilerle bağlantılı olan kimdir? Kaliteli bağlantılar"

---

### 2. LangGraph Framework (8 dakika)

#### Slide: LangGraph Nedir?
**Açıklama:** "LangGraph, özellikle AI agent sistemleri için tasarlanmış bir framework. Geleneksel linear iş akışlarından farklı olarak, durumsal hafızaya sahip ve döngüsel süreçleri destekler."

**Avantajlar Vurgusu:**
- "Type Safety sayesinde geliştirme sürecinde hata yakalama"
- "Conditional Routing ile dinamik karar verme"

#### Slide: State Yönetimi
**Kod Açıklaması:** "TypedDict kullanarak her state değişkeninin tipini önceden belirliyoruz. Bu hem hata önleme hem de kod okunabilirliği açısından kritik."

---

### 3. Sistem Mimarisi (7 dakika)

#### Slide: Genel Mimari
**Diyagram Açıklaması:** "Katmanlı mimari yaklaşımı kullandık:
1. Kullanıcı doğal dil ile sorgu girer
2. Agent sorguyu analiz eder ve uygun araçları seçer  
3. NetworkX ile matematiksel hesaplamalar yapılır
4. LLM sonuçları yorumlayarak kullanıcı dostu açıklamalar üretir"

---

### 4. Demo Senaryoları

#### Demo 1: Temel Sorgu
```python
# Canlı demo için hazır komut
agent = SocialGraphAgent()
result = agent.analyze_social_network("Bu ağda en etkili kişiler kimler?")
print(result['insights'])
```

**Beklenen Çıktı Açıklaması:** "Sistem otomatik olarak merkezi önem analizine yönlendirildi ve Frank'in en etkili kişi olduğunu tespit etti."

#### Demo 2: Karmaşık Analiz
```python
result = agent.analyze_social_network("Frank'in ayrılması organizasyonu nasıl etkiler?")
```

**Sonuç Yorumlama:** "AI sadece rakamları vermekle kalmıyor, sonuçların pratik anlamını da açıklıyor."

---

## Soru-Cevap Hazırlığı

### Teknik Sorular

**S: "NetworkX yerine daha hızlı alternatifler var mı?"**
C: "Evet, NetworkX Python için ideal ama büyük ölçekli ağlar için igraph veya graph-tool daha performanslı. Ancak LangGraph yapısı sayesinde backend değişimi kolay."

**S: "Ollama yerine OpenAI API kullanılabilir mi?"**  
C: "Kesinlikle! LLM client modüler tasarlandı. Sadece base class'ı implement ederek farklı LLM'ler eklenebilir."

**S: "Gerçek zamanlı ağ değişimlerini takip edebilir mi?"**
C: "Şu anki versiyon statik analizler yapıyor. Ancak streaming data desteği için LangGraph'ın state persistence özelliği kullanılabilir."

### Algoritma Soruları

**S: "Topluluk tespitinde neden Louvain algoritması seçildi?"**
C: "Louvain modülerlik optimizasyonu yapar ve büyük ağlarda hızlı çalışır. Ayrıca hiyerarşik topluluk yapısını da destekler."

**S: "Merkezi önem ölçümleri arasında öncelik var mı?"**
C: "Analiz amacına bağlı. Bilgi yayılımı için yakınlık, kontrol için arasındalık, popülerlik için derece merkeziliği daha uygun."

### Uygulama Soruları

**S: "Hangi sektörlerde uygulanabilir?"**
C: "Çok geniş uygulama alanı var:
- Akademide işbirliği ağları
- İş dünyasında org chart analizi  
- Sosyal medyada influence tracking
- Finans sektöründe risk analizi"

**S: "Performans sınırları neler?"**
C: "1000 düğüme kadar sorunsuz. Daha büyük ağlar için paralel işleme ve graf partitioning gerekir."

---

## Demo Script Detayları

### Pre-Demo Hazırlık
```bash
# Terminal hazırlığı
cd /Users/emre/code/latex/LangGraph
source .venv/bin/activate

# Ollama servis kontrolü
ollama list | grep gemma

# Test komutu
python -c "from social_graph_agent import SocialGraphAgent; print('✓ Ready')"
```

### Demo 1: Hızlı Analiz
```python
agent = SocialGraphAgent()

# Basit sorgu
result = agent.analyze_social_network("Who are the most influential people?")
print("=== ANALYSIS RESULTS ===")
print(result['insights'][:200] + "...")
```

### Demo 2: Topluluk Analizi
```python
# Topluluk tespiti
result = agent.analyze_social_network("What groups exist in this network?")
print("=== COMMUNITY ANALYSIS ===")
for analysis in result['analysis_results']:
    if analysis['operation'] == 'community_detection':
        print(f"Found {len(analysis['result']['communities'])} communities")
```

### Demo 3: Dayanıklılık
```python
# Robustness analizi
result = agent.analyze_social_network("How robust is this network?")
print("=== ROBUSTNESS ANALYSIS ===")
print(result['insights'][:300] + "...")
```

---

## Görsel Materyal Rehberi

### Slides için Ek Görseller
1. **NetworkX örnek graf çıktısı** - `matplotlib` ile basit ağ görselleştirmesi
2. **Merkezi önem karşılaştırma tablosu** - Excel/matplotlib
3. **LangGraph iş akışı animasyonu** - Draw.io veya Miro
4. **Performans grafikleri** - Düğüm sayısı vs süre

### Code Syntax Highlighting
```latex
% LaTeX için kod renklendirme
\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}
```

---

## Zaman Yönetimi

### Slide Geçiş Süreleri
- **Giriş:** 5 dakika (3 slide)
- **Çizge Teorisi:** 10 dakika (5 slide)  
- **LangGraph:** 8 dakika (4 slide)
- **Sistem Mimarisi:** 7 dakika (3 slide)
- **Analiz Türleri:** 8 dakika (4 slide)
- **AI Entegrasyonu:** 5 dakika (3 slide)
- **Demo ve Örnekler:** 7 dakika (3 slide)
- **Sonuç:** 5 dakika (4 slide)

### Backup Planları
- **Ollama çalışmıyorsa:** Önceden kaydedilmiş çıktıları göster
- **İnternet yoksa:** Local demo verileri kullan
- **Zaman kısıtlıysa:** Demo bölümünü kısalt, teoriye odaklan

---

## Son Kontrol Listesi

### Teknik Hazırlık
- [ ] Laptop şarj dolu
- [ ] Backup USB drive
- [ ] PDF ve LaTeX source kopyaları
- [ ] Demo environment test edildi
- [ ] Ollama servisi çalışır durumda

### Sunum Materyalleri  
- [ ] Presentation remote kontrol
- [ ] Laser pointer (isteğe bağlı)
- [ ] Su/kahve
- [ ] Backup slides (PDF)
- [ ] Demo script çıktısı

### İçerik Kontrolleri
- [ ] Tüm formüller doğru
- [ ] Türkçe karakterler çalışıyor
- [ ] Code syntax highlighting aktif
- [ ] TikZ diyagramları düzgün render
- [ ] Hyperlink'ler çalışıyor

---

## Sonuç Mesajları

### Ana Takeaway'ler
1. **Hibrit yaklaşım:** Matematik + AI kombinasyonu güçlü
2. **Practical value:** Gerçek problemlere uygulanabilir
3. **Extensible:** Framework genişletilebilir
4. **User-friendly:** Doğal dil arayüzü

### Call to Action
"Bu proje açık kaynak. GitHub'dan inceleyebilir, katkıda bulunabilir veya kendi projelerinizde kullanabilirsiniz. Sorularınız varsa benimle iletişime geçmekten çekinmeyin." 