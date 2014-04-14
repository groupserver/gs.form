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
from __future__ import unicode_literals
from io import StringIO
import httplib
import mimetools
import mimetypes


class Connection(object):
    '''A wrapper for the HTTP(S) connection'''
    def __init__(self, host, port=None, usessl=False):  # Port?
        if usessl:
            self.connectionFactory = httplib.HTTPSConnection
        else:
            self.connectionFactory = httplib.HTTPConnection            
        self.host = self.connectionFactory(host)  # Port?

    def request(self, requestType, selector, body, headers):
        self.host.request(requestType, selector, body, headers)
        
    def getresponse(self):
        retval = self.host.getresponse()
        return retval


def post_multipart(host, selector, fields, files=[], usessl=False):
    """
    Post fields and files to an http host as multipart/form-data.  

    Arguments
    ``fields``: a sequence of (name, value) elements for regular form fields.  
    ``files``:  a sequence of (name, filename, value) elements for data to be
                uploaded as files 

    Returns the server's response page.
    """
    if type(fields) == dict:
        f = fields.items()
    else:
        f = fields
    if type(f) not in (list, tuple):
        m = 'Fields must be a dict, tuple, or list, not "{0}".'
        msg = m.format(type(fields))
        raise ValueError(msg)

    connection = Connection(host, usessl=usessl)
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
    boundary = mimetools.choose_boundary()
    buf = StringIO()
    for (key, value) in fields:
        buf.write('--%s\r\n' % boundary)
        buf.write('Content-Disposition: form-data; name="%s"' % key)
        buf.write('\r\n\r\n' + value + '\r\n')
    for (key, filename, value) in files:
        buf.write('--%s\r\n' % boundary)
        buf.write('Content-Disposition: form-data; name="%s"; '
                     'filename="%s"\r\n' % (key, filename))
        buf.write('Content-Type: %s\r\n' % get_content_type(filename))
        buf.write('\r\n%s\r\n' % value)

    buf.write('--%s--\r\n\r\n' % boundary)
    buf = buf.getvalue()

    content_type = 'multipart/form-data; boundary=%s' % boundary

    return content_type, buf


def get_content_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'
