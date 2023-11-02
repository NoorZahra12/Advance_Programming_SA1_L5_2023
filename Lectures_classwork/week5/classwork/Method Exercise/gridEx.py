#import tkinter module
from tkinter import *

#Creates the window
main = Tk()
main.title("using grid()")

# this will create a label widget
label1 = Label(main, text = "A")
label2 = Label(main, text = "B")
 
# grid method to arrange labels in respective
# rows and columns as specified

#this will be displayed in first row 
#in the west which is on the left side
label1.grid(row = 0, column = 0, sticky = W, pady = 2)
#this will be displayed in second row
label2.grid(row = 1, column = 0, sticky = W, pady = 2)
 
main.mainloop()