# Julius Hollis
# 6-16-2025
# P1HW1_HollisJulius
# This program asks the user for input to calculate:
# 1. A base raised to an exponent
# 2. The result of adding two numbers and subtracting a third

# Part 1: Exponentiation
base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
power = base ** exponent
print()
print(base, "raised to the power of", exponent, "is", power, "!")
print()

# Part 2: Arithmetic expression
num1 = int(input("Enter integer #1: "))
num2 = int(input("Enter integer #2: "))
num3 = int(input("Enter integer #3: "))

sum_result = num1 + num2
final_result = sum_result - num3

print()
print(num1, "+", num2, "=", sum_result)
print(sum_result, "-", num3, "=", final_result)
