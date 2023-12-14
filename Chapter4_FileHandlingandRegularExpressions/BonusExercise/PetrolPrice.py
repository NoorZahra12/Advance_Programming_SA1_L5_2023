# importing library
import tkinter as tk
import os

def calculate_statistics():
    # using os to get the file and storing in variable
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, "petrolPrice.txt")

    # opening the filee with r to read
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # since there are 2 list in the file i ill have 2 empty ists to store the information or elements in this list from file
    liters_list = []
    cost_list = []

    # using slice method to start from the index 1 and end is nothing so there's no end, it will take all elements available starting from index 1
    for line in lines[1:]:
        # basocaly I'm using the map function storing the elements as liters and cost after a \t in it. so using map() to say the liter and cost is divided by a \t
        # so each line is divided into 2 variable that's split between liters and cost
        liters, cost = map(float, line.split('\t'))
        # appending to the empty lists
        liters_list.append(liters)
        cost_list.append(cost)

    # Calculating cost per liter
    cost_per_liter = [round(cost / liters, 2) for cost, liters in zip(cost_list, liters_list)]

    # Calculating overall average price per liter
    overall_average_price = round(sum(cost_list) / sum(liters_list), 2)

    # Calculating petrol bought at under 3.5 AED per liter
    under_3_5_liters = sum(1 for cost, liters in zip(cost_list, liters_list) if cost / liters < 3.5)

    # Update result labels
    per_l.config(text=f"Cost per liter: {cost_per_liter}")
    average.config(text=f"Overall average price per liter: {overall_average_price}")
    under3_5l.config(text=f"Petrol bought at under 3.5 AED per liter: {under_3_5_liters} liters")


# creating the main Tkinter window
root = tk.Tk()
root.title("Petrol Price Calculator")
root.geometry("300x200")
root.config(bg="skyblue")

# 3 result labels
per_l = tk.Label(root, text="Cost per liter: ",pady=10, bg="skyblue", fg="darkblue")
per_l.pack()
# calculating avg
average = tk.Label(root, text="Average price per liter: ", bg="skyblue", fg="darkblue")
average.pack()

under3_5l = tk.Label(root, text="Petrol bought under 3.5 AED per liter: ",pady=10, bg="skyblue", fg="darkblue")
under3_5l.pack()

# button
calculate_button = tk.Button(root, text="Calculate Statistics", command=calculate_statistics, bg="blue", fg="white")
calculate_button.pack(pady=10)

root.mainloop()