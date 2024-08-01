import unittest
from io import StringIO
from unittest.mock import patch

from helper.time_utils import Time


class TestTime(unittest.TestCase):
    def test_time(self, obj=None):
        time = Time()

        # set message
        message1: str = "random text"
        time.setMessage(message1)
        self.assertEqual(time.message, message1)
        message2: str = "another text"
        time.setMessage(message2)
        self.assertEqual(time.message, message2)

        # start
        self.assertIsNotNone(time.start_time)

        # end
        with patch('sys.stdout', new=StringIO()) as fake_out:
            time.end()
            output = fake_out.getvalue().strip()
            self.assertFalse(message1 in output)
            self.assertTrue(message2 in output)
