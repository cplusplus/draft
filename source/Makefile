default: full

clean:
	rm -f *.aux std.pdf std-gram.ext *.idx *.ilg *.ind *.log *.lot *.lof *.tmp *.out *.glo *.gls *.fls *.fdb* *.toc *.xtr

refresh:
	pdflatex std

full:
	latexmk -pdf std

%.pdf: %.dot
	dot -o $@ -Tpdf $<
