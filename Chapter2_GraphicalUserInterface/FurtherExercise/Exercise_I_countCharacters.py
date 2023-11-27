# Exercise I: Count characters
# Develop a GUI to count the number of vowels and consonants in the given string. 
# Ask the user to enter the string 
# For example Enter a word: hello world 
# Total number of letters: 11 Number of vowels: 3 Number of consonants: 7 Number of special characters: 1

import tkinter as tk

root = tk.Tk()
root.title('26/nov/2023 Counting Characters')
root.geometry("400x250")

# making a function to count the letters user entered
def characterCount():
    # getting user input and storing in a variable
    user_string = str(user_input.get())
    # storing vowel letters in a variable
    vowel = "aeiou"
    
    letter = 0
    alphabets = 0
    vowel_count = 0
    consonant = 0
    special = 0
    number = 0

    for character in user_string:
        # for each alphabet or number the variable letter is increased
        letter+=1

        # increasing the alphabet by 1 if character is alphabet
        if character.isalpha():
            alphabets+=1

            # checking for any vowels
            if character.lower() in vowel:
                # increasing vowel by 1 if the statement is true
                vowel_count+=1
            # if it is not a vowel, it is consonant
            else:
                consonant+=1

         # checking if the character is number or not
        elif character.isdigit():
            # increasing number if it is a number
            number+=1
        else:
            special+=1

        result.set("Characters: {}\nAlphabet letters: {}\nVowels: {}\nConsonants: {}\nNumbers: {}\nSpecial characters: {}".format(letter, alphabets, vowel_count, consonant, number, special))
    

wordLabel = tk.Label(root, text="Enter a word: ")
wordLabel.pack(pady=10)

user_input = tk.StringVar()
wordEntry = tk.Entry(root, textvariable=user_input)
wordEntry.pack()

submitButton = tk.Button(root, text='Submit', command=characterCount)
submitButton.pack(pady=15)

result = tk.StringVar()
resultLabel = tk.Label(root, textvariable=result, anchor='w', justify='left')
resultLabel.pack()

root.mainloop()