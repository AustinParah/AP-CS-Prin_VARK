

def eraseVowels(input):
    current = ""
    for letter in input:
        if(letter == 'x'):
            break
    
        if(letter != 'a' and letter != 'i' and letter != 'e' and letter != 'o' and letter != 'u'):
            current += letter
        
    return current

while(True):
    ini = input("Enter a phrase to process: ")
    if(ini == 'quit'):
        break
    print(eraseVowels(ini))
print("Program complete")
