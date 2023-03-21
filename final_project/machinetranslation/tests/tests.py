import unittest
from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("Yes"), "Oui")
        self.assertEqual(english_to_french("Boy"), "Garçon")
        self.assertEqual(english_to_french(""), "error")


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Oui"), "Yes")
        self.assertEqual(french_to_english("Garçon"), "Boy")
        self.assertEqual(french_to_english(""), "error")


if __name__ == '__main__':
    unittest.main()