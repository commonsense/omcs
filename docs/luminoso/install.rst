.. _install_luminoso:

Installing and running Luminoso
===============================

The easiest way to use Luminoso is to install a self-contained package for
Windows. The second easiest way to install it is to build it on Linux.

Self-contained Windows packages
-------------------------------

If you have a Windows computer and want to get up and running with a released
version of Luminoso, these directions are for you.

- Download this file: http://conceptnet.media.mit.edu/dist/Luminoso/Luminoso-1.3.3-win.zip
- Extract the file wherever you want.
- Run :file:`run_luminoso.exe` to launch Luminoso.

The ZIP file contains all the files Luminoso requires; it does not have to be
installed to anywhere in particular.

You can also download a couple of small example studies, which show you what a
study should look like and let you test that Luminoso works: http://conceptnet.media.mit.edu/dist/Luminoso/Luminoso-1.3-example-studies.zip

If this documentation becomes out of date, there may be newer versions in
http://conceptnet.media.mit.edu/dist/Luminoso.

Building on Linux from Git
--------------------------

If you want to get updates more frequently than the releases we make every few
months, we recommend running on Linux and getting the code from our Git
repository. 

You only need to install the packages we depend on, and then checkout and
install Luminoso. You may be able to adjust these directions to work on Windows
or Mac OS, but then you will need to install lots of dependencies separately
(see below for details about Mac OS).

Here's what you do on Ubuntu Linux::

    sudo aptitude install build-essential python-dev python-setuptools python-pip python-numpy python-qt4 git
    git clone git://github.com/commonsense/luminoso.git
    cd luminoso
    sudo pip install -r requirements.txt
    sudo python setup.py install

Then run Luminoso by simply typing::

    luminoso

Building on Mac OS
------------------
There are two approaches to using Python on a Mac, and both have their
advantages and drawbacks.

Mac OS has a built-in Python installation, and in OS 10.6 and later this
version of Python is sufficient to run Luminoso. However, the Mac has no
built-in *package management*, so using this approach you will need to compile
many things yourself. The "Using the Mac's system Python" section explains how
to do this.

MacPorts is a third-party package manager for the Mac that is capable of
automatically compiling and installing many useful tools. The potential problem
is that MacPorts installs its own, completely separate, version of Python. You
may prefer this approach if you already use MacPorts, or if you run into
problems compiling PyQt without it. See the "Using MacPorts" section for this
approach.

You can tell if your Python runs through MacPorts by typing at the command line::

    which python

If the answer starts with `/opt`, you use MacPorts. If it starts with
`/usr/bin`, you use the system Python. A third possibility is that if it starts
with `/usr/local/bin`, you may be using a separate version of Python downloaded
from python.org.

If you don't currently use Python through MacPorts, we suggest trying the
non-MacPorts instructions first, to avoid an unnecessary proliferation of
Python environments.

Using the Mac's system Python
`````````````````````````````

You will need:

- Xcode 3 or later. You can get this for free on your Mac OS installation DVD,
  or you can buy it in the App Store.
- The OS 10.4 development libraries, which are an optional part of the Xcode
  installation. If you didn't choose to install these before, go back to the
  Xcode installer and check it.

Then, do the following steps:

#. Follow our :doc:`/install`, including installing NumPy.
#. Install Qt (the GUI library we use) from http://qt.nokia.com/products/.
#. Install SIP (a Python-to-C++ bridge):
    - Download it from
      http://www.riverbankcomputing.co.uk/software/sip/download.
    - Run its `configure.py`.
    - Run `make` and `sudo make install`.
#. Install PyQt4:
    - Download it from
      http://www.riverbankcomputing.co.uk/software/pyqt/download.
    - Run its `configure.py`.
    - Run `make` and `sudo make install`.
#. Install Git from http://git-scm.com/.
#. Download Luminoso with `git clone git://github.com/commonsense/luminoso.git`.
#. Install Luminoso with `sudo python setup.py install`.

If that all worked correctly, then you should be able to simply type `luminoso`
to run Luminoso.

Using MacPorts
``````````````

On a Mac, the build process can be done similarly, but you'll suffer from a
multiplicity of pythons; as Macs have no One True Package Manager, you probably
have several copies of python installed already. For this install process we'll
use MacPorts to install the dependencies, then ensure that all our python
commands refer to the MacPorts version.

Most Python packages for MacPorts have names like py26-dev for python 2.6, so::

	sudo port install py26-pip py26-numpy py26-pyqt4 git-core python_select

This will likely take a long time. ATLAS, a linear algebra program that is a
dependency for numPy, is a particular offender here; it recommends that you
disable processor throttling during its install as it will do a lot of
processor timing to optimize itself.  If you know how to do that by all means
do, but it won't hurt your build to ignore it.  You'll also get a Fortran
compiler. One way or another, just run the command and come back later.

Once that's done, use python_select to choose the correct python::
	
	python_select -l

will give you a list of Python installs; use ::

	sudo python_select <install_name>
	
where <install_name> is one of the results from the previous command to switch
between them. After doing so, run ::

	which python

to see python's path; the correct result is something like /opt/local/Library/Frameworks/Python.framework/Versions/2.6/bin/python
rather than /Library... Also run ::

	which pip
	
If you don't get something like
/opt/local/Library/Frameworks/Python.framework/Versions/2.6/bin/pip you'll need
to change your .bash_profile to include the line ::

	export PATH=/opt/local/Library/Frameworks/Python.framework/Versions/2.6/bin:/opt/local/bin:$PATH

then run ::
	
	source .bash_profile
	
and the results of which pip should be correct.

All that done, use the same install process as for Ubuntu::

    git clone git://github.com/commonsense/luminoso.git
    cd luminoso
    sudo pip install -r requirements.txt
    sudo python setup.py install

And run by typing ::

	luminoso

Building on Windows
-------------------

You will need:

- An official version of Python 2.5 or 2.6 from http://python.org.
- A C compiler that is compatible with Python. We suggest `mingw32`, which is
  free; a sufficiently recent version of Visual Studio should also work.
- You will also need to be able to run `python`, `gcc` and `make` at your
  Windows command line of choice. This may require editing your PATH
  environment variable in the Control Panel.
- Depending how your Windows is configured, you may need to "run as
  administrator" when you open the command line.

#. Follow our :doc:`/install`, including installing NumPy.
#. Install Qt (the GUI library we use) from http://qt.nokia.com/products/.
#. Install SIP (a Python-to-C++ bridge):
    - Download it from
      http://www.riverbankcomputing.co.uk/software/sip/download.
    - Run `python configure.py`.
    - Run `make` and `make install`.
#. Install PyQt4:
    - Download it from
      http://www.riverbankcomputing.co.uk/software/pyqt/download.
    - Run `python configure.py`.
    - Run `make` and `make install`.
#. Install Git from http://git-scm.com/.
#. Download Luminoso with `git clone git://github.com/commonsense/luminoso.git`.
#. Install Luminoso with `python setup.py install`.

.. _command-line-luminoso:

Getting the command-line version
--------------------------------
As of Luminoso 1.3.1, you can run the core of Luminoso from the command line,
using the `luminoso-study` command. If you don't need the GUI, the setup
process is easier:

#. Follow our :doc:`/install`.
#. Install Git from http://git-scm.com/.
#. Download Luminoso with `git clone git://github.com/commonsense/luminoso.git`.
#. Install Luminoso with `sudo python setup.py install`.

