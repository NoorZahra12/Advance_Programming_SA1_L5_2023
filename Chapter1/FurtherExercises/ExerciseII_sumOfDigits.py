# Write Python Program to Find the Sum of Digits in a Number .
# For example if enters a number 1234 the result is 1+2+3+4 = 10



number=input("Enter many digits of numbers to add them: ")#taking input as string

#this is the total sum variable
sum=0


#this equation message is for displaying all the different numbers in the "number" string 
# with a + sign between them
#like if user writes 649 then the equation meassage will show 6+7+9 as a string 
# without adding them because it's not integer
#for now the string will be empty
equation_msg=""

# the variable for each digit inside the number is called "i"
for i in number:

    # here after getting each new digit from the string
    # converting the digits into integer in order to add them in the "sum" variable
    # it means sum = sum + int(i) the sum will keep adding itself with each new number until the total is calculated
    sum+=int(i)

    # this variable will keep increasing with each new number along with a plus sign at the end
    # if user types 81 it will first add 8 + as string
    # and then add 1 + in the equation_msg variable as string
    # until it becomes 8 +  1 + in the equation_msg variable
    equation_msg +=  i + " + "

#removing the last plus sign in the end
equation_msg=equation_msg[:-1]

# printing the answer
print("Result is:",equation_msg,"=",sum)

