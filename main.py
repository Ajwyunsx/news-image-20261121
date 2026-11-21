#!/usr/bin/env python3
"""Copy the finished front page to /output/entry.png.

Deterministic and stdlib-only: same input bytes in, same output bytes out,
no timestamps, no compression changes.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUT_DIR = "/output"
TARGET = os.path.join(OUT_DIR, "entry.png")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    size = os.path.getsize(TARGET)
    print(f"wrote {TARGET} ({size} bytes)")


if __name__ == "__main__":
    main()
