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


TEXTCMDS=tcode,term,grammarterm,techterm,defnx,defn,Fundescx,Fundesc,state,leftshift,EnterBlock,ExitBlock,NTS,EXPO,impdefx,UNSP,xname,mname,diffdef,stage,doccite,cvqual,numconst,logop
SAFECMDS=Rplus,Cpp,CppIII,opt,shl,shr,dcr,exor,bigoh,tilde,bitand,bitor,xor,rightshift,enternote,enterexample,exitexample,required,requires,effects,postconditions,postcondition,preconditions,precondition,returns,throws,default,complexity,remark,remarks,note,notes,realnote,realnotes,errors,sync,implimits,replaceable,exceptionsafety,returntype,cvalue,ctype,ctypes,dtype,ctemplate,templalias,xref,xsee,ntbs,ntmbs,ntwcs,ntcxvis,ntcxxxiis,expos,impdef,notdef,unspec,unspecbool,seebelow,unspecuniqtype,unspecalloctype,unun,change,rationale,effect,difficulty,howwide,uniquens,cv
for i in *.tex ; do
	latexdiff --append-textcmd=$TEXTCMDS --append-safecmd=$SAFECMDS -c PICTUREENV='(?:picture|DIFnomarkup|codeblock)[\w\d*@]*' before/$i after/$i > $i
done

