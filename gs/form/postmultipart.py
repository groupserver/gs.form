# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
from __future__ import absolute_import, unicode_literals
from email.mime.multipart import MIMEMultipart
from email.mime.nonmultipart import MIMENonMultipart
from email.header import Header
import mimetypes
from gs.core import to_unicode_or_bust
from .httplib import HTTPSConnection, HTTPConnection
UTF8 = 'utf-8'


class Connection(object):
    '''A wrapper for the HTTP(S) connection'''
    def __init__(self, host, port=None, usessl=False):
        if usessl:
            self.connectionFactory = HTTPSConnection
        else:
            self.connectionFactory = HTTPConnection
        self.host = self.connectionFactory(host, port)

    def request(self, requestType, selector, body, headers):
        self.host.request(requestType, selector, body, headers)

    def getresponse(self):
        retval = self.host.getresponse()
        return retval


def post_multipart(host, selector, fields, files=[], port=None, usessl=False):
    """Post fields and files to an http host as multipart/form-data.

    Arguments
    ``fields``: a sequence of (name, value) 2-tuple elements for regular form
                fields.
    ``files``:  a sequence of (name, filename, value) 3-tuple elements for data
                to be uploaded as files

    Returns a 3-tuple: the reponse-status, reason, and data."""
    if type(fields) == dict:
        f = list(fields.items())
    else:
        f = fields
    if type(f) not in (list, tuple):
        m = 'Fields must be a dict, tuple, or list, not "{0}".'
        msg = m.format(type(fields))
        raise ValueError(msg)

    connection = Connection(host, port=port, usessl=usessl)
    content_type, body = encode_multipart_formdata(f, files)
    headers = {
        'User-Agent': 'gs.form',
        'Content-Type': content_type
        }
    connection.request('POST', selector, body, headers)
    res = connection.getresponse()
    return res.status, res.reason, res.read()


def encode_multipart_formdata(fields, files):
    """
    fields is a sequence of (name, value) elements for regular form fields.
    files is a sequence of (name, filename, value) elements for data to be
    uploaded as files Return (content_type, body) ready for httplib.HTTP
    instance
    """

    container = MIMEMultipart('form-data')
    for (key, value) in fields:
        part = MIMENonMultipart('foo', 'bar')
        part['Content-Disposition'] = Header('form-data').encode()
        part.set_param('name', key, 'Content-Disposition')
        data = to_unicode_or_bust(value).encode(UTF8)
        part.set_payload(data)
        del(part['Content-Type'])
        del(part['MIME-Version'])
        container.attach(part)
    for (key, filename, value) in files:
        part = MIMENonMultipart('foo', 'bar')
        part['Content-Disposition'] = Header('form-data').encode()
        part.set_param('name', key, 'Content-Disposition')
        part.set_param('filename', filename, 'Content-Disposition')
        part['Content-Type'] = Header(get_content_type(filename)).encode()
        part.set_payload(value)
        del(part['Content-Type'])
        del(part['MIME-Version'])
        container.attach(part)

    content_type = container['Content-Type']
    del(container['MIME-Version'])
    buf = container.as_string()
    return content_type, buf


def get_content_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'
