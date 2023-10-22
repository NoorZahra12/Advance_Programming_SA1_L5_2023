# Write Python Program to Count the Number of Times an Item Appears in the List
# staff = ["Arshiya", "Usman", "Iftikhar", "Usman","Rafia", "Mary", "Anmol","Zainab","Iftikhar", "Arshiya","Rafia","Jake"]
# (Hint: For each item in the list consider it as a key, and the number of times these items appear will be its associated value)



staff = ["Arshiya", "Usman", "Iftikhar", "Usman", "Rafia", "Mary", "Anmol", "Zainab", "Iftikhar", "Arshiya", "Rafia", "Jake"]

# Initialize an empty dictionary with default values of 0
staff_dictionary = {item: 0 for item in staff}

# Count the occurrences of each item and increasing the value of key by 1 in the the dictionary
for item in staff:
    staff_dictionary[item] += 1

#displaying the dictionary using for loop
for name, count in staff_dictionary.items():
    print(name,count)