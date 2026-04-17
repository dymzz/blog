#!/usr/bin/env python

import os
import sys


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "build"

    if cmd == "build":
        os.system("pelican content -s pelicanconf.py")
    elif cmd == "preview":
        os.system("pelican content -s pelicanconf.py")
        os.system("pelican --listen")
    elif cmd == "publish":
        os.system("pelican content -s publishconf.py")
    elif cmd == "dev":
        os.system("pelican --autoreload --listen")
    else:
        print(f"未知命令: {cmd}")
        print("可用命令: build, preview, publish, dev")


if __name__ == "__main__":
    main()
