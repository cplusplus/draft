#!/bin/bash

set -e

function usage () {
	echo "Usage: $0 old-commit new-commit"
	exit 1
}

BEFORE="$1"
AFTER="$2"

if [ -z $BEFORE ] ; then
	usage
fi

if [ -z $AFTER ] ; then
	usage
fi

mkdir before
mkdir after

git archive $BEFORE *.tex | tar xC before
git archive $AFTER *.tex | tar xC after 

for i in *.tex ; do
	latexdiff before/$i after/$i > $i
done

