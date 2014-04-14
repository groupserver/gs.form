from __future__ import absolute_import, unicode_literals
from unittest import TestCase, main as unittest_main
from mock import MagicMock
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
        retval = encode_multipart_formdata(self.fields, [])
        self.assertEqual(retval[0][:20], 'multipart/form-data;')

    def test_encode_multipart_form_data_fields(self):
        '''Test the function that the field IDs are in the retval.'''
        retval = encode_multipart_formdata(self.fields, [])
        names = ['name="{}"'.format(f[0]) for f in self.fields]
        for name in names:
            self.assertIn(name, retval[1])

    def test_encode_multipart_form_data_files_names(self):
        '''Test the field-names for the files are right'''
        retval = encode_multipart_formdata([], self.files)
        names = ['name="{}"'.format(f[0]) for f in self.files]
        for name in names:
            self.assertIn(name, retval[1])

    def test_encode_multipart_form_data_files_filenames(self):
        '''Test the filenames for the files are right'''
        retval = encode_multipart_formdata([], self.files)
        filenames = ['filename="{}"'.format(f[1]) for f in self.files]
        for filename in filenames:
            self.assertIn(filename, retval[1])

if __name__ == '__main__':
    unittest_main()
