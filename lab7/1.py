import socketserver

class MyTCPHandler(socketserver.StreamRequestHandler):
    def handle(self):
        self.db = {'Асаян': 'Аркадий', 'Борисов': 'Дмитрий',
                    'Быстров': 'Александр', 'Васильев': 'Даниил',
                    'Водолазов': 'Даниил', 'Гарынов': 'Даниил',
                    'Глебов': 'Илья', 'Гусев': 'Данила',
                    'Ивин': 'Дмитрий', 'Карамышев': 'Илья',
                    'Каратаева': 'Мария', 'Кондратьев': 'Кирилл',
                    'Краснов': 'Павел', 'Кузьмин': 'Захар',
                    'Кукушкин': 'Владислав', 'Маслов': 'Сергей',
                    'Мачалихин': 'Данила', 'Нефёдова': 'Виктория',
                    'Пономарёв': 'Вадим', 'Попов': 'Максим',
                    'Родионова': 'Алина', 'Сергеева': 'Софья',
                    'Соколенко': 'Никита', 'Фейгина': 'Екатерина',
                    'Хемчян': 'Артур', 'Юлгушев': 'Рамиль',
                    'Юртаев': 'Вадим'}
        self.data = self.rfile.readline().decode().rstrip('\n')
        print(f"{self.client_address} написал: {self.data}")
        if self.data in self.db:
            print(f"{self.data} найден(-а)! Имя отправлено.")
            self.wfile.write(f"Привет, {self.db[self.data]}!\n".encode())
        else:
            print(f"{self.data} не найден(-а). Уведомление отправлено.")
            self.wfile.write(f"{self.data} не найден(-а).".encode())
with socketserver.TCPServer(('', 7777), MyTCPHandler) as server:
    server.serve_forever()