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
- `How to submit a new issue/defect report <https://isocpp.org/std/submit-issue>`_ for non-editorial issues

More information about the C++ standard can be found at `isocpp.org <http://isocpp.org/std>`_.

---------------------------
Getting Started on Mac OS X
---------------------------

Install the `MacTeX distribution <http://tug.org/mactex/>`_.

If you are on a slow network, you'll want to get the `BasicTeX package <http://tug.org/mactex/morepackages.html>`_ instead,
then run the following command to install the other packages that the draft requires:

   sudo tlmgr install latexmk isodate substr relsize ulem fixme rsfs extract layouts enumitem l3packages l3kernel imakeidx splitindex xstring

---------------------------------------
Getting Started on Debian-based Systems
---------------------------------------

Install the following packages:

   sudo apt-get install latexmk texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended lmodern

-------------------------
Getting Started on Fedora
-------------------------

Install the following packages:

   dnf install latexmk texlive texlive-isodate texlive-relsize texlive-ulem texlive-fixme texlive-extract texlive-l3kernel texlive-l3packages texlive-splitindex texlive-imakeidx

-----------------------------
Getting Started on Arch Linux
-----------------------------

Install the following packages:

   pacman -S texlive-latexextra

-----------------------------
Getting Started on Microsoft Windows
-----------------------------

Install Perl (for example, using a `Cygwin installation <https://cygwin.com/install.html>`_ and adding perl.
See `sample instructions <https://bennierobinson.com/programming/2016/01/24/perl-windows-2016.html>`_ for more details)

Install `MiKTeX <https://miktex.org/download>`_

------------
Instructions
------------

To typeset the draft document, from the ``source`` directory run::

  make

That's it! You should now have an ``std.pdf`` containing the typeset draft.

Generated input files
=====================

To regenerate figures from .dot files, run::

   make <pdfname>

For example::

   make figvirt.pdf

----------------
Acknowledgements
----------------

A great deal of gratitude goes out to Pete Becker for his amazing work
in the original conversion of the C++ standard drafts to LaTeX, and
his subsequent maintenance of the standard drafts up to C++11. Thank
you Pete.

Thanks to Walter Brown for suggesting the use of ``latexmk``.
