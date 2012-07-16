Introduction
============

``post_multipart``
==================

The ``gs.content.form.post_multipart`` function is used to post data to a
``zope.formlib`` form [#formlib]_.

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

.. _OnlineGroups.Net: http://onlinegroups.net/

.. [#formlib] See <http://docs.zope.org/zope.formlib/>
