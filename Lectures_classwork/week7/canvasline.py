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
line= canvas.create_line(50,70,100,70, fill="red",width=2)
canvas.pack()
root.mainloop()