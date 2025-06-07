# LangGraph Sosyal Ağ Analizi Sunumu - Makefile

# Değişkenler
TEXFILE = presentation
PDFFILE = $(TEXFILE).pdf
LATEX = pdflatex
BIBTEX = bibtex

# Varsayılan hedef
all: $(PDFFILE)

# PDF oluşturma
$(PDFFILE): $(TEXFILE).tex references.bib
	@echo "LaTeX sunumu derleniyor..."
	$(LATEX) $(TEXFILE).tex
	@echo "BibTeX referansları işleniyor..."
	$(BIBTEX) $(TEXFILE)
	@echo "İkinci LaTeX geçişi..."
	$(LATEX) $(TEXFILE).tex
	@echo "Üçüncü LaTeX geçişi (referanslar için)..."
	$(LATEX) $(TEXFILE).tex
	@echo "✓ Sunum başarıyla derlendi: $(PDFFILE)"

# Hızlı derleme (sadece LaTeX, referans olmadan)
quick: $(TEXFILE).tex
	@echo "Hızlı LaTeX derlemesi..."
	$(LATEX) $(TEXFILE).tex
	@echo "✓ Hızlı derleme tamamlandı"

# XeLaTeX ile derleme (gelişmiş font desteği için)
xelatex: $(TEXFILE).tex
	@echo "XeLaTeX ile derleniyor..."
	xelatex $(TEXFILE).tex
	xelatex $(TEXFILE).tex
	@echo "✓ XeLaTeX derlemesi tamamlandı"

# Temizlik
clean:
	@echo "Geçici dosyalar temizleniyor..."
	rm -f *.aux *.log *.out *.toc *.nav *.snm *.vrb *.bbl *.blg *.fls *.fdb_latexmk *.synctex.gz
	@echo "✓ Temizlik tamamlandı"

# Tam temizlik (PDF dahil)
distclean: clean
	@echo "PDF dosyası da siliniyor..."
	rm -f $(PDFFILE)
	@echo "✓ Tam temizlik tamamlandı"

# PDF'yi açma (macOS için)
open: $(PDFFILE)
	@if command -v open >/dev/null 2>&1; then \
		open $(PDFFILE); \
	elif command -v evince >/dev/null 2>&1; then \
		evince $(PDFFILE) & \
	elif command -v okular >/dev/null 2>&1; then \
		okular $(PDFFILE) & \
	else \
		echo "PDF görüntüleyici bulunamadı"; \
	fi

# Sürekli derleme modu
watch:
	@echo "Dosya değişikliği izleniyor (Ctrl+C ile çıkış)..."
	@while true; do \
		inotifywait -e modify $(TEXFILE).tex 2>/dev/null && \
		make quick && \
		echo "Güncellendi: $(shell date)"; \
	done

# Spellcheck (aspell gerekli)
spell:
	@echo "Yazım denetimi yapılıyor..."
	aspell check $(TEXFILE).tex

# Presentation notes'u Markdown'dan PDF'e çevirme
notes: presentation_notes.md
	@echo "Sunum notları PDF'e çevriliyor..."
	@if command -v pandoc >/dev/null 2>&1; then \
		pandoc presentation_notes.md -o presentation_notes.pdf; \
		echo "✓ Notlar PDF'e çevrildi"; \
	else \
		echo "Pandoc yüklü değil, Markdown dosyası olarak bırakıldı"; \
	fi

# Sistem gereksinimlerini kontrol etme
check:
	@echo "Sistem gereksinimleri kontrol ediliyor..."
	@command -v $(LATEX) >/dev/null 2>&1 || { echo "❌ PDFLaTeX yüklü değil"; exit 1; }
	@command -v $(BIBTEX) >/dev/null 2>&1 || { echo "❌ BibTeX yüklü değil"; exit 1; }
	@echo "✓ LaTeX sistemi hazır"
	@echo "✓ Tüm gereksinimler karşılanıyor"

# Yardım menüsü
help:
	@echo "LangGraph Sosyal Ağ Analizi Sunumu - Makefile"
	@echo ""
	@echo "Kullanılabilir hedefler:"
	@echo "  all       - Tam derleme (varsayılan)"
	@echo "  quick     - Hızlı derleme"
	@echo "  xelatex   - XeLaTeX ile derleme"
	@echo "  clean     - Geçici dosyaları temizle"
	@echo "  distclean - Tüm dosyaları temizle"
	@echo "  open      - PDF'yi aç"
	@echo "  watch     - Sürekli derleme modu"
	@echo "  spell     - Yazım denetimi"
	@echo "  notes     - Notları PDF'e çevir"
	@echo "  check     - Sistem gereksinimlerini kontrol et"
	@echo "  help      - Bu yardım menüsünü göster"
	@echo ""
	@echo "Örnek kullanım:"
	@echo "  make        # Sunumu derle"
	@echo "  make open   # Derle ve aç"
	@echo "  make clean  # Temizle"

# Phony targets
.PHONY: all quick xelatex clean distclean open watch spell notes check help 