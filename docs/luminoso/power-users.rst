Scripting with Luminoso (for power users)
=========================================

Behind the scenes, Luminoso is running :doc:`divisi2 </divisi2/index>` on a
matrix that it builds from your documents and from common sense.

If you want to examine Luminoso's results with Python -- for example, because
you want to be able to look up the similarity of any two points in your space,
or to compare results between many different runs of Luminoso, you can do this
by loading your Luminoso results with divisi2.

This also lets you work with Luminoso entirely from the command line, in a
situtation where you don't want to or can't use the GUI.

Setup
-----
You will need to install Divisi2 and Luminoso as Python packages. This will be
simpler than the full build process for Luminoso, because you don't need PyQt4
or its dependencies. See :ref:`command-line-luminoso`.

Creating a study
----------------
A study is a directory that must contain subdirectories with particular names.
You can get an empty study in a few ways:

- At the command line: Copy the "study_skel" directory out of Luminoso.
- In Python: `from luminoso.study import StudyDirectory; StudyDirectory.make_new(dirname)`
- By using any other tools to make a directory that conforms to the
  :doc:`Luminoso study layout </luminoso/study-layout>`.

Running a study
---------------
By now you've installed Luminoso and made your study. Let's suppose the name of
your study directory is "MyStudy".

At your command line, go to the directory containing MyStudy and type::

    luminoso-study MyStudy

Various progress information will appear on the screen, and if all goes well,
you will be uneventfully returned to the command line. What's different now is
that the Results directory of your study contains your results.

Accessing the results
---------------------
Luminoso outputs its results in several files, some of which may be
useful to you. The files with extensions `.dvec`, `.dmat`, `.smat`, and `.rmat`
are vectors and matrices that can be loaded with Divisi2.

- `documents.smat`: a :doc:`SparseMatrix </divisi2/sparse>` whose rows are
  documents and whose columns are concepts. The entries indicate how many times
  each concept appears in each document.
- `spectral.rmat`: a symmetrical :doc:`ReconstructedMatrix </divisi2/reconstruct>`
  expressing how strongly every concept and every document are associated with
  each other. (The obscure name comes from our technique of "spectral
  association".)
- `projections.dmat`: a :doc:`DenseMatrix </divisi2/dense>` whose rows are
  concepts and documents, and whose columns are axes (also known as principal
  components or eigenvectors). This gives the coordinates of every concept and
  document in the space.
- `magnitudes.dvec`: a vector of eigenvalues that goes with `projections.dmat`.
  This expresses the magnitude of each axis (how much of the data it accounts
  for), which you may need if you want to do matrix operations on the data
  yourself.
- `stats.json`: contains the statistics that Luminoso calculates, including the
  consistency and correlation for each canonical document. This is a standard
  JSON file, so you can load it with any JSON reader, including Python 2.6's
  `json.load`, or even simply `eval`.
- `report.html`: a human-readable version of `stats.json`.

To load one of the Divisi2 files, you use the `divisi2.load` function. See the
next section for an example.

Example
-------
Let's access the ThaiFoodStudy results at the Python prompt::

    >>> from csc import divisi2
    >>> assoc = divisi2.load('ThaiFoodStudy/Results/spectral.rmat')
    >>> print assoc
    <ReconstructedMatrix: 372 by 372>

We can look for associations between concepts by examining rows of this
ReconstructedMatrix. For example, to see the strongest associations with the
concept "curry"::

    >>> print assoc.row_named('curry').top_items()
    [(u'curry', 0.99999999999999989), (u'crispy', 0.99182961432896466),
     (u'egg noodle', 0.98721328226393767),
     (u'noodle dish', 0.98689402327077547), (u'watery', 0.98686111284616118),
     (u'pancake', 0.98444444661922803), (u'shrimp', 0.98428171042567703),
     (u'scallion pancake', 0.98202248820385074),
     (u'peanut sauce', 0.98075292713607232), (u'noodle', 0.98029932202575432)]

To see the things that are most associated with the canonical document
"good_review.txt"::

    >>> print assoc.row_named('good_review.txt').top_items(8)
    [('good_review.txt', 1.0), ('jessicar.txt', 0.97577833964984861),
     ('sandrac.txt', 0.9580045079574262),
     (u'quick', 0.9505259843376358),
     ('ruthp.txt', 0.94588831590264377),
     (u'good vegetarian', 0.94541634793231299),
     (u'vegetarian option', 0.94541634793231288),
     (u'vegetarian', 0.94389482721261653)]

And finally, to see the strength of the relationship between "curry" and
"good_review.txt" (which may indicate what reviewers think of the curry)::

    >>> print assoc.entry_named('curry', 'good_review.txt')
    0.68903313654

