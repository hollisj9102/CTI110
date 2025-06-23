# Julius Hollis
# 06-23-2025
# P2HW1 – Travel Budget Formatting
# This program collects travel budgeting information from the user,
# performs basic calculations, and displays the results in a neatly
# formatted output with aligned columns and currency formatting.

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
print("\n------------Travel Expenses------------")
print(f"{'Location:':<20}{destination}")
print(f"{'Initial Budget:':<20}${budget:.2f}")
print(f"{'Fuel:':<20}${gas:.2f}")
print(f"{'Accommodation:':<20}${accommodation:.2f}")
print(f"{'Food:':<20}${food:.2f}")
print("----------------------------------------")
print(f"{'Remaining Balance:':<20}${remaining_balance:.2f}")

