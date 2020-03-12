FIGURES=$(patsubst %.dot,%.pdf,$(wildcard *.dot))

default: full

clean:
	rm -f *.aux std.pdf std-gram.ext *.idx *.ilg *.ind *.log *.lot *.lof *.tmp *.out *.glo *.gls *.fls *.fdb* *.toc *.xtr

refresh:
	pdflatex std

full:
	latexmk -pdf std

quiet:
	latexmk -pdf std -e '$$max_repeat = 1;' -silent || ( rm std.pdf; latexmk -pdf std -e '$$max_repeat = 4;' )

%.pdf: %.dot
	dot -o $@ -Tpdf $<

clean-figures:
	rm -f $(FIGURES)

figures: $(FIGURES)
