Introduction
============

This product contains the core functions and classes for dealing with forms
in `GroupServer`_. For the most part it consists of the
``gs.form.post_multipart`` utility, for posting data for a form (see
`post_multipart`_ below).

The ``gs.content.form`` module supplies the handling for the
user-interface [#contentForm]_.

``post_multipart``
==================

The ``gs.content.form.post_multipart`` function is used to post data to a
form.

Synopsis
--------

::

  post_multipart(host, selector, fields, files=[])

Arguments
---------

``host``:
  The HTTP host to connect to.

``selector``:
  The page that processes the form.

``fields``:
  The list of fields and the values to post. It is either

  * A dictionary of  the form (``'formField': value``), or

  * A list (or tuple) of 2-tuples of the form ``('formField', value)``.

``files``:
  An optional list of files as 3-tuples: ``('formField', fileName, fileData)``.

Returns
-------

A 3-tuple of ``status, reason, data``.

.. [#contentForm] See 
                  <https://source.iopen.net/groupserver/gs.content.form/summary>
.. _GroupServer: http://groupserver.org/
