import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

def calculate_total_price(coffee_type, sugar_level, milk_level, cup_size):
    # setting prices and getting what user picked
    coffee_price_dict = {"Black Coffee": 2.50, "Latte": 3.00, "Espresso": 2.00}
    base_price = coffee_price_dict.get(coffee_type, 0)
    sugar_price_dict = {"None": 0, "Less": -0.25, "Standard": 0, "Extra": 0.25}
    sugar_price = sugar_price_dict.get(sugar_level, 0)
    milk_price_dict = {"None": 0, "Less": -0.25, "Standard": 0, "Extra": 0.25}
    milk_price = milk_price_dict.get(milk_level, 0)
    
    # Add price based on cup size
    cup_size_price_dict = {"Small": 0.25, "Medium": 0.50, "Large": 1.00}
    cup_size_price = cup_size_price_dict.get(cup_size, 0)

    return base_price + sugar_price + milk_price + cup_size_price

def make_receipt():
    # getting user data
    coffee_type = coffee_var.get()
    sugar_level = sugar_var.get()
    milk_level = milk_var.get()
    cup_size = cup_size_var.get()

    total_price = calculate_total_price(coffee_type, sugar_level, milk_level, cup_size)
    receipt_total_price.config(text=f"Total Price: ${total_price:.2f}")

    # Update the order_label with the customized message
    order_message = f"You ordered a {cup_size} cup size {coffee_type.lower()} with {milk_level.lower()} milk and {sugar_level.lower()} sugar."
    order_label.config(text=order_message)

    receipt_frame.pack()

def calc_change():
    cost = float(receipt_total_price.cget("text").split("$")[1])
    change = float(money_entry.get()) - cost
    if change > 0:
        receipt_total_price.config(text="Total Price: $0.00")
        change_label.config(text=f"Change: ${change:.2f}")
        changelabel.config(text="Thank you for buying!\nEnjoy your coffee!")
    else:
        change_label.config(text=f"Insufficient money. Try again")
        changelabel.config(text="")

root = tk.Tk()
root.geometry("900x400")
root.title("Coffee Vending Machine")

# colors
dark_brown = "#2E1A0D"
light_brown = "#D2B48C"
cream = "#FFF5E1"
dark_red = "#4F1B10"




# Input Frame
input_frame = tk.Frame(root, bg=light_brown, pady=10, border=1, relief="solid", highlightbackground=dark_red, highlightcolor=dark_red)
input_frame.pack(side="left", expand=1, fill="both", padx=10, pady=10)


# welcome text
label_title = tk.Label(input_frame, text="Welcome to the Coffee Vending Machine!", fg=dark_red, font=("Helvetica", 14, "bold"), bg=light_brown)
label_title.pack(pady=10)
# type
label_coffee_type = tk.Label(input_frame, text="Coffee Type:", bg=light_brown)
label_coffee_type.pack()
# dropdown for user to pick
coffee_options = ["Black Coffee", "Latte", "Espresso"]
coffee_var = tk.StringVar()
coffee_menu = ttk.Combobox(input_frame, textvariable=coffee_var, values=coffee_options, style="TCombobox")
coffee_menu.pack(pady=5)
coffee_var.set("Black Coffee")
# SUGAR
label_sugar = tk.Label(input_frame, text="Sugar:", bg=light_brown)
label_sugar.pack()
sugar_options = ["None", "Less", "Standard", "Extra"]
sugar_var = tk.StringVar()
sugar_menu = ttk.Combobox(input_frame, textvariable=sugar_var, values=sugar_options, style="TCombobox")
sugar_menu.pack(pady=5)
sugar_var.set("Standard")

# MILK
label_milk = tk.Label(input_frame, text="Milk:", bg=light_brown)
label_milk.pack()
milk_options = ["None", "Less", "Standard", "Extra"]
milk_var = tk.StringVar()
milk_menu = ttk.Combobox(input_frame, textvariable=milk_var, values=milk_options, style="TCombobox")
milk_menu.pack(pady=5)
milk_var.set("Standard")

# CUP
label_cup_size = tk.Label(input_frame, text="Cup Size:", bg=light_brown)
label_cup_size.pack()
cup_size_options = ["Small", "Medium", "Large"]
cup_size_var = tk.StringVar()
cup_size_menu = ttk.Combobox(input_frame, textvariable=cup_size_var, values=cup_size_options, style="TCombobox")
cup_size_menu.pack(pady=5)
cup_size_var.set("Medium")

# Receipt making button which will show the receipt
make_receipt_button = tk.Button(input_frame, text="Make Receipt", command=make_receipt)
make_receipt_button.pack(pady=10)


# Display Frame
display_frame = tk.Frame(root, bg=dark_brown, pady=10, border=1, relief="solid")
display_frame.pack(side="right", expand=1, fill="both", padx=10, pady=10)

script_directory = os.path.dirname(os.path.realpath(__file__))
img = Image.open(os.path.join(script_directory, "coffee_image.png"))
tk_img = ImageTk.PhotoImage(img)

# Creating a label which contains the image and placing it as a background
background_label = tk.Label(display_frame, image=tk_img)
background_label.place(relwidth=1, relheight=1)




# Receipt Frame
receipt_frame = tk.Frame(display_frame, bg=dark_red, pady=20, padx=20)

# user's order label
order_label = tk.Label(receipt_frame, text="", wraplength=300, justify='left', fg=cream, bg=dark_red)
order_label.pack(pady=10)

receipt_total_price = tk.Label(receipt_frame, text="Total Price: $0.00", fg=cream, bg=dark_red)
receipt_total_price.pack()

# Enter Money Label
enter_money_label = tk.Label(receipt_frame, text="Enter Money:", fg=cream, bg=dark_red,)
enter_money_label.pack()
# Entry for user to input money
money_entry = tk.Entry(receipt_frame, bg=cream)
money_entry.pack(pady=10)

# Change and bill labels
change_label = tk.Label(receipt_frame, text="", fg=cream, bg=dark_red)
change_label.pack()

# this is the change label which will either give a change or say thank you for buying
changelabel = tk.Label(receipt_frame, text="", fg=cream, bg=dark_red)
changelabel.pack()

# buy button which will give the change if there is any using the function to calculate
buy_button = tk.Button(receipt_frame, text="Buy", command=calc_change)
buy_button.pack(pady=10)

receipt_frame.pack()

root.mainloop()
