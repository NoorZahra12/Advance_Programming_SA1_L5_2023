# Exercise 4: Draw Shape☑️
# Using tkinter module develop Gui to ask the user to select shapes like oval, rectangle, square, and triangle and 
# draw the shape using canvas.  

# Extension
# Ask the user to input the coordinate values of the selected option

import tkinter as tk
from tkinter.ttk import Combobox

def draw_shape(shape, coordinates):
    # this function takes in the shape selected by user and it's coordinates to draw in the blackboard
    if shape == "oval":
        canvas.create_oval(coordinates, outline="black")
    elif shape == "rectangle":
        canvas.create_rectangle(coordinates, outline="black")
    elif shape == "square":
        canvas.create_rectangle(coordinates, outline="black")
    elif shape == "triangle":
        canvas.create_polygon(coordinates, outline="black")
# function for asking coordinaes
def update_coordinates_label():
    # getting shape selected
    shape = shape_var.get()

    if shape == "Select Shape":
        # this is default msg
        coordinates_label.config(text="Enter Coordinates:")
    elif shape == "triangle":
        # for triangle user needs to type 6 numbers
        coordinates_label.config(text="Enter coordinates for triangle (x1 y1 x2 y2 x3 y3):")
    else:
        # otherwise user will be asked to put 4 numbers
        coordinates_label.config(text=f"Enter coordinates for {shape} (x1 y1 x2 y2):")

def get_coordinates():
    shape = shape_var.get()

    if shape == "Select Shape":
        return

    coordinates_text = coordinates_entry.get()
    if not coordinates_text:
        return

    coordinates = [int(coord) for coord in coordinates_text.split()]

    draw_shape(shape, coordinates)

def clear_canvas():
    # clearing the canvas
    canvas.delete("all")

# Create the main window
root = tk.Tk()
root.title("4/dec/2023 Draw Shape")
root.config(bg="#abcdef")

shapes = ["oval", "rectangle", "square", "triangle"]
shape_var = tk.StringVar()
shape_var.trace_add("write", update_coordinates_label)

shape_label = tk.Label(root, text="Select Shape:", bg="#abcdef")
shape_label.pack(pady=10)

shape_combobox = Combobox(root, textvariable=shape_var, values=shapes)
shape_combobox.pack()

# making a canvas
canvas = tk.Canvas(root, width=300, height=200, bg="green")
canvas.pack(pady=10)

# Coordinates entry
coordinates_label = tk.Label(root, text="Enter Coordinates:", bg="#abcdef")
coordinates_label.pack()

coordinates_entry = tk.Entry(root)
coordinates_entry.pack(pady=10)

# Buttons
draw_button = tk.Button(root, text="Draw Shape", command=get_coordinates)
draw_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear Canvas", command=clear_canvas)
clear_button.pack()

root.geometry("400x450")

# Run the GUI
root.mainloop()
