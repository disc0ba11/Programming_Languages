import http.client
from html.parser import HTMLParser

def connect(url, page):
    conn = http.client.HTTPSConnection(url)
    conn.request('GET', f'https://{url}/{page}', headers = {'Host': 'disc0ba11', 'User-agent': 'Python program'})
    return conn.getresponse().read().decode()

def download(url, page, filename, ext):
    conn = http.client.HTTPSConnection(url)
    conn.request('GET', f'https://{url}/{page}{filename}.{ext}', headers = {'Host': 'disc0ba11', 'User-agent': 'Python program'})
    open(f"{filename}.{ext}", "wb").write(conn.getresponse().read())

def crawl(url, page):
    parser = MyParser()
    parser.feed(connect(url, page))
    hrefs = parser.hrefs
    return hrefs

class MyParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for attr in attrs:
                if attr[0] == 'src':
                    download('beda.pnzgu.ru', 'anatoly/', attr[1].split('.')[0], attr[1].split('.')[1])
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    self.hrefs.append(attr[1])

for i in crawl('beda.pnzgu.ru', 'anatoly/'):
    crawl('beda.pnzgu.ru', f'anatoly/{i}')