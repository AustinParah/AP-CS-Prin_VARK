#Austin Parah

numItems = 4
costPerItem = 10.0
taxRate = 0.08
subTotal = 0
taxAmount = 0
totalPrice = 0


def doCalculations(items, howmany, taxes):
    subTotal = items * howmany
    taxAmount = taxes * subTotal
    totalPrice = taxAmount + subTotal
    return totalPrice

doCalculations(costPerItem, numItems, taxRate)


print("""SALES RECEIPT
Number of items : """ + str(numItems) +"""
Cost per item   : $""" + str(costPerItem) +"""
Tax rate        : """  + str(taxRate) +"""
Tax amount      : $"""  + str(taxAmount) +"""
TOTAL SALE PRICE: $"""  + str(totalPrice))
