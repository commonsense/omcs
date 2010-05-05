.. _nl: 
    
Natural language tools
======================

The :mod:`csc.nl` module provides tools for working with natural language text.

To use any of these methods, you must first get an :class:`NLTools` object.
Here is how to get that object for English::

    >>> from csc.nl import get_nl
    >>> en_nl = get_nl('en')

Because :class:`Language` objects store a reference to their :class:`NLTools`,
an alternate way to get the same object is::

    >>> from csc.conceptnet4.models import Language
    >>> en = Language.get('en')
    >>> en_nl = en.nl

.. automodule:: csc.nl

.. autoclass:: NLTools

.. automodule:: csc.nl.euro

.. autoclass:: EuroNL
    :members: is_stopword, is_blacklisted, tokenize, untokenize

.. autoclass:: LemmatizedEuroNL
    :members: normalize, word_split, lemma_split, lemma_combine, lemmatizer, unlemmatizer, get_windows, extract_concepts

.. autoclass:: StemmedEuroNL
    :members:

