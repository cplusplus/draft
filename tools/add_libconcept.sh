#!/bin/bash

usage() {
  cat <<EOF
Usage: $0 <LaTeX source>

Greedy application of \\libconcept and \\exposconcept macros to anything that
looks like a concept.
EOF
}

case "$1" in
  -h|--help|"")
    usage
    exit 1
    ;;
esac

source_dir="${0%/*}/../source"

concepts=$(grep -oh 'deflibconcept{[a-z_:]*}' "$source_dir"/*.tex \
  | sed -e 's/^deflibconcept{\(.*\)}$/\1/' \
  | sed -e ':a; N; $!ba; s/\n/\\|/g'
)

exposconcepts=$(grep -oh 'defexposconceptn\?c\?{[a-z-]*}' "$source_dir"/*.tex \
  | sed -e 's/^defexposconceptn\?c\?{\(.*\)}$/\1/' \
  | sed -e ':a; N; $!ba; s/\n/\\|/g'
)

sed -e 's,\([^\\{.-]\)\<\('"$concepts"'\)\>\([^-]\),\1@\\libconcept{\2}@\3,g' \
  -e 's,\([^\\{.-]\)\<\('"$exposconcepts"'\)\>\([^-]\),\1@\\exposconcept{\2}@\3,g' \
  -e 's,\\exposid\(nc\)\?{\('"$concepts"'\)},\\libconcept{\2},g' \
  -e 's,\\exposid\(nc\)\?{\('"$exposconcepts"'\)},\\exposconcept\1{\2},g' \
  -e 's,\<\(The\|the\|or\|valid\|supplied\) @\\libconcept{range}@,\1 range,g' \
  -e 's,\<\(The\|the\|following\|equivalence\) @\\libconcept{relation}@,\1 relation,g' \
  -e 's,\<\(The\|the\|calling\) @\\libconcept{regular}@,\1 regular,g' \
  -e 's,\<\(trivially\) @\\libconcept{copyable}@,\1 copyable,g' \
  -e 's,@\\libconcept{integral}@ \(promotion\|value\|of\|constant\|constants\|type\|types\)\>,integral \1,g' \
  -e 's,@\\libconcept{view}@ \(the\|of\)\>,view \1,g' \
  "$@"
