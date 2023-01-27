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
        self.res = []
        random.setstate(self.state)
        for _ in range (1, self.amount):
            rand = random.randrange(1, self.base + 1)
            self.state = random.getstate()
            self.res.append(rand)
        return self.res

print(Cube("10d20").dice(), Cube("10d20").dice())
print(Cube("20d20", seed="какой-то сид").dice(), Cube("20d20", seed="какой-то сид").dice())