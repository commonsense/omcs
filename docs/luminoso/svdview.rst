.. _svdview:

SVDView (a quick and dirty visualizer)
======================================

SVDView is a viewer for multi-dimensional data, such as the SVD results of
Divisi. It is comparable to :doc:`Luminoso </luminoso/index>`, but it makes no
attempt to have a user interface to speak of. It's faster, but it does less.

SVDView is a Processing application. To use it, install it into your Processing
workspace, choose "svdview" from Processing's project menu, and run it.

You will see a set of *points*, generally representing words or phrases that
appeared in the data, and a set of perpendicular *axes* that define where the
points appear. Many of the points will also be labeled, particularly those that
are close to your mouse pointer.

This is not just a three-dimensional view! As you interact with SVDView, you
will be able to see many axes emerging from the center of the view (up to 20 in
this version). The purpose of SVDView is to help you make sense of this
multi-dimensional data.

Setting up the data
-------------------
The `write_packed` function in `csc.divisi.export_svdview` will write a Divisi
matrix in a form that SVDView understands: a pair of files, called
*filename*.coords and *filename*.names.

Put these files in your svdview/data directory. They might not work elsewhere.

When you start SVDView, it will prompt you for which data file to load. Choose
the .coords file for the data set you're interested in.

At first, you will be looking at the first two dimensions of the data. You can
use the mouse or the keyboard to change your viewpoint, as described below.

Using the mouse
---------------

* Use the mouse wheel (or the scroll feature of a trackpad) to zoom in and out.
* Drag with the right mouse button to pan the view.
* Drag with the left mouse button to *rotate* the view. 

When you rotate using the mouse, you do so by "grabbing" a point and pulling it
in the direction that you move your mouse. The rotation will cause other nearby
points to move in that direction as well. While you rotate, the points will
also be colored in a way that distinguishes nearby points from far-away ones.

The rotations might get a bit confusing, because you have more than three
dimensions to rotate through! The current version of SVDView allows you to
rotate through 20 dimensions of data.

Using the keyboard
------------------

You can also use the keyboard to rotate in precise directions. Pressing the
keys "0" through "9" will rotate that numbered axis toward the right side of
the screen, and the next-numbered axis toward the top. If you hold one of those
keys, you will eventually be looking at those two axes straight on.

If you aren't looking for anything in particular, you can have the program
*auto-rotate*. Press "g" to start automatic rotation and "s" to stop.

The "r" key resets the entire program.

