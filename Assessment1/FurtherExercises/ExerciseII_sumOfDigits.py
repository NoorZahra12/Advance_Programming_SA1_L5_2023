# Write Python Program to Find the Sum of Digits in a Number .For example if enters a number 1234 the result is 1+2+3+4 = 10
number=int(input("Enter many digits of numbers to add them: "))
sum=0

#converting the user integer input into a string to use each digit inside the number in for loop
# the variable for each digit inside the number is called "i"
for i in str(number):
    #here after getting each new digit from the string
    #converting the digits into integer in order to add them in the "sum" variable
    sum+=int(i)
# printing the answer
print("Anwser: ",sum)