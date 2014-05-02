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
from cgi import FieldStorage
import os
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO  # lint:ok
from unittest import TestCase, main as unittest_main
from gs.form.postmultipart import encode_multipart_formdata


class TestEncode(TestCase):
    '''Test the encode_content_type function of gs.form'''

    def setUp(self):
        self.fields = [('parrot', 'dead'), ('piranha', 'brother'),
                       ('ethyl', 'frog')]
        self.files = [('unwritten', 'rule.txt', 'This is a transgression.'),
                      ('boot', 'in.jpg', 'Tonight we look at violence.')]

    def test_encode_multipart_form_data_retval(self):
        '''Test that we get a 2-tuple back from the encode_multipart
        function'''
        retval = encode_multipart_formdata(self.fields, [])
        self.assertEqual(len(retval), 2)

    def test_encode_multipart_form_data_encoding(self):
        '''Test the function that encodes the data.'''
        contentType, data = encode_multipart_formdata(self.fields, [])
        self.assertEqual(contentType[:19], 'multipart/form-data')

    def test_encode_multipart_form_data_fields(self):
        '''Test the function that the field IDs are in the retval.'''
        contentType, data = encode_multipart_formdata(self.fields, [])
        names = ['name="{}"'.format(f[0]) for f in self.fields]
        for name in names:
            self.assertIn(name, data)

    def test_encode_multipart_form_data_files_names(self):
        '''Test the field-names for the files are right'''
        contentType, data = encode_multipart_formdata([], self.files)
        names = ['name="{}"'.format(f[0]) for f in self.files]
        for name in names:
            self.assertIn(name, data)

    def test_encode_multipart_form_data_files_filenames(self):
        '''Test the filenames for the files are right'''
        contentType, data = encode_multipart_formdata([], self.files)
        filenames = ['filename="{}"'.format(f[1]) for f in self.files]
        for filename in filenames:
            self.assertIn(filename, data)

    def test_parse(self):
        'Test if cgi.FieldStorage can parse the data'
        contentType, data = encode_multipart_formdata(self.fields, self.files)
        d = StringIO(data)
        # --=mpj17=-- Pretend we does be a web server, weeee!
        os.environ['CONTENT_TYPE'] = contentType
        os.environ['REQUEST_METHOD'] = 'POST'
        # Parse the data
        fs = FieldStorage(fp=d, environ=os.environ)

        allFields = self.fields + self.files
        self.assertEqual(len(allFields), len(fs.list))
        for fieldId, fieldValue in self.fields:
            self.assertIn(fieldId, fs)
            self.assertEqual(fieldId, fs[fieldId].name)
            self.assertEqual(fieldValue, fs[fieldId].value)
        for fileId, filename, fileValue in self.files:
            self.assertIn(fileId, fs)
            self.assertEqual(fileId, fs[fileId].name)
            self.assertEqual(filename, fs[fileId].filename)
            self.assertEqual(fileValue, fs[fileId].value)

if __name__ == '__main__':
    unittest_main()
