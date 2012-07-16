# coding=utf-8
'''Post multipart form-data to a zope.formlib form. Originally from
<http://code.activestate.com/recipes/146306-http-client-to-post-using-multipartform-data/>.
'''
import httplib, mimetypes

def post_multipart(host, selector, fields, files=[]):
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
    h = httplib.HTTPConnection(host)
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
    BOUNDARY = '----------ThIs_Is_tHe_bouNdaRY_$'
    CRLF = '\r\n'
    L = []
    for (key, value) in fields:
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"' % key)
        L.append('')
        L.append(value)
    for (key, filename, value) in files:
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"; '\
                     'filename="%s"' % (key, filename))
        L.append('Content-Type: %s' % get_content_type(filename))
        L.append('')
        L.append(value)
    L.append('--' + BOUNDARY + '--')
    L.append('')
    body = CRLF.join(L)
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
    return content_type, body

def get_content_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'
