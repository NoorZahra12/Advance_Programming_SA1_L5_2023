# Code a program to display a menu on the screen that asks if the user wants to
# 1: Calculate the area of a square
# 2: Calculate the area of a circle
# 3: Calculate the area of a triangle 
# Each of the 3 functions should ask for the necessary information 
# (e.g. lengths and/or angles and output the answer.

#importing math library
import math

#making 3 functions to calculate the area
def area_square():
    #asking necessary input from user
    side=float(input("Enter length of side: "))
    #formula for calculating the area and storing the answer inside a variable
    area=side*side
    # returnimg the answer
    return area
def area_circle():
    #asking necessary input from user
    radius=float(input("Enter radius: "))
    #formula for calculating the area and storing the answer inside a variable
    area=math.pi*radius**2
    # returnimg the answer
    return area
def area_triangle():
    #asking necessary input from user
    b=float(input("Enter breadth: "))
    h=float(input("Enter height: "))
    #formula for calculating the area and storing the answer inside a variable
    area=(b*h)/2
    # returnimg the answer
    return area

# this is where the code starts for the user
# asking user for the shape
shape=input("1.Square\n2.Circle\n3.Triangle\nSelect a shape you want to find it's area: ")

while True:
    #using if else statements to print the answers according to what the user chooses
    #writing 1 2 and 3 inside "" as i am taking user input as a string
    if shape=="1" or shape.lower()=="square":
        print("The area of square is: ",area_square())
        break
    elif shape=="2" or shape.lower()=="circle":
        print("The area of circle is: ",area_circle())
        break
    elif shape=="3" or shape.lower()=="triangle":
        print("The area of triangle is: ",area_triangle())
        break
    #if user entered the wrong spelling this output is shown
    else:
        print("Your input was invalid")
        shape=input("\n1.Square\n2.Circle\n3.Triangle\nSelect a shape you want to find it's area: ")
        # the loop will keep giving the user another chance to type a valid input in case user types an invalid answer 
        # until user types correct