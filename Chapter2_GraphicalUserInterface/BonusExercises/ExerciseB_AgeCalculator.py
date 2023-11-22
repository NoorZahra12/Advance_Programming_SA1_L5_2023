# Exercise B: Age Calculator
# Create a program to take input of the user's date of birth and output the age. 
# Expected input: 8/5/2018 
# Expected output: Your age is 5 years 
# Hint: you can use the date from datetime package to get today's date

import tkinter as tk
import datetime

root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x200")
def calculate_age():
    def convert(date):
        return int(datetime.datetime.strptime(date, "%m/%d/%Y").timestamp())
    date_of_birth = "08/05/2018"
    current_date = datetime.datetime.current_date().timestamp()
    current_age = current_date - convert(date_of_birth) // (60 * 60 * 24 * 365)
    print('Your age is', current_age//365,"years old.")

label = tk.Label(root, text="Enter Date of Birth: ")
label.pack()
entry = tk.Entry(root, text="dd-mm-yyyy", width=20)
entry.pack()
button = tk.Button(root, text="Calculate", command=calculate_age)
button.pack()

resultLabel = tk.Label(root)

root.mainloop()