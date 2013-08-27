# -*- coding: utf-8 -*-
# Post multipart form-data to a zope.formlib form. Originally from
# <http://code.activestate.com/recipes/146306-http-client-to-post-using-multipartform-data/>

from cStringIO import StringIO
import httplib
import mimetools
import mimetypes


def post_multipart(host, selector, fields, files=[], usessl=False):
    """
    Post fields and files to an http host as multipart/form-data.  fields
    is a sequence of (name, value) elements for regular form fields.  files
    is a sequence of (name, filename, value) elements for data to be
    uploaded as files Return the server's response page.
    """
    if type(fields) == dict:
        f = fields.items()
    else:
        f = fields
    assert type(f) in (list, tuple), 'Fields must be a dict, tuple, or list, '\
        'not "%s".' % type(fields)

    content_type, body = encode_multipart_formdata(f, files)
    if usessl:
        connectionFactory = httplib.HTTPSConnection
    else:
        connectionFactory = httplib.HTTPConnection

    h = connectionFactory(host)
    headers = {
        'User-Agent': 'noddy post it',
        'Content-Type': content_type
        }
    h.request('POST', selector, body, headers)
    res = h.getresponse()
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
