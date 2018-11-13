import iolib
from unittest import TestCase, mock
import unittest
from io import BytesIO


class FSTest(TestCase):
    @mock.patch('iolib.fs.open')
    def test_file_hashing(self):
        with mock.patch('iolib.fs.open') as mock_open:
            mock_open.return_value.__enter__.return_value = BytesIO().write('Hello There general you know who'.encode('utf-8'))
            f1 = iolib.fs.File('aaa', True)
            f2 = iolib.fs.File('bbb', True)
            self.assertEqual(f1.hash[0], f2.hash[0], 'hash of different files, pass')

    def test_file_not_found(self):
        with self.assertRaises(IOError):
            reqs = iolib.fs.File('requirements_testing_dummy.tx', True, 'File not found exception handling, not pass')
        # print('File not found exception handling, pass')

    def test_split_path(self):
        self.assertEqual(iolib.util.Utils.split_path('/a/b/c/.d.a'), ('/a/b/c', '.d.a'), 'split_path , not pass')
        # print('split_path , pass')


if __name__ == '__main__':
    unittest.main()
