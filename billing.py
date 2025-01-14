
bill = int(input("How much is the bill? ")) * 1.0
tip = int(input("What percentage do you want to tip? "))

percent = tip/100.0

tipCalc = bill + percent
total = tipCalc * bill


print("Your tip should be:", tipCalc)
print("Your total will be:", total)

