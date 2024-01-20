def calculate_error_rate():
    while True:
        print("Welcome to the Error Rate Calculator!")
        choice = input("Are you trying to calculate X, Y, or E? ")

        if choice.lower() == 'e':
            # X is the actual value
            X = float(input("Please enter the actual value (X): "))
            # Y is the experimental value
            Y = float(input("Please enter the experimental value (Y): "))
            E = (X - Y) / Y
            print(f"The calculated error rate E is: {E}")

        elif choice.lower() == 'x':
            E = float(input("Please enter the value for E: "))
            # Y is the experimental value
            Y = float(input("Please enter the experimental value (Y): "))
            # X is the actual value
            X = E * Y + Y
            print(f"The calculated actual value (X) is: {X}")

        elif choice.lower() == 'y':
            E = float(input("Please enter the value for E: "))
            # X is the actual value
            X = float(input("Please enter the actual value (X): "))
            # Y is the experimental value
            Y = X / (E + 1)
            print(f"The calculated experimental value (Y) is: {Y}")

        else:
            print("Invalid choice. Please enter either 'X', 'Y', or 'E'.")

        restart = input("Would you like to perform a new calculation? (yes/no) ")
        if restart.lower() != 'yes':
            break

calculate_error_rate()

