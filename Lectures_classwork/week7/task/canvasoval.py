#import tkinter module
import tkinter as tk

#Creates the output window
root = tk.Tk()
root.title("drawing an oval")
root.geometry("400x400")

#making a canvas widget
canvas= tk.Canvas(root, height=400, width=400,bg='black')

#TASK: 
#fill=red, 
# width = 2, 
#x1:50 y1:70 x2:100 y2:70
oval= canvas.create_oval(170,180,300,310, fill="red",outline='white',width=2)
canvas.pack()
root.mainloop()