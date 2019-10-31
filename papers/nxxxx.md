# Nxxxx Editors' Report -- Programming Languages -- C++

2019-11-xx  
Richard Smith (editor) (Google Inc)  
Thomas Köppe (co-editor) (Google DeepMind)  
Jens Maurer (co-editor)  
Dawn Perchik (co-editor) (Bright Side Computing, LLC)  
`<cxxeditor@gmail.com>`

## Acknowledgements

...

Thanks to all those who have [submitted editorial
issues](https://github.com/cplusplus/draft/wiki/How-to-submit-an-editorial-issue)
and to those who have provided pull requests with fixes.

## New papers

 * [Nxxxx](http://wg21.link/nxxxx) is the committee draft for C++20. It replaces [N4835](http://wg21.link/n4835).
 * Nxxxx is this Editors' Report.

## Motions incorporated into working draft

### Core working group motions

CWG motion 1: [Core issue resolutions](http://wg21.link/pxxxxr0) for N issues in "tentatively ready" status applied: **(DR)**

 * [123](http://wg21.link/cwg123) Issue description
 * ...

CWG motion 2: [P1234R5 "Paper name"](http://wg21.link/p1234r5), resolving 3 NB comments:

 * NB 123: Terse description of issue

### Library working group motions

...

## Notable changes to papers as moved

### CWG motion 1

...

## Disposition of editorial NB comments on C++ 2020 CD1

Listed below are draft disposition for all comments that were
filed as editorial in the ISO 14882 CD (2019) NB comments,
[Nxxxx](http://wg21.link/nxxxx).
Except where otherwise noted, these dispositions only represent the current
viewpoint of the Project Editor.

US 021: Accepted, fixed in 50e55ce9.

 * Split index entries to "block (execution)" and "block (statement)".
 * Also added the statement form to Clause 3, Terms and Definitions.

GB 022: Accepted with modifications, fixed in 8cc6bd34.

 * The relevant change had already been made to [using.headers],
   but this corresponding change was missed.

JP 023: Accepted, fixed in 868934f7.

JP 030: No consensus for change.

 * The text immediately following the grammar makes it clear that
   both lowercase `p` and uppercase `P` are permitted.

US 031: No consensus for change.

 * The example appears to be valid as-is;
   adding `!= 0` does not appear to serve any purpose.

GB 032: Accepted, fixed in 84a1cd53.

US 037: **SG2 to handle issue**

 * The proposed change is not editorial.

JP 045: Accepted, fixed in d401794f.

 * This fixes a misapplication of the resolution of CWG 2381.

US 047: Accepted with modifications, fixed in 785f689d.

 * **Modified resolution:**
  Instead of removing the redundant sentence, it was converted into a note
  and moved after the following sentence of which it is a consequence.

US 052: **CWG to handle issue**

 * The proposed change is not editorial.

JP 057: Accepted, fixed in a06b7a49.

GB 078: Accepted, fixed in e3bb2eba.

 * Italicized references to *digit*s that intended to refer to the grammar production.
 * Also made some nearby editorial improvements:
   added cross-references and fixed an adjacent grammar issue ("is" / "are") in [diff.cpp14.library].

GB 079: **Deferred until US 036 is resolved**

US 085: No consensus for change.

 * Per the description in [module.import],
   translation units are imported, modules are not.
   The wording appears to be correct as-is.

US 088: Accepted with modifications, fixed in d382ea4e.

 * **Modified resolution:**
  Instead of either of the proposed renamings,
  renamed [module.global] to [module.global.frag] and
  renamed [cpp.glob.frag] to [cpp.global.frag].

GB 089: Accepted, fixed in fa42d5a6.

US 099: Accepted, fixed in 9b0502bf.

US 106: **CWG to handle issue**

US 108: Accepted, fixed in 2f42a930.

US 153: Propose accepting; **LWG to approve direction**

 * Can be handled editorially if approved.

US 154: Duplicate of US 153.

US 155: Propose accepting; **LWG to approve direction**

 * Can be handled editorially if approved.

JP 177: Accepted, fixed in 8be40ff0.

 * Replaces a reference to ISO/IEC/IEEE 60599 with a reference to the intended ISO/IEC/IEEE 60559.
 * IEC 60599 is "Mineral oil-filled electrical equipment in service --
   guidance on the interpretation of dissolved and free gases analysis"
 * ISO/IEC/IEEE 60559 is "Information Technology - Microprocessor Systems --
   Floating-Point Arithmetic"

GB 200: No consensus for change.

 * The example already includes all combinations of `const`/non-`const` LHS and RHS,
   as described by paragraph 6.
   The suggested combinations `b == d` and `a == c` are both identical to `a == d`.
   (Note that only `a` and `c` are used on the LHS,
    and only `b` and `d` are used on the RHS.)

US 216: Propose accepting; **LWG to approve direction**

 * Can be handled editorially if approved.

JP 218: **LWG to handle issue**

JP 219: **LWG to handle issue**

GB 225: **LWG to handle issue**

US 242: Propose rejecting; **LWG to approve direction**

 * Organizationally, it seems more consistent to list `span` near the
   sequence containers, just as we list `string_view` near `string.

US 258: Accepted, fixed in f36f871c.

US 280: **LEWG to select a better name or reject**

 * Can be handled editorially if an alternative name is approved.

US 295: **TODO**

JP 314: Accepted with modifications, fixed in 136312cf.

 * This is not an ISO "Terms and Definitions" Clause,
   so the rules for such a Clause do not apply.
 * **Modified resolution:**
   Renamed subclause from "Terms and Definitions" to "Preamble"
   to make it clear that this is not an ISO "Terms and Definitions" Clause.
   Also moved [algorithms.parallel] paragraph 1 into this subclause
   to avoid a hanging paragraph.

JP 319: Accepted, fixed in 5ac298cc.

US 325: No consensus for change.

 * We do not wish to perform this reorganization at this stage,
   but will reconsider the organization of the standard library clauses
   for a future standard.

US 327: **SG6 / LEWG to handle issue**

 * The proposed change is not editorial.
 * Duplicate of PL 326

US 328: **SG6 / LEWG to handle issue**

 * The proposed change is not editorial.

US 330: No consensus for change.

 * The wording to which this comment is objecting
   was removed by [P1355R2](http://wg21.link/p1355r2),
   which was adopted by 2019-07 LWG Motion 2.

GB 335: **LWG to handle issue**

 * The intent of the wording is unclear;
   this issue cannot be resolved editorially.

JP 338: Accepted, fixed in 742f1086.

JP 339: Accepted, fixed in 25a08918.

JP 340: Accepted, fixed in f88f6747.

JP 341: Accepted, fixed in d545c37d.

JP 343: Accepted, fixed in 9252441e.

JP 348: Accepted, fixed in 01dea5f5.

 * Adding the default template arguments here is likely not the best resolution in the long term.
   The explicit default template arguments, if implemented literally, would disallow including
   this header and `<iosfwd>` in the same translation unit.
   However, adding them here makes this header consistent with the rest of this Clause.
 * An LWG issue will be opened to consider
   whether we should require more of the iostreams headers to include `<iosfwd>` and
   which header inclusions should result in the default arguments being made available.

JP 349: Accepted, fixed in adcf12ea.

 * See JP 348.

JP 350: Accepted, fixed in 53b429c9.

 * See JP 348.

US 357: Accepted with modifications, fixed in af747d64.

 * **Modified resolution:**
   A different revised wording was chosen for the notes:
   "The specialization `atomic<bool>` uses the primary template."

US 359: **SG1 / LWG to handle issue**

JP 362: Accepted with modifications, fixed in 195d5bab.

 * **Modified resolution:**
   In addition to adding the missing `[[nodiscard]]`,
   also added the missing `static` and `int` from the synopsis.

CA 366: Accepted, fixed in eaf23727.

JP 373: Accepted with modifications, fixed in 41058d90.

 * **Modified resolution:** In addition to requested changes,
   also added cross-reference to [temp.pre]
   for the *requires-clause* grammar production.

JP 374: Accepted, fixed in dbc3d6a5.

JP 376: Accepted, fixed in 8b5c768e.

## Notable editorial changes

...

### Section label changes

 * [module.global] -> [module.global.frag]
 * [cpp.glob.frag] -> [cpp.global.frag]

## Feature test macros

...

## Minor editorial fixes

A log of editorial fixes made to the working draft since N4835 is below.
This list excludes changes
that do not affect the body text or only affect whitespace or typeface. For a
complete list including such changes (or for the actual deltas applied by these
changes), consult the [draft sources on github](https://github.com/cplusplus/draft/compare/n4835...nxxxx).
