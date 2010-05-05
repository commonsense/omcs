.. _statistics:

Statistics
==========
Luminoso measures various kinds of statistics about your data, which appear in
the Info pane. These show up when the study is done analyzing, and you can get
back to this page by choosing **Show Study Info** from the **Study** menu.

Core concepts
-------------
The set of documents that define your study will generally occupy some subset
of the full range of AnalogySpace, because the documents will have meanings in
common. Understanding the space your documents occupy within AnalogySpace can
help to understand what to look for in your data.

At the top of the info page, you will find the *core concepts*. These are the
concepts whose meanings are most centrally located in your set of documents.
This will be a recurring idea that we use in these statistics, and we can
compute this by calculating the *average similarity* between each concept
vector and all the other concepts in the space. The concepts that are most
similar to everything else -- and therefore most central -- are listed as the
core concepts.

.. note:: We may revise the way we calculate this list of core concepts soon,
   in order to emphasize more frequent concepts. Right now, it can choose some
   very infrequent concepts that are not representative of what is really going
   on in the set of documents.

The *consistency* measurement goes along with this: it expresses how *broad*
your space of document meanings is, by measuring the average similarity of all
documents with each other on a scale from -1.0 to 1.0.

The ideas of "core concepts" and "consistency" make the most sense in a blend:
that is, a space that contains both a set of documents and a file containing
general knowledge such as `conceptnet.pickle`. Without the general knowledge,
the space will be entirely made from your documents; there will be no
particular meaning to how broad the space is, and the concepts that end up in
the "center" may have no particular significance.

Congruence
----------
When you use canonical documents, you may be particularly interested in whether
these documents are central to your space or not. In other words, do these
documents represent common topics, or uncommon ones, in your set of data?

Congruence is a statistical measure that measures how central each canonical
document is, compared to all documents in general. This amounts to comparing
two distributions of similarity scores with each other, so we can use the
statistical measure called the Z-test that is designed for this purpose.

A congruence score is a positive or negative number. A document with positive
congruence is more centrally located than the average document; a document with
negative congruence is less.  If the congruence value is greater than about 1.7
or less than about -1.7, it is statistically significant at a 95% confidence
level. Use 2.4 instead of 1.7 to get 99% confidence.

Example: testing for positive emotion
.....................................
If you want to see if your documents are generally expressing positive or
negative emotions, use :file:`positive-emotion.txt` (included with Luminoso) as
a canonical document. This document contains a number of words labeled as
positive in Affective WordNet, followed by the keyword "NOT" and a number of
words labeled as negative, so it should end up pointing in a direction
representing positive emotion in your space.

The congruence score of `positive-emotion.txt`, then, will show whether it is
typical for your documents to express positive emotions. If its congruence
value is over 2.4, you can say with 99% confidence that they do.

