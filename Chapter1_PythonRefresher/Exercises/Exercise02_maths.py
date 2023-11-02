#Write a program that evaluates the following calculations for two int numbers obtained from the user 
#and outputs the results to the console:
#Sum (+) | Diff (-) | Product (x) | Quotient (/) | Remainder (%)


#taking 2 user input as int numbers
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

#making 4 variables for the calculations
addition=a+b
subtract=a-b
divide=a/b
remainder=a%b

#taking user input for the calculations
user_choice=input("Type add,subtract, divide or remainder:\n")

#using if statements to display the answers according to what the user chooses
#if user typed add i will use the add variable to add the 2 user input 
# and display the answer using + sign to add them
if user_choice=="add":
    print("Addition: ",addition)
elif user_choice=="subtract": #if user wrote subtract it will subtract the 2 numbers to display the subtraction
    print("Subtraction: ",subtract)
elif user_choice=="divide": #if user wrote divide then it will divide the first number with second and give the answer
    print("Divide: ",divide)
elif user_choice=="remainder": #if user wrote remainder it will display the remainder of the 2 input
    print("Remainder: ",remainder)
    
#if user wrote the anything other than add, subtract, divide, or remainder. this output will be shown
else:
    print("you have entered the wrong spelling")