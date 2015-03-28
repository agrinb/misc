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
        inp = 'PRGFX' #raw_input() 
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
        return soup

    def get_cik(self, link):
      num = re.findall(r'(?<=action=getcompany&CIK=).*?(?=&)', link)
      return num

    def find_in_string(self, link):
        word = '?action=getcompany&CIK='
        match = re.search(r'action=getcompany&CIK=', link)
        try: 
           if match.group(0) is not None:
              return True
        except: AttributeError
        else: 
            return False

    def check_a_nodes(self):
        dom = self.get_dom()
        a_nodes = dom.find_all('a')
        for a in a_nodes:
            href = a.get('href')
            if self.find_in_string(href):
                return self.get_cik(href)



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





