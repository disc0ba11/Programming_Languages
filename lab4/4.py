from pathlib import Path

def getExt(dir, ext):
    return [str(i) for i in Path(dir).resolve().rglob(ext)]

print(getExt("filtered", "*.png"))