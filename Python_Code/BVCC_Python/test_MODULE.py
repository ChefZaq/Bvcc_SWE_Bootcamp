import unittest
from MODULE import number_factors
from MODULE import anagram
from MODULE import factorial

class TestMODULE(unittest.TestCase):
    def test_number_factors(self):
        assert number_factors(6) == [1,2,3,6]
        self.assertEqual(number_factors(0),[])
        self.assertTrue(number_factors(64) == [1,2,4,8,16,32,64])
        self.assertEqual(number_factors(47),[1,47])
        self.assertEqual(number_factors(-47),[])
        self.assertNotEqual(number_factors(49),[1,49])

    def test_anagram(self):
        #assert anagram('aNaGram', 'nag a ram') == True
        assert (anagram('','hello')) == False
        assert (anagram('world','')) == False
        self.assertEqual(anagram('123','abc'),False)
        self.assertFalse(anagram('aNaGram', 'nag a ram') != True)
        self.assertTrue(anagram('evil', 'vile '))
        self.assertFalse(anagram('eyes', 'yess'))
        self.assertEqual(anagram('racecar','car race'),True)
        self.assertNotEqual(anagram('pork', 'chop'),True) 

    def test_factorial(self):
        self.assertGreaterEqual(factorial(5),100)
        self.assertEqual(factorial(2),2)
        self.assertFalse(factorial(3)>7)

if __name__ == "__main__":
    unittest.main()