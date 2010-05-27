Building and Installing Divisi
==============================

Prerequisites
-------------
Follow the :doc:`/install` before these instructions.

Dependencies
------------

In addition to the common prerequisites, Divisi also needs `NumPy`_.

.. _`NumPy`: http://numpy.scipy.org

Ubuntu
......

On Ubuntu, you can get everything that Divisi needs with the command::

  sudo apt-get install python-dev python-setuptools build-essential python-numpy

(If you've already done the prerequisites, the above is slightly and harmlessly redundant.)

Fedora
......

On Fedora, you can get everything Divisi needs with the command::

  sudo yum install python-devel python-setuptools numpy gcc make

(If you have already done the prerequisites, the above is slightly and harmlessly redundant.)


Installing Divisi
-----------------

Once you have this set up, installing Divisi should be as easy as::

  sudo pip install divisi

or in a virtual environment::

  pip install divisi

or on Windows::

  C:\Python26\Scripts\easy_install divisi

But it's probably not that easy on Windows unless Python already knows how to
use your C compiler. See below for one way to do that.

Setting up GCC on Windows
.........................

The easiest way to get GCC on Windows is to download and install the MinGW_
suite. 

.. _MinGW: http://www.mingw.org/wiki/HOWTO_Install_the_MinGW_GCC_Compiler_Suite

After you do this, you need to tell Python to use it. Create a text file called
``C:\Python26\Lib\distutils\distutils.cfg`` containing the following::

    [build]
    compiler=mingw32

Windows .exe installer
......................

Because it is difficult to set up a C compiler on Windows, we occasionally
distribute compiled versions of Divisi for Windows as .exe files.

The `latest .exe installer`_ (version 0.6.8) requires Python 2.5 (not 2.6).

.. _`latest .exe installer`: http://launchpad.net/divisi/trunk/0.6/+download/Divisi-0.6.8.win32-py2.5.exe

Alternative: development install
................................

If you think you might want to hack on the Divisi source instead, get
`Bazaar`_ and run::

  bzr branch lp:divisi
  cd divisi
  python setup.py develop

See :doc:`/developers/setup` for more information about Bazaar and
the development process.

.. _`Bazaar`: http://bazaar-vcs.org/
