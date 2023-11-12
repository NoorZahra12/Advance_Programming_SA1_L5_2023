# Exercise 2: Managing Layout ☑️
# Exercise 2 a: Using pack ☑️
# Create a GUI with 4 labels using the pack() geometry as shown in the below images. 
# The first image on the left shows the original display and the second image on right 
# shows what happens when the window is resized.

# Additional information
# Arguments values for many widgets, including Frames for Borders and Background

# bd is used for border width. For example bd=5
# Relief is used for border-style values are FLAT, RAISED, 
# GROOVE, SUNKEN, and RIDGE. For example relief=RAISED
# bg is used for background color.For example bg="white" or bg="#FFFFFF".
# Pack arguments

# Fill: Fill the space with the widget, Values are Y, X, BOTH. For example fill=Y
# Expand: The size of the button is expanded if the window is maximized. Values are 0,1, 
# any number, YES, NO. For example expand=0 (default) no expansion

import tkinter as tk
root=tk.Tk()
root.geometry("200x100")
root.title("11/nov/2023")

label1 = tk.Label(root,text="A", background="red", bd=5)
label2 = tk.Label(root,text="B", background="blue")
label3 = tk.Label(root,text="C", background="white")
label4 = tk.Label(root,text="D", background="yellow")

label1.pack(side="top", fill=tk.X, expand=True)
label2.pack(side="bottom")
label3.pack(side="left",fill=tk.Y, expand=True)
label4.pack(side="right")

root.mainloop()