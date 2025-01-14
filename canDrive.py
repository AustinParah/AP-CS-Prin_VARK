age = int(input("How old are you? "))
hasLicense = input("Do you have your license? ")

# student code here
if(age >= 16 and hasLicense == "yes"):
    print("You can drive")
elif(age >= 16):
    print("You need to get a license.")
else:
    print("You can't drive")
