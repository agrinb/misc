import pdb
from bs4 import BeautifulSoup
import requests
import pprint
import urllib2
import re




class Ticker(object):
    def __init__(self):
        self.ticker = ''


    def get_ticker(self):
        return self.__ticker

    def set_ticker(self, value):
        self.__ticker = value

    def init_input(self):
        print "Please input a ticker:"
        inp = raw_input()
        self.set_ticker_attr(inp)

    def set_ticker_attr(self, inp):
        while len(inp) >= 6 or len(inp) <= 3 :
            print "Sorry it does not appear you entered a valid ticker, please try again:"
            inp = raw_input()
        self.ticker = inp
        return self.ticker

    def get_dom(self):
        self.init_input()
        page = urllib2.urlopen('http://www.sec.gov/cgi-bin/browse-edgar?CIK={}&Find=Search&owner=exclude&action=getcompany'.format(self.ticker)).read()
        soup = BeautifulSoup(page)
        soup.prettify()
        pdb.set_trace()
        tree = html.fromstring(page.text)

    def match(self):
      link = "http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001166559&owner=exclude&count=40"
      pdb.set_trace()
      num = re.findall(r'(?<=action=getcompany&CIK=).*?(?=&owner)', link)
      #re.findall('^def(.*?)^end',doc,re.DOTALL|re.MULTILINE)
      return num

    def find_in_string(self):
        link = "http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001166559&owner=exclude&count=40"
        word = '?action=getcompany&CIK='
        match = re.search(r'action=getcompany&CIK=', link)
        if match.group(0) is not None:
            return True

    #get a elements
    #find a link that includes 'action=getcompany&CIK'
    #parse out the number between 'action=getcompany&CIK' and '&owner'
    #check that parsed info is a number or return warning
    #request html at http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001177017&type=13F-HR&dateb=&count=40&scd=filings using the CIK 
    #look in the table element, find row with a cell that includes '13F-HR'
    #in the same row find cell with "documentsbutton" id
    #get url for 'documentsbody' id 
    #find row elem with string "Complete submission text file"
    #find link in the same row
    #parse all rows for "<nameOfIssuer>"
    #in the same element get <value>





    ticker = property(get_ticker, set_ticker)





