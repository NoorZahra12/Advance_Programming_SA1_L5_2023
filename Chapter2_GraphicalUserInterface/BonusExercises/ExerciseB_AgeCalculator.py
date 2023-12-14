# Exercise B: Age Calculator
# Create a program to take input of the user's date of birth and output the age. 
# Expected input: 8/5/2018 
# Expected output: Your age is 5 years 
# Hint: you can use the date from datetime package to get today's date

import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("Age Calculator")
root.geometry("350x200")

def calculate_age():
    # storing today's date in a variable
    today = datetime.today()
    # storing user's birthdate in variable by getting from entry
    user_birthday_string = entry.get()
    # converting string into date object
    user_birthdate = datetime.strptime(user_birthday_string, "%d/%m/%Y")
    # calculating the user's age in years
    user_ageyear = today.year - user_birthdate.year
    # well now we know the user's age in years but just to be more precise of the user's age
    # let's check the the month and date part ofthe user to be more precise with the answer

    # if today's month and date is the same as user's birthday
    if (today.month, today.day) == (user_birthdate.month, user_birthdate.day):
        # if statement is true, it is the user's birthday
        result.set("Happy Birthday!!\nYour age is now {}".format(user_ageyear))
    # checking if current month and date is earlier than user's birth month and date
    elif (today.month, today.day) > (user_birthdate.month, user_birthdate.day):
        # if the statement is true, it means user has yet to complete the year
        # in other words, user did not celebrate his birthday yet so subtracting his age by 1
        incompleteyear = user_ageyear - 1
        # displaying result of the user's age if user has not passed birthday
        result.set("Your age is {}\n you will be {} by the end of this year".format(incompleteyear, user_ageyear))
    # if the user has passed his birth month and date it means he completed the year 
    # and no subtraction is needed
    else:
        # displaying result of the user's age if user has passed his birthday
        result.set("Your age is {}".format(user_ageyear))

# text label widget
label = tk.Label(root, text="Enter birth date (DD/MM/YYYY):")
label.pack(pady=20)
# entry widget for user to type
entry = tk.Entry(root, width=20)
entry.pack()
# submit button to calculate the age
button = tk.Button(root, text="Calculate my age", command=calculate_age)
button.pack(pady=15)

result = tk.StringVar()
# result label where it shows the user's age
resultLabel = tk.Label(root, textvariable=result)
resultLabel.pack()

root.mainloop()
