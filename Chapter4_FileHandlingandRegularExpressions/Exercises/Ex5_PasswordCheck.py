import tkinter as tk

# Set up the main window
root = tk.Tk()
root.title("10/dec/2023 Password Checker")
root.geometry("300x300")

# Global variable to track attempts
attempts_num = 5


def submit_password():
    # Get the password entered by the user
    entered_password = password_entry.get()

    if any(chr.islower() for chr in entered_password) and any(chr.isupper() for chr in entered_password) and any(
            chr.isdigit() for chr in entered_password) and any(chr in "$#@ " for chr in entered_password) and 6 <= len(
        entered_password) <= 12:
        attempts_label.config(text="Success\nPassword is valid!")
        root.after(3000, shut_down)

    else:
        # Update attempts remaining
        global attempts_num

        # Check if attempts are zero
        if attempts_num <= 0:
            attempts_label.config(text="Shutting Down!")
            root.after(3000, shut_down)

        else:
            attempts_num -= 1
            attempts_label.config(text=f"Attempts remaining: {attempts_num}")

def shut_down():
    root.destroy()


# Create and pack widgets
userlabel = tk.Label(root, text="Enter a password:")
userlabel.pack(pady=10)
# User entry
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=10)
# calling function btn
submit_button = tk.Button(root, text="Submit", command=submit_password, bg="#565888", fg="white", padx=10, pady=5,font=("Arial", 9, "bold"))
submit_button.pack(pady=10)
# attempts
attempts_label = tk.Label(root, text=f"Attempts remaining: {attempts_num}")
attempts_label.pack(pady=10)

# Start the main loop
root.mainloop()
