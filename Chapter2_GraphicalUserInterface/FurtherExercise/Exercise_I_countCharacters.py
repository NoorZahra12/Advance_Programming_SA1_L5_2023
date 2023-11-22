# Exercise I: Count characters
# Develop a GUI to count the number of vowels and consonants in the given string. 
# Ask the user to enter the string 
# For example Enter a word: hello world 
# Total number of letters: 11 Number of vowels: 3 Number of consonants: 7 Number of special characters: 1

import tkinter as tk

root = tk.Tk()
root.title('14/nov/2023 Temperature Converter')
root.geometry("400x200")

def characterCount():
    user_string = str(user_input.get())
    letter = 0
    alphabets = 0
    vowel = "aeiou"
    vowel_count = 0
    consonant = 0
    special = 0
    for character in user_string:
        letter+=1
        if character.isalpha():
            alphabets+=1
        elif character.lower() in vowel:
            vowel_count+=1
        elif character.lower() not in vowel:
            consonant+=1
        elif not character.isalpha():
            special+=1
        result.set("Total number of letters: {}\nNumber of vowels: {3}\nNumber of consonants: {7}\nNumber of special characters: {1}")
    

wordLabel = tk.Label(root, text="Enter a word: ")

user_input = tk.StringVar()
wordEntry = tk.Entry(root, textvariable=user_input)

result = tk.StringVar()
resultLabel = tk.Label(root, textvariable=result)
resultLabel.pack()