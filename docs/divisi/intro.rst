Tutorial: Getting Started
=========================

Once you've `built and installed <install.html>`_ Divisi, you can start
by making your own AnalogySpace.

1. Download the `ConceptNet tensor for English <http://commons.media.mit.edu/en/tensor.gz>`_.
2. Load it::

    from csc.util.persist import get_picklecached_thing
    tensor = get_picklecached_thing('tensor.gz')

3. Run the SVD::

    svd = tensor.svd(k=100)

4. Get similar concepts (to 'teach')::

    svd.u_dotproducts_with(svd.weighted_u_vec('teach')).top_items(10)

5. Predict properties (for 'trumpet')::

    svd.v_dotproducts_with(svd.weighted_u_vec('trumpet')).top_items(10)

(These things that look like `('right', 'IsA', 'pet')` are how we represent the
*features* in ConceptNet.)

6. Evaluate possible assertions::

     # Is a dog a pet?
     svd.get_ahat(('dog', ('right', 'IsA', 'pet')))

     # Is a hammer a pet?
     svd.get_ahat(('hammer', ('right', 'IsA', 'pet')))

.. note::

   The concepts are represented by their *normalized form*, which is how
   they are represented internally in ConceptNet.
   
   If you look up a value for "scissors", for example, you won't find anything.
   It's under "scissor".
   The reason for this is so that phrases like "eat a
   sandwich" and "eating sandwiches" correspond to the same
   concept. See :ref:`nl` for details on how this works.
