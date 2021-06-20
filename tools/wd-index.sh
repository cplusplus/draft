#!/bin/sh

# Create index of Working Drafts with links

baseurl="http://www.open-std.org/jtc1/sc22/wg21/docs/papers"

echo "# Index of C++ Working Drafts"
echo ""
git tag --list 'n*' |
while read tag; do
    paper=`echo $tag | tr n N`
    date=`git show  --format=%as --no-patch $tag | tail -1`
    year=`echo $date | cut -d- -f1`
    month=`echo $date | cut -d- -f2`
    echo " * [$paper]($baseurl/$year/$tag.pdf) $year-$month C++ Working Draft"
done
