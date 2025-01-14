livesNum = int(input("How many lives do you have left in the game? "))
print("You have", livesNum, "lives left.")

# student code here
def e(livesNum):
    if(livesNum <= 0):
        return "Game over."
    elif(livesNum <= 3):
        return "You should be careful."
    return "You should keep playing."

print(e(livesNum))
