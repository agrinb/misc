
from hash_me import Hash_me
import unittest
import pdb




class HashMeTest(unittest.TestCase):


    def test_init(self):
        ha = Hash_me(5,6)
        self.assertIsInstance(ha, Hash_me)

    def test_add(self):
        ha = Hash_me(5,6,7,8,1,2,3,4)
        ha2 = Hash_me(5,6,7,8,1,2,3,4,11,12,13,14,15,16,17,18)
        self.assertEquals(ha.get(5), 6)
        self.assertEquals(ha2.get(7), 8)
        self.assertEquals(ha2.get(1), 2)
        self.assertEquals(ha2.get(3), 4)
        self.assertEquals(ha2.get(11), 12)
        self.assertEquals(ha2.get(13), 14)
        self.assertEquals(ha2.get(15), 16)
        self.assertEquals(ha2.get(17), 18)
      
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