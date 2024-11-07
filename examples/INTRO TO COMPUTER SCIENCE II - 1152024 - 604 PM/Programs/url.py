from urllib.request import urlopen

def getHTML(url):
    file = urlopen(url)
    b = file.read()
    html = b.decode()
    return html
