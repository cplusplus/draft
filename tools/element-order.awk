#!/usr/bin/awk -f

BEGIN {
    items = "constraints  mandates  expects  effects  sync  ensures  returns  throws  complexity  remarks  errors"
    linematch = "^[\\\\](" items ")"
    gsub(/  /, "|", linematch)
    items = " " items
    # print linematch
}

/^.begin{itemdescr}/ {
    elements = ""
    startline = FNR
    check = 1
    if (/% NOCHECK:.* order/) {
	check = 0
    }
}

/^.end{itemdescr}/ {
    if (check && length(elements) > 0) {
	regex = substr(elements, 2)
	gsub(/ /, " .* ", regex)
	if (items !~ regex) {
	    printf "%s:%d-%d: bad element ordering: %s\n", FILENAME, startline, FNR, elements
	}
    }
}

match ($0, linematch) > 0 {
    elements = elements " " substr($0, 2)
}
