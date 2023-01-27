import random
import string

def randomFilename(length, ext):
    alpha = string.ascii_letters
    res = ""
    for i in range (length):
        res = res + random.choice(alpha)
    res = res + "." + ext
    return res

for _ in range (10):
    print(randomFilename(10, "png"))