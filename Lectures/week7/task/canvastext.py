#import tkinter module
import tkinter as tk

#Creates the output window
root = tk.Tk()
root.title("drawing a  line")
root.geometry("400x400")

#making a canvas widget
canvas= tk.Canvas(root, height=400, width=400)

texts= canvas.create_text(40,30,text="Hello World",font=("Arial",14),fill='green')
canvas.pack()
root.mainloop()