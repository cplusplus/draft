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

US 021: Accepted, fixed in [50e55ce9](https://github.com/cplusplus/draft/commit/50e55ce9).

 * Split index entries to "block (execution)" and "block (statement)".
 * Also added the statement form to Clause 3, Terms and Definitions.

GB 022: Accepted with modifications, fixed in [8cc6bd34](https://github.com/cplusplus/draft/commit/8cc6bd34).

 * The relevant change had already been made to [using.headers],
   but this corresponding change was missed.

 * **Modified resolution:**
   Added a cross-reference to [using.headers] instead of
   the suggested cross-reference to [headers].

JP 023: Accepted, fixed in [868934f7](https://github.com/cplusplus/draft/commit/868934f7).

JP 030: No consensus for change.

 * The text immediately following the grammar makes it clear that
   both lowercase `p` and uppercase `P` are permitted.

US 031: No consensus for change.

 * The example appears to be valid as-is;
   adding `!= 0` does not appear to serve any purpose.

GB 032: Accepted, fixed in [84a1cd53](https://github.com/cplusplus/draft/commit/84a1cd53).

US 037: No consensus for change.

 * The proposed change is not editorial.
   Forwarded to SG2 for consideration and rejected.

FR 039: Accepted with modifications, fixed in [68a6dfef](https://github.com/cplusplus/draft/commit/68a6dfef).

 * **Filed as technical**; SG2 concluded the wording is confusing,
   already does what the comment requests
   (except that ADL also finds friend declarations in a class
   in the same conditions under which
   member lookup would find member declarations in the class).
   Recategorized as editorial to clarify the wording.

 * **Modified resolution:**
   Definition of "interface" (of a module) inlined into its only use (and removed),
   making it clear that [basic.lookup.argdep]/4.4 only finds exported declarations.

JP 045: Accepted, fixed in [d401794f](https://github.com/cplusplus/draft/commit/d401794f).

 * This fixes a misapplication of the resolution of CWG 2381.

US 047: Accepted with modifications, fixed in [785f689d](https://github.com/cplusplus/draft/commit/785f689d).

 * **Modified resolution:**
  Instead of removing the redundant sentence, it was converted into a note
  and moved after the following sentence of which it is a consequence.

US 052: TODO Accepted contingent on P1971R0

 * The proposed change is not editorial.
   Forwarded to CWG for consideration and accepted.

JP 057: Accepted, fixed in [a06b7a49](https://github.com/cplusplus/draft/commit/a06b7a49).

GB 078: Accepted, fixed in [e3bb2eba](https://github.com/cplusplus/draft/commit/e3bb2eba).

 * Italicized references to *digit*s that intended to refer to the grammar production.
 * Also made some nearby editorial improvements:
   added cross-references and fixed an adjacent grammar issue ("is" / "are") in [diff.cpp14.library].

GB 079: TODO Accepted contingent on P1971R0

 * Forwarded to SG2 for consideration. Accepted and example added by CWG.

US 085: No consensus for change.

 * Per the description in [module.import],
   translation units are imported, modules are not.
   The wording appears to be correct as-is.

US 088: Accepted with modifications, fixed in [d382ea4e](https://github.com/cplusplus/draft/commit/d382ea4e).

 * **Modified resolution:**
  Instead of either of the proposed renamings,
  renamed [module.global] to [module.global.frag] and
  renamed [cpp.glob.frag] to [cpp.global.frag].

GB 089: Accepted, fixed in [fa42d5a6](https://github.com/cplusplus/draft/commit/fa42d5a6).

US 099: Accepted, fixed in [9b0502bf](https://github.com/cplusplus/draft/commit/9b0502bf).

US 106: No consensus for change.

 * Forwarded to CWG for consideration and rejected.

US 108: Accepted, fixed in [2f42a930](https://github.com/cplusplus/draft/commit/2f42a930).

US 153: No consensus for change.

 * Forwarded to LWG for consideration; rejected by LEWG.

US 154: Duplicate of US 153.

GB 155: Accepted, fixed in [98e57ff5](https://github.com/cplusplus/draft/commit/98e57ff5).

 * **LWG concurs with this direction**

JP 177: Accepted, fixed in [8be40ff0](https://github.com/cplusplus/draft/commit/8be40ff0).

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

US 216: Accepted, fixed in [dfcc4691](https://github.com/cplusplus/draft/commit/dfcc4691).

 * **LWG concurs with this direction**

JP 218: **Unresolved, reassigned to LWG**

 * Forwarded to LWG for consideration;
   [LWG issue 3310](https://cplusplus.github.io/LWG/issue3310) opened to track this comment.

JP 219: **Unresolved, reassigned to LWG**

 * Forwarded to LWG for consideration;
   [LWG issue 3310](https://cplusplus.github.io/LWG/issue3310) opened to track this comment.

GB 225: **Unresolved, reassigned to LWG**

 * Proposed change is not editorial. Forwarded to LWG for consideration.
   [LWG issue 3327](https://cplusplus.github.io/LWG/issue3327) opened to track this comment.

US 242: No consensus for change.

 * Organizationally, it seems more consistent to list `span` near the
   sequence containers, just as we list `string_view` near `string.

 * Forwarded to LWG for consideration and rejected.

US 258: Accepted, fixed in [f36f871c](https://github.com/cplusplus/draft/commit/f36f871c).

GB 280: TODO Accepted contingent on P1870R1

 * Forwarded to LEWG to select a better name or reject,
   LEWG selected `safe_range` as a replacement non-exposition-only concept name.

US 295: Accepted with modifications, fixed in [53f0651e](https://github.com/cplusplus/draft/commit/53f0651e).

 * Instead of proposed change, incorporated the leading
   "If `ref_is_glvalue` is `true`" into the bullets
   and removed the bullet nesting
   to clarify the meaning of the "Otherwise"s.

JP 314: Accepted with modifications, fixed in [136312cf](https://github.com/cplusplus/draft/commit/136312cf).

 * This is not an ISO "Terms and Definitions" Clause,
   so the rules for such a Clause do not apply.
 * **Modified resolution:**
   Renamed subclause from "Terms and Definitions" to "Preamble"
   to make it clear that this is not an ISO "Terms and Definitions" Clause.
   Also moved [algorithms.parallel] paragraph 1 into this subclause
   to avoid a hanging paragraph.

JP 319: Accepted, fixed in [5ac298cc](https://github.com/cplusplus/draft/commit/5ac298cc).

US 325: No consensus for change.

 * We do not wish to perform this reorganization at this stage,
   but will reconsider the organization of the standard library clauses
   for a future standard.

US 327: **Unresolved, reassigned to LEWG**

 * The proposed change is not editorial.
   Forwarded to LEWG for consideration.
 * Duplicate of PL 326, which may be addressed by [P1956](http://wg21.link/p1956).

US 328: **Unresolved, reassigned to LEWG**

 * The proposed change is not editorial.
   Forwarded to LEWG for consideration.
 * Duplicate of PL 326, which may be addressed by [P1956](http://wg21.link/p1956).

US 330: No consensus for change.

 * The wording to which this comment is objecting
   was removed by [P1355R2](http://wg21.link/p1355r2),
   which was adopted by 2019-07 LWG Motion 2.

JP 338: Accepted, fixed in [742f1086](https://github.com/cplusplus/draft/commit/742f1086).

JP 339: Accepted, fixed in [25a08918](https://github.com/cplusplus/draft/commit/25a08918).

JP 340: Accepted, fixed in [f88f6747](https://github.com/cplusplus/draft/commit/f88f6747).

JP 341: Accepted, fixed in [d545c37d](https://github.com/cplusplus/draft/commit/d545c37d).

JP 343: Accepted, fixed in [9252441e](https://github.com/cplusplus/draft/commit/9252441e).

JP 348: Accepted, fixed in [01dea5f5](https://github.com/cplusplus/draft/commit/01dea5f5).

 * Per [iosfwd.syn]p1, the duplication of default template arguments
   between `<iosfwd>` and `<syncstream>`
   does not prevent a translation unit including both.
 * An LWG issue will be opened to consider
   whether we should require more of the iostreams headers to include `<iosfwd>`;
   currently only `<ios>` and `<iostream>` are guaranteed to provide the forward declarations.
   Similarly LWG should consider whether `<istream>` and `<ostream>` should
   be guaranteed to include `<ios>`.

JP 349: Accepted, fixed in [adcf12ea](https://github.com/cplusplus/draft/commit/adcf12ea).

 * See JP 348.

JP 350: Accepted, fixed in [53b429c9](https://github.com/cplusplus/draft/commit/53b429c9).

 * See JP 348.

US 357: Accepted with modifications, fixed in [af747d64](https://github.com/cplusplus/draft/commit/af747d64).

 * **Modified resolution:**
   A different revised wording was chosen for the notes:
   "The specialization `atomic<bool>` uses the primary template."

US 359: TODO Accepted contingent on P1960

 * Forwarded to SG1 for consideration and accepted by LWG.

JP 362: Accepted with modifications, fixed in [195d5bab](https://github.com/cplusplus/draft/commit/195d5bab).

 * **Modified resolution:**
   In addition to adding the missing `[[nodiscard]]`,
   also added the missing `static` and `int` from the synopsis.

CA 366: Accepted, fixed in [eaf23727](https://github.com/cplusplus/draft/commit/eaf23727).

JP 373: Accepted with modifications, fixed in [41058d90](https://github.com/cplusplus/draft/commit/41058d90).

 * **Modified resolution:** In addition to requested changes,
   also added cross-reference to [temp.pre]
   for the *requires-clause* grammar production.

JP 374: Accepted, fixed in [dbc3d6a5](https://github.com/cplusplus/draft/commit/dbc3d6a5).

JP 376: Accepted, fixed in [8b5c768e](https://github.com/cplusplus/draft/commit/8b5c768e).

### Late comments

CH 02: Accepted, fixed in [5ee93fd7](https://github.com/cplusplus/draft/commit/5ee93fd7).

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
