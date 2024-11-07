from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen


def testParser(url):
    content = urlopen(url).read().decode()
    parser = PrettyParser()
    parser.feed(content)

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
