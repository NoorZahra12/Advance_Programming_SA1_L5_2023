# Write a program that prints the even numbers from 1 to 100. 
# Hint - Use Continue Statement

number=1
#this code will loop until it is less than or equal to 100
while number<=100:
    #chceking if number is divisible by 2
    if number%2==0:
        #if it is an even number it will print and increase by 1
        print(number)
        number+=1
        continue
    #if it is odd number it wil increment by 1 without printing it
    else:
        number+=1