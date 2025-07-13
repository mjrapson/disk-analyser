from src.analyser.size import Size

import unittest

class TestSize(unittest.TestCase):
    def test_size_str_bytes(self):
        self.assertEqual(str(Size(100)), "100 B")
    
    def test_size_str_kb(self):
        self.assertEqual(str(Size(10000)), "10.0 KB")

    def test_size_str_mb(self):
        self.assertEqual(str(Size(20000000)), "20.0 MB")