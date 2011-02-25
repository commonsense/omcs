Installing ConceptNet
=====================

.. _install:

So you want to install the ConceptNet API. Here's the summary of how to do it:

1. Install system-wide packages that we depend on, including Python and Pip.
2. Use ``pip install`` to download and install ConceptNet.
3. Acquire the `ConceptNet database`_ and tell Python where to find it.

.. _`ConceptNet database`: http://conceptnet.media.mit.edu/dist/ConceptNet-sqlite.tar.gz

If you're an Open Mind developer, these aren't really the right directions.
Look at the "CSC Development" section of the documentation.

Quick start
-----------

On Ubuntu, this should get you from zero to ConceptNet::

    $ sudo aptitude install python-dev python-setuptools python-pip ipython
    $ sudo pip install conceptnet
    $ ipython -cl
    >>> from conceptnet.models import *

Then type 'y' to download and install the ConceptNet database.

On other operating systems, you'll need to keep reading.

Prerequisites
-------------
You need Python 2.5 or 2.6, plus Pip for managing packages. If you don't have
these, follow the :doc:`/install` first.

Remember to leave the "sudo" off of these commands if you're on Windows.

Install ConceptNet and its dependencies
---------------------------------------
Pip will take care of the hard work; all you need to type is::

  sudo pip install conceptnet

This should download ConceptNet and its dependencies, which include:

- Django
- csc-utils (our utility package)
- south (allows the database to be upgraded later)

If for some reason ``pip install`` fails, you can get the release `from PyPI`_.

.. _`from PyPI`: http://pypi.python.org/pypi/ConceptNet/

Getting the database
--------------------
With the newest release of ConceptNet, just try importing ConceptNet
and it will download the database for you if necessary::

    >>> from conceptnet.models import *

If that works for you, you're done. Skip to :ref:`the last section <tryitout>`.
If that fails, or you just want to do things manually, keep reading.

Downloading the database manually
.................................

The easiest way to get the database is as a SQLite file. You can get this file
from here_.

.. _here: http://conceptnet.media.mit.edu/dist/ConceptNet-sqlite.tar.gz

Unzipping this file gives you the database (``ConceptNet.db``) and a
configuration file (``db_config.py``).

If you're just trying it out, the easiest approach is to just run
``python`` (or ``ipython``) in the same directory where you put the
extracted files.

Your Python code will only be able to find the database if one of these is the
case:

- The environment variable ``CONCEPTNET_DB_CONFIG`` contains the full path to
  ``db_config.py``
- ``db_config.py`` is in the current directory
- ``db_config.py`` is in a directory in your PYTHONPATH

On Python 2.6, you get a `per-user site-packages directory
<http://docs.python.org/whatsnew/2.6.html#pep-370-per-user-site-packages-directory>`_,
which is a great place to put ``db_config.py``.

Optional: Using a PostgreSQL database
.....................................

We have also periodically provided PostgreSQL dumps of the ConceptNet database.
PostgreSQL is much faster than SQLite at looking things up in ConceptNet, but
it is harder to set up.

If you want to use one of these, follow the directions here. You do *not* need
to do this if you are using the SQLite database.

You will need to set up PostgreSQL, and install the ``psycopg2`` library for
Python.  Then, edit ``db_config.py`` as follows::

  from db_password import DB_PASSWORD
  DB_ENGINE = "postgresql_psycopg2"
  DB_NAME = "ConceptNet"
  DB_HOST = "localhost"    # or whatever server it's on
  DB_PORT = "5432"         # or whatever port it's on
  DB_USER = "username"     # change this to your PostgreSQL username
  DB_SCHEMAS = "public"

Finally, make a file ``db_password.py`` containing the line ``DB_PASSWORD =
"yourpassword"``, and make sure that the file is only readable by you.

.. _tryitout:

Try it out
----------
If you've set up ConceptNet correctly, you should be able to run the following
small example. Start ``ipython`` and type the following lines::

  from conceptnet.models import Concept
  dog = Concept.get('dog', 'en')
  for fwd in dog.get_assertions_forward()[:20]:
      print fwd

To understand what that just printed, go on to :doc:`the conceptnet4 module
<conceptnet4>`.
