Tensors and Views
=================
The fundamental objects represented by Divisi are *tensors* and *views*.

Tensors
-------

In Divisi, you collect and manipulate data in :class:`Tensors <Tensor>`. 
A Tensor, in short, is an array of data that we can do math to.

This is the general term that we use for such things throughout Divisi. The
term "tensor" may evoke images of complicated theoretical physics, but that's
not what we're going for. If you understand vectors and matrices, you
understand two examples of tensors.

The most important thing to know about a tensor is its *order*, which is
effectively its number of "dimensions". The order of a tensor tells you how
many inputs you have to give it to get a value out.

- A *vector* is a 1st-order tensor. To look up a value in a vector, you give it
  a single input (an *index*) and get a number as an output.

  In the vector `v = [3, 5, -2]`, the possible inputs are the indices 0, 1, and
  2, which give you the outputs 3, 5, and -2 respectively.

- A *matrix* is a 2nd-order tensor. To look up a value in a matrix, you give it
  two inputs: a row index and a column index.

- Divisi can represent tensors of order 3 or higher, as well.

Tensors of order 2 and higher can be *sparse* or *dense*. In a dense tensor,
you can look up essentially any combination of indices and find a useful
value. The output of an :ref:`SVD <SVD>`, for example, is a dense matrix. Dense
matrices can be expressed by arrays that list all of their values, which is
how the :class:DenseTensor class works.

In a sparse tensor, most combinations of indices bring you to values that are
zero or "missing". Only a relatively small subset of values -- the useful ones
-- are non-zero. As an example, when :ref:`ConceptNet <conceptnet>` is
represented as a matrix, it is a sparse matrix.  Sparse tensors can be
expressed as dictionaries that enumerate only the useful values, leaving the
large number of zero values implied, which is how the :class:`DictTensor` class
works.

Tensors support various operations through their API, described below. However,
they also act like Python dictionaries wherever possible -- for example, you
can use `values()` to get a list of their values, the `[]` operator to access
those values, and `iteritems()` to get an iterator over keys and values.

.. _views:

Views
-----
A View wraps around a Tensor to change the way you look at the data in it. One
of the most important uses of Views, in Divisi, is to *label* a tensor.

In a standard mathematical vector or matrix, the indices are simply integers,
like in a Python list. However, your data is presumably not just numbers
indexed by other numbers.

Instead, Divisi tensors can refer to data using meaningful
indices that you choose, such as strings of text, which makes them act more like
Python dictionaries than lists. This functionality is provided by
:class:`divisi.labeled_view.LabeledView`; see :ref:`labeled_view` for more.

Different kinds of views can be layered on top of one another. To access the
contents of the view *v*, no matter whether it wraps a tensor or another view,
you can call `v.unwrap()` (as of version 0.6). `unwrap()` also works on plain
Tensors, returning the array or dictionary that is being used to store the
data.

.. include:: ../recipes/divisi_labels.txt

.. note::

    Whether a tensor is labeled is independent of whether it is sparse or
    dense. All combinations of these are possible in Divisi.

API Documentation
-----------------

The base objects of Divisi, Tensors and Views, are defined in the ``tensor``
module.

.. automodule:: csc.divisi.tensor
  :members:

