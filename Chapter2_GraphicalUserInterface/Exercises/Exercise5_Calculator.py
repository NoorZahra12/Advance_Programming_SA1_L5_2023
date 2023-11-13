# Exercise 5: Calculator☑️
# Develop a GUI to perform basic arithmetic operations like addition, subtraction, multiplication, 
# Division, and modulo division using buttons. You can ask the user to enter the values in entry widget and 
# select the operation to be performed.

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("13/nov/2023 Calculator")

# basically there's gonna be 2 entry widgets for the user to type in
# then 5 options
# if user types evething correctly it will display the answer otherwise it will say that input is invalid

def calculate(operation):
    num1_val = num1Entry.get()
    num2_val = num2Entry.get()

    # checking if both string entry is in digits
    if num1_val.isdigit() and num2_val.isdigit():
        # converting string into float
        num1 = float(num1_val)
        num2 = float(num2_val)
        # performing the selected operation
        if operation == "+":
            result.set(num1 + num2)
        elif operation == "-":
            result.set(num1 - num2)
        elif operation == "x":
            result.set(num1 * num2)
        if operation == "/":
            # error handling in case user types 0 in division and remainder
            if num2 != 0:
                result.set(num1 / num2)
            # the message will be displayed instead of result in case user types 0
            else:
                result.set("Cannot divide by zero")
        elif operation == "Remainder":
            if num2 != 0:
                result.set(num1 % num2)
            # error handling
            else:
                result.set("Cannot divide by zero")
    # incase entry is not digits
    else:
        result.set("Invalid input")


# First Number
num1Label = tk.Label(root, text="First Number")
num1Label.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

num1Entry = tk.Entry(root, width=12)
num1Entry.grid(row=0, column=4, columnspan=3, padx=10, pady=10)

# Second Number
num2Label = tk.Label(root, text="Second Number")
num2Label.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

num2Entry = tk.Entry(root, width=12)
num2Entry.grid(row=1, column=4, columnspan=3, padx=10, pady=10)

# Buttons for calculations
buttons = ["+", "-", "x", "/", "Remainder"]
# this will display 5 buttons using for loop and it will do the necessary calculation according to which ever button user clicks
for i, operation in enumerate(buttons):
    tk.Button(root, text=operation, command=lambda op=operation: calculate(op)).grid(row=2, column=i, padx=5, pady=5)

# this will help link with the widget and modify it based on user input
result = tk.StringVar()
# Result label where the answer will be displayed or a message(about invalid input or can't divide by 0)
# here i am linking the widget with the result variable which holds the tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.grid(row=3, column=0, columnspan=7, pady=10)

# Start the main loop
root.mainloop()
