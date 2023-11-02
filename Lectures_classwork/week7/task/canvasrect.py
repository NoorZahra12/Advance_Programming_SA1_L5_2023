#import tkinter module
import tkinter as tk

#Creates the output window
root = tk.Tk()
root.title("drawing a  line")
root.geometry("400x400")

#making a canvas widget
canvas= tk.Canvas(root, height=400, width=400)

rect1= canvas.create_rectangle(70,80,100,110,fill="yellow")
canvas.pack()
root.mainloop()