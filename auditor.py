totalunitprocessed=0
numberoffailedunits=0

print("===Smart Inventory Auditor===")
stock=input("Enter stock quantity. Type quit to exit. \n")
while stock != "quit":
    if not stock.isdigit():
        print("Error, please enter a valid number.")
        numberoffailedunits += 1
    else: 
        totalunitprocessed += int(stock)
        print("Total units processed:", totalunitprocessed)
    if int(totalunitprocessed) > 500:
        print("Warning: Stock exceeds maximum limit of 500 units.")
        break
    if int(totalunitprocessed) == 500:
        print("Stock is at maximum limit of 500 units.")
        break
    stock=input("Enter stock quantity. Type quit to exit. \n")
print("Total units processed:", totalunitprocessed)
print("Number of failed units:", numberoffailedunits)
        

