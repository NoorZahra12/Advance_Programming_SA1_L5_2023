#  Exercise A: Multiplication Tables ☑️ 
# Write a program to print Multiplication table in following format from 1 to 10 tables
# Hint: Use nested loops
# Multiplication table of : 1
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# 1 x 5 = 5
# 1 x 6 = 6
# 1 x 7 = 7
# 1 x 8 = 8
# 1 x 9 = 9
# 1 x 10 = 10
# …
# Multiplication table of : 10
# 10 x 1 = 10
# 10 x 2 = 20
# 10 x 3 = 30
# 10 x 4 = 40
# 10 x 5 = 50
# 10 x 6 = 60
# 10 x 7 = 70
# 10 x 8 = 80
# 10 x 9 = 90
# 10 x 10 = 100





#this is the table number
table_num=1
#and this will be the number which will increase in each line of a table
count=1

#let's start with the number of table since i need to print only 10 tables
#so i will put the condition of the while loop to keep running while the table 
#less than or equal to 10 until the table number is increased to 10
while table_num<=10: #outer loop
    #here once it has fulfiled the else statement and the count reaches 10
    # the last line which is increasing the number to 11
    #once count is 11 it will reset the count number to one 
    #and increase the table number yo print the next table starting from 1
    #it will keep doing this until it reaches 11 and repeat the process until the outer loop is false
    if count==11:
        table_num+=1
        count=1
    #this is the default else statement if count is less than 11
    else:
        #print the message to let user know which table number is being printed
        print("\nMultiplication table of: ",table_num)

        #this inner loop will run until count reaches 10 and go back to the outer loop and loop from there until outer loop's condition is false
        while count<=10: #inner loop

            #in this the product variable, the table number is multiplied by a new number and printing the line
            product=table_num*count
            print(table_num,"x",count,"=",product)
            # increasing the count variable by one 
            #to multiply the table_num by a new number(the new number is count)
            count+=1