from ticker import Ticker
import unittest
import pdb 
import csv



class TickerTest(unittest.TestCase):

    def setUp(self):
        self.tk = Ticker()
        self.tk.cik_url_prop = 'http://www.sec.gov/cgi-bin/browse-edgar?CIK={}&Find=Search&owner=exclude&action=getcompany'
        self.tk.f13_url_prop = 'http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={}&type=13F-HR&dateb=&count=40&scd=filings'
        
    def test_init(self):  
        tk = Ticker()
        self.assertIsInstance(tk, Ticker)
    # given a CIK, sets self.cik
    def test_set_input(self):
        inp = '0001166559'
        self.tk.set_input(inp)
        self.assertEquals(self.tk.cik, '0001166559')
    #given a ticker, CIK is not set
    def test_set_input_w_ticker(self):
        inp = 'PRGFX'
        self.tk.set_input(inp)
        self.assertEquals(self.tk.cik, '0000080257')
    #given a ticker, ticker is set
    def test_set_ticker_attr(self):
        inp = 'PRGFX'
        self.tk.set_ticker_attr(inp)
        self.assertEquals(self.tk.ticker, 'PRGFX')
    #given a link, CIK is extracted and set
    def test_get_cik(self):
        link =  'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001177017&owner=exclude&count=40'
        self.tk.get_cik(link)
        self.assertEquals(self.tk.cik, '0001177017')

    def test_find_in_string(self):
        link =  'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001177017&owner=exclude&count=40'
        self.tk.find_in_string(link)
        self.assertEquals(self.tk.find_in_string(link), True)

    def test_page_with_cik(self):
        link =  'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001177017&owner=exclude&count=40'
        self.assertEquals(self.tk.page_with_cik(link), '0001177017')
    #turn BeautifulSoup into a string and test for HTML 
    def test_get_dom(self):
        link =  'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001177017&owner=exclude&count=40'
        self.assertEquals(unicode(self.tk.get_dom(link))[:9], '<!DOCTYPE')

    def test_get_report_dom(self):
       self.assertEquals(unicode(self.tk.get_report_dom())[:9], '<!DOCTYPE')

    def test_get_report_path(self):
        link =  'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001166559&owner=exclude&count=40'
        self.tk.get_cik(link)
        dom = self.tk.get_dom(link)
        self.tk.cik = '0001166559'
        rdom = self.tk.get_report_dom()
        self.assertEquals(self.tk.get_report_path(rdom), 'http://www.sec.gov//Archives/edgar/data/1166559/000110465915010462/0001104659-15-010462-index.htm')

    def test_get_docs_path(self):
        link = 'http://www.sec.gov//Archives/edgar/data/1166559/000110465915010462/0001104659-15-010462-index.htm'
        self.assertEquals(self.tk.get_docs_path(link), 'http://www.sec.gov//Archives/edgar/data/1166559/000110465915010462/0001104659-15-010462.txt')

    def get_file_text(self):
        link = 'http://www.sec.gov//Archives/edgar/data/1166559/000110465915010462/0001104659-15-010462.txt'
        self.assertEquals(unicode(self.tk.get_file_text(link))[:5], '<XML>')

    def test_to_csv(self):
        link = 'http://www.sec.gov//Archives/edgar/data/1166559/000110465915010462/0001104659-15-010462.txt'
        data = self.tk.get_file_text(link)
        csv_file = self.tk.to_csv(data) 
        is_csv = None
        with open('report.csv', 'rb') as csv_file:
            try:
                dialect = csv.Sniffer().sniff(csv_file.read(1024))
                csv_file.seek(0)
                is_csv = True
            except: csv.Error
            reader = csv.reader(csv_file, delimiter=',')
            headers = reader.next()
        self.assertEquals(is_csv, True)
        self.assertEquals(headers[0], 'nameofissuer')
        csv_file.close()




if __name__ == '__main__':
    unittest.main()