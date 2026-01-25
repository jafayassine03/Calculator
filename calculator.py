while True:
    print("\nchoose the oepration you want to perform")
    print("1 for addition (+) ")
    print("2 for subtraction (-)")
    print("3 for division (/)")
    print("4 for multiplication (*)")
    print("5 to exit")

    Ch =int(input("your choice: "))
        
    if Ch < 1 or Ch > 5:
        print("invalid choice")
    else:

        a = float(input("input your first number: "))
        b = float(input("input your second number: "))

        if Ch  == 1:
                print("Result: ", a+b)
        elif Ch == 2:
                print("Result: ", a-b)
        elif Ch == 3:
                print("Result: ", a/b)
        elif Ch == 4:
                print("Result: ", a*b)
        elif Ch == 5:
                print("Goodbye:" )
   
    again = input("Do you want to calculate again? (y/n): ")
    if again != 'y' and again != 'Y':
        print("Goodbye!")
        break