# process ordinary section headers
s/^\\rSec[[:digit:]]\[\([^]]*\)\].*$/\1 xref/p

# process definitions
s/^\\definition{[^}]*}{\([^}]*\)}.*$/\1 xref/p

# process informative annex headers
s/^\\infannex{\([^}]*\)}.*$/\1 xref/p

# process normative annex headers
s/^\\normannex{\([^}]*\)}.*$/\1 xref/p
