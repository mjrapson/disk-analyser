from src.analyser.directory import Directory
from src.analyser.file import File

import unittest

class TestDirectory(unittest.TestCase):
    def test_basic_directory(self):
        self.assertEqual(Directory(name="dev").name, "dev")

    def test_directory_size(self):
        directory = Directory(name="test")

        self.assertEqual(directory.get_size(), 0)

        directory.children.append(File("doc.txt", 1024))
        directory.children.append(File("sound.wav", 512))
        self.assertEqual(directory.get_size(), 1024 + 512)

    