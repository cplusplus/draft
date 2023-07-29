FIGURES=$(patsubst %.dot,%.pdf,$(wildcard assets/*.dot))

default: full

clean:
	rm -f *.aux std.pdf std-gram.ext *.idx *.ilg *.ind *.log *.lot *.lof *.tmp *.out *.glo *.gls *.fls *.fdb* *.toc *.xtr

refresh:
	lualatex std

full:
	latexmk -pdflua std

quiet:
	latexmk -pdflua std -e '$$max_repeat = 1;' -silent || ( rm std.pdf; latexmk -pdflua std -e '$$max_repeat = 4;' )

%.pdf: %.dot
	dot -o $@ -Tpdf $< -Nfontname=NewComputerModernSans10

clean-figures:
	rm -f $(FIGURES)

figures: $(FIGURES)
