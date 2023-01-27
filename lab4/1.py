import shutil
from pathlib import Path

def unpack(file, unpack_dir="masterclass", copy_dir="filtered", mask=None):
    Path(unpack_dir).mkdir()
    shutil.unpack_archive(file, unpack_dir)
    if mask:
        shutil.copytree(unpack_dir, copy_dir, ignore=shutil.ignore_patterns(mask))
    else:
        shutil.copytree(unpack_dir, copy_dir)
    shutil.make_archive(unpack_dir, "gztar", copy_dir)

unpack("masterclass.tar", mask="*.exe")