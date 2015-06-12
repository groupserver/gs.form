# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2014, 2015 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import absolute_import, unicode_literals, print_function
from collections import namedtuple
from io import BytesIO, StringIO
import sys
import requests
BYTES_TYPE = str if sys.version_info < (3, ) else bytes


Response = namedtuple('response', ['status', 'reason', 'text'])


def post_multipart(netloc, selector, fields, files=None, usessl=False):
    """Post fields and files to an http host as ``multipart/form-data``.

:param str netloc: The netloc (``host`` or ``host:port``).
:param str selector: The path to the form that will be posted to.
:param list fields: A sequence of ``(name, value)`` 2-tuple elements for
                    regular form fields.
:param list files: A sequence of ``(name, filename, value)`` 3-tuple
                   elements for data to be uploaded as files
:param bool usessl: ``True`` if TLS should be used to communicate with the
                    server.
:return: A 3-tuple: the reponse-status, reason, and data.

:Example:

    Post three normal form fields (``parrot``, ``piranah``, and ``ethyl``)
    and one file (the text file ``rule.txt``, sent as the ``unwritten`` form
    field) to ``example.com`` on port ``2585``, using normal HTTP rather
    than TLS (the default)::

        fields = [('parrot', 'dead'), ('piranha', 'brother'),
                  ('ethyl', 'frog')]
        files = [('unwritten', 'rule.txt', 'This is a transgression.')]
        r = post_multipart('example.com:2585', '/form.html', fields, files)
        status, reason, data = r
"""
    protocol = 'https' if usessl else 'http'
    u = '{0}://{1}{2}'.format(protocol, netloc, selector)
    d = dict(fields)
    f = files_to_dict(files)
    res = requests.post(u, data=d, files=f, timeout=4*60,
                        allow_redirects=True, verify=False, stream=False)
    retval = Response(res.status_code, res.reason, res.text)
    return retval


def files_to_dict(files):
    retval = None
    if files is not None:
        retval = {}
        for fileInfo in files:
            fieldName, filename, d = fileInfo
            data = BytesIO(d) if type(d) == BYTES_TYPE else StringIO(d)
            retval[fieldName] = (filename, data)
    return retval
