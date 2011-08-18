==========================
C++ Standard Draft Sources
==========================

These are the sources used to generate drafts of the C++
standard. These sources should not be considered an ISO publication,
nor should documents generated from them unless officially adopted by
the C++ working group (ISO/IEC JTC1/SC22/WG21).

------------
Instructions
------------

To regenerate figures from .dot files, run::

   dot -o<pdfname> -Tpdf <dotfilename>

For example::

   dot -ofigstreampos.pdf -Tpdf figstreampos.dot

To regenerate the grammar appendix, run the following from the source
directory::

   ../tools/makegram

To regenerate the cross-references appendix, run the following from
the source directory::

   ../tools/makexref

To typeset the draft document:

#. run ``pdflatex std`` until there are no more changed labels or changed tables
#. run ``makeindex generalindex``
#. run ``makeindex libraryindex``
#. run ``makeindex grammarindex``
#. run ``makeindex impldefindex``
#. run ``pdflatex std`` twice more.

----------------
Acknowledgements
----------------

A great deal of gratitude goes out to Pete Becker for his amazing work
in the original conversion of the C++ standard drafts to LaTeX, and
his subsequent maintenance of the standard drafts up to C++11. Thank
you Pete.
