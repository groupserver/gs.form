===========
``gs.form``
===========
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Submit a form to a Web server using a ``POST``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2015-06-10
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.Net`_.

Introduction
============

This package provides a useful way of pushing data to a server by
making a ``POST`` to a form. While originally written for
GroupServer_, there is nothing specific to GroupServer in this
product. Mostly it is a light facade around the ``requests``
library <http://requests.readthedocs.org>. Use ``requests``
instead of this module.

Acknowledgements
================

The post_multipart_ code was based on `a Python recipe by Wade
Leftwich`_. It was changed to use ``email.multipart`` to create
the multipart document that is sent using a ``POST``.

Resources
=========

- Documentation: http://groupserver.rtfd.org/projects/gsform/
- Code repository: https://github.com/groupserver/gs.form
- Questions and comments to
  http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
.. _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/
.. _a Python recipe by Wade Leftwich: http://code.activestate.com/recipes/146306-http-client-to-post-using-multipartform-data/
