#import tkinter module
import tkinter as tk

#Creates the output window
root = tk.Tk()
root.title("drawing a  line")
root.geometry("400x400")

#making a canvas widget
canvas= tk.Canvas(root, height=400, width=400)

#TASK: 
#fill=red, 
# width = 2, 
#x1:50 y1:70 x2:100 y2:70
rect1= canvas.create_rectangle(5,5,30,30, fill="red",outline="black",width=1)
rect1= canvas.create_rectangle(200,50,30,200, fill="red",outline="black",width=2)
rect1= canvas.create_rectangle(350,150,400,200, fill="red",outline="black",width=2,dash=(5,5))
canvas.pack()
root.mainloop()