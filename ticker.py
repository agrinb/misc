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
        self.cik = None

    def init_input(self):
        print "Please input a ticker or CIK#:"
        inp = raw_input()
        return inp

    #test whether interger(CIK) or ticker
    def set_input(self, inp):
        try: 
            #testing first chr because CIK start with 000
            if isinstance(((int(inp[0]))), int) and len(inp) == 10: 
                self.cik = inp
                return self.cik
        except ValueError:
            print "{} is a Ticker".format(inp) 
            return self.get_cik_num(inp)
        
    def get_cik_num(self, inp): 
        self.set_ticker_attr(inp)
        self.page_with_cik(self.cik_url_prop)
           
    def set_ticker_attr(self, inp):
        while len(inp) >= 6 or len(inp) <= 3 :
            print "Sorry it does not appear you entered a valid ticker, please try again:"
            inp = raw_input()
        self.ticker = inp
        return self.ticker

    def get_dom(self, link):
        page = urllib2.urlopen(link.format(self.ticker)).read()
        soup = BeautifulSoup(page)
        return soup

    def get_cik(self, link):
      num = re.findall(r'(?<=action=getcompany&CIK=).*?(?=&)', link)
      self.cik = num[0]
      return self.cik 
  
    def find_in_string(self, link):
        match = re.search(r'action=getcompany&CIK=', link)
        try: 
           if match.group(0) is not None:
              return True
        except: AttributeError
        else: 
            return False

    def page_with_cik(self, link):
        dom = self.get_dom(link)
        a_nodes = dom.find_all('a')
        for a in a_nodes:
            href = a.get('href')
            if self.find_in_string(href):
                return self.get_cik(href)

    def get_report_dom(self):
        f13_link = self.f13_url_prop.format(self.cik)
        reports_dom = self.get_dom(f13_link)
        return reports_dom

    def get_report_path(self, dom):
        if not dom.select(".tableFile2")[0].find_all('td'):
            print "{} does not have a 13F-HR report asscociated with it".format(self.ticker)
            raise SystemExit
        else: 
            cells = dom.select(".tableFile2")[0].find_all('td')
            the_cell = None
            for cell in reversed(cells):
                if cell.string == '13F-HR':
                    the_cell = cell
            href = the_cell.find_next().find('a')['href']
            report_url = self.sec_url + href
            return report_url
    
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
        return file_url
     
    def get_file_text(self, link):
        page = urllib2.urlopen(link).read().replace('\n', '')
        data = re.findall ('<TEXT>(.*?)</TEXT>', page, re.DOTALL)
        data_xml = BeautifulSoup(data[1], "lxml")
        return data_xml

    def to_csv(self, data):
        with open('report.csv', 'w') as csvfile:
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
            csvfile.close()
        return csvfile
    
    def read_text_file(self, link):  
        page = urllib2.urlopen(link)
        report = list(csv.reader(page , delimiter='\t'))
        for line in report:
            print line

    def ticker_flow(self): 
        inp = self.init_input()
        self.set_input(inp)
        report_dom = self.get_report_dom()
        report_url = self.get_report_path(report_dom)
        file_url = self.get_docs_path(report_url)
        data_xml = self.get_file_text(file_url)
        return self.to_csv(data_xml)









