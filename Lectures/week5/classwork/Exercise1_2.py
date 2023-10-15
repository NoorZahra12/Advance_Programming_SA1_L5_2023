#import tkinter module
from tkinter import *

#Creates the output window
main = Tk()
main.title("exercise 1.2")
main.geometry("300x400")

#making a function
def click():
    print("You have clicked the button")

#the button will show a text 'Click here' 
#and when you click it, it will call the click() function in command
Button(main, text='Click here', command=click).pack(side=TOP)
main.mainloop()