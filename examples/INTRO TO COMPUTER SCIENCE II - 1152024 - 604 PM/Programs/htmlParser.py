from html.parser import HTMLParser
from urllib.request import urlopen

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a {} start tag".format(tag))
    def handle_endtag(self, tag):
        print("Encountered a {} end tag".format(tag))

def testParser(url):
    content = urlopen(url).read().decode()
    parser = MyHTMLParser()
    parser.feed(content)
