.. _webapi-client:

A ConceptNet Web API Client
===========================

The previous section of the documentation defines a :ref:`web API <webapi>` for interacting
with ConceptNet. Any programming language that can read JSON, YAML, or XML, and
can send and receive HTTP, can interact with the API as specified.

Here, we describe `rest_client.py`_, a straightforward Python implementation of
a client for the Web API. In addition to the preceding download link, the
client can be found in the `csc/webapi/` directory of the full ConceptNet 4 API.

.. _`rest_client.py`: http://openmind.media.mit.edu/site_media/rest_client.py

This client is not object-oriented. The data structures you work with are
simple dictionaries, with the fields described in the :ref:`web API <webapi>`
documentation.

The main function :func:`lookup` can be used to look up many different kinds of
data. The module also contains convenience functions for performing common
operations on this data, such as looking up assertions given a concept.

Looking up information
----------------------

.. module:: conceptnet.webapi.rest_client

.. autofunction:: lookup
.. autofunction:: lookup_concept_raw
.. autofunction:: lookup_concept_from_surface
.. autofunction:: lookup_concept_from_nl
.. autofunction:: assertions_for_concept
.. autofunction:: surface_forms_for_concept
.. autofunction:: votes_for

Adding information
------------------

.. autofunction:: add_statement

Examples
--------

.. include:: ../recipes/webapi_client.txt

