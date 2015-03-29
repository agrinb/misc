from ticker import Ticker
import unittest
import pdb 



class TickerTest(unittest.TestCase):

    def setUp(self):
        self.tk = Ticker()
        self.tk.cik_url_prop = 'http://www.sec.gov/cgi-bin/browse-edgar?CIK={}&Find=Search&owner=exclude&action=getcompany'
        self.tk.f13_url_prop = 'http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={}&type=13F-HR&dateb=&count=40&scd=filings'

            
    # def test_init(self):  
    #     tk = Ticker()
    #     self.assertIsInstance(tk, Ticker)

    def test_setter(self):
        inp = 'PRGFX'
        self.tk.ticker = inp
        self.assertEquals(self.tk.init_input(), 'PRGFX')

    # def test_check_input(self):
    #     inp = 'PRGFX'
    #     self.assertEquals(self.tk.set_ticker_attr(inp), 'PRGFX')

    # def test_get_dom(self):
    #     self.assertEquals(self.tk.get_dom(), 'PRGFX')

    # def test_matching(self):
    #     self.assertEquals(self.tk.match(), 000116655 )

    # def test_find_in_string(self):
    #     self.assertEquals(self.tk.find_in_string(), True )

    # def cik_url_prop_test(self):
    #     self.tk.ticker = 'PRGFX'
    #     self.assertEquals(self.tk.a_nodes_to_cik(self.tk.cik_url_prop)[0], '0000080257' )

    # def test_report_dom(self):
    #     self.tk.cik = '0001166559'
    #     # self.tk.set_ticker_attr(self.tk.ticker)
    #     #self.assertEquals(self.tk.get_report_dom(self.tk.f13_url_prop))
    #     link = "http://www.sec.gov/cgi-bin/browse-edgar?CIK=0001166559&Find=Search&owner=exclude&action=getcompany"
    #     self.assertEquals(self.tk.get_report_dom(link))






if __name__ == '__main__':
    unittest.main()