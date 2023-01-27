import os

def getTree(dir):
    for start, dirs, files in os.walk(dir):
        print('{}{}/'.format(' ' * 4 * (start.replace(dir, '').count(os.sep)), os.path.basename(start)))
        for f in files:
            print('{}{}'.format(' ' * 4 * (start.replace(dir, '').count(os.sep) + 1), f))

getTree("filtered")