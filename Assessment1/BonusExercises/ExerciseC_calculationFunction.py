# The program should display the following calculator menu:

# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
# 5. Modulus

# The program will prompt the user to choose the operation choice (from 1 to 5). 
# Then it asks the user to input values for the calculation. The program outputs the results of the calculation. 
# The program should end by asking if the user would like to perform another calculation or not.

def add(x,y):
    ans= x+y
    return ans
def sub(x,y):
    ans= x-y
    return ans
def mul(x,y):
    ans= x*y
    return ans
def div(x,y):
    ans= x/y
    return ans
def mod(x,y):
    ans= x%y
    return ans

user_continue=input("Press 's' to start calculation: ")

while user_continue!="q":
    user_choice=float(input("\nSelect a number from the options given below:\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Modulus\nYour choice: "))
    if user_choice==1:
        user_a=float(input("\nEnter a number: "))
        user_b=float(input("Enter another number: "))
        print("Here is your result: ",add(user_a,user_b))
    elif user_choice==2:
        user_a=float(input("\nEnter a number: "))
        user_b=float(input("Enter another number: "))
        print("Here is your result: ",sub(user_a,user_b))
    elif user_choice==3:
        user_a=float(input("\nEnter a number: "))
        user_b=float(input("Enter another number: "))
        print("Here is your result: ",mul(user_a,user_b))
    elif user_choice==4:
        user_a=float(input("\nEnter a number: "))
        user_b=float(input("Enter another number: "))
        print("Here is your result: ",div(user_a,user_b))
    elif user_choice==5:
        user_a=float(input("\nEnter a number: "))
        user_b=float(input("Enter another number: "))
        print("Here is your result: ",mod(user_a,user_b))
    else:
        print("\nWhoops! looks like you entered the wrong number. Please try again.")

    user_continue=input("\nPress 'q' to quit or press anything if would you like to do another calculation: ")

print("\nThank you for using this 2 digit calculator")