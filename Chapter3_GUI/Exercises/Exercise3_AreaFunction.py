# Exercise 3: Area Function☑️
# Develop a GUI application using tkinter that allows users to calculate and display the areas of various shapes, 
# including circles, squares, and rectangles. The application should utilize a tabbed interface to organize the 
# calculations for each shape. Each of the 3 functions should ask for the necessary information 
# (e.g. lengths and/or angles and output the answer.


import tkinter as tk
from tkinter import ttk
import math
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.title("8/Dec/2023 Calculating Area")
root.geometry("650x450")
root.resizable(0,0)

script_directory = os.path.dirname(os.path.realpath(__file__))
img = Image.open(os.path.join(script_directory, "shapesbg.jpg"))

# Resize the image to fit the dimensions of the root window
img = img.resize((650, 450), Image.BICUBIC)

tk_img = ImageTk.PhotoImage(img)

# Creating a label which contains the image and placing it as a background
background_label = tk.Label(root, image=tk_img)
background_label.place(relwidth=1, relheight=1)



def take_entry(selected_shape):
    # clearing the previous answers if the user wants to do another calculation
    clear_inputs()

    # checking which button is pressed in each if and elif statements and asking for required inputs
    if selected_shape == "circle":
        # if the user clicks circle it will display a label to type radius
        label1 = tk.Label(ansFrame, text="Enter radius:")
        label1.pack()
        # since circles only need one number, packing one entry only which has been declared outside the function already
        # it will display 1 entry box for the user and be taken as radius
        entrya.pack()

    elif selected_shape == "square":
        # making a label to enter side length for square
        label1 = tk.Label(ansFrame, text="Enter side length:")
        # displaying the label
        label1.pack()
        # since only one number is required I will display just one entry to the user to be taken as the side length of a square
        entrya.pack()

    elif selected_shape == "rectangle":
        # two numbers are required for this shape, so I will display 2 labels and pack the 2 pre-defined entries to take 2 inputs from the user
        # making a label for the first number
        label1 = tk.Label(ansFrame, text="Enter height:")
        # displaying the label for height
        label1.pack()
        # displaying entrya too take the first input from the user to take as height
        entrya.pack()
        # making a label for the second number
        label2 = tk.Label(ansFrame, text="Enter width:")
        # displaying the second label
        label2.pack()
        # displaying the second entry to take the second input as width
        entryb.pack()

    elif selected_shape == "triangle":
        # two numbers are required for this shape, so I will display 2 labels and pack the 2 pre-defined entries to take 2 inputs from the user
        # making a label for the first number
        label1 = tk.Label(ansFrame, text="Enter height:")
        # displaying the label for height
        label1.pack()
        # displaying entrya too take the first input from the user to take as height
        entrya.pack()
        # making a label for the second number
        label2 = tk.Label(ansFrame, text="Enter base:")
        # displaying the second label
        label2.pack()
        # displaying the second entry to take the second input as base
        entryb.pack()

    # a calculation button will appear for the user to press after filling all the entries
    calcbtn = tk.Button(ansFrame, text="Calculate", command=lambda: calc_area(selected_shape))
    calcbtn.pack(pady=10)

def is_entry_empty():
    # checking if entry a or entry b is typed
    if entrya.get() == "" or entryb.get() == "":
        # the reason I wrote or instead of and is because then the circle and square won't work
        # because it requires only 1 input from the user
        # however it will still work with a rectangle if the user types in only one entry
        # it will still display the message to fill all required entries in order to calculate the area
        result_label.config(text="Please fill all the required entry with numbers", bg="#FF7E7E") 
        result_label.pack()
        # after 3000 ms which is 3 seconds it will clear the result label
        ansFrame.after(3000, clear_result_label)

def clear_result_label():
    # text being nothing
    result_label.config(text="", bg="#4B89AC")
    result_label.pack_forget()


def calc_area(selected_shape):
    # checking for errors with this function to add error handling
    is_entry_empty()
    if selected_shape == "circle":
        # taking user entry and calculating the area
        area = math.pi * float(entrya.get())**2
        # displaying the answer in result
        result_label.config(text=f"Area: {area}", bg="lightgreen")
        # packing the result label to display in ansFrame
        result_label.pack()
    elif selected_shape == "square":
        area = float(entrya.get())**2
        result_label.config(text=f"Area: {area}", bg="lightgreen")
        result_label.pack()
    elif selected_shape == "rectangle":
        area = float(entrya.get()) * float(entryb.get())
        result_label.config(text=f"Area: {area}", bg="lightgreen")
        result_label.pack()
    elif selected_shape == "triangle":
        area = 0.5 * float(entrya.get()) * float(entryb.get())
        result_label.config(text=f"Area: {area}", bg="lightgreen")
        result_label.pack()

def clear_inputs():
    # using a for loop to select all widgets inside the ansFrame and unpack them or forget them to clear it
    for widget in ansFrame.winfo_children():
        widget.pack_forget()
    # removing the result label from the display
    result_label.pack_forget()


rootframe = tk.Frame(root, pady=20, padx=20)
rootframe.pack(pady=40)

labeltext = tk.Label(rootframe, text="Let's calculate the area of a shape.\nSelect a shape:", fg="purple", font=("Helvetica", 12, "bold"))
labeltext.pack(pady=20)

shape_frame = ttk.Frame(rootframe, style="TFrame")
shape_frame.pack()

shapelist = ["circle", "square", "rectangle", "triangle"]
for index, shapeform in enumerate(shapelist):
    shape_button = tk.Button(shape_frame, text=shapeform, command=lambda s=shapeform: take_entry(s))
    shape_button.grid(row=1, column=index, padx=5, pady=5)

ansFrame = tk.Frame(rootframe)
ansFrame.pack()

entrya = tk.Entry(ansFrame)
entryb = tk.Entry(ansFrame)

result_label = tk.Label(ansFrame, text="")
result_label.pack()

root.mainloop()