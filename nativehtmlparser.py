#!/usr/bin/env python
"""
Python 3.x HTMLParser extension with ElementTree support.
"""

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

    url = "https://sneakernews.com/?s=air%20jordan"
    article = Article(url)
    article.download()    
    parser = NaiveHTMLParser()
    root = parser.feed(article.html)
    parser.close()

    # root is an xml.etree.Element and supports the ElementTree API
    # (e.g. you may use its limited support for XPath expressions)

    # get title
    print(root.find('head/title'))

    # get all anchors
    for a in root.findall("div", {"class": "post-content"}):
        print(a.get('href'))
    ancList = [] 
    for a in root.findall(".//a"):
    	if(a.get('href').find("2018")!=-1):
    		ancList.append(a.get('href'))

    for anc in ancList:
    	print(anc)

    # for more information, see:
    # http://docs.python.org/2/library/xml.etree.elementtree.html
    # http://docs.python.org/2/library/xml.etree.elementtree.html#xpath-support

    html = urlopen(url).read()
    soup = BeautifulSoup(html,"lxml")
    
    mydivs = soup.findAll("div", {"class": "post-content"})

    '''
    for div in mydivs:
    	anchors = div.findall(".//a")
    	for anc in anchors:
    		print(anc.get('href'))

   ''' 
