# Write a program that prints the even numbers from 1 to 100. 
# Hint - Use Continue Statement

# number=1
# #this code will loop until it is less than or equal to 100
# while number<=100:
#     #chceking if number is not divisible by 2
#     if number %2 != 0:
#         number+=1
#         continue
#     else:
#         print(number)
#         #if it is odd number it wil increment by 1 without printing it
#         number+=1



for number in range(1, 101):
    if number % 2 != 0: # checking if the number is an odd number
        continue  # Skiping the odd numbers if the statement is true
    #continue will help not going in the next line to print
    print(number) #printing the number if it is an even number