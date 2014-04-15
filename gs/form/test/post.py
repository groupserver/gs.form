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
import httplib
from mock import MagicMock
from types import TupleType
from unittest import TestCase
from gs.form.postmultipart import post_multipart, Connection
from gs.form.postmultipart import httplib as ph


class FauxResponse(TupleType):

    @property
    def status(self):
        return self[0]

    @property
    def reason(self):
        return self[1]

    def read(self):
        return self[2]

class TestPostMultipart(TestCase):
    '''Test the post_multipart function of gs.form'''
    fauxResponse = FauxResponse(('200', 'Mock', 
                                 'He has joined the choir invisible'))
    fields = [('parrot', 'dead'), ('piranha', 'brother'),
              ('ethyl', 'frog')]
    files = [('unwritten', 'rule.txt', 'This is a transgression.'), 
             ('toad', 'sprocket.jpg', 'Tonight we look at violence.')]


    def setUp(self):
        ph.HTTPConnection.getresponse = MagicMock(return_value=self.fauxResponse)
        ph.HTTPConnection.request = MagicMock()

        ph.HTTPSConnection.getresponse = MagicMock(return_value=self.fauxResponse)
        ph.HTTPSConnection.request = MagicMock()
        
    def test_connection(self):
        connection = Connection('example.com')
        self.assertIsInstance(connection.host, httplib.HTTPConnection)

    def test_tls_connection(self):
        tlsConnection = Connection('example.com', usessl=True)
        self.assertIsInstance(tlsConnection.host, httplib.HTTPSConnection)

    def test_post_multipart_resp_status(self):
        retval = post_multipart('example.com', 'form.html', self.fields)
        self.assertEqual(len(retval), len(self.fauxResponse))

    def test_post_multipart_resp_status(self):
        retval = post_multipart('example.com', 'form.html', self.fields)
        self.assertEqual(retval[0], self.fauxResponse.status)

    def test_post_multipart_resp_reason(self):
        retval = post_multipart('example.com', 'form.html', self.fields)
        self.assertEqual(retval[1], self.fauxResponse.reason)

    def test_post_multipart_resp_read(self):
        retval = post_multipart('example.com', 'form.html', self.fields)
        self.assertEqual(retval[2], self.fauxResponse.read())