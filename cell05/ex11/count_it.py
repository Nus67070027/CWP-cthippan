#!/usr/bin/env python3

import sys; a=sys.argv[1:]
print(f"parameters: {len(a)}\n" + "\n".join(f"{s}: {len(s)}" for s in a) if a else "none")