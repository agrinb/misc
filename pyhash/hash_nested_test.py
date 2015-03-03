from hash_nested import nested
import unittest


class HashNestedTest(unittest.TestCase):

    def setUp(self):
        self.arr = ['a', 'b', 'c']
        self.arr2 = ['a', 'b', 'f']
        self.arr3 = ['a', 'r', 'f']
        self.arr4 = ['a','z']
        self.dct = {}


    def test_nested(self):
        nes = nested(self.dct, self.arr)
        self.assertEquals(nes, {'a': {'b': {'c': 1}}})

    def test_nested2(self):
        nes = nested(self.dct, self.arr)
        self.arr = ['a', 'b', 'c']
        nes = nested(self.dct, self.arr)
        self.assertEquals(nes, {'a': {'b': {'c': 2}}})


    def test_nested3(self):
        nes = nested(self.dct, self.arr)
        self.arr = ['a', 'b', 'c']
        nes = nested(self.dct, self.arr)
        nes = nested(self.dct, self.arr2)
        self.assertEquals(nes, {'a': {'b': {'c': 2, 'f': 1}}})


    def test_nested4(self):
        nes = nested(self.dct, self.arr)
        self.arr = ['a', 'b', 'c']
        nes = nested(self.dct, self.arr)
        nes = nested(self.dct, self.arr2)
        nes = nested(self.dct, self.arr3)
        self.assertEquals(nes, {'a': {'r': {'f': 1}, 'b': {'c': 2, 'f': 1}}})

    def test_nested5(self):
        nes = nested(self.dct, self.arr)
        self.arr = ['a', 'b', 'c']
        nes = nested(self.dct, self.arr)
        nes = nested(self.dct, self.arr2)
        nes = nested(self.dct, self.arr3)
        nes = nested(self.dct, self.arr4)
        self.assertEquals(nes, {'a': {'r': {'f': 1}, 'b': {'c': 2,'f': 1}, 'z': 1}})





if __name__ == '__main__':
    unittest.main()