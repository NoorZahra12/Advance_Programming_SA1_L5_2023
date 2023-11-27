# Exercise II: Capitalize letters
# Create a GUI that takes input and changes all letters to upper case. 
# hint : Use upper() function

import tkinter as tk

root = tk.Tk()
root.title('27/nov/2023 Capitalizing letters')
root.geometry("400x200")

def LOUD_WORD():
    # getting user input and storing in a variable
    user_string = str(user_input.get())
    new_string = ""
    for character in user_string:
        new_string += character.upper()
    result.set("{}!!!".format(new_string))
    

wordLabel = tk.Label(root, text="Enter a word: ")
wordLabel.pack(pady=10)

user_input = tk.StringVar()
wordEntry = tk.Entry(root, textvariable=user_input)
wordEntry.pack()

submitButton = tk.Button(root, text='Make it loud', command=LOUD_WORD)
submitButton.pack(pady=15)

result = tk.StringVar()
resultLabel = tk.Label(root, textvariable=result)
resultLabel.pack()

root.mainloop()