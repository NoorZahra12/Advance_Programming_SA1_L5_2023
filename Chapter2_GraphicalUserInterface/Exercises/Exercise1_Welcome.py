# Exercise 1: Welcome ☑️
# Develop a GUI program to do the following using the tkinter module

# /create a label to display the welcome message and change the label font style (font name, bold, size)
# /Set the default window size
# /Disable resizing the window
# /Add background color to the Window.

import tkinter as tk
root=tk.Tk()
root.geometry("200x200")
root.title("31/oct/2023")

label = tk.Label(root,text="Hello World!", font=("Arial", 16, "bold"))
label.pack()

root.resizable(0,0)

root.configure(bg="pink")

root.mainloop()