.. _walkthrough:

Luminoso step-by-step
=====================

You can use Luminoso on any set of plain-text documents. Luminoso will analyze
the words and short phrases in those documents, and create a semantic space
from them.

This document explains how to create and analyze a study, and what you can do
with it once you have done so.

Step 1: Create a new study
--------------------------
When Luminoso has loaded, click the "New Study" button. This will prompt you
for a directory name for where to save the study.

A Luminoso study is a directory (folder), containing the following:

Canonical/
    A directory in which you can put documents with known semantics, so that
    you can compare your other documents to them.

Documents/
    The directory where you should put the text documents that comprise your
    study.

Matrices/
    This directory contains other matrices that you want to "blend" into the
    analysis, to help define the semantic space. These matrices are stored as
    .pickle files of the kind that can be saved from Divisi.
    
    By default, a matrix representing ConceptNet will be here -- we have found
    that blending with ConceptNet can help establish semantic similarities,
    especially when there is a small number of documents. You can delete the
    ConceptNet matrix if you do not want to blend with

Results/
    Luminoso will place its analysis results here, in various formats.

Step 2: Add files
-----------------
The next step is to add documents to your study.

Luminoso does not attempt to be a file manager -- instead, clicking "Edit
Study" will open the file manager your operating system already uses, in the
study folder. You can then add any number of plain-text documents to the
Documents/ folder.

Step 3: Analyze
---------------
Click the "Analyze" button. This will construct a Divisi matrix from your data
and prepare the visualization. This process may take a minute or two.

(If for some reason the analysis fails halfway through, you might need to
remove files from the Results/ directory before trying again. Please tell us
about any bugs that might cause this to be necessary.)

The "Info" panel will then contain some statistics about your documents. See
:ref:`statistics` for more information about what
these statistics mean.

Step 4: Explore
---------------
After the analysis is done, the viewer will appear, where your documents and
the concepts they contain appear as points in a many-dimensional space.

The points will be scattered around the origin. Points that appear farther
from the origin are considered more relevant. Points that appear in the same
*direction* from the origin are those that are similar to each other.

Though this space has many dimensions, you can only see a few of them at a
time. The viewer will start by automatically choosing an X and Y axis that it
considers interesting. To show differences between things that do not appear in
this two-dimensional projection, it will also assign colors to the points,
representing their location in three more dimensions.

Some of the points will be labeled, with preference given to points near your
mouse pointer. You can move the mouse to see other labels.

You can change the two-dimensional projection that puts points on your screen
in a few ways:

- You can "grab" a concept or document by clicking and dragging the mouse. The
  projection will then rotate and stretch so that that concept follows the
  mouse, and the similar concepts will come along with it.

- You can choose particular directions to be the X and Y axes from the dropdown
  menus. "Default" means what it was in the original view. You can also choose
  particular principal components. (In blends with ConceptNet, note that the
  first few principal components may not make interesting distinctions over
  your documents -- they will simply distinguish your documents from the rest
  of the body of general knowledge.)

When you click and hold the mouse on a point, the other points will be
re-colored on a sort of "heat" scale. The brightest colored points are the ones
that are most similar to the concept you selected.

Step 5: Experiment with canonical documents
-------------------------------------------
Canonical documents are example documents that you supply. You can use them to
help find your way in the space, by labeling directions that have a particular
meaning.

Luminoso will calculate "congruence" statistics about how the documents relate
to your canonical documents, and lets you set a given canonical document as the
X or Y axis.

When possible, canonical documents should be written in the style of other
documents. For example, in a database of reviews, you can write a canonical
"good review" representing the favorable things you hope someone would say.
In this way, both the words and the phrases will line up with other documents,
making it possible to achieve a high congruence score.

However, a canonical document can also be just a set of related words that are
not connected by sentences, such as "car train bus taxi". You can think of this
as defining a vector that represents the "category" containing all those words.
