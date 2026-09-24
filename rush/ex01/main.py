#!/usr/bin/env python3

import sys
from checkmate import checkmate

def main():
    if len(sys.argv) < 2:
        print("Error")
        return
    
    for file_path in sys.argv[1:]:
        try:
            with open(file_path, 'r') as f:
                board = f.read()
                checkmate(board)
        except (FileNotFoundError, IOError):
            print("Error")

if __name__ == "__main__":
    main()