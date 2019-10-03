#!/bin/bash

# Ignore files where rules may be violated within macro definitions.
texfiles=$(ls *.tex | grep -v macros.tex | grep -v layout.tex | grep -v tables.tex)
texlib="lib-intro.tex support.tex concepts.tex diagnostics.tex utilities.tex iterators.tex ranges.tex algorithms.tex numerics.tex time.tex locales.tex iostreams.tex regex.tex atomics.tex threads.tex"

grep -Fe "Overfull \\hbox" std.log && exit 1
grep "LaTeX Warning..There were undefined references" std.log && exit 1

# Trailing whitespace in a line.
grep -ne '\s$' *.tex | sed 's/$/<--- trailing whitespace/' | grep . && exit 1

# Trailing empty lines
for f in *.tex; do [ $(tail -c 2 $f | wc -l) -eq 1 ] || (echo "$f has trailing empty lines"; exit 1 ) done

# \pnum not alone on a line.
grep -ne '^.\+\\pnum' $texfiles && exit 1
grep -ne '\\pnum.\+$' $texfiles && exit 1
# Fixup: sed '/\\pnum.\+$/s/\\pnum\s*/\\pnum\n/'

# \opt used incorrectly.
grep -n '\\opt[^{]' $texfiles && exit 1
grep -n 'opt{}' *.tex && exit 1

# Library element introducer followed by stuff.
grep -ne '^\\\(contraints\|mandates\|expects\|effects\|sync\|ensures\|returns\|throws\|complexity\|remarks\|errors\).\+$' $texfiles && exit 1
# Fixup: sed 's/^\\\(contraints\|mandates\|expects\|effects\|sync\|ensures\|returns\|throws\|complexity\|remarks\|errors\)\s*\(.\)/\\\1\n\2/'
# Fixup: sed 's/^\\ //'

# Change marker in [diff] followed by stuff.
grep -Hne '^\\\(change\|rationale\|effect\|difficulty\|howwide\)\s.\+$' compatibility.tex && exit 1
# Fixup: sed 's/^\\\(change\|rationale\|effect\|difficulty\|howwide\)\s\(.\)/\\\1\n\2/'q

# "template <class" (with space) in library clause.
grep -ne 'template\s<class' $texlib && exit 1

# \begin{example/note} with non-whitespace in front on the same line.
grep -ne '^.*[^ ]\s*\\\(begin\|end\){\(example\|note\)}' $texfiles && exit 1
# Fixup: sed 's/^\(.*[^ ]\)\s*\(\\\(begin\|end\){\(example\|note\)}\)/\1\n\2/'

# \begin/end{example/note} with stuff (except %) following on the same line.
grep -ne '\\\(begin\|end\){\(example\|note\)}[^%]\+$' $texfiles && exit 1
# Fixup: sed 's/\(\\\(begin\|end\){\(example\|note\)}\)\s*\([^ ].*\)$/\1\n\4/'

# Blank line between "begin example" and "begin codeblock"
for f in $texfiles; do
    sed -n '/\\begin{example}/{N;N;/\n\n\\begin{codeblock}$/{=;p}}' $f |
    # prefix output with filename and line
    sed '/^[0-9]\+$/{N;s/\n/:/}' | sed "s/.*/$f:&/"
done | grep . && exit 1
# Fixup: sed '/\\begin{example}/{N;s/\n$//}'

# Comment not aligned to multiple of four. (Ignore lines with "@".)
for f in $texfiles; do
    sed -n '/begin{codeblock}/,/end{codeblock}/{/^[^@]*[^ @][^@]*\/\//{=;p}}' $f |
    # prefix output with filename and line
    sed '/^[0-9]\+$/{N;s/\n/:/}' | sed "s/.*/$f:&/" |
    awk '{ match($0,"^[-a-z0-9]*\.tex:[0-9]*:"); n=match(substr($0,RLENGTH+1),"[ ;]//"); if (n % 4 != 0) print $0 " <--- comment starts in column " n; }'
done | grep . && exit 1

# Deleted special member function with a parameter name.
grep -n "&[ 0-9a-z_]\+) = delete" $texfiles && exit 1
# to fix: sed '/= delete/s/&[ 0-9a-z_]\+)/\&)/'

# \placeholder before (
#egrep 'placeholder{[-A-Za-z]*}@?\(' *.tex
# to fix: sed -i 's/placeholder\({[-A-Za-z]*}@\?(\)/placeholdernc\1/g' *.tex

# \placeholdernc before <
#egrep 'placeholdernc{[-A-Za-z]*}@?<' *.tex 
# to fix: sed -i 's/placeholdernc\({[-A-Za-z]*}@\?<\)/placeholder\1/g' *.tex 

# \placeholder before . or ,
# egrep 'placeholder{[-A-Za-z]*}@?[,.]' *.tex 
# to fix: sed -i 's/placeholder\({[-A-Za-z]*}@\?[.,]\)/placeholdernc\1/g' *.tex

exit 0
