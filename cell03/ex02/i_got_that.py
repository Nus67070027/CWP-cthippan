f: bool = False

while 1:
    if not f:
        print("What you gotta say? : ", end="")
        f = True
    else:
        print("I got that! Anything else? : ", end="")
    
    if input() == "STOP":
        break