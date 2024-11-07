from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen

def testParser(url):
    content = urlopen(url).read().decode()
    parser = DataCollector()
    parser.feed(content)
    return parser.getData()

class DataCollector(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.text = ""
    def handle_data(self, data):
        self.text += data
    def getData(self):
        return self.text

class NodeParser(HTMLParser):
    def handle_data(self, data):
        print(data)

class LinkParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    print(attr[1])

class AltPrettyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.indent = 0

    def handle_starttag(self, tag, attrs):
        if tag not in {'br', 'hr', 'img'}:
            print('{}{} start'.format(self.indent*' ', tag))
            self.indent += 4
        else:
            print('{}{} start'.format(self.indent*' ', tag))

    def handle_endtag(self, tag):
        self.indent -= 4
        print('{}{} end'.format(self.indent*' ', tag))

class PrettyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.indent = 0

    def handle_starttag(self, tag, attrs):
        if tag not in {'br', 'p'}:
            print('{}{} start'.format(self.indent*' ', tag))
            self.indent += 4

    def handle_endtag(self, tag):
        if tag not in {'p'}:
            self.indent -= 4
            print('{}{} end'.format(self.indent*' ', tag))

class Collector(HTMLParser):
    def __init__(self, url):
        HTMLParser.__init__(self)
        self.url = url
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:4] == 'http':
                        self.links.append(absolute)

    def getLinks(self):
        return self.links
