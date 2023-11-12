# Write a program that prints the even numbers from 1 to 100. 
# Hint - Use Continue Statement

#using range starting from 1 to 101 
#the reason it is 101 instead of 100 is because it will stop at 100
#tried 100but stoped at 99 so i'm writing 101 to end at 100 because it 
# will stop at 101 without printing 101......or atleast that's what i think is gooing on here
for number in range(1, 101):
    if number % 2 != 0: # checking if the number is an odd number
        continue  # Skiping the odd numbers if the statement is true
    #continue will help not going in the next line to print
    print(number) #printing the number if it is an even number