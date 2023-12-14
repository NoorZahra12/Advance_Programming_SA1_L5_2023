# Exercise 1: User information ☑️
# Develop a GUI App to create a file called bio.txt and write the following information to the file asking user 
# to enter the values: Name Age Hometown Each piece of data should be on a new line Once the data has been written 
# to the file, read the data from the file and output the data.    

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("6/Dec/2023 User Information App")

bgcolor = "#d2f5e3"
root.configure(bg = bgcolor)


def save_to_file():
    name = entry_name.get()
    age = entry_age.get()
    hometown = entry_hometown.get()

    file = open("bio.txt", "w")
    file.write(f"Name: {name}\nAge: {age}\nHometown: {hometown}\n")
    file.close()

def read_from_file():
    file = open("bio.txt", "r")
    content = file.read()
    file.close()
    messagebox.showinfo("User Information", content)


label_name = tk.Label(root, text="Enter Name:", bg=bgcolor)
label_name.pack(pady=10)

entry_name = tk.Entry(root)
entry_name.pack()

label_age = tk.Label(root, text="Enter Age:", bg=bgcolor)
label_age.pack()

entry_age = tk.Entry(root)
entry_age.pack()

label_hometown = tk.Label(root, text="Enter Hometown:", bg=bgcolor)
label_hometown.pack()

entry_hometown = tk.Entry(root)
entry_hometown.pack()

button_frame = tk.Frame(root, bg=bgcolor)
button_frame.pack()

save_button = tk.Button(button_frame, text="Save", command=save_to_file, bg="#66cc22", fg="white")
save_button.pack(side=tk.LEFT, pady=10, padx=5)

read_button = tk.Button(button_frame, text="Read", command=read_from_file, bg="#44aa88", fg="white")
read_button.pack(side=tk.LEFT, pady=10, padx=5)

root.geometry("300x200")
root.mainloop()