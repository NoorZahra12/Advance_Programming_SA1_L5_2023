# Import necessary modules
import tkinter as tk
from tkinter import ttk
import math
from PIL import Image, ImageTk
import os

# Function to calculate the area of a shape
def calculate_area(shape_name, entries, ans_frame, result_label):
    # Check if any entry is empty
    def is_entry_empty():
        for entry in entries:
            if entry.get() == "":
                result_label.config(text="Please fill all the required entries with numbers", bg="#FF7E7E")
                result_label.pack()
                ans_frame.after(3000, clear_result_label)
                return True
        return False

    # Clear the result label
    def clear_result_label():
        result_label.config(text="", bg="#4B89AC")
        result_label.pack_forget()

    # Clear all input widgets
    def clear_inputs():
        for widget in ans_frame.winfo_children():
            widget.pack_forget()
        result_label.pack_forget()

    # Calculate and display the area
    def calc_area():
        if not is_entry_empty():
            try:
                if shape_name == "Circle":
                    area = math.pi * float(entries[0].get())**2
                elif shape_name == "Rectangle":
                    area = float(entries[0].get()) * float(entries[1].get())
                elif shape_name == "Triangle":
                    area = 0.5 * float(entries[0].get()) * float(entries[1].get())
                else:
                    return

                result_label.config(text=f"{shape_name} Area: {area}", bg="lightgreen")
                result_label.pack()
            except ValueError:
                result_label.config(text="Invalid input. Please enter valid numbers.", bg="#FF7E7E")
                result_label.pack()
                ans_frame.after(3000, clear_result_label)

    # Clear existing inputs and result labels
    clear_inputs()

    # Create appropriate labels and entry widgets based on the shape
    if shape_name == "Circle":
        label1 = tk.Label(ans_frame, text="Enter radius:")
    elif shape_name == "Rectangle":
        label1 = tk.Label(ans_frame, text="Enter height:")
        label2 = tk.Label(ans_frame, text="Enter width:")
    elif shape_name == "Triangle":
        label1 = tk.Label(ans_frame, text="Enter height:")
        label2 = tk.Label(ans_frame, text="Enter base:")
    else:
        return

    label1.pack()
    entry1 = tk.Entry(ans_frame)
    entry1.pack()
    entries.append(entry1)

    # Add a second entry widget for Rectangle and Triangle shapes
    if shape_name == "Rectangle" or shape_name == "Triangle":
        label2.pack()
        entry2 = tk.Entry(ans_frame)
        entry2.pack()
        entries.append(entry2)

    # Create a button to trigger the area calculation
    calc_btn = tk.Button(ans_frame, text="Calculate", command=calc_area, bg="purple", fg="white")
    calc_btn.pack(pady=10)

    # Result label is now part of ans_frame
    result_label = tk.Label(ans_frame, text="")
    result_label.pack()

# Create the main Tkinter window
root = tk.Tk()
root.title("8/Dec/2023 Calculating Area")
root.geometry("800x450")

# Load and resize the background image
script_directory = os.path.dirname(os.path.realpath(__file__))
img = Image.open(os.path.join(script_directory, "shapesbg.jpg"))
img = img.resize((800, 450), Image.BICUBIC)
tk_img = ImageTk.PhotoImage(img)

# Creating a label which contains the image and placing it as a background
background_label = tk.Label(root, image=tk_img)
background_label.place(relwidth=1, relheight=1)

# Create a frame for the main content
root_frame = tk.Frame(root, padx=20, pady=20)
root_frame.pack(pady=60)

# Create a label for the instruction text
label_text = tk.Label(root_frame, text="Let's calculate the area of a shape.\nSelect a shape:", fg="purple", font=("Helvetica", 12, "bold"))
label_text.pack(pady=20)

# Create a Notebook for tabbed interface
notebook = ttk.Notebook(root_frame)

# Create tabs for each shape
shape_list = ["Circle", "Rectangle", "Triangle"]
for shape_name in shape_list:
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=shape_name)

    entries = []
    ans_frame = tab
    result_label = tk.Label(ans_frame, text="")
    result_label.pack()

    calculate_area(shape_name, entries, ans_frame, result_label)

# Pack the Notebook
notebook.pack(expand=True, fill='both')

# Result label now belongs to the root_frame
result_label = tk.Label(root_frame, text="")
result_label.pack()

# Start the Tkinter event loop
root.mainloop()
