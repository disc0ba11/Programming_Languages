import random

class Cube:
    def __init__(self, cube, *, seed=None):
        random.seed(seed)
        self.state = random.getstate()
        self.base = int(cube.split("d")[1])
        if cube.split("d")[0] != "":
            self.amount = int(cube.split("d")[0])
        else:
            self.amount = ""
    def dice(self):
        if self.amount != "":
            self.res = []
            random.setstate(self.state)
            for _ in range (0, self.amount):
                rand = random.randrange(1, self.base + 1)
                self.state = random.getstate()
                self.res.append(rand)
            return self.res
        else:
            random.setstate(self.state)
            rand = random.randrange(1, self.base+1)
            self.state = random.getstate()
            return rand

res = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
for _ in range (0, 100001):
    res[str(Cube("d6").dice() + Cube("d6").dice())] = res[str(Cube("d6").dice() + Cube("d6").dice())] + 1
for i in res:
    res[i] = res[str(i)] / 100001
    print(i, res[i])