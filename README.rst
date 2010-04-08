Open Mind Common Sense
======================
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
- divisi_: A library for learning from dimensionality reduction of a semantic network.
- divisi2_: A new version of Divisi that integrates with NumPy and PySparse.
- csc-utils_: Useful tools shared between our projects.

.. _conceptnet: http://github.com/commonsense/conceptnet
.. _csc-utils: http://github.com/commonsense/csc-utils
.. _divisi: http://github.com/commonsense/divisi
.. _divisi2: http://github.com/commonsense/divisi2

About this repository
=====================

This is the top-level project for Open Mind Common Sense. All of the actual
code is in submodules. To check out its contents, run::

  git submodule init
  git submodule update

Alternatively, you can install the submodules into your Python environment 
using ``pip``. See `requirements.txt` or `devel_requirements.txt`.

