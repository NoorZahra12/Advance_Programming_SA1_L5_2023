# The file sentences.txt has a list of string data. Develop a GUI root that finds out how many times the following string rootears

# Hello my name is Peter Parker
# I love Python Programming
# Love
# Enemy  

import tkinter as tk
import os

# Define color palette
bgcolor = "#ffa522"  # orange
button_color = "#ed5d66"  # pinkish

def count_occurrences(content, target):
    return {string: content.lower().count(string.lower()) for string in target}

def update_results():
    search_string = search_entry.get()
    if search_string:
        target_search = target + [search_string]
    else:
        target_search = target
    occurrences = count_occurrences(content, target_search)

    for label in result_sentences:
        label.destroy()

    # Display results for the four target strings
    for string in target:
        count = occurrences.get(string, 0)
        result_str = f"{string}: {count} occurrences"
        result_sentence = tk.Label(root, text=result_str, bg=bgcolor)
        result_sentence.pack(pady=5)
        result_sentences.append(result_sentence)

    # Display result for the custom search string
    if search_string:
        count = occurrences.get(search_string, 0)
        result_str = f"{search_string}: {count} occurrences"
        result_sentence = tk.Label(root, text=result_str, bg=button_color)
        result_sentence.pack(pady=5)
        result_sentences.append(result_sentence)

# Set up the main window
root = tk.Tk()
root.title("9/dec/2023 String Counter")
root.geometry("400x300")
root.configure(bg=bgcolor)

# Read file content
script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "sentences.txt")

with open(file_path, 'r') as file:
    content = file.read()

# Strings to search for
target = [
    "Hello my name is Peter Parker",
    "I love Python Programming",
    "Love",
    "Enemy"
]

# Widgets for search and results
search_label = tk.Label(root, text="Search a word", bg=bgcolor, fg="red", font=("Arial", 12))
search_label.pack(pady=5)

search_entry = tk.Entry(root, width=30)
search_entry.pack(pady=5)

search_button = tk.Button(root, text="Search", command=update_results, bg=button_color)
search_button.pack(pady=5)

# List to store result labels
result_sentences = []

# Display initial results for the four target strings
update_results()

# Start the main loop
root.mainloop()
