# Julius Hollis
# 06-23-2023
# P2LAB2 – Vehicle MPG Dictionary
# This program stores MPG values for vehicles in a dictionary, allows the user to 
# select a vehicle, and calculates how many gallons of gas are needed to drive a 
# user-specified number of miles.

# Define the vehicle MPG dictionary
vehicle_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Create a variable that holds all the keys (vehicle names)
keys = vehicle_mpg.keys()

# Print the list of vehicle options
print("Available vehicles:")
print(keys)

# Prompt the user to enter one of the vehicles
vehicle = input("Enter the vehicle name exactly as shown above: ")

# Check if the vehicle exists in the dictionary
if vehicle in vehicle_mpg:
    mpg = vehicle_mpg[vehicle]
    print(f"{vehicle} gets {mpg} miles per gallon.")

    # Ask the user how many miles they will drive
    miles = float(input("Enter the number of miles you will drive: "))

    # Calculate the gallons needed
    gallons_needed = miles / mpg

    # Display the result rounded to two decimal places
    print(f"You will need {gallons_needed:.2f} gallons of gas to drive {miles} miles in a {vehicle}.")
else:
    print("Invalid vehicle name. Please run the program again and enter the name exactly as shown.")
