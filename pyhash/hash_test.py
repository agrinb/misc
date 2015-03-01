
from hash_me import Hash_me
import unittest
import pdb

ha = Hash_me()

class HashMeTest(unittest.TestCase):


    def test_init(self):
        ha = Hash_me()
        self.assertIsInstance(ha, Hash_me)

    def test_add(self):
        ha = Hash_me()
        ha.add(5,6)
        self.assertEquals(ha.get(5), 6)

    def test_add(self):
        ha = Hash_me()
        self.assertRaises(TypeError, ha.add, (5))
        self.assertRaises(TypeError, ha.add, (5,6,7))
        
    def test_get(self):
        ha = Hash_me()
        ha.add(8,9)
        self.assertEquals(ha.get(8), 9)

    def test_keys(self):
        ha = Hash_me()
        ha.add(8,9)
        ha2 = Hash_me()
        ha2.add(55,66)
        ha.merge(ha2)
        self.assertItemsEqual(ha.keys(),[55, 8])

    def test_values(self):
        ha = Hash_me()
        ha.add(8,9)
        ha2 = Hash_me()
        ha2.add(55,66)
        ha.merge(ha2)
        self.assertItemsEqual(ha.values(),[66, 9])


    def test_merge(self):
        ha = Hash_me()
        ha.add(8,9)
        ha2 = Hash_me()
        ha2.add(55,66)
        ha.merge(ha2)
        self.assertItemsEqual(ha.keys(),[55, 8])
        self.assertItemsEqual(ha.values(),[66, 9])




if __name__ == '__main__':
    unittest.main()