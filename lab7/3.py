import http.client

conn = http.client.HTTPSConnection("beda.pnzgu.ru")
conn.request('GET', 'https://beda.pnzgu.ru/anatoly/', headers = {'Host': 'disc0ba11', 'User-agent': 'Python program'})
print(conn.getresponse().read().decode())