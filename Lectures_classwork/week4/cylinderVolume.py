import math
#using a math module

#making a function to calculate the cylinder volume with default values
def cylinerVolume(r=10,h=5):
    #entering formula and returning the result to the caller
    return math.pi*(r**2)*h

#replacing both the default values of the function
answer=cylinerVolume(6,9)
print("The cylinder volume of radius=6 and height=9 is: ",answer)

#over riding only the first value of the function
#while the second value stays the same as default
answer=cylinerVolume(7)
print("The cylinder volume of radius=7 is: ",answer)

#calling the function with it's default value
print("The cylinder volume of default is: ",cylinerVolume())