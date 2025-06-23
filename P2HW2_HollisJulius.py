# Julius Hollis
# 06-23-2025
# P2HW2 – List and Grade Statistics
# This program prompts the user to enter 6 test grades,
# stores them in a list, and then calculates and displays
# the lowest grade, highest grade, total, and average.
# The output is properly formatted as specified.

'''
Pseudocode:
1. Prompt user to input grades for Module 1 through Module 6.
2. Convert each input to float and store in a list named "grades".
3. Use built-in functions to:
    - Find the lowest grade (min)
    - Find the highest grade (max)
    - Find the sum of all grades (sum)
    - Calculate average (sum divided by length of list)
4. Display the results:
    - Use labels like "Lowest Grade:", "Highest Grade:", etc.
    - Display values with correct spacing and formatting (2 decimal places for average).
'''

# Step 1: Get grades from user
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

# Step 2: Store grades in a list
grades = [grade1, grade2, grade3, grade4, grade5, grade6]

# Step 3: Perform calculations
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

# Step 4: Display results
print("\n------------Results------------")
print(f"Lowest Grade:      {lowest}")
print(f"Highest Grade:     {highest}")
print(f"Sum of Grades:     {total}")
print(f"Average:           {average:.2f}")
print("--------------------------------")
