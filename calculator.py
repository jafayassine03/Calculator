while True:
    print("\n--- Calculator ---")
    print("1) Add")
    print("2) Subtract")
    print("3) Divide")
    print("4) Multiply")
    print("5) Power")
    print("6) Exit")

    try:
        choice = int(input("Choose an option (1-6): "))
    except ValueError:
        print("Please enter a number between 1 and 6.")
        continue

    if choice == 6:
        print("Goodbye 👋")
        break

    if choice not in [1, 2, 3, 4, 5]:
        print("Invalid choice. Try again.")
        continue

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Numbers only please.")
        continue

    if choice == 1:
        print("Result:", a + b)

    elif choice == 2:
        print("Result:", a - b)

    elif choice == 3:
        if b == 0:
            print("You can't divide by zero.")
        else:
            print("Result:", a / b)

    elif choice == 4:
        print("Result:", a * b)

    elif choice == 5:
        print("Result:", a ** b)

    again = input("Do you want to calculate again? (y/n): ").lower()
    if again != "y":
        print("Alright, see you next time.")
        breaks
