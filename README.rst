==========================
C++ Standard Draft Sources
==========================

These are the sources used to generate drafts of the C++
standard. These sources should not be considered an ISO publication,
nor should documents generated from them unless officially adopted by
the C++ working group (ISO/IEC JTC1/SC22/WG21).

Get involved:

- `How to submit an editorial issue <https://github.com/cplusplus/draft/wiki/How-to-submit-an-editorial-issue>`_
- `How to tell if an issue is editorial <https://github.com/cplusplus/draft/wiki/How-to-tell-if-an-issue-is-editorial>`_
- `How to submit a new issue/defect report <http://isocpp.org/std/submit-a-library-issue>`_ for non-editorial issues

More information about the C++ standard can be found at `isocpp.org <http://isocpp.org/std>`_.

---------------------------
Getting Started on Mac OS X
---------------------------

Install the `MacTeX distribution <http://tug.org/mactex/>`_.

If you are on a slow network, you'll want to get the `BasicTeX package <http://tug.org/mactex/morepackages.html>`_ instead,
then run the following command to install the other packages that the draft requires:

   sudo tlmgr install latexmk isodate substr relsize ulem fixme rsfs

------------
Instructions
------------

To typeset the draft document, from the ``source`` directory:

#. run ``latexmk -pdf std``

That's it! You should now have an ``std.pdf`` containing the typeset draft.

Alternative instructions
========================

If you can't use latexmk for some reason, you can use the Makefiles instead:

#. run ``make rebuild``
#. run ``make reindex``

If you can't use latexmk or make for some reason, you can run LaTeX manually instead:

#. run ``pdflatex std`` until there are no more changed labels or changed tables
#. run ``makeindex generalindex``
#. run ``makeindex libraryindex``
#. run ``makeindex grammarindex``
#. run ``makeindex impldefindex``
#. run ``pdflatex std`` twice more.

Generated input files
=====================

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

----------------
Acknowledgements
----------------

A great deal of gratitude goes out to Pete Becker for his amazing work
in the original conversion of the C++ standard drafts to LaTeX, and
his subsequent maintenance of the standard drafts up to C++11. Thank
you Pete.

Thanks to Walter Brown for suggesting the use of ``latexmk``.
