from src.analyser.directory import Directory
from src.analyser.file import File
from src.analyser.size import Size

import unittest

class TestDirectory(unittest.TestCase):
    def test_basic_directory(self):
        self.assertEqual(Directory(name="dev").name, "dev")

    def test_directory_size(self):
        directory = Directory(name="test")

        self.assertEqual(directory.get_size(), Size(0))

        directory.children.append(File("doc.txt", Size(1024)))
        directory.children.append(File("sound.wav", Size(512)))
        self.assertEqual(directory.get_size(), Size(1536))

    