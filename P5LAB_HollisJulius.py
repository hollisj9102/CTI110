# Julius Hollis
# 7-14-2025
# P5LAB – Self-Checkout Change Calculator
# This program simulates a self-checkout machine. It generates a random total, 
# asks the user for payment, then calculates and displays the change broken down 
# into dollars, quarters, dimes, nickels, and pennies.

import random

def disperse_change(change):
    # Convert change to cents for easier calculation
    cents = round(change * 100)

    dollars = cents // 100
    cents = cents % 100

    quarters = cents // 25
    cents = cents % 25

    dimes = cents // 10
    cents = cents % 10

    nickels = cents // 5
    cents = cents % 5

    pennies = cents

    # Output the result
    print("Your change is:")
    print(f"Dollars: {dollars}")
    print(f"Quarters: {quarters}")
    print(f"Dimes: {dimes}")
    print(f"Nickels: {nickels}")
    print(f"Pennies: {pennies}")

def main():
    # Generate a random total owed
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"Amount owed: ${total_owed:.2f}")

    # Prompt user for payment
    amount_paid = float(input("Enter the amount you are paying: $"))

    # Check if enough was paid
    if amount_paid < total_owed:
        print("Insufficient amount paid. Transaction cancelled.")
        return

    # Calculate change
    change = round(amount_paid - total_owed, 2)
    print(f"Change owed: ${change:.2f}")

    # Disperse change
    disperse_change(change)

# Call the main function
main()
