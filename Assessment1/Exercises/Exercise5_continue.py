# Write a program that implements a while loop. 
# This program should ask the user if they would like to continue and 
# use the while loop to keep looping as long as they enter the letter Y. 
# Once the while loop has terminated output the number of times it is executed.

#importing random library
import random
#while loop will keep looping itself while it is True until it turns false or i break the loop with a conditon
while True:
    #printing a random integer ranging from 1 until 6 inside a variable called dice which will keep 
    #regenerating a new number every time the loop is being looped again a new dice number will appear
    dice=random.randint(1,6)
    print(dice)
    #asking user if they want another new number of the dice which will determine if the while loop should continue or break
    answer=input("Roll the dice?\nType 'y' if yes: ")
    #if user clicks y and continues then the while loop's condition stays true
    if answer=="y":
        continue
    #otherwise with break it will end the loop if the user inputs any other letter than y
    else:
        break