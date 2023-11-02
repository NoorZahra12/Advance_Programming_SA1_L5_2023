#import tkinter module
from tkinter import *

#Creates the output window
main = Tk()
main.title("using place()")

# setting geometry of tk window
main.geometry("200x200")

#making a function
def clicked():
    print("You have clicked me \nI am using place() method")
#making a button widget
button1 = Button(main, text = "Click me !", command=clicked)
button1.place(anchor = NE)
 
#making a label widget
label1 = Label(main, text = "I'm a Label")
label1.place(anchor = NW)

main.mainloop()