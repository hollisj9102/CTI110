# Julius Hollis
# 7-7-2025
# P4HW1: Score Processor with Grade
# This program collects a set number of test scores, drops the lowest,
# calculates the average, and displays the corresponding letter grade.

# --- Pseudocode ---
# 1. Ask user how many scores they want to enter
# 2. Loop to collect that many valid scores (0–100 only)
#    - If invalid, re-prompt until valid
# 3. Add all valid scores to a list
# 4. Drop the lowest score
# 5. Display:
#    - Lowest score
#    - Modified list (without lowest)
#    - Average of modified list
#    - Letter grade based on average

# Get number of scores to collect
num_scores = int(input("How many scores would you like to enter? "))

# Initialize empty list to store valid scores
score_list = []

# Collect scores using a loop
for i in range(num_scores):
    while True:
        try:
            score = float(input(f"Enter score #{i + 1}: "))
            if 0 <= score <= 100:
                score_list.append(score)
                break
            else:
                print("Invalid score. Must be between 0 and 100. Try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Drop the lowest score
lowest = min(score_list)
score_list.remove(lowest)

# Calculate average of remaining scores
average = sum(score_list) / len(score_list)

# Determine letter grade
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

# Display results
print("\n----------Results----------")
print(f"{'Lowest score dropped:':<40} {lowest}")
print(f"{'Scores after drop:':<40} {score_list}")
print(f"{'Average of remaining scores:':<40} {average:.2f}")
print("---------------------------")
print(f"{'Letter grade:':<40} {grade}")
