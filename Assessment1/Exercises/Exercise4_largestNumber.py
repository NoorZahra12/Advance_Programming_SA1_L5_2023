#Write a program to input three numbers and outputs the largest using the multiple if -else statements

#asking user to type 3 numbers
print("Enter 3 numbers")
#taking 3 user inputs
num1=int(input("First number: "))
num2=int(input("Second number: "))
num3=int(input("Thrid number: "))

#if first number is the largest
if num1>num2 and num1>num3:
    print(num1, "is the largest number")
#if second number is the largest
elif num2>num1 and num2>num3:
    print(num2, "is the largest number")
#if third number is the largest
elif num3>num1 and num3>num2:
    print(num3, "is the largest number")
#if the largest number is written in 2 or all 3 variables
else:
    print("there are 2 or more largest numbers which are equal")