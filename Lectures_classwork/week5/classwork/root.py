#import tkinter module
from tkinter import *

#Creates the output window
root = Tk()
root.title("Widget Example")

#creating a label widget
mylabel = Label(root, text="I am a label widget")
mylabel.pack(side=TOP) #displaying the label on the top

mybutton = Button(root, text="I am a button")
mybutton.pack()

root.geometry('350x200')
root.mainloop()