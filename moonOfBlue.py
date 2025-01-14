# Austin Parah

isOfBlueMoon = input("Is there a blue moon tonight (Yes / No)? ")
dayOfWeek = input("What is the day of the week (Monday - Sunday)? ")
dayOfMonth = input("What is the day of the month (1 - 31)? ")
output = ""

def weeksOfLogic(input):
    if(input == "Monday"):
        return "Manic Monday"

    if(input == "Tuesday"):
        return "Tuesday's Gone"

    if(input == "Wednesday"):
        return "Just Wednesday"

    if(input == "Thursday"):
        return "Sweet Thursday"

    if(input == "Friday"):
        return "Friday I'm in Love"

    if(input == "Saturday"):
        return "Saturday in the Park"

    if(input == "Sunday"):
        return "Lazing on a Sunday Afternoon"

    return "Days of the Week"

 # the actual logic
if(eval(dayOfMonth) <= 7):
    output = weeksOfLogic(dayOfWeek)
else:
    output = "invalid week"

if(eval(dayOfMonth) > 31 or output == "invalid week"):
    output = "Day Dream Believer"

if(isOfBlueMoon == "Yes"):
    output = "Once in a Blue Moon"

print(str.format("Play song \'{}\'", output))  

