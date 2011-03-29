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

Mac packages
------------
While we develop Luminoso primarily on Macs, we have no experience with making
nicely-packaged Mac applications. So far, the only way to run Luminoso on a Mac
is to build it from source using the directions below.

Building from source
--------------------

If you are using a Mac or Linux, or you are on Windows and you want to get
updates more frequently than the releases we make every few months, you can
install Luminoso from its source code.

On a Linux system, you only need to install the packages we depend on and then
checkout and install Luminoso. Here's what you do on Ubuntu::

    sudo aptitude install build-essential python-dev python-setuptools python-pip python-numpy python-qt4 git
    git clone git://github.com/commonsense/luminoso.git
    cd luminoso
    sudo pip install -r requirements.txt
    sudo python setup.py install

Then run Luminoso by simply typing::

    luminoso
    
On a Mac, the build process can be done similarly, but you'll suffer from a 
multiplicity of pythons; as Macs have no One True Package Manager, you probably
have several copies of python installed already. For this install process we'll use
MacPorts to install the dependencies, then ensure that all our python commands refer
to the MacPorts version.

Most Python packages for MacPorts have names like py26-dev for python 2.6, so:

	sudo port install py26-pip py26-numpy py26-pyqt4 git-core python_select

This will likely take a long time. ATLAS, a linear algebra program that is a dependency
for numPy, is a particular offender here; it recommends that you disable processor
throttling during its install as it will do a lot of processor timing to optimize itself.
If you know how to do that by all means do, but it won't hurt your build to ignore it.
You'll also get a Fortran compiler. One way or another, just run the command and come
back later.

Once that's done, use python_select to choose the correct python:
	
	python_select -l

will give you a list of Python installs; use

	sudo python_select <install_name>
	
where <install_name> is one of the results from the previous command to switch between
them. After doing so, run

	which python

to see python's path; the correct result is something like /opt/local/Library/Frameworks/Python.framework/Versions/2.6/bin/python
rather than /Library... Also run

	which pip
	
If you don't get something like /opt/local/Library/Frameworks/Python.framework/Versions/2.6/bin/pip
you'll need to change your .bash_profile to include the line

	export PATH=/opt/local/Library/Frameworks/Python.framework/Versions/2.6/bin:/opt/local/bin:$PATH

then run
	
	source .bash_profile
	
and the results of which pip should be correct.

All that done, use the same install process as for Ubuntu:

    git clone git://github.com/commonsense/luminoso.git
    cd luminoso
    sudo pip install -r requirements.txt
    sudo python setup.py install

And run by typing

	luminoso

On a non-Linux system, this is harder to do, as it requires setting up a development environment with Python and Qt. This requires familiarity with using your operating system's command line.

You will need:

- An official version of Python 2.5 or 2.6 from http://python.org.
- A C compiler. We suggest mingw32 on Windows, and
  Xcode on a Mac (it's on your Mac OS installation DVD). You will need to be
  able to run the `make` command, as well.
- On recent versions of Mac OS, you need to be sure to install the OS 10.4
  development libraries, which are not installed by default. This will be an
  option when you install Xcode; if you didn't choose it, go back to the Xcode
  installer on the DVD and check it.

Then, do the following steps (ignoring `sudo` if you're on Windows):

#. Follow our :doc:`/install`.
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

If that all worked correctly, then you should be able to
simply type `luminoso` to run Luminoso.

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

