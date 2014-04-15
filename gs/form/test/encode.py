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
from unittest import TestCase, main as unittest_main
from gs.form.postmultipart import encode_multipart_formdata


class TestEncode(TestCase):
    '''Test the encode_content_type function of gs.form'''

    def setUp(self):
        self.fields = [('parrot', 'dead'), ('piranha', 'brother'),
                       ('ethyl', 'frog')]
        self.files = [('unwritten', 'rule.txt', 'This is a transgression.'),
                      ('ethyl', 'frog.jpg', 'Tonight we look at violence.')]

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

if __name__ == '__main__':
    unittest_main()
