import calculator

selection = int(input("\nSelect your calculator operation:  \
                       \n1. Addition  \
                       \n2. Subtraction  \
                       \n3. Multiplication  \
                       \n4. Division  \
                       \nSelection: "))
if selection not in (1, 2, 3, 4):
    print("Wrong selection.")
else: 
    print(f"You have selected: {selection}")
    num1 = int(input("Please provide your first value:\n"))
    num2 = int(input("Please provide your second value:\n"))
    if selection == 1:
        result = calculator.add(num1, num2)
        print(f"{num1} + {num2} = {result}.")

    if selection == 2:
        result = calculator.subtract(num1, num2)
        print(f"{num1} - {num2} = {result}.")

    if selection == 3:
        result = calculator.multiply(num1, num2)
        print(f"{num1} * {num2} = {result}.")

    if selection == 4:
        if num2 == 0:
            print("0 is not allowed")
        else: 
            result = calculator.divide(num1, num2)
            print(f"{num1} / {num2} = {result}.")

    if selection == 5:
        result = calculator.powerOf(num1, num2)
        print(f"{num1} to the power of {num2} is {result}.")
