# Exercise 1: Woof Woof ☑️
# Develop a GUI using Tkinter with a class that defines the characteristics of a dog. 
# The program should instantiate two objects from this class and assign data to its members. 
# The program should then output the data from each object and the oldest dog should woof via a class method.

import tkinter as tk
# creaing a class for Dogs
class Dog:
    # Class variable to keep track of the oldest dog
    oldest_dog = None

    def __init__(self, name, breed, Birthyear):
        self.name = name
        self.breed = breed
        self.Birthyear = Birthyear

        # Check if this dog is the oldest
        if Dog.oldest_dog is None or self.calculate_age() > Dog.oldest_dog.calculate_age():
            Dog.oldest_dog = self

    def calculate_age(self):
        current_year = 2023  # Set the current year manually or use another method to get the current year
        return current_year - self.Birthyear

    @classmethod
    def woof_oldest(cls):
        if cls.oldest_dog:
            return f"{cls.oldest_dog.name} (Breed: {cls.oldest_dog.breed}) says: Woof!"
        else:
            return "No dogs have been instantiated yet."

# Create instances of the Dog class
dog1 = Dog("Buddy", "Labrador Retriever", 2010)
dog2 = Dog("Max", "German Shepherd", 2015)

# Tkinter GUI
root = tk.Tk()
root.title("Dog Information")

# Display information for dog1
label_dog1 = tk.Label(root, text=f"{dog1.name} ({dog1.breed}), Age: {dog1.calculate_age()} years")
label_dog1.pack(pady=10)

# Display information for dog2
label_dog2 = tk.Label(root, text=f"{dog2.name} ({dog2.breed}), Age: {dog2.calculate_age()} years")
label_dog2.pack(pady=10)

# Button to make the oldest dog woof
oldestbtn = tk.Button(root, text="Woof Oldest Dog", command=lambda: result.config(text=Dog.woof_oldest()))
oldestbtn.pack(pady=10)

# result label for woof message
result = tk.Label(root, text="")
result.pack(pady=10)

root.mainloop()