import swan
from unittest import TestCase
import unittest
import io
import random
import warnings


class FSTest(TestCase):
    def test_stream_hashing(self):
        streams = (
            io.BytesIO(),
            io.BytesIO()
        )
        for stream in streams:
            stream.write(bytes(f'Hello There general you know who{random.randint(1, 1000)}'.encode('utf-8')))
            stream.getbuffer()
            stream.seek(0)

        self.assertNotEqual(swan.ioutil.stream_sha256_hash(streams[0]),
                            swan.ioutil.stream_sha256_hash(streams[1]), )

    def test_md5_deprecation(self):
        stream = io.BytesIO()
        stream.write(b'Test of MD5 deprecation')
        stream.seek(0)

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            swan.ioutil.stream_md5_hash(stream)  # Should throw a deprecation warning
            self.assertGreaterEqual(len(w), 1)
            self.assertTrue(issubclass(w[-1].category, DeprecationWarning))

    def test_file_not_found(self):
        with self.assertRaises(IOError):
            reqs = swan.fs.File('requirements_testing_dummy.tx', True)

    def test_split_path(self):
        self.assertEqual(swan.ioutil.split_path('/a/b/c/.d.a'), ('/a/b/c', '.d.a'))


if __name__ == '__main__':
    unittest.main()
