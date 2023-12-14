# Exercise 2: Student Class ☑️
# Develop a GUI using Tkinter to Create a class called Students.

# The class should have the following members.Name (string), Mark1 (int), Mark2 (int), Mark3 (int) 
# The class should have the following methods calcGrade() - should return an average from the three marks.display()- 
# should output the student name and calculated grade average
# Create one object using a constructor that contains parameters to initialize all of the variables
# Ask user to input the variable values using input() and pass the values to the second object

import tkinter as tk

# Making a class for student
class Students:
    def __init__(self, name, mark1, mark2, mark3):
        # student attributes
        self.name = name.title()
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    # making function calculate the average grade
    def calcGrade(self):
        return (self.mark1 + self.mark2 + self.mark3) / 3

    # function for displaying student information
    def display(self):
        return f"Name: {self.name}\nAverage marks: {self.calcGrade()}"

# Function to calculate the average when the button is clicked
def calc_average():
    # Getting input values from user entry
    name = entry_name.get()
    mark1 = int(entry_mark1.get())
    mark2 = int(entry_mark2.get())
    mark3 = int(entry_mark3.get())

    # Create a Students object with the input values
    student = Students(name, mark1, mark2, mark3)

    # Update the result label with the student information
    result_label.config(text=student.display())

# Create the main Tkinter window
root = tk.Tk()
root.title("10/dec/2023 Student Class")
root.geometry("200x250")

# Initialize entry in variables to be none
entry_name = None
entry_mark1 = None
entry_mark2 = None
entry_mark3 = None

# Create labels and entry widgets for name and marks
for index, labeltext in enumerate(["Name:", "Mark 1:", "Mark 2:", "Mark 3:"]):
    label_name = tk.Label(root, text=labeltext)
    label_name.grid(row=index, column=0, pady=5)

    # making entry widgets and storing them insiide variables
    if labeltext == "Name:":
        entry_name = tk.Entry(root)
        entry_name.grid(row=index, column=1, pady=5)
    elif labeltext == "Mark 1:":
        entry_mark1 = tk.Entry(root)
        entry_mark1.grid(row=index, column=1, pady=5)
    elif labeltext == "Mark 2:":
        entry_mark2 = tk.Entry(root)
        entry_mark2.grid(row=index, column=1, pady=5)
    elif labeltext == "Mark 3:":
        entry_mark3 = tk.Entry(root)
        entry_mark3.grid(row=index, column=1, pady=5)

# avg btn
calc_avg_btn = tk.Button(root, text="Calculate Average", command=calc_average)
calc_avg_btn.grid(row=4, column=0, columnspan=2, pady=10)

# Result label to display student information
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()