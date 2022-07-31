import unittest

from translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(" ")," ") # test null to null
        self.assertEqual(french_to_english("Bonjour"), "Hello")  # test Hello to Bonjour
        

class TestEnglishToFrench(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(english_to_french(" ")," ") # test null to null
        self.assertEqual(english_to_french("Hello"), "Bonjour") # test Bonjour to Hello
        
unittest.main()