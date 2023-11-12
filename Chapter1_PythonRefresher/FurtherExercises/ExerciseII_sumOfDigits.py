# Write Python Program to Find the Sum of Digits in a Number .
# For example if enters a number 1234 the result is 1+2+3+4 = 10



number=input("Enter many digits of numbers to add them: ")#taking input as string

#this is the total sum variable
sum_of_digits=0


#this equation message is for displaying all the different numbers in the "number" string 
# with a + sign between them
#like if user writes 649 then the equation meassage will show 6+7+9 as a string 
# without adding them because it's not integer
#for now the string will be empty
number_string=""

# the variable for each digit inside the number is called "i"
for digit_of_string in number:

    # here after getting each new digit from the string
    # converting the digits into integer in order to add them in the "sum" variable
    # it means sum = sum + int(i) the sum will keep adding itself with each new number until the total is calculated
    sum_of_digits+=int(digit_of_string)

    # this variable will keep increasing with each new number along with a plus sign at the end
    # if user types 81 it will first add 8 + as string
    # and then add 1 + in the equation_msg variable as string
    # until it becomes 8 +  1 + in the equation_msg variable
    number_string +=  digit_of_string + " + "

#removing the last plus sign in the end
number_string=number_string[:-1]

# printing the answer
print("Result is:",number_string,"=",sum_of_digits)