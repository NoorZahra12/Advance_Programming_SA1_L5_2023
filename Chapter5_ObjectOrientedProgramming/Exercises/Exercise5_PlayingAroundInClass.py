# Exercise 5: Playing around in class ☑️
# Use this exercise to play around with creating and accessing class members and methods. 
# Develop a GUI using Tkinter to Create a class called Animal

# Give the class at least the following members Type, Name, Colour, Age, Weight, Noise
# The class should have the following methods sayHello() - says its name via print,makeNoise() 
# -make an appropriate noise via print, animalDetails() -output all the details of the animal object
# Instantiate at least two objects from your animal class (e.g. Dog, Cow)
# Set values for each of the variables
# Invoke each of the class functions

# importing all the library
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk 
import os

# making animal class
class Animal:
    # attributes being type of animal, name, colour, age weight and noise
    def __init__(self, animaltype, name, colour, age, weight, noise):
        # storing the attributes in variables
        self.animaltype = animaltype
        self.name = name
        self.colour = colour
        self.age = age
        self.weight = weight
        self.noise = noise

    # animal greeting user
    def sayHello(self):
        return f"Hello, I'm {self.name} the {self.animaltype}!"
    # animal selected making it's respective sound
    def makeNoise(self):
        return f"{self.name} says: {self.noise}"
    # displaying details of the animal selected
    def animalDetails(self):
        return f"Type: {self.animaltype}\nName: {self.name}\nColour: {self.colour}\nAge: {self.age}\nWeight: {self.weight}\nNoise: {self.noise}"


# function for updating the text in answer label
def display_answer(answer_label, message):
    answer_label.config(text=message)


root = tk.Tk()
root.title("Chp5 Ex5 Playing around in class")
root.geometry("500x375")

# setting up a bg image
bg_image_path = os.path.join(os.path.dirname(__file__), "petshopbg.png")
original_bg_image = Image.open(bg_image_path)
resized_bg_image = ImageTk.PhotoImage(original_bg_image.resize((500, 375), Image.BICUBIC))
bg_label = tk.Label(root, image=resized_bg_image)
bg_label.place(relwidth=1, relheight=1)

# just pretend its a petshop where the user interacts with the pets and check the details of the pets
heading = tk.Label(root, text="Welcome to the Pet Shop", font=("Helvetica", 10, "bold"), bg="#CEE3F8", fg="blue")
heading.pack(side="top", pady=30)

# using the class Animal but storing in a list to later on use in a for loop
animals = [
    Animal("Dog", "Bob", "grey", 7, 15, "woof"),
    Animal("Cow", "Daisy", "white and brown", 12, 500, "moo"),
    Animal("Goldfish", "Dori", "gold", 1, 0.1, "blub"),
    Animal("Cat", "Tom", "blue", 5, 8, "meow"),
    Animal("Mouse", "Jerry", "brown", 2, 0.2, "squeak")
]

# creating a notebook for a tabbed interface
notebook = ttk.Notebook(root)

for animal in animals:
    # making a frame called tab which will contain all the buttons and texts
    tab = tk.Frame(notebook, bg="white")
    # adding a new tab for each animal in the animals list and the tab's title is what the name of aimal will be
    notebook.add(tab, text=animal.name)
    # container for buttons
    btnframe = tk.Frame(tab, bg="white")
    btnframe.pack(side="top", pady=10)
    # creating a label to display the answer or the detail of the animals
    answer_label = tk.Label(tab, pady=10, bg="white", fg="darkblue")
    answer_label.pack(pady=5)
    # using lamnba function for the buttons to let each button to say hello, make noise, and display details according to the animal
    # say hello button
    button_hello = tk.Button(btnframe, bg="skyblue", fg="darkblue", text="Greet", command=lambda a=animal, label=answer_label: display_answer(label, a.sayHello()))
    button_hello.pack(side=tk.LEFT, padx=10)
    # noise button
    button_noise = tk.Button(btnframe, bg="skyblue", fg="darkblue", text="Make Noise", command=lambda a=animal, label=answer_label: display_answer(label, a.makeNoise()))
    button_noise.pack(side=tk.LEFT, padx=10)
    # details button
    button_details = tk.Button(btnframe, bg="skyblue", fg="darkblue", text="Animal Details", command=lambda a=animal, label=answer_label: display_answer(label, a.animalDetails()))
    button_details.pack(side=tk.LEFT, padx=10)

# packing the notebook so it displays in the root window
notebook.pack()
# running the mainloop which will listen n run the root window
root.mainloop()