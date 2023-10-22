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


################################## making a function called add for sum #############################
# user can will be asked 2 numbers and then user has to option to add as many numbers as user wants
def add():
    a=float(input("Enter first number: "))
    b=float(input("Enter first number: "))
    ans= a+b
    print(ans)
    while True:
        user_choice=input("\nDo you want to add the answer with more number? (y/n): ")
        if user_choice == "y":
            number=float(input("Enter number: "))
            ans+=number
            print("Here is your answer: ",ans)
        elif user_choice == 'n':
            print("Here is your answer: ",ans)
            break
        #if user types anything other than y or n it displays this message
        else:
            print("Invalid entry, try again")


################################ making a subtract function for subtraction ################################
#user will be asked 2 numbers and the user can subtract the numbber(minuend) with as many number as user wants
def sub():
    minuend = float(input("Enter the minuend: "))
    subtrahend = float(input("Enter the subtrahend: "))
    ans= minuend-subtrahend
    print("Here is your answer: ",ans)
    while True:
        user_choice=input("\nDo you want to subtract the answer with more subtrahends? (y/n): ")
        if user_choice == "y":
            number=float(input("Enter number: "))
            ans-=number
            print("Here is your answer: ",ans)
        elif user_choice == "n":
            print("Here is your answer: ",ans)
            break
        #if user types anything other than y or n it displays this message
        else:
            print("Invalid entry, try again")

######################## making a function for multiplication ######################################
# user can will be asked 2 numbers and then user has to option to multiply it with as many numbers as user wants
def mul():
    table=float(input("Enter table number: "))
    count=float(input("Enter multiplying number: "))
    prod=table*count
    print("Here is your answer: ",prod)
    while True:
        user_choice=input("\nDo you want to subtract the answer with more subtrahends? (y/n): ")
        if user_choice == "y":
            number=float(input("Enter number: "))
            prod*=number
            print("Here is your answer: ",prod)
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
    ans = x/y
    return ans

################################ making a function for multiplication ######################################
#user will be asked only two numbers
def mod():
    #using division terms to display the remainder
    x=float(input("Enter Dividend: "))
    y=float(input("Enter Divisor: "))
    ans = x%y
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
    operation_choice=float(input("\nSelect a number from the options given below:\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Modulus\nYour choice of operation: "))
    print("\n")

    #there are 2 if statements in this loop

    ######### this first 'if else statement' is to check which nuumber the user typed to select an operation from the list ##################
    
    # If the user types 1 for addition
    if operation_choice==1:
        add()

    # If the user types 2 for subtraction
    elif operation_choice==2:
        sub()

    # If the user types 3 for multiplication
    elif operation_choice==3:
        mul()

    # If the user types 4 for division
    elif operation_choice==4:
        print("Here is your result: ",div())

    # If the user types 5 for subtraction
    elif operation_choice==5:
        print("Here is your remainder: ",mod())

    # Error handling: If the user types the wrong number
    else:
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