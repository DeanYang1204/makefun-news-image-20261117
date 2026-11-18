"""Entry program for make.fun news-image-20261117 (Python 3.13, stdlib only).

Copies the finished front page, entry.png, which sits beside this file,
to /output/entry.png (or $MAKEFUN_OUTPUT_DIR when set). The image is a
static asset: the program does no network access and writes identical
bytes on every run.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    if not SRC.is_file():
        print(f"entry.png not found beside main.py ({SRC})", file=sys.stderr)
        raise SystemExit(1)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    dest = OUT_DIR / "entry.png"
    shutil.copyfile(SRC, dest)
    if sha256(SRC) != sha256(dest):
        print("copied entry.png does not match the source", file=sys.stderr)
        raise SystemExit(1)
    print(f"wrote {dest} ({dest.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
