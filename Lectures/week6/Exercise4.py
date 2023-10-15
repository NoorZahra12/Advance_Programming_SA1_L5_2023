from tkinter import*
main= Tk()
main.title("GUI Example 2")
b1=Label(main, text="A", width=12, bg='red', relief=GROOVE,bd=5)
b2=Label(main, text="B", width=12, bg='yellow')
b3=Label(main, text="C", width=12, bg='blue')
b4=Label(main, text="D", width=12, bg='white')

b1.pack(side=TOP, fill=X, expand=1)
b2.pack(side=BOTTOM)
b3.pack(side=LEFT, fill=Y, expand=1)
b4.pack(side=RIGHT)

main.mainloop()