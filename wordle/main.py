import words
import art

language = "undefined"
length = 1
isRunning = True

art.StartText()

def askPlaying():
    if(input("Keep Playing TERMINAL WORDLE? (Y/n)\n  [$] ").lower() == "y"):
        return True
    return False

def checkValidLang(lan):
    if(lan == "en" or
       lan == "es" or
       lan == "fr" or
       lan == "it" or
       lan == "de" or
       lan == "zh"):
        return False
    return True

def checkValidLength(l):
    l = str(l)
    if(not l.isnumeric()):
        return True
    if(int(l) < 2 or int(l) > 15):
        return True
    return False

# startup
while(checkValidLang(language.lower())):
    language = input("Enter language (en, es, fr, it, de, zh)\n  [$] ")

    #lang logic
    if(language.lower() != "en"):
        words.params.update({"lang": language.lower()})

while(checkValidLength(length)):
    length = input("Enter length of word (2 - 15)\n  [$] ")
    if(not checkValidLength(length)):
        words.params.update({"length": str(length)})

# now time for the actual game

while(isRunning):
    word = words.getWord()
    
    guess = input("Please make a guess\n  [$] ")
    art.printWord(guess, [art.RED, art.RED, art.RED, art.RED])
    isRunning = askPlaying()


