import http.client
from html.parser import HTMLParser

def connect(url, page):
    conn = http.client.HTTPSConnection(url)
    conn.request('GET', f'https://{url}/{page}', headers = {'Host': 'disc0ba11', 'User-agent': 'Python program'})
    return conn.getresponse().read().decode()

def download(url, page, filename, ext):
    conn = http.client.HTTPSConnection(url)
    conn.request('GET', f'https://{url}/{page}/{filename}.{ext}', headers = {'Host': 'disc0ba11', 'User-agent': 'Python program'})
    open(f"{filename}.{ext}", "wb").write(conn.getresponse().read())

class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for attr in attrs:
                if attr[0] == 'src':
                    download('beda.pnzgu.ru', 'anatoly', attr[1].split('.')[0], attr[1].split('.')[1])

parser = MyParser()
parser.feed(connect('beda.pnzgu.ru', 'anatoly/'))