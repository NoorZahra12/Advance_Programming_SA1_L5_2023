# The program should display the following calculator menu:

# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
# 5. Modulus

# The program will prompt the user to choose the operation choice (from 1 to 5). 
# Then it asks the user to input values for the calculation. The program outputs the results of the calculation. 
# The program should end by asking if the user would like to perform another calculation or not.
################################################################################################################################################################################




########################################################################################
#########################  making 5 self defined functions  ############################
########################################################################################
# Note: 1. In addition and multiplication function the user can type as may input as user wants
# 2. In the subtraction function user will type one number and then whatever number user types after 
# that, the function will subtract those numbers with the first number
# 3. In multiplication and division function only 2 inuts will be taken from the user

################################## making a function called add for sum #############################
# user can will be asked 2 numbers and then user has to option to add as many numbers as user wants
def add():
    # storing the first number inside a variable called a
    a=float(input("Enter first number: "))
    # storing the second number inside a variable called b
    b=float(input("Enter first number: "))
    # adding the two numbers and storing the new number inside a variable called ans
    ans= a+b
    #printing ans variable's value
    print(ans)
    #letting the user add as many numbers as they want
    while True:
        #asking the user a question and taking user input to store that inside this variable
        user_choice=input("\nDo you want to add the answer with more number? (y/n): ")
        #based on what the user wrote
        # asking user if they want to type any additional input. then the following insructions will be executed
        # if user types "y" to type another number
        if user_choice == "y":
            # asking user input
            number=float(input("Enter number: "))
            # doing the calculation and storing it inside a variable
            ans+=number
            print("Here is your answer: ",ans)
  
        # If user wants to stop calculation and break the loop
        elif user_choice == 'n':
            # showing the answer and then repeating the while loop in case user wants to type another input
            print("Here is your answer: ",ans)
            break
        #if user types anything other than y or n it displays this message
        else:
            print("Invalid entry, try again")


################################ making a subtract function for subtraction ################################
#user will be asked 2 numbers and the user can subtract the numbber(minuend) with as many number as user wants
def sub():
    # first number
    minuend = float(input("Enter the minuend: "))
    # second number which will be subtracted from the first number
    subtrahend = float(input("Enter the subtrahend: "))
    ans= minuend-subtrahend
    print("Here is your answer: ",ans)
    # while loop for addiion numbers
    while True:
        # asking user if they want to tpe any additional inputs
        user_choice=input("\nDo you want to subtract the answer with more subtrahends? (y/n): ")
        # if user types "y" to type another number
        if user_choice == "y":
            # asking user input
            number=float(input("Enter number: "))
            # doing the calculation and storing it inside a variable
            ans-=number
            # showing the answer and then repeating the while loop in case user wants to type another input
            print("Here is your answer: ",ans)
        # If user wants to stop calculation and break the loop
        elif user_choice == "n":
            print("Here is your answer: ",ans)
            break
        #if user types anything other than y or n it displays this message
        else:
            print("Invalid entry, try again")

######################## making a function for multiplication ######################################
# user can will be asked 2 numbers and then user has to option to multiply it with as many numbers as user wants
def mul():
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    prod=a*b
    print("Here is your answer: ",prod)
    # while loop for addiion numbers
    while True:
        # asking user if they want to tpe any additional inputs
        user_choice=input("\nDo you want to multiply the answer with more numbers? (y/n): ")
        # if user types "y" to type another number
        if user_choice == "y":
            # asking user input
            c=float(input("Enter number: "))
            # doing the calculation and storing it inside a variable
            prod*=c
            # showing the answer and then repeating the while loop in case user wants to type another input
            print("Here is your answer: ",prod)
        # If user wants to stop calculation and break the loop
        elif user_choice == "n":
            print("Here is your answer: ",prod)
            break
        #if user types anything other than y or n it displays this message
        else:
            print("Invalid entry, try again")

######################## making a function for multiplication ######################################
#user will be asked only two numbers
def div():
    #using fraction terms so user knows which number is being asked to type
    x=float(input("Enter Numerator: "))
    y=float(input("Enter Dominator: "))
    # calculating the answer inside a variable
    ans = x/y
    # returing the variable with the answer stored inside it
    return ans

################################ making a function for multiplication ######################################
#user will be asked only two numbers
def mod():
    #using division terms to display the remainder
    x=float(input("Enter Dividend: "))
    y=float(input("Enter Divisor: "))
    # calculating the answer inside a variable
    ans = x%y
    # returing the variable with the answer stored inside it
    return ans

##########################################################################
###################### end of making functions ###########################
##########################################################################



############################################################################################################################3#############################################


###########################################################################
############################### start of while loop #######################
###########################################################################

while True:
    # displaying the 5 operations for calculation
    operation_choice=input("\nSelect a number from the options given below:\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Modulus\nYour choice of operation: ")

    #there are 2 if statements in this loop

    ######### this first 'if else statement' is to check which nuumber the user typed to select an operation from the list ##################
    
    if operation_choice.isdigit():
        user_choice = int(operation_choice)
        # If the user types 1 for addition
        if user_choice == 1:
            add()

        # If the user types 2 for subtraction
        elif user_choice == 2:
            sub()

        # If the user types 3 for multiplication
        elif user_choice == 3:
            mul()

        # If the user types 4 for division
        elif user_choice == 4:
            print("Here is your result: ",div())

        # If the user types 5 for subtraction
        elif user_choice == 5:
            print("Here is your remainder: ",mod())
        else:
            print("\nWhoops! Invalid input. Please try again.")
            continue


    else:# Error handling: If the user types the wrong number or if user types string
        print("\nWhoops! Invalid input. Please try again.")
        #continue will skip the instructions written below this if else statement and start the loop again
        continue


    ######### this second 'if else statement' is to check if user wants to use the calculator again or stop ##################

    #asking user if he/she would like to do another calculation
    user_continue=input("\nwould you like to do another calculation?\nType 'n' if no: ")
    # if user types 'n' the loop will break with a thank you message
    if user_continue=="n":
        print("\nThank you for using this calculator")
        break

##############################################################################
############################### end of while loop ############################
##############################################################################