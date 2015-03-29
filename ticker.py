import pdb
from bs4 import BeautifulSoup
import requests
import pprint
import urllib2
import re
import xmltodict
import csv
import sys





class Ticker(object):
    def __init__(self):
        self.ticker = ''
        self.cik_url_prop = "http://www.sec.gov/cgi-bin/browse-edgar?CIK={}&Find=Search&owner=exclude&action=getcompany"
        self.f13_url_prop = "http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={}&type=13F-HR&dateb=&count=40&scd=filings"
        self.sec_url = 'http://www.sec.gov/'
        self.company = 'Temp'
        self.cik = None



    # def get_ticker(self):
    #     return self.__ticker

    # def set_ticker(self, value):
    #     self.__ticker = value

    def init_input(self):
        print "Please input a ticker or CIK#:"
        inp = raw_input()
        try: 
            if isinstance(((int(inp[0]))), int) and len(inp) == 10:
                self.cik = inp
                return self.get_report_dom(self.cik_url_prop)
        except ValueError:
            print "{} is a Ticker".format(inp) 
        else:
            print '2'
            self.set_ticker_attr(inp)
            self.a_nodes_to_cik(self.cik_url_prop)
    
    def set_ticker_attr(self, inp):
        while len(inp) >= 6 or len(inp) <= 3 :
            print "Sorry it does not appear you entered a valid ticker, please try again:"
            inp = raw_input()
        self.ticker = inp


    def get_dom(self, link):
        page = urllib2.urlopen(link.format(self.ticker)).read()
        soup = BeautifulSoup(page)
        return soup

    def get_cik(self, link):
      num = re.findall(r'(?<=action=getcompany&CIK=).*?(?=&)', link)
      self.cik = num[0]
  

    def find_in_string(self, link):
        word = '?action=getcompany&CIK='
        match = re.search(r'action=getcompany&CIK=', link)
        try: 
           if match.group(0) is not None:
              return True
        except: AttributeError
        else: 
            return False

    def a_nodes_to_cik(self, link):
        dom = self.get_dom(link)
        a_nodes = dom.find_all('a')
        for a in a_nodes:
            href = a.get('href')
            if self.find_in_string(href):
                self.get_cik(href)
                self.get_report_dom(self.cik_url_prop)


    def get_report_dom(self, link):
        # #####
        # temp = "http://www.sec.gov/cgi-bin/browse-edgar?CIK=0001166559&Find=Search&owner=exclude&action=getcompany"
        # #####
        # cik = self.a_nodes_to_cik(self.cik_url_prop)
      
        f13_link = self.f13_url_prop.format(self.cik)
        reports_dom = self.get_dom(f13_link)
        self.get_report_path(reports_dom)

    def get_report_path(self, dom):
        # pdb.set_trace()
        cells = dom.select(".tableFile2")[0].find_all('td')
        the_cell = None
        for cell in reversed(cells):
            if cell.string == '13F-HR':
                the_cell = cell
        href = the_cell.find_next().find('a')['href']
        report_url = self.sec_url + href
        self.get_docs_path(report_url)


    def get_docs_path(self, link):
        dom = self.get_dom(link)
        cells = dom.select(".tableFile")[0].find_all('td')
        the_cell = None
        for cell in cells:
            try:
                if 'Complete submission' in cell.string: #find the row with file
                    the_cell = cell
            except: TypeError
        href = the_cell.find_next().find('a')['href']
        file_url = self.sec_url + href
        self.get_file_text(file_url)

    def get_file_text(self, link):
        page = urllib2.urlopen(link).read().replace('\n', '')
        data = re.findall ('<TEXT>(.*?)</TEXT>', page, re.DOTALL)
        data_xml = BeautifulSoup(data[1], "lxml")
        self.to_csv(data_xml)

    def to_csv(self, data):
        with open('{}.csv'.format(self.company), 'w') as csvfile:
            co = data.find('infotable')
            fieldnames = []
            for child in co.children:
                if hasattr(child, 'tag'):
                     fieldnames.append(child.name)             
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            cos = data.find_all('infotable')
            for co in cos:
                row = {}
                for child in co.children:
                    if hasattr(child, 'tag'):
                         string = unicode(child.string)
                         row['{}'.format(child.name)] = string 
                writer.writerow(row) 
                print '1'       
            csvfile.close()


    
    def read_text_file(self, link):  
        page = urllib2.urlopen(link)
        report = list(csv.reader(page , delimiter='\t'))
        for line in report:
            print line
        # with open(page) as tsv:

          




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










