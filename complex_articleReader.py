#!/usr/bin/env python
"""
Python 3.x HTMLParser extension with ElementTree support.
"""
import sys
import requests
from html.parser import HTMLParser
from xml.etree import ElementTree
from bs4 import BeautifulSoup
from urllib.request import urlopen
from newspaper import Article

class NaiveHTMLParser(HTMLParser):
    """
    Python 3.x HTMLParser extension with ElementTree support.
    @see https://github.com/marmelo/python-htmlparser
    """

    def __init__(self):
        self.root = None
        self.tree = []
        HTMLParser.__init__(self)

    def feed(self, data):
        HTMLParser.feed(self, data)
        return self.root

    def handle_starttag(self, tag, attrs):
        if len(self.tree) == 0:
            element = ElementTree.Element(tag, dict(self.__filter_attrs(attrs)))
            self.tree.append(element)
            self.root = element
        else:
            element = ElementTree.SubElement(self.tree[-1], tag, dict(self.__filter_attrs(attrs)))
            self.tree.append(element)

    def handle_endtag(self, tag):
        self.tree.pop()

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)
        pass

    def handle_data(self, data):
        if self.tree:
            self.tree[-1].text = data

    def get_root_element(self):
        return self.root

    def __filter_attrs(self, attrs):
        return filter(lambda x: x[0] and x[1], attrs) if attrs else []


if __name__ == "__main__":
	 
    keyword = sys.argv[1]
    print(sys.argv)
    url = "http://www.complex.com/search?q="+keyword
    print(url)
    article = Article(url)
    article.download()    
    parser = NaiveHTMLParser()
    root = parser.feed(article.html)
    parser.close()

    # root is an xml.etree.Element and supports the ElementTree API
    # (e.g. you may use its limited support for XPath expressions)

    # get all anchors
    #for a in root.findall("div"):
    #    print(a.get('href'))
    ancList = [] 
    for a in root.findall(".//a"):
    	#print(ElementTree.tostring(a, encoding='utf8', method='xml'))
    	if(a.get('href') is not None and  a.get('href').find("2018")!=-1):
    		ancList.append(a.get('href'))

    for anc in ancList:
    	print(anc)
    
    #soup = BeautifulSoup(html,"lxml")
    
    #mydivs = soup.findAll("div", {"class": "post-content"})

    for anc in ancList:
    	resp = requests.get(anc)
    	if (requests.get(anc).status_code>=300):
    		anc = resp.url
    	article = Article(anc)
    	article.download()
    	article.parse()
    	print('Publish Date : '+article.publish_date.strftime("%Y-%m-%d %H:%M:%S"))
    	print('Content : '+ str(article.text).encode('ascii','ignore').decode('ascii','ignore'))
    	article.nlp()
    	print('Keywords : '+ ', '.join(article.keywords)) 
    	print('######################################################## \n \n')  

