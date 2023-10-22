#Exercise 1: User Input Output ☑️ 
#Write code to prompt the user to input her/his name and age and print these details on the screen. Find the length of the name and also the age of the user after one year.
#The format of text should look like the sample output below.
#(Use title() function)
#Hello, user!
#What is your name?
#alpha
#What is your age?
#22
#It is good to meet you, Alpha S
#The length of your name is:
#5
#You will be 23 in a year.


#i will make 4 variables and one print line for this
#taking user input for name in a variable
user_name=input("Hello, user \nWhat is your name?\n")
#taking user inout for age in a variable
user_age=int(input("What is your age?\n"))
#increasing the user's age by 1 in variable
user_newAge=user_age + 1
#using the len() to count the length of string (not letters because it also counts the space)
username_length=len(user_name)

#after taking all the input i will display the message starting in new line
print("\nIt is good to meet you,", user_name.title(),
      "\nThe length od your name is:\n",username_length,
      "\nYou will be",user_newAge,"in a year")