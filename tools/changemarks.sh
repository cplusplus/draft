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
	latexdiff --append-textcmd=tcode,term,grammarterm,techterm,defnx,defn --append-safecmd=Rplus,Cpp,CppIII,opt,shl,shr,dcr,exor,bigoh,tilde -c PICTUREENV='(?:picture|DIFnomarkup|codeblock)[\w\d*@]*' before/$i after/$i > $i
done

