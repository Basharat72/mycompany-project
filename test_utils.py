import unittest
from utils import greet
from io import StringIO
import sys

class TestUtils(unittest.TestCase):
    def test_greet_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        greet()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Namaste from Ram!")

if __name__ == '__main__':
    unittest.main()
