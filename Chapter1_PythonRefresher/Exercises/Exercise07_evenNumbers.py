# Write a program that prints the even numbers from 1 to 100. 
# Hint - Use Continue Statement


# here I am using the range function
# i can type 100 directly but then the range function will use a list of numbers starting from 0 to the 100th index
# and if u start from 0 to reach 100th index u get 99. so it will stop at 98
# therefore i wrote 1 to start from 1 and 101 to stop at the 101th index which is 100
for number in range(1, 101):
    if number % 2 != 0: # checking if the number is an odd number
        continue  # Skiping the odd numbers if the statement is true
    #continue will help not going in the next line to print
    print(number) #printing the number if it is an even number