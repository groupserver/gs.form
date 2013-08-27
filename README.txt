===========
``gs.form``
===========
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Core form handling for GroupServer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2013-08-27
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 3.0 New Zealand License`_
  by `OnlineGroups.Net`_.

Introduction
============

This product contains the core functions and classes for dealing with forms
in GroupServer_. For the most part it consists of the post_multipart_
utility, for posting data to a form.

The ``gs.content.form`` module supplies the handling for the
user-interface [#contentForm]_.

``post_multipart``
==================

The ``gs.content.form.post_multipart`` function is used to post data to a
form.

Synopsis
--------

::

  post_multipart(host, selector, fields, files=[], usessl=False)

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

  The **submit button** is also passed through as a field. Normally the
  ``value`` is set to the label of the button.

``files``:
  An optional list of files as 3-tuples: ``('formField', fileName, fileData)``.

``usessl``:
  Whether to use SSL to communicate to the server.

Returns
-------

A 3-tuple of ``status, reason, data``.

Acknowledgements
================

The post_multipart_ code was based on `a Python recipe by Wade Leftwich`_.


Resources
=========

- Code repository: https://source.iopen.net/groupserver/gs.form
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
.. _Creative Commons Attribution-Share Alike 3.0 New Zealand License:
   http://creativecommons.org/licenses/by-sa/3.0/nz/
.. _a Python recipe by Wade Leftwich: http://code.activestate.com/recipes/146306-http-client-to-post-using-multipartform-data/

.. [#contentForm] See 
                  <https://source.iopen.net/groupserver/gs.content.form/summary>

