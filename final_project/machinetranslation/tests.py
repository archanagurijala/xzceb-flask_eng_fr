import unittest

from translator import englishToFrench
from translator import frenchToEnglish

class TestString(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench("Hello"),"Bonjour") 
    def test2(self): 
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello") 
    def test3(self): 
        self.assertNotEqual(frenchToEnglish("null"),"Hello") 
    def test4(self): 
        self.assertNotEqual(englishToFrench("null"),"Bonjour")  

unittest.main()