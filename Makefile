### -*- mode: makefile-gmake -*-

# Note: If building on Mac OS X, and if you use MacPorts, the following ports
# should be installed:
#
#   texlive-latex
#   texlive-plain-extra
#   texlive-latex-recommended
#   texlive-latex-extra
#   texlive-fonts-recommended
#   texlive-fonts-extra

FIGURES = $(patsubst %.dot,%.pdf,$(wildcard source/*.dot))

all: $(FIGURES) grammar xrefs document
	echo Draft standard compiled

%.pdf: %.dot
	dot -o $@ -Tpdf $<

grammar:
	(cd source ; sh ../tools/makegram)

xrefs:
	(cd source ; sh ../tools/makexref)

document:
	(cd source ; pdflatex std; pdflatex std; pdflatex std)
	(cd source ; makeindex generalindex)
	(cd source ; makeindex libraryindex)
	(cd source ; makeindex grammarindex)
	(cd source ; makeindex impldefindex)
	(cd source ; pdflatex std; pdflatex std)

### Makefile ends here
