from src.analyser.analyser import analyse

import unittest

class TestAnalyser(unittest.TestCase):
    def test_analyse_empty_path(self):
        self.assertRaises(ValueError, analyse, "")
    
    def test_analyse_invalid_path(self):
        self.assertRaises(ValueError, analyse, "some:/junk")

    