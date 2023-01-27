import os

def getTree(dir):
    tree = os.walk(dir)
    res = []
    for i in tree:
        res.append(i)
    list(res)
    res = list(res[0])
    res.pop(0)
    res = tuple(res)
    return res

print(getTree("Directories"))