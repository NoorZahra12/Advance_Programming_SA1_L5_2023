#Excerise 2

#I will try to replicate the output as best as i can as in the picture in different file

#importing tkinter module
from tkinter import *

#Creates the output window
main = Tk()
main.title("GUI example exercise 2")

# setting geometry of tk window
main.geometry("400x200")

#making a function
def clicked():
    #changing the text of label
    label1["text"] = "Changed Text"

#making a label widget
label1 = Label(main, text = "Old Text")
label1.pack(side=BOTTOM)

#making a button widget
#callig the function with command when the user will click on this button
button1 = Button(main, text = "Change Text",command=clicked)
button1.pack(side=BOTTOM)


main.mainloop()