# Exercise A: Playing around in class - Extension
# In the above Exercise -Playing around in class ask the user to enter the values of the Animal  

# Importing libraries
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

# making a class for animals
class Animal:
    def __init__(self, type, name, colour, age, weight, noise):
        self.type = type
        self.name = name
        self.colour = colour
        self.age = age
        self.weight = weight
        self.noise = noise

    # making 3 functions for 3 buttons
    def sayHello(self):
        return f"Hello, I'm {self.name} the {self.type}!"

    def makeNoise(self):
        return f"{self.name} says: {self.noise}"

    def animalDetails(self):
        return f"Type: {self.type}\nName: {self.name}\nColour: {self.colour}\nAge: {self.age}\nWeight: {self.weight}\nNoise: {self.noise}"

# making a function for changing the answer label's text with a certain message
def display_answer(answer_label, message):
    answer_label.config(text=message)

# making a  function for making a new tab when user clicks button
def add_animal():
    # getting all the user inputs about the animal's information from the entries
    animal_type = animal_type_entry.get()
    name = name_entry.get()
    colour = colour_entry.get()
    age = age_entry.get()
    weight = weight_entry.get()
    noise = noise_entry.get()
    # using class and adding the animal's attributes from user
    new_animal = Animal(animal_type, name, colour, age, weight, noise)
    # making a tab in notebook
    tab = ttk.Frame(notebook, style='TFrame')
    notebook.add(tab, text=new_animal.name)

    # making a frame which will contain the 3 buttons
    btn3frame = tk.Frame(tab, bg="#bce8e5")
    btn3frame.pack(side="top", pady=10)
    # this label will display a text based on what button user clicks out of the 3 buttons available
    answer_label = tk.Label(tab, text="", pady=10, bg="#bce8e5")
    answer_label.pack()

    # Making 3 buttons and using lamba functions to call function based on animal's name
    greetbtn = tk.Button(btn3frame, text="Greet", command=lambda a=new_animal, label=answer_label: display_answer(label, a.sayHello()), bg="#ff4444", fg="white")
    greetbtn.pack(side=tk.LEFT, padx=10)
    noisebtn = tk.Button(btn3frame, text="Make Noise", command=lambda a=new_animal, label=answer_label: display_answer(label, a.makeNoise()), bg="#ff4444", fg="white")
    noisebtn.pack(side=tk.LEFT, padx=10)
    detailsbtn = tk.Button(btn3frame, text="Animal Details", command=lambda a=new_animal, label=answer_label: display_answer(label, a.animalDetails()), bg="#ff4444", fg="white")
    detailsbtn.pack(side=tk.LEFT, padx=10)

    # when user clicks the add new animal tab button all the entries will become empty
    animal_type_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    colour_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    noise_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Chapter 5 Bonus")
root.geometry("550x330")
# setting the background color
root.configure(bg="#bce8e5")


# adding an image at the bg
# i couldn't use the image normally so im using import os to make a path and find the image file to be able to use it
bg_image_path = os.path.join(os.path.dirname(__file__), "petbg.jpg")
original_bg_image = Image.open(bg_image_path)
resized_bg_image = ImageTk.PhotoImage(original_bg_image.resize((550, 330), Image.BICUBIC))
bg_label = tk.Label(root, image=resized_bg_image)
bg_label.place(relwidth=1, relheight=1)
# using style and storing in variable
style = ttk.Style()
# decorating the tab frame and calling it TFrame to use this later in tab frame, reason being i can't use bg or background to add the color there
# so using style to fix that problem
style.configure("TFrame", background="#bce8e5")


# this is the frame which the user need to sill out to make an animal tab
# in this form user will be asked to fill the entries of an Animal and those entries will be used when calling the class
# so whatever attribute is written by user is going to be used when the class is called
form_frame = tk.Frame(root, bg="#bce8e5")
form_frame.pack(side="left", padx=20)

# ANIMAL TYPE
animal_type_label = tk.Label(form_frame, text="Animal Type:", bg="#bce8e5")
animal_type_label.grid(row=0, column=0, padx=5, pady=5)
animal_type_entry = tk.Entry(form_frame)
animal_type_entry.grid(row=0, column=1, padx=5, pady=5)
# ANIMAL NAME
name_label = tk.Label(form_frame, text="Name:", bg="#bce8e5")
name_label.grid(row=1, column=0, padx=5, pady=5)
name_entry = tk.Entry(form_frame)
name_entry.grid(row=1, column=1, padx=5, pady=5)
# COLOUR OF THE ANIMAL
colour_label = tk.Label(form_frame, text="Colour:", bg="#bce8e5")
colour_label.grid(row=2, column=0, padx=5, pady=5)
colour_entry = tk.Entry(form_frame)
colour_entry.grid(row=2, column=1, padx=5, pady=5)
# ANIMAL'S AGE
age_label = tk.Label(form_frame, text="Age:", bg="#bce8e5")
age_label.grid(row=3, column=0, padx=5, pady=5)
age_entry = tk.Entry(form_frame)
age_entry.grid(row=3, column=1, padx=5, pady=5)
# ANIMAL'S WEIGHT
weight_label = tk.Label(form_frame, text="Weight:", bg="#bce8e5")
weight_label.grid(row=4, column=0, padx=5, pady=5)
weight_entry = tk.Entry(form_frame)
weight_entry.grid(row=4, column=1, padx=5, pady=5)
# NOISE OF THE ANIMAL
noise_label = tk.Label(form_frame, text="Noise:", bg="#bce8e5")
noise_label.grid(row=5, column=0, padx=5, pady=5)
noise_entry = tk.Entry(form_frame)
noise_entry.grid(row=5, column=1, padx=5, pady=5)

# add button
add_button = tk.Button(form_frame, text="Add Animal", command=add_animal, bg="#ff4444", fg="white")
add_button.grid(row=6, columnspan=2, pady=10)


# this is a notebook which is stacked to the left like the form. first form will be on the left and this will just be inline next to the formframe
notebook = ttk.Notebook(root)
notebook.pack(side="left", padx=10)

root.mainloop()
