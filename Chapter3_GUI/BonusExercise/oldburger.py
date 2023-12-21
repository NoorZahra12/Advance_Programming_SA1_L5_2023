import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

def onclick():
    # Update the order summary label based on user's selections
    selected_burger_type = combobox_meat.get()
    selected_toppings = [var.get() for var in topping_checkbox_vars]
    selected_condiments = [var.get() for var in condiment_checkbox_vars]
    selected_sides = [var.get() for var in side_checkbox_vars]

    # Calculate total price
    burger_price = burger_prices.get(selected_burger_type, 0)
    topping_price_total = sum([topping_price for topping in selected_toppings if topping])
    condiment_price_total = sum([condiment_price for condiment in selected_condiments if condiment])
    side_price_total = sum([side_price for side in selected_sides if side])

    total_price = burger_price + topping_price_total + condiment_price_total + side_price_total

    # Display the order summary and total price
    order_summary_label.config(text=f"Burger Type: {selected_burger_type}\n"
                                   f"Toppings: {', '.join(selected_toppings)}\n"
                                   f"Condiments: {', '.join(selected_condiments)}\n"
                                   f"Sides: {', '.join(selected_sides)}")

    total_price_label.config(text=f"Total Price: ${total_price:.2f}")




root = tk.Tk()
root.title("Burger Shack Vendor")
root.geometry("800x600")
root.resizable(1, 0)

script_directory = os.path.dirname(os.path.realpath(__file__))

# Heading Frame
heading_frame = tk.Frame(root, width=800, height=100, bg="#232323")
heading_frame.pack(side="top", fill="x")

# Create Canvas for heading
heading_canvas = tk.Canvas(heading_frame, width=800, height=100, bg="#232323", highlightthickness=0)
heading_canvas.pack()

# Logo Image
logo_image_path = os.path.join(script_directory, "burgerlogo.png")
original_logo = Image.open(logo_image_path)
resized_logo = original_logo.resize((78, 78), Image.BICUBIC)
logo_image = ImageTk.PhotoImage(resized_logo)

logo_image_id = heading_canvas.create_image(50, 50, anchor="center", image=logo_image)
text_id = heading_canvas.create_text(290, 50, text="Burger Shack Vendor", font=("Helvetica", 25, "bold"), fill="white")

# this is the main which will hold the form and the img
main_canvas = tk.Canvas(root, width=800, height=600)
main_canvas.pack(fill="both", expand=True)

linearbg_path = os.path.join(script_directory, "linearbg.png")
linearbg_img = Image.open(linearbg_path)
sized_linearbg = linearbg_img.resize((800, 600), Image.BICUBIC)
linear_bg_image = ImageTk.PhotoImage(sized_linearbg)

# Left Canvas with Linear Background, in the left canvas is where I'll have the form thing for coffee
left_canvas = tk.Canvas(main_canvas, width=400, height=600, bd=0, highlightthickness=0)
left_canvas.create_image(200, 300, anchor="center", image=linear_bg_image)
main_canvas.create_window(0, 0, anchor="nw", window=left_canvas)

# Right Canvas with Linear Background, The ight canvas is where I'll have the juicy burger image
right_canvas = tk.Canvas(main_canvas, width=400, height=600, bd=0, highlightthickness=0)
right_canvas.create_image(200, 300, anchor="center", image=linear_bg_image)
main_canvas.create_window(800, 0, anchor="ne", window=right_canvas)

# Image in the right canvas (Juicy Burger with Transparent Background)
juicy_burger_path = os.path.join(script_directory, "juicyburger.png")
juicy_burger_image = Image.open(juicy_burger_path)
juicy_burger_image = ImageTk.PhotoImage(juicy_burger_image)

# Place linear background image behind the burger image
linear_bg_id = right_canvas.create_image(200, 300, anchor="center", image=linear_bg_image)
juicy_burger_id = right_canvas.create_image(200, 250, anchor="center", image=juicy_burger_image)







# making a user frame
userframe = tk.Frame(left_canvas, width=360, height=450)
userframe.pack_propagate(0)
left_canvas.create_window(200, 250, anchor="center", window=userframe)

# Add labels, combobox, checkboxes, and radio buttons to the user frame
meatframe = tk.Frame(userframe)
meatframe.pack(pady=20, anchor="w")

label1 = tk.Label(meatframe, text="Burger Type:", font=("Helvetica", 10, "bold"))
label1.grid(row=1, column=0, padx=10)

burger_meat = ["Chicken", "Mutton", "Beef", "Vegetarian"]
combobox_meat = ttk.Combobox(meatframe, values=burger_meat, width=30)
combobox_meat.grid(row=1, column=1, padx=20)

the3frames = tk.Frame(userframe, width=30)
the3frames.pack()

toppingframe = tk.Frame(the3frames)
condimentframe = tk.Frame(the3frames)
sideframe = tk.Frame(the3frames)

toppingframe.pack(side="left")
condimentframe.pack(side="left", padx=30)
sideframe.pack(side="left")

# TOPPINGS CONTENT
toppinglabel = tk.Label(toppingframe, text="Toppings", font=("Helvetica", 10, "bold"))
toppinglabel.pack(pady=10, anchor="w")
# Checkboxes for sides
topping_options = ["Cheese", "Onion", "Pickle", "Tomato", "Lettuce"]
topping_checkbox_vars = [tk.StringVar() for _ in range(len(topping_options))]

for i, topping in enumerate(topping_options):
    checkbox = tk.Checkbutton(toppingframe, text=topping, variable=topping_checkbox_vars[i], onvalue=topping, offvalue="", command=onclick)
    checkbox.pack(anchor="w")

# CONDIMENTS CONTENT
condimentlabel = tk.Label(condimentframe, text="Condiments", font=("Helvetica", 10, "bold"))
condimentlabel.pack(pady=10, anchor="w")
# Checkboxes for sides
condiments_option = ["Ketchup", "Mayonnaise", "BBQ Sauce", "Hot Sauce", "Special Sauce"]
condiment_checkbox_vars = [tk.StringVar() for _ in range(len(condiments_option))]

for i, condiment in enumerate(condiments_option):
    checkbox = tk.Checkbutton(condimentframe, text=condiment, variable=condiment_checkbox_vars[i], onvalue=condiment, offvalue="", command=onclick)
    checkbox.pack(anchor="w")

# SIDES CONTENT
sideslabel = tk.Label(sideframe, text="Sides", font=("Helvetica", 10, "bold"))
sideslabel.pack(pady=10, anchor="w")
# Checkboxes for sides
side_options = ["Fries", "Lemon Soda", "Water", "Fresh Juice", "Garlic Bread"]
side_checkbox_vars = [tk.StringVar() for _ in range(len(side_options))]

for i, side in enumerate(side_options):
    checkbox = tk.Checkbutton(sideframe, text=side, variable=side_checkbox_vars[i], onvalue=side, offvalue="", command=onclick)
    checkbox.pack(anchor="w")



# Your Order
# here is the summary of user's order in real-time with "\ntotal price:" also shown at the end of the order
# Your Order Label
order_label = tk.Label(userframe, text="Your Order:", font=("Helvetica", 12, "bold"))
order_label.pack(pady=10, anchor="center")

# Label to display the order summary
order_summary_label = tk.Text(userframe, text="", font=("Helvetica", 10))
order_summary_label.pack(anchor="w")

# Label to display the total price
total_price_label = tk.Label(userframe, text="Total Price: $0.00", font=("Helvetica", 10))
total_price_label.pack(anchor="w")


# PRICES
burger_prices = {"Chicken": 4.00, "Mutton": 5.00, "Beef": 6.00, "Vegetarian": 3.50}
topping_price = 1.00  # Price per topping
condiment_price = 0.50  # Price per condiment
side_price = 2.00  # Price per side

# Bind events to update order summary in real-time
combobox_meat.bind("<FocusOut>", onclick)


for var in topping_checkbox_vars + condiment_checkbox_vars + side_checkbox_vars:
    var.trace_add("write", onclick)


# Buy button
btn =  tk.Button(userframe, text="Place your Order", bg="#ff0000", fg="white", pady=5,padx=30, font=("Helvetica", 10,"bold"))
btn.pack(side="bottom", pady=20)

# Main loop
root.mainloop()