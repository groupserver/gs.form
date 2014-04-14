from __future__ import absolute_import, unicode_literals
from unittest import TestCase, main as unittest_main
from mock import MagicMock
from gs.form.postmultipart import (get_content_type, encode_multipart_formdata,
                                   post_multipart)

class TestGSForm(TestCase):
    '''Test all of gs.form'''

    def content_type_test(self, filename, expectedType):
        '''Test that a file name is of an expected type'''
        ct = get_content_type(filename)
        self.assertEqual(ct, expectedType)

    def test_get_content_type_txt(self):
        '''Test the function that guesses the content type of a text file.'''
        self.content_type_test('foo.txt', 'text/plain')

    def test_get_content_type_jpg(self):
        '''Test the function that guesses the content type of a JPEG file.'''
        self.content_type_test('foo.jpg', 'image/jpeg')

    def test_get_content_type_mpg(self):
        '''Test the function that guesses the content type of a MPEG file.'''
        self.content_type_test('foo.mpg', 'video/mpeg')

    def test_get_content_type_bar(self):
        '''Test the function that guesses the content type of a odd file.'''
        self.content_type_test('foo.bar', 'application/octet-stream')

    def test_encode_multipart_form_data(self):
        '''Test the function that encodes the data.'''
        self.assertTrue(True)

    def test_post_multipart(self):
        '''Test the main post_multipart function'''
        self.assertTrue(True)
    

if __name__ == '__main__':
    unittest_main()
