import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from PIL import Image, ImageTk
import os


def reset_order_summary():
    # Unchecking all checkboxes
    for var in topping_checkbox_vars + condiment_checkbox_vars + side_checkbox_vars:
        var.set("")

    # Resetting the eveything to its default state which is none
    combobox_meat.set("")
    meatorder_var.set("")
    toppingorder_var.set("")
    condimentsorder_var.set("")
    sidesorder_var.set("")
    totalprice.config(text="Total: $0.00")


def update_meat_order(event):
    # Get the selected value from the combo box
    selected_meat = combobox_meat.get()
    # Update the StringVar associated with meatorder
    meatorder_var.set(f"Burger Type: {selected_meat}")
    # Update the order summary
    update_order_summary()

def update_order_summary():
    # Get the selected toppings
    selected_toppings = [topping for topping, var in zip(topping_options, topping_checkbox_vars) if var.get()]
    toppingorder_var.set(f"Toppings: {', '.join(selected_toppings)}")

    # Get the selected condiments
    selected_condiments = [condiment for condiment, var in zip(condiments_option, condiment_checkbox_vars) if var.get()]
    condimentsorder_var.set(f"Condiments: {', '.join(selected_condiments)}")

    # Get the selected sides
    selected_sides = [side for side, var in zip(side_options, side_checkbox_vars) if var.get()]
    sidesorder_var.set(f"Sides: {', '.join(selected_sides)}")

    # Calculate total price
    total_price = calculate_total_price()
    totalprice.config(text=f"Total: ${total_price:.2f}")

# function for calculating the total cost price of the user's order
def calculate_total_price():
    # setting the Prices of everything
    burger_prices = {"Chicken": 4.00, "Mutton": 5.00, "Beef": 6.00, "Vegetarian": 3.50}
    topping_price = 1.00  # Price per topping
    condiment_price = 0.50  # Price per condiment
    side_price = 1.50  # Price per side

    # now getting the sum of each section to get total
    burger_price = burger_prices.get(combobox_meat.get(), 0)
    topping_price_total = sum([topping_price for topping, var in zip(topping_options, topping_checkbox_vars) if var.get()])
    condiment_price_total = sum([condiment_price for condiment, var in zip(condiments_option, condiment_checkbox_vars) if var.get()])
    side_price_total = sum([side_price for side, var in zip(side_options, side_checkbox_vars) if var.get()])

    # adding the sum of all sections for total cost
    total_price = burger_price + topping_price_total + condiment_price_total + side_price_total
    return total_price

# function for calculating the change
def calculate_change(total_price, payment):
    # calculating change and returning the value
    change = payment - total_price
    return change

def userpayment():
    # Firsst getting the total price of when the user clicked button
    total_price = calculate_total_price()
    # Taking user input
    # telling user the total and asking user to enter money
    payment = simpledialog.askfloat("Payment", f"Total Price: ${total_price:.2f}\nEnter payment amount:")

    # check if payment is sufficient
    if payment < total_price:
        messagebox.showwarning("Insufficient Payment", "Payment is less than the total price. Please enter a sufficient amount.")
    else:
        change = calculate_change(total_price, payment)
        # giving change back to user and also showing the change
        messagebox.showinfo("Payment Successful", f"Payment successful!\nTotal Price: ${total_price:.2f}\nPayment: ${payment:.2f}\nChange: ${change:.2f}")
        # reseting the order summary
        reset_order_summary()


root = tk.Tk()
root.title("Burger Shack Vendor")
root.geometry("800x542")
root.resizable(0, 0)

# storing the image's file path in variable
bgimg_path = os.path.join(os.path.dirname(__file__), "burgerbg.png")
bgimg = Image.open(bgimg_path)  # opening image with the file path
resized_bgimg = ImageTk.PhotoImage(bgimg.resize((800, 542), Image.BICUBIC))  # resizing image to fit root

# img container label placed at the back
labelbg = tk.Label(root, image=resized_bgimg)
labelbg.place(relwidth=1, relheight=1)  # place the label to cover the entire window

# userframe positioned horizontally left
userframe = tk.Frame(root)
userframe.pack(pady=(108,0), padx=20, anchor="w")

# BURGER TYPE
meatframe = tk.Frame(userframe)
meatframe.pack(pady=15)
# the label n combo box inside meatframe to be inline
meatlabel = tk.Label(meatframe, text="Burger Type:", font=("Helvetica", 10, "bold"))
meatlabel.grid(row=1, column=0, padx=10)
burger_meat = ["Chicken", "Mutton", "Beef", "Vegetarian"]
combobox_meat = ttk.Combobox(meatframe, values=burger_meat, width=30)
combobox_meat.grid(row=1, column=1, padx=20)
# updating the summary order by using bind to call the function
combobox_meat.bind("<<ComboboxSelected>>", update_meat_order)

# a container for 3 frames inline
the3frames = tk.Frame(userframe, width=30)
the3frames.pack()

# the 3 frames in the container
toppingframe = tk.Frame(the3frames)
toppingframe.pack(side="left")

condimentframe = tk.Frame(the3frames)
condimentframe.pack(side="left", padx=30)

sideframe = tk.Frame(the3frames)
sideframe.pack(side="left")

# TOPPINGS CONTENT
toppinglabel = tk.Label(toppingframe, text="Toppings", font=("Helvetica", 10, "bold"))
toppinglabel.pack(pady=10, anchor="w")
# Checkboxes for sides
topping_options = ["Cheese", "Onion", "Pickle", "Tomato", "Lettuce"]
topping_checkbox_vars = [tk.StringVar() for _ in range(len(topping_options))]
for i, topping in enumerate(topping_options):
    checkbox = tk.Checkbutton(toppingframe, text=topping, variable=topping_checkbox_vars[i], onvalue=topping, offvalue="")
    checkbox.pack(anchor="w")

# CONDIMENTS CONTENT
condimentlabel = tk.Label(condimentframe, text="Condiments", font=("Helvetica", 10, "bold"))
condimentlabel.pack(pady=10, anchor="w")
# Checkboxes for sides
condiments_option = ["Ketchup", "Mayonnaise", "BBQ Sauce", "Hot Sauce", "Special Sauce"]
condiment_checkbox_vars = [tk.StringVar() for _ in range(len(condiments_option))]
for i, condiment in enumerate(condiments_option):
    checkbox = tk.Checkbutton(condimentframe, text=condiment, variable=condiment_checkbox_vars[i], onvalue=condiment, offvalue="")
    checkbox.pack(anchor="w")

# SIDES CONTENT
sideslabel = tk.Label(sideframe, text="Sides", font=("Helvetica", 10, "bold"))
sideslabel.pack(pady=10, anchor="w")
# Checkboxes for sides
side_options = ["Fries", "Lemon Soda", "Water", "Fresh Juice", "Garlic Bread"]
side_checkbox_vars = [tk.StringVar() for _ in range(len(side_options))]
for i, side in enumerate(side_options):
    checkbox = tk.Checkbutton(sideframe, text=side, variable=side_checkbox_vars[i], onvalue=side, offvalue="")
    checkbox.pack(anchor="w")

# Your Order
# here is the summary of user's order in real-time with "\ntotal price:" also shown at the end of the order
# Your Order Label
order_label = tk.Label(userframe, text="Your Order:", font=("Helvetica", 12, "bold"))
order_label.pack(pady=10, anchor="center")

summaryframe = tk.Frame(userframe, bg="black", width=330, height=102)
summaryframe.pack(padx=10)

# preventing the summaryframe from resizing to fit its contents by default
summaryframe.pack_propagate(False)
# using stringvar to update texts based on user selection
meatorder_var = tk.StringVar()
toppingorder_var = tk.StringVar()
condimentsorder_var = tk.StringVar()
sidesorder_var = tk.StringVar()
# creating a text 
meatorder = tk.Label(summaryframe, textvariable=meatorder_var, bg="black", fg="white", anchor="w", justify="left")
toppingorder = tk.Label(summaryframe, textvariable=toppingorder_var, bg="black", fg="white", anchor="w", justify="left")
condimentsorder = tk.Label(summaryframe, textvariable=condimentsorder_var, bg="black", fg="white", anchor="w", justify="left")
sidesorder = tk.Label(summaryframe, textvariable=sidesorder_var, bg="black", fg="white", anchor="w", justify="left")
totalprice = tk.Label(summaryframe, text="Total: ", bg="black", fg="white")

meatorder.pack(fill="both", expand=True)
toppingorder.pack(fill="both", expand=True)
condimentsorder.pack(fill="both", expand=True)
sidesorder.pack(fill="both", expand=True)
totalprice.pack()

# Bind update functions to checkbox events
combobox_meat.bind("<<ComboboxSelected>>", update_meat_order)

# Bind the update_order_summary function to checkbox events
for selection in topping_checkbox_vars + condiment_checkbox_vars + side_checkbox_vars:
    # updating the order summary based on  user selection with the help of trace write to edit and write the order summary
    selection.trace_add("write", lambda *args: update_order_summary())

# this button will call the userpayment 
btn = tk.Button(userframe, text="Place your Order", command=userpayment, bg="#ff0000", fg="white", pady=5, padx=30, font=("Helvetica", 10, "bold"))
btn.pack(side="bottom", pady=10)

# displaying the window
root.mainloop()