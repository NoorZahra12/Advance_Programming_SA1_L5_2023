import tkinter as tk
root=tk.Tk()
root.geometry("200x200")
root.title("31/oct/2023")
canvas=tk.Canvas(root,height=200,width=200)
line=canvas.create_line(50,70,100,70, fill="red",width=2)
canvas.pack()
root.mainloop()