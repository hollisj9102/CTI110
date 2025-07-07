def show_table(number):
    # for loop to print multiplication table from 1 to 12
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")

def main():
    run_again = "yes"
    
    while run_again.lower() == "yes":
        try:
            user_input = int(input("Enter an integer: "))
            if user_input >= 0:
                show_table(user_input)
            else:
                print("This program does not handle negative numbers.")
        except ValueError:
            print("Please enter a valid integer.")

        run_again = input("Would you like to run the program again? (yes/no): ")

    print("Existing program...")

# Run the program
main()
