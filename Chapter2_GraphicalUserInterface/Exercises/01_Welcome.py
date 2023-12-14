# Exercise 1: Welcome ☑️
# Develop a GUI program to do the following using the tkinter module

# /create a label to display the welcome message and change the label font style (font name, bold, size)
# /Set the default window size
# /Disable resizing the window
# /Add background color to the Window.

import tkinter as tk
root=tk.Tk()
root.geometry("300x200")
root.title("31/oct/2023")

# making label to display text
label = tk.Label(root,text="Hello World!", font=("Arial", 16, "bold"),pady=60,bg="pink")
# displaying in window by packing it
label.pack()
# root can't be resized
root.resizable(0,0)
# adding bg to root
root.configure(bg="pink")
# running the mainlopp to run the window
root.mainloop()