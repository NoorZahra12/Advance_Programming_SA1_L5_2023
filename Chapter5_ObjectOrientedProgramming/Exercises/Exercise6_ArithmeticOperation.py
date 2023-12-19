# Exercise 6: Arithmetic Operation ☑️
# Develop a GUI to perform Arithmetic Operations.

# Create a class ArithmeticOperations with the following
# a result variable to store the result after calculation
# a function Calculate() - To perform an arithmetic operation selected by the user.
# You can use Combobox to provide users with options to perform selected arithmetic operations and entry widgets for the values.


# importing libraries
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

# making a class which takes 2 numbers and a selected operator by the user
class ArithmeticOperations:
    def __init__(self, num1, num2, selected_operator):
        # the input is string by default so need to convert it into float before calculating it
        self.number1 = float(num1)
        self.number2 = float(num2)
        # storing the selected operator in a variable
        self.selected_operator = selected_operator
        self.result = ""

    # making a function which will calculate the numbers
    def calculate(self):
        
        if self.selected_operator == "Addition":
            return self.number1 + self.number2
        elif self.selected_operator == "Subtraction":
            return self.number1 - self.number2
        elif self.selected_operator == "Multiplication":
            return self.number1 * self.number2
        elif self.selected_operator == "Division":
            if self.number2 != 0:
                return self.number1 / self.number2
            else:
                return "Cannot divide by zero"
        elif self.selected_operator == "Remainder":
            if self.number2 != 0:
                return self.number1 % self.number2
            else:
                return "Cannot calculate remainder with zero divisor"


# functionn which will call the calculate function and display the result
def calculate_result():
    num1_value = entry_num1.get()
    num2_value = entry_num2.get()
    selected_operator = combo_operator.get()

    # using class the calculation
    calculator = ArithmeticOperations(num1_value, num2_value, selected_operator)
    # calulating the answer and storing it in variable
    result = calculator.calculate()

    # updating the the result label with the new answer
    result_var.set(f"Result: {result}")

# Main Tkinter window
root = tk.Tk()
root.title("Chp5 Ex6 Arithmetic Operations")
root.geometry("400x300")

# Background image
bg_image_path = os.path.join(os.path.dirname(__file__), "arth_op_bg.png")
original_bg_image = Image.open(bg_image_path)
resized_bg_image = ImageTk.PhotoImage(original_bg_image.resize((400, 300), Image.BICUBIC))
bg_label = tk.Label(root, image=resized_bg_image)
bg_label.place(relwidth=1, relheight=1)

# Form frame with labels and entries in a grid
form_frame = tk.Frame(root)
form_frame.pack(pady=20)
# NUMBER 1
label_num1 = tk.Label(form_frame, text="Enter Num 1:")
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
entry_num1 = tk.Entry(form_frame)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

# NUMBER 2
label_num2 = tk.Label(form_frame, text="Enter Num 2:")
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
entry_num2 = tk.Entry(form_frame)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

# OPERATOR
label_operator = tk.Label(form_frame, text="Select Operator:")
label_operator.grid(pady=5, columnspan=2)
options = ["Addition", "Subtraction", "Multiplication", "Division", "Remainder"]
combo_operator = ttk.Combobox(form_frame, values=options)
combo_operator.grid(pady=10, columnspan=2)

# Button to call the function and do the calculation
calculate_button = tk.Button(form_frame, text="Calculate", command=calculate_result, bg="indigo", fg="white",padx=5,pady=2)
calculate_button.grid(pady=10, columnspan=2)

# result label to display the answer
result_var = tk.StringVar()
result_label = tk.Label(form_frame, textvariable=result_var, padx=10)
result_label.grid(pady=10, columnspan=2)

root.mainloop()