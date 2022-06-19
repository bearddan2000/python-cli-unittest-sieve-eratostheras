from io import StringIO
from unittest.mock import patch
import unittest

import main

class TestMain(unittest.TestCase):
    """docstring for TestMain."""
    def test_SieveOfEratosthenes(self):
        with patch('sys.stdout', new = StringIO()) as captured:
            main.SieveOfEratosthenes(2)
            self.assertEqual(captured.getvalue(), "2\n")
