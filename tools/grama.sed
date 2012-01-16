# remove index "see" entries
/\\index.*|see/d

# insert newlines after groups
/\\end/s/\(.*\)/\1\
/
