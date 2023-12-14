# importing the math library
import math


# CEIL
# ceil  is to round to the nearest small integer
userceil = float(input("Enter number for ceil: "))
# doing the calculation with the imported math library
numceil = math.ceil(userceil)
# printing the answer of ceil
print(f'Ceil of {userceil} = {numceil}')
# floor is to round to the nearest larger integer
userfloor = float(input("Enter number for floor: "))
# doing the calculation with the imported math library
numfloor = math.floor(userfloor)
# printing the answer of floor
print(f'Floor of {userfloor} = {numfloor}')

# FACTORIAL
# factorial is to multiply by numbers by -= 1. like if the number is 3. the calculation will be 3x2x1 = 6.
# the number keeps reducing by 1 until it reaches 1.
userfoctorial = int(input("Enter number for factorial: "))
# doing the calculation with the imported math library
numfactorial = math.factorial(userfoctorial)
# printing the answer of factorial
print(f'Factorial of {userfoctorial} = {numfactorial}')


# EXPONENTS
# taking user inut
userbase = float(input("Enter the base for exponentiation: "))
userexpo = float(input("Enter the exponent for exponentiation: "))
# doing the calculation with the imported math library
ansexpo = math.pow(userbase, userexpo)
# printing the answer of exponents
print(f'{userbase} with power of {userexpo} = {ansexpo}')

# SQUARE ROOT
# takig user input
usersr = float(input("Enter number for square root: "))
# doing the calculation with the imported math library
numsqrt = math.sqrt(usersr)
# printing the answer of square root
print(f'Square root of {usersr} = {numsqrt}')