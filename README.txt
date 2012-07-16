Introduction
============

This product contains many useful functions and classes for dealing with
``zope.formlib`` forms [#formlib]_ in `GroupServer`_.

``gs.content.form.SiteForm``:
  An abstract base-class for a that provides the ``siteInfo`` and
  ``loggedInUser`` properties.

``groupserver.FormStatusMessage``:
  A *content provider* for displaying the status-message of a form, after
  it submits.

``gs.content.form.radio_widget``:
  A factory for creating a non-broken radio-widget.

``gs.content.form.select_widget``:
  A factory for creating a select-widget that is slightly larger than the
  normal widget (15 items).

``gs.content.form.disabled_text_widget``:
  A factory for creating text widget that is always disabled.

``gs.content.form.post_multipart``:
  A utility for posting data for a form (see `post_multipart`_ below).

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

.. [#formlib] See <http://docs.zope.org/zope.formlib/>
.. _GroupServer: http://groupserver.org/
