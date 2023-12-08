import tkinter as tk

root = tk.Tk()
root.title('28/nov/2023 Pop Quiz')
root.geometry("250x120")

# making a function
def clicker():
    # entering a text in the result variable
    result.set("you have clicked a button")


# creating a button that says click me
submitButton = tk.Button(root, text='Click me', command=clicker)
# displaying the button in the app by adding some margin or space outside the widget on the y axis
submitButton.pack(pady=20)

result = tk.StringVar()
resultLabel = tk.Label(root, textvariable=result)
# displaying this label in the app but it is empty for now as there is no text
# when user will click the button in the function it adds a text
resultLabel.pack()

root.mainloop()