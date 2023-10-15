# from tkinter import*
# root = Tk()
# root.title("GUI Exercise 3")
# root.geometry("200x200")
# def button_clicked():
#     print('You have clicked the button')
# button = Button(root, text='Click Me', command=button_clicked)
# button.pack(side=TOP)
# root.mainloop()


#entry
#button
#label

from tkinter import*

root = Tk()
root.title("GUI Exercise 3")
root.geometry("200x200")

v=StringVar()

def copyTextToLabel():
    print(v.get())
    
l1=Label(root, text="I am a label").pack(side=TOP)
e1=Entry(root,textvariable=v).pack(side=TOP)
b1=Button(root, text="Copy Text", command=copyTextToLabel).pack(side=TOP)
root.mainloop()