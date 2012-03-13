.. _corpus:

The :mod:`corpus` module
========================

The :mod:`corpus` module contains classes and methods for working with the Open
Mind data as a low-level corpus. It provides the basic functionality that
ConceptNet is built on, while being agnostic about the representation of such a
semantic network.

The most important database models described here are :class:`Language` and
:class:`Sentence`. We also define the generally useful abstract class
:class:`ScoredModel`, and the :class:`TaggedSentence` and
:class:`DependencyParse` classes that are used in some applications that work
with raw Open Mind data.

.. automodule:: conceptnet.corpus.models

Languages
---------

.. autoclass:: Language
    :members: get, nl

    .. attribute:: id

        The ISO language code of this language.
    
    .. attribute:: name

        The name of this language in English.

    .. attribute:: sentence_count

        A cached count of how many sentences Open Mind has collected in this
        language.

Sentences
---------
This database model represents all the sentences that Open Mind has collected
in a variety of languages. Some of them come from the original Open Mind, which
took free-text input; some come from activities on modern iterations of the
Open Mind web site; and some come from related sites such as GlobalMind.

.. autoclass:: Sentence
    
    .. attribute:: text
        
        The natural-language text that a user entered into Open Mind.

    .. attribute:: language

        The :class:`Language` that this sentence is in.

    .. attribute:: creator

        The :class:`User` who entered this sentence.

    .. attribute:: created_on

        The timestamp when this sentence was created.

    .. attribute:: score
        
        The cached score of this sentence: the number of users who have voted
        for it versus the number who have voted against it.

    .. attribute:: activity

        An object identifying how this sentence came to be.

Scored Models
-------------

.. autoclass:: ScoredModel
    :members:

Other classes
-------------

.. autoclass:: DependencyParse
    :members:

.. autoclass:: TaggedSentence
    :members:

