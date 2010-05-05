.. _install_luminoso:

Installing and running Luminoso
===============================

Self-contained packages
-----------------------

The easiest way to use Luminoso is to use one of our self-contained packages
for Windows or Mac. To be specific, you don't even have to install these. The
latest versions of these packages can be found at:
http://launchpad.net/luminoso

On Windows, you download a ``.zip`` file that contains all the files Luminoso
requires, as well as a program called :file:`run_luminoso.exe`. Running this
program will launch Luminoso. The zip file also contains studies such as
ThaiFoodStudy that you can use as an example.

On Mac, you download a ``.dmg`` file containing Luminoso as a Mac application.
This means that it contains all the files it needs within it. You can drag
Luminoso to your `Applications` folder to install it. The examples, also found
within the .dmg, can go anywhere.

Installing from scratch
-----------------------
On a Linux system, you only need to install the packages we depend on and then
checkout and install Luminoso. Here's what you do on Ubuntu::

    sudo aptitude install build-essential python-dev python-setuptools python-pip python-numpy python-qt4 bzr
    bzr checkout lp:luminoso
    cd luminoso
    sudo pip install -r requirements.txt
    sudo python setup.py install

On a non-Linux system, this is much harder to do, as it requires setting up a development environment with Python and Qt. You will need:

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
    - Run its `configure.py`. If you are on Snow Leopard, you will need to give
      the ``--arch i386`` option.
    - Run `make` and `sudo make install`.
#. Install PyQt4:
    - Download it from
      http://www.riverbankcomputing.co.uk/software/pyqt/download.
    - Run its `configure.py`. If you are on Snow Leopard, you will need to give
      the ``--arch i386`` option.
    - Run `make` and `sudo make install`.
#. Install Bazaar, either with `sudo pip install bzr` or by downloading it from
   http://bazaar-vcs.org.
#. Download Luminoso with `bzr checkout lp:luminoso`.
#. Install Luminoso with `sudo python setup.py install`.

If that all worked correctly, which is a big if, then you should be able to
simply type `luminoso` to run Luminoso.

If it fails with an "interrupted system call", you've encountered a bug in
IPython. `luminoso --no-console` will work around it.

