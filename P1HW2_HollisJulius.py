# Julius Hollis
# 6-16-2025
# P1HW2_HollisJulius
# This program asks the user for a travel budget and expenses,
# calculates total expenses and remaining balance,
# then displays the results in a formatted output.

# Pseudocode:
# 1. Ask the user to enter their total budget.
# 2. Ask for their travel destination.
# 3. Ask how much they plan to spend on gas.
# 4. Ask how much they plan to spend on accommodation.
# 5. Ask how much they plan to spend on food.
# 6. Calculate total expenses by adding gas, accommodation, and food.
# 7. Calculate remaining budget by subtracting expenses from the total budget.
# 8. Display all results clearly.

# Collect user inputs
print("\nThis program calculates and displays travel expenses")
budget = float(input("Enter your budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Perform calculations
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

# Display results
print("\n----------Travel Summary----------")
print("Destination:", destination)
print("Initial Budget: $" + format(budget, ".2f"))
print("\nExpenses")
print("Gas: $" + format(gas, ".2f"))
print("Accommodation: $" + format(accommodation, ".2f"))
print("Food: $" + format(food, ".2f"))
print("----------------------------------")

print("Remaining Balance: $" + format(remaining_balance, ".2f"))
