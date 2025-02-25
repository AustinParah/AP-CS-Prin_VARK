# student code here
def findOdds(numbers):
    temp = []
    for num in numbers:
        if(num % 2 == 1):
            temp.append(num)
    return temp

# main code (no change below this line)
numbers = []
data = input("Enter a series of numbers: ")
splits = data.split(" ")
for split in splits:
    numbers.append(int(split))
    
odds = findOdds(numbers)
print("Odd Numbers:",odds)
print("That was easy!")


