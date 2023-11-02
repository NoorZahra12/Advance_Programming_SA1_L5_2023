#Write a program to input three numbers and outputs the largest using the multiple if -else statements



#asking user to type 3 numbers
print("Enter 3 numbers")
#taking 3 user inputs
num1=int(input("First number: "))
num2=int(input("Second number: "))
num3=int(input("Third number: "))

#checking if all 3 numbers are equal
if num1==num2==num3:
    print("All three numbers ", num1, num2, num3, "are equal")

#checking if there are 2 numbers which are equal and largest
elif num1==num2>num3:
    print("The first number", num1,", and second number",num2,", are the largest number")
elif num1==num3>num2:
    print("The first number:", num1,", and third number",num3,", are the largest number")
elif num2==num3>num1:
    print("The second number", num2,", and third number",num3,", are the largest number")


#Finding only ONE largest number in the input
#checking if first number is the largest
elif num1>num2 and num1>num3:
    print(num1, "is the largest number")
#checking if second number is the largest
elif num2>num1 and num2>num3:
    print(num2, "is the largest number")
#checking if third number is the largest
elif num3>num1 and num3>num2:
    print(num3, "is the largest number")

#there are no else statements here as default