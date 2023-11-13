# Exercise 3: Login page ☑️
# Create a login page using the Grid geometry.

import tkinter as tk

root = tk.Tk()
root.title("12/nov/2023")
root.geometry("300x200")


def checker():
    # if user types everything correctly
    if username.get() == "user" and user_password.get() == "password":
        submitbtn.config(text="Submitted")
        invalidlabel.pack_forget() #hiding the invalid label if user succesfully submits
    
    # if user types the wrong input
    else:
        submitbtn.config(text="Submit")
        invalidlabel.pack()

welcome = tk.Label(root, text="Welcome Back!", font=("Helvetica", 14)).pack()

# Create a frame
box = tk.Frame(root, pady=20)
box.pack()

# Username
usernamelabel = tk.Label(box, text="Enter username:")
usernamelabel.grid(row=1,column=0)

username = tk.Entry(box)
username.grid(row=1,column=2)

# Password
passwordlabel = tk.Label(box, text="Enter password:")
passwordlabel.grid(row=2,column=0)

user_password = tk.Entry(box, show="*")
user_password.grid(row=2,column=2)

# Invalid label
invalidlabel = tk.Label(root, text="Invalid input", pady=20)

# Submit button
submitbtn = tk.Button(root, text="Submit", command=checker, bg="#22263D", fg="white")
submitbtn.pack()

# Display the window with mainloop
root.mainloop()