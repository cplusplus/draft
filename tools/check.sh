#!/bin/bash

# Exit the script if any command (or pipeline) ends with an error
set -e

# Filter that exits the process if its input is non-empty.
# If $* args given, prefixes each line of input with "Error: $*: ".
fail() {
  awk -v str="$*" '/./ { if (length(str)) { print "Error: " str ": " $0 } } END { exit NR }'
}

# Ignore files where rules may be violated within macro definitions.
texfiles=$(ls *.tex | grep -v macros.tex | grep -v layout.tex | grep -v tables.tex)
texlibdesc="support.tex concepts.tex diagnostics.tex utilities.tex strings.tex containers.tex iterators.tex ranges.tex algorithms.tex numerics.tex time.tex locales.tex iostreams.tex regex.tex atomics.tex threads.tex"
texlib="lib-intro.tex $texlibdesc"

# Discover "Overfull \[hv]box" and "Reference ... undefined" messages from LaTeX.
sed -n '/\.tex/{s/^.*\/\([-a-z0-9]\+\.tex\).*$/\1/;h};
/Overfull [\\][hv]box\|LaTeX Warning..Reference/{x;p;x;p}' std.log |
sed '/^.\+\.tex$/{N;s/\n/:/}' | fail

# Find non-ASCII (Unicode) characters in the source
LC_ALL=C grep -ne '[^ -~	]' *.tex | fail "non-ASCII character"

# Trailing whitespace in a line.
grep -ne '\s$' *.tex | fail "trailing whitespace"

# Trailing empty lines
for f in *.tex; do [ $(tail -c 2 $f | wc -l) -eq 1 ] || (echo "$f has trailing empty lines"; exit 1 ) done

# indented \begin{codeblock} / \end{codeblock} (causes unwanted empty space)
grep -ne '^.\+\\\(begin\|end\){codeblock}' $texfiles | fail "indented codeblock env"

# \pnum not alone on a line.
grep -ne '^[^%]\+\\pnum' $texfiles | fail "pnum not alone on line"
grep -ne '\\pnum.\+$' $texfiles | fail "pnum not alone on line"
# Fixup: sed '/\\pnum.\+$/s/\\pnum\s*/\\pnum\n/'

# Two consecutive \pnum
for f in $texfiles; do
    awk 'prev == $0 && /^\\pnum/ { print FILENAME ":" FNR ": duplicate \\pnum on consecutive lines" } { prev = $0 }' $f
done | fail

# punctuation after the footnote marker
grep -n "\\end{footnote" $texfiles | grep -v '}[@)%]\?$' | fail "punctuation after footnote marker"

# \opt used incorrectly.
grep -n '\\opt[^{]' $texfiles | fail "\\\\opt used incorrectly"
grep -n 'opt{}' *.tex | fail "\\\\opt used incorrectly"

# Use \notdef instead of "not defined".
grep -n "// not defined" $texfiles | fail "use \\notdef instead"

# Library element introducer followed by stuff.
grep -ne '^\\\(constraints\|mandates\|expects\|effects\|sync\|ensures\|returns\|throws\|complexity\|remarks\|errors\).\+$' $texlibdesc | fail 'stuff after library element'
# Fixup: sed 's/^\\\(constraints\|mandates\|expects\|effects\|sync\|ensures\|returns\|throws\|complexity\|remarks\|errors\)\s*\(.\)/\\\1\n\2/'
# Fixup: sed 's/^\\ //'

# Change marker in [diff] followed by stuff.
grep -Hne '^\\\(change\|rationale\|effect\|difficulty\|howwide\)\s.\+$' compatibility.tex | fail "change marker in [diff] followed by stuff"
# Fixup: sed 's/^\\\(change\|rationale\|effect\|difficulty\|howwide\)\s\(.\)/\\\1\n\2/'q

# "template <class" (with space) in library clause.
grep -ne 'template\s<class' $texlib | fail 'space between "template" and "<class"'

# \begin{example/note} with non-whitespace in front on the same line.
grep -ne '^.*[^ ]\s*\\\(begin\|end\){\(example\|note\)}' $texfiles | fail "non-whitespace before note/example begins"
# Fixup: sed 's/^\(.*[^ ]\)\s*\(\\\(begin\|end\){\(example\|note\)}\)/\1\n\2/'

# \begin/end{example/note} with stuff (except %) following on the same line.
grep -ne '\\\(begin\|end\){\(example\|note\)}[^%]\+$' $texfiles | fail "content following note/example env"
# Fixup: sed 's/\(\\\(begin\|end\){\(example\|note\)}\)\s*\([^ ].*\)$/\1\n\4/'

# \end{note} or \end{example} at the end of a table cell
grep -n -A1 '\\end{\(example\|note\)}' $texfiles | grep -- '- *\(\\\\\|&\)' |
fail "needs tailnote or tailexample"

# Blank line between "begin example" and "begin codeblock"
for f in $texfiles; do
    sed -n '/\\begin{example}/{N;N;/\n\n\\begin{codeblock}$/{=;p}}' $f |
    # prefix output with filename and line
    sed '/^[0-9]\+$/{N;s/\n/:/}' | sed "s/.*/$f:&/"
done | fail 'blank line between "begin example" and "begin codeblock"'
# Fixup: sed '/\\begin{example}/{N;s/\n$//}'

# Comment not aligned to multiple of four. (Ignore lines with "@".)
for f in $texfiles; do
    sed -n '/begin{codeblock\(tu\)\?}/,/end{codeblock\(tu\)\?}/{/^[^@]*[^ @][^@]*\/\//{=;p}}' $f |
    # prefix output with filename and line
    sed '/^[0-9]\+$/{N;s/\n/:/}' | sed "s/.*/$f:&/" |
    awk '{ match($0,"^[-a-z0-9]*[.]tex:[0-9]*:"); n=match(substr($0,RLENGTH+1),"[ ;]//"); if (n % 4 != 0) print "Error: comment starts in column " n ": " $0; }'
done | fail

# Deleted special member function with a parameter name.
grep -n "&[ 0-9a-z_]\+) = delete" $texfiles | fail "named parameter in deleted special member"
# to fix: sed '/= delete/s/&[ 0-9a-z_]\+)/\&)/'

# Bad characters in label. "-" is allowed due to a single remaining offender.
grep -n '^\\rSec.\[[^]]*[^-a-z.0-9][^]]*\]{' $texfiles | fail 'bad character in label'

# "shall", "may", or "should" inside a note
for f in $texfiles; do
    sed -n '/begin{\(note\|footnote\)}/,/end{\(note\|footnote\)}/{/\(shall\|may\|should\)[^a-zA-Z]/{=;p}}' $f |
    # prefix output with filename and line
    sed '/^[0-9]\+$/{N;s/\n/:/}' | sed "s/.*/$f:&/"
done | fail '"shall", "should", or "may" inside a note'

# Hanging paragraphs
for f in $texfiles; do
    sed -n '/^\\rSec/{=;p};/^\\pnum/{s/^.*$/x/;=;p}' $f |
    # prefix output with filename and line
    sed '/^[0-9]\+$/{N;s/\n/:/}' | sed "s/.*/$f:&/" |
    awk -F: 'BEGIN { prevlevel = 0 } $3 ~ /^\\rSec./ { match($3, "[0-9]"); level=substr($3, RSTART, 1); if (text && level > prevlevel) { print prevsec " <-- Hanging paragraph follows" } prevlevel = level; prevsec = $3; text = 0 } $3 == "x" { text = 1 }'
done | fail "hanging paragraph"

# Subclauses without siblings
for f in $texfiles; do
    sed -n '/^\\rSec/{=;p}' $f |
    # prefix output with filename and line
    sed '/^[0-9]\+$/{N;s/\n/:/}' | sed "s/.*/$f:&/" |
    awk -F: 'BEGIN { prevlevel = 0 }
      {
	match($3, "[0-9]");
	level = substr($3, RSTART, 1);
	if (level < prevlevel && secs[prevlevel] == 1) { print title[prevlevel] " <-- Subclause without siblings" }
	++secs[level];
	title[level] = $0;
	secs[level + 1] = 0;
	prevlevel = level;
      }'
done | fail


# Library descriptive macros not immediately preceded by \pnum.
for f in $texlibdesc; do
    sed -n '/^\\pnum/{h;:x;n;/^\\index/b x;/^\\\(constraints\|mandates\|expects\|effects\|sync\|ensures\|returns\|throws\|complexity\|remarks\|errors\)/{x;/\n/{x;=;p};d};/^\\pnum/D;H;b x}' $f |
    # prefix output with filename and line
    sed '/^[0-9]\+$/{N;s/\n/:/}' | sed "s/.*/$f:&/"
done | fail "pnum missing"

# Cross-references pointing to their own section.
for f in $texfiles; do
    sed -n '/^\\rSec/{s/^.rSec.\[/S /;s/\].*$//;=;p};/\\iref{/{s/^.*\\.\?ref{\([-a-z.0-9]\+\)}.*/R \1/g;=;p}' $f |
    sed '/^[0-9]\+$/{N;s/\n/: /}' | sed "s/.*/$f:&/" |
    awk '$2 == "S" { seclabel = $3 } $2 == "R" && $3 == seclabel { print $1 " section self-reference to [" $3 "]" }'
done | fail "cross-ref to its own section"

# \placeholder before (
#egrep 'placeholder{[-A-Za-z]*}@?\(' *.tex
# to fix: sed -i 's/placeholder\({[-A-Za-z]*}@\?(\)/placeholdernc\1/g' *.tex

# \placeholdernc before <
#egrep 'placeholdernc{[-A-Za-z]*}@?<' *.tex
# to fix: sed -i 's/placeholdernc\({[-A-Za-z]*}@\?<\)/placeholder\1/g' *.tex

# \placeholder before . or ,
# egrep 'placeholder{[-A-Za-z]*}@?[,.]' *.tex
# to fix: sed -i 's/placeholder\({[-A-Za-z]*}@\?[.,]\)/placeholdernc\1/g' *.tex

# We can't reliably check if the PDF is up to date, because we don't have a
# deterministic rebuild process, and different versions of dot produce
# different files anyway. So just check the timestamp.
for f in *.dot; do
  if [ "$f" -nt "${f%.dot}.pdf" ]; then
    echo -e "need to rebuild ${f%.dot}.pdf:\nmake clean-figures && make figures" >&2
    exit 1
  fi
done

# Cross references since the previous standard.
function indexentries() { sed 's,\\glossaryentry{\(.*\)@.*,\1,' "$1" | LANG=C sort; }
function removals() { diff -u "$1" "$2" | grep '^-' | grep -v '^---' | sed 's/^-//'; }
function difference() { diff -u "$1" "$2" | grep '^[-+]' | grep -v '^\(---\|+++\)'; }
XREFDELTA="$(difference <(indexentries xrefdelta.glo) <(removals <(indexentries xrefprev) <(indexentries xrefindex.glo)) ; true)"
if [ -n "$XREFDELTA" ]; then
  echo "incorrect entries in xrefdelta.tex:" >&2
  echo "$XREFDELTA" | sed 's,^-,spurious ,; s,^+,missing ,;' >&2
  exit 1
fi

exit 0
