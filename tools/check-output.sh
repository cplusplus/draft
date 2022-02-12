#!/bin/bash

# This script checks the results of the LaTeX run.

failed=0

function fail() {

    # echo "::error file=app.js,line=10,col=15::Something went wrong"

    ! sed 's/^\(.\+\.tex\):/file=\1::/;s/^/::error /' | grep .
}


# Discover "Overfull \[hv]box" and "Reference ... undefined" messages from LaTeX.
sed -n '/\.tex/{s/^.*\/\([-a-z0-9]\+\.tex\).*$/\1/;h};
/Overfull [\\][hv]box\|LaTeX Warning..Reference/{x;p;x;p}' std.log |
    sed '/^.\+\.tex$/{N;s/\n/:/}' | fail || failed=1

# Check for dangling "see" in general index (does not work with formatting)
grep item < std-generalindex.ind | sed 's/,.*$//;s/\\[sub]*item //' |
    awk '/^  [^ ]/ { item=$0; print $0 }  /^    [^ ]/ { subitem=$0; print item ", " $0 } /^      [^ ]/ { print item ", " subitem ", " $0 }' |
    sed 's/^ *//;s/  */ /g' | sort > tmp.txt

grep -o '\\see{[^}]*}' < std-generalindex.ind |
    sed 's/^\\see{//;s/}$//;s/\\-//' |
    grep -v "leavevmode\|texttt\|textsc\|kern" |
    while read see; do
	if grep -q "$see" tmp.txt; then
	    :
	else
	    grep -n "see{$see}" *.tex | sed 's/$/ is dangling/'
	fi
    done | fail || failed=1
rm -f tmp.txt

# Find grammar index entries missing a definition
cat std-grammarindex.ind |
    awk 'BEGIN { def=1 } /^  .item/ { if (def==0) { gsub("[{},]", "", item); print item } item=$NF; def=0; next } /hyperindexformat/ { def=1 }' |
    grep -v -- '-keyword$' |    # xxx-keyword is special
    sed 's/^\(.*\)$/grammar non-terminal \1 has no definition/' |
    fail || failed=1

# Cross references since the previous standard.
function indexentries() { sed 's,\\glossaryentry{\(.*\)@.*,\1,' "$1" | LANG=C sort; }
function removals() { diff -u "$1" "$2" | grep '^-' | grep -v '^---' | sed 's/^-//'; }
function difference() { diff -u "$1" "$2" | grep '^[-+]' | grep -v '^\(---\|+++\)'; }
XREFDELTA="$(difference <(indexentries xrefdelta.glo) <(removals <(indexentries xrefprev) <(indexentries xrefindex.glo)))"
if [ -n "$XREFDELTA" ]; then
  echo "incorrect entries in xrefdelta.tex:" >&2
  echo "$XREFDELTA" | sed 's,^-,spurious ,; s,^+,missing ,;' >&2
  failed=1
fi

exit $failed
