# Exercise 3: Calculator☑️
# Write a program that will display the following calculator menu

# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
# 5. Modulus
# 6. Check greater number
# The program will prompt the user to choose the operation choice (from 1 to 6). Then it asks the user to input values for the calculation. The program outputs the results of the calculation.Use operator module functions

# Extension Problem (Bonus):
# Allow the user to keep entering values until they enter Q to quit.
# Handle incorrect input


# making a function for addition where user can add as many value as they want
def add():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    ans = num1 + num2
    print("The sum is: ", ans)

    while True:
        addv = input("Do you want to add value?\ntype q to quit:")
        if addv.lower() == "q":
            break
        else:
            v = float(input("Number: "))
            ans += v
            print("Answer: ", ans)
# making a function for subtraction where user can subtract as many ties as they want
def subtract():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    ans = num1 - num2
    print("The difference is: ", ans)

    while True:
        addv = input("Do you want to subtract value?\ntype q to quit:")
        if addv.lower() == "q":
            break
        else:
            v = float(input("Number: "))
            ans -= v
            print("Answer: ", ans)

# making a function for multipication where user can multiply as many ties as they want
def mul():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    ans = num1 * num2
    print("The product is: ", ans)

    while True:
        addv = input("Do you want to multiply value?\ntype q to quit:")
        if addv.lower() == "q":
            break
        else:
            v = float(input("Number: "))
            ans *= v
            print("Answer: ", ans)

def greater():
    userlist = []
    while True:
        n = input("Enter Number (type q to quit): ")
        if n.lower() == "q":
            break
        else:
            userlist.append(float(n))
    # displaying answer
    ans = max(userlist)
    print("The greatest number is: ", ans)
    # thinking about it now, i could have used prod() on the list for the multiplication function but oh well i already wrote the mul()

while True:
    # displaying menu
    useroperation = input("\nChoose an operation by typing the number:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus\n6. Check greater number\nYou can also press q to quit\n\nOperation:")
    # loop will break if user types q
    if useroperation.lower() == "q":
        break

    if useroperation in ['1', '2', '3', '4', '5', '6']:
        # calling functions based on users choice
        if useroperation == '1':
            # calling function
            add()
        elif useroperation == '2':
            # calling function
            subtract()
        elif useroperation == '3':
            # calling function
            mul()
        elif useroperation == '4':
            # taking only 2 inputs
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            ans = a / b
            print("Answer: ", ans)
        elif useroperation == '5':
            # taking only 2 inputs
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            ans = a % b
            print("Answer: ", ans)
        elif useroperation == '6':
            # calling function
            greater()
    # error handling
    else:
        print("Invalid input")
