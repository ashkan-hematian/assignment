import os
import unittest
import helper.utils as utils


class TestUtils(unittest.TestCase):
    def test_is_convertible_to_int(self):
        self.assertTrue(utils.is_convertible_to_int('1'))
        self.assertTrue(utils.is_convertible_to_int('0'))
        self.assertFalse(utils.is_convertible_to_int('n91'))
        self.assertFalse(utils.is_convertible_to_int(' '))
        self.assertFalse(utils.is_convertible_to_int('74nd'))

        self.assertTrue(utils.is_convertible_to_int(1))
        self.assertTrue(utils.is_convertible_to_int(0))
        self.assertTrue(utils.is_convertible_to_int(3))

    def test_extract_file_names(self):

        os.environ['FILENAMES'] = 'a,b'
        self.assertEqual(utils.extract_file_names(), ['a', 'b'])

        os.environ['FILENAMES'] = ''
        self.assertEqual(utils.extract_file_names(), [])


if __name__ == '__main__':
    unittest.main()
