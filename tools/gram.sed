# extract lines marked with '%gram:'
/^%gram:/s/^%gram:[[:space:]]*//p

# copy bnftab groups:
/^\\begin{bnftab}/,/^\\end{bnftab}/p

# copy simplebnf groups:
/^\\begin{simplebnf}/,/^\\end{simplebnf}/p

# copy bnf groups:
/^\\begin{bnf}/,/^\\end{bnf}/p

# copy bnfkeywordtab groups:
/^\\begin{bnfkeywordtab}/,/^\\end{bnfkeywordtab}/p
