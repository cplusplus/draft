### -*- mode: makefile-gmake -*-

FIGURES = $(patsubst %.dot,%.pdf,$(wildcard *.dot))

STDPDF = pdflatex std | grep -v "^Overfull"

default: rebuild

clean:
	rm -f *.aux std.pdf std-gram.ext *.idx *.ilg *.ind *.log *.lot *.lof *.tmp *.out *.glo *.gls *.fls *.fdb* *.toc *.xtr

refresh:
	$(STDPDF)

rebuild:
	$(STDPDF)
	$(STDPDF)
	$(STDPDF)

full: $(FIGURES) reindex

%.pdf: %.dot
	dot -o $@ -Tpdf $<

reindex:
	$(STDPDF)
	$(STDPDF)
	$(STDPDF)
	makeindex -s generalindex.ist generalindex
	makeindex headerindex
	makeindex -s libraryindex.ist libraryindex
	makeindex grammarindex
	makeindex impldefindex
	$(STDPDF)
	makeindex -s basic.gst -o xrefindex.gls xrefindex.glo
	makeindex -s basic.gst -o xrefdelta.gls xrefdelta.glo
	$(STDPDF)
	$(STDPDF)

### Makefile ends here
