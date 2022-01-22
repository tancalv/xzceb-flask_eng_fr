"""Import test module"""
import unittest
from translator import frenchToEnglish, englishToFrench

class TestEnglishToFrench(unittest.TestCase):
    """Tests cases for all englishToFrench function in module translator.py"""
    def test(self):
        """"Tests for null inputs"""
        self.assertEqual(englishToFrench(""),"")
    def test_one_word(self):
        """"Tests for all one word inputs"""
        self.assertEqual(englishToFrench("Hello"),"Bonjour")

class TestFrenchToEnglish(unittest.TestCase):
    """Tests cases for all frenchToEnglish function in module translator.py"""
    def test_null(self):
        """"Tests for null inputs"""
        self.assertEqual(frenchToEnglish(""),"")
    def test_one_word(self):
        """"Tests for all one word inputs"""
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")
unittest.main()
