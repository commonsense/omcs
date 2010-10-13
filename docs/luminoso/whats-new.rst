What's new in Luminoso 1.3?
===========================

Luminoso 1.3 was released on September 27, 2010. There have been some minor bug
fixes since then, so the current version is 1.3.2. This version makes many
changes from version 1.2.

**Changes to the semantic model:**

- Concepts are now weighted using TF-IDF normalization.
- Centrality is now calculated by creating an "average document" and comparing
  all documents to it. Previously, it would compare all documents to all other
  documents, which was less statistically justifiable.
- Tags. Often you want to distinguish different kinds of documents from each
  other. For example, your documents may come from people reacting to two
  different stimuli, "version A" and "version B". You can now mark these with
  tags like `#versionA` and `#versionB`. Anything beginning with a hash sign
  will pass through the text processing step completely unchanged, and will not
  bring in common-sense semantic associations. You can also add the opposite of
  a tag by adding a hyphen after the hash sign -- for example, you could encode
  a survey response about whether people would or would not recommend something
  as `#WouldRecommend` and `#-WouldRecommend`.
  
  Tags make great canonical documents.

**Interface changes:**

- You can now change the "concept threshold", which is the number of times a
  word or phrase must appear in the documents to be considered as a concept in
  the study. The default value, 2, is reasonable for small studies; turn it up
  as your study gets larger.
- When a concept is selected, it now shows gray lines to other related
  concepts (in addition to the blue lines to the documents that include it,
  and the red lines to the documents that include its negation).
- Axes no longer show up much further from the origin than concepts and
  documents.
- More points are labeled at one time.
- (Luminoso 1.3.1) Made it easier to work with Luminoso from the command line.
  See :doc:`/luminoso/power-users`.

**Bug fixes:**

- (Luminoso 1.3.2) Made tags associate throughout the document, not just to
  nearby words.
- (Luminoso 1.3.1) Version 1.3.0 was ignoring the word "not". This is fixed
  now.
- Luminoso will complain but not crash when you load something that isn't a
  study.
- It no longer crashes when a "core concept" or "interesting concept" contains
  a non-ASCII character. Report files are now fully Unicode.

Previous changes
----------------

Luminoso 1.2
............

Luminoso 1.2, released May 27, 2010, has many changes over previous versions.
In some cases, you will benefit from changing your studies accordingly.

- We use a new model for reading in your data and blending it with ConceptNet,
  called "spectral association". This understands differences in emotion
  much better than the previous model, and also recognizes that there can be
  positive and negative sentences in the same document.
- "Congruence" is now known as "centrality". It has basically the same
  definition, except for the fact that the underlying model is different.
- The results page identifies "interesting concepts" for each canonical
  document. These are concepts that show up in a relatively high number of
  related documents, and it tells you what percentage of related documents that
  is.
- Concepts now have their own info pages. When you click a concept, it will
  show similar concepts, and which documents the concept came from, in the
  info pane.
- Studies no longer explode when you change them and try to re-analyze.
- The backend uses :doc:`/divisi2/index.rst <divisi2>` instead of divisi. This
  has various benefits, including making already-computed matrices load faster.

