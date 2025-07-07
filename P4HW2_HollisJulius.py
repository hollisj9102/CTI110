# Julius Hollis
# 7-7-2025
# P4HW2: Payroll Report
# This program calculates gross pay for multiple employees. It separates overtime pay and regular pay,
# and totals these values across all employees until the user enters "Done".

# Pseudocode:
# 1. Initialize totals: total_overtime, total_regular, total_gross, employee_count
# 2. Loop:
#    a. Ask for employee name (end if "Done")
#    b. Ask for hours worked and pay rate
#    c. Calculate regular pay (up to 40 hours), overtime (hours > 40)
#    d. Compute gross pay = regular + overtime
#    e. Add values to totals
#    f. Display individual breakdown for the employee
# 3. After loop ends, display total summary

# Initialize total trackers
total_overtime = 0
total_regular = 0
total_gross = 0
employee_count = 0

# Start sentinel loop
while True:
    employee_name = input("Enter employee name or 'Done' to terminate: ")

    if employee_name.lower() == "done":
        break

    try:
        hours_worked = float(input(f"How many hours did {employee_name} work? "))
        pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours_worked

    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

    # Accumulate totals
    total_overtime += overtime_pay
    total_regular += regular_pay
    total_gross += gross_pay
    employee_count += 1

    # Display individual breakdown
    print("-" * 40)
    print(f"Employee Name: {employee_name}")
    print(f"Hours Worked:     {hours_worked}")
    print(f"Pay Rate:         ${pay_rate:.2f}")
    print(f"Overtime Pay:     ${overtime_pay:.2f}")
    print(f"Regular Pay:      ${regular_pay:.2f}")
    print(f"Gross Pay:        ${gross_pay:.2f}")
    print("-" * 40)
    print()

# Final summary
print("\nSummary Report")
print("=" * 40)
print(f"Total employees entered:       {employee_count}")
print(f"Total overtime pay:            ${total_overtime:.2f}")
print(f"Total regular pay:             ${total_regular:.2f}")
print(f"Total gross pay:               ${total_gross:.2f}")
