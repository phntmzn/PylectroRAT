

# Unit tests for keylogger.py in PlectroRAT

import unittest
from unittest.mock import patch, MagicMock
import src.keylogger as keylogger

class TestKeylogger(unittest.TestCase):

    def setUp(self):
        keylogger.clear_log()

    def test_on_press_character(self):
        mock_key = MagicMock()
        mock_key.char = 'a'
        keylogger.on_press(mock_key)
        self.assertIn('a', keylogger.get_log())

    def test_on_press_special_key(self):
        mock_key = MagicMock()
        mock_key.char = None
        mock_key.name = 'enter'
        keylogger.on_press(mock_key)
        self.assertIn('[enter]', keylogger.get_log())

    def test_clear_log(self):
        keylogger.log.append('test')
        keylogger.clear_log()
        self.assertEqual(keylogger.get_log(), '')

if __name__ == "__main__":
    unittest.main()