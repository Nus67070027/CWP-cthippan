import sys

if len(sys.argv) != 2:
    print("none")
else:
    param = sys.argv[1]
    text = input() 
    if param == text:
        print("Good job!")
    else:
        print("Nope, sorry...")