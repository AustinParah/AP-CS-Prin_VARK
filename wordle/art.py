def StartText():
    print("""
|''||''| '||''''| '||'''|, '||\   /||` |''||''| '||\   ||`      /.\      '||     
   ||     ||   .   ||   ||  ||\\\\.//||     ||     ||\\\\  ||      // \\\\      ||     
   ||     ||'''|   ||...|'  ||     ||     ||     || \\\\ ||     //...\\\\     ||     
   ||     ||       || \\\\    ||     ||     ||     ||  \\\\||    //     \\\\    ||     
  .||.   .||....| .||  \\\\. .||     ||. |..||..| .||   \||. .//       \\\\. .||...|
          
                     ▗▖ ▗▖ ▗▄▖ ▗▄▄▖ ▗▄▄▄  ▗▖   ▗▄▄▄▖
                     ▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▐▌  █ ▐▌   ▐▌   
                     ▐▌ ▐▌▐▌ ▐▌▐▛▀▚▖▐▌  █ ▐▌   ▐▛▀▀▘
                     ▐▙█▟▌▝▚▄▞▘▐▌ ▐▌▐▙▄▄▀ ▐▙▄▄▖▐▙▄▄▖
                               """)

def a():
    return"""
 ▗▄▖ 
▐▌ ▐▌
▐▛▀▜▌
▐▌ ▐▌
          """
def b():
    return"""
▗▄▄▖ 
▐▌ ▐▌
▐▛▀▚▖
▐▙▄▞▘
          """

def c():
    return"""
 ▗▄▄▖
▐▌   
▐▌   
▝▚▄▄▖
          """

def d():
    return"""
▗▄▄▄  
▐▌  █ 
▐▌  █ 
▐▙▄▄▀ 
          """


def e():
    return"""
▗▄▄▄▖
▐▌   
▐▛▀▀▘
▐▙▄▄▖
          """
def f():
    return"""
▗▄▄▄▖
▐▌   
▐▛▀▀▘
▐▌   
          """

def g():
    return"""
 ▗▄▄▖
▐▌   
▐▌▝▜▌
▝▚▄▞▘
          """

def h():
    return"""
▗▖ ▗▖
▐▌ ▐▌
▐▛▀▜▌
▐▌ ▐▌
          """

def i():
    return"""
▗▄▄▄▖
  █  
  █  
▗▄█▄▖
          """


def j():
    return"""
   ▗▖
   ▐▌
   ▐▌
▗▄▄▞▘
          """

def k():
    return"""
▗▖ ▗▖
▐▌▗▞▘
▐▛▚▖ 
▐▌ ▐▌
          """

def l():
    return"""
▗▖   
▐▌   
▐▌   
▐▙▄▄▖
          """

def m():
    return"""
▗▖  ▗▖
▐▛▚▞▜▌
▐▌  ▐▌
▐▌  ▐▌
          """

def n():
    return"""
▗▖  ▗▖
▐▛▚▖▐▌
▐▌ ▝▜▌
▐▌  ▐▌
          """

def o():
    return"""
 ▗▄▖ 
▐▌ ▐▌
▐▌ ▐▌
▝▚▄▞▘
          """

def p():
    return"""
▗▄▄▖ 
▐▌ ▐▌
▐▛▀▘ 
▐▌   
          """

def q():
    return"""
▗▄▄▄▖ 
▐▌ ▐▌ 
▐▌ ▐▌ 
▐▙▄▟▙▖
          """

def r():
    return"""
▗▄▄▖ 
▐▌ ▐▌
▐▛▀▚▖
▐▌ ▐▌
          """

def s():
    return"""
 ▗▄▄▖
▐▌   
 ▝▀▚▖
▗▄▄▞▘
          """

def t():
    return"""
▗▄▄▄▖
  █  
  █  
  █  
          """
def u():
    return"""
▗▖ ▗▖
▐▌ ▐▌
▐▌ ▐▌
▝▚▄▞▘
          """
def v():
    return"""
▗▖  ▗▖
▐▌  ▐▌
▐▌  ▐▌
 ▝▚▞▘ 
          """

def w():
    return"""
▗▖ ▗▖
▐▌ ▐▌
▐▌ ▐▌
▐▙█▟▌
          """

def x():
    return"""
▗▖  ▗▖
 ▝▚▞▘ 
  ▐▌  
▗▞▘▝▚▖
          """

def y():
    return"""
▗▖  ▗▖
 ▝▚▞▘ 
  ▐▌  
  ▐▌  
          """

def z():
    return """
▗▄▄▄▄▖
   ▗▞▘
 ▗▞▘  
▐▙▄▄▄▖
          """

def multiPrinter(strings, colors):
    lines = [s.splitlines() for s in strings]  # Split each string into lines
    max_lines = max(map(len, lines))  # Find the longest string (in terms of lines)
    
    # Ensure colors list is the same length as strings list
    if len(colors) != len(strings):
        raise ValueError("The number of colors must match the number of strings.")

    # Get max width per column for proper alignment
    col_widths = [max(len(line[i]) if i < len(line) else 0 for line in lines) for i in range(max_lines)]

    # Construct colored output
    result = [
        ' '.join(
            f"{colors[idx]}{(line[i] if i < len(line) else '').ljust(col_widths[i])}\033[0m"
            for idx, line in enumerate(lines)
        )
        for i in range(max_lines)
    ]

    return '\n'.join(result)

def getArtOf(letter):
    if(letter == "a"):
        return a()
    if(letter == "b"):
        return b()
    if(letter == "c"):
        return c()
    if(letter == "d" ):
        return d()
    if(letter == "e"):
        return e()
    if(letter == "f"):
        return f()
    if(letter == "g"):
        return g()
    if(letter == "h"):
        return h()
    if(letter == "j"):
        return "j"
    if(letter == "k"):
        return "k"
    if(letter == "l"):
        return l()
    if(letter == "m"):
        return m()
    if(letter == "n"):
        return n()
    if(letter == "o"):
        return o()
    if(letter == "p"):
        return p()
    if(letter == "q"):
        return q()
    if(letter == "r"):
        return r()
    if(letter == "s"):
        return s()
    if(letter == "t"):
        return t()
    if(letter == "u"):
        return u()
    if(letter == "v"):
        return v()
    if(letter == "x"):
        return x()
    if(letter == "y"):
        return y()
    if(letter == "z"):
        return z()
    return ""

RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"
YELLOW = "\033[0;33m"
def printWord(string, colors):
    temp = []
    for l in string:
        temp.append(getArtOf(l))
    print(multiPrinter(temp, colors))

printWord("your mom",[YELLOW, RED, RED, RED,RED,RED,RED,RED])

print(multiPrinter([getArtOf("a"), getArtOf("b"), getArtOf("c")], [RED, GREEN, RED]))

