# Develop a GUI using Tkinter to Create an employee class with the following members: name, age, id, salary

# Add the following methods: setData() - should allow employee data to be set via user input,getData()- 
# should output employee data to the console
# Create a list of 5 employees. Ask the user to enter the details of 5 employees using the add_employee method 
# and then display the output using the display_emloyee method as mentioned below Expected output:
# Name	Position	Salary	ID
# Alice	Manager		9500.0	1
# Bob	Accountant	6000.0	2
# Brain	Social Media	4000.0	3
# Frank	Salesman	2500.0	4
# Marker	Clerk		1500.0	5
# import the tkinter module and alias it as tk
import tkinter as tk

# create a class to represent an Employee
class Employee:
    def __init__(self):
        # initialize attributes for an employee
        self.name = ""
        self.position = ""
        self.salary = 0.0
        self.id = 0

    # method to set data for an employee
    def set_data(self, name, position, salary, emp_id):
        self.name = name
        self.position = position
        self.salary = salary
        self.id = emp_id

    # method to get formatted data for an employee
    def get_data(self):
        return f"{self.name}\t{self.position}\t{self.salary}\t{self.id}"

# create a class for the EmployeeApp
class EmployeeApp:
    def __init__(self, root):
        # initialize the main Tkinter window
        self.root = root
        self.root.title("Employee Class")
        self.root.geometry("500x400")

        # create left frame for user input
        self.left_frame = tk.Frame(self.root)
        self.left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # create right frame for displaying employee information
        self.right_frame = tk.Frame(self.root)
        self.right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # create lists to store employee information
        self.employee_list = []
        self.name_labels = []   # labels for employee names
        self.position_labels = []   # labels for employee positions
        self.salary_labels = []   # labels for employee salaries
        self.id_labels = []   # labels for employee IDs

        # create widgets for the left frame
        self.name_label = tk.Label(self.left_frame, text="Name:")
        self.name_label.grid(row=0, column=0, pady=5)
        self.name_entry = tk.Entry(self.left_frame)
        self.name_entry.grid(row=0, column=1, pady=5)

        self.position_label = tk.Label(self.left_frame, text="Position:")
        self.position_label.grid(row=1, column=0, pady=5)
        self.position_entry = tk.Entry(self.left_frame)
        self.position_entry.grid(row=1, column=1, pady=5)

        self.salary_label = tk.Label(self.left_frame, text="Salary:")
        self.salary_label.grid(row=2, column=0, pady=5)
        self.salary_entry = tk.Entry(self.left_frame)
        self.salary_entry.grid(row=2, column=1, pady=5)

        self.add_button = tk.Button(self.left_frame, text="Add Employee", command=self.add_employee)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        # create widgets for the right frame
        self.create_right_frame_widgets()

        # configure column and row weights for both frames
        self.configure_frame_weights()

    # method to add an employee
    def add_employee(self):
        # retrieve input values from entry widgets
        name = self.name_entry.get()
        position = self.position_entry.get()
        salary_str = self.salary_entry.get()

        # validate input values
        if not (name and position and salary_str):
            warning = tk.Label(root, text="Input Error: Please enter all details.")
            warning.grid()
            return

        if not (name.isalpha() and position.isalpha()):
            warning = tk.Label(root, text="Input Error: Please enter alphabets in name and position.")
            warning.grid()
            return

        if not salary_str.isdigit():
            warning = tk.Label(root, text="Input Error: Please enter numbers in salary.")
            warning.grid()
            return

        # convert salary to float and generate an employee ID
        salary = float(salary_str)
        emp_id = len(self.employee_list) + 1

        # create an Employee object, set data, and append to the list
        employee = Employee()
        employee.set_data(name, position, salary, emp_id)
        self.employee_list.append(employee)

        # display "Added" for 1.5 seconds
        self.add_button.config(text="Added", bg="green")
        self.root.after(1500, self.reset_button)

        # clear entry fields
        self.name_entry.delete(0, tk.END)
        self.position_entry.delete(0, tk.END)
        self.salary_entry.delete(0, tk.END)

        # display employee information in the right frame
        self.display_employee(employee)

    # method to reset the button text and color
    def reset_button(self):
        self.add_button.config(text="Add Employee", bg="SystemButtonFace")

    # method to display employee information in the right frame
    def display_employee(self, employee):
        # create and display labels for each attribute
        name_label = tk.Label(self.name_frame, text=employee.name)
        name_label.pack()

        position_label = tk.Label(self.position_frame, text=employee.position)
        position_label.pack()

        salary_label = tk.Label(self.salary_frame, text=str(employee.salary))
        salary_label.pack()

        id_label = tk.Label(self.id_frame, text=str(employee.id))
        id_label.pack()

        # add labels to the label lists
        self.name_labels.append(name_label)
        self.position_labels.append(position_label)
        self.salary_labels.append(salary_label)
        self.id_labels.append(id_label)

    # method to configure column and row weights for both frames
    def configure_frame_weights(self):
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.left_frame.rowconfigure(4, weight=1)
        self.right_frame.rowconfigure(1, weight=1)
        self.right_frame.columnconfigure(0, weight=1)
        self.right_frame.columnconfigure(1, weight=1)
        self.right_frame.columnconfigure(2, weight=1)
        self.right_frame.columnconfigure(3, weight=1)

    # method to create widgets for the right frame
    def create_right_frame_widgets(self):
        self.name_frame = tk.Frame(self.right_frame)
        self.name_frame.grid(row=0, column=0, pady=5)
        tk.Label(self.name_frame, text="Name").pack()

        self.position_frame = tk.Frame(self.right_frame)
        self.position_frame.grid(row=0, column=1, pady=5)
        tk.Label(self.position_frame, text="Position").pack()

        self.salary_frame = tk.Frame(self.right_frame)
        self.salary_frame.grid(row=0, column=2, pady=5)
        tk.Label(self.salary_frame, text="Salary").pack()

        self.id_frame = tk.Frame(self.right_frame)
        self.id_frame.grid(row=0, column=3, pady=5)
        tk.Label(self.id_frame, text="ID").pack()

# create the main Tkinter window and the EmployeeApp instance
root = tk.Tk()
app = EmployeeApp(root)

# start the Tkinter event loop
root.mainloop()