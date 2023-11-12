# Develop a GUI using Tkinter to Create an employee class with the following members: name, age, id, salary

# Add the following methods: setData() - should allow employee data to be set via user input,getData()- should output employee data to the console
# Create a list of 5 employees. Ask the user to enter the details of 5 employees using the add_employee method and then display the output using the display_emloyee method as mentioned below Expected output:
# Methods: get_name(), set_name(n), get_age(), set_age(a), get_id(), set_
# id(i), get_salary(), set_salary(s)

import tkinter as tk

window=tk.Tk()

class Employee:
    def __init__(self):
        self.name = ""
        self.position = ""
        self.age = 0
        self.salary = 0.0
        self.id = 0

    def setData(self,name,position,salary,age,id):
        self.name=name
        self.position=position
        self.salary=salary
        self.age=age
        self.id=id
        # self.setName(name)
        # self.setPosition(position)
        # self.setSalary(salary)
        # self.setId(id)
        
    def getData(self):
        # return f"Name:{self.name},Position:{self.position},Salary:{self.salary},Age:{self.age},ID:{self.id},"
        return self.name, self.position, self.salary, self.age, self.id

class Employee_GUI:
    def __init__(self):
        super().__init__()
        self.title("list")
        self.geometry("500x500")
        self.employeeList = []
        self.add_employee()
    
    def add_employee(self):
        for item in range(5):
            name=input("Enter name:")
            position=input("Enter position:")
            salary=input("Enter salary:")
            age=input("Enter age:")
            id=input("Enter id:")

            newEmployee = Employee()
            newEmployee.setData(name,position,salary,age,id)
            self.employeeList.append(newEmployee)
        self.display_employees()

    def display_employees(self):
        for employee in self.employeeList:
            print(employee.getData())
window=Employee_GUI()
window.mainloop()