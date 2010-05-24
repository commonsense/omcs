Common Installation Instructions
================================

Installing the CSC tools is very easy on Ubuntu, somewhat easy on Mac OS X,
and usually works on Windows.

.. note:: 
  We don't install from scratch very often, so we might accidentially
  break the installation process. If we broke it, let us know and
  we'll fix it.

Before you can install any of the CSC packages, you will need to have:

- `Python`_ 2.5 or 2.6 with its development headers
- The Python ``distribute`` package, which gives you the convenient ``pip``
  command for installing packages (http://pypi.python.org/pypi/distribute).
  An older alternative which may work for you is ``setuptools`` and
  ``easy_install``.

.. _`Python`: http://python.org

If you are going to install Divisi, or plan to work with our natural language
tools in languages other than English, you will also need a C compiler. 

GNU/Linux
---------

Ubuntu
......
On Ubuntu GNU/Linux, you can get the above with this command::

  $ sudo apt-get install python-dev python-setuptools python-pip build-essential

Fedora
......
On Fedora, you can get the required packages by using:

  $ sudo yum install python-devel python-setuptools python-pip gcc make 

Mac OS X
--------

OS 10.6 (Snow Leopard)
......................
Snow Leopard comes with a reasonable Python 2.6 and most of the tools we need.
Just open up a Terminal window and type::

  sudo easy_install pip

If you want to be able to install modules that involve C code, such as Divisi,
you will need Xcode. You can install it from the DVD that OS X came on.

You will need to do a custom install of Xcode, so that you can install an
optional component called the "10.4u SDK", or else you might run into strange
error messages later.

OS 10.3 through 10.5
....................

You should download Python from http://python.org. We
do not recommend relying on the version of Python that came with your operating
system. Just be careful not to get the versions confused!  (Quit and reopen any
Terminal windows you may have had open, just in case.)

To install Distribute quickly on a Mac, run these two lines in your
terminal::

  $ curl -O http://nightly.ziade.org/distribute_setup.py
  $ sudo python distribute_setup.py

If you want to be able to install modules that involve C code, such as Divisi,
you will need Xcode. You can install it from the DVD that OS X came on.

Windows
-------
If you develop Python code on Windows, you probably have devised some bag of
tricks for working with other people's Python packages. You may have Cygwin
installed, for example, so that it acts more like a Unix machine, and you may
have something like `easy_install` or `pip` already on your computer by now.
You don't have to follow our directions literally if you've come up with a
better way.

If we are the first Python packages you're installing, however, you can give
this a try. Good luck.

- Install Python from http://python.org
- Set your environment variables so that you can use Python from the command
  line. Instructions on how to do this are at:
  http://docs.python.org/using/windows.html
- Download the `distribute installer`_.
- Run it from a command prompt::
  
    python distribute_setup.py

.. _`distribute installer`: http://nightly.ziade.org/distribute_setup.py

In the following sections, if "pip install" doesn't work, try replacing it with
"easy_install".

Next Steps
----------

That's all you need. From here, you can go on to:

* :doc:`Installing ConceptNet <conceptnet/install>`
* :doc:`Installing Divisi <divisi/install>`
* :doc:`Installing Luminoso <luminoso/install>`
* :doc:`developers/setup`

Optional: IPython
.................

To run the examples in this documentation, and to generally make it more
pleasant to interact with Python and ConceptNet, you will probably want to
install the ``ipython`` interpreter shell. Once you have Pip, you can
type::

  $ sudo pip install ipython

Leave off the `sudo` if you are on Windows or inside a `virtualenv`.

You can exit IPython, like a normal Python shell, by typing Ctrl-D and
pressing Enter.

