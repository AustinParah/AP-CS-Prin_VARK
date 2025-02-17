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

def getGuessColors(word, guess):
    out = []
    for i in range(0, len(word)):
        itterout = ""
        if(guess[i] in word):
            itterout = art.YELLOW
        if(guess[i] == word[i]):
            itterout = art.GREEN
            out.append(itterout)
            continue
        if(guess[i] in word):
            out.append(itterout)
            continue
        out.append(art.RED)
    return out

def inputGuess(prompt, word):
    valid = False
    inp = ""
    while not valid:
        inp = input(prompt)
        if(len(inp) != len(word)):
            print("guesses must be the same length as selected word, currently", len(word))
        else:
            valid = True
    return inp


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
    for i in range(0, 5): 
        guess = inputGuess("Please make a guess\n  [$] ", word)
        guessColors = getGuessColors(word.lower(), guess.lower())
        art.printWord(guess.lower(), guessColors)
        if(guess.lower() == word.lower()):
            print("Congrats! you beat Terminal Wordle! ")
            break
    isRunning = askPlaying()


