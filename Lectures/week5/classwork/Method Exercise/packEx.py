#import tkinter module
from tkinter import *

#Creates the output window
main = Tk()
main.title("using pack()")

#displaying 4 buttons
Button(main, text='A').pack(side=LEFT, expand=YES, fill=Y)
Button(main, text='B').pack(side=TOP, expand=YES, fill=BOTH)
Button(main, text='C').pack(side=RIGHT, expand=YES, fill=NONE, anchor=NE, pady=6)
Button(main, text='D').pack(side=BOTTOM, expand=NO, fill=Y, pady=6)

main.mainloop()