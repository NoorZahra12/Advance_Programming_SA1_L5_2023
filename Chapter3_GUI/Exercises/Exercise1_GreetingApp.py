# Exercise 1: Greeting App ☑️
# Develop a GUI to greet the user. The app should have two frames: InputFrame and DisplayFrame.

# In InputFrame, include the following:

# A title label in blue.
# An entry field for the user's name.
# A dropdown menu for selecting a color.
# An "Update Greeting" button.

# In DisplayFrame, include a label to display the personalized greeting.
# Initially, DisplayFrame is empty, when the user clicks the "Update Greeting" button in InputFrame, the personalized greeting should appear in DisplayFrame with the selected color.
# Use different background colors for each frame.



import tkinter as tk
# Import themed Tkinter
from tkinter import ttk 

def updatebtn():
    selected_color = colorvar.get()
    # Updating the greeting text
    result.set(f"Hello {entry_username.get()}!\nYour favorite color is {selected_color}.")
    # Updating the text color in the display frame according to what the user picks
    resultlabel.config(fg=selected_color)
    # Updating the border color in the display frame according to what the user picks
    displayframe.config(highlightbackground=selected_color, highlightcolor=selected_color)


root = tk.Tk()
root.geometry("700x350")
root.title("28/nov/2023")

# making frame
inputframe = tk.Frame(root, bg="#aef", pady=10, border=1, relief="solid", highlightbackground="#004080", highlightcolor="#004080")
inputframe.pack(side="left", expand=1, fill="both", padx=10, pady=10)

# Name
label_title = tk.Label(inputframe, text="Hello user!", fg="blue", font=("Helvetica", 16, "bold"), bg="#aef")
label_title.pack(pady=10)
askinglabel = tk.Label(inputframe, text="What is your good name?", bg="#aef")
askinglabel.pack()
entry_username = tk.Entry(inputframe, bg="#fff") 
entry_username.pack(pady=10)


# color
menuframe = tk.Frame(inputframe, bg="#aef")
menuframe.pack(pady=5)
selectlabel = tk.Label(menuframe, text="Select Color:", pady=5, padx=5, bg="#aef")
selectlabel.pack(side="left")
colorvar = tk.StringVar()
dropdown_color_list = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]


# Style for the Combobox
optionmenu_style = ttk.Style()
optionmenu_style.configure("TCombobox", background="#fff", fieldbackground="#fff", foreground="black", font=("Helvetica", 10))

color_menu = ttk.Combobox(menuframe, textvariable=colorvar, values=dropdown_color_list, style="TCombobox")
colorvar.set(dropdown_color_list[0])
color_menu.pack(side="right")


# button
update_btn = tk.Button(inputframe, text="Update Greeting", command=updatebtn)
update_btn.pack(pady=10)




# DISPLAY FRAME

displayframe = tk.Frame(root, bg="#000", pady=80, border=1, relief="solid")
displayframe.pack(side="right", expand=1, fill="both", padx=10, pady=10)
# result
result = tk.StringVar()
resultlabel = tk.Label(displayframe, textvariable=result, bg="#000")
resultlabel.pack()

root.mainloop()
