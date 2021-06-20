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
