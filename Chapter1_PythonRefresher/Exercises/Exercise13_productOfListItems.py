# Write a program that passes a list as an argument to a function. 
# The function should then calculate the product (values multiplied) of the list values 
# and return this value back to the main program.


# I'd rather just import math to get the product of the list but rules are rules

# making an empty list which will be be adding user input as element of the list later on
# I plan on letting the user write the numbers they wanna calculate inside a list and then get the product
user_list=[]

#making a function where user needs to type the name of the list inside the brackets when you call it
def multiply_list():
    #can't write 0 because anything multiplied by 0 is 0 but the answer will be same if it's 1
    prod_list=1

    #using a for loop and making a variable for each element in list to be multiplied with prod
    #the prod variable will be multiplied with each element
    #so it will be like 1x6x2x9x4
    for user_number in user_list:
        prod_list *= user_number
    #after the for loop ends and the prod variable is multiplied by all the elements
    #returning the prod variable to the user
    return prod_list

# START OF WHILE LOOP


while True:
    # taking user input
    # the idea is that only the numbers will be appended in the list
    # i will take the input as a string if it is q the loop will break
    # if it is not q or a non integer input, it will be appended in the list after converting it into an integer
    # as i am taking input string datatype so if it is an integer then ill conveert into an integer and append it in the list
    choice=input("Enter number or 'q' to quit: ")
    # the loop will break if user types q
    if choice=="q":
        break

    # error handling of user's input
    else:
        #considering the user can type an invalid input such as a different alphabet other than q or any non integer number or anything gibberish such as "seyuyuytrtyhj"
        #this if statement will give the user another chance
        if not choice.isdigit():
            # here i am using a built in function for strings isdigit() which is used to check if the string is a digit or not(letters)
            # if the user input is NOT a digit then it will display a message that it is an invalid input
            print("Invalid input")
            continue

        # the following instructions are to be followed if the user wrote the correct input if the string is a digit
        # then the digit will be converted from string to integer
        user_number=int(choice)
        #after converting it into an integer it wil be appended in the user's list to be later on multiplied with the other elements to get the list product answer
        user_list.append(user_number)
# END OF WHILE LOOP

#printing the answer by calling function
print("\nList:",user_list,"\nProduct:", multiply_list())