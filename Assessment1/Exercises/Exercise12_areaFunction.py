# Code a program to display a menu on the screen that asks if the user wants to
# 1: Calculate the area of a square
# 2: Calculate the area of a circle
# 3: Calculate the area of a triangle 
# Each of the 3 functions should ask for the necessary information 
# (e.g. lengths and/or angles and output the answer.

#importing math library
import math

#making 3 functions to calculate the area
def area_square(side):
    area=side*side
    return area

def area_circle(radius):
    area=math.pi*radius**2
    return area

def area_triangle(b,h):
    area=(b*h)/2
    return area

# asking user for the shape
shape=input("1.Square\n2.Circle\n3.Triangle\nSelect a shape you want to find it's area: ")

#using if else statements to print the answers
if shape=="square" or shape=="Square":
    user_side=float(input("Enter length of side: "))
    print("The area of square is: ",area_square(user_side))

elif shape=="circle" or shape=="Circle":
    user_radius=float(input("Enter radius: "))
    print("The area of circle is: ",area_circle(user_radius))

elif shape=="triangle" or shape=="Triangle":
    user_b=float(input("Enter breadth: "))
    user_h=float(input("Enter height: "))
    print("The area of triangle is: ",area_triangle(user_b,user_h))

#if user entered the wrong spelling this output is shown
else:
    print("Your input was invalid")