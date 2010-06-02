What's new in Luminoso 1.2?
===========================
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

