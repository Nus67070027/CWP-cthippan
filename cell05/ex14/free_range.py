#!/usr/bin/env python3
import sys

try: a, b = map(int, sys.argv[1:3]); print(list(range(a, b + 1)))
except: print("none")