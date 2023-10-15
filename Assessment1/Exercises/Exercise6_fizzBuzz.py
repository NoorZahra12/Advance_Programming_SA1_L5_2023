#Write a program that prints the numbers from 1 to 100. 
#But for multiples of three print Fizz” instead of the number 
#and for the multiples of five print “Buzz”. 
#For numbers which are multiples of both three and five print “FizzBuzz”.


#using for loop and range from 1 to 101 to print numbers from 1 til 100
for num in range(1,101):
    #if a number is divisible by both 3 and 5
    if num%3==0 and num%5==0:
        print("Fizzbuzz")
        
    #if a number is divisible by 3
    elif num%3==0:
        print("Fizz")
        
    #if a number is divisible by 5
    elif num%5==0:
        print("Buzz")

    #this is the default statement if all the statements above are false
    else:
        print(num)