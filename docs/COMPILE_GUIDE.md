# LangGraph Sosyal Ağ Analizi Sunumu - Derleme Kılavuzu

## Hızlı Başlangıç

```bash
# Docs klasörüne gidin
cd docs/

# Sunumu derleyin
make

# PDF'yi açın
make open
```

## Sistem Gereksinimleri

### macOS
```bash
# MacTeX kurulumu (tam LaTeX dağıtımı)
brew install mactex

# Veya daha hafif BasicTeX
brew install basictex
sudo tlmgr update --self
sudo tlmgr install collection-latexrecommended beamer
```

### Ubuntu/Debian
```bash
# Tam TeX Live kurulumu
sudo apt-get update
sudo apt-get install texlive-full

# Türkçe dil desteği
sudo apt-get install texlive-lang-turkish

# İsteğe bağlı: PDF görüntüleyici
sudo apt-get install evince okular
```

### Windows
1. [MiKTeX](https://miktex.org/download) indirip kurun
2. MiKTeX Console'dan gerekli paketleri indirin:
   - beamer
   - tikz
   - listings
   - babel-turkish

## Gerekli LaTeX Paketleri

Sunumun derlenmesi için aşağıdaki paketler gereklidir:

```latex
% Temel paketler
\usepackage[utf8]{inputenc}
\usepackage[turkish]{babel}
\usepackage{amsmath, amsfonts, amssymb}

% Görsel paketler
\usepackage{graphicx}
\usepackage{tikz}
\usepackage{xcolor}

% Kod ve algoritma
\usepackage{listings}
\usepackage{algorithm}
\usepackage{algorithmic}

% Diğer
\usepackage{hyperref}
```

## Derleme Seçenekleri

### 1. Makefile Kullanımı (Önerilen)

```bash
# Tam derleme
make

# Hızlı derleme (referanslar olmadan)
make quick

# XeLaTeX ile derleme (gelişmiş font desteği)
make xelatex

# Sistem kontrolü
make check

# Yardım
make help
```

### 2. Manuel Derleme

```bash
# PDFLaTeX ile
pdflatex presentation.tex
bibtex presentation
pdflatex presentation.tex
pdflatex presentation.tex

# XeLaTeX ile (Türkçe karakterler için önerilen)
xelatex presentation.tex
bibtex presentation
xelatex presentation.tex
xelatex presentation.tex
```

### 3. Latexmk ile Otomatik Derleme

```bash
# Sürekli derleme modu
latexmk -pdf -pvc presentation.tex

# Tek seferlik derleme
latexmk -pdf presentation.tex
```

## Sorun Giderme

### Türkçe Karakter Problemi

**Problem:** Türkçe karakterler düzgün görünmüyor
**Çözüm:**
```bash
# XeLaTeX kullanın
make xelatex

# Veya fontenc paketini ekleyin
\usepackage[T1]{fontenc}
```

### TikZ Diyagramları Çalışmıyor

**Problem:** Diyagramlar görünmüyor
**Çözüm:**
```bash
# TikZ paketini kontrol edin
tlmgr install pgf tikz

# Shell escape'i etkinleştirin
pdflatex -shell-escape presentation.tex
```

### Referanslar Görünmüyor

**Problem:** \cite komutları çalışmıyor
**Çözüm:**
```bash
# BibTeX adımını atlamamış olduğunuzdan emin olun
pdflatex presentation.tex
bibtex presentation      # Bu adım önemli!
pdflatex presentation.tex
pdflatex presentation.tex
```

### Font Bulunamıyor Hatası

**Problem:** "Font not found" hatası
**Çözüm:**
```bash
# Font cache'i yenileyin
fc-cache -fv

# Veya daha basit fontlar kullanın
\usepackage{lmodern}
```

## Dosya Yapısı

```
docs/
├── presentation.tex          # Ana sunum dosyası
├── references.bib           # Kaynakça
├── presentation_notes.md    # Sunum notları
├── README_presentation.md   # Sunum dokümantasyonu
├── COMPILE_GUIDE.md        # Bu dosya
├── Makefile                # Derleme otomasyonu
└── output/                 # Oluşturulan dosyalar (otomatik)
    ├── presentation.pdf
    ├── presentation.aux
    └── ...
```

## Özelleştirme

### Tema Değiştirme

```latex
% Ana tema
\usetheme{Madrid}          % Varsayılan

% Alternatifler
\usetheme{Warsaw}
\usetheme{Singapore}
\usetheme{CambridgeUS}

% Renk şeması
\usecolortheme{default}    % Varsayılan
\usecolortheme{whale}
\usecolortheme{dolphin}
```

### Kod Renklendirme

```latex
\lstset{
    backgroundcolor=\color{gray!10},
    basicstyle=\footnotesize\ttfamily,
    keywordstyle=\color{blue},
    commentstyle=\color{green!60!black},
    stringstyle=\color{red},
    numbers=left,              % Satır numaraları
    showstringspaces=false,
    breaklines=true,
    language=Python
}
```

### Kişisel Bilgileri Güncelleme

`presentation.tex` dosyasında aşağıdaki satırları düzenleyin:

```latex
\title{LangGraph ile Sosyal Ağ Analizi: \\ Çizge Teorisi ve AI Ajanları}
\subtitle{Bilgisayar Mühendisliği Yüksek Lisans - Çizge Teorisi}
\author{[Öğrenci Adı]}        % Buraya adınızı yazın
\institute{[Üniversite Adı]}  % Üniversite adını güncelleyin
\date{\today}
```

## Performance İpuçları

### Hızlı Geliştirme

```bash
# Sadece değişen kısımları derle
make quick

# Sürekli derleme modu
make watch

# Draft modu (daha hızlı)
\documentclass[draft]{beamer}
```

### Büyük Dosyalar için

```bash
# SSD kullanıyorsanız paralel derleme
latexmk -pdf -pvc -interaction=nonstopmode

# RAM disk kullanımı (Linux)
sudo mount -t tmpfs -o size=1G tmpfs /tmp/latex-build
```

## Versiyon Kontrolü

### Git için .gitignore

```gitignore
# LaTeX build dosyaları
*.aux
*.log
*.out
*.toc
*.nav
*.snm
*.vrb
*.bbl
*.blg
*.fls
*.fdb_latexmk
*.synctex.gz

# Geçici dosyalar
*~
.DS_Store
```

### Yedekleme

```bash
# Önemli dosyaları yedekleyin
cp presentation.tex presentation_backup_$(date +%Y%m%d).tex
cp references.bib references_backup_$(date +%Y%m%d).bib
```

## Çıktı Kalitesi

### Yüksek Kalite PDF

```bash
# DPI ayarı
pdflatex -interaction=nonstopmode -output-directory=output presentation.tex

# Vector grafikleri koruma
\usepackage[pdftex]{graphicx}
\DeclareGraphicsExtensions{.pdf,.png,.jpg}
```

### Print Kalitesi

```latex
% Yüksek çözünürlük için
\pdfcompresslevel=0
\pdfobjcompresslevel=0

% Renkli baskı için
\usepackage[cmyk]{xcolor}
```

## Son Kontrol Listesi

Sunumdan önce aşağıdakileri kontrol edin:

- [ ] PDF başarıyla derlendi
- [ ] Tüm slide'lar düzgün görünüyor
- [ ] Türkçe karakterler doğru
- [ ] Matematik formülleri okunabilir
- [ ] Kod blokları syntax highlighted
- [ ] TikZ diyagramları tam
- [ ] Hyperlink'ler çalışıyor
- [ ] PDF boyutu makul (< 10MB)
- [ ] Backup kopyalar alınmış

## Destek

Problem yaşadığınızda:

1. **Log dosyalarını kontrol edin:** `presentation.log`
2. **Makefile help'i çalıştırın:** `make help`
3. **Online LaTeX editör deneyin:** [Overleaf](https://overleaf.com)
4. **TeX Stack Exchange'e başvurun:** [tex.stackexchange.com](https://tex.stackexchange.com)

## Başarılı Derleme Örneği

```bash
$ make
LaTeX sunumu derleniyor...
This is pdfTeX, Version 3.141592653-2.6-1.40.22 (TeX Live 2021)
...
Output written on presentation.pdf (25 pages, 1234567 bytes).
BibTeX referansları işleniyor...
...
✓ Sunum başarıyla derlendi: presentation.pdf

$ make open
# PDF otomatik olarak açılır
```

Başarılar! 🎉 