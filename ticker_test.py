from ticker import Ticker
import unittest
import pdb 



class TickerTest(unittest.TestCase):

    def setUp(self):
        self.tk = Ticker()
            
    def test_init(self):  
        tk = Ticker()
        self.assertIsInstance(tk, Ticker)

    # def test_setter(self):
    #     inp = 'PRGFX'
    #     self.tk.ticker = inp
    #     self.assertEquals(self.tk.ticker, 'PRGFX')

    # def test_check_input(self):
    #     inp = 'PRGFX'
    #     self.assertEquals(self.tk.set_ticker_attr(inp), 'PRGFX')

    # def test_get_dom(self):
    #     self.assertEquals(self.tk.get_dom(), 'PRGFX')

    # def test_matching(self):
    #     self.assertEquals(self.tk.match(), 000116655 )

    def test_find_in_string(self):
        self.assertEquals(self.tk.find_in_string(), True )




if __name__ == '__main__':
    unittest.main()