# Exercise 4: Draw Shape☑️
# Using tkinter module develop Gui to ask the user to select shapes like oval, rectangle, square, and triangle and 
# draw the shape using canvas.  

# Extension
# Ask the user to input the coordinate values of the selected option

import tkinter as tk
from tkinter.ttk import Combobox

def draw_shape(shape, coordinates):
    if shape == "oval":
        canvas.create_oval(coordinates, outline="black")
    elif shape == "rectangle":
        canvas.create_rectangle(coordinates, outline="black")
    elif shape == "square":
        canvas.create_rectangle(coordinates, outline="black")
    elif shape == "triangle":
        canvas.create_polygon(coordinates, outline="black")

def update_coordinates_label(*args):
    shape = shape_var.get()

    if shape == "Select Shape":
        coordinates_label.config(text="Enter Coordinates:")
    elif shape == "triangle":
        coordinates_label.config(text="Enter coordinates for triangle (x1 y1 x2 y2 x3 y3):")
    else:
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
    canvas.delete("all")  # Deletes all items on the canvas

# Create the main window
root = tk.Tk()
root.title("Shape Drawer")

# Shape selection
shapes = ["Select Shape", "oval", "rectangle", "square", "triangle"]
shape_var = tk.StringVar()
shape_var.set(shapes[0])  # Default to "Select Shape"
shape_var.trace_add("write", update_coordinates_label)

shape_label = tk.Label(root, text="Select Shape:")
shape_label.pack(pady=10)

shape_combobox = Combobox(root, textvariable=shape_var, values=shapes)
shape_combobox.pack()

# Create canvas
canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=10)

# Coordinates entry
coordinates_label = tk.Label(root, text="Enter Coordinates:")
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
