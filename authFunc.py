#Austin Parah
import datetime

def get_verified_integer(prmpt, min, max):
    temp = input(prmpt)
    GreaterThanMin = False
    LesserThanMax = False
    TypeConvert = False
    firstTime = True
    while((!GreaterThanMin or !LesserThanMax or !TypeConvert) or firstTime):
        firstTime = False
        if(temp < min):
            GreaterThanMin = True
        if(temp > max):
            LesserThanMax = True
        try:
           temp = int(temp)
           TypeConvert = True
        except:
        
    



# main program starts here
month = get_verified_integer("Please enter today's month (1-12): ",1,12)
day   = get_verified_integer("Please enter today's day (1-31): ",1,31)
year  = get_verified_integer("Please enter today's year (2000 - 2030): ",2000,2030)

# build date object and print out the day of the week
today = datetime.date(year,month,day)
print("Today is a " + today.strftime("%A"))
