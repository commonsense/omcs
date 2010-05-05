Setting up a CSC development environment
========================================

These are Rob and Ken's suggestions for how to set up your development
environment to work on ConceptNet, Divisi, and related
projects. Everyone has different preferences, so your mileage may
vary.

Step 0: Prerequisites
---------------------
Follow the :doc:`/install` before these instructions.

Step 1: Get a virtual environment
---------------------------------
``virtualenv`` is a system that sets up an isolated Python environment
for you to develop in. This is nice. It means when something breaks,
you don't have to try to pick the pieces out of your systemwide Python
configuration; you can just make a fresh virtual environment. It also
means less ``sudo``.

Because you got `pip` from the :doc:`/install`, all you need to type is::
  
  pip install virtualenv

Now set up a virtual environment. This command will create one called "csc"
under your home directory::

  virtualenv ~/csc

To activate the environment, you run this::

  source ~/csc/bin/activate

You may want to add this to your .bashrc so that it runs by default when you
start a shell. You can get back to your normal Python by typing ``deactivate``.

If you want to give yourself some nice shell commands for working with virtual
environments, try out virtualenvwrapper:
http://www.doughellmann.com/projects/virtualenvwrapper/

Optional: IPython
.................
Python development is painful without IPython. You should make sure you have
it running *inside* your virtual environment -- a system-wide IPython isn't
going to be useful here. 

With your virtual environment activated, type `pip install ipython`.

Step 2: Set up Bazaar and Launchpad
-----------------------------------

Directions for installing and setting up Bazaar and Launchpad are in
the :doc:`bzr-howto` section.

Make sure you register a public key with Launchpad, and then let the command
line client know about your Launchpad username::

  bzr launchpad-login myusername


Step 3: Get the packages
------------------------

If you were merely using the packages, you'd ``pip install`` them,
but since you might want to change the code, branch them from Bazaar
instead. Run this inside your ``~/csc`` directory::

  bzr co lp:csc-utils
  bzr co lp:conceptnet
  bzr co lp:divisi
  bzr co lp:~commonsense/cscweb/documentation/

(I suggest branching ConceptNet and Divisi because you'll more often
make changes that break things there, but checkouts of ``csc-utils``
and this documentation should be fine.)

There are some other codebases you won't be messing with, and which you will
really want to be installed::

  pip install django
  pip install psycopg2
  pip install PyStemmer

Step 4: Install
---------------
For each package in (``csc-utils``, ``conceptnet``, and ``divisi``)::

  cd ~/csc/$package
  python setup.py develop

Step 5: Configure the database
------------------------------
You'll probably want to run ConceptNet on a PostgreSQL database, as described
in :doc:`/conceptnet/install`. If you're in the Media Lab, you'll probably want
to run on *the* PostgreSQL database, so ask someone for what to put in your
db_config.py.

Step 6: Test
------------
Start up your ipython. Try importing ``csc.conceptnet.models`` and ``csc.divisi``. Run some of the code in the "Examples" section. If it works, you're all set.

