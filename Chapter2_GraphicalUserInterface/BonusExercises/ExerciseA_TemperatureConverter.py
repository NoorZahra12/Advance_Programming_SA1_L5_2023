# Exercise A: Temperature Converter
# Develop a GUI that implements a temperature converter application using Tkinter, 
# allowing users to convert between Celsius and Fahrenheit.


########### Plan ############
# in order to let user convert between celsius and fahrenheit.
# user just has to type one number
# and then select a unit (fehrenheit or celsius) to convert that number user wrote into that selected unit



# importing tkinter library
import tkinter as tk

root = tk.Tk()
root.title('14/nov/2023 Temperature Converter')
root.geometry("400x200")

# converting number user wrote into a fahrenheit with this function
def celsius_to_fahrenheit():
    # assuming the number is celsius and converting it into fahrenheit with this formula
    fahrenheit = (float(user_input.get()) * 9/5) + 32
    # then displaying the answer in the result label with the degree sign \u00B0 is the code for degree sign
    result.set(f"{fahrenheit:.2f} \u00B0F")


# converting number user wrote into a celsius with this function
def fahrenheit_to_celsius():
    # assuming the number user wrote is fahrenheit and converting it into celsius with ths formula
    celsius = (float(user_input.get()) - 32) * 5/9
    # then displaying the answer in the result label with the degree sign \u00B0 is the code for degree sign
    result.set(f"{celsius:.2f} \u00B0C")

# displaying a label heading
headingLabel = tk.Label(root, text="Temperature Converter", font=("Arial", 16, "bold"), pady=12)
headingLabel.pack(side="top")

# asking user to type a number in this label
enterLabel = tk.Label(root, text="Enter Number: ")
enterLabel.pack()

# this helps to let user modify their input in the entry
user_input = tk.StringVar()
entry = tk.Entry(root, textvariable=user_input, width=20)
entry.pack()

# making a frame which will contain both the buttons inside it
button_frame = tk.Frame(root)
# adding padding outside the frame in the y axis (vertical)
button_frame.pack(pady=10)

# making a button for calling the celsius_to_fahrenheit function to convert the number user types
# assuming it is celsius and displaying the answer in the result label after converting it into fahrenheit
fahrenheit_button = tk.Button(button_frame, text="Fahrenheit", command=celsius_to_fahrenheit)
# placing the button to the left and padding the outer area of the button on x axis(horizontal)
fahrenheit_button.pack(side="left",padx=5)

# making a celsius button
# when user clicks this button it will run the fahrenheit_to_celsius function
# by assuming the number user typed is fahrenheit and displays the answer after converting the number into celsius
celsius_button = tk.Button(button_frame, text="Celsius", command=fahrenheit_to_celsius)
# placing the button to the right and padding the outer area of the button on x axis(horizontal)
celsius_button.pack(side="right",padx=5)

# RESULT label which will dislay the answer
# user can modify the result displayed in the window when clicking the buttons and it can show 2 different results
# one being fahrenhiet and the other being celsius
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.pack()

root.mainloop()