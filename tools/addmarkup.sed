# Adds LaTeX markup to HTML documents
# 
# Supports the kind of HTML markup used by the Core Working Group.
#
# To use this, run something like
#   gsed -f addmarkup.sed < cwg-active.html > out.html
#
# Note: requires GNU sed. On Mac OS X, "brew install gnu-sed" if you have Homebrew.

# Skip headings
/^<H3>.*<\/H3>$/I b

# Add the stylesheet
s,<HEAD>,<HEAD><style type="text/css">.latex {color: #444444; background: #dddddd; font-family: monospace; }</style>,i

# Inline code
s,<TT>,<span class="latex">\\tcode{</span><TT>,gi
s,</TT>,</TT><span class="latex">}</span>,gi

# Bullets
#
# Disabled for now, since these don't interact very well with bnf grammars and things
#
# s,<UL>,<span class="latex">\\begin{itemize}</span><UL>,gi
# s,<LI>,<LI><span class="latex">\\item</span>,gi
# s,</UL>,</UL><span class="latex">\\end{itemize}</span>,gi

# Notes and examples
s,\[<I>Note:</I>,<span class="latex">\\enternote</span>,gi
s,&#8212;<I>end note</I>\],<span class="latex">\\exitnote</span>,gi
s,\[<I>Example:</I>,<span class="latex">\\enterexample</span>,gi
s,&#8212;<I>end example</I>\],<span class="latex">\\exitexample</span>,gi

# Footnotes
s,<I>\[Footnote:</I>,<span class="latex">\\footnote{</span>,gi
s,\[<I>Footnote:</I>,<span class="latex">\\footnote{</span>,gi
s,&#8212;<I>end footnote</I>],<span class="latex">}</span>,gi

# References
s,([0-9.]\+ \[\([a-z.]\+\)\]),<span class="latex">~(\\ref{\1})</span>,gi

# Code blocks
s,<PRE>,<span class="latex">\\begin{codeblock}</span><PRE>,gi
s,</PRE>,</PRE><span class="latex">\\end{codeblock}</span>,gi

# Grammar terms
# I generated this list with
#  cat ../source/grammar.tex  | grep nontermdef | sed 's,\\nontermdef{\([a-z_0-9-]*\)}.*,\1,' | tr '\n' '|'
s,<I>\(hex-quad\|universal-character-name\|preprocessing-token\|token\|header-name\|h-char-sequence\|h-char\|q-char-sequence\|q-char\|pp-number\|identifier\|identifier-nondigit\|nondigit\|digit\|preprocessing-op-or-punc\|literal\|integer-literal\|decimal-literal\|octal-literal\|hexadecimal-literal\|binary-literal\|nonzero-digit\|octal-digit\|hexadecimal-digit\|binary-digit\|integer-suffix\|unsigned-suffix\|long-suffix\|long-long-suffix\|character-literal\|c-char-sequence\|c-char\|escape-sequence\|simple-escape-sequence\|octal-escape-sequence\|hexadecimal-escape-sequence\|floating-literal\|fractional-constant\|exponent-part\|sign\|digit-sequence\|floating-suffix\|string-literal\|encoding-prefix\|s-char-sequence\|s-char\|raw-string\|r-char-sequence\|r-char\|d-char-sequence\|d-char\|boolean-literal\|pointer-literal\|user-defined-literal\|user-defined-integer-literal\|user-defined-floating-literal\|user-defined-string-literal\|user-defined-character-literal\|ud-suffix\|translation-unit\|primary-expression\|id-expression\|unqualified-id\|qualified-id\|nested-name-specifier\|lambda-expression\|lambda-introducer\|lambda-capture\|capture-default\|capture-list\|capture\|simple-capture\|init-capture\|lambda-declarator\|postfix-expression\|expression-list\|pseudo-destructor-name\|unary-expression\|unary-operator\|new-expression\|new-placement\|new-type-id\|new-declarator\|noptr-new-declarator\|new-initializer\|delete-expression\|noexcept-expression\|cast-expression\|pm-expression\|multiplicative-expression\|additive-expression\|shift-expression\|relational-expression\|equality-expression\|and-expression\|exclusive-or-expression\|inclusive-or-expression\|logical-and-expression\|logical-or-expression\|conditional-expression\|assignment-expression\|assignment-operator\|expression\|constant-expression\|statement\|labeled-statement\|expression-statement\|compound-statement\|statement-seq\|selection-statement\|condition\|iteration-statement\|for-init-statement\|for-range-declaration\|for-range-initializer\|jump-statement\|declaration-statement\|declaration-seq\|declaration\|block-declaration\|alias-declaration\|simple-declaration\|static_assert-declaration\|empty-declaration\|attribute-declaration\|decl-specifier\|decl-specifier-seq\|storage-class-specifier\|function-specifier\|typedef-name\|type-specifier\|trailing-type-specifier\|type-specifier-seq\|trailing-type-specifier-seq\|simple-type-specifier\|type-name\|decltype-specifier\|elaborated-type-specifier\|enum-name\|enum-specifier\|enum-head\|opaque-enum-declaration\|enum-key\|enum-base\|enumerator-list\|enumerator-definition\|enumerator\|namespace-name\|original-namespace-name\|namespace-definition\|named-namespace-definition\|original-namespace-definition\|extension-namespace-definition\|unnamed-namespace-definition\|namespace-body\|namespace-alias\|namespace-alias-definition\|qualified-namespace-specifier\|using-declaration\|using-directive\|asm-definition\|linkage-specification\|attribute-specifier-seq\|attribute-specifier\|alignment-specifier\|attribute-list\|attribute\|attribute-token\|attribute-scoped-token\|attribute-namespace\|attribute-argument-clause\|balanced-token-seq\|balanced-token\|init-declarator-list\|init-declarator\|declarator\|ptr-declarator\|noptr-declarator\|parameters-and-qualifiers\|trailing-return-type\|ptr-operator\|cv-qualifier-seq\|cv-qualifier\|ref-qualifier\|declarator-id\|type-id\|abstract-declarator\|ptr-abstract-declarator\|noptr-abstract-declarator\|abstract-pack-declarator\|noptr-abstract-pack-declarator\|parameter-declaration-clause\|parameter-declaration-list\|parameter-declaration\|function-definition\|initializer\|brace-or-equal-initializer\|initializer-clause\|initializer-list\|braced-init-list\|class-name\|class-specifier\|class-head\|class-head-name\|class-virt-specifier\|class-key\|member-specification\|member-declaration\|member-declarator-list\|member-declarator\|virt-specifier-seq\|virt-specifier\|pure-specifier\|base-clause\|base-specifier-list\|base-specifier\|class-or-decltype\|base-type-specifier\|access-specifier\|conversion-function-id\|conversion-type-id\|conversion-declarator\|ctor-initializer\|mem-initializer-list\|mem-initializer\|mem-initializer-id\|operator-function-id\|operator\|literal-operator-id\|template-declaration\|template-parameter-list\|template-parameter\|type-parameter\|simple-template-id\|template-id\|template-name\|template-argument-list\|template-argument\|typename-specifier\|explicit-instantiation\|explicit-specialization\|try-block\|function-try-block\|handler-seq\|handler\|exception-declaration\|throw-expression\|exception-specification\|dynamic-exception-specification\|type-id-list\|noexcept-specification\|preprocessing-file\|group\|group-part\|if-section\|if-group\|elif-groups\|elif-group\|else-group\|endif-line\|control-line\|text-line\|non-directive\|lparen\|identifier-list\|replacement-list\|pp-tokens\|new-line\)</I>,<span class="latex">\\grammarterm{</span><I>\1</I><span class="latex">}</span>,gi

