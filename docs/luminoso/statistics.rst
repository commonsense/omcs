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

The *consistency* measurement goes along with this: it expresses how *broad*
your space of document meanings is, by measuring the average similarity of all
documents with each other on a scale from -1.0 to 1.0.

The ideas of "core concepts" and "consistency" make the most sense in a blend:
that is, a space that contains both a set of documents and a file containing
general knowledge such as `conceptnet.pickle`. Without the general knowledge,
the space will be entirely made from your documents; there will be no
particular meaning to how broad the space is, and the concepts that end up in
the "center" may have no particular significance.

Centrality
----------
.. note::

   This was formerly known as "congruence".

When you use canonical documents, you may be particularly interested in whether
these documents are central to your space or not. In other words, do these
documents represent common topics, or uncommon ones, in your set of data?

Centrality is a statistical measure that measures how central each canonical
document is, compared to all documents in general. This amounts to comparing
two distributions of similarity scores with each other, so we can use the
statistical measure called the Z-test that is designed for this purpose.

A centrality score is a positive or negative number. A document with positive
centrality is more centrally located than the average document; a document with
negative centrality is less.  If the centrality value is greater than about 1.7
or less than about -1.7, it is statistically significant at a 95% confidence
level. Use 2.4 instead of 1.7 to get 99% confidence.

Example: testing for positive emotion
.....................................
In Luminoso 1.2, this has become much easier. Create a file called
:file:`positive-emotion.txt` in your Canonical directory. It will have this
form: ``a few clearly positive words, NOT a few clearly negative words``.

As long as some of the words appear in ConceptNet, Luminoso will be able to
generalize from them to many related words, so you no longer need a huge, messy
list of examples of positive and negative emotion. It can also be useful to add
some words that are particular to the domain.

Here's what we use for :file:`positive-emotion.txt`::

    good like love enjoy happy nice easy,
    NOT bad dislike hate sad angry hard difficult
    
The congruence score of `positive-emotion.txt`, then, will show whether it is
typical for your documents to express positive emotions. If its congruence
value is over 2.4, you can say with 99% confidence that they do.

