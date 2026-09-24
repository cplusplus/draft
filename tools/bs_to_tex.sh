#!/bin/bash

itemize=0
empty=0

sed -e 's,<pre>,\\begin{itemdecl},g' \
    -e 's,</pre>,\\end{itemdecl},g' \
    -e 's,</\?blockquote>,,g' \
    -e 's,</\?code>,`,g' \
    -e 's,// exposition only,// \\expos,g' \
    -e 's,<i>implementation-defined</i>,@\\impdefx{TODO}@,g' \
    -e 's,<i>see below</i>,@\\seebelow@,g' \
    -e 's,concept <i>\([a-z]\+-[a-z-]\+\)</i>,concept @\\defexposconcept{\1}@,g' \
    -e 's,<i>\([a-z]\+-[a-z-]\+\)</i>,@\\exposid{\1}@,g' \
    -e 's,<i>Constraints</i>:,\\pnum\n\\constraints,g' \
    -e 's,<i>Effects</i>:,\\pnum\n\\effects,g' \
    -e 's,<i>Mandates</i>:,\\pnum\n\\mandates,g' \
    -e 's,<i>Preconditions</i>:,\\pnum\n\\expects,g' \
    -e 's,<i>Remarks</i>:,\\pnum\n\\remarks,g' \
    -e 's,<i>Returns</i>:,\\pnum\n\\returns,g' \
    -e 's,<i>Throws</i>:,\\pnum\n\\throws,g' \
    -e 's,</\?i>,,g' \
    -e 's,&lt;,<,g' \
    -e 's,`i`<sup>th</sup>,#iiiiiiiiith#,g' \
    -e 's,`i`,i,g' \
    -e 's,// \[\([.a-z]\+\)],// \\ref{\1},g' \
    -e 's, *(\[\([.a-z]\+\)]),\\iref{\1},g' \
    -e 's,\<i\>,$i$,g' \
    -e 's,#iiiiiiiiith#,$i^\\text{th}$,g' \
    -e 's,`\[\([^\,]\+\)\, *\([^`]\+\))`,\\range{\1}{\2},' \
    -e 's,`\[\([^\,]\+\)\, *\([^`]\+\)]`,\\crange{\1}{\2},' \
    -e 's,`\([^`]\+\)`,\\tcode{\1},g' \
    $1 | while IFS='' read -r line; do
    if [[ "$line" =~ ^-  ]]; then
      if ((!itemize)); then
        itemize=1
        echo -E '\begin{itemize}'
      fi
      echo -E "\item${line#-}"
      continue
    elif ((itemize)); then
      echo -E '\end{itemize}'
      itemize=0
    elif [[ -z "$line" ]]; then
      ((empty)) && continue
      empty=1
    elif ((empty)); then
      empty=0
    fi
    echo -E "$line"
  done
