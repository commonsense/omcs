Tutorial: Getting Started
=========================

Once you've `built and installed <install.html>`_ Divisi, you can start
by making your own AnalogySpace.

1. Download the `ConceptNet matrix data for English <http://conceptnet.media.mit.edu/dist/en_tuples.gz>`_.
2. Load it:

>>> from csc import divisi
>>> matrix = divisi.load('en_tuples.gz')

3. Run the SVD:

>>> concept_axes, axis_weights, feature_axes = matrix.normalize_all().svd(k=100)

4. Get similar concepts (to 'teach'):

>>> teach = concept_axes.row_named('teach').weighted(axis_weights)
>>> similarities = concept_axes.weighted(axis_weights).dot(teach)
>>> similarities.top_items(10)

Or:

>>> sim_matrix = divisi.reconstruct_similarity(concept_axes, axis_weights)
>>> sim_matrix.row_named('teach').top_items(10)

5. Predict properties (for 'trumpet'):

>>> trumpet = concept_axes.row_named('trumpet').weighted(axis_weights)
>>> predictions = feature_axes.dot(trumpet)
>>> predictions.top_items(10)

Or:

>>> predict_matrix = divisi.reconstruct(concept_axes, axis_weights,
...                                     feature_axes)
>>> predict_matrix.row_named('trumpet').top_items(10)

(These things that look like `('right', 'IsA', 'pet')` are how we represent the
*features* in ConceptNet.)

6. Evaluate possible assertions::

>>> predict_matrix = divisi.reconstruct(concept_axes, axis_weights,
...                                     feature_axes)

Is a dog a pet?

>>> predict_matrix.entry_named('dog', ('right', 'IsA', 'pet'))

Is a hammer a pet?

>>> predict_matrix.entry_named('hammer', ('right', 'IsA', 'pet'))

.. note::

   The concepts are represented by their *normalized form*, which is how
   they are represented internally in ConceptNet.
   
   If you look up a value for "scissors", for example, you won't find anything.
   It's under "scissor".
   The reason for this is so that phrases like "eat a
   sandwich" and "eating sandwiches" correspond to the same
   concept. See :ref:`nl` for details on how this works.
