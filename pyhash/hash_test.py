
from hash_me import Hash_me
import unittest
import pdb


class HashMeTest(unittest.TestCase):

    #I focussed on the functionality of the Class rather than
    #syntax, I did not create a hash literal method.
    
    #ha is an instance of Hash_me
    def test_init(self):
        ha = Hash_me(5,6)
        ha2 = Hash_me('string', 1)
        ha3 = Hash_me('string1', "string2")
        self.assertIsInstance(ha, Hash_me)
        self.assertIsInstance(ha2, Hash_me)
        self.assertIsInstance(ha3, Hash_me)

    #instantiating a Hash with more that two 
    def test_init_mult(self):
        ha2 = Hash_me(5,6,7,8,1,2,3,4,11,12,13,14,15,16,17,18)
        self.assertEquals(ha2.get(5), 6)
        self.assertEquals(ha2.get(11), 12)
        self.assertEquals(ha2.get(17), 18)


    def test_init_with_strings(self):
        string1 = 'string1'
        string2 = 'string2'
        ha = Hash_me('string1', 'string2')
        self.assertEquals(ha.get('string1'), 'string2')
    
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