#!/usr/bin/env python3

from __future__ import annotations

import argparse
import fnmatch
import os
import re
import sys
import unicodedata
from abc import ABC
from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Pattern, Set, Tuple


# ==================================================================================================
# Lookup tables
# ==================================================================================================

# Remember to keep this in sync with [structure.specifications] and our set of macros.
# The order matters for ElementOrderCheck.
FUNCTION_DESCRIPTORS = [
    "constraints",  # Constraints
    "mandates",  # Mandates
    "constantwhen",  # Constant When
    "expects",  # Preconditions
    "hardexpects",  # Hardened preconditions
    "effects",  # Effects
    "sync",  # Synchronization
    "ensures",  # Postconditions
    "returns",  # Returns
    "throws",  # Throws
    "complexity",  # Complexity
    "remarks",  # Remarks
    "errors",  # Error conditions
]

# All library descriptors.
# The order doesn't matter; this list is used for checking whether e.g. `\recommended`
# is preceded by `\pnum`
PARAGRAPH_DESCRIPTORS = [
    *FUNCTION_DESCRIPTORS,
    "recommended",  # Recommended practice
    "required",  # Required behavior
    "implimits",  # Implementation limits
    "returntype",  # Return type
    "ctype",  # Type
    "templalias",  # Alias template
]

DIFF_DESCRIPTORS = [
    "change",
    "rationale",
    "effect",
    "difficulty",
    "howwide",
]

KNOWN_COMMANDS = {
    "0",
    "Annex",
    "BODY",
    "BnfInc",
    "BnfIndent",
    "BnfNontermshape",
    "BnfReNontermshape",
    "BnfRest",
    "BnfTermshape",
    "BreakableUnderscore",
    "CodeBlockSetup",
    "CodeStyle",
    "CodeStylex",
    "CodeStylexGuarded",
    "Cpp",
    "CppIII",
    "CppXI",
    "CppXIV",
    "CppXVII",
    "CppXX",
    "CppXXIII",
    "CppXXVI",
    "D",
    "DeclareCaptionLabelSeparator",
    "DeclareMathOperator",
    "DisableLigatures",
    "EXPO",
    "ExplSyntaxOff",
    "ExplSyntaxOn",
    "Fundesc",
    "Fundescx",
    "Gamma",
    "GrammarStylex",
    "Head",
    "Huge",
    "IsoC",
    "IsoCUndated",
    "IsoFloatUndated",
    "IsoPosix",
    "IsoPosixUndated",
    "LARGE",
    "Large",
    "N",
    "NTS",
    "NewDocumentCommand",
    "NewEnviron",
    "OldTextAsciiTilde",
    "Pi",
    "RSsmallest",
    "Range",
    "S",
    "Sec",
    "Sigma",
    "StrClosingbrace",
    "StrSubstitute",
    "StrTextsc",
    "StrTextsmaller",
    "The",
    "U",
    "UAX",
    "UNSP",
    "UNSPnc",
    "W",
    "a",
    "abovecaptionskip",
    "addcontentsline",
    "added",
    "addednb",
    "addtocontents",
    "addtocounter",
    "addtolength",
    "addxref",
    "advance",
    "afterchapskip",
    "afterchapternum",
    "afterskip",
    "aliaspagestyle",
    "allowbreak",
    "alpha",
    "annexlabel",
    "annexnumberlinebox",
    "appendix",
    "appendixname",
    "arabic",
    "atsign",
    "b",
    "backmatter",
    "backslash",
    "bar",
    "baselineskip",
    "beforechapskip",
    "beforeskip",
    "begin",
    "begingroup",
    "belowcaptionskip",
    "beta",
    "bfseries",
    "bgroup",
    "bibitem",
    "bibname",
    "big",
    "bigl",
    "bigoh",
    "bigr",
    "bigskip",
    "binom",
    "bitand",
    "bitor",
    "bm",
    "bmod",
    "bnfindent",
    "bnfindentfirst",
    "bnfindentinc",
    "bnfindentrest",
    "bot",
    "bottomline",
    "br",
    "brange",
    "break",
    "brk",
    "c",
    "capsep",
    "caption",
    "captionsetup",
    "caret",
    "cdot",
    "cdots",
    "cedef",
    "centering",
    "cftsetindents",
    "change",
    "changed",
    "changednb",
    "changeglossnumformat",
    "chapnamefont",
    "chapnumfont",
    "chapter",
    "chaptermark",
    "chaptername",
    "chapternamenum",
    "chapternumberlinebox",
    "chapterstyle",
    "chaptitlefont",
    "char",
    "chdr",
    "chdrx",
    "checkandfixthelayout",
    "cite",
    "clauselabel",
    "clearpage",
    "cline",
    "clist",
    "closeout",
    "clubpenalty",
    "cname",
    "colhdr",
    "color",
    "columnbreak",
    "commentellip",
    "complexity",
    "constantwhen",
    "constraints",
    "contentsname",
    "continuedcaption",
    "copyboxwidth",
    "copypagestyle",
    "copyright",
    "cos",
    "countedrange",
    "counterwithin",
    "counterwithout",
    "cppver",
    "cptn",
    "crange",
    "cs",
    "ctype",
    "customlabel",
    "cv",
    "cvqual",
    "d",
    "def",
    "default",
    "defexposconcept",
    "defexposconceptnc",
    "definecolor",
    "definition",
    "deflibconcept",
    "defn",
    "defnadj",
    "defnadjx",
    "defncontext",
    "defnlibxname",
    "defnnewoldconcept",
    "defnoldconcept",
    "defnx",
    "defnxname",
    "delta",
    "deprxref",
    "descr",
    "diffdef",
    "diffhead",
    "difficulty",
    "diffref",
    "diffrefs",
    "discretionary",
    "displaystyle",
    "do",
    "doccite",
    "docno",
    "documentclass",
    "doindexescape",
    "doneindexescape",
    "dotsb",
    "dotsc",
    "ecname",
    "edef",
    "ednote",
    "effect",
    "effectafteritemize",
    "effects",
    "egroup",
    "ell",
    "else",
    "emergencystretch",
    "emph",
    "end",
    "endfirsthead",
    "endgroup",
    "endhead",
    "endmulticols",
    "ensuremath",
    "ensures",
    "eqref",
    "equiv",
    "errors",
    "everypar",
    "exp",
    "expandafter",
    "expects",
    "expos",
    "exposconcept",
    "exposconceptnc",
    "exposconceptx",
    "exposid",
    "exposidnc",
    "f",
    "fakegrammarterm",
    "fbox",
    "fboxrule",
    "fboxsep",
    "feetatbottom",
    "fi",
    "figurerefname",
    "fill",
    "firstlibchapter",
    "fmtgrammarterm",
    "fmtnontermdef",
    "foo",
    "footmarkstyle",
    "footnote",
    "footnotemark",
    "footnotesize",
    "footnotetext",
    "frac",
    "fref",
    "frenchspacing",
    "frontmatter",
    "g",
    "gamma",
    "ge",
    "geq",
    "global",
    "glossary",
    "glossaryname",
    "glossitem",
    "glue",
    "gramSec",
    "gramWrite",
    "grammarterm",
    "grammartermnc",
    "gramout",
    "gterm",
    "hangpara",
    "hardexpects",
    "hbox",
    "hd",
    "hdstyle",
    "hdwidth",
    "hfill",
    "hline",
    "howwide",
    "hrule",
    "hsize",
    "hspace",
    "hss",
    "hyperpage",
    "hyperref",
    "hypersetup",
    "hypertarget",
    "hyphenation",
    "idxCpp",
    "idxbfpage",
    "idxcode",
    "idxconcept",
    "idxexposconcept",
    "idxgram",
    "idxhdr",
    "idxmname",
    "idxnewoldconcept",
    "idxoldconcept",
    "idxterm",
    "idxxname",
    "if",
    "ifcase",
    "iffalse",
    "ifhmode",
    "ifinner",
    "ifmmode",
    "ifnum",
    "iftrue",
    "ifvmode",
    "ifx",
    "immediate",
    "impdef",
    "impdefnc",
    "impdefx",
    "impldef",
    "impldefplain",
    "impldefrootname",
    "implimits",
    "importexample",
    "include",
    "includegraphics",
    "index",
    "indexconcept",
    "indexcont",
    "indexdefn",
    "indexescape",
    "indexgram",
    "indexgrammar",
    "indexhdr",
    "indexheader",
    "indeximpldef",
    "indexlibrary",
    "indexlibraryboth",
    "indexlibraryctor",
    "indexlibrarydtor",
    "indexlibraryglobal",
    "indexlibrarymember",
    "indexlibrarymemberexpos",
    "indexlibrarymemberx",
    "indexlibrarymisc",
    "indexlibraryzombie",
    "indexname",
    "indexoff",
    "indexordmem",
    "indextext",
    "indexunordmem",
    "infannex",
    "infty",
    "input",
    "int",
    "iref",
    "isocopyright",
    "itcorr",
    "itcorrwidth",
    "item",
    "itletterwidth",
    "itshape",
    "kern",
    "keyword",
    "kill",
    "l",
    "label",
    "labelitemi",
    "labelitemii",
    "labelitemiii",
    "labelitemiv",
    "labelsep",
    "lambda",
    "land",
    "large",
    "larger",
    "lastcorechapter",
    "lastlibchapter",
    "lbl",
    "lceil",
    "ldots",
    "le",
    "leaders",
    "leavevmode",
    "left",
    "leftmargin",
    "leftmargini",
    "leftmark",
    "leftshift",
    "leq",
    "let",
    "lfloor",
    "lhdr",
    "lhdrx",
    "libconcept",
    "libconceptx",
    "libdeprheaderref",
    "libglobal",
    "libheader",
    "libheaderdef",
    "libheaderref",
    "libheaderrefx",
    "libheaderrefxx",
    "libheaderx",
    "libmacro",
    "libmember",
    "libnoheader",
    "libreqtabenv",
    "libspec",
    "libxmacro",
    "lim",
    "linebreak",
    "listing",
    "listparindent",
    "ln",
    "locgrammarterm",
    "locnontermdef",
    "log",
    "logop",
    "lor",
    "lst",
    "lstdefinelanguage",
    "lsthk",
    "lstnewenvironment",
    "lstsaved",
    "lstset",
    "m",
    "mainmatter",
    "makeatletter",
    "makeatother",
    "makebox",
    "makechapterstyle",
    "makeevenfoot",
    "makeevenhead",
    "makeglossary",
    "makeheadrule",
    "makeindex",
    "makeoddfoot",
    "makeoddhead",
    "makepagestyle",
    "makepsmarks",
    "mandates",
    "mapsto",
    "markboth",
    "mathbin",
    "mathit",
    "mathop",
    "mathrel",
    "mathrm",
    "mathscr",
    "mathsf",
    "mathtt",
    "max",
    "maxsecnumdepth",
    "maybeaddpnum",
    "mbox",
    "meaning",
    "meaningbody",
    "microtypesetup",
    "min",
    "mname",
    "mod",
    "movedxref",
    "movedxrefii",
    "movedxrefiii",
    "movedxrefs",
    "mu",
    "mulhi",
    "mullo",
    "multicols",
    "multicolumn",
    "n",
    "nb",
    "nbc",
    "nc",
    "neq",
    "newcolumntype",
    "newcommand",
    "newcounter",
    "newenvironment",
    "newlabel",
    "newlength",
    "newline",
    "newlist",
    "newnoteenvironment",
    "newoldconcept",
    "newpage",
    "newsavebox",
    "newsubclausecounter",
    "newwrite",
    "nobreak",
    "nocode",
    "nocontentsline",
    "nocorr",
    "nodiffref",
    "noexpand",
    "noindent",
    "nolinebreak",
    "nonfrenchspacing",
    "nontermdef",
    "normalbaselines",
    "normalbaselineskip",
    "normalcolor",
    "normalfont",
    "normalsize",
    "normannex",
    "notdef",
    "noteintro",
    "noteoutro",
    "ntbs",
    "ntcxvis",
    "ntcxxxiis",
    "ntmbs",
    "ntwcs",
    "nu",
    "numberwithin",
    "numconst",
    "oBreakableUnderscore",
    "oCpp",
    "oexposid",
    "ogrammarterm",
    "ohdr",
    "ohdrx",
    "oindex",
    "oldconcept",
    "oldconceptname",
    "oldcontentsline",
    "oldxref",
    "omname",
    "onelineskip",
    "openout",
    "operatorname",
    "opt",
    "or",
    "orange",
    "otcode",
    "otextup",
    "otherwise",
    "overline",
    "pagebreak",
    "pagestyle",
    "par",
    "parabullnum",
    "paragraph",
    "paragraphmark",
    "parindent",
    "parshape",
    "parskip",
    "partopsep",
    "pdfbookmark",
    "pdfcolorstack",
    "pdfcompresslevel",
    "pdfminorversion",
    "pdfobjcompresslevel",
    "pdfstringdefDisableCommands",
    "penalty",
    "phantom",
    "phantomsection",
    "phi",
    "pi",
    "placeholder",
    "placeholdernc",
    "pnum",
    "preglossaryhook",
    "preindexhook",
    "prevdocno",
    "prime",
    "printchapternum",
    "printglossary",
    "printindex",
    "protect",
    "protected",
    "providecommand",
    "qquad",
    "quad",
    "r",
    "rSec",
    "rSecindex",
    "raggedbottom",
    "raggedright",
    "raise",
    "raisebox",
    "range",
    "rationale",
    "rb",
    "rceil",
    "realglossitem",
    "recommended",
    "ref",
    "reflexpr",
    "refstepcounter",
    "regrammarterm",
    "relax",
    "reldate",
    "remarks",
    "remitem",
    "removed",
    "removednb",
    "removedxref",
    "removelastskip",
    "renewcommand",
    "renontermdef",
    "required",
    "result",
    "returns",
    "returntype",
    "rfloor",
    "rhdr",
    "rhdrx",
    "rho",
    "right",
    "rightarrow",
    "rightmargin",
    "rightmark",
    "rightshift",
    "rlap",
    "rmfamily",
    "rowhdr",
    "rowsep",
    "s",
    "savedallowbreak",
    "scriptsize",
    "secref",
    "section",
    "sectionmark",
    "seeabove",
    "seeabovenc",
    "seebelow",
    "seebelownc",
    "setafterparaskip",
    "setaftersecskip",
    "setaftersubparaskip",
    "setaftersubsecskip",
    "setaftersubsubsecskip",
    "setbeforeparaskip",
    "setbeforesecskip",
    "setbeforesubparaskip",
    "setbeforesubsecskip",
    "setbeforesubsubsecskip",
    "setbox",
    "setcounter",
    "setglobalstyles",
    "setheaderspaces",
    "setheadfoot",
    "setlength",
    "setlist",
    "setlrmarginsandblock",
    "setmarginnotes",
    "setparaheadstyle",
    "setparaindent",
    "setsecheadstyle",
    "setsecindent",
    "setsubparaheadstyle",
    "setsubparaindent",
    "setsubsecheadstyle",
    "setsubsecindent",
    "setsubsubsecheadstyle",
    "setsubsubsecindent",
    "settowidth",
    "setulmarginsandblock",
    "sffamily",
    "sigma",
    "sin",
    "small",
    "smaller",
    "sout",
    "space",
    "sqrt",
    "stage",
    "state",
    "stepcounter",
    "stopindexescape",
    "string",
    "strip",
    "subparagraph",
    "subsection",
    "subsectionmark",
    "subsubsection",
    "subsubsectionmark",
    "sum",
    "supercite",
    "swallow",
    "sync",
    "t",
    "tabcolsep",
    "tableofcontents",
    "tablerefname",
    "tabularnewline",
    "tcode",
    "temp",
    "templalias",
    "term",
    "terminal",
    "termref",
    "texorpdfstring",
    "text",
    "textasciitilde",
    "textbackslash",
    "textbf",
    "textbullet",
    "textcolor",
    "textit",
    "textlangle",
    "textlarger",
    "textmu",
    "textnormal",
    "textrangle",
    "textregistered",
    "textrm",
    "textsc",
    "textsection",
    "textsf",
    "textsl",
    "textsmaller",
    "textsuperscript",
    "texttt",
    "textunderscore",
    "textup",
    "textwidth",
    "the",
    "thechapter",
    "thepage",
    "theparagraph",
    "thesection",
    "thesubsection",
    "thesubsubsection",
    "theta",
    "thispagestyle",
    "throws",
    "times",
    "tllo",
    "to",
    "today",
    "tokenize",
    "topline",
    "topskip",
    "tref",
    "ttfamily",
    "twocolglossary",
    "u",
    "ucode",
    "uline",
    "uname",
    "ungap",
    "unhbox",
    "unicode",
    "unskip",
    "unspec",
    "unspecalloctype",
    "unspecbool",
    "unspecnc",
    "unspecuniqtype",
    "unun",
    "upshape",
    "url",
    "urlstyle",
    "usepackage",
    "v",
    "value",
    "vbox",
    "vcenter",
    "vdots",
    "verb",
    "verbtocs",
    "vfill",
    "vrule",
    "vskip",
    "vspace",
    "vtop",
    "w",
    "widowpenalties",
    "write",
    "x",
    "xA",
    "xBB",
    "xBF",
    "xEF",
    "xF",
    "xc",
    "xdef",
    "xname",
    "xor",
    "xref",
    "xrefc",
    "z",
    "zeta",
}

# ===============================================================================
# Terminal color support
# ===============================================================================

ANSI_RESET = "\033[0m"
ANSI_BOLD = "\033[1m"
ANSI_RED = "\033[31m"
ANSI_GREEN = "\033[32m"
ANSI_YELLOW = "\033[33m"
ANSI_GRAY = "\033[90m"

COLOR = sys.stderr.isatty() and "NO_COLOR" not in os.environ


def style(text: str, code: str) -> str:
    if not COLOR:
        return text
    return f"{code}{text}{ANSI_RESET}"


# ==================================================================================================
# Data types
# ==================================================================================================


class Environment(Enum):
    ITEMDESCR = "itemdescr"
    CODEBLOCK = "codeblock"
    CODEBLOCKTU = "codeblocktu"
    NOTE = "note"
    FOOTNOTE = "footnote"
    EXAMPLE = "example"

    def __init__(self, _name: str):
        self.begin_pattern: Pattern[str] = re.compile(
            r"\\begin\{" + re.escape(_name) + r"\}"
        )
        self.end_pattern: Pattern[str] = re.compile(
            r"\\end\{" + re.escape(_name) + r"\}"
        )


@dataclass
class Failure:
    file: str
    """File path relative to the working directory."""
    line: int
    """0-based line number."""
    column_start: int
    """0-based inclusive start column."""
    column_end: int
    """0-based exclusive end column."""
    message: str
    """The error message."""
    check_id: str
    """The id of the check."""


@dataclass
class ExpectedFailure:
    file: str
    """File path relative to the working directory."""
    comment_line: int
    """0-based line number of the directive comment."""
    check_id: str
    """The id of the check that is expected to fail."""
    hit: bool = False
    """`true` if a matching failure was reported."""


# ==================================================================================================
# Global state
# ==================================================================================================

source_dir: Path = Path()
_file_locations: Dict[str, Path] = {}
expected_registry: Dict[Tuple[str, int], ExpectedFailure] = {}

# ==================================================================================================
# Expected-failure tracking
# ==================================================================================================


def register_expected(file: str, comment_line: int, check_id: str) -> None:
    key = (file, comment_line)
    if key not in expected_registry:
        expected_registry[key] = ExpectedFailure(file, comment_line, check_id)


def consume_expected(file: str, failure_line: int, check_id: str) -> bool:
    # Walk backwards through *consecutive* %EXPECTCHECKNEXTLINE directives
    # only.  A blank line (or any other content) breaks the chain —
    # EXPECTCHECKNEXTLINE always refers to the immediately following line.
    for offset in range(1, min(failure_line, 20) + 1):
        entry = expected_registry.get((file, failure_line - offset))
        if entry is None:
            # Not an EXPECTCHECKNEXTLINE line — chain is broken.
            return False
        if entry.check_id == check_id:
            entry.hit = True
            return True
        # A different EXPECTCHECKNEXTLINE — keep looking (stacked directives).
    return False


def collect_unexpectedly_not_failed() -> List[ExpectedFailure]:
    return [e for e in expected_registry.values() if not e.hit]


# ==================================================================================================
# Utilities
# ==================================================================================================


COMMENT_PATTERN = re.compile(r"^\s*%")


def make_alt_pattern(items: List[str]) -> str:
    return "(?:" + "|".join(re.escape(s) for s in items) + ")"


def read_file(path: Path) -> List[str]:
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read().splitlines()
    except OSError:
        return []


def format_failure(fail: Failure, lines: List[str]) -> str:
    parts: List[str] = []
    message = (
        re.sub(r"`([^`]+)`", f"{ANSI_YELLOW}\\1{ANSI_RESET}", fail.message)
        if COLOR
        else fail.message
    )
    parts.append(
        f"{style(fail.file, ANSI_BOLD)}:"
        f"{style(str(fail.line + 1), ANSI_BOLD)}:"
        f"{style(str(fail.column_start + 1), ANSI_BOLD)}: "
        f"{style('error:', ANSI_RED)} {message}"
        f" {style(f'[{fail.check_id}]', ANSI_GRAY)}"
    )
    if fail.line < len(lines):
        src_line = lines[fail.line]
        display_line = src_line.replace("\t", "    ")
        line_num_str = str(fail.line + 1)
        num_width = max(6, len(line_num_str))
        pad = " " * (num_width - len(line_num_str))
        col1 = fail.column_start + 1
        col2 = fail.column_end + 1
        parts.append(f"{pad}{line_num_str} | {display_line}")
        prefix = display_line[: col1 - 1]
        highlight_pad = len(prefix)
        highlight_len = max(1, col2 - col1)
        if col1 - 1 + highlight_len > len(display_line):
            highlight_len = max(1, len(display_line) - (col1 - 1))
        gutter = " " * (num_width + 1) + "| "
        hl = style("^" + "~" * (highlight_len - 1), ANSI_GREEN)
        parts.append(f"{gutter}{' ' * highlight_pad}{hl}")
    return "\n".join(parts)


def find_env_ranges(
    lines: List[str],
    env: Environment,
) -> List[Tuple[int, int]]:
    begin_re = env.begin_pattern
    end_re = env.end_pattern
    ranges: List[Tuple[int, int]] = []
    stack: List[int] = []
    for idx, line in enumerate(lines):
        if begin_re.search(line):
            stack.append(idx)
        if end_re.search(line) and stack:
            ranges.append((stack.pop(), idx + 1))
    return ranges


_unexpected_count = 0


def emit_check_failure(
    check: Check,
    file: str,
    line: int,
    column_start: int,
    column_end: int,
    message: str,
) -> None:
    """
    Prints a failure immediately (unless consumed by an expected-failure marker).
    Line numbers and columns follow the same convention as `Failure`.
    """
    global _unexpected_count
    if consume_expected(file, line, check.id):
        return
    _unexpected_count += 1
    fail = Failure(
        file=file,
        line=line,
        column_start=column_start,
        column_end=column_end,
        message=message,
        check_id=check.id,
    )
    # Reading the file from scratch is very slow,
    # but we don't care because this is the unhappy path anyway,
    # and we usually don't expect failures anyway.
    file_path = _file_locations[file]
    lines = read_file(file_path)
    print(format_failure(fail, lines), file=sys.stderr)
    print(file=sys.stderr)


# ==================================================================================================
# Checks
# ==================================================================================================


class Check(ABC):
    """Base class for all checks."""

    id: str = ""

    def begin_file(self, file_path: Path, lines: List[str]) -> None:
        """Called before processing any line of `file_path`."""
        self.file_path = file_path
        self.lines = lines

    def check_line(self, line_num: int, line: str) -> None:
        """Called for each line while the check is active."""
        pass

    def end_file(self, file_path: Path) -> None:
        """Called after processing all lines of `file_path`."""
        pass

    def end_checks(self) -> None:
        """Called once after all files have been processed."""
        pass

    def fail(
        self,
        line: int,
        column_start: int,
        column_end: int,
        message: str,
    ) -> None:
        """Report a failure at `self.file_path`."""
        emit_check_failure(
            self,
            os.path.relpath(self.file_path),
            line,
            column_start,
            column_end,
            message,
        )


class BannedPatternCheck(Check):
    """Reports a failure on every line matching a banned regex pattern."""

    def __init__(
        self,
        check_id: str,
        pattern: Pattern[str],
        message: str,
    ):
        self.id = check_id
        self.pattern = pattern
        self.message = message

    def check_line(self, line_num: int, line: str) -> None:
        if COMMENT_PATTERN.match(line):
            return
        m = self.pattern.search(line)
        if m is None:
            return
        self.fail(
            line_num,
            m.start(),
            m.end(),
            self.message,
        )


class _EnvRanges:
    """Pre-computed line ranges for a LaTeX environment within one file."""

    def __init__(self, lines: List[str], env: Environment):
        self.in_range: Set[int] = set()
        for start, end in find_env_ranges(lines, env):
            self.in_range.update(range(start, end))

    def contains(self, line_num: int) -> bool:
        return line_num in self.in_range


class BannedPatternInEnvironmentCheck(Check):
    """Checks a pattern only within a given LaTeX environment.

    Environment ranges are pre-computed in ``begin_file`` so they are
    always available even if the check is temporarily inactive.
    """

    def __init__(
        self,
        check_id: str,
        env: Environment,
        pattern: Pattern[str],
        message: str,
    ):
        self.id = check_id
        self._env = env
        self._pattern = pattern
        self._message = message

    def begin_file(self, file_path: Path, lines: List[str]) -> None:
        super().begin_file(file_path, lines)
        self._ranges = _EnvRanges(lines, self._env)

    def check_line(self, line_num: int, line: str) -> None:
        if not self._ranges.contains(line_num):
            return
        if COMMENT_PATTERN.match(line):
            return
        m = self._pattern.search(line)
        if m is None:
            return
        self.fail(
            line_num,
            m.start(),
            m.end(),
            self._message,
        )


class NonAsciiCheck(Check):
    NON_ASCII_PATTERN = re.compile(r"[^\x09\x0a\x0d\x20-\x7e]")

    def __init__(self, check_id: str):
        self.id = check_id

    def check_line(self, line_num: int, line: str) -> None:
        for m in self.NON_ASCII_PATTERN.finditer(line):
            ch, cp = m.group(0), ord(m.group(0))
            name = unicodedata.name(ch, "<unknown>")
            self.fail(
                line_num,
                m.start(),
                m.end(),
                f"Non-ASCII character U+{cp:04X} {name} found; "
                f"use the appropriate LaTeX macro instead.",
            )


class TrailingEmptyLinesCheck(Check):
    def __init__(self, check_id: str):
        self.id = check_id

    def end_file(self, file_path: Path) -> None:
        try:
            raw = file_path.read_bytes()
        except OSError:
            return
        if len(raw) >= 2 and raw[-2:] == b"\n\n":
            count = sum(1 for b in reversed(raw) if b == 0x0A)
            self.fail(
                raw.decode(errors="replace").count("\n"),
                0,
                0,
                f"File ends with {count} trailing newlines; "
                f"files must end with exactly one newline.",
            )


class ConsecutivePnumCheck(Check):
    def __init__(self, check_id: str):
        self.id = check_id

    def begin_file(self, file_path: Path, lines: List[str]) -> None:
        super().begin_file(file_path, lines)
        self._prev_was_pnum = False

    def check_line(self, line_num: int, line: str) -> None:
        if COMMENT_PATTERN.match(line):
            return
        is_pnum = line == "\\pnum"
        if is_pnum and self._prev_was_pnum:
            self.fail(
                line_num,
                0,
                0,
                "Two consecutive `\\pnum` found; remove the duplicate.",
            )
        self._prev_was_pnum = is_pnum


class TailnoteTailexampleCheck(Check):
    def __init__(self, check_id: str):
        self.id = check_id

    END_PATTERN = re.compile(r"\\end\{(?:example|note)\}")
    TAIL_PATTERN = re.compile(r"- *(?:\\\\|&)")

    def begin_file(self, file_path: Path, lines: List[str]) -> None:
        super().begin_file(file_path, lines)
        self._pending: Optional[Tuple[int, int, int]] = None

    def check_line(self, line_num: int, line: str) -> None:
        # Check whether the previous line should have used \\tailnote.
        if self._pending is not None:
            prev_line_num, cs, ce = self._pending
            if self.TAIL_PATTERN.search(line):
                self.fail(
                    prev_line_num,
                    cs,
                    ce,
                    "`\\end{note}` or `\\end{example}` appears at the end of a table cell; "
                    "use `\\tailnote` or `\\tailexample` instead.",
                )
            self._pending = None

        m = self.END_PATTERN.search(line)
        if m is not None:
            self._pending = (line_num, m.start(), m.end())


class BlankLineExampleCodeblockCheck(Check):
    def __init__(self, check_id: str):
        self.id = check_id

    def begin_file(self, file_path: Path, lines: List[str]) -> None:
        super().begin_file(file_path, lines)
        self._prev: Optional[str] = None

    def check_line(self, line_num: int, line: str) -> None:
        if (
            self._prev == "\\begin{example}"
            and line == ""
            and line_num + 1 < len(self.lines)
            and self.lines[line_num + 1] == "\\begin{codeblock}"
        ):
            self.fail(
                line_num,
                0,
                0,
                "Blank line between `\\begin{example}` and `\\begin{codeblock}`; "
                "remove the empty line.",
            )
        self._prev = line


class CommentAlignmentCheck(Check):
    def __init__(self, check_id: str):
        self.id = check_id

    # This pattern checks for //, with some notable exemptions:
    # - If '@' is present anywhere, we don't match the comment because we cannot compute alignment.
    # - There needs to be non-whitespace somewhere before `//`,
    #   otherwise we would match misaligned comments like `// \ref{...}` (in synopses).
    # - We require a space before `//` to avoid false positives in string literals,
    #   which is not perfectly reliable, but works for now.
    CHECKED_COMMENT_PATTERN = re.compile(r"^[^@]*[^@\s][^@]*? //")
    ENVIRONMENTS = (Environment.CODEBLOCK, Environment.CODEBLOCKTU)

    def begin_file(self, file_path: Path, lines: List[str]) -> None:
        super().begin_file(file_path, lines)
        self._in_range: Set[int] = set()
        for env in self.ENVIRONMENTS:
            for start, end in find_env_ranges(lines, env):
                self._in_range.update(range(start, end))

    def check_line(self, line_num: int, line: str) -> None:
        if line_num not in self._in_range:
            return
        m = self.CHECKED_COMMENT_PATTERN.search(line)
        if m is None:
            return
        column_start = m.end() - 2
        if column_start % 4 != 0:
            self.fail(
                line_num,
                column_start,
                m.end(),
                f"Comment is preceded by `{column_start}` columns, "
                f"which is not a multiple of `4`; move the comment either "
                f"`{column_start % 4}` to the left or "
                f"`{4 - (column_start % 4)}` columns to the right.",
            )


class HangingParagraphsCheck(Check):
    _rsec_re = re.compile(r"^\\rSec([0-9])")

    def __init__(self, check_id: str):
        self.id = check_id

    def begin_file(self, file_path: Path, lines: List[str]) -> None:
        super().begin_file(file_path, lines)
        self._prev_level = 0
        self._prev_line = 0
        self._prev_text = ""
        self._has_text = False

    def check_line(self, line_num: int, line: str) -> None:
        if line == "\\pnum":
            self._has_text = True
            return
        m = self._rsec_re.match(line)
        if not m:
            return
        level = int(m.group(1))
        if self._has_text and level > self._prev_level:
            self.fail(
                line_num,
                0,
                0,
                f"Hanging paragraph: `{self._prev_text.strip()}` has text "
                f"but no `\\pnum` before a deeper subclause follows.",
            )
        self._prev_level = level
        self._prev_line = line_num
        self._prev_text = line
        self._has_text = False


class SubclausesWithoutSiblingsCheck(Check):
    _rsec_re = re.compile(r"^\\rSec([0-9])")

    def __init__(self, check_id: str):
        self.id = check_id

    def begin_file(self, file_path: Path, lines: List[str]) -> None:
        super().begin_file(file_path, lines)
        self._prev_level = 0
        self._secs: Dict[int, int] = {}
        self._titles: Dict[int, str] = {}

    def check_line(self, line_num: int, line: str) -> None:
        m = self._rsec_re.match(line)
        if not m:
            return
        level = int(m.group(1))
        if level < self._prev_level and self._secs.get(self._prev_level, 0) == 1:
            self.fail(
                line_num,
                0,
                0,
                f"Subclause without siblings: "
                f"`{self._titles.get(self._prev_level, '?').strip()}` "
                f"is the only subclause at its level.",
            )
        self._secs[level] = self._secs.get(level, 0) + 1
        self._titles[level] = line
        self._secs[level + 1] = 0
        self._prev_level = level


class SectionSelfReferenceCheck(Check):
    _sec_re = re.compile(r"^\\rSec.\[([^\]]*)\]")
    _iref_re = re.compile(r"\\iref\{([^\}]*)\}")

    def __init__(self, check_id: str):
        self.id = check_id

    def begin_file(self, file_path: Path, lines: List[str]) -> None:
        super().begin_file(file_path, lines)
        self._current_label: Optional[str] = None

    def check_line(self, line_num: int, line: str) -> None:
        m = self._sec_re.match(line)
        if m:
            self._current_label = m.group(1)
            return
        if self._current_label is None:
            return
        for im in self._iref_re.finditer(line):
            if im.group(1) == self._current_label:
                self.fail(
                    line_num,
                    im.start(),
                    im.end(),
                    f"Section self-reference: "
                    f"`\\iref{{{self._current_label}}}` must not refer to its own section.",
                )


class PnumMissingInItemdescrCheck(Check):
    _element_re = re.compile(r"^\\" + make_alt_pattern(PARAGRAPH_DESCRIPTORS))

    def __init__(self, check_id: str):
        self.id = check_id

    def begin_file(self, file_path: Path, lines: List[str]) -> None:
        super().begin_file(file_path, lines)
        self.check_file(file_path, lines)

    def check_file(self, file_path: Path, lines: List[str]) -> None:
        for start, end in find_env_ranges(lines, Environment.ITEMDESCR):
            seen_pnum = False
            for idx in range(start, end):
                line = lines[idx]
                if line == "\\pnum":
                    seen_pnum = True
                    continue
                if line.startswith("\\index"):
                    continue
                if self._element_re.match(line):
                    if not seen_pnum:
                        self.fail(
                            idx,
                            0,
                            0,
                            "Library element descriptor must be preceded by "
                            "`\\pnum` inside `\\begin{itemdescr}`.",
                        )
                    seen_pnum = False
                else:
                    seen_pnum = False


class ClassDefinitionOutsideNamespaceCheck(Check):
    _class_sec_re = re.compile(r"\\rSec[0-9].*\{Class")
    _rsec_re = re.compile(r"\\rSec")
    _template_re = re.compile(r"template<[^>]*>")
    _class_def_re = re.compile(r"(?:class|struct)\s+[A-Za-z0-9_:]+\s*\{")
    _namespace_re = re.compile(r"^\s*namespace\s", re.MULTILINE)

    def __init__(self, check_id: str):
        self.id = check_id

    def begin_file(self, file_path: Path, lines: List[str]) -> None:
        super().begin_file(file_path, lines)
        self.check_file(file_path, lines)

    def check_file(self, file_path: Path, lines: List[str]) -> None:
        in_section = False
        in_example = False
        in_cb = False
        cb_lines: List[str] = []
        cb_start = 0
        for idx, line in enumerate(lines):
            if self._class_sec_re.search(line):
                in_section = True
                continue
            if in_section and self._rsec_re.match(line):
                in_section = False
                continue
            if not in_section:
                continue
            if "\\begin{example}" in line:
                in_example = True
                continue
            if "\\end{example}" in line:
                in_example = False
                continue
            if in_example:
                continue
            if "\\begin{codeblock}" in line:
                in_cb = True
                cb_lines, cb_start = [], idx
                continue
            if "\\end{codeblock}" in line:
                in_cb = False
                cb_text = "\n".join(cb_lines)
                stripped = self._template_re.sub("", cb_text)
                if self._class_def_re.search(stripped):
                    if not self._namespace_re.search(stripped):
                        for ci, cline in enumerate(cb_lines):
                            cs = self._template_re.sub("", cline)
                            if self._class_def_re.search(cs):
                                self.fail(
                                    cb_start + ci,
                                    0,
                                    0,
                                    "Class definition in a `Class` section "
                                    "not wrapped in a `namespace` block.",
                                )
                                break
                continue
            if in_cb:
                cb_lines.append(line)


class OutdatedFiguresCheck(Check):
    def __init__(self, check_id: str):
        self.id = check_id

    def end_checks(self) -> None:
        for dot_file in sorted(source_dir.glob("*.dot")):
            pdf_file = dot_file.with_suffix(".pdf")
            if (
                pdf_file.exists()
                and dot_file.stat().st_mtime > pdf_file.stat().st_mtime
            ):
                emit_check_failure(
                    self,
                    os.path.relpath(dot_file),
                    0,
                    0,
                    0,
                    f"Figure `{dot_file.name}` is newer than "
                    f"`{pdf_file.name}`; run "
                    f"`make clean-figures && make figures`.",
                )


class FunctionDescriptorOutOfOrderCheck(Check):
    _element_index: Dict[str, int] = {e: i for i, e in enumerate(FUNCTION_DESCRIPTORS)}
    _relevant_line_pattern = re.compile(r"^\\" + make_alt_pattern(FUNCTION_DESCRIPTORS))

    def __init__(self, check_id: str):
        self.id = check_id

    def begin_file(self, file_path: Path, lines: List[str]) -> None:
        super().begin_file(file_path, lines)
        self.check_file(file_path, lines)

    def check_file(self, file_path: Path, lines: List[str]) -> None:
        for start, end in find_env_ranges(lines, Environment.ITEMDESCR):
            if "% NOCHECK:" in lines[start] and "order" in lines[start]:
                continue
            prev_name: Optional[str] = None
            for idx in range(start, end):
                m = self._relevant_line_pattern.match(lines[idx])
                if not m:
                    continue
                name = m.group(0)[1:]
                if prev_name is not None:
                    if self._element_index[name] < self._element_index[prev_name]:
                        self.fail(
                            idx,
                            m.start(),
                            m.end(),
                            f"`{name}` must not precede `{prev_name}`.",
                        )
                prev_name = name


class UnbalancedBeginAndEndCheck(Check):
    BEGIN_OR_END_PATTERN = re.compile(r"\\(begin|end)\{([^}]+)\}")

    def __init__(self, check_id: str):
        self.id = check_id

    def begin_file(self, file_path: Path, lines: List[str]) -> None:
        super().begin_file(file_path, lines)
        self._stack: List[Tuple[str, int, int, int]] = []

    def check_line(self, line_num: int, line: str) -> None:
        if COMMENT_PATTERN.match(line):
            return
        for m in self.BEGIN_OR_END_PATTERN.finditer(line):
            directive = m.group(1)  # begin or end
            name = m.group(2)
            column_start = m.start()
            column_end = m.end()

            if directive == "begin":
                self._stack.append((name, line_num, column_start, column_end))
            else:
                if not self._stack:
                    self.fail(
                        line_num,
                        column_start,
                        column_end,
                        f"`\\end{{{name}}}` has no matching `\\begin{{{name}}}`.",
                    )
                else:
                    open_name, open_line_num, _, _ = self._stack.pop()
                    if open_name != name:
                        self.fail(
                            line_num,
                            column_start,
                            column_end,
                            f"`\\end{{{name}}}` does not match "
                            f"`\\begin{{{open_name}}}` "
                            f"(opened at line {open_line_num}).",
                        )

    def end_file(self, file_path: Path) -> None:
        for name, line_num, column_start, column_end in self._stack:
            self.fail(
                line_num,
                column_start,
                column_end,
                f"`\\begin{{{name}}}` has no matching `\\end{{{name}}}`.",
            )


class UnknownCommandCheck(Check):
    """
    Report `\\command` not seen anywhere in the codebase.
    It is very unlikely that a novel command is used unintentionally at this point,
    and much more likely that someone made a typo like `\\tocde` instead of `\\tcode`.

    If this check ever reports a false positive,
    add the command to `KNOWN_COMMANDS` above.
    """

    def __init__(self, check_id: str):
        self.id = check_id

    _cmd_re = re.compile(r"\\([a-zA-Z][a-zA-Z]*)")

    def check_line(self, line_num: int, line: str) -> None:
        if COMMENT_PATTERN.match(line):
            return
        for m in self._cmd_re.finditer(line):
            cmd = m.group(1)
            if cmd in KNOWN_COMMANDS:
                continue
            self.fail(
                line_num,
                m.start(),
                m.end(),
                f"Unknown command `{cmd}`.",
            )


class UseOfUndefinedCheck(Check):
    """
    Tracks definitions and uses across all files.
    Some of this is already covered by check-output.sh,
    but running that script is tremendously expensive and doesn't give pretty error feedback,
    so we may as well catch some of these issues here.

    `definition_pattern` and each pattern in `usage_pattern` must capture the name in group 1.
    """

    def __init__(
        self,
        check_id: str,
        definition_pattern: Pattern[str],
        usage_pattern: List[Pattern[str]],
    ):
        self.id = check_id
        self._def_re = definition_pattern
        self._use_res = usage_pattern
        self._defined: Set[str] = set()
        self._used: Dict[str, List[Tuple[str, int]]] = defaultdict(list)

    def check_line(self, line_num: int, line: str) -> None:
        for m in self._def_re.finditer(line):
            self._defined.add(m.group(1))
        for use_re in self._use_res:
            for m in use_re.finditer(line):
                name = m.group(1)
                self._used[name].append((os.path.relpath(self.file_path), line_num))

    def end_checks(self) -> None:
        for name, locations in sorted(self._used.items()):
            if name not in self._defined:
                file_name, line_num = locations[0]
                emit_check_failure(
                    self,
                    file_name,
                    line_num,
                    0,
                    0,
                    f"`{name}` has no definition.",
                )


CHECKS: List[Check] = [
    # -- Text checks -------------------------------------------------------------------------------
    # Such checks run on all files and identify problems like illegal characters,
    # trailing whitespace, etc.
    # ----------------------------------------------------------------------------------------------
    NonAsciiCheck("text-non-ascii-char"),
    BannedPatternCheck(
        "text-trailing-ws",
        re.compile(r"\s+$"),
        "Line has trailing whitespace; remove the extra spaces.",
    ),
    TrailingEmptyLinesCheck("text-trailing-empty-lines"),
    # -- Base checks -------------------------------------------------------------------------------
    # These run in both the core and library TeX sources.
    # ----------------------------------------------------------------------------------------------
    BannedPatternCheck(
        "base-indented-codeblock",
        re.compile(r"(?<=.)\\(?:begin|end)\{codeblock\}"),
        "`\\begin{codeblock}` or `\\end{codeblock}` must not be indented.",
    ),
    BannedPatternCheck(
        "base-pnum-alone",
        re.compile(r"^[^%].*\\pnum"),
        "`\\pnum` must be on its own line; move preceding text to a separate line.",
    ),
    BannedPatternCheck(
        "base-pnum-alone",
        re.compile(r"\\pnum(?=\s*.)"),
        "`\\pnum` must be on its own line; move trailing text to a separate line.",
    ),
    ConsecutivePnumCheck("base-consecutive-pnum"),
    BannedPatternCheck(
        "base-footnote-punct",
        re.compile(r"\\end\{footnote\}(?![@%\\]|$)"),
        "`\\end{footnote}` must be followed by `@`, `%`, `\\`, or nothing.",
    ),
    BannedPatternCheck(
        "base-opt",
        re.compile(r"\\opt(?![{])"),
        "`\\opt` must be followed by a brace group `{...}`; write `\\opt{...}`.",
    ),
    BannedPatternCheck(
        "base-opt",
        re.compile(r"opt\{\}"),
        "`opt{}` is incorrectly used; provide an argument to `\\opt`.",
    ),
    BannedPatternCheck(
        "base-expos",
        re.compile(r"//\s+exposition only"),
        "Write `\\expos` instead of the literal comment `// exposition only`.",
    ),
    BannedPatternCheck(
        "base-notdef",
        re.compile(r"//\s+not defined"),
        "Write `\\notdef` instead of the literal comment `// not defined`.",
    ),
    BannedPatternCheck(
        "base-cpp",
        re.compile(r'^[^%]*[^{"]C\+\+[^"}]'),
        "Write `\\Cpp{}` instead of literally `C++`.",
    ),
    BannedPatternCheck(
        "base-caret",
        re.compile(re.escape(r"\^")),
        "Write `\\caret` or `\\reflexpr` instead of literally `\\^`.",
    ),
    BannedPatternCheck(
        "base-u-plus",
        re.compile(r"U\+"),
        "Write `\\unicode{...}`, `\\ucode{...}`, or `\\uname{...}` "
        "(with digits and/or lower-case letters) instead of `U+NNNN`.",
    ),
    BannedPatternCheck(
        "base-hex-ucode-case",
        re.compile(r"ucode\{[^}]*[A-F][^}]*\}"),
        "Hex digits inside `\\ucode{...}` must be lowercase.",
    ),
    BannedPatternCheck(
        "base-hex-unicode-case",
        re.compile(r"unicode\{[^}]*[A-F][^}]*\}"),
        "Hex digits inside `\\unicode{...}` must be lowercase.",
    ),
    BannedPatternCheck(
        "base-tcode-exposid",
        re.compile(r"\\tcode\{\\exposid\{[^\{]*\}\}"),
        "Do not write `\\tcode{\\exposid{...}}` use `\\exposid{...}` directly.",
    ),
    BannedPatternCheck(
        "base-ref-in-parens",
        re.compile(r"(?<=\()\\ref(?=\{)(?!.*--)"),
        "Write `\\iref{...}` instead of `(\\ref{...})`.",
    ),
    BannedPatternCheck(
        "base-iref-location",
        re.compile(r"^\\iref"),
        "`\\iref` must not appear at the start of the line.",
    ),
    BannedPatternCheck(
        "base-iref-location",
        re.compile(r"(?<= )\\iref"),
        "`\\iref` must be flush against the preceding word; "
        "remove the space in front of it.",
    ),
    BannedPatternCheck(
        "base-xrefc",
        re.compile(r"^ISO C [0-9]*(?=\.)"),
        "Write `\\xrefc{...}` instead of the literal `ISO C` reference.",
    ),
    BannedPatternCheck(
        "base-diff-marker",
        re.compile(r"^\\" + make_alt_pattern(DIFF_DESCRIPTORS) + r"\s.+$"),
        "A change marker in (like `\\change`, `\\rationale`, etc.) "
        "must not have trailing text on the same line.",
    ),
    BannedPatternCheck(
        "base-note-not-alone",
        re.compile(r"^.*[^ ]\s*\\(?:begin|end)\{(?:example|note)\}"),
        "`\\begin{note}` / `\\begin{example}` (or their `\\end` forms) "
        "must appear alone on their line; move preceding text to a separate line.",
    ),
    BannedPatternCheck(
        "base-note-not-alone",
        re.compile(r"\\(?:begin|end)\{(?:example|note)\}(?!%)(.+)$"),
        "`\\begin{note}` / `\\begin{example}` (or their `\\end` forms) "
        "must appear alone on their line; move trailing text to a separate line.",
    ),
    TailnoteTailexampleCheck("base-tailnote-needed"),
    BlankLineExampleCodeblockCheck("base-blank-example-codeblock"),
    CommentAlignmentCheck("base-comment-align"),
    BannedPatternCheck(
        "base-deleted-param-name",
        re.compile(r"&[ 0-9a-z_]+\)\s*=\s*delete"),
        "Deleted special member function has a named parameter; "
        "remove the parameter name.",
    ),
    BannedPatternCheck(
        "base-bad-label-chars",
        re.compile(r"^\\rSec.\[[^\]]*[^a-z\.0-9][^\]]*\]\{"),
        "Section label contains an invalid character; use only `[a-z.0-9]` in labels.",
    ),
    BannedPatternInEnvironmentCheck(
        "base-normative-in-note",
        Environment.NOTE,
        re.compile(r"(?:shall|may|should)(?=[^a-zA-Z])"),
        "Neither `shall`, `should`, nor `may` is allowed in notes. Prefer `can` or `cannot`.",
    ),
    BannedPatternInEnvironmentCheck(
        "base-normative-in-footnote",
        Environment.FOOTNOTE,
        re.compile(r"(?:shall|may|should)(?=[^a-zA-Z])"),
        "Neither `shall`, `should`, nor `may` is allowed in footnotes. Prefer `can` or `cannot`.",
    ),
    BannedPatternCheck(
        "base-eg-comma",
        re.compile(r"e\.g\.(?!,)"),
        "`e.g.` must be followed by a comma.",
    ),
    BannedPatternCheck(
        "base-ie-comma",
        re.compile(r"i\.e\.(?!,)"),
        "`i.e.` must be followed by a comma.",
    ),
    BannedPatternCheck(
        "base-logop-case",
        re.compile(r"\\logop\{[^}]*[^andor\}][^}]*\}"),
        "`\\logop` argument must use only lowercase letters `a`, `n`, `d`, `o`, `r`.",
    ),
    HangingParagraphsCheck("base-hanging-paragraph"),
    SubclausesWithoutSiblingsCheck("base-lonely-subclause"),
    UnknownCommandCheck("base-unknown-command"),
    SectionSelfReferenceCheck("base-self-ref"),
    UseOfUndefinedCheck(
        "base-grammarterm-undef",
        definition_pattern=re.compile(r"\\nontermdef\{([^}]+)\}"),
        usage_pattern=[re.compile(r"\\grammarterm\{([^}]+)(?<!-keyword)\}")],
    ),
    UnbalancedBeginAndEndCheck("base-env-balancing"),
    OutdatedFiguresCheck("base-outdated-figure"),
    # -- Library checks ----------------------------------------------------------------------------
    # These are additional stricter checks that only run on library TeX sources.
    # Since they all start with `lib`, they can be disabled in bulk using `lib-*`.
    # ----------------------------------------------------------------------------------------------
    BannedPatternCheck(
        "lib-template-space",
        re.compile(r"template\s+<"),
        "Space between `template` and `<`; write `template<`.",
    ),
    BannedPatternCheck(
        "lib-keywords-explicit-constexpr",
        re.compile(r"\bexplicit\b.*\bconstexpr\b"),
        "Wrong order: `explicit constexpr` should be `constexpr explicit`.",
    ),
    BannedPatternCheck(
        "lib-keywords-constexpr-static",
        re.compile(r"\bconstexpr\b.*\sstatic\s"),
        "Wrong order: `constexpr static` should be `static constexpr`.",
    ),
    BannedPatternCheck(
        "lib-using-typename",
        re.compile(r"using.*= typename"),
        "Type alias uses `typename` unnecessarily; remove "
        "`typename` from the alias declaration.",
    ),
    ClassDefinitionOutsideNamespaceCheck("lib-class-no-namespace"),
    BannedPatternCheck(
        "lib-cv-ref-space",
        re.compile(r"\)\s+const&"),
        "Missing space between cv-qualifier and ref-qualifier; "
        "write `) const &` instead of `) const&`.",
    ),
    BannedPatternCheck(
        "lib-element-alone",
        re.compile(r"^\\" + make_alt_pattern(FUNCTION_DESCRIPTORS) + r".+$"),
        "A library element introducer (like `\\effects`, `\\returns`, etc.) "
        "must not have trailing text on the same line.",
    ),
    FunctionDescriptorOutOfOrderCheck("lib-element-order"),
    PnumMissingInItemdescrCheck("lib-missing-pnum"),
    BannedPatternCheck(
        "lib-bad-concept-name",
        re.compile(
            r"\\(?:def)?(?:lib|expos)concept\{[a-z0-9_-]*[^a-z0-9_}\-][a-z0-9_-]*\}"
        ),
        "Concept name contains invalid characters; use only lowercase "
        "letters, digits, hyphens, and underscores.",
    ),
    UseOfUndefinedCheck(
        "lib-header-undef",
        definition_pattern=re.compile(
            r"\\(?:libheaderdef|indexheader|libnoheader)\{([^}]+)\}"
        ),
        usage_pattern=[
            re.compile(r"\\libheader(?:ref(?:x{1,2})?)?\{([^}]+)\}"),
            re.compile(r"\\libheaderx\{[^}]+\}\{([^}]+)\}"),
        ],
    ),
    UseOfUndefinedCheck(
        "lib-concept-undef",
        definition_pattern=re.compile(r"\\def(?:lib|expos)concept(?:nc)?\{([^}]+)\}"),
        usage_pattern=[
            re.compile(r"\\(?:lib|expos)concept(?:nc)?\{([^}]+)\}"),
            re.compile(r"\\libconceptx\{[^}]+\}\{([^}]+)\}"),
            re.compile(r"\\exposconceptx\{[^}]+\}\{([^}]+)\}"),
        ],
    ),
    # -- Ranges library checks ---------------------------------------------------------------------
    # These checks are specific to [ranges].
    # They all start with `lib-ranges`, so they can be disabled in bulk using `lib-ranges-*`.
    # ----------------------------------------------------------------------------------------------
    BannedPatternCheck(
        "lib-ranges-iterator-indexing",
        re.compile(r"\\indexlibrary(?:ctor|member).*::(?:iterator|sentinel)\}.*"),
        "Use `\\exposid` for `::iterator` / `::sentinel` member indexing.",
    ),
    BannedPatternCheck(
        "lib-ranges-iterator-global-index",
        re.compile(r"\\indexlibraryglobal.*::(?:iterator|sentinel)\}.*"),
        "Do not index exposition-only `::iterator` and `::sentinel` "
        "class names with `\\indexlibraryglobal`.",
    ),
]


# ==================================================================================================
# Check runner
# ==================================================================================================

NO_CHECK_PATTERN = re.compile(r"^\s*%NOCHECK(BEGIN|END|NEXTLINE)(?:\((\S*)\))?\s*$")


def run_checks(tex_files: List[Path]) -> int:
    """Run all registered checks. Returns the number of unexpected failures."""
    global _unexpected_count
    _unexpected_count = 0
    _file_locations.clear()

    for fp in tex_files:
        _file_locations[os.path.relpath(fp)] = fp

    all_ids = {c.id for c in CHECKS if c.id}

    for file_path in tex_files:
        if not file_path.exists():
            continue

        lines = read_file(file_path)

        # Always call begin_file.
        for c in CHECKS:
            c.begin_file(file_path, lines)

        # Active-set management — controls whether check_line is called.
        active: Set[str] = set(all_ids)
        # Per-check next-line skips: check_id → set of line numbers.
        skip_next: Dict[str, Set[int]] = defaultdict(set)

        for idx, line in enumerate(lines):
            line_num = idx

            # Process %NOCHECK… directives.
            m = NO_CHECK_PATTERN.match(line)
            if m:
                directive = m.group(1)  # BEGIN, END, or NEXTLINE
                cid = m.group(2) or "*"
                if directive == "BEGIN":
                    if cid == "*":
                        active.clear()
                    else:
                        active = {a for a in active if not fnmatch.fnmatch(a, cid)}
                elif directive == "END":
                    if cid == "*":
                        active = set(all_ids)
                    else:
                        active |= {a for a in all_ids if fnmatch.fnmatch(a, cid)}
                elif directive == "NEXTLINE":
                    if cid == "*":
                        for c in all_ids:
                            skip_next[c].add(line_num + 1)
                    else:
                        matched = {a for a in all_ids if fnmatch.fnmatch(a, cid)}
                        for c in matched:
                            skip_next[c].add(line_num + 1)

            # Call check_line only on active checks (not skipped).
            for c in CHECKS:
                if c.id in active and line_num not in skip_next.get(c.id, set()):
                    c.check_line(line_num, line)

        # Always call end_file.
        for c in CHECKS:
            c.end_file(file_path)

    # After all files, run end-of-checks hooks.
    for c in CHECKS:
        c.end_checks()

    return _unexpected_count


def parse_expected_from_files(tex_files: List[Path]) -> None:
    """Pre-scan ``.tex`` files for ``%EXPECTCHECKNEXTLINE(id)`` directives.

    The directive must appear alone on its line; *id* is the check that is
    expected to fire on the **next** line.
    """
    expect_re = re.compile(r"^\s*%EXPECTCHECKNEXTLINE\((\S+)\)\s*$")

    for file_path in tex_files:
        lines = read_file(file_path)
        for idx in range(len(lines) - 1):
            m = expect_re.match(lines[idx])
            if m:
                register_expected(os.path.relpath(file_path), idx, m.group(1).strip())


def collect_tex_files_recursively(root_paths: List[Path]) -> List[Path]:
    result: List[Path] = []
    for root in root_paths:
        if root.is_dir():
            result.extend(sorted(root.rglob("*.tex")))
        elif root.suffix == ".tex":
            result.append(root)
    return result


def find_project_root() -> Path:
    """Locate the project root by looking for ``source/std.tex``."""
    script_dir = Path(__file__).resolve().parent
    for candidate in (script_dir.parent, Path.cwd()):
        if (candidate / "source" / "std.tex").exists():
            return candidate
        if (candidate / "std.tex").exists():
            return candidate
    return script_dir.parent


# ==================================================================================================
# CLI
# ==================================================================================================


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Check LaTeX sources for C++ standard drafting rules."
    )
    parser.add_argument(
        "files",
        nargs="*",
        help="Specific .tex files or directories to check (default: all .tex files"
        " under the project root).",
    )
    args = parser.parse_args()

    global source_dir
    project_root = find_project_root()
    source_dir = (
        project_root / "source" if (project_root / "source").is_dir() else project_root
    )

    tex_files = (
        collect_tex_files_recursively([Path(f).resolve() for f in args.files])
        if args.files
        else collect_tex_files_recursively([project_root])
    )
    if not tex_files:
        print("error: no .tex files found", file=sys.stderr)
        sys.exit(1)

    parse_expected_from_files(tex_files)
    num_failures = run_checks(tex_files)

    unhit = collect_unexpectedly_not_failed()
    num_failures += len(unhit)
    for entry in unhit:
        fp = _file_locations.get(entry.file)
        if fp is None:
            fp = Path.cwd() / entry.file
        lines = read_file(fp)
        comment_line = entry.comment_line
        if comment_line < len(lines):
            line_text = lines[comment_line]
            column = line_text.find(entry.check_id)
            if column < 0:
                column = 0
            fail = Failure(
                file=entry.file,
                line=comment_line,
                column_start=column,
                column_end=column + len(entry.check_id),
                message=f"expected failure `{entry.check_id}` was not triggered",
                check_id=entry.check_id,
            )
            print(format_failure(fail, lines), file=sys.stderr)
            print(file=sys.stderr)
        else:
            print(
                f"  {entry.file}:{entry.comment_line + 1}: expected '{entry.check_id}'",
                file=sys.stderr,
            )

    if num_failures:
        print(
            f"{style(str(num_failures), ANSI_RED)} error(s) emitted.",
            file=sys.stderr,
        )

    exit_code = 1 if num_failures > 0 else 0
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
