#import tkinter module
import tkinter as tk

#Creates the output window
root = tk.Tk()
root.title("drawing a  line")
root.geometry("400x400")

#making a canvas widget
canvas= tk.Canvas(root, height=400, width=400)

image = PhotoImage(file=image.png)
img = canvas.create_image(50,70, anchor='nw',image=image)


canvas.pack()
root.mainloop()