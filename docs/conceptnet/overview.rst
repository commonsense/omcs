Overview 
========

The current ConceptNet API has the ability to access the database we call
"ConceptNet 4". Once this API is stable enough, we'll call it ConceptNet 4.0.

How does this code work?
------------------------
The answer from 30,000 feet up is simple: It's Django.

Django is a Python framework for working with databases and web applications.
All of ConceptNet is represented as Django models that interact with each other
and with a database. We don't use the web application part -- not here, at
least -- but we provide the appropriate hooks so that ConceptNet can power a
Django web application. (Because it does. It's at
http://openmind.media.mit.edu.)

The code is divided into a few main modules, or *apps*:

- :mod:`corpus`, representing the sentences of glorious, ambiguous natural
  language that our contributors have provided us with.
- :mod:`nl`, which lets you do useful transformations on natural language text.
- :mod:`conceptnet`, representing the structured
  assertions that we have parsed from the corpus.
- :mod:`events`, which lets us keep track of how, when, and why various objects
  came into being.
- (:mod:`voting`, which actually isn't by us at all; it's the `django-voting`_
  package by Jonathan Buchanan.)

.. _`django-voting`: http://code.google.com/p/django-voting/

Each app contains several *models*, representing objects that are stored in a
database. The information in ConceptNet is represented by these models and
their relationships to each other.

.. image:: _static/graph/conceptnet_all.png
   :width: 600
   :alt: ConceptNet 4 model diagram
   :target: ../_static/graph/conceptnet_all.png

(`PDF version`_)

.. _`PDF version`: ../_static/graph/conceptnet_all.pdf


