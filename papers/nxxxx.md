# Nxxxx Editors' Report -- Programming Languages -- C++

2019-11-xx  
Richard Smith (editor) (Google Inc)  
Thomas Köppe (co-editor) (Google DeepMind)  
Jens Maurer (co-editor)  
Dawn Perchik (co-editor) (Bright Side Computing, LLC)  
`<cxxeditor@gmail.com>`

## Acknowledgements

Special thanks to
Marshall Clow,
Jeff Garland,
and
Daniel Sunderland
for providing LaTeX sources for the LWG "Mandating" papers.

Special thanks to
Johel Ernesto Guerrero Peña
for reviewing the edits for many of the motions
and catching numerous issues.

Thanks to all those who have [submitted editorial
issues](https://github.com/cplusplus/draft/wiki/How-to-submit-an-editorial-issue)
and to those who have provided pull requests with fixes.

## New papers

 * [Nxxxx](http://wg21.link/nxxxx) is the committee draft for C++20. It replaces [N4835](http://wg21.link/n4835).
 * Nxxxx is this Editors' Report.

## Motions incorporated into working draft

### Core working group motions

CWG motion 1: [Core issue resolutions](http://wg21.link/p1969r0) for 4 issues in "ready" status applied: **(DR)**

 * [2280](http://wg21.link/cwg2280) Matching a usual deallocation function with placement `new`
 * [2382](http://wg21.link/cwg2382) Array allocation overhead for non-allocating placement `new`
 * [2416](http://wg21.link/cwg2416) Explicit specializations vs `constexpr` and `consteval`
 * [2441](http://wg21.link/cwg2441) Inline function parameters

CWG motion 2: [Core issue resolutions](http://wg21.link/p1968r0) for 18 issues in "ready" status applied, resolving 19 issues: **(DR)**

 * [1621](http://wg21.link/cwg1621) Member initializers in anonymous unions
 * [2126](http://wg21.link/cwg2126) Lifetime-extended temporaries in constant expressions
 * [2282](http://wg21.link/cwg2282) Consistency with mismatched aligned/non-over-aligned allocation/deallocation functions
 * [2347](http://wg21.link/cwg2347) Passing short scoped enumerations to ellipsis
 * [2374](http://wg21.link/cwg2374) Overly permissive specification of `enum` *direct-list-initialization*
 * [2399](http://wg21.link/cwg2399) Unclear referent of “expression” in *assignment-expression*
 * [2419](http://wg21.link/cwg2419) Loss of generality treating pointers to objects as one-element arrays
 * [2422](http://wg21.link/cwg2422) Incorrect grammar for *deduction-guide*
 * [2424](http://wg21.link/cwg2424) `constexpr` initialization requirements for variant members
 * [2426](http://wg21.link/cwg2426) Reference to destructor that cannot be invoked
 * [2427](http://wg21.link/cwg2427) Deprecation of volatile operands and unevaluated contexts
 * [2429](http://wg21.link/cwg2429) Initialization of `thread_local` variables referenced by lambdas
 * [2430](http://wg21.link/cwg2430) Completeness of return and parameter types of member functions
 * [2431](http://wg21.link/cwg2431) Full-expressions and temporaries bound to references
 * [2432](http://wg21.link/cwg2432) Return types for defaulted `<=>`
 * [2433](http://wg21.link/cwg2433) Variable templates in the ODR
 * [2437](http://wg21.link/cwg2437) Conversion of `std::strong_ordering` in a defaulted `operator<=>`
 * [2439](http://wg21.link/cwg2439) Undefined term in definition of "usable in constant expressions" **resolved by CWG 2126**
 * [2442](http://wg21.link/cwg2442) Incorrect requirement for default arguments

CWG motion 3: [Core NB comment resolutions](http://wg21.link/p1971r0), resolving 17 NB comments:

 * NB RU 007: Relax pointer value / aliasing rules
 * NB US 019: Update ISO 9899 document reference from C11 to C17
 * NB US 020: Update ISO 9899 document reference from C11 to C17
 * NB CA 038: Consider trailing *requires-clause*s for function identity
 * NB US 042: Relax pointer value / aliasing rules **in P1971R1 this is incorrectly listed as US047**
 * NB CZ 044: Allow constexpr `construct_at` / `destroy_at` for automatic storage duration
 * NB US 052: Non-executed `return` statements in coroutines
 * NB US 053: Mandate the return type for `return_void` and `return_value` to be `void`
 * NB US 065: Apply Coroutines TS issue 24 from [P0664R8](http://wg21.link/p0664r8)
 * NB GB 079: Add example for *private-module-fragment* **with editorial changes; see below**
 * NB US 087: Header unit imports cannot be cyclic, either
 * NB US 095: Equivalence of *requires-clause*s
 * NB US 109: Non-templates may also have associated constraints
 * NB CA 110: Associated constraints for non-template functions
 * NB US 111: Constraint normalization and negation
 * NB US 132: Macros from the command-line not exported by header units
 * NB US 367: Instead of header inclusion, also permit header unit import
 * NB CA 378: Remove constrained non-template functions

CWG motion 4: [P1972R0 "US105 Check satisfaction of constraints for non-templates when forming pointer to function"](http://wg21.link/p1972r0), resolving 1 NB comment:

 * NB US 105: Check satisfaction of constraints for non-templates when forming pointer to function

CWG motion 5: [P1975R0 "Fixing the wording of parenthesized aggregate-initialization"](http://wg21.link/p1975r0)

CWG motion 6: [P1874R1 "Dynamic initialization order of non-local variables in modules"](http://wg21.link/p1874r1), resolving 1 NB comment:

 * NB US 082: Define order of initialization for globals in modules

CWG motion 7: [P1946R0 "Allow defaulting comparisons by value"](http://wg21.link/p1946r0)

CWG motion 8: [P1907R1 "Inconsistencies with non-type template parameters"](http://wg21.link/p1907r1), resolving 5 NB comments: **with changes; see below**

 * NB US 092: Array members should have strong structural equality
 * NB US 093: Move definition of "strong structural equality" near its use in [temp.param]
 * NB US 100: Reference types should not have strong structural equality
 * NB US 102: Allow non-type template parameters of floating-point type
 * NB US 114: Class types as non-type template arguments

CWG motion 9: [P1979R0 "Resolution to US086"](http://wg21.link/p1979r0), resolving 1 NB comment:

 * NB US 086: Treatment of non-exported imports

CWG motion 10: [P1980R0 "Declaration matching for non-dependent *requires-clause*s"](http://wg21.link/p1980r0), resolving 2 NB comments:

 * NB US 095: Equivalence of *requires-clause*s
 * NB CA 096: Declaration matching for non-dependent *requires-clause*s

### Library working group motions

#### Issues

LWG motion 1: [Library issue resolutions](http://wg21.link/p1917r0) for 27 issues in "Ready" and "Tentatively Ready" status, resolving 3 NB comments:

 * [3070](http://wg21.link/lwg3070) `path::lexically_relative` causes surprising results if a filename can also be a *root-name*
 * [3103](http://wg21.link/lwg3103) Errors in taking subview of `span` should be ill-formed where possible
 * [3149](http://wg21.link/lwg3149) `default_constructible` should require default initialization
 * [3190](http://wg21.link/lwg3190) `std::allocator::allocate` sometimes returns too little storage
 * [3218](http://wg21.link/lwg3218) Modifier for `%d` parse flag does not match POSIX and format specification
 * [3221](http://wg21.link/lwg3221) Result of `year_month` arithmetic with `months` is ambiguous
 * [3222](http://wg21.link/lwg3222) [P0574R1](http://wg21.link/p0574r1) introduced preconditions on non-existent parameters
 * [3224](http://wg21.link/lwg3224) `zoned_time` constructor from `TimeZonePtr` does not specify initialization of `tp_`
 * [3225](http://wg21.link/lwg3225) `zoned_time` converting constructor shall not be `noexcept`
 * [3230](http://wg21.link/lwg3230) Format specifier `%y`/`%Y` is missing locale alternative versions
 * [3231](http://wg21.link/lwg3231) year_month_day_last::day specification does not cover !ok() values
 * [3232](http://wg21.link/lwg3232) Inconsistency in `zoned_time` deduction guides
 * [3235](http://wg21.link/lwg3235) `parse` manipulator without abbreviation is not callable
 * [3241](http://wg21.link/lwg3241) *chrono-spec* grammar ambiguity in [time.format]
 * [3244](http://wg21.link/lwg3244) Constraints for `Source` in [fs.path.req] insufficiently constrainty
 * [3245](http://wg21.link/lwg3245) Unnecessary restriction on `%p` parse specifier
 * [3246](http://wg21.link/lwg3246) What are the constraints on the template parameter of `basic_format_arg`?
 * [3253](http://wg21.link/lwg3253) `basic_syncbuf::basic_syncbuf()` should not be `explicit`
 * [3256](http://wg21.link/lwg3256) Feature testing macro for `constexpr` algorithms
 * [3257](http://wg21.link/lwg3257) Missing feature testing macro update from [P0858](http://wg21.link/p0858)
 * [3259](http://wg21.link/lwg3259) The definition of constexpr iterators should be adjusted
 * [3266](http://wg21.link/lwg3266) `to_chars(bool)` should be deleted
 * [3272](http://wg21.link/lwg3272) `%I%p` should parse/format `duration` since midnight
 * [3273](http://wg21.link/lwg3273) Specify `weekday_indexed` to range of [0, 7]
 * [3274](http://wg21.link/lwg3274) Missing feature test macro for `<span>`
 * [3276](http://wg21.link/lwg3276) Class `split_view::outer_iterator::value_type` should inherit from `view_interface`
 * [3277](http://wg21.link/lwg3277) Pre-increment on prvalues is not a requirement of `weakly_incrementable`
 * NB GB 166: Feature-test macro for `span` **resolved by LWG 3274**
 * NB US 261: Pre-increment on an rvalue iterator **resolved by LWG 3277**
 * NB US 297: `split_view::iterator::value_type` should inherit from `view_interface` **resolved by LWG 3276**

#### Papers

LWG motion 2: [P1855R0 "Make `<compare>` freestanding"](http://wg21.link/p1855r0), resolving 6 NB comments:
 * NB RU 009: Make `<compare>` a freestanding header
 * NB FI 010: Make `<compare>` a freestanding header
 * NB US 158: Ensure `<coroutine>` can be used as a freestanding header despite including `<compare>`
 * NB US 159: Make `<compare>` a freestanding header
 * NB GB 160: Make `<compare>` a freestanding header
 * NB PL 161: Make `<compare>` a freestanding header

LWG motion 3: [P1690R1 "Refinement proposal for P0919 heterogeneous lookup for unordered containers"](http://wg21.link/p1690r1), resolving 4 NB comments:

 * NB US 235: Heterogenous lookup using `Hash::transparent_key_equal` is problematic
 * NB US 236: Novel heterogenous lookup is problematic
 * NB PL 237: Novel heterogenous hash lookup is problematic
 * NB US 238: Heterogenous lookup using `Hash::transparent_key_equal` is problematic

LWG motion 4: [P1872R0 "`span` should have `size_type`, not `index_type`"](http://wg21.link/p1872r0), resolving 3 NB comments:

 * NB FR 240: Rename `span::index_type` to `span::size_type`
 * NB PL 248: Rename `span::index_type` to `span::size_type`
 * NB US 245: Rename `span::index_type` to `span::size_type`

LWG motion 5: [P1965R0 "Hidden friends"](http://wg21.link/p1965r0), resolving 1 LWG issue and 1 NB comment:

 * [3239](http://wg21.link/lwg3239) Hidden friends should be specified more narrowly
 * NB DE 165: Regular unqualified lookup of functions specified as friends

LWG motion 6: [P1716R3 "`ranges` comparison algorithms are over-constrained"](http://wg21.link/p1716r3), resolving 4 NB comments:

 * NB GB 183: Adopt P1716
 * NB US 267: Ranges compare algorithms are over-constrained
 * NB US 306: Relax constraints on ranges comparison algorithms
 * NB PL 312: Fix constraints on ranges comparison algorithms

LWG motion 7: [P1869R1 "Rename `condition_variable_any` interruptible wait methods"](http://wg21.link/p1869r1), resolving 1 NB comment:

 * NB PL 363: `wait_until` has misleading naming

LWG motion 8: [P1961R0 "Harmonizing the definitions of total order for pointers"](http://wg21.link/p1961r0), resolving 2 NB comments:

 * NB US 176: Harmonize definitions of total order for pointers
 * NB US 220: Harmonize definitions of total order for pointers

LWG motion 9: [P1878R1 "Constraining `readable` types"](http://wg21.link/p1878r1), resolving 1 LWG issue and 3 NB comments:

 * [3279](http://wg21.link/lwg3279) `shared_ptr<int>&` does not not satisfy `readable`
 * NB US 263: Make `shared_ptr<int>&` satisfy `readable`
 * NB US 264: Problems with `readable` concept
 * NB US 268: `iter_swap` should be callable with rvalue iterators

LWG motion 10: [P1871R1 "Concept traits should be named after concepts"](http://wg21.link/p1871r1), resolving 1 NB comment:

 * NB US 257: Avoid double negatives for ranges opt-in variable templates

LWG motion 11: [P1456R1 "Move-only views"](http://wg21.link/p1456r1), resolving 2 NB comments: **with changes; see below**

 * NB GB 277: Conflict of `istream_view` and `view` requirements
 * NB FR 281: Copyability of `view`

LWG motion 12: [P1391R4 "Range constructor for `std::string_view`"](http://wg21.link/p1391r4), resolving 1 NB comment:

 * NB US 232: Make `string_view` constructible from contiguous character ranges

LWG motion 13: [P1394R4 "Range constructor for `std::span`"](http://wg21.link/p1394r4), resolving 3 NB comments:

 * NB US 233: Integrate `span` constructors with range concepts
 * NB US 246: `span` should be constructible from a contiguous range
 * NB PL 251: `span` should be constructible from a contiguous range

LWG motion 14 was withdrawn.

LWG motion 15: [P1862R1 "Ranges adaptors for non-copyable iterators"](http://wg21.link/p1862r1)

LWG motions 11 and 15 together resolve 1 NB comment:

 * NB GB 270: Collateral damage with move-only input iterators

LWG motions 11-15 together resolve 2 NB comments:

 * NB US 272: API improvements for ranges
 * NB DE 288: Overspecification of return types of view adaptors

LWG motion 16: [P1870R1 "`forwarding-range<T>` is too subtle"](http://wg21.link/p1870r1), resolving 2 NB comments: **with changes; see below**

 * NB US 279: Use variable template opt-in for *`forwarding-range`*
 * NB GB 280: Rename *`forwarding-range`* to avoid near-clash with `forward_range`

LWG motion 17: [P1865R1 "Add `max()` to `latch` and `barrier`"](http://wg21.link/p1865r1), resolving 1 NB comment:

 * NB US 365: For `latch` and `barrier`, do not require full range of `ptrdiff_t`

LWG motion 18: [P1960R0 "NB comment changes reviewed by SG1"](http://wg21.link/p1960r0), resolving 5 NB comments:

 * NB US 355: Make `atomic_ref<T>::notify_one` and `atomic_ref<T>::notify_all` `const`
 * NB US 356: Make `atomic_ref<T>::is_lock_free` type-specific, not object-specifc
 * NB US 358: Make `atomic_ref<`*float*`>::operator=` `const`
 * NB US 359: Incorrect return value in specification of atomic increment / decrement
 * NB US 364: Clarify spurious failure for `try_acquire`

LWG motion 19: [P1902R1 "Missing feature-test macros 2017-2019"](http://wg21.link/p1902r1), resolving 6 NB comments: **with changes; see below**

 * NB FI 015: Missing feature-testing macros
 * NB GB 146: Add a feature-test macro for concepts
 * NB GB 147: Add a feature-test macro for `consteval`
 * NB US 150: Add feature-test macro for "familiar template syntax for generic lambdas"
 * NB US 167: Feature-test macro for non-member `ssize()`
 * NB DE 168: Feature-test macros for `constexpr`

LWG motion 20: [P0883R2 "Fixing atomic initialization"](http://wg21.link/p0883r2), resolving 1 LWG issue and 4 NB comments:

 * [2334](http://wg21.link/lwg2334) `atomic`'s default constructor requires "uninitialized" state even for types with non-trivial default-constructor
 * NB RU 006: Adopt P0883 (value-initialize atomics by default)
 * NB DE 018: Value-initialize atomics by default
 * NB US 351: Value-initialize atomics by default
 * NB CA 353: Value-initialize atomics by default

LWG motion 21: [P1959R0 "Remove `std::weak_equality` and `std::strong_equality`"](http://wg21.link/p1959r0), resolving 2 NB comments:

 * NB US 170: Remove `strong_equality` and `weak_equality`
 * NB CA 173: Remove `weak_equality`

LWG motion 22: [P1892R1 "Extended locale-specific presentation specifiers for `std::format`"](http://wg21.link/p1892r1), resolving 1 NB comment:

 * NB GB 226: Make locale-dependent formats for `std::format()` congruent with default formatting

LWG motion 23: [P1645R1 "`constexpr` for `<numeric>` algorithms"](http://wg21.link/p1645r1), resolving 1 NB comment:

 * NB US 320: Make numeric algorithms `constexpr`

#### Mandating

LWG motion 24: [P1718R2 "Mandating the standard library: Clause 25 - Algorithms library"](http://wg21.link/p1718r2)

LWG motion 25: [P1719R2 "Mandating the standard library: Clause 26 - Numerics library"](http://wg21.link/p1719r2)

LWG motion 26: [P1686R2 "Mandating the standard library: Clause 27 - Time library"](http://wg21.link/p1686r2)

LWG motion 27: [P1720R2 "Mandating the standard library: Clause 28 - Localization library"](http://wg21.link/p1720r2)

LWG motion 28: [P1721R2 "Mandating the standard library: Clause 29 - Input/Output library"](http://wg21.link/p1721r2)

LWG motion 29: [P1722R2 "Mandating the standard library: Clause 30 - Regular Expression library"](http://wg21.link/p1722r2)

LWG motion 30: [P1723R2 "Mandating the standard library: Clause 31 - Atomics library"](http://wg21.link/p1723r2)

LWG motion 31: [P1622R3 "Mandating the standard library: Clause 32 - Thread support library"](http://wg21.link/p1622r3)

## Notable changes to papers as moved

### CWG motion 3

The note added as part of the resolution of NB GB 079 was reworded editorially,
as described below in the list of editorial NB comment resolutions.

### CWG motion 8

The following feature test macro changes were made for this paper,
after consultation with SG10:

The feature test macro `__cpp_nontype_template_parameter_class` has been removed
to indicate that the feature added by [P0732R2](http://wg21.link/p0732r2)
is no longer present in the same form.

The value of the feature test macro `__cpp_nontype_template_args` has been increased
to `201911L` to indicate support for [P1907R1](http://wg21.link/p1907r1).

### LWG motion 11

The description of this paper specifies that:

> each such `base()` member [of a range adaptor, that returns a copy of the underlying view]
> be replaced to by two overloads:
> a `const`-qualified overload that requires the type of the underlying view to model CopyConstructible, and
> a `&&`-qualified overload that extracts the underlying view from the adaptor

but the wording changes omitted explicit editing instructions
to make these changes to the
`take_while_view`, `drop_view`, `drop_while_view` and `elements_view`
range adaptors, which were added by [P1035R7](http://wg21.link/p1035r7)
(2019-07 LWG Motion 23), after R0 of this paper was authored.

Consistent with the proposal in the paper,
and after consulting the paper authors and the LWG chair,
the corresponding changes were also applied to
the additional range adaptors listed above.

### LWG motion 16

This paper removed the exposition-only concept *`range-impl`*,
inlining it into its only remaining user, the `range` concept.
However, two uses of *`range-impl`* were left behind.
These have been updated and suitably adjusted
to refer to `range` instead.

LWG motion 13 ([P1394R4](http://wg21.link/p1394r4))
added a couple of new uses of
the exposition-only concept *`forwarding-range`*,
which was removed by this paper.
These uses have been replaced with `safe_range`.

### LWG motion 19

Did not add the macro `__cpp_lib_atomic_ref`.
This macro already existed with the specified value.

Did not change the value of the `__cpp_lib_chrono` macro.
The requested new value of this macro (`201803L`)
is actually lower than the current value
(`201907L`, not `201611L` as listed in [P1902R1](http://wg21.link/p1902r1)).
The chair of SG10 has confirmed that the request to change this macro's value
is an error. The pre-existing, higher value is retained.

Did not change the value of the `__cpp_lib_ranges` macro.
The requested new value of this macro (`201907L`)
is lower than the value `201911L` introduced by
[P1716R3](http://wg21.link/po1716r3) (LWG motion 6).

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

 * **Modified resolution:**
   Added a cross-reference to [using.headers] instead of
   the suggested cross-reference to [headers].

JP 023: Accepted, fixed in 868934f7.

JP 030: No consensus for change.

 * The text immediately following the grammar makes it clear that
   both lowercase `p` and uppercase `P` are permitted.

US 031: No consensus for change.

 * The example appears to be valid as-is;
   adding `!= 0` does not appear to serve any purpose.

GB 032: Accepted, fixed in 84a1cd53.

US 037: No consensus for change.

 * The proposed change is not editorial.
   Forwarded to SG2 for consideration and rejected.

FR 039: Accepted with modifications, fixed in 68a6dfef.

 * **Filed as technical**; SG2 concluded the wording is confusing,
   already does what the comment requests
   (except that ADL also finds friend declarations in a class
   in the same conditions under which
   member lookup would find member declarations in the class).
   Recategorized as editorial to clarify the wording.

 * **Modified resolution:**
   Definition of "interface" (of a module) inlined into its only use (and removed),
   making it clear that [basic.lookup.argdep]/4.4 only finds exported declarations.

JP 045: Accepted, fixed in d401794f.

 * This fixes a misapplication of the resolution of CWG 2381.

US 047: Accepted with modifications, fixed in 785f689d.

 * **Modified resolution:**
  Instead of removing the redundant sentence, it was converted into a note
  and moved after the following sentence of which it is a consequence.

US 052: Accepted, fixed by [P1971R0](http://wg21.link/p1971r0) (CWG motion 3).

 * The proposed change is not editorial.
   Forwarded to CWG for consideration and accepted.

JP 057: Accepted, fixed in a06b7a49.

GB 078: Accepted, fixed in e3bb2eba.

 * Italicized references to *digit*s that intended to refer to the grammar production.
 * Also made some nearby editorial improvements:
   added cross-references and fixed an adjacent grammar issue ("is" / "are") in [diff.cpp14.library].

GB 079: Accepted, fixed by [P1971R0](http://wg21.link/p1971r0) (CWG motion 3).

 * Forwarded to SG2 for consideration. Accepted and example added by CWG.
 * Added note prior to example editorially revised after consultation with CWG.

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

US 106: No consensus for change.

 * Forwarded to CWG for consideration and rejected.

US 108: Accepted, fixed in 2f42a930.

US 153: No consensus for change.

 * Forwarded to LWG for consideration; rejected by LEWG.

US 154: Duplicate of US 153.

GB 155: Accepted, fixed in 98e57ff5.

 * **LWG concurs with this direction**

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

US 216: Accepted, fixed in dfcc4691.

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

US 258: Accepted, fixed in f36f871c.

GB 280: Accepted, fixed by [P1870R1](http://wg21.link/p1870r1) (LWG motion 16).

 * Forwarded to LEWG to select a better name or reject,
   LEWG selected `safe_range` as a replacement non-exposition-only concept name.

US 295: Accepted with modifications, fixed in 53f0651e.

 * Instead of proposed change, incorporated the leading
   "If `ref_is_glvalue` is `true`" into the bullets
   and removed the bullet nesting
   to clarify the meaning of the "Otherwise"s.

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

JP 338: Accepted, fixed in 742f1086.

JP 339: Accepted, fixed in 25a08918.

JP 340: Accepted, fixed in f88f6747.

JP 341: Accepted, fixed in d545c37d.

JP 343: Accepted, fixed in 9252441e.

JP 348: Accepted, fixed in 01dea5f5.

 * Per [iosfwd.syn]p1, the duplication of default template arguments
   between `<iosfwd>` and `<syncstream>`
   does not prevent a translation unit including both.
 * An LWG issue will be opened to consider
   whether we should require more of the iostreams headers to include `<iosfwd>`;
   currently only `<ios>` and `<iostream>` are guaranteed to provide the forward declarations.
   Similarly LWG should consider whether `<istream>` and `<ostream>` should
   be guaranteed to include `<ios>`.

JP 349: Accepted, fixed in adcf12ea.

 * See JP 348.

JP 350: Accepted, fixed in 53b429c9.

 * See JP 348.

US 357: Accepted with modifications, fixed in af747d64.

 * **Modified resolution:**
   A different revised wording was chosen for the notes:
   "The specialization `atomic<bool>` uses the primary template."

US 359: Accepted, fixed by [P1960R0](http://wg21.link/p1960r0) (LWG motion 18).

 * Forwarded to SG1 for consideration and accepted by LWG.

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

### Late comments

CH 02: Accepted, fixed in 5ee93fd7.

## Notable editorial changes

### Typeface

The typeface used for grammar productions has been changed
from italic to a slanted sans-serif font
in order to distinguish grammar productions
from defined terms.
Many other options have been considered,
but this option provided the most visually appealing outcome.

Please inform the editors if you discover
any places where the wrong typeface is used
for a grammar production or other italicized term.

### Section moves

Moved [temp.deduct.guide] under [temp.class],
alongside the description of members of class templates.

Moved [range.istream] under [range.factories].
`basic_istream_view` is a range factory not a range adaptor.

### Section label changes

 * [module.global] -> [module.global.frag]
 * [cpp.glob.frag] -> [cpp.global.frag]

## Minor editorial fixes

A log of editorial fixes made to the working draft since N4835 is below.
This list excludes changes
that do not affect the body text or only affect whitespace or typeface. For a
complete list including such changes (or for the actual deltas applied by these
changes), consult the [draft sources on github](https://github.com/cplusplus/draft/compare/n4835...nxxxx).
