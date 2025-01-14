

valid = True

def e():
    answer = input("Knock Knock\n")
    if(answer != "Who's there?"):
        return False
    answer = input("Beet\n")
    if(answer != "Beet who?"):
        return False
    return True

valid = e()

if(valid):
    print("Beets me!")
else:
    print("Try again")
