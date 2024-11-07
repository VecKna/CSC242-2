from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen


def testParser(url):
    content = urlopen(url).read().decode()
    parser = PParser()
    parser.feed(content)
    print(parser.getFinalData())

class PParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.text=''
        self.foundPTag=False

    def getFinalData(self):
        return self.text
        
    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.foundPTag=True
            
    def handle_data(self,data):
        if self.foundPTag==True:
            self.text = self.text+data

    def handle_endtag(self, tag):
        if tag == 'p':
            self.foundPTag=False
