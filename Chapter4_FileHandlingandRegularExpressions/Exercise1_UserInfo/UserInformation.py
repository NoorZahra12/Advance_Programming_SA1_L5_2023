# Exercise 1: User information ☑️
# Develop a GUI App to create a file called bio.txt and write the following information to the file asking user 
# to enter the values: Name Age Hometown Each piece of data should be on a new line Once the data has been written 
# to the file, read the data from the file and output the data.    


import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("6/dec/2023 User Information App")

def save_to_file(self):
    name = entry_name.get()
    age = entry_age.get()
    hometown = entry_hometown.get()

    try:
        with open("bio.txt", "w") as file:
            file.write(f"Name: {name}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Hometown: {hometown}\n")

        messagebox.showinfo("Success", "Data saved to bio.txt")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def read_from_file(self):
    try:
        with open("bio.txt", "r") as file:
            content = file.read()
        messagebox.showinfo("User Information", content)
    except FileNotFoundError:
        messagebox.showwarning("File Not Found", "bio.txt not found. Save data first.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")




label_name = tk.Label(root, text="Name:")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label_age = tk.Label(root, text="Age:")
label_age.pack()

entry_age = tk.Entry(root)
entry_age.pack()

label_hometown = tk.Label(root, text="Hometown:")
label_hometown.pack()

entry_hometown = tk.Entry(root)
entry_hometown.pack()

save_button = tk.Button(root, text="Save", command=save_to_file)
save_button.pack()

read_button = tk.Button(root, text="Read", command=read_from_file)
read_button.pack()


root.geometry("300x200")
root.mainloop()
