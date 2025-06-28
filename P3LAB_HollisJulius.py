# Julius Hollis
# 6-28-2025
# P3LAB_HollisJulius
# This program calculates the most efficient number of dollars, quarters,
# dimes, nickels, and pennies needed to make the given amount of money.

# Get input from user
amount = float(input("Enter amount in dollars and cents (e.g., 2.36): "))

# Convert amount to cents
cents = int(round(amount * 100))

# Calculate each coin
dollars = cents // 100
cents -= dollars * 100

quarters = cents // 25
cents -= quarters * 25

dimes = cents // 10
cents -= dimes * 10

nickels = cents // 5
cents -= nickels * 5

pennies = cents

# Output results
if dollars == 1:
    print("1 dollar")
elif dollars > 1:
    print(f"{dollars} dollars")

if quarters == 1:
    print("1 quarter")
elif quarters > 1:
    print(f"{quarters} quarters")

if dimes == 1:
    print("1 dime")
elif dimes > 1:
    print(f"{dimes} dimes")

if nickels == 1:
    print("1 nickel")
elif nickels > 1:
    print(f"{nickels} nickels")

if pennies == 1:
    print("1 penny")
elif pennies > 1:
    print(f"{pennies} pennies")
