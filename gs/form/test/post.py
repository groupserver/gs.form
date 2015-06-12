# -*- coding: utf-8 -*-
##############################################################################
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
##############################################################################
from __future__ import absolute_import, unicode_literals, print_function
from mock import patch
from unittest import TestCase
from gs.form.postmultipart import post_multipart, files_to_dict


class TestPostMultipart(TestCase):
    '''Test the post_multipart function of gs.form'''
    fields = [('parrot', 'dead'), ('piranha', 'brother'),
              ('ethyl', 'frog')]
    files = [('unwritten', 'rule.txt', 'This is a transgression.'),
             ('toad', 'sprocket.jpg', 'Tonight we look at violence.')]

    @patch('gs.form.postmultipart.requests.post')
    def test_response(self, faux_post):
        'Test that we get the response back'
        fauxRes = faux_post()
        eCode = 987
        eReason = 'Being tested'
        eText = 'Tonight on Ethel the Frog we look at violence.'
        fauxRes.status_code = eCode
        fauxRes.reason = eReason
        fauxRes.text = eText

        r = post_multipart('example.com', '/form.json', {})
        self.assertEqual(eCode, r[0])
        self.assertEqual(eCode, r.status)
        self.assertEqual(eReason, r[1])
        self.assertEqual(eReason, r.reason)
        self.assertEqual(eText, r[2])
        self.assertEqual(eText, r.text)

    @patch('gs.form.postmultipart.requests.post')
    def test_request_http(self, faux_post):
        post_multipart('example.com', '/form.json', {})
        args, kwargs = faux_post.call_args
        self.assertEqual('http://example.com/form.json', args[0])

    @patch('gs.form.postmultipart.requests.post')
    def test_request_tls(self, faux_post):
        post_multipart('example.com', '/form.json', {}, usessl=True)
        args, kwargs = faux_post.call_args
        self.assertEqual('https://example.com/form.json', args[0])

    @patch('gs.form.postmultipart.requests.post')
    def test_tuple_fields(self, faux_post):
        post_multipart('example.com', '/form.json', self.fields)
        expected = dict(self.fields)
        args, kwargs = faux_post.call_args
        self.assertEqual(expected, kwargs['data'])

    @patch('gs.form.postmultipart.requests.post')
    def test_dict_fields(self, faux_post):
        d = dict(self.fields)
        post_multipart('example.com', '/form.json', d)
        args, kwargs = faux_post.call_args
        self.assertEqual(d, kwargs['data'])

    @patch('gs.form.postmultipart.requests.post')
    def test_files(self, faux_post):
        post_multipart('example.com', '/form.json', {}, self.files)
        args, kwargs = faux_post.call_args
        self.assertEqual(len(self.files), len(kwargs['files']))


class TestFilesToDict(TestCase):
    'Test the files_to_dict function'
    files = [('unwritten', 'rule.txt', 'This is a transgression.'),
             ('toad', 'sprocket.jpg', b'Tonight we look at violence.')]

    def test_none(self):
        r = files_to_dict(None)
        self.assertIs(None, r)

    def assertFile(self, expected, v):
        eFieldName, eFilename, eData = expected
        vFieldName = v.keys()[0]
        self.assertEqual(
            eFieldName, vFieldName,
            'Expected key name "{0}", got "{1}"'.format(eFieldName, vFieldName))
        vFilename = v[eFieldName][0]
        self.assertEqual(
            eFilename, vFilename,
            'Expected file name "{0}", got "{1}"'.format(eFilename, vFilename))
        vData = v[eFieldName][1].read()
        self.assertEqual(
            eData, vData,
            'Expected data "{0}", got "{1}"'.format(eData, vData))

    def test_unicode_file(self):
        f = [self.files[0]]  # Just the first file, as a list of one
        r = files_to_dict(f)
        self.assertFile(self.files[0], r)

    def test_binary_file(self):
        f = [self.files[1]]
        r = files_to_dict(f)
        self.assertFile(self.files[1], r)

    def test_all(self):
        r = files_to_dict(self.files)
        self.assertEqual(len(self.files), len(r))
