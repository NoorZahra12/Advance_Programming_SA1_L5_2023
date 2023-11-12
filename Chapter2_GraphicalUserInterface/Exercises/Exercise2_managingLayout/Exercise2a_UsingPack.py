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
root.title("11/nov/2023")
#  Borders: flat, groove, raised, ridge, solid, or sunken
#padx meanig to add padding in the x axis(horizontal axis)
labelA = tk.Label(root,text="A", relief="groove", background="red", padx=30 , bd=5)
labelB = tk.Label(root,text="B", relief="raised", background="yellow", padx=30, bd=3)
labelC = tk.Label(root,text="C", background="blue", padx=30 )
labelD = tk.Label(root,text="D", background="white", padx=30 )

#displaying the labels inside the window using pack
labelA.pack(side="top", fill=tk.X, expand=True)
labelB.pack(side="bottom")
labelC.pack(side="left",fill=tk.Y, expand=True)
labelD.pack(side="right")

#displaying the window with mainloop
root.mainloop()