import unittest

from translator import english_to_french, french_to_english

class Testetof1(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")

class Testetof2(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(" ")," ")

class Testftoe1(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")

class Testftoe2(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(" ")," ")     

unittest.main()
