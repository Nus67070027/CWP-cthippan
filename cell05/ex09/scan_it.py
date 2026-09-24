#!/usr/bin/env python3
import sys

a = sys.argv; print(a[2].count(a[1]) if len(a) == 3 else "none")