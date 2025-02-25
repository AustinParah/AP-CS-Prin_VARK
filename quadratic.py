
import math

def findQuadraticRoots(A,B,C):
    # student code here
    if(not (B**2 + -4*A*C < 0)):
        root1 = (-B + math.sqrt(B**2 + -4*A*C) ) / (2*A)
        root2 = (-B - math.sqrt(B**2 + -4*A*C) ) / (2*A)
        print("root1: ",root1)
        print("root2: ", root2)
    else:
        print("no real roots")



# main code (no change below this line)
equation = input("Enter A B C for your quadratic expression: ")
terms = equation.split()
A = int(terms[0])
B = int(terms[1])
C = int(terms[2])
findQuadraticRoots(A,B,C)
