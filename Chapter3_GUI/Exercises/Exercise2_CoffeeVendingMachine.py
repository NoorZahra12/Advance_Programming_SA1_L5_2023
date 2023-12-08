import tkinter as tk
from tkinter import ttk

def calc_change():
    # Retrieve selected options from the input frame
    coffee_type = coffee_var.get()
    sugar_level = sugar_var.get()
    milk_level = milk_var.get()

    # Update labels in the receipt frame
    label_coffee_type.config(text=f"Coffee Type: {coffee_type}")
    label_sugar.config(text=f"Sugar: {sugar_level}")
    label_milk.config(text=f"Milk: {milk_level}")

# def calc_change():
    # coffee_type = coffee_var.get()
    # sugar_level = sugar_var.get()
    # milk_level = milk_var.get()

    # # Update labels in receipt_frame
    # label_coffee_type.config(text=f"Coffee Type: {coffee_type}")
    # label_sugar.config(text=f"Sugar: {sugar_level}")
    # label_milk.config(text=f"Milk: {milk_level}")

    # # Calculate total price based on selected options (you can customize this logic)
    # total_price = calculate_total_price(coffee_type, sugar_level, milk_level)
    # receipt_total_price.config(text=f"Total Price: ${total_price:.2f}")

def calculate_total_price(coffee_type, sugar_level, milk_level):
    # Your logic to calculate the total price based on the selected options
    # This is just a placeholder, replace it with your actual pricing logic
    base_price = 2.50
    sugar_price = 0.25 if sugar_level != "None" else 0
    milk_price = 0.50 if milk_level != "None" else 0

    return base_price + sugar_price + milk_price


root = tk.Tk()
root.geometry("800x300")
root.title("Coffee Vending Machine")

darkerbgc = "#221100"
lighterdarkerbgc = "#554333"
# Input Frame
input_frame = tk.Frame(root, bg= darkerbgc , pady=10, border=1, relief="solid", highlightbackground="#004080", highlightcolor="#004080")
input_frame.pack(side="left", expand=1, fill="both", padx=10, pady=10)

label_title = tk.Label(input_frame, text="Welcome to the Coffee Vending Machine!", fg="blue", font=("Helvetica", 14, "bold"), bg= darkerbgc)
label_title.pack(pady=10)

label_prompt = tk.Label(input_frame, text="Please place your order", bg= darkerbgc)
label_prompt.pack(pady=10)

# Coffee lsbel
label_coffee_type = tk.Label(input_frame, text="Coffee Type:", bg= darkerbgc)
label_coffee_type.pack()
# Coffee Options
coffee_options = ["Black Coffee", "Latte", "Espresso"]
coffee_var = tk.StringVar()
coffee_menu = ttk.Combobox(input_frame, textvariable=coffee_var, values=coffee_options, style="TCombobox")
coffee_var.set(coffee_options[0])
coffee_menu.pack(pady=5)

# sugar label
label_sugar = tk.Label(input_frame, text="Sugar:", bg= darkerbgc)
label_sugar.pack()
# Sugar Options
sugar_options = ["None", "Less", "Standard", "Extra"]
sugar_var = tk.StringVar()
sugar_menu = ttk.Combobox(input_frame, textvariable=sugar_var, values=sugar_options, style="TCombobox")
sugar_var.set(sugar_options[0])
sugar_menu.pack(pady=5)


# milk label
label_milk = tk.Label(input_frame, text="Milk:", bg= darkerbgc)
label_milk.pack()
# Milk Options
milk_options = ["None", "Less", "Standard", "Extra"]
milk_var = tk.StringVar()
milk_menu = ttk.Combobox(input_frame, textvariable=milk_var, values=milk_options, style="TCombobox")
milk_var.set(milk_options[0])
milk_menu.pack(pady=5)

# Display Frame
display_frame = tk.Frame(root, bg= lighterdarkerbgc , pady=10, border=1, relief="solid")
display_frame.pack(side="right", expand=1, fill="both", padx=10, pady=10)

# Receipt Frame
receipt_frame = tk.Frame(display_frame, bg="#000", pady=20, padx=20)
receipt_frame.pack(pady=20)

# Labels for Coffee Type, Sugar, and Milk in Receipt Frame
# label_coffee_type = tk.Label(receipt_frame, text= "Coffee Type: {milk_var}", fg="white", bg="#000")
bill_label= tk.Label(receipt_frame, text=f"Coffee Type: {coffee_var.get()}\nSugar: {sugar_var.get()}\nMilk: {milk_var.get()}", fg="white", bg="#000")
bill_label.pack()
# Total Price Label
receipt_total_price = tk.Label(receipt_frame, text="Total Price: $0.00", fg="white", bg="#000")
receipt_total_price.pack()

# Insert Money Entry
money_entry = tk.Entry(display_frame, bg="#fff")
money_entry.pack(pady=10)

# Buy Button
buy_button = tk.Button(display_frame, text="Buy", command=calc_change)
buy_button.pack(pady=10)

root.mainloop()