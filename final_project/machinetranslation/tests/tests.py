import unittest
from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("Yes"), "Oui")
    def test2(self):
        self.assertNotEqual(english_to_french("Table"), "Garçon")
    def test3(self):
        self.assertNotEqual(english_to_french(" "), "null")


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Oui"), "Yes")
    def test2(self):
        self.assertNotEqual(french_to_english("Garçon"), "Table")
    def test3(self):
        self.assertNotEqual(french_to_english(" "), "null")


if __name__ == '__main__':
    unittest.main()