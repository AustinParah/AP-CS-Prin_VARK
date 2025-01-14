import random
rolls = []

# student code here
def roll():
    temp = random.randrange(1,7)
    rolls.append(temp);
    return temp

#main program code (no changes below this line)
seed = int(input("Enter random seed: "))
random.seed(seed)

roll()
roll()
roll()

print("All rolls:",rolls)

