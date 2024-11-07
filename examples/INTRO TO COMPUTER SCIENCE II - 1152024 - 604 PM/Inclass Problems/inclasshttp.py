from urllib.request import urlopen
from html.parser import HTMLParser

response = urlopen('http://www.google.com')
class MyHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            print('Found a tag!')
    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)
    def handle_data(self, data):
        print("Encountered some data  :", data)

def testParser(url):
    html = urlopen('http://facweb.cdm.depaul.edu/azoko/csc242').read().decode()
    parser = LinkParser()
    parser.feed(html)

testParser('http://facweb.cdm.depaul.edu/azoko/csc242')