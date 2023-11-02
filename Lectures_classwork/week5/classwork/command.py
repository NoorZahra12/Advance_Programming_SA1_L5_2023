import tkinter as tk

root = tk.Tk()


def button_clicked():
    print('You have clicked the button')


button = tk.Button(root, text='Click Me', command=button_clicked)
button.pack()

root.mainloop()
