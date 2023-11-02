#import tkinter module
import tkinter as tk

#Creates the output window
root = tk.Tk()
root.title("drawing a  line")
root.geometry("400x400")

#making a canvas widget
canvas= tk.Canvas(root, height=400, width=400, bg='blue')

texts= canvas.create_text(40,30,text="Hello World",font=("Arial",14),fill='green')
rect1= canvas.create_rectangle(70,80,100,110,fill="yellow")
oval= canvas.create_oval(170,180,300,310, fill="red",outline='white',width=2)


canvas.pack()
root.mainloop()