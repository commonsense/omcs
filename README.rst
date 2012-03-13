`Open Mind Common Sense`_
=========================

.. _`Open Mind Common Sense`: http://csc.media.mit.edu

When people communicate, they rely on a large body of shared common sense
knowledge in order to understand each other. Many barriers we face today in
artificial intelligence and user interface design are due to the fact that
computers do not share this knowledge. To improve computers' understanding of
the world that people live in and talk about, we need to provide them with
usable knowledge about the basic relationships between things that nearly every
person knows.

In 1999, we began a project at the MIT Media Lab to collect common sense from
volunteers on the internet. Nearly ten years later our project has expanded to
encompass many different areas, languages, and problems. Currently, our English
dataset has over a million sentences from over 15,000 contributors. We have
expanded far beyond the original Web site, but we are still collecting
knowledge at http://openmind.media.mit.edu.

Subprojects
-----------

OMCS includes the following subprojects, among others:

- conceptnet_: A semantic network of the knowledge we have collected.
- simplenlp_: Lightweight natural language processing tools.
- divisi2_: A library for learning from dimensionality reduction of a semantic network.
- csc-utils_: Useful tools shared between our projects.
- openmind-commons_: The code of our Web site for browsing and collecting knowledge.

.. _conceptnet: http://github.com/commonsense/conceptnet
.. _simplenlp: http://github.com/commonsense/simplenlp
.. _csc-utils: http://github.com/commonsense/csc-utils
.. _divisi2: http://github.com/commonsense/divisi2
.. _openmind-commons: http://github.com/rspeer/openmind-commons

Non-core subprojects
--------------------

The following projects are also in the OMCS namespace but are not
currently managed as subprojects:

- divisi_: The old version of Divisi, no longer supported.
- LexiconLinking_: A project to learn a lexicon of verb classes and the nouns that they relate to.

.. _divisi: http://github.com/commonsense/divisi
.. _LexiconLinking: http://github.com/commonsense/LexiconLinking

About this repository
=====================

This is the top-level project for Open Mind Common Sense. All of the
actual code is in submodules. To check out or update its contents, run
``./update`` (requires a recent version of git). To install everything,
decide if you want the equivalent of ``python setup.py develop`` or
``python setup.py install``, and run one of ``./develop`` or ``./install``.

The git submodule system is a bit strange in that it checks out
commits instead of branches. This means checkouts start in
"disconnected head" mode, which makes it too easy to lose work. You
may want to do something like the following::

    git submodule foreach git checkout master

If not, at least make a branch for your own work first::

  git checkout -b universal_semantics

Alternatively, you can install the submodules into your Python environment 
using ``pip``. See ``requirements.txt`` or ``devel_requirements.txt``.
