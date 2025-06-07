# LangGraph ile Sosyal Ağ Analizi - Sunum Dokümantasyonu

Bu döküman, "LangGraph ile Sosyal Ağ Analizi" projesi için hazırlanan LaTeX sunumunun detaylarını içermektedir.

## Sunum Özeti

**Başlık:** LangGraph ile Sosyal Ağ Analizi: Çizge Teorisi ve AI Ajanları  
**Alan:** Bilgisayar Mühendisliği Yüksek Lisans - Çizge Teorisi  
**Süre:** ~45 dakika  
**Slide Sayısı:** 25+  

## Sunum Yapısı

### 1. Giriş ve Motivasyon (5 dakika)
- Proje motivasyonu ve problem tanımı
- Geleneksel yaklaşım vs. modern çözüm
- Projenin teorik ve pratik avantajları

### 2. Çizge Teorisi Temelleri (10 dakika)
- Temel tanımlar ve kavramlar
- Merkezi önem (centrality) ölçümleri
  - Derece merkeziliği
  - Arasındalık merkeziliği  
  - Yakınlık merkeziliği
  - Özvektor merkeziliği
- Topluluk tespiti algoritmaları

### 3. LangGraph Framework (8 dakika)
- LangGraph nedir ve temel bileşenleri
- State yönetimi ve tip güvenliği
- İş akışı tasarımı ve conditional routing

### 4. Sistem Mimarisi (7 dakika)
- Genel sistem mimarisi
- Pydantic veri modelleri
- NetworkX entegrasyonu
- Modüler tasarım ilkeleri

### 5. Analiz Türleri ve Algoritmalar (8 dakika)
- Desteklenen 6 farklı analiz türü
- Algoritmik implementasyonlar
- Louvain algoritması detayı

### 6. AI Entegrasyonu (5 dakika)
- Ollama LLM entegrasyonu
- Doğal dil sorgu işleme
- AI destekli içgörü üretimi

### 7. Uygulama Örnekleri (7 dakika)
- Gerçek kullanım senaryoları
- Performans analizi
- Örnek çıktılar

### 8. Sonuçlar ve Gelecek Çalışmalar (5 dakika)
- Proje başarıları ve katkıları
- Sistem limitasyonları
- Gelecek geliştirmeler

## Teknik Özellikler

### Kullanılan LaTeX Paketleri
```latex
\usepackage[utf8]{inputenc}
\usepackage[turkish]{babel}
\usepackage{amsmath, amsfonts, amssymb}
\usepackage{graphicx}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{tikz}
\usepackage{algorithm, algorithmic}
\usepackage{hyperref}
```

### Görsel Elementler
- TikZ ile çizilmiş sistem mimarisi diyagramları
- Algorithm pseudocode blokları
- Syntax highlighted kod örnekleri
- Matematiksel formül gösterimleri
- Tablo ve grafik örnekleri

### Tema ve Stil
- **Beamer Theme:** Madrid
- **Aspect Ratio:** 16:9
- **Font:** Computer Modern + Türkçe karakter desteği
- **Color Scheme:** Professional blue/green/orange kombinasyonu

## Matematiksel Formüller

Sunumda kullanılan temel formüller:

### Çizge Yoğunluğu
```latex
\delta = \frac{2|E|}{|V|(|V|-1)}
```

### Merkezi Önem Ölçümleri
```latex
% Derece Merkeziliği
C_D(v) = \frac{d(v)}{|V|-1}

% Arasındalık Merkeziliği  
C_B(v) = \sum_{s \neq v \neq t} \frac{\sigma_{st}(v)}{\sigma_{st}}

% Yakınlık Merkeziliği
C_C(v) = \frac{|V|-1}{\sum_{u \neq v} d(v,u)}
```

### Modülerlik Metriği
```latex
Q = \frac{1}{2m} \sum_{i,j} \left[ A_{ij} - \frac{k_i k_j}{2m} \right] \delta(c_i, c_j)
```

## Kod Örnekleri

Sunumda yer alan temel kod blokları:

### State Tanımı
```python
class GraphAgentState(TypedDict):
    user_query: str
    graph: Optional[Any]
    analysis_results: List[GraphAnalysisResult]
    current_metrics: Dict[str, float]
    insights: List[str]
    error_message: Optional[str]
    llm_response: str
```

### Analiz Fonksiyonu
```python
def calculate_comprehensive_metrics(self) -> GraphMetrics:
    density = nx.density(self.graph)
    degree_centrality = nx.degree_centrality(self.graph)
    betweenness_centrality = nx.betweenness_centrality(self.graph)
    return GraphMetrics(...)
```

## Sunum Hazırlama Talimatları

### LaTeX Derleme
```bash
# PDFLaTeX ile derleme (Türkçe karakter desteği için)
pdflatex presentation.tex
pdflatex presentation.tex  # İkinci geçiş referanslar için

# XeLaTeX ile derleme (alternatif)
xelatex presentation.tex
```

### Gerekli Paketler
```bash
# Ubuntu/Debian için
sudo apt-get install texlive-full
sudo apt-get install texlive-lang-turkish

# macOS için (MacTeX)
brew install mactex

# Windows için MiKTeX indirin
```

## Sunum Notları

### Önemli Vurgu Noktaları
1. **Hibrit Yaklaşım:** Klasik çizge teorisi + Modern AI birleşimi
2. **Type Safety:** Pydantic ile güvenli veri işleme
3. **Natural Language:** Doğal dil ile ağ analizi
4. **Modular Design:** Genişletilebilir mimari
5. **Real-time Analysis:** Anlık sonuç üretimi

### Demo Senaryoları
1. Temel ağ istatistikleri sorgusu
2. En etkili kişi analizi
3. Topluluk tespiti
4. Dayanıklılık analizi

### Soru-Cevap Hazırlığı
Potansiyel sorular ve cevaplar:

**S:** Neden LangGraph kullandınız?  
**C:** Durumsal iş akışları ve tip güvenliği için ideal

**S:** Büyük ağlarda performans nasıl?  
**C:** 1000 düğüme kadar O(n²) kompleksitesi, paralel işleme desteği

**S:** Diğer dil modellerini destekliyor mu?  
**C:** Evet, Ollama API üzerinden farklı modeller kullanılabilir

## Ek Materyaller

### Referanslar
- NetworkX Documentation
- LangGraph Official Guide  
- Ollama Model Repository
- Graph Theory Textbooks
- Social Network Analysis Literature

### Genişletilmiş Örnekler
`docs/examples/` klasöründe ek kod örnekleri ve kullanım senaryoları

### Görselleştirme Araçları
- TikZ ile ağ diyagramları
- Matplotlib ile grafik çizimleri
- Gephi ile ağ görselleştirme

## Sonuç

Bu sunum, LangGraph framework'ü ile sosyal ağ analizinin nasıl modern AI teknolojileriyle birleştirilebileceğini kapsamlı bir şekilde göstermektedir. Hem teorik temelleri hem de pratik uygulamaları içeren bu çalışma, çizge teorisi alanında yenilikçi bir yaklaşım sunmaktadır. 