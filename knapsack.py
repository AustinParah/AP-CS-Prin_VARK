import random

# Austin Parah

# The student will complete this method where shown.
# Given a sorted list of products and a maximum weight, find the mix of 
# products that will fit and produce maximum value
def solve(products, maxWeight):
    
    # keep track of our current weight and value
    currentWeight = 0
    currentValue = 0
    
    # get a rough idea of algorithm effort
    statementCount = 0
    
    # create a list to count the number of each product added
    productCount = []
    
    # STUDENT CODE BEGINS HERE
    

     
    # STUDENT CODE ENDS HERE
    
    # display totals for this algorithm   
    print("Final value $" + str(currentValue) + ", Final weight " + str(currentWeight) +\
          ", Statement count: " + str(statementCount))
    
    print("Product Counts: ",end="")
    for i in range(len(productCount)):
        print("Product #" + str(i) + ": " + str(productCount[i]) + ", ",end="" )
    print()

# NO STUDENT CHANGES BELOW THIS LINE

# sorting helper method
def byValue(element):
    return element[1]  # use the value as the sort key

# sorting helper method
def byValueToWeight(element):
    return element[1] / element[2]  # use the value / weight as the sort key

# heuristic #1 will add in the most expensive items while room remains
def solveKnapsack1(products,maxWeight):
    print("===Heuristic 1===")
    
    # sort products by value, descending order
    products.sort(reverse=True, key=byValue)  
    
    # display sorted products
    displayProducts("Sorted for heuristic 1",products)
    
    # run algorithm for this heuristic
    solve(products,maxWeight)
    
# heuristic #2 will add in the most valuable items per pound while room remains
def solveKnapsack2(products,maxWeight):
    print("===Heuristic 2===")

    # sort products by most valuable per pound, descending order
    products.sort(reverse=True, key=byValueToWeight)

    # display sorted products
    displayProducts("Sorted for heuristic 2",products)

    # run algorithm for this heuristic
    solve(products,maxWeight)

# display information about all products in the input list, with a prefix description
def displayProducts(prefix, products):
    print(prefix + ": ",end="")
    for product in products:
        num = product[0]
        value = product[1]
        weight = product[2]
        print("#" + str(num) + ", Value $" + str(value) + \
               ", Weight " + str(weight) + " | ", end="")
    print()
        
# main program logic starts here

# get the number of products and the simulation number
commands = str.split(input("Enter number of products and simulation number: "))
numProducts = int(commands[0])
simNumber = int(commands[1])

random.seed(simNumber)  # seed the random number generator for consistent results

# create set of products with random value and weight
products = []

for i in range(numProducts):
    product = []
    product.append(i)  # product number
    product.append(random.randrange(1,5))  # value  1-4
    product.append(random.randrange(1,5))  # weight 1-4
    product.append(0)  # initial number of times this product added
    products.append(product)

# display our initial set of products    
displayProducts("Unsorted products    ",products)

# run both heuristic algorithms to see which is better
solveKnapsack1(products,10)
solveKnapsack2(products,10)
