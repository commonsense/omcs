Tutorial: Measuring similarity
==============================

One useful thing to do with AnalogySpace is to compute the similarity of
different concepts and features.

First we create a matrix of ConceptNet by loading it from the database. This
assumes you have the Python code for ConceptNet 4 installed.

>>> from csc.conceptnet.analogyspace import conceptnet_tuples
>>> cnet_tuples = conceptnet_tuples('en')
>>> cnet_sparse = divisi.from_sparse_labels(cnet_tuples)
>>> print cnet_sparse
Divisi sparse matrix, shape=(13559, 125285), 463276 items
    ... cool pysparse-based preview goes here ...

Then we create AnalogySpace by running a SVD on ConceptNet. We should specify a
number of *axes*, or principal components, that will be used to define a space
containing all the concepts and features in ConceptNet. Here we set k=50.

Running this will output some nitty-gritty details in all caps, which you can
safely ignore. (We're wrapping a Lanczos SVD algorithm that was apparently
written before there were lowercase letters.)

>>> concept_axes, axis_weights, feature_axes = cnet.normalize_all().svd(k=50)
SOLVING THE [A^TA] EIGENPROBLEM
NO. OF ROWS               = 125285
NO. OF COLUMNS            =  13559
NO. OF NON-ZERO VALUES    = 463276
MATRIX DENSITY            =   0.03%
...

AnalogySpace is expressed using three factors, called U, Sigma, and V. Here,
we're giving them more descriptive names: `concept_axes`, `axis_weights`, and
`feature_axes`.

`concept_axes` is a matrix of the concepts in AnalogySpace versus their axes,
`feature_axes` is the same for the features in AnalogySpace. Unlike concepts
and features, the axes have no names, so we refer to them with numbers from 0
to 49. This is why an entry in the `concept_axes` matrix is named something
like `(u'baseball', 0)`.

You can create a vector representing a row in u, which is a concept in
AnalogySpace. (Using `:` as the second index means to take the entire row.)

>>> cow = concept_axes.row_named('cow')
>>> print cow
Divisi dense vector, length=50
    ... cool preview goes here ...

The similarity of these concepts to each other is represented in a
similarity matrix that could be computed as U * Sigma^2 * U^T. Another way to
say this is that we want to multiply the matrix (U * Sigma) by its own
transpose. (U * Sigma), in our terms, is `concept_axes` weighted by
`axis_weights`.

The result of this would be a very large matrix. This is where a function such
as :meth:`divisi.reconstruct_symmetric` is useful: it returns an object that
acts like that product, without actually having to compute the entire product.

>>> similarity = divisi.reconstruct_symmetric(concept_axes.weighted(axis_weights))
>>> similarity.entry_named('cow', 'horse')
0.068418769278489167
   
But what scale is this on? We really want a measure of similarity that is
affected only by the angle between "cow" and "horse" in AnalogySpace, not their
magnitudes, which will put the similarity on a scale from -1.0 to 1.0. We want
the symmetric matrix of `concept_axes.weighted(axis_weights).normalize_rows()`.
This is getting very wordy, so Divisi has a shorthand for this:

>>> similarity = divisi.reconstruct_similarity(concept_axes, axis_weights,
...                                            post_normalize=True)
>>> similarity.entry_named('cow', 'horse')
0.88958857691685023
>>> similarity.entry_named('cow', 'pencil')
-0.0069139647165505575

Cows and pencils are not very similar.

What are the most similar things to pencils? We can find out by making a vector
containing its dot products with *every* concept in the u matrix:

>>> pencil_like = similarity.row_named('pencil')
>>> pencil_like.top_items()
[(u'computer', 1.2202528641389825), (u'book', 1.215170152903311),
(u'paper', 1.1891308539695427), (u'pen', 0.69290768233550337), (u'pencil',
0.52037765001335479), (u'chair', 0.40438769349078618), (u'desk',
0.38914275787095587), (u'stapler', 0.37656131323591657), (u'telephone',
0.36938823750426064), (u'something', 0.36815695629688239)]
# these results are not what we'll get, incidentally

Let's look at v.  We need to understand what features look like in ConceptNet:

>>> feature_axes.row_labels()[:10]
[('right', u'IsA', u'sport'),
 ('left', u'IsA', u'baseball'),
 ('right', u'IsA', u'toy'),
 ('left', u'IsA', u'yo-yo'),
 ('right', u'IsA', u'write'),
 ('left', u'IsA', u'pen'),
 ('right', u'CapableOf', u'bark'),
 ('left', u'CapableOf', u'dog'),
 ('right', u'IsA', u'game'),
 ('left', u'IsA', u'polo')]

`'right'` features form the right side of an assertion, such as "is a sport", while `'left'` features form the left side of an assertion, such as "a pen is a".

>>> fit = ('right', u'UsedFor', u'fit')
>>> isSport = ('right', u'IsA', u'sport')
>>> isMetal = ('right', u'MadeOf', u'metal')

We can compare these for similarity as well.
>>> fsim = divisi.reconstruct_similarity(feature_axes, axis_weights,
...                                      post_normalize=True)
>>> fsim.entry_named(fit, isSport)
0.148864235859517    
>>> fsim.entry_named(fit, isMetal)
0.023851155065313375

... bit about concepts vs. features ...
