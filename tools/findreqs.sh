#!/bin/bash
# Finds instances of requirements (like CopyConstructible) that are not formatted correctly.

requirements="EqualityComparable LessThanComparable DefaultConstructible MoveConstructible CopyConstructible MoveAssignable CopyAssignable Destructible Swappable NullablePointer ValueSwappable"
# These have too many false positive
more_requirements="Hash Allocator"

for req in $requirements ; do
	grep "\\<$req\\>" *.tex | grep -v "\\tcode{$req}" | grep -v "\\idxcode{$req}"
done