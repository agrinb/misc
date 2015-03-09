
from hash_me import Hash_me
import unittest
import pdb 



class HashMeTest(unittest.TestCase):    
    #ha is an instance of Hash_me
    def test_init(self):
        ha = Hash_me(5,6)
        ha2 = Hash_me('string', 1)
        ha3 = Hash_me('string1', "string2")
        self.assertIsInstance(ha, Hash_me)
        self.assertIsInstance(ha2, Hash_me)
        self.assertIsInstance(ha3, Hash_me)

    #instantiating a Hash with more than two args
    def test_init_mult(self):
        ha = Hash_me(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
            26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
            51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75,
            76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100)
        self.assertEquals(ha.get(5), 6)
        self.assertEquals(ha.get(33), 34)
        self.assertEquals(ha.get(55), 56)
        self.assertEquals(ha.get(75), 76)

    def test_rehash(self):
        ha = Hash_me(5,6,7,8)
        hash_size = len(ha.bins)
        ha.rehash()
        self.assertEquals(len(ha.bins), hash_size * 2 )
        self.assertEquals(ha.get(5), 6)
        self.assertEquals(ha.get(7), 8)

    def test_init_with_strings(self):
        string1 = 'string1'
        string2 = 'string2'
        ha = Hash_me('string1', 'string2')
        self.assertEquals(ha.get('string1'), 'string2')

    def test_add(self):
        ha = Hash_me(8,9)
        self.assertEquals(ha.get(8), 9)
    
    def test_get(self):
        ha = Hash_me(8,9)
        self.assertEquals(ha.get(8), 9)

    def test_keys(self):
        ha = Hash_me(8,9)
        ha2 = Hash_me(55,66)
        ha.merge(ha2)
        self.assertItemsEqual(ha.keys(),[55, 8])

    def test_values(self):
        ha = Hash_me(8,9)
        ha2 = Hash_me(55,66)
        ha.merge(ha2)
        self.assertItemsEqual(ha.values(),[66, 9])

    def test_merge(self):
        ha = Hash_me(8,9)
        ha2 = Hash_me(55,66)
        ha.merge(ha2)
        self.assertItemsEqual(ha.keys(),[55, 8])
        self.assertItemsEqual(ha.values(),[66, 9])



if __name__ == '__main__':
    unittest.main()