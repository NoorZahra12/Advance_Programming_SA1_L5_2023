from tkinter import*
main = Tk()
main.title("Class Task")
main.geometry("1366x768")

v=StringVar()

def clicked():
    l1["text"] = "Submitted"

l1=Label(main, text="Enter Password:",  bg='yellow')
l1.pack(side=TOP, fill=X)
e1=Entry(main,textvariable=v)
e1.pack(side=TOP)
b1=Button(main, text="Submit", command=clicked,  bg='red')
b1.pack(side=TOP, fill=Y)
r1=Radiobutton(main,text="Male", variable=v,value=1)
r2=Radiobutton(main,text="Female", variable=v,value=2)
# checkbox=Checkbutton(main,text="Remember Me", variable=v, value= TRUE)
# checkbox.pack(side=TOP)

main.resizable(0,0)

main.mainloop()