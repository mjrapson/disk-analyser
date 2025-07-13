from src.analyser.file import File

import unittest

class TestFile(unittest.TestCase):
    def test_file_basic(self):
        file = File("doc.txt", 32)
        self.assertEqual(file.name, "doc.txt")
        self.assertEqual(file.size, 32)