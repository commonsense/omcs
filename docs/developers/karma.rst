Documenting and Testing (instant coding karma)
==============================================

If you're at a loss about how to make progress in your research, one way that
you can *always* advance the project is to document and test it.

This file describes a few things you can do to earn the admiration of your
peers, as well as Coding Karma that will pay you back in the form of code that
just works better.

Here's a summary of karmically positive things you can do:

* Write docstrings
* Write "recipes" for things you can do with existing code
* Write tests
* Write doctests
* Write pages of documentation like this one

Docstrings (the low-hanging fruit)
----------------------------------
Every Python function that's meant for other people to use should have a
*docstring* -- a string at the top of the function explaining what it does.

Many of our functions don't have docstrings, especially in the `conceptnet`
package. Writing docstrings for functions you use, or for new functions you
have written, is an easy form of coding karma. These docstrings can easily be
included in more complete documentation later.

The documentation directory
---------------------------

What you're reading right now comes from a directory called "docs" under the
"omcs" Git repository. You can edit it in its checked-out version, or you can
make changes through the Web at
http://github.com/commonsense/omcs/tree/master/docs/.

The documentation repository contains a couple of things:

* **Recipes**, which are useful snippets of code
* **Sphinx documentation**. Sphinx is a shiny system for documenting Python
  code. Using Sphinx, you can also include the docstrings that you write
  within the actual code. The document you're reading right now was produced
  using Sphinx.

Writing "recipes"
-----------------
If you have an example of accomplishing something useful with our tools, show
it to other people! 

The `recipes/` directory of the documentation is the place to put
these. They can even be included as pages of the Sphinx documentation later.

Writing tests
-------------
We use `nose` for testing. You can get this program with::

  easy_install nose

The nice thing about `nose` is that you basically just write a file called
`test.py`, or any Python file with "test" in the name, when you have things to
test. `nose` will find these files and run them.

(If you want to be more principled about this, put the test code under a
top-level directory called `test/`.)

This `test.py` file contains functions that test things. It can tell something
is a test function because it has `test_` or `_test` or something like it in
the name.

If a test function returns uneventfully, it passes. If it raises an error or
fails an assertion, it fails.

Running `nosetests` will find all the test functions and run them. If your
tests rely on the database, you may need to run it like this::

  DJANGO_SETTINGS_MODULE=csc.django_settings nosetests

Writing doctests
----------------
Doctests are great. They're documentation *and* tests. *At the same time.*

Python's framework for doctests is not quite as great, but we can use them
within `nose`.

In a doctest, you write things like this into a docstring:

    >>> do.stuff.with_your(code)
    'result'

The doctest framework runs the code, and checks that the repr() of the result
matches what you wrote.

You can turn this into a `nose` test by dropping a couple of lines of code into
a `test.py` file. Here's an example of running the doctests for the
:mod:`simplenlp.euro` module::

    from csc_utils import run_doctests
    import simplenlp.euro
    run_doctests(simplenlp.euro)

This even allows you to define a function called :meth:`doctest_globals` that
returns the global environment that other doctests should run in. This is
something you can't normally do with doctests.

If you look up nose's documentation (which generally can't hurt), you'll hear
about a doctest plugin for nose. It doesn't work, though. Use ours.

Writing documentation pages
---------------------------

In the docs repository, you'll see a bunch of directories full of
``.rst`` files. These files are reStructuredText -- a format that lets
you write documentation that is also readable as plain text -- and
Sphinx can put them, along with the docstrings, together into the kind
of web page you're probably reading now.

Probably the best way to get the hang of writing Sphinx files is by
example--look at the existing ``.rst`` files. Unsurprisingly, the
`Sphinx docs`_ are pretty good too. A major caveat: the
reStructuredText format is very whitespace-sensitive. Blank lines or
their absence can be meaningful.

.. _`Sphinx docs`: http://sphinx.pocoo.org/contents.html

Updating
........

To generate the docs, you'll need to have Sphinx installed
(``easy_install sphinx``). You also need to have ConceptNet and Divisi installed
so that their docstrings can be included. If Sphinx can't find them, it'll spit
out a bunch of warnings, and then produce **blank** documentation pages for
those parts of the documentation.

Running `make html` in the main documentation directory will put the
documentation together into nice-looking HTML pages, including pulling in all
of the docstrings.

If you have access to the docs server, and you have Fabric installed
(``easy_install fabric``), you can update the
documentation on the Web site (http://csc.media.mit.edu/docs/) by running::

  git commit -a
  fab test
  fab update    # if the test works

"fab update" might crash with an error about setting attributes on files, but
if it does, it already got far enough.

