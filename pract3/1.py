import random
import argparse

def encrypt(unfiltered_text, alphabet, key):
    numAlpha = dict()
    for i in range(len(alphabet)):
        numAlpha[i] = alphabet[i]
    alphaNum = dict()
    for i in range(len(alphabet)):
        alphaNum[alphabet[i]] = i
    text = ""
    for i in unfiltered_text:
        if i in alphabet:
            text += i
    text.upper()
    random.seed(key)
    randlist = []
    for _ in range(len(text)):
        randlist.append(random.randrange(len(alphabet)))
    result = ""
    for i in range(len(text)):
        result += numAlpha[(alphaNum[text[i]] + randlist[i]) % len(alphabet)]
    return result

def decrypt(unfiltered_text, alphabet, key):
    numAlpha = dict()
    for i in range(len(alphabet)):
        numAlpha[i] = alphabet[i]
    alphaNum = dict()
    for i in range(len(alphabet)):
        alphaNum[alphabet[i]] = i
    text = ""
    for i in unfiltered_text:
        if i in alphabet:
            text += i
    text.upper()
    random.seed(key)
    randlist = []
    for _ in range(len(text)):
        randlist.append(random.randrange(len(alphabet)))
    result = ""
    for i in range(len(text)):
        result += numAlpha[(alphaNum[text[i]] - randlist[i] + 33) % len(alphabet)]
    return result

parser = argparse.ArgumentParser(prog = '1.py', description = 'Encrypt or decrypt string by polyalphabetic cipher')
parser.add_argument('-m', '--mode', required=True, type=str, choices=['encrypt', 'decrypt'], help='encrypt or decrypt')
parser.add_argument('-t', '--text', required=True, type=str, help='string to encrypt or decrypt')
parser.add_argument('-a', '--alpha', type=str, default="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ", help='alphabet to use')
parser.add_argument('-k', '--key', required=True, type=str, help='key to use')
args = parser.parse_args()

match args.mode:
    case 'encrypt':
        print(encrypt(args.text, args.alpha, args.key))
    case 'decrypt':
        print(decrypt(args.text, args.alpha, args.key))