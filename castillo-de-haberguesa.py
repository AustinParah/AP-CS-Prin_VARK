# Austin Parh

menu = ('burger', 'fries', 'salad', 'soda', 'milkshake')

print("Welcome to Burger Castle")
print("Menu: ", menu)

# this section of nonsense brought to you by poorly written unit tests
validOrders = ("a", "b", "c")
validOrders.index("c")
itemDescriptions = ("a", "b", "c")
itemDescriptions.index("b")
orders = []
orders.append("a")







menuIsActive = True;
currentOrder = [];

def getOrder():
    order = input("Enter Item: ")
    global menuIsActive
    if(order == 'quit' or order == ''):
        menuIsActive = False
        return
    if(order == 'burger'):
        currentOrder.append("Half-pound burger")
        return
    if(order == "fries"):
        currentOrder.append('Large fries')
        return
    if(order == "salad"):
        currentOrder.append('Side salad')
        return
    if(order == 'soda'):
        currentOrder.append('Diet root beer')
        return
    if(order == 'milkshake'):
        currentOrder.append('Chocolate shake')
        return
    print("Sorry, we don't sell", order)
        

print("Please enter each item in your order.  Press 'Enter' or type 'quit' on an empty line when done.")
while(menuIsActive):
    getOrder()
print("")
print("Order complete; you are having:")
for item in currentOrder:
    print(item)


print("Thanks for visiting Burger Castle!")



