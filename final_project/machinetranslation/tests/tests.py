import unittest

from translator import englishToFrench
from translator import frenchToEnglish

class TestString(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench("Hello"),"Bonjour") 
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello") 

unittest.main()