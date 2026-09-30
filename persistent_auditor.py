FILE_NAME = "inventory.txt"
 
 
def load_inventory():
    """Read the saved total and transaction history from the file.
    If the file does not exist yet, start with an empty inventory."""
    total = 0
    history = []
 
    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()          # list of strings, one per line
 
        if len(lines) > 0:
            total = int(lines[0].strip())     # line 1 = the running total
            for line in lines[1:]:            # every other line = one transaction
                line = line.strip()
                if line != "":
                    history.append(int(line))
 
        print("Inventory loaded from", FILE_NAME)
 
    except FileNotFoundError:
        print("No saved inventory found. Starting with an empty inventory.")
 
    return total, history
 
 
def save_inventory(total, history):
    """Write the total and every transaction back to the file."""
    with open(FILE_NAME, "w") as file:
        file.write(str(total) + "\n")         # line 1 = total
        for amount in history:
            file.write(str(amount) + "\n")    # one transaction per line
    print("Inventory successfully saved to", FILE_NAME)
 
 
def get_valid_input():
    """Keep asking until the user types a whole number or 'quit'.
    Returns the number, 'quit', or None for a rejected entry."""
    stock = input("Enter stock quantity. Type quit to exit: ")
 
    if stock.lower() == "quit":
        return "quit"
 
    if stock.isdigit():
        return int(stock)
 
    print("Error: Please enter a valid number.")
    return None
 
 
def process_delivery(current_total, new_value):
    return current_total + new_value
 
 
def calculate_tax(amount):
    return amount * 0.10
 
 
def generate_report(total_units, history, failed_attempts):
    print("\n=== Final Inventory Report ===")
    print("Total units in inventory:", total_units)
    print("Total deliveries on record:", len(history))
    print("Transaction history:", history)
    print("Number of failed/rejected entries this session:", failed_attempts)
 
 
# ---------------- Main program ----------------
print("=== Smart Inventory Auditor ===")
 
total_units, history = load_inventory()
failed_attempts = 0
limit_exceeded = False                        # becomes True if stock goes past 500
 
print("Current total:", total_units)
print("Previous transactions:", history)
 
while True:
    stock = get_valid_input()
 
    if stock == "quit":
        break
 
    if stock is None:
        failed_attempts += 1
        continue
 
    total_units = process_delivery(total_units, stock)
    history.append(stock)                     # remember this transaction
    tax = calculate_tax(stock)
 
    print("Delivery accepted:", stock, "units")
    print("Tax for this delivery: $", format(tax, ".2f"))
    print("Total units processed:", total_units)
 
    if total_units > 500:
        print("ALERT: Stock exceeds maximum limit of 500 units. Stopping program.")
        limit_exceeded = True
        break
    elif total_units == 500:
        print("Stock is at maximum limit of 500 units.")
 
# Show the report first, so the user sees what happened before any reset
generate_report(total_units, history, failed_attempts)
 
if limit_exceeded:
    save_inventory(0, [])                     # wipe the saved data
    print("Inventory has been reset. The next run will start from 0.")
else:
    save_inventory(total_units, history)      # normal save when user quits
