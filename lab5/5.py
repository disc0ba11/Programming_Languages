import random
import string

class Password:
    def __init__(self, bundles=[]):
        self.tmp = ""
        self.bundles = bundles
    def gen(self, length):
        for i in self.bundles:
            self.tmp += random.choice(i)
        for _ in range (0, length - len(self.bundles)):
            self.tmp += random.choice(random.choice(self.bundles))
        res = list(self.tmp)
        random.shuffle(res)
        return ''.join(res)

bundles = [string.ascii_lowercase, string.ascii_uppercase, string.digits]
for _ in range (10):
    print(Password(bundles).gen(30))