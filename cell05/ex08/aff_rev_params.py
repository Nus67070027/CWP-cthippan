#!/usr/bin/env python3
import sys

args = sys.argv[1:]
print(*(args[::-1] if len(args) > 2 else ["none"]), sep="\n")