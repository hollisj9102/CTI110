# Julius Hollis
# 6-28-2025
# P3HW2_Salary_HollisJulius
# This program calculates the gross pay for an employee, including regular and overtime pay.
# It asks the user to enter the employee's name, hours worked, and pay rate,
# then calculates and displays a breakdown of regular pay, overtime pay, and gross pay.

# Pseudocode:
# 1. Ask the user to enter the employee's name.
# 2. Ask for number of hours worked.
# 3. Ask for pay rate.
# 4. Check if hours worked > 40 to determine overtime.
# 5. If overtime, calculate overtime hours and pay.
# 6. Calculate regular hours and regular pay.
# 7. Calculate gross pay (regular pay + overtime pay).
# 8. Display a well-formatted breakdown.

# Input
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Calculations
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

overtime_pay = overtime_hours * (pay_rate * 1.5)
regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

# Output
print()
print("----------------------------------------------------------")
print(f"{'Employee Name:':<25} {employee_name}")
print("----------------------------------------------------------")
print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'Overtime Hours':<18}{'Overtime Pay':<15}{'Reg Pay':<15}{'Gross Pay'}")
print(f"{hours_worked:<15.2f}{pay_rate:<15.2f}{overtime_hours:<18.2f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:.2f}")
print("----------------------------------------------------------")
