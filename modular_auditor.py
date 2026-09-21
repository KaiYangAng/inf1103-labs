def get_valid_input():
    while True:
        stock = input("Enter stock quantity. Type quit to exit: ")

        if stock.lower() == "quit":
            return "quit"

        if stock.isdigit():
            return int(stock)

        print("Error: Please enter a valid number.")


def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total


def calculate_tax(amount):
    tax = amount * 0.10
    return tax


def generate_report(total_units, failed_attempts):
    print("\n=== Final Inventory Report ===")
    print("Total units processed:", total_units)
    print("Total deliveries processed:", deliveries_processed)
    print("Number of failed/rejected entries:", failed_attempts)


# Main program
total_units = 0
failed_attempts = 0
deliveries_processed = 0

print("=== Smart Inventory Auditor ===")

while True:
    stock = get_valid_input()

    if stock == "quit":
        break

    # Process the valid delivery
    total_units = process_delivery(total_units, stock)

    # Calculate tax for this delivery
    tax = calculate_tax(stock)

    # Update delivery counter
    deliveries_processed += 1

    print("Delivery accepted:", stock, "units")
    print("Tax for this delivery: $", format(tax, ".2f"))
    print("Total units processed:", total_units)

    # Check inventory limit
    if total_units > 500:
        print("Warning: Stock exceeds maximum limit of 500 units.")
    elif total_units == 500:
        print("Stock is at maximum limit of 500 units.")

# Final report
generate_report(total_units, failed_attempts)
