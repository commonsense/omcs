Setting up a CSC development environment
========================================

These are Rob and Ken's suggestions for how to set up your development
environment to work on ConceptNet, Divisi, and related
projects.

Everyone has different preferences for how to develop code and
differently-configured systems, so no single set of directions can possibly
cover everything. So that's why we hope to cover a lot of common cases with
these "choose your own adventure"-esque directions.

Here's where we start:

Setting up your GitHub account
------------------------------
Wait, why are we doing this first? Because one of the later steps works better
if you're already added to the GitHub projects. This would probably be easiest
for one of the existing developers to do.

If you already have a GitHub account, skip to the bottom of this section.

- Go to http://github.com and create an account.
- Follow the instructions at http://github.com/guides/providing-your-ssh-key, to associate your account with an SSH public key on your computer.
- Ask an existing OMCS developer to add you to the `commonsense` organization
  on GitHub.

For the next step:

- If you use Linux, go to :ref:`linux`.
- If you use Mac OS X, go to :ref:`mac`.
- 2If you use Windows, go to :ref:`windows`.
- If you are working entirely within a virtual Python environment on a system
that somebody else set up, go to :ref:`in_virtualenv`.

Whoa there
----------
You just kept reading! This isn't how this page is designed to be read.

This document has instructions for three different operating systems and
different Python setups on those operating systems. Most of the page isn't
going to apply to you. That's why reading straight through it doesn't work.

Now go back a section.

.. _linux:

Linux setup
-----------
On Ubuntu, you can get the required packages with this command::

  $ sudo apt-get install python-dev python-setuptools python-pip python-virtualenv build-essential git python-numpy

On Fedora, you can get the required packages by using::

  $ sudo yum install python-devel python-setuptools python-pip python-virtualenv gcc make git python-numpy

That's all for the platform-specific stuff. Go on to :ref:`cross_platform`.

.. _mac:

Mac OS setup
------------
If you have OS 10.6, you almost have everything you need. You can use the
built-in `easy_install` to get `pip`::

    sudo easy_install pip

Then go onto :ref:`have_mac_pip`.

On the other hand, if you're on Mac OS 10.5, the version of Python that is pre-installed in OS 10.5 is insufficient. You'll
first need to download and install Python 2.6 from http://python.org. 

Then you need to download Distribute. You can set it up by typing these
two commands in your Terminal::

    curl -O http://python-distribute.org/distribute_setup.py
    python distribute_setup.py

Once this runs, go on to the next section.

.. _have_mac_pip:

Installing other Mac tools
..........................

You can get a NumPy 1.4 installer for the Mac at https://sourceforge.net/projects/numpy/files/.

Once you download and install it, you can skip to the section called
:ref:`cross_platform`.

.. _windows:

Windows setup
-------------
If you already have Python 2.6 and can run it from the command prompt, skip to :ref:`have_windows_python`. Otherwise, continue to the next section.

Setting up Python on Windows
............................

First, you need to download Python 2.6 from http://python.org, and install it.

After that, you will need to set it up so that you can use Python from the
command line, by setting the PATH environment variable. Instructions for doing
this are at:
http://docs.python.org/using/windows.html#excursus-setting-environment-variables

If you've done all this, you should be able to open a command prompt and type
`python`, and get an interactive Python prompt. Once you can do this, go on to
the next step.

.. _have_windows_python:

Getting NumPy for Windows
.........................
Download and install NumPy, from https://sourceforge.net/projects/numpy/files/. Choose the latest Python 2.6 "superpack" version.

Type ``import numpy`` at the Python
prompt and make sure you don't get an error, and go on to the next step.

Getting Distribute/Pip for Windows
..................................
Distribute is a system for managing Python packages. Pip is a useful
command-line program for downloading and installing packages.

Distribute comes with Pip pre-installed, so to get both of them, download
http://python-distribute.org/distribute_setup.py and run it.

Your Python is now ready to go. In the next step, you'll set up the MinGW
version of `gcc`, so you can compile the C code we use. But if you already
program in C on Windows using Cygwin, you probably would prefer to follow the
:ref:`cygwin_directions`.

Setting up MinGW and msysgit
............................
Download and install MinGW from http://www.mingw.org/. This gives you a
slightly better command line, and a minimal installation of `gcc`.

You need to tell Python to use MinGW to compile things. You can do this by
creating (or updating) the file named
`C:\Python26\Lib\distutils\distutils.cfg`. It should contain the following
two lines::
    
    [build]
    compiler=mingw32

You'll also need Git, so download and install msysgit (the official Windows version of Git) from http://code.google.com/p/msysgit/.

Now you're ready to jump to the section on :ref:`install_packages`.

.. _cygwin_directions:

Alternate Cygwin directions
...........................

Use Cygwin Setup to install `gcc`, `make`, and `git`.

Using the Cygwin shell, you can follow the directions in :ref:`cross_platform`
and just leave off the "sudo". I think. I've never tried using virtualenv on
Cygwin. You can also just skip to :ref:`install_packages` and run without
virtual environments.

Cross-platform directions
-------------------------

.. _cross_platform:

Setting up virtualenv
.....................
``virtualenv`` is a system that sets up an isolated copy of Python
for you to develop in.

This is optional, but it's nice. It means when something breaks, you don't have
to try to pick the pieces out of your systemwide Python configuration; you can
just make a fresh virtual environment. It also means that these are the last
few Python commands you'll have to run with "sudo" or as root.

Use `pip` to get virtualenv and a nice command-line wrapper for it::

    sudo pip install virtualenv virtualenvwrapper

Then go on to the next section.

.. _in_virtualenv:

Setting up your virtual environment
...................................

At this point, the system you're on should have `virtualenv` and
`virtualenvwrapper` installed, along with other Python tools. Everything else
can be done within your own user account.

Make a directory for Python environments::

    mkdir ~/py

Now set up your shell to work with virtualenvwrapper. On Linux, you do this::

    echo "export PIP_RESPECT_VIRTUALENV=true" >> ~/.bashrc
    echo "export WORKON_HOME=$HOME/py" >> ~/.bashrc
    echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc

On a Mac, you do this::

    echo "export PIP_RESPECT_VIRTUALENV=true" >> ~/.bashrc
    echo "export WORKON_HOME=$HOME/py" >> ~/.bashrc
    echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc

These changes won't take effect until you **open a new terminal window**.
After you do that, you can type::

    mkvirtualenv omcs

You should now be using a copy of Python that is installed into your
`~/py/omcs` directory. In the future, you activate this version of Python with
this command::

    workon omcs

Now go on to the next section.

.. _install_packages:

Installing CSC packages and their dependencies
..............................................

You've got Git, so check out our top-level repository. Type this command
anywhere besides the 'py' directory::

    git clone git@github.com:commonsense/omcs.git

If that doesn't work, you're not yet listed as a developer. You'll have to poke
a developer or use the alternate read-only URL::

    git clone git://github.com/commonsense/omcs.git

You get an `omcs/` directory with some stuff in it, some documentation, and
some empty subprojects. Subprojects are an advanced Git feature and you don't
need to use them yet -- we'll be getting the code through Pip, anyway.

Inside the `omcs/` directory, run::

    pip install -r devel_requirements.txt

(Use `requirements.txt` instead of `devel_requirements.txt` if you don't have
read-write access. We can add write access later.)

This is what everything else has been building up to. It does the following
things:

- It makes sure that numpy is installed.
- It installs other useful Python tools: `ipython`, `nose`, `fabric`, and `sphinx`.
- It checks out the Git repositories for our core projects, compiles the C code
  for Divisi, and installs them all in development mode.

Now you have editable code for our projects in some directory inside your
Python environment -- most likely `~/py/omcs/src`. The directories under it are
Git repositories. One thing, though: they're in this stupid default mode called
"headless mode".

If you want to be able to commit changes to one of these projects, get out of
headless mode and onto the "master" branch, by typing this command in the
project's directory::

    git checkout master

Now go on to the next step.

Configure the ConceptNet database
.................................

You'll probably want to run ConceptNet on a PostgreSQL database, as described
in :doc:`/conceptnet/install`. If you're in the Media Lab, you'll probably want
to run on *the* PostgreSQL database, so ask someone for what to put in your
`db_config.py`.

Finally:

Test stuff
..........
Start up your ipython. Try importing ``csc.conceptnet.models`` and
``csc.divisi2``. Run some of the code in the "Examples" sections. If it works,
you're all set.

Reading list
------------
If you are unfamiliar with the details of Git, you should take half an hour or
so to read the first three chapters of `Pro Git`_.

.. _`Pro Git`: http://progit.org/book/

Python packaging is way more stupid and complicated than it should be, and
changing rapidly as people try to deal with that fact. But understanding how to
do it right -- or at least a reasonable approximation of right -- can help make
your contributions more usable.

To that end, we'd like you to skim through the `Hitchhiker's Guide to Python
Packaging`_ sometime. You don't have to do it right away, but it could be
relevant when you're contributing code.

.. _`Hitchhiker's Guide to Python Packaging`: http://guide-python-distribute.org

