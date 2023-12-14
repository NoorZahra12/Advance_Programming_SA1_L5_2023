# Exercise 1: User information ☑️
# Develop a GUI App to create a file called bio.txt and write the following information to the file asking user 
# to enter the values: Name Age Hometown Each piece of data should be on a new line Once the data has been written 
# to the file, read the data from the file and output the data.    


# importing library
import tkinter as tk
from tkinter import messagebox

# making window
root = tk.Tk()
root.title("6/Dec/2023 User Information App")
# storing color in a variable
bgcolor = "#d2f5e3"
root.configure(bg = bgcolor)

# making function for save button
def save_to_file():
    # getting entry data and storing in variables
    name = entry_name.get()
    age = entry_age.get()
    hometown = entry_hometown.get()

    # w is to write in the bio.txt file
    file = open("bio.txt", "w")
    # this is what will be written in the file using the variables which stored user's entry data
    file.write(f"Name: {name}\nAge: {age}\nHometown: {hometown}\n")
    # closing file
    file.close()

# making function for read button
def read_from_file():
    file = open("bio.txt", "r")
    content = file.read()
    file.close()
    messagebox.showinfo("User Information", content)

# asking user to type name
label_name = tk.Label(root, text="Enter Name:", bg=bgcolor)
label_name.pack(pady=10)
# getting user input
entry_name = tk.Entry(root)
entry_name.pack()
# asking user age
label_age = tk.Label(root, text="Enter Age:", bg=bgcolor)
label_age.pack()
# taking user entry
entry_age = tk.Entry(root)
entry_age.pack()
# hometown
label_hometown = tk.Label(root, text="Enter Hometown:", bg=bgcolor)
label_hometown.pack()
entry_hometown = tk.Entry(root)
entry_hometown.pack()

# making frame for 2 buttons
button_frame = tk.Frame(root, bg=bgcolor)
button_frame.pack()
# packing the 2 buttons in frame
save_button = tk.Button(button_frame, text="Save", command=save_to_file, bg="#66cc22", fg="white")
save_button.pack(side=tk.LEFT, pady=10, padx=5)
read_button = tk.Button(button_frame, text="Read", command=read_from_file, bg="#44aa88", fg="white")
read_button.pack(side=tk.LEFT, pady=10, padx=5)

root.geometry("300x200")
root.mainloop()