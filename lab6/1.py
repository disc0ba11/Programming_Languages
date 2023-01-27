import random
import string
import argparse

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

parser = argparse.ArgumentParser(prog = 'Password generator', description = 'Generate passwords')
parser.add_argument('-c', '--count', type=int, default=1, help='number of passwords to generate')
parser.add_argument('-l', '--length', type=int, default=10, help='length of each password')
parser.add_argument('-b', '--bundle', type=str, choices=['digits', 'uppers', 'lowers', 'uppers-lowers-digits', 'uppers-lowers', 'uppers-digits', 'lowers-digits'], default='uppers-lowers-digits', help='symbols to use')
args = parser.parse_args()

match args.bundle:
    case 'digits':
        bundles = [string.digits]
    case 'uppers':
        bundles = [string.ascii_uppercase]
    case 'lowers':
        bundles = [string.ascii_lowercase]
    case 'uppers-lowers-digits':
        bundles = [string.ascii_lowercase, string.ascii_uppercase, string.digits]
    case 'uppers-lowers':
        bundles = [string.ascii_lowercase, string.ascii_uppercase]
    case 'uppers-digits':
        bundles = [string.ascii_uppercase, string.digits]
    case 'lowers-digits':
        bundles = [string.ascii_lowercase, string.digits]
for _ in range (args.count):
    print(Password(bundles).gen(args.length))